#!/usr/bin/env python3
"""
Date : 02/09/2026
Author : Avinash(deep0ctave)
Purpose : This is a ray-tracing project built from scratch to learn how it works. The project is built using Python. The project is inspired by the book "Ray Tracing in One Weekend" by Peter Shirley.
"""

import tqdm
from color import Color
from ray import Ray
from vector import Vector

def main():

    # Image Generation
    aspect_ratio = 16 / 9
    image_width = 256
    image_height = int(image_width / aspect_ratio)
    image_height = image_height if image_height > 0 else 1

    # Camera Properties
    focal_length = 2.0
    viewport_height = 2.0
    viewport_width = (image_width / image_height) * viewport_height
    camera_origin = Vector(0, 0, 5)

    # Viewport vectors
    horizontal = Vector(viewport_width, 0, 0)
    vertical = Vector(0, -viewport_height, 0)

    # Calculating pixel density
    pixel_delta_x = horizontal / (image_width - 1)
    pixel_delta_y = vertical / (image_height - 1)

    # Top-left corner of the viewport
    viewport_top_left = camera_origin - horizontal / 2 - vertical / 2 - Vector(0, 0, focal_length)
    pixel00 = viewport_top_left + pixel_delta_x * 0.5 + pixel_delta_y * 0.5

    # Initialize a ppm file
    print("P3")
    print(f"{image_width} {image_height}")
    print("255")

    def is_sphere_hit(center, radius, ray):
        oc = ray.origin - center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - radius * radius
        discriminant = b * b - 4 * a * c
        return discriminant > 0 
    
    for y in tqdm.tqdm(range(0, image_height)):
        for x in range(0, image_width):
            pixel = pixel00 + pixel_delta_x * x + pixel_delta_y * y
            ray_direction = pixel - camera_origin
            ray = Ray(camera_origin, ray_direction)
            ray_color = ray.direction.normalize()

            sphere_center = Vector(0, 0, -5)
            sphere_radius = 1.0

            if is_sphere_hit(sphere_center, sphere_radius, ray):
                ray_color = Color(1, 0, 0)  # Red color for the sphere
            else:
                ray_color = Color(0.0, 0.0, 0.0)  # Background color
            print(ray_color.write_color())


if __name__ == "__main__":
    main()