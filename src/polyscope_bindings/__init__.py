from .polyscope_bindings import *

# Re-export submodules at the correct level
import sys
from .polyscope_bindings import imgui as _imgui, implot as _implot
sys.modules['polyscope_bindings.imgui'] = _imgui
sys.modules['polyscope_bindings.implot'] = _implot
imgui = _imgui
implot = _implot
