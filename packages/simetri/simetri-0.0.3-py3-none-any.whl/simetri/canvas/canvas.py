""" Canvas class for drawing shapes and text on a page. All drawing
operations are handled by the Canvas class. Canvas class can draw all
graphics objects and text objects. It also provides methods for
drawing basic shapes like lines, circles, and polygons.
"""

import os
import webbrowser
import subprocess
import logging
from typing import Optional, Any, Tuple, Sequence
from typing_extensions import Self
from pathlib import Path
from dataclasses import dataclass

from numpy import ndarray
import networkx as nx
import fitz

from ..graphics.affine import (
    rotation_matrix,
    translation_matrix,
    scale_matrix,
    identity_matrix,
)
from ..graphics.common import common_properties, _set_Nones, VOID, Point, Vec2
from ..graphics.all_enums import Types, Drawable, Result, Anchor
from ..settings.settings import defaults
from ..graphics.bbox import bounding_box
from ..graphics.batch import Batch
from ..graphics.shape import Shape
from ..colors import colors
from ..canvas import draw
from ..helpers.utilities import wait_for_file_availability
from ..tikz.tikz import Tex, get_tex_code
from ..helpers.validation import validate_args
from ..canvas.style_map import canvas_args
from ..notebook import display

Color = colors.Color


class Canvas:
    """Canvas class for drawing shapes and text on a page. All drawing
    operations are handled by the Canvas class. Canvas class can draw all
    graphics objects and text objects. It also provides methods for
    drawing basic shapes like lines, circles, and polygons.
    """

    def __init__(
        self,
        size: Vec2 = None,
        back_color: Optional[Color] = None,
        title: str = "",
        border=None,
        **kwargs,
    ):

        validate_args(kwargs, canvas_args)
        _set_Nones(self, ["back_color", "border"], [back_color, border])
        self.size = size
        self.title = title
        self.border = border
        self.type = Types.CANVAS
        self.subtype = Types.CANVAS
        self._code = []
        self._font_list = []
        self._pos = [0, 0]
        self._angle = 0
        self._scale = [1, 1]
        self.preamble = defaults["preamble"]
        self.back_color = back_color
        self.pages = [Page(self.size, self.back_color, self.border)]
        self.active_page = self.pages[0]
        self._all_vertices = []
        self.blend_mode = None
        self.blend_group = False
        self.transparency_group = False
        self.alpha = None
        self.line_alpha = None
        self.fill_alpha = None
        self.text_alpha = None
        self.clip = None  # if True then clip the canvas to the mask
        self.mask = None  # Mask object
        self.even_odd_rule = None  # True or False
        self.draw_grid = False
        common_properties(self)

        for k, v in kwargs.items():
            setattr(self, k, v)

        self._xform_matrix = identity_matrix()
        self.tex: Tex = Tex()
        self.render = defaults["render"]
        self.limits = None

    def __setattr__(self, name, value):
        if hasattr(self, "active_page") and name in ["back_color", "border", "size"]:
            self.active_page.__setattr__(name, value)
            self.__dict__[name] = value
        else:
            self.__dict__[name] = value

    def display(self) -> Self:
        """Show the canvas in a notebook cell."""
        display(self)

    def arc(
        self,
        center: Point,
        radius: float,
        start_angle: float,
        end_angle: float,
        **kwargs,
    ) -> Self:
        """Draw an arc with the given center, radius, start angle and end angle."""
        draw.arc(self, center, radius, start_angle, end_angle, **kwargs)
        return self

    def circle(self, center: Point, radius: float, **kwargs) -> Self:
        """Draw a circle with the given center and radius."""
        draw.circle(self, center, radius, **kwargs)
        return self

    def text(
        self,
        text: str,
        pos: Point,
        font_name: str = None,
        font_size: int = None,
        anchor: Anchor = None,
        **kwargs,
    ) -> Self:
        """Draw text at the given point."""
        draw.text(
            self,
            txt=text,
            pos=pos,
            font_name=font_name,
            font_size=font_size,
            anchor=anchor,
            **kwargs,
        )
        return self

    def grid(
        self, pos: Point, x_len: float, y_len: float, spacing: float, **kwargs
    ) -> Self:
        """Draw a grid with the given size and spacing."""
        draw.grid(self, pos, x_len, y_len, spacing, **kwargs)
        return self

    def line(self, start: Point, end: Point, **kwargs) -> Self:
        """Draw a line from start to end."""
        draw.line(self, start, end, **kwargs)
        return self

    def lines(self, points: Sequence[Point], **kwargs) -> Self:
        """Draw a polyline through the given points."""
        draw.lines(self, points, **kwargs)
        return self

    def draw_lace(self, lace: Batch, **kwargs) -> Self:
        """Draw the lace."""
        draw.draw_lace(self, lace, **kwargs)
        return self

    def draw_dimension(self, dim: Shape, **kwargs) -> Self:
        """Draw the dimension."""
        draw.draw_dimension(self, dim, **kwargs)
        return self

    def draw(self, item: Drawable, **kwargs) -> Self:
        """Draw the item."""

        draw.draw(self, item, **kwargs)
        return self

    def draw_CS(self, size: float = None, **kwargs) -> Self:
        """Draw the Canvas coordinate system."""
        draw.draw_CS(self, size, **kwargs)
        return self

    def reset(self) -> Self:
        """Reset the canvas to its initial state."""
        self._code = []
        self._pos = [0, 0]
        self._angle = 0
        self._scale = [1, 1]
        self.preamble = defaults["preamble"]
        self.pages = [Page(self.size, self.back_color, self.border)]
        self.active_page = self.pages[0]
        self._all_vertices = []
        self.tex: Tex = Tex()
        self.clip: bool = False  # if true then clip the canvas to the mask
        self._xform_matrix = identity_matrix()
        self.active_page = self.pages[0]
        self._all_vertices = []
        return self

    def __str__(self) -> str:
        return "Canvas()"

    def __repr__(self) -> str:
        return "Canvas()"

    @property
    def xform_matrix(self) -> ndarray:
        """The transformation matrix of the canvas."""
        return self._xform_matrix.copy()

    def reset_transform(self) -> Self:
        """Reset the transformation matrix of the canvas.
        The canvas origin is at (0, 0) and the orientation angle is 0.
        Transformation matrix is the identity matrix."""
        self._xform_matrix = identity_matrix()
        self._pos = [0, 0]
        self._angle = 0
        self._scale = [1, 1]

        return self

    def translate(self, x: float, y: float) -> Self:
        """Translate the canvas by x and y."""
        self._pos[0] += x
        self._pos[1] += y
        self._xform_matrix = translation_matrix(x, y) @ self._xform_matrix

        return self

    def rotate(self, angle: float) -> Self:
        """Rotate the canvas by angle in radians about the origin."""
        self._angle += angle
        about = (self.x, self.y)
        self._xform_matrix = rotation_matrix(angle, about) @ self._xform_matrix

        return self

    def _flip(self, axis: str) -> Self:
        if axis == "x":
            self._scale[0] *= -1
        elif axis == "y":
            self._scale[1] *= -1

        sx, sy = self._scale
        self._xform_matrix = scale_matrix(sx, sy) @ self._xform_matrix

        return self

    def flip_x_axis(self) -> Self:
        """Flip the x-axis direction."""
        return self._flip("x")

    def flip_y_axis(self) -> Self:
        """Flip the y-axis direction."""
        return self._flip("y")

    def scale(self, sx: float, sy: float = None) -> Self:
        """Scale the canvas by sx and sy about the Canvas origin."""
        if sy is None:
            sy = sx
        self._scale[0] *= sx
        self._scale[1] *= sy
        self._xform_matrix = scale_matrix(sx, sy) @ self._xform_matrix

        return self

    @property
    def x(self) -> float:
        """_the x coordinate of the canvas origin."""
        return self._pos[0]

    @property
    def y(self) -> float:
        """_the y coordinate of the canvas origin."""
        return self._pos[1]

    @property
    def angle(self) -> float:
        """_orientation angle in radians."""
        return self._angle

    @property
    def scale_factors(self) -> Vec2:
        """The scale factors."""
        return self._scale

    def batch_graph(self, batch: "Batch") -> nx.DiGraph:
        """Return a directed graph of the batch and its elements.
        Canvas is the root of the graph.
        Graph nodes are the ids of the elements."""

        def add_batch(batch, graph):
            graph.add_node(batch.id)
            for item in batch.elements:
                graph.add_edge(batch.id, item.id)
                if item.subtype == Types.BATCH:
                    add_batch(item, graph)
            return graph

        di_graph = nx.DiGraph()
        di_graph.add_edge(self.id, batch.id)
        for item in batch.elements:
            if item.subtype == Types.BATCH:
                di_graph.add_edge(batch.id, item.id)
                add_batch(item, di_graph)
            else:
                di_graph.add_edge(batch.id, item.id)

        return di_graph

    def _resolve_property(self, item: Drawable, property_name: str) -> Any:
        """Handles None values for properties.
        try item.property_name first,
        then try canvas.property_name,
        finally use the default value.
        """
        value = getattr(item, property_name)
        if value is None:
            value = self.__dict__.get(property_name, None)
            if value is None:
                value = defaults.get(property_name, VOID)
            if value == VOID:
                print(f"Property {property_name} is not in defaults.")
                value = None
        return value

    def get_fonts_list(self) -> list[str]:
        """Get the list of fonts used in the canvas."""
        user_fonts = set(self._font_list)
        latex_fonts = set(
            [defaults["main_font"], defaults["sans_font"], defaults["mono_font"]]
        )

        return list(user_fonts.difference(latex_fonts))

    def _calculate_size(self, border=None, b_box=None) -> Tuple[float, float]:
        """Calculate the size of the canvas based on the bounding box and border."""
        vertices = self._all_vertices
        if vertices:
            if b_box is None:
                b_box = bounding_box(vertices)

            if border is None:
                if self.border is None:
                    border = defaults["border"]
                else:
                    border = self.border
            w = b_box.width + 2 * border
            h = b_box.height + 2 * border
            offset_x, offset_y = b_box.south_west
            res = w, h, offset_x - border, offset_y - border
        else:
            logging.warning("No vertices to calculate the size.")
            res = None
        return res

    def _show_browser(
        self, file_path: Path, show_browser: bool, multi_page_svg: bool
    ) -> None:
        """Show the file in the browser."""
        if show_browser is None:
            show_browser = defaults["show_browser"]
        if show_browser:
            if multi_page_svg:
                for i, _ in enumerate(self.pages):
                    f_path = file_path.replace(".svg", f"_page{i+1}.svg")
                    webbrowser.open(f_path)
            else:
                webbrowser.open(file_path)

    def save(
        self,
        file_path: Path = None,
        overwrite: bool = None,
        show: bool = None,
        print_output=True,
    ) -> Self:
        """Save the canvas to a file."""

        def validate_file_path(file_path: Path, overwrite: bool) -> Result:
            # if file exists and not overwrite, raise error
            path_exists = os.path.exists(file_path)
            if path_exists and not overwrite:
                raise FileExistsError(
                    f"File {file_path} already exists. \n"
                    "Set overwrite=True to overwrite the file."
                )
            # get parent_dir, file_name, extension
            parent_dir, file_name = os.path.split(file_path)
            file_name, extension = os.path.splitext(file_name)
            # check if the extension is valid
            if extension not in [".pdf", ".eps", ".ps", ".svg", ".png", ".tex"]:
                raise RuntimeError("File type is not supported.")
            # check if the parent_dir exists and writable
            if not os.path.exists(parent_dir):
                raise NotADirectoryError(f"Directory {parent_dir} does not exist.")
            if not os.access(parent_dir, os.W_OK):
                raise PermissionError(f"Directory {parent_dir} is not writable.")

            return parent_dir, file_name, extension

        def compile_tex(cmd):
            os.chdir(parent_dir)
            with subprocess.Popen(
                cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
            ) as p:
                output = p.communicate("_s\n_l\n")[0]
            if print_output:
                print(output.split("\n")[-3:])
            return output

        def remove_aux_files():
            time_out = 10  # seconds
            aux_file = os.path.join(parent_dir, file_name + ".aux")
            if os.path.exists(aux_file):
                if not wait_for_file_availability(aux_file, time_out):
                    print(
                        (
                            f"File '{aux_file}' is not available after waiting for "
                            f"{time_out} seconds."
                        )
                    )
                else:
                    os.remove(aux_file)
            log_file = os.path.join(parent_dir, file_name + ".log")
            if os.path.exists(log_file):
                if not wait_for_file_availability(log_file, time_out):
                    print(
                        (
                            f"File '{log_file}' is not available after waiting for "
                            f"{time_out} seconds."
                        )
                    )
                else:
                    os.remove(log_file)
            tex_file = os.path.join(parent_dir, file_name + ".tex")
            if os.path.exists(tex_file):
                if not wait_for_file_availability(tex_file, time_out):
                    print(
                        (
                            f"File '{tex_file}' is not available after waiting for "
                            f"{time_out} seconds."
                        )
                    )
                else:
                    os.remove(tex_file)

        def run_job():
            output_path = os.path.join(parent_dir, file_name + extension)
            cmd = "xelatex " + tex_path
            res = compile_tex(cmd)
            if "No pages of output" in res:
                raise RuntimeError("Failed to compile the tex file.")
            # check if the file exists
            pdf_path = os.path.join(parent_dir, file_name + ".pdf")
            if not os.path.exists(pdf_path):
                raise RuntimeError("Failed to compile the tex file.")

            if extension in [".eps", ".ps"]:
                ps_path = os.path.join(parent_dir, file_name + extension)
                os.chdir(parent_dir)
                cmd = f"pdf2ps {pdf_path} {ps_path}"
                res = subprocess.run(cmd, shell=True, check=False)
                if res.returncode != 0:
                    raise RuntimeError("Failed to convert pdf to ps.")
            elif extension == ".svg":
                doc = fitz.open(pdf_path)
                page = doc.load_page(0)
                svg = page.get_svg_image()
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(svg)
            elif extension == ".png":
                pdf_file = fitz.open(pdf_path)
                page = pdf_file[0]
                pix = page.get_pixmap()
                pix.save(output_path)
                pdf_file.close()

        parent_dir, file_name, extension = validate_file_path(file_path, overwrite)

        tex_code = get_tex_code(self)
        tex_path = os.path.join(parent_dir, file_name + ".tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex_code)
        if extension == ".tex":
            return self

        run_job()
        remove_aux_files()
        # show the file in the browser
        self._show_browser(file_path=file_path, show_browser=show, multi_page_svg=False)
        return self

        # for i, page in enumerate(pages):
        #     sketches = page.sketches
        #     back_color = f"\\pagecolor{color2tikz(page.back_color)}"
        #     if i == 0:
        #         code = [back_color]
        #     else:
        #         code.append(defaults['end_tikz'])
        #         code.append('\\newpage')
        #         code.append(defaults['begin_tikz'])
        #     ind = 0
        #     for sketch in sketches:
        #         sketch_code, ind = get_sketch_code(sketch, canvas, ind)
        #         code.append(sketch_code)

    def new_page(self, **kwargs) -> Self:
        """create a new page and add it to the canvas.pages"""

        page = Page()
        self.pages.append(page)
        self.active_page = page
        for k, v in kwargs.items():
            setattr(page, k, v)


@dataclass
class PageGrid:
    """Grid class for drawing grids on a page."""

    spacing: float = None
    back_color: Color = None
    line_color: Color = None
    line_width: float = None
    line_dash_array: Sequence[float] = None
    x_shift: float = None
    y_shift: float = None

    def __post_init__(self):
        self.type = Types.PAGEGRID
        self.subtype = Types.RECTANGULAR
        self.spacing = defaults["page_grid_spacing"]
        self.back_color = defaults["page_grid_back_color"]
        self.line_color = defaults["page_grid_line_color"]
        self.line_width = defaults["page_grid_line_width"]
        self.line_dash_array = defaults["page_grid_line_dash_array"]
        self.x_shift = defaults["page_grid_x_shift"]
        self.y_shift = defaults["page_grid_y_shift"]
        common_properties(self)


@dataclass
class Page:
    """Page class for drawing sketches and text on a page. All drawing
    operations result as sketches on the canvas.active_page.
    """

    size: Vec2 = None
    back_color: Color = None
    mask = None
    margins = None  # left, bottom, right, top
    recto: bool = True  # True if page is recto, False if verso
    grid: PageGrid = None
    kwargs: dict = None

    def __post_init__(self):
        self.type = Types.PAGE
        self.sketches = []
        if self.grid is None:
            self.grid = PageGrid()
        if self.kwargs:
            for k, v in self.kwargs.items():
                setattr(self, k, v)
        common_properties(self)
