import sys; sys.path.append('src')
import matplotlib.pyplot as plt

from zyxxy2 import prepare_axes, _find_scale_place_axes

def try_canvas(axes_bbox=[[.5, .5], [1, 1]], canvas_width=25, canvas_height=20, gap_x=0.05, gap_y=0.05):
  ##########################################################################################

  main_ax = _find_scale_place_axes(
    max_width=axes_bbox[1][0] - axes_bbox[0][0] - 2 * gap_x,
    max_height=axes_bbox[1][1] - axes_bbox[0][1] - 2 * gap_y,
    canvas_width=canvas_width,
    canvas_height=canvas_height,
    min_margin=0,
    font_size={},
    title_pad=0,
    xlabel="",
    ylabel="",
    tick_step_x=None, tick_step_y=None,
    xy=(axes_bbox[0][0]+gap_x, axes_bbox[0][1]+gap_y))

  canvas_parameters = {
    'canvas_width': canvas_width,
    'canvas_height': canvas_height,
    'tick_step_x': None,
    'tick_step_y': None,
    'add_border': True
  }
  prepare_axes(ax=main_ax, **canvas_parameters)


plt.figure(dpi=50, figsize=(11, 8))
try_canvas()
plt.show()
