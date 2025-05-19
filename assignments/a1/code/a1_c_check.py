import numpy as np
import matplotlib.pyplot as plt

def compute_pairwise_stats(num_points, dims):
    """
    For each d in dims:
      - Sample `num_points` points in [0,1]^d.
      - Compute pairwise squared-L2 and L1 distances via explicit loops.
      - Return lists of means and stds for each metric.
    """
    mean_sq = []
    std_sq  = []
    mean_l1 = []
    std_l1  = []

    for d in dims:
        # Sample points in ℝ^d
        points = np.random.rand(num_points, d)

        # Lists to accumulate distances
        sq_dists = []
        l1_dists = []

        # Compute distances for each unique pair (i < j)
        for i in range(num_points):
            for j in range(i + 1, num_points):
                diff = points[i] - points[j]
                sq = np.dot(diff, diff)          # squared Euclidean: sum(diff**2)
                l1 = np.sum(np.abs(diff))        # L1: sum(|diff|)
                sq_dists.append(sq)
                l1_dists.append(l1)

        # Convert to arrays and compute statistics
        sq_arr = np.array(sq_dists)
        l1_arr = np.array(l1_dists)

        mean_sq.append(sq_arr.mean())
        std_sq.append(sq_arr.std())
        mean_l1.append(l1_arr.mean())
        std_l1.append(l1_arr.std())

    return mean_sq, std_sq, mean_l1, std_l1

def plot_stats(dims, mean_sq, std_sq, mean_l1, std_l1):
    """
    Plot mean & std for squared-L2 and L1 distances vs. dimension on a log2 x-axis.
    """
    plt.figure(figsize=(8,5))
    plt.plot(dims, mean_sq, marker='o', label='mean $\\|\\cdot\\|_2^2$')
    plt.plot(dims, std_sq,   marker='s', label='std  $\\|\\cdot\\|_2^2$')
    plt.plot(dims, mean_l1,  marker='^', label='mean $\\|\\cdot\\|_1$')
    plt.plot(dims, std_l1,   marker='x', label='std  $\\|\\cdot\\|_1$')

    plt.xscale('log', base=2)
    plt.xlabel('Dimension $d$')
    plt.ylabel('Distance statistic')
    plt.title('Mean and Std of Pairwise Distances vs Dimension')
    plt.legend()
    plt.grid(which='both', ls='--', lw=0.5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    num_points = 100
    dims       = [2**i for i in range(11)]  # 1, 2, 4, ..., 1024

    mean_sq, std_sq, mean_l1, std_l1 = compute_pairwise_stats(num_points, dims)
    plot_stats(dims, mean_sq, std_sq, mean_l1, std_l1)

# Notes on readability:
# - We avoid `pts[:, None, :] - pts[None, :, :]`, which uses NumPy broadcasting
#   to build an (n,n,d) array of all differences in one shot.
# - We also avoid `np.triu_indices`, which finds the upper-triangle indices
#   (i<j) of that big matrix. Instead, we explicitly loop over i<j,
#   which is clearer for understanding exactly which pairs we're computing.

