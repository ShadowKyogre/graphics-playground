center_x = size.width / 2
center_y = size.height / 2

symmetry_count = 5
symmetry_slice = 2 * math.pi / symmetry_count

dab_x = 100
dab_y = 100
dab_r = 20

dist_x = (dab_x - center_x)
dist_y = (dab_y - center_y)

dab_dist = math.sqrt(dist_x**2 + dist_y**2)
dab_angle = math.atan2(dist_y, dist_x)

for i in range(symmetry_count):
	rot_x = center_x + dab_dist * math.cos(symmetry_slice * i + dab_angle)
	rot_y = center_y + dab_dist * math.sin(symmetry_slice * i + dab_angle)
	ctxt.arc(rot_x, rot_y, 20, 0, 2*math.pi)
	if i == 0:
		ctxt.set_source_rgba(0.5, 0, 1.0, 1)
	else:
		ctxt.set_source_rgba(0.5, 0, 0.5, 1)
	ctxt.fill()


for i in range(symmetry_count):
	ctxt.move_to(center_x, center_y)
	rot_x = center_x + longest_dim * math.cos(symmetry_slice * i)
	rot_y = center_y + longest_dim * math.sin(symmetry_slice * i)
	ctxt.line_to(rot_x, rot_y)
	ctxt.set_source_rgba(1, 0, 0, 0.2)
	ctxt.stroke()
