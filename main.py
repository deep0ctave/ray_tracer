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
import random

def random_unit_vector():
    # Rejection sampling: pick random points in a cube until one lands inside
    # the unit sphere, then normalize it to get a uniformly random direction.
    while True:
        p = Vector(
            random.uniform(-1, 1),
            random.uniform(-1, 1),
            random.uniform(-1, 1),
        )
        length_squared = p.dot(p)
        # avoid picking a near-zero vector (normalize would blow up / lose precision)
        if 1e-160 < length_squared <= 1:
            return p.normalize()

def random_on_hemisphere(normal):
    on_unit_sphere = random_unit_vector()
    if on_unit_sphere.dot(normal) > 0.0:
        return on_unit_sphere
    else:
        return on_unit_sphere * -1.0

def is_sphere_hit(center, radius, ray, t_min, t_max):
    oc = ray.origin - center
    a = ray.direction.dot(ray.direction)
    b = 2.0 * oc.dot(ray.direction)
    c = oc.dot(oc) - radius * radius
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return -1
    sqrt_d = discriminant ** 0.5
    root = (-b - sqrt_d) / (2 * a)
    if root <= t_min or root >= t_max:
        root = (-b + sqrt_d) / (2 * a)
        if root <= t_min or root >= t_max:
            return -1
    return root

def ray_color(ray, sphere_center, sphere_radius, depth):
    if depth <= 0:
        return Color(0.0, 0.0, 0.0)  # no more light gathered past bounce limit

    # t_min = 0.001, NOT 0 - prevents "shadow acne" from the bounced ray
    # re-hitting the same surface point due to floating point rounding
    t = is_sphere_hit(sphere_center, sphere_radius, ray, 0.001, float("inf"))

    if t > 0:
        point_hit = ray.at(t)
        normal = (point_hit - sphere_center).normalize()

        bounce_direction = random_on_hemisphere(normal)
        bounce_ray = Ray(point_hit, bounce_direction)

        # each bounce absorbs 50% of light (diffuse reflectance)
        bounced_color = ray_color(bounce_ray, sphere_center, sphere_radius, depth - 1)
        return Color(
            0.5 * bounced_color.x,
            0.5 * bounced_color.y,
            0.5 * bounced_color.z,
        )

    # background: simple sky gradient based on ray's y direction
    unit_direction = ray.direction.normalize()
    a = 0.5 * (unit_direction.y + 1.0)
    return Color(
        (1.0 - a) * 1.0 + a * 0.5,
        (1.0 - a) * 1.0 + a * 0.7,
        (1.0 - a) * 1.0 + a * 1.0,
    )

def main():

    # Image Generation
    aspect_ratio = 16 / 9
    image_width = 512
    image_height = int(image_width / aspect_ratio)
    image_height = image_height if image_height > 0 else 1

    samples_per_pixel = 20
    max_depth = 10  # max number of bounces per ray

    # Camera Properties
    focal_length = 8.0
    viewport_height = 2.0
    viewport_width = (image_width / image_height) * viewport_height
    camera_origin = Vector(0, 0, 5)

    # Viewport vectors
    horizontal = Vector(viewport_width, 0, 0)
    vertical = Vector(0, -viewport_height, 0)

    pixel_delta_x = horizontal / (image_width - 1)
    pixel_delta_y = vertical / (image_height - 1)

    viewport_top_left = camera_origin - horizontal / 2 - vertical / 2 - Vector(0, 0, focal_length)
    pixel00 = viewport_top_left + pixel_delta_x * 0.5 + pixel_delta_y * 0.5

    print("P3")
    print(f"{image_width} {image_height}")
    print("255")

    sphere_center = Vector(0, 0, -5)
    sphere_radius = 1.0

    for y in tqdm.tqdm(range(0, image_height)):
        for x in range(0, image_width):
            accumulated = Color(0, 0, 0)

            for _ in range(samples_per_pixel):
                offset_x = x + random.random()
                offset_y = y + random.random()
                pixel = pixel00 + pixel_delta_x * offset_x + pixel_delta_y * offset_y
                ray_direction = pixel - camera_origin
                ray = Ray(camera_origin, ray_direction)

                sample_color = ray_color(ray, sphere_center, sphere_radius, max_depth)

                accumulated = Color(
                    accumulated.x + sample_color.x,
                    accumulated.y + sample_color.y,
                    accumulated.z + sample_color.z,
                )

            final_color = Color(
                accumulated.x / samples_per_pixel,
                accumulated.y / samples_per_pixel,
                accumulated.z / samples_per_pixel,
            )
            print(final_color.write_color())


if __name__ == "__main__":
    main()