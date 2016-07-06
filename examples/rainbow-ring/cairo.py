def rainbow_ring(ctxt, cx, cy, cr, sw, colors):
	len_colors = len(colors)

	part_arc = (2 * math.pi) / len_colors
	gradient = None
	start_color, end_color = None, None

	ctxt.set_line_width(sw)

	for i, color in enumerate(colors):
		start_color = color
		end_color = colors[ (i + 1) % len_colors]

		start_arc = part_arc * i
		end_arc   = part_arc * (i + 1)

		x1 = cx + math.cos(start_arc) * cr
		x2 = cx + math.cos(end_arc) * cr

		y1 = cy + math.sin(start_arc) * cr
		y2 = cy + math.sin(end_arc) * cr

		ctxt.arc(cx, cy, cr, start_arc, end_arc)
		gradient = cairo.LinearGradient(x1, y1, x2, y2)
		gradient.add_color_stop_rgba(0, *start_color)
		gradient.add_color_stop_rgba(1, *end_color)

		ctxt.set_source(gradient)
		ctxt.stroke()

colors = [
	(1, 1, 0, 1),
	(0, 1, 1, 1),
	(1, 0, 1, 1),
]
sw = 30
shadow_w = 10
cr = shortest_dim / 2 - sw / 2

shadow = ctxt.arc(size.width / 2, size.height / 2, cr - shadow_w / 2, 0, 2 * math.pi)

ctxt.set_source_rgba(0, 0, 0, 0.2)
ctxt.set_line_width(sw + shadow_w)
ctxt.stroke_preserve()

ctxt.set_source_rgba(0, 0, 0, 0.4)
ctxt.set_line_width(sw + shadow_w / 2)
ctxt.stroke()

rainbow_ring(ctxt, size.width / 2, size.height / 2, cr - shadow_w / 2, sw, colors)
