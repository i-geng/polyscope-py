# Tetetrapolyscope Docs

- Last updated: 9/16/24, [alpha release](https://pypi.org/project/tetrapolyscope/0.0.3/)
  - Examples scripts available at [Chromalab - Coretsumo](https://github.com/varunneal/ChromaLab/tree/master/notebooks/coretsumo).

### Tetracolor Quantities

#### Point Clouds

API follows general style [here](https://polyscope.run/py/structures/point_cloud/color_quantities/).

```
PointCloud.add_tetracolor_quantity(name, values, enabled=None)
```
Add a tetracolor quantity to the point cloud.
- `name` string, a name for the quantity
- `values` and `Nx4` numpy array, with tetracolor values $[0, 1]$ at points.
- `enabled` boolean, whether the quantity is initially enabled.

#### Surface Meshes

API follows general style [here](https://polyscope.run/py/structures/surface_mesh/color_quantities/).

```
SurfaceMesh.add_tetracolor_quantity(name, values, defined_on='vertices', enabled=None)
```
Add a tetracolor quantity to the mesh.
- `name` string, a name for the quantity
- `values` an `Nx4` numpy array, with tetracolor values $[0, 1]$ at vertices or faces
- `defined_on` string, one of `['vertices', 'faces']`, is this data a tetracolor per vertex or face? (`'texture'` not implemented)
- `enabled` boolean, whether the quantity is initially enabled.

### Screenshots

```
set_use_flat_lighting(b)
```
- `b` boolean, whether to use flat lighting. This means that no gamma correction or tonemapping is applied.
  - This option only makes sense for scenes that have tetracolor structures, not regular RGB or even-odd rendering.
  - For regular RGB, follow polyscope's instructions (set material to `'flat'`)
  - For even-odd rendering, just register a six channel color quantity.
  
<br/>

```
rasterize_tetra(filename, save_image_mode)
```
- Saves a screenshot to the path given as `filename` and `save_image_mode`. Extension should be .png.
- `save_image_mode` stromg should be one of `['RG1G2B', 'LMS_Q', 'four_gray']`.
  - `'RG1G2B'`: saves 4 color channels to one RGBA .png file.
  - `'LMS_Q'`: saves first 3 color channels to RGB .png file, saves 4th color channel to grayscale .png file.
  - `'four_gray'`: saves each of 4 color channels to a separate grayscale .png file.

### Video Exports

These methods require FFmpeg to be installed on your system.

#### RGB Video Export

```
open_video_file(filename, fps)
```
- Opens a video file to path given as `filename` with specified `fps`.
- Returns `fd` file descriptor.

<br/>

```
write_video_frame(fd)
```
- Requires `fd` file descriptor returned from a prior call to `open_video_file()`.

<br/>

```
close_video_file(fd)
```
- Requires `fd` file descriptor returned from a prior call to `open_video_file()`.

#### Tetracolor Video Export

```
open_tetra_video_file(filename, fps, save_image_mode).
```
- Opens a video file to path given as `filename` with specified `fps` and `save_image_mode`. Extension should be .mp4
- `save_image_mode` string should be one of `['LMS_Q', 'four_gray']`
  - `'LMS_Q'`: saves first 3 color channels to RGB .mp4 file, saves 4th color channel to grayscale .mp4 file
  - `'four_gray'`: saves each of 4 color channels to a separate grayscale .mp4 file
  - Note: `'RG1G2B'` mode not available for video export
- Returns `tfds` file descriptor

<br/>

```
write_tetra_video_frame(tfds)
```
- Requires `tfds` file descriptor returned from a prior call to `open_tetra_video_file()`.

<br/>

```
close_tetra_video_file(tfds)
```
- Requires `tfds` file descriptor returned from a prior call to `open_tetra_video_file()`

### Six Channel Color Quantities

#### Surface Meshes

API follows general style [here](https://polyscope.run/py/structures/surface_mesh/color_quantities/).

```
SurfaceMesh.add_six_channel_color_quantity(name, values_even, values_odd, defined_on='vertices', enabled=None)
```
Add a six channel color quantity to the mesh.
- `name` string, a name for the quantity
- `values_even` an `Nx4` numpy array, with values $[0, 1]$ at vertices/faces to be rendered on even frames
- `values_odd` an `Nx4` numpy array, with values $[0, 1]$ at vertices/faces to be rendered on odd frames
- `defined_on` string, one of `['vertices', 'faces']`, is this data per vertex or face? (`'texture'` not implemented)
- `enabled` boolean, whether the quantity is initially enabled

#### Render Loop

```
set_render_even_odd_absolute_clock(b=True)
```
- Set this option to `True`, and then call `show()` later on

<br/>

```
set_target_sleep(x)
```
- `x` float, should be in range $[0.0, 100.0]$ for reasonable results

<br/>

```
set_always_redraw(True)
```
- Required to alternate even-odd frames.

#### Debug Options

```
set_draw_even_frame_first(b)
```
- `b` boolean, toggle if even-odd cycle is out of phase with 6-primary LED projector display.

<br/>

```
set_black_out_even_frames(b)
```
- `b` boolean, toggle to black out even frames.

<br/>

```
set_black_out_odd_frames(b)
```
- `b` boolean, toggle to black out odd frames.

<br/>

```
set_build_even_odd_gui_panel(b)
```
- `b` boolean, set to `True` to build debug gui panel.

### Point Lighting

Example script available [here](https://github.com/varunneal/ChromaLab/blob/irene/notebooks/exploration/tetra_polyscope.ipynb).

```
register_point_light(name, position, color)
```
- `name` string to refer to the point light.
- `position` a `1x3` Numpy array for the light's position.
- `color` a `1x3` Numpy array for the light's color.
