import random
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TreeNode:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

class RangeTree2D:
    def __init__(self, points):
        self.root = self.build(points, depth=0)

    def build(self, points, depth):
        if not points:
            return None

        axis = depth % 2
        points.sort(key=lambda point: getattr(point, 'x' if axis == 0 else 'y'))
        median = len(points) // 2

        root = TreeNode(points[median])
        root.left = self.build(points[:median], depth + 1)
        root.right = self.build(points[median + 1:], depth + 1)
        return root

def find_range(root, x_min, x_max, y_min, y_max):
    results = []

    def search_recursive(node):
        if node is None:
            return

        if x_min <= node.point.x <= x_max and y_min <= node.point.y <= y_max:
            results.append(node.point)

        if node.left:
            search_recursive(node.left)

        if node.right:
            search_recursive(node.right)

    search_recursive(root)
    return results

def generate_random_points(num_points, x_min, x_max, y_min, y_max):
    points = []
    for _ in range(num_points):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        points.append(Point(x, y))
    return points

def show_points(points, range_points, x_min, x_max, y_min, y_max):
    x_coords = [point.x for point in points]
    y_coords = [point.y for point in points]

    x_coords_r = [point.x for point in range_points]
    y_coords_r = [point.y for point in range_points]


    plt.scatter(x_coords, y_coords, color='red')
    plt.scatter(x_coords_r, y_coords_r, color='yellow')

    # Draw range lines
    plt.axvline(x=x_min, color='k', linestyle='-')
    plt.axvline(x=x_max, color='k', linestyle='-')
    plt.axhline(y=y_min, color='k', linestyle='-')
    plt.axhline(y=y_max, color='k', linestyle='-')

    plt.grid(True)
    plt.axis("equal")


def print_2d_util(node, x, y, dx, dy):
    if node is None:
        return

    plt.scatter(x, y, color='black')
    plt.text(x, y, f"({node.point.x:.2f}, {node.point.y:.2f})", ha='center', va='center')

    if node.left:
        plt.plot([x, x - dx], [y, y - dy], 'k-')
        print_2d_util(node.left, x - dx, y - dy, dx / 2, dy / 2)
    if node.right:
        plt.plot([x, x + dx], [y, y - dy], 'k-')
        print_2d_util(node.right, x + dx, y - dy, dx / 2, dy / 2)

def print_2d(root):
    plt.figure(figsize=(5, 5))
    print_2d_util(root, 0, 0, 10, 10)
    plt.axis('off')


# Generowanie losowych punktów
num_points = 15
x_min, x_max = -10, 10
y_min, y_max = -10, 10
random_points = generate_random_points(num_points, x_min, x_max, y_min, y_max)

kd_tree = RangeTree2D(random_points)

choose_x_min = -3
choose_x_max = 4
choose_y_min = -5
choose_y_max = 6
points_in_range = find_range(kd_tree.root, choose_x_min, choose_x_max, choose_y_min, choose_y_max)

print("Punkty pomiędzy x: ", choose_x_min, ",", choose_x_max, "| y: ", choose_y_min, ",", choose_y_max, "  to: ")
for point in points_in_range:
    print(f"({point.x:.2f}, {point.y:.2f})")

show_points(random_points, points_in_range, choose_x_min, choose_x_max, choose_y_min, choose_y_max)
print_2d(kd_tree.root)
plt.show()