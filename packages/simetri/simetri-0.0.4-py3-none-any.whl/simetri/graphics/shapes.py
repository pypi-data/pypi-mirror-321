"""Shapes module contains classes and functions for creating shapes."""

from math import pi, gcd, sin, cos, comb
from typing import List
import copy

from numpy import ndarray
import numpy as np

from ..graphics.batch import Batch

from ..graphics.shape import Shape, custom_attributes

from ..graphics.common import axis_x, get_defaults, Sequence, Point
from ..graphics.all_enums import Types
from ..settings.settings import defaults
from ..helpers.geometry import (
    side_len_to_radius,
    offset_polygon_points,
    distance,
    mid_point,
    close_points2,
)
import simetri.colors as colors

Color = colors.Color


class Ellipse(Shape):
    """An ellipse defined by center, width, and height."""

    def __init__(self, center: Point, width: float, height: float, **kwargs) -> None:
        x, y = center[:2]
        a = width / 2
        b = height / 2
        vertices = [(x, y), (x + a, y), (x, y + b), (x - a, y), (x, y - b)]
        super().__init__(vertices, closed=True, **kwargs)
        self.subtype = Types.ELLIPSE

    @property
    def center(self):
        """Return the center of the ellipse."""
        return self.vertices[0]

    @center.setter
    def center(self, new_center: Point):
        center = self.center
        x_diff = new_center[0] - center[0]
        y_diff = new_center[1] - center[1]
        for i in range(5):
            x, y = self.vertices[i]
            self[i] = (x + x_diff, y + y_diff)

    @property
    def width(self):
        """Return the width of the ellipse."""
        vertices = self.vertices
        return distance(vertices[0], vertices[1]) * 2

    @width.setter
    def width(self, new_width: float):
        center = self.center
        height = self.height
        vertices = []
        vertices.append(center)
        a = new_width / 2
        b = height / 2
        vertices.append((center[0] + a, center[1]))
        vertices.append((center[0], center[1] + b))
        vertices.append((center[0] - a, center[1]))
        vertices.append((center[0], center[1] - b))
        self[:] = vertices

    @property
    def height(self):
        """Return the height of the ellipse."""
        vertices = self.vertices
        return distance(vertices[0], vertices[2]) * 2

    @height.setter
    def height(self, new_height: float):
        center = self.center
        width = self.width
        vertices = []
        a = width / 2
        b = new_height / 2
        vertices.append(center)
        vertices.append((center[0] + a, center[1]))
        vertices.append((center[0], center[1] + b))
        vertices.append((center[0] - a, center[1]))
        vertices.append((center[0], center[1] - b))
        self[:] = vertices

    @property
    def closed(self):
        """Return True ellipse is always closed."""
        return True

    @closed.setter
    def closed(self, value: bool):
        pass

    def copy(self):
        """Return a copy of the ellipse."""
        center = self.center
        width = self.width
        height = self.height
        ellipse = Ellipse(center, width, height)
        # ellipse.style = self.style.copy()
        custom_attribs = custom_attributes(self)
        for attrib in custom_attribs:
            setattr(ellipse, attrib, getattr(self, attrib))

        return ellipse


class Rectangle(Shape):
    """A rectangle defined by width and height."""

    def __init__(self, center: Point, width: float, height: float, **kwargs) -> None:
        x, y = center
        half_width = width / 2
        half_height = height / 2
        vertices = [
            (x - half_width, y - half_height),
            (x + half_width, y - half_height),
            (x + half_width, y + half_height),
            (x - half_width, y + half_height),
        ]
        super().__init__(vertices, closed=True, **kwargs)
        self.subtype = Types.RECTANGLE

    @property
    def width(self):
        """Return the width of the rectangle."""
        return distance(self.vertices[0], self.vertices[1])

    @width.setter
    def width(self, new_width: float):
        center = self.center
        height = self.height
        self[0] = (center[0] - new_width / 2, center[1] - height / 2)
        self[1] = (center[0] + new_width / 2, center[1] - height / 2)
        self[2] = (center[0] + new_width / 2, center[1] + height / 2)
        self[3] = (center[0] - new_width / 2, center[1] + height / 2)

    @property
    def height(self):
        """Return the height of the rectangle."""
        return distance(self.vertices[1], self.vertices[2])

    @height.setter
    def height(self, new_height: float):
        center = self.center
        width = self.width
        self[0] = (center[0] - width / 2, center[1] - new_height / 2)
        self[1] = (center[0] + width / 2, center[1] - new_height / 2)
        self[2] = (center[0] + width / 2, center[1] + new_height / 2)
        self[3] = (center[0] - width / 2, center[1] + new_height / 2)

    @property
    def center(self):
        """Return the center of the rectangle."""
        return mid_point(self.vertices[0], self.vertices[2])

    @center.setter
    def center(self, new_center: Point):
        center = self.center
        x_diff = new_center[0] - center[0]
        y_diff = new_center[1] - center[1]
        for i in range(4):
            x, y = self.vertices[i]
            self[i] = (x + x_diff, y + y_diff)

    def copy(self):
        """Return a copy of the rectangle."""
        center = self.center
        width = self.width
        height = self.height
        rectangle = Rectangle(center, width, height)
        style = copy.deepcopy(self.style)
        rectangle.style = style
        rectangle._set_aliases()
        custom_attribs = custom_attributes(self)
        for attrib in custom_attribs:
            setattr(rectangle, attrib, getattr(self, attrib))

        return rectangle


class Rectangle2(Shape):
    """A rectangle defined by two opposite corners."""

    def __init__(self, corner1: Point, corner2: Point, **kwargs) -> None:
        x1, y1 = corner1
        x2, y2 = corner2
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        vertices = [(x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)]
        super().__init__(vertices, closed=True, **kwargs)
        self.subtype = Types.RECTANGLE

    @property
    def corner1(self):
        """Return the first corner of the rectangle."""
        return self.vertices[0]

    @corner1.setter
    def corner1(self, new_corner: Point):
        corner2 = self.corner2
        self[0] = new_corner
        self[3] = (new_corner[0], corner2[1])
        self[1] = (corner2[0], new_corner[1])

    @property
    def corner2(self):
        """Return the second corner of the rectangle."""
        return self.vertices[2]

    @corner2.setter
    def corner2(self, new_corner: Point):
        corner1 = self.corner1
        self[2] = new_corner
        self[1] = (new_corner[0], corner1[1])
        self[3] = (corner1[0], new_corner[1])

    @property
    def width(self):
        """Return the width of the rectangle."""
        return distance(self.vertices[0], self.vertices[1])

    @width.setter
    def width(self, new_width: float):
        corner1 = self.corner1
        corner2 = self.corner2
        self[1] = (corner1[0] + new_width, corner1[1])
        self[2] = (corner1[0] + new_width, corner2[1])

    @property
    def height(self):
        """Return the height of the rectangle."""
        return distance(self.vertices[1], self.vertices[2])

    @height.setter
    def height(self, new_height: float):
        corner1 = self.corner1
        corner2 = self.corner2
        self[2] = (corner2[0], corner1[1] + new_height)
        self[3] = (corner1[0], corner1[1] + new_height)

    def copy(self):
        """Return a copy of the rectangle."""
        corner1 = self.corner1
        corner2 = self.corner2
        rectangle = Rectangle(corner1, corner2)
        style = copy.deepcopy(self.style)
        rectangle.style = style
        rectangle._set_aliases()
        custom_attribs = custom_attributes(self)
        for attrib in custom_attribs:
            setattr(rectangle, attrib, getattr(self, attrib))

        return rectangle


class Circle(Shape):
    """A circle defined by a center point and a radius."""

    def __init__(
        self,
        center: Point = (0, 0),
        radius: float = None,
        xform_matrix: np.array = None,
        **kwargs,
    ) -> None:
        if radius is None:
            radius = defaults["circle_radius"]

        x, y = center[:2]
        p1 = (x + radius, y)
        p2 = (x, y + radius)
        p3 = (x - radius, y)
        p4 = (x, y - radius)
        points = [(x, y), p1, p2, p3, p4]
        super().__init__(points, xform_matrix=xform_matrix, **kwargs)
        self.subtype = Types.CIRCLE

    @property
    def closed(self):
        """Return True. Circles are closed."""
        return True

    @closed.setter
    def closed(self, value: bool):
        pass

    @property
    def center(self):
        """Return the center of the circle."""
        return self.vertices[0]

    @property
    def radius(self):
        """Return the radius of the circle."""
        return distance(self.vertices[0], self.vertices[1])

    @center.setter
    def center(self, new_center: Point):
        radius = self.radius
        self[0] = new_center
        self[1] = (new_center[0] + radius, new_center[1])
        self[2] = (new_center[0], new_center[1] + radius)
        self[3] = (new_center[0] - radius, new_center[1])
        self[4] = (new_center[0], new_center[1] - radius)

    @radius.setter
    def radius(self, new_radius: float):
        center = self.center
        self[1] = (center[0] + new_radius, center[1])
        self[2] = (center[0], center[1] + new_radius)
        self[3] = (center[0] - new_radius, center[1])
        self[4] = (center[0], center[1] - new_radius)

    def copy(self):
        """Return a copy of the circle."""
        center = self.center
        radius = self.radius
        circle = Circle(center=center, radius=radius)
        style = copy.deepcopy(self.style)
        circle.style = style
        circle._set_aliases()

        custom_attribs = custom_attributes(self)
        for attrib in custom_attribs:
            setattr(circle, attrib, getattr(self, attrib))

        return circle


class Segment(Shape):
    """A line segment defined by two points."""

    def __init__(self, start: Point, end: Point, **kwargs) -> None:
        dist_tol2 = defaults["dist_tol"] ** 2
        if close_points2(start, end, dist2=dist_tol2):
            raise ValueError("Segment: start and end points are the same!")
        points = [start, end]
        super().__init__(points, **kwargs)
        self.subtype = Types.SEGMENT

    @property
    def start(self):
        """Return the start point of the segment."""
        return self.vertices[0]

    @property
    def end(self):
        """Return the end point of the segment."""
        return self.vertices[1]

    @property
    def length(self):
        """Return the length of the segment."""
        return distance(self.start, self.end)

    def copy(self) -> Shape:
        """Return a copy of the segment."""
        return Segment(self.start, self.end, **self.kwargs)

    def __str__(self):
        return f"Segment({self.start}, {self.end})"

    def __repr__(self):
        return f"Segment({self.start}, {self.end})"

    def __eq__(self, other):
        return (
            other.type == Types.SEGMENT
            and self.start == other.start
            and self.end == other.end
        )


class Arc(Shape):
    def __init__(
        self,
        center: Point,
        radius: float,
        start_angle: float,
        end_angle: float,
        xform_matrix: ndarray = None,
        **kwargs,
    ):
        self.center = center
        self.radius = radius
        self.start_angle = start_angle
        self.end_angle = end_angle
        x, y = center
        x1 = x + radius * cos(start_angle)
        y1 = y + radius * sin(start_angle)
        x2 = x + radius * cos(end_angle)
        y2 = y + radius * sin(end_angle)
        self.start_point = x1, y1
        self.end_point = x2, y2
        self.primary_points = [(x, y), (x1, y1), (x2, y2)]
        self.xform_matrix = xform_matrix

        super().__init__(self.primary_points, subtype=Types.ARC, **kwargs)


class Mask(Shape):
    """
    A mask is a closed shape that is used to clip other shapes.
    All it has is points and a transformation matrix.
    """

    def __init__(self, points, reverse=False, xform_matrix=None):
        super().__init__(points, xform_matrix, subtype=Types.MASK, closed=True)
        self.reverse: bool = reverse
        # mask should be between \begin{scope} and \end{scope}
        # canvas, batch, and shapes can have scope


def ellipse_points(
    x: float, y: float, width: float, height: float, angle: float = 0, n: int = 30
) -> list[Point]:
    """
    Return a list of points that form an ellipse
       with the given parameters.
       n is the total number of points in the ellipse.
    """
    from .affine import rotate

    points = []
    for i in range(n):
        t = 2 * pi * i / n
        points.append([x + width / 2 * cos(t), y + height / 2 * sin(t)])

    if angle != 0:
        points = rotate(points, angle, (x, y))
    return points

def circle_points(x: float, y: float, radius: float, n: int = 30) -> list[Point]:
    """
    Return a list of points that form a circle
    with the given parameters.
    n is the total number of points in the circle.
    """
    return arc_points(x, y, radius, 0, 2 * pi, n=n)


def arc_points(
    x: float,
    y: float,
    radius: float,
    start_angle: float,
    end_angle: float,
    clockwise: bool = False,
    n: int = 20,
) -> list[Point]:
    """
    Return a list of points that form a circular arc with the given
    parameters. n is the total number of points in the arc.
    """
    points = []
    if clockwise:
        start_angle, end_angle = end_angle, start_angle
    step = (end_angle - start_angle) / n
    for i in np.arange(start_angle, end_angle + 1, step):
        points.append([x + radius * cos(i), y + radius * sin(i)])
    return points


def bezier_points(points: list[Point], n: int = 100) -> list[Point]:
    """
    points = [a, b, c, d] control points,
    n is the number of points to generate.
    Return a list of points representing the curve.
    """

    def bernstein(n, i, t):
        """Bernstein polynomial."""
        return comb(n, i) * t ** (n - i) * (1 - t) ** i

    n_points = len(points)
    x_array = np.array([p[0] for p in points])
    y_array = np.array([p[1] for p in points])
    t = np.linspace(0.0, 1.0, n)
    poly_array = np.array([bernstein(n_points - 1, i, t) for i in range(0, n_points)])
    x_values = np.dot(x_array, poly_array)
    y_values = np.dot(y_array, poly_array)

    return list(zip(x_values, y_values))


def hex_points(side_length: float) -> List[List[float]]:
    """
    Return a list of points that define a hexagon with a given side
    length.
    """
    points = []
    for i in range(6):
        x = side_length * cos(i * 2 * pi / 6)
        y = side_length * sin(i * 2 * pi / 6)
        points.append((x, y))
    return points


def rectangle_points(
    x: float, y: float, width: float, height: float, angle: float = 0
) -> Sequence[Point]:
    """Return a list of points that form a rectangle
    with the given parameters."""
    from affine import rotate

    points = []
    points.append([x - width / 2, y - height / 2])
    points.append([x + width / 2, y - height / 2])
    points.append([x + width / 2, y + height / 2])
    points.append([x - width / 2, y + height / 2])
    """_summary_

    Return:
        _type_: _description_
    """
    if angle != 0:
        points = rotate(points, angle, (x, y))
    return points


def reg_poly_points_side_length(pos: Point, n: int, side_len: float) -> Sequence[Point]:
    """
    Return a regular polygon points list with n sides, side_len length
    """
    rad = side_len_to_radius(n, side_len)
    angle = 2 * pi / n
    x, y = pos[:2]
    points = [[cos(angle * i) * rad + x, sin(angle * i) * rad + y] for i in range(n)]
    points.append(points[0])
    return points


def reg_poly_points(pos: Point, n: int, r: float) -> Sequence[Point]:
    """
    Return a regular polygon points list with n sides, side_len length
    """

    angle = 2 * pi / n
    x, y = pos[:2]
    points = [[cos(angle * i) * r + x, sin(angle * i) * r + y] for i in range(n)]
    points.append(points[0])
    return points


def di_star(points: Sequence[Point], n: int) -> Batch:
    """
    Dihedral star with n petals.
    n: Number of petals.
    points: List of [x, y] points
    return a Batch instance (dihedral star with n petals)
    """
    batch = Batch(Shape(points))
    return batch.mirror(axis_x, reps=1).rotate(2 * pi / n, reps=n - 1)


def hex_grid_centers(x, y, side_length, n_rows, n_cols):
    """Return a list of points that define the centers of hexagons in a grid."""
    centers = []
    for row in range(n_rows):
        for col in range(n_cols):
            x_ = col * 3 * side_length + x
            y_ = row * 2 * side_length + y
            if col % 2:
                y_ += side_length
            centers.append((x_, y_))

    centers = []
    # first row
    origin = Point(x, y)
    grid = Batch(Point)
    grid.transform()
    return centers


def rect_grid(x, y, cell_width, cell_height, n_rows, n_cols, pattern):
    width = cell_width * n_cols
    height = cell_height * n_rows
    horiz_line = line_shape((x, y), (x + width, y))
    horiz_lines = Batch(horiz_line)
    horiz_lines.translate(0, cell_height, reps=n_rows)
    vert_line = line_shape((x, y), (x, y + height))
    vert_lines = Batch(vert_line)
    vert_lines.translate(cell_width, 0, reps=n_cols)
    grid = Batch(horiz_lines, *vert_lines)
    for row in range(n_rows):
        for col in range(n_cols):
            if pattern[row][col]:
                x_, y_ = (col * cell_width + x, (n_rows - row - 1) * cell_height + y)
                points = [
                    (x_, y_),
                    (x_ + cell_width, y_),
                    (x_ + cell_width, y_ + cell_height),
                    (x_, y_ + cell_height),
                ]
                cell = Shape(points, closed=True, fill_color=colors.gray)
                grid.append(cell)
    return grid


def regular_star_polygon(n, step, rad):
    angle = 2 * pi / n
    points = [(cos(angle * i) * rad, sin(angle * i) * rad) for i in range(n)]
    if n % step:
        indices = [i % n for i in list(range(0, (n + 1) * step, step))]
    else:
        indices = [i % n for i in list(range(0, ((n // step) + 1) * step, step))]
    vertices = [points[ind] for ind in indices]
    return Batch(Shape(vertices)).rotate(angle, reps=gcd(n, step) - 1)


# These may have to be removed


def star_shape(points, reps=5, scale=1):
    """Return a dihedral star from a list of points"""
    shape = Shape(points, subtype=Types.STAR)
    batch = Batch(shape)
    batch.mirror(axis_x, reps=1)
    batch.rotate(2 * pi / (reps), reps=reps - 1)
    batch.scale(scale)
    return batch


def dot_shape(
    x,
    y,
    radius=1,
    fill_color=None,
    line_color=None,
    line_width=None,
):
    """Return a Shape object with a single point."""
    fill_color, line_color, line_width = get_defaults(
        ["fill_color", "line_color", "line_width"], [fill_color, line_color, line_width]
    )
    dot_shape = Shape(
        [(x, y)],
        closed=True,
        fill_color=fill_color,
        line_color=line_color,
        line_width=line_width,
        subtype=Types.D_o_t,
    )
    dot_shape.marker = radius
    return dot_shape


def rect_shape(
    x: float,
    y: float,
    width: float,
    height: float,
    fill_color: Color = colors.white,
    line_color: Color = defaults["line_color"],
    line_width: float = defaults["line_width"],
    fill: bool = True,
    marker: "Marker" = None,
) -> Shape:
    """Given lower left corner position, width, and height,
    return a Shape object with points that form a rectangle.
    subtype is Types.RECTANGLE
    """
    return Shape(
        [(x, y), (x + width, y), (x + width, y + height), (x, y + height)],
        closed=True,
        fill_color=fill_color,
        line_color=line_color,
        fill=fill,
        line_width=line_width,
        marker=marker,
        subtype=Types.RECTANGLE,
    )


def arc_shape(x, y, radius, start_angle, end_angle, clockwise=False, n=20):
    """Return a Shape object with points that form a circular arc
    with the given parameters.
    n is the number of points that will be used to approximate the arc."""
    points = arc_points(x, y, radius, start_angle, end_angle, clockwise=clockwise, n=n)
    return Shape(points, closed=False, subtype=Types.ARC)


def circle_shape(x, y, radius, n=30):
    """Return a list of points that form a circle
    with the given parameters.
    If the step is one then there is a point for each degree
    of the circle. If the step is 3 then there is a point for every
     three degrees."""
    circ = arc_shape(x, y, radius, 0, 2 * pi, n=n)
    circ.subtype = Types.CIRCLE
    return circ


def reg_poly_shape(pos, n, r=100, **kwargs):
    """Return a regular polygon"""
    x, y = pos[:2]
    points = reg_poly_points((x, y), n=n, r=r)
    return Shape(points, closed=True, **kwargs)


def ellipse_shape(x, y, width, height, n=30):
    """Return a list of points that form an ellipse
    with the given parameters.
    If the step is one then there is a point for each degree
    of the circle. If the step is 3 then there is a point for every
     three degrees."""
    points = ellipse_points(x, y, width, height, n=n)
    return Shape(points, subtype=Types.ELLIPSE)


def line_shape(p1, p2, line_width=1, line_color=colors.black, **kwargs):
    """Return a Shape object with two points p1, and p2
    This can represent a line from p1(x1, y1) to p2(x2, y2)"""
    x1, y1 = p1
    x2, y2 = p2
    return Shape(
        [(x1, y1), (x2, y2)],
        closed=False,
        line_color=line_color,
        line_width=line_width,
        subtype=Types.L_i_n_e,
        **kwargs,
    )


def offset_polygon_shape(
    polygon_shape, offset: float = 1, dist_tol: float = defaults["dist_tol"]
) -> list[Point]:
    """Return a copy of a polygon with offset edges.
    Negative offset values will create a smaller polygon.
    Polygon: [(x1, y1), (x2, y2), ...]
    return: [(x1, y1), (x2, y2), ...]
    """
    vertices = offset_polygon_points(polygon_shape.vertices, offset, dist_tol)

    return Shape(vertices)
