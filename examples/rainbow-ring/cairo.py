def rainbow_ring(ctxt, cx, cy, cr, sw, colors, fine_tune=39):
	len_colors = len(colors)
	full_circle = 2 * math.pi

	part_arc = (full_circle) / len_colors
	fine_tune_arc = part_arc / fine_tune
	gradient = None
	start_color, end_color = None, None

	for i, color in enumerate(colors):
		start_color = color
		end_color = colors[ (i + 1) % len_colors]

		start_arc = part_arc * i
		end_arc   = start_arc + fine_tune_arc

		for j in range(0, fine_tune+1):
			color = tuple(gfx_utils.blend_colors(start_color, end_color, j / fine_tune))

			ctxt.arc(cx, cy, cr - sw / 2, start_arc, end_arc)
			ctxt.arc_negative(cx, cy, cr + sw / 2, end_arc, start_arc)

			ctxt.set_source_rgba(*color)
			ctxt.close_path()

			ctxt.fill_preserve()
			ctxt.set_line_width(1)
			ctxt.stroke()

			start_arc += fine_tune_arc
			end_arc += fine_tune_arc

colors = [
	(1, 1, 0, 1),
	(0, 1, 1, 1),
	(1, 0, 1, 1),
]
sw = 30.0
shadow_w = 10.0
cr = shortest_dim / 2 - sw / 2

shadow = ctxt.arc(size.width / 2, size.height / 2, cr - shadow_w / 2, 0, 2 * math.pi)

ctxt.set_source_rgba(0, 0, 0, 0.2)
ctxt.set_line_width(sw + shadow_w)
ctxt.stroke_preserve()

ctxt.set_source_rgba(0, 0, 0, 0.4)
ctxt.set_line_width(sw + shadow_w / 2)
ctxt.stroke()

rainbow_ring(ctxt, size.width / 2, size.height / 2, cr - shadow_w / 2, sw, colors)
