import torch
import numpy as np
import torch.nn.functional as F
import pywt

# Precompute wavelet filters once
def get_wavelet_filters(wavelet_name='db1', device='cpu'):
    wavelet = pywt.Wavelet(wavelet_name)
    lo = torch.tensor(wavelet.dec_lo, device=device).flip(dims=(0,)).float().view(1,1,-1)
    hi = torch.tensor(wavelet.dec_hi, device=device).flip(dims=(0,)).float().view(1,1,-1)
    lo_rec = torch.tensor(wavelet.rec_lo, device=device).float().view(1,1,-1)
    hi_rec = torch.tensor(wavelet.rec_hi, device=device).float().view(1,1,-1)
    return lo, hi, lo_rec, hi_rec

# Then in your decomposition code, you do not rebuild them:
def decompose_1d(data, lo, hi):
    # data is shape (N, 1, L) for 1D
    out_lo = F.conv1d(data, lo, stride=2)
    out_hi = F.conv1d(data, hi, stride=2)
    return out_lo, out_hi

def recompose_1d(out_lo, out_hi, lo_rec, hi_rec):
    rec_lo = F.conv_transpose1d(out_lo, lo_rec, stride=2)
    rec_hi = F.conv_transpose1d(out_hi, hi_rec, stride=2)
    return rec_lo + rec_hi

def decompose_along_dim(x, dim, lo, hi):
    """
    Apply a 1D wavelet decomposition (with precomputed filters lo, hi)
    along a particular dimension `dim` of x. Returns (lo_out, hi_out)
    with the same shape as x except that the dimension `dim` is halved
    by stride=2.

    x can be of shape (N, C, D1, D2, ..., DN).
    lo, hi: PyTorch tensors of shape (1, 1, filter_length),
            typically from get_wavelet_filters(...).
    """
    # 1) Move `dim` to the last dimension via permutation
    total_dims = x.ndim  
    perm = list(range(total_dims))
    perm.append(perm.pop(dim))  # move `dim` to end

    x_perm = x.permute(*perm)   # shape (..., length)

    # 2) Flatten everything except the first two dims (N, C) so we can
    #    call decompose_1d on shape (N*C*extra, 1, length).
    shape_perm = x_perm.shape
    N, C = shape_perm[0], shape_perm[1]
    L = shape_perm[-1]
    
    # Product of any intermediate dims
    intermediate = shape_perm[2:-1]
    extra_size = 1
    for s in intermediate:
        extra_size *= s

    # Reshape => (N*C*extra_size, 1, L)
    x_reshaped = x_perm.reshape(N * C * extra_size, 1, L)

    # 3) Decompose using the precomputed filters
    lo_coeffs, hi_coeffs = decompose_1d(x_reshaped, lo, hi)
    # lo_coeffs, hi_coeffs: shape (N*C*extra_size, 1, L/2)

    # 4) Reshape back to (N, C, *intermediate, L/2)
    new_length = lo_coeffs.shape[-1]
    lo_perm = lo_coeffs.reshape(N, C, *intermediate, new_length)
    hi_perm = hi_coeffs.reshape(N, C, *intermediate, new_length)

    # 5) Invert the permutation so dimension `dim` returns to its original place
    inv_perm = [0]*total_dims
    for i, p in enumerate(perm):
        inv_perm[p] = i

    lo_final = lo_perm.permute(*inv_perm)
    hi_final = hi_perm.permute(*inv_perm)

    return lo_final, hi_final

def recompose_along_dim(lo, hi, dim, lo_rec, hi_rec):
    """
    Invert a one-level 1D wavelet decomposition (lo, hi) along dimension `dim`,
    matching `decompose_along_dim(x, dim, lo, hi)`.

    lo, hi: Tensors each with the same shape as x had after being halved along `dim`.
    dim:  The dimension along which we want to invert the wavelet transform.
    lo_rec, hi_rec: Precomputed reconstruction filters of shape (1,1,filter_length),
                    e.g. from get_wavelet_filters(...).

    Returns:
      A tensor of the same shape as the original x (before decomposition).
    """

    # 1) Move `dim` to the last dimension (just like we did in decompose_along_dim)
    total_dims = lo.ndim
    perm = list(range(total_dims))
    perm.append(perm.pop(dim))  # move `dim` to the end

    lo_perm = lo.permute(*perm)  # shape (..., length//2)
    hi_perm = hi.permute(*perm)  # shape (..., length//2)

    # For example, shape_perm might be (N, C, ..., length//2)
    shape_perm = lo_perm.shape  
    N, C = shape_perm[0], shape_perm[1]
    length_half = shape_perm[-1]

    # 2) Flatten all other dims so we do a 1D inverse transform:
    #    shape => (N*C*extra_size, 1, length_half)
    intermediate = shape_perm[2:-1]  # dims between C and the last dimension
    extra_size = 1
    for s in intermediate:
        extra_size *= s

    lo_reshaped = lo_perm.reshape(N*C*extra_size, 1, length_half)
    hi_reshaped = hi_perm.reshape(N*C*extra_size, 1, length_half)

    # 3) Inverse 1D wavelet transform with conv_transpose1d
    rec_lo = F.conv_transpose1d(lo_reshaped, lo_rec, stride=2)
    rec_hi = F.conv_transpose1d(hi_reshaped, hi_rec, stride=2)

    # 4) Sum partial reconstructions (lo + hi)
    rec_reshaped = rec_lo + rec_hi  # shape => (N*C*extra_size, 1, length_full)

    # 5) Reshape back to (N, C, *intermediate, length_full)
    length_full = rec_reshaped.shape[-1]
    rec_perm = rec_reshaped.reshape(N, C, *intermediate, length_full)

    # 6) Invert the permutation so dimension `dim` goes back to its original place
    inv_perm = [0]*total_dims
    for i, p in enumerate(perm):
        inv_perm[p] = i
    rec_final = rec_perm.permute(*inv_perm)

    return rec_final

def decompose_nd(x, dims=None, lo=None, hi=None):
    """
    Perform a single-level, full N-D wavelet decomposition on tensor x
    using separable 1D wavelet transforms along each dimension in `dims`.

    - x:  Input tensor (N, C, D1, D2, ...)
    - dims: List of dimensions along which to decompose, e.g. [2, 3, 4]
      (Default: all spatial dims beyond N, C)
    - lo, hi: Precomputed decomposition filters (1,1,filter_length) from get_wavelet_filters()

    Returns:
      A list of 2^len(dims) sub-bands (lo/hi combos).
    """
    if dims is None:
        # By default, transform all dims except (batch, channel).
        dims = list(range(2, x.ndim))
    if lo is None or hi is None:
        raise ValueError("You must supply precomputed wavelet filters (lo, hi).")

    # Start with a single sub-band: the entire tensor.
    current_subbands = [x]

    for d in dims:
        new_subbands = []
        # Decompose each existing sub-band along dimension d
        for sb in current_subbands:
            lo_sb, hi_sb = decompose_along_dim(sb, d, lo, hi)
            new_subbands.append(lo_sb)
            new_subbands.append(hi_sb)
        current_subbands = new_subbands

    # After going through all dims, we have 2^len(dims) sub-bands
    return current_subbands

def recompose_nd(subbands, dims=None, lo_rec=None, hi_rec=None):
    """
    Invert a single-level ND wavelet transform.
    `subbands` is a list of 2^len(dims) sub-bands (from decompose_nd).
    - dims: same dims used in decompose_nd
    - lo_rec, hi_rec: Precomputed reconstruction filters from get_wavelet_filters()

    Returns:
      A single tensor of the original shape.
    """
    if not subbands:
        raise ValueError("subbands list is empty.")
    if dims is None:
        # default: guess dims from the shape
        dims = list(range(2, subbands[0].ndim))
    if lo_rec is None or hi_rec is None:
        raise ValueError("You must supply precomputed reconstruction filters (lo_rec, hi_rec).")

    current_subbands = subbands  # list of Tensors
    # number of subbands = 2^len(dims)

    # We recompose in reverse order of dims
    for d in reversed(dims):
        new_subbands = []
        # We'll group subbands in pairs: (lo_sb, hi_sb)
        for i in range(0, len(current_subbands), 2):
            lo_sb = current_subbands[i]
            hi_sb = current_subbands[i+1]
            # Recompose along dimension d
            new_sb = recompose_along_dim(lo_sb, hi_sb, d, lo_rec, hi_rec)
            new_subbands.append(new_sb)
        current_subbands = new_subbands

    # In the end, we have a single sub-band => the original volume
    return current_subbands[0]

def wavelet_packet_decompose_nd_to_leaves(
    x, dims=None, lo=None, hi=None, level=0, max_level=1, leaves=None
):
    """
    Recursively decompose ALL sub-bands at each level (wavelet packet),
    storing only the final sub-bands (leaves at level == max_level) in `leaves`.

    Args:
      x:         The input tensor (N, C, ...).
      dims:      Which dimensions to decompose (default: [2..ndim-1]).
      lo, hi:    Precomputed decomposition filters from get_wavelet_filters(...).
      level:     Current recursion depth (start at 0).
      max_level: Number of levels to decompose.
      leaves:    Accumulator list for final sub-bands.

    Returns:
      A list of final sub-bands (leaves), each sub-band is a PyTorch tensor.
    """
    if leaves is None:
        leaves = []
    if dims is None:
        dims = list(range(2, x.ndim))
    if lo is None or hi is None:
        raise ValueError("Must provide precomputed filters lo, hi for decomposition.")

    # Base case: if we've reached max_level, store x as a 'leaf'
    if level >= max_level:
        leaves.append(x)
        return leaves

    # 1) Decompose current x by one level across all dims
    subbands = decompose_nd(x, dims=dims, lo=lo, hi=hi)
    # subbands is a list of 2^len(dims)

    # 2) For a wavelet *packet*, we recursively decompose *every* sub-band
    next_level = level + 1
    for sb in subbands:
        wavelet_packet_decompose_nd_to_leaves(
            sb, dims=dims, lo=lo, hi=hi,
            level=next_level, max_level=max_level, leaves=leaves
        )

    return leaves

def wavepack_dec(x, dims=None, lo=None, hi=None, max_level=1):
    """
    Perform a full wavelet-packet decomposition up to `max_level`,
    returning a single tensor with final sub-bands concatenated along channel dim.

    Args:
      x:          The input tensor (N, C, ...).
      dims:       Which dimensions to decompose (default: [2..ndim-1]).
      lo, hi:     Precomputed decomposition filters from get_wavelet_filters(...).
      max_level:  How many levels of wavelet-packet decomposition.

    Returns:
      A single PyTorch tensor `stacked`: shape (N, C*num_leaves, ...) if
      all leaves share the same spatial shape.  (No explicit `num_leaves`
      return here, but you can always compute 2^(len(dims)*max_level)
      or check stacked.shape[1]/C.)
    """
    # Gather final leaves
    leaves = wavelet_packet_decompose_nd_to_leaves(
        x, dims=dims, lo=lo, hi=hi, level=0, max_level=max_level
    )
    # Example: for 2D, each level doubles each dimension => at level=2 => 4^2=16 leaves

    # Concatenate along channel dimension (dim=1),
    # shape => (N, C * num_leaves, H_final, W_final, ...)
    stacked = torch.cat(leaves, dim=1)
    return stacked

def wavelet_packet_recompose_nd_from_leaves(
    leaves, dims=None, lo_rec=None, hi_rec=None, level=0, max_level=1
):
    """
    Invert a wavelet-packet decomposition from a list of final sub-bands `leaves`.

    The recursion pattern is:
      - If level == max_level, pop exactly 1 leaf from the front => returned as a node.
      - Otherwise, gather 2^len(dims) children, recompose them into one sub-band,
        then bubble up.

    Args:
      leaves:   A list of final sub-band Tensors (the 'leaves').
      dims:     Which dims were decomposed (default: tries [2..ndim-1] if None).
      lo_rec, hi_rec: Precomputed reconstruction filters (1,1,kernel_length).
      level:    Current recursion depth.
      max_level:Max depth of packet decomposition.

    Returns:
      A single reconstructed PyTorch tensor at this node.
    """
    if not leaves:
        raise ValueError("Leaves list is empty; nothing to recompose.")
    if dims is None:
        # guess from the last leaf shape (or any leaf shape)
        dims = list(range(2, leaves[-1].ndim))
    if lo_rec is None or hi_rec is None:
        raise ValueError("Must provide precomputed reconstruction filters lo_rec, hi_rec.")

    # Base case: if we've reached max_level, pop one leaf
    if level >= max_level:
        return leaves.pop(0)

    # Otherwise, gather 2^len(dims) children
    n_children = 2 ** len(dims)
    children = []
    next_level = level + 1
    for _ in range(n_children):
        child = wavelet_packet_recompose_nd_from_leaves(
            leaves, dims=dims, lo_rec=lo_rec, hi_rec=hi_rec,
            level=next_level, max_level=max_level
        )
        children.append(child)

    # Recompose those children with recompose_nd
    x_rec = recompose_nd(children, dims=dims, lo_rec=lo_rec, hi_rec=hi_rec)
    return x_rec

def wavepack_rec(
    x_stacked, dims=None, lo_rec=None, hi_rec=None, max_level=1, original_channels=1
):
    """
    Invert wavelet_packet_decompose_nd_stacked.

    - x_stacked: shape (N, C*num_leaves, H', W', ...).
    - dims: which dims were transformed.
    - lo_rec, hi_rec: precomputed reconstruction filters.
    - max_level: how many levels of wavelet-packet were done.
    - original_channels: how many channels the original data had.

    Returns:
      A single tensor with shape (N, original_channels, H, W, ...)
      matching the original data shape.
    """
    # Number of final leaves for wavelet-packet:
    # In ND, each level => 2^(len(dims)) expansions. Over max_level => 2^(len(dims)*max_level).
    num_leaves = 2 ** ((len(x_stacked.shape) - 2) * max_level)

    # x_stacked is (N, C*num_leaves, ...)
    N = x_stacked.shape[0]
    bigC = x_stacked.shape[1]
    expected_C = original_channels * num_leaves
    if bigC != expected_C:
        raise ValueError(
            f"Channel mismatch: got {bigC}, expected {expected_C} "
            f"({original_channels} * {num_leaves})."
        )

    # Split into final sub-bands
    leaves_list = []
    chunk_size = original_channels
    for i in range(num_leaves):
        c_start = i * chunk_size
        c_end = (i + 1) * chunk_size
        leaf = x_stacked[:, c_start:c_end, ...]
        leaves_list.append(leaf)

    # Now recompose from leaves
    leaves_list_m = leaves_list[:]  # shallow copy so we can pop
    x_rec = wavelet_packet_recompose_nd_from_leaves(
        leaves_list_m, dims=dims, lo_rec=lo_rec, hi_rec=hi_rec,
        level=0, max_level=max_level
    )
    return x_rec