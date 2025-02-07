import inspect

from .get_b_vars import get_scene, get_props

def add_row_with_label_and_operator (
  layout, 
  data, 
  prop, 
  text,
  op,
  op_text = '',
  icon = ''
):
  row = layout.row()
  row.prop(data, prop, text = text)
  return _add_row_with_operator(row, op, op_text, icon)
      
def _add_row_with_operator (row, operator, text = '', icon = None):
  if icon:
    return row.operator(operator, text = text, icon = icon)
  
  return row.operator(operator, text = text)

def add_row (layout, data, prop, text):
  row = layout.column().row()
  row.prop(data, prop, text = text)

def add_row_with_label (layout, label, data, prop, factor):
  split = layout.column().split(factor = factor)
  row_label = split.row()
  row_label.label(text = label)
  row_prop = split.row()
  row_prop.prop(data, prop, text = "")

def add_row_with_operator (layout, operator, text = '', icon = None):
  row = layout.column().row()
  _add_row_with_operator(row, operator, text, icon)

def add_scene_custom_prop (
  name = None, 
  prop_type = None, 
  default = None, 
  desc = None,
  min = None,
  max = None,
  type = None
):
  kwargs = {}
  
  if name is not None:
    kwargs['name'] = name
  if type is not None:
    kwargs['type'] = type
  if default is not None:
    kwargs['default'] = default
  if desc is not None:
    kwargs['description'] = desc
  if min is not None:
    kwargs['min'] = min
  if max is not None:
    kwargs['max'] = max

  print(kwargs)
  fn = getattr(get_props(), f'{ prop_type }Property')
  scene = get_scene()
  setattr(scene, name, fn(**kwargs))
  # setattr(scene, name, fn(name = name, description = desc, default = default))

  # bpy.types.Scene.body_type = bpy.props.IntProperty(
  #   name = 'body_type',
  #   description = 'Loli / Boy / Girl / Male / Lady => [1, 5]',
  #   default = 3,
  #   min = 1,
  #   max = 5
  # )
  