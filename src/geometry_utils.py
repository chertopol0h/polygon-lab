class GeometryUtils:
    @staticmethod
    def get_polygon_center(polygon):
        """Нахождение центра полигона"""
        x_coords = [x for x, y in polygon]
        y_coords = [y for x, y in polygon]
        return sum(x_coords) / len(x_coords), sum(y_coords) / len(y_coords)

    @staticmethod
    def is_point_inside_polygon(point, polygon):
        """Проверка принадлежности точки полигону (алгоритм ray casting)"""
        x, y = point
        n = len(polygon)
        inside = False
        px, py = polygon[0]
        for i in range(n + 1):
            cx, cy = polygon[i % n]
            if y > min(py, cy):
                if y <= max(py, cy):
                    if x <= max(px, cx):
                        if py != cy:
                            xinters = (y - py) * (cx - px) / (cy - py) + px
                        if px == cx or x <= xinters:
                            inside = not inside
            px, py = cx, cy
        return inside

    @staticmethod
    def get_point_position_relative_to_line(px, py, x1, y1, x2, y2):
        """Определение положения точки относительно прямой"""
        determinant = (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)
        if determinant < 0:
            return "Слева"
        elif determinant > 0:
            return "Справа"
        else:
            return "На линии"

    @staticmethod
    def get_intersection_point(p1, p2, p3, p4):
        """Нахождение точки пересечения двух отрезков p1p2 и p3p4, если она существует"""
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denominator == 0:
            return None  # Отрезки параллельны

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator

        # Проверяем, лежат ли параметры t и u в диапазоне от 0 до 1 (отрезки пересекаются в пределах их длины)
        if 0 <= t <= 1 and 0 <= u <= 1:
            # Вычисляем точку пересечения
            ix = x1 + t * (x2 - x1)
            iy = y1 + t * (y2 - y1)
            return ix, iy

        return None