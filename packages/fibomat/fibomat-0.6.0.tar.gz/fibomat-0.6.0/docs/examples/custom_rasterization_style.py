import numpy as np

from fibomat.raster_styles import RasterStyle
from fibomat.units import LengthQuantity, has_length_dim, LengthUnit, TimeUnit, scale_to, scale_factor
from fibomat.shapes import Shape, DimShape
from fibomat.mill import Mill
from fibomat.rasterizedpattern import RasterizedPattern
from fibomat.curve_tools import rasterize


class ConsecutiveRamped(RasterStyle):
    def __init__(self, pitch: LengthQuantity, ramp_start: float, ramp_end: float):
        """
        Raster style with ramped dwell times.
        The first spot will have dwell time ``mill.dwell_time * ramp_start`` and the last
        ``mill.dwell_time * ramp_end``. All others are linearly interpolated.


        Args:
            pitch (LengthQuantity): pitch of spots
            ramp_start (float): ramp start
            ramp_end (float): ramp end
        """
        if not has_length_dim(pitch):
            raise ValueError('pitch must have dimension [length].')
        self._pitch = pitch

        if ramp_start < 0 or ramp_end < 0:
            raise ValueError('ramp_start and ramp_end must be greater than 0.')

        self._ramp_start = ramp_start
        self._ramp_end = ramp_end

    def dimension(self) -> int:
        return 1

    def rasterize(
        self,
        dim_shape: DimShape,
        mill: Mill,
        out_length_unit: LengthUnit,
        out_time_unit: TimeUnit
    ) -> RasterizedPattern:

        # Rasterize the passed shape with the pitch provided by the user.
        # The pitch must be scaled to the shape unit first to be consistent.
        points = np.array(rasterize(dim_shape.shape, scale_to(dim_shape.unit, self._pitch)).dwell_points)

        # Assign the dwell ramp to the weights of points
        points[:, 2] = np.linspace(self._ramp_start, self._ramp_end, len(points))

        # Scale the mill.dwell_time to the output time unit and multiply it to the dwell ramp values.
        points[:, 2] *= scale_to(out_time_unit, mill.dwell_time)

        # Scale the spots to the output length unit
        points[:, :2] *= scale_factor(out_length_unit, dim_shape.unit)

        # Create a RasterizedPattern object and return it.
        # np.tile repeats the points mill.repeats times.
        return RasterizedPattern(
            np.tile(points, (mill.repeats, 1)),
            length_unit=out_length_unit,
            time_unit=out_time_unit
        )


from fibomat import Sample, U_, Q_, Mill
from fibomat import shapes, default_backends

s = Sample()
site = s.create_site(
    dim_position=(0, 0) * U_('µm'),
    dim_fov=(1, 1) * U_('µm')
)
site.create_pattern(
    dim_shape=shapes.Line((-.75, -.75), (.75, .75)) * U_('µm'),
    mill=Mill(dwell_time=Q_('1 ms'), repeats=5),
    raster_style=ConsecutiveRamped(pitch=Q_('1 nm'), ramp_start=1, ramp_end=np.pi)
)
s.export(default_backends.SpotListBackend).save('rasterized.txt')
