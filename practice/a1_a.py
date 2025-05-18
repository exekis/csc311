import matplotlib.pyplot as plt

# Generate 101 points from 0.0 to 1.0, spaced by 0.01
print("count = " + str(100 * 0.02))
x = [round(i * 0.02, 2) for i in range(101)]
y = [0] * len(x)  # y-values are all 0 (so it's a horizontal row of points)

# Plot the points
plt.scatter(x, y, c='blue', s=10)  # small blue dots
plt.title("Points from 0.0 to 1.0 (step 0.01)")
plt.xlabel("x")
plt.yticks([])  # remove y-axis ticks for cleaner view
plt.grid(True)
plt.show()