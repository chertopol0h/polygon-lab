import numpy as np
from math import cos, sin


class AffineTransforms:
    @staticmethod
    def translate(polygon, dx, dy, translation_point=(0, 0)):
        """Смещение полигона на dx, dy относительно заданной точки"""
        translation_matrix = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

        transformed_polygon = []
        for x, y in polygon:
            point = np.array([x - translation_point[0], y - translation_point[1], 1])
            new_point = translation_matrix @ point
            transformed_polygon.append(
                (new_point[0] + translation_point[0], new_point[1] + translation_point[1])
            )

        return transformed_polygon

    @staticmethod
    def rotate(polygon, angle, rotation_point):
        """Поворот полигона на заданный угол относительно заданной точки"""
        rotation_matrix = np.array(
            [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]]
        )

        transformed_polygon = []
        for x, y in polygon:
            translated_point = np.array([x - rotation_point[0], y - rotation_point[1], 1])
            rotated_point = rotation_matrix @ translated_point
            transformed_polygon.append(
                (rotated_point[0] + rotation_point[0], rotated_point[1] + rotation_point[1])
            )

        return transformed_polygon

    @staticmethod
    def scale(polygon, scale_factor, scaling_point):
        """Масштабирование полигона на заданный коэффициент относительно заданной точки"""
        scaling_matrix = np.array(
            [[scale_factor, 0, 0], [0, scale_factor, 0], [0, 0, 1]]
        )

        transformed_polygon = []
        for x, y in polygon:
            translated_point = np.array([x - scaling_point[0], y - scaling_point[1], 1])
            scaled_point = scaling_matrix @ translated_point
            transformed_polygon.append(
                (scaled_point[0] + scaling_point[0], scaled_point[1] + scaling_point[1])
            )

        return transformed_polygon