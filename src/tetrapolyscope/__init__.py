# Track the __version__ attribute
try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    # Python < 3.8
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version("tetrapolyscope")
except PackageNotFoundError:
    # Package is not installed, fall back to a default
    __version__ = "unknown"

from .core import *

from .structure import *
from .floating_quantities import *
from .managed_buffer import *
from .implicit_helpers import *
from .device_interop import *

from .surface_mesh import *
from .point_cloud import *
from .curve_network import *
from .volume_mesh import *
from .volume_grid import *
from .camera_view import *
from .global_floating_quantity_structure import *
from .point_light import *
