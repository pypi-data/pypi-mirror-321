import sys; sys.path.append('src')

from zyxxy2 import *
try_shapes()


import matplotlib.pyplot as plt
from zyxxy2 import draw_a_circle, _find_scale_place_axes, draw_a_segment, create_canvas_and_axes

params = {'figsize': (11.69,8.27), 'dpi' : 200, 'font_size' : 15, 'nb_problems_row' : 1, 'nb_problems_col' : 1, 'lw' : 2, 'bw' : 5}

def draw_a_problem(position, text, shift, nb_rows, board_size=13, edge_position='b', star_point_lines=[]):
  assert edge_position in ['b', None, 't']
  show_top = (edge_position == 't') or (nb_rows == board_size)
  show_bottom = (edge_position == 'b') or (nb_rows == board_size)

  dict_ = dict(max_width = 1./params['nb_problems_col'],
           max_height=1./params['nb_problems_row'],
           canvas_width = board_size + 1,
           canvas_height = nb_rows + 1,
           min_margin=0.5,
           font_size=params['fontsize'],
           title_pad=0, tick_step_x=None, tick_step_y=1, ylabel='None',
           xlabel=text,
           canvas_aspect=1,
           xy=[.1, .1])
  print(dict_)
  ax = _find_scale_place_axes(max_width = .5, #1./params['nb_problems_col'],
           max_height=.5, #./params['nb_problems_row'],
           canvas_width = 20, #board_size + 1,
           canvas_height =  20, # nb_rows + 1,
           min_margin=0.5,
           font_size=params['fontsize'],
           title_pad=0, tick_step_x=None, tick_step_y=1, ylabel='None',
           xlabel=text,
           canvas_aspect=1,
           xy=[.1, .1])
  return
  start_y = 1-1/3. if position == 'b' else 1
  length = nb_rows + ((not show_bottom) + (not show_top)) * 0.3
  for v in range(board_size):
    draw_a_segment(start_x=v+.5, start_y=start_y, length=length, color='black', linewidth=params['bw' if v in (0, board_size-1) else 'lw'])
  for h in range(nb_rows):
    draw_a_segment(start_x=0.5, start_y=h+.5, length=length, color='black', linewidth=params['bw' if ((h == 0) and show_bottom) or ((h == nb_rows-1) and show_top) else 'lw'])
  for y, r in enumerate(position):
    for x, s in enumerate(r):
      if s in ['b', 'w']:
        draw_a_circle(center_x=shift[0]+x+0.5, center_y=shift[1]+y+0.5, radius=0.5, color=s)
      

fig = plt.figure(figsize=params['figsize']) #, dpi=params['dpi'])

board_size = 13
nb_rows = 3
title = 'Problem'
main_ax = _find_scale_place_axes(
    max_width = 1./params['nb_problems_col'],
           max_height=1./params['nb_problems_row'],
    canvas_width = board_size + 1,
           canvas_height = nb_rows + 1,
    min_margin=0,
    font_size={
      l: params['font_size']
      for l in ['axes_label', 'axes_tick']
    },
    title_pad=0,
    xlabel=title,
    ylabel=title,
    tick_step_x=None, tick_step_y=None,
    xy=(0.1, 0.1))

canvas_parameters = {
    'canvas_width': board_size + 1,
    'canvas_height': nb_rows + 1,
    'tick_step': None,
    'axes_label_font_size': params['font_size'],
    'axes_tick_font_size': params['font_size']
  }
create_canvas_and_axes(**canvas_parameters, axes=main_ax)

#draw_a_problem(position=['b'], text='b', shift=(1,1), nb_rows=3)
fig.savefig("test.pdf")
print('done')