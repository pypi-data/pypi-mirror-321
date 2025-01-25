# simetri.graphics ![logo](/images/logo4.svg)
*simetri.graphics* is a graphics library for Python that focuses on 2D symmetry operations and pattern generation. It uses the TikZ library (see https://tikz.net) and generates .tex files that can be compiled to create output files. It can also be used in Jupyter notebooks to create complex geometric patterns and designs. The library is designed to be easy to use and flexible, allowing users to create a wide variety of symmetrical patterns with minimal effort. The library also includes a number of computational geometry utility functions for working with 2D geometry.

It is designed to be used in conjunction with XeLaTeX rendering engine. Currently the project is in its late alpha stages and is not ready for production use. Beta release is expected to be in March 2025. Although this version is a proof of concept and is likely to change significantly in the future, it is already capable of producing some interesting results.

*simetri.graphics* can generate output files with .tex, .pdf, .ps, .eps, .svg, or .png extensions. It can also generate Jupyter notebook cells with the output embedded in them.

The documentation is available at [simetri/docs](https://github.com/mekanimo/simetri/blob/master/docs/brief_overview.ipynb). There is also a gallery of examples available at [simetri/gallery](https://github.com/mekanimo/simetri/blob/master/gallery.ipynb).

## Version

This is the first alpha version of the library and is not yet ready for production use. The library is still in its early stages of development and is likely to change significantly in the near future. The beta release is expected to be in March 2025.

## Installation
If you have a Python version >= 3.9 installed, execute the following command in the terminal:

```pip install simetri```

This will not install a LaTeX distribution, so you will need to install one separately.



### Install a LaTeX distribution
There are several LaTeX distributions freely available for different operating systems. The recommended distribution is the MikTeX app.

MikTeX handles package installations automatically, so it is recommended for users who are not familiar with LaTeX typesetting engines.

MiKTeX can be downloaded from https://miktex.org/download.

## Requirements

- Python version 3.9 or later.
- A LaTeX distribution with XeLaTeX engine is required for rendering the output. Miktex is the recommended distribution since it handles installation of required packages automatically.

The library requires the following Python packages:

- `numpy`
- `networkx`
- `matplotlib`
- `Pillow`
- `IPython`
- `pymupdf`
- `strenum`
- `typing-extensions`

These extensions are installed automatically when you install the library using pip or uv.

## Example
```python
import simetri.graphics as sg

canvas = sg.Canvas()

for  i in range(8, 15, 2):
    star = sg.stars.Star(n=i, circumradius=150).level(4)
    star.translate(i * 170, 0)
    swatch = sg.random_swatch()
    lace = sg.Lace(star, swatch=swatch, offset=5)
    canvas.draw(lace.scale(.75))

canvas.display()
```
![12 sided star](/images/example.svg)

> [!NOTE]
> All examples use `canvas.display()` to show the results in a Jupyter notebook. If you are using it as a stand alone library, use `canvas.save("c:/temp/example.pdf")` to save the output as a pdf file. You can generate .pdf, .svg, .ps, .eps, .tex, and .png output.

## Contact

If you have any questions or suggestions, please feel free to contact me at [fbasegmez@gmail.com](mailto:fbasegmez@gmail.com)

## Feedback

If you have any feedback or suggestions for the library, please feel free to open an issue on the GitHub repository or contact me by email. I am always looking for ways to improve the library and make it more useful for users.

## License

This project is licensed under the GNU General Public License v2.0 (GPLv2) - see the LICENSE file for details.
