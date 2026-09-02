#!/usr/bin/env python3
"""
Date : 02/09/2026
Author : Avinash(deep0ctave)
Purpose : This is a ray-tracing project built from scratch to learn how it works. The project is built using Python and uses the Pygame library for rendering the final image. The project is inspired by the book "Ray Tracing in One Weekend" by Peter Shirley.
"""

import tqdm

def main():

    # Image Generation
    image_width = 256
    image_height = 256

    # Initialize a ppm file
    print("P3")
    print(f"{image_width} {image_height}")
    print("255")

    for y in tqdm.tqdm(range(0, image_height)):
        for x in range(0, image_width):
            r = x / (image_width - 1)
            g = y / (image_height - 1)
            b = 0

            print(f"{int(r * 255)} {int(g * 255)} {int(b * 255)}")

if __name__ == "__main__":
    main()