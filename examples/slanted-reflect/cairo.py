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
    print(180 / math.pi * angle)
    ctxt.move_to(cx, cy) 
    ctxt.line_to(
        length * math.cos(angle) + cx,
        length * math.sin(angle) + cy
    )
    ctxt.set_source_rgba(*color)
    ctxt.stroke()

axis_angle = 108
cx = size.width / 2
cy = size.height * 0

angled_guide(
    ctxt,
    cx,
    cy,
    max(size.width, size.height),
    2 * math.pi * axis_angle / 360,
    (0, 0, 0, 1)
)

angled_guide(
    ctxt,
    cx,
    cy,
    max(size.width, size.height),
    2 * math.pi * 90 / 360,
    (0, 0, 1, 1)
)

dab_angle = 0
x = size.width * 0.8
y = size.height * 0.5

draw_dab(
  ctxt,
  dab_angle,
  x,
  y,
  (0, 0, 1, 0.8)
)

#get the angle of the axis
# axis_angle

#get the coordinates of the brush stroke
# x, y

#get the distance between point and center
distance = math.sqrt((x-cx)**2+(y-cy)**2)
point_angle = math.atan2(y-cy, x-cx) * 180 / math.pi

#flip the angle of point
new_point_angle = -(point_angle - axis_angle) + axis_angle

#add the dab angle and axis angle
#also add 90 to adjust for perpendicular
new_dab_angle = -(dab_angle - axis_angle - 90) + (axis_angle + 90)

print("P1::", point_angle, dab_angle)
print("P2::", new_point_angle, new_dab_angle)

# place the dab
draw_dab(
  ctxt,
  new_dab_angle * 2 * math.pi / 360,
  distance * math.cos(new_point_angle * 2 * math.pi / 360) + cx,
  distance * math.sin(new_point_angle * 2 * math.pi / 360) + cy,
  (1, 0, 0, 0.8)
)
