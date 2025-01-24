# Ignore the following lines. These are used to adjust the plot for the documentation.
import sys
if 'sphinx-build' in sys.argv:
    _fullscreen = False
else:
    _fullscreen = True

import numpy as np

from fibomat import Sample, U_
from fibomat import default_backends, shapes, curve_tools


sample = Sample()

enclosing_rect = shapes.Rect(width=3.5, height=2.5, theta=0).to_arc_spline()


rect_site = sample.create_site(
    dim_position=(-2.5, 2.5) * U_('µm'),
    dim_fov=(4, 4) * U_('µm'),
    description='Enclosing rectangular spline'
)

rect_site.create_pattern(
    dim_shape=enclosing_rect * U_('µm'),
    mill=None,
    raster_style=default_backends.StubRasterStyle(2)
)

rect_filled_site = sample.create_site(
    dim_position=(2.5, 2.5) * U_('µm'),
    dim_fov=(4, 4) * U_('µm'),
    description='Filling lines'
)

rect_filling_lines = curve_tools.fill_with_lines(shape=enclosing_rect, pitch=.05, alpha=0, invert=False)

for row in rect_filling_lines:
    for line in row:
        rect_filled_site.create_pattern(
            dim_shape=line * U_('µm'),
            mill=None,
            raster_style=default_backends.StubRasterStyle(2)
        )


# ----------------------------------------------------------------------------------------------------------------------

boundary_spline = shapes.ArcSpline.from_segments([
    shapes.Arc.from_bulge((-1, 0), (-.5, .5), -1),
    shapes.Line((-.5, .5), (.5, 0)),
    shapes.Arc.from_bulge((.5, 0), (1, 0), -1),
    shapes.Arc.from_bulge((1, 0), (-1, 0), -1)
]).scaled(1.5)

# holes must be arc splines, too
holes = [
    shapes.Circle(r=.5, center=(-.75, -.5)).to_arc_spline(),
    shapes.Circle(r=.25, center=(0.25, -.25)).to_arc_spline()
]

hollow_spline = shapes.HollowArcSpline(
    boundary=boundary_spline,
    holes=holes
)

arc_spline_site = sample.create_site(
    dim_position=(-2.5, -2.5) * U_('µm'),
    dim_fov=(4, 4) * U_('µm'),
    description='Enclosing arc spline'
)

arc_spline_site.create_pattern(
    dim_shape=hollow_spline * U_('µm'),
    mill=None,
    raster_style=default_backends.StubRasterStyle(2)
)

arc_spline_filled_site = sample.create_site(
    dim_position=(2.5, -2.5) * U_('µm'),
    dim_fov=(4, 4) * U_('µm'),
    description='Filling lines'
)

arc_spline_filling_lines = curve_tools.fill_with_lines(
    shape=hollow_spline, pitch=.05, alpha=np.pi/6, invert=False
)

for row in arc_spline_filling_lines:
    for line in row:
        arc_spline_filled_site.create_pattern(
            dim_shape=line * U_('µm'),
            mill=None,
            raster_style=default_backends.StubRasterStyle(2)
        )

sample.plot(fullscreen=_fullscreen, legend=False, rasterize_pitch=0.001 * U_('µm'))
