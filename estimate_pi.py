import argparse
import numpy as np


def estimate_pi(num_points: int, seed: int = None):
    """
    Estimate the value of Pi using the Monte Carlo method.

    Args:
        num_points : The number of random points to generate.
        seed : An optional random seed for reproducibility.
    """
    # 1. Use the seed if it's provided
    if seed is not None:
        np.random.seed(seed)

    # Generate random points between -1 and 1 for both x and y axes.
    # This creates points within a 2x2 square centered at (0, 0).
    x_coords = np.random.uniform(-1, 1, num_points)
    y_coords = np.random.uniform(-1, 1, num_points)

    # Calculate the distance of each point from the origin (0, 0).
    # The formula for a circle is x^2 + y^2 = r^2.
    # Our circle has radius r = 1, so we check if x^2 + y^2 <= 1.
    distances = x_coords**2 + y_coords**2
    points_inside_circle = np.sum(distances <= 1)

    # The ratio of areas is (pi * r^2) / (2r)^2 = pi / 4.
    # This ratio should be approximately equal to the ratio of points.
    # (points_inside_circle / num_points) ~= pi / 4
    pi_estimate = 4 * points_inside_circle / num_points

    print(f"Number of points: {num_points}")
    print(f"Points inside circle: {points_inside_circle}")
    print(f"Estimated value of Pi: {pi_estimate}")
    print(f"Seed used: {seed}")

    # This is a standard practice to make script reusable


def main():
    """Main function to parse arguments and run the estimation"""
    # 2. Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Estimate Pi using Monte Carlo simulation"
    )
    parser.add_argument(
        "--num-points",
        type=int,
        default=100000,
        help="Number of random points to generate",
    )
    parser.add_argument(
        "--seed", type=int, default=None, help="Random seed for reproducibility"
    )
    args = parser.parse_args()

    # 3. Call our function with the parsed arguments
    estimate_pi(num_points=args.num_points, seed=args.seed)


if __name__ == "__main__":
    main()
