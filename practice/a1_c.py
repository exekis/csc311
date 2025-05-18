import matplotlib
import numpy

# define unit cube
def unit_cube():
    """
    Returns the vertices of a unit cube.
    """
    return numpy.array([[0, 0, 0],
                        [1, 0, 0],
                        [1, 1, 0],
                        [0, 1, 0],
                        [0, 0, 1],
                        [1, 0, 1],
                        [1, 1, 1],
                        [0, 1, 1]])

# sample a random point in the unit cube
def sample_point():
    """
    Returns a random point in the unit cube.
    """
    return numpy.random.rand(3)

# comute the distance between two points and calculate the Euclidean distance by hand with no sqrt given d as the dimension
def distance(point1: numpy.ndarray, point2: numpy.ndarray) -> numpy.float64:
    """
    Returns the Euclidean distance between two points.
    """
    return numpy.sum((point1 - point2) ** 2)

def one_dimensional_distance(point1: numpy.ndarray, point2: numpy.ndarray) -> numpy.float64:
    """
    Returns the Euclidean distance between two points in 1D.
    """
    return numpy.abs(point1 - point2)


possible_dimensions = [2 ** 0, 2 ** 1, 2 ** 2, 2 ** 3, 2 ** 4, 2 ** 5, 2 ** 6, 2 ** 8, 2 ** 9, 2 ** 10]

averages = []
stds = []

for dim in possible_dimensions:
    # sample 100 random points in the unit cube
    points = numpy.array([sample_point() for _ in range(100)])
    # compute the distance between ALL PAIRS of points
    distances = numpy.array([[distance(points[i], points[j]) for j in range(100)] for i in range(100)])
    # compute the AVERAGE distance between all pairs of points
    avg_distance = numpy.mean(distances)
    # compute the standard deviation of the distances
    std_distance = numpy.std(distances)
    # append the average and standard deviation to the lists
    averages.append(avg_distance)
    stds.append(std_distance)


import matplotlib.pyplot as plt

# plot the average distance and standard deviation as a function of the dimension
# plt.figure()
# plt.errorbar(possible_dimensions, averages, yerr=stds, fmt='o-', capsize=5)
# plt.xscale('log', base=2)
# plt.xlabel('Dimension')
# plt.ylabel('Average Squared Distance')
# plt.title('Mean Pairwise Distance vs Dimension')
# plt.grid(True, which='both', ls='--', lw=0.5)
# plt.show()

# plot the standard deviation of the distances as a function of the dimension
plt.figure()
plt.plot(possible_dimensions, stds, 's-', color='C1')
plt.xscale('log', base=2)
plt.xlabel('Dimension')
plt.ylabel('Standard Deviation of Squared Distance')
plt.title('Std Dev of Pairwise Distances vs Dimension')
plt.grid(True, which='both', ls='--', lw=0.5)
plt.show()



