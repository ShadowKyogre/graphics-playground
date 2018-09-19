def angled_guide(ctxt, cx, cy, length, angle, color):
    print(180 / math.pi * angle)
    ctxt.move_to(cx, cy) 
    ctxt.line_to(
        length * math.cos(angle) + cx,
        length * math.sin(angle) + cy
    )
    ctxt.set_source_rgba(*color)
    ctxt.stroke()

guides = 5

for g in range(guides):
    angled_guide(
        ctxt,
        size.width / 2,
        size.height / 2,
        max(size.width, size.height),
        2 * math.pi * g / guides,
        (0, 0, 0, 1)
    )
    angled_guide(
        ctxt,
        size.width / 2,
        size.height / 2,
        max(size.width, size.height),
        -(2 * math.pi * (g + 0.5) / guides),
        (0, 0, 1, 1)
    )
