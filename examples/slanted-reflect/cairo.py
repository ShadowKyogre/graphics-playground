def draw_dab(ctxt, angle, x, y, color):
  '''
  An arrow shape
  to represent a possible dab
  '''
  ctxt.save()

  shape = (
    (-10.0,  10.0),
    (  0.0,  -0.0),
    ( 10.0,  10.0),
    (  0.0, -10.0),
  )
  #shape = []
  #for point in base_shape:
  #    shape.append((
  #        (point[0] * math.cos(angle) - point[1] * math.sin(angle)),
  #        (point[0] * math.sin(angle) + point[1] * math.cos(angle)),
  #    ))
  ctxt.translate(x, y)
  ctxt.rotate(angle)

  point = shape[-1]
  ctxt.move_to(
    point[0],
    point[1]
  )
  for point in shape:
    ctxt.line_to(
      point[0],
      point[1]
    )

  ctxt.translate(-x, -y)
  ctxt.set_source_rgba(*color)
  ctxt.fill()
  ctxt.restore()

def angled_guide(ctxt, cx, cy, length, angle, color):
    print(math.degrees(angle))
    ctxt.move_to(cx, cy) 
    ctxt.line_to(
        length * math.cos(angle) + cx,
        length * math.sin(angle) + cy
    )
    ctxt.set_source_rgba(*color)
    ctxt.stroke()

axis_angle = 108+120
cx = size.width / 2
cy = size.height / 2

# Visual aid

angled_guide(
    ctxt,
    cx,
    cy,
    max(size.width, size.height),
    math.radians(90),
    (0, 0.5, 0.5, 1)
)

angled_guide(
    ctxt,
    cx,
    cy,
    max(size.width, size.height),
    math.radians(0),
    (0, 0.5, 0.5, 1)
)

# Draw slanted reflect

angled_guide(
    ctxt,
    cx,
    cy,
    max(size.width, size.height),
    math.radians(axis_angle),
    (1, 0, 1, 1)
)

angled_guide(
    ctxt,
    cx,
    cy,
    max(size.width, size.height),
    math.radians(axis_angle + 180),
    (1, 0, 1, 0.5)
)

# dab

dab_angle = 75
x = size.width * 0.8
y = size.height * 0.5

draw_dab(
  ctxt,
  math.radians(dab_angle),
  x,
  y,
  (0, 0, 1, 0.8)
)

angled_guide(
    ctxt,
    x,
    y,
    max(size.width, size.height),
    math.radians(axis_angle+270),
    (0, 0, 0, 0.5)
)

angled_guide(
    ctxt,
    x,
    y,
    max(size.width, size.height),
    math.radians(90+dab_angle),
    (0, 0, 1, 0.5)
)

#get the angle of the axis
# axis_angle

#get the coordinates of the brush stroke
# x, y

#get the distance between point and center
distance = math.sqrt((x-cx)**2+(y-cy)**2)
point_angle = math.degrees(math.atan2(y-cy, x-cx))

#flip the angle of point
new_point_angle = -(point_angle - axis_angle) + axis_angle

#add the dab angle and new point angle
# place the dab
draw_dab(
  ctxt,
  math.radians(new_point_angle - (180 + dab_angle)),
  distance * math.cos(math.radians(new_point_angle)) + cx,
  distance * math.sin(math.radians(new_point_angle)) + cy,
  (1, 0, 0, 0.8)
)

# place angled guide perpendicular to dab center
angled_guide(
    ctxt,
    distance * math.cos(math.radians(new_point_angle)) + cx,
    distance * math.sin(math.radians(new_point_angle)) + cy,
    max(size.width, size.height),
    math.radians(new_point_angle - (90 + dab_angle)),
    (1, 0, 0, 0.5)
)
