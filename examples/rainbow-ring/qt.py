offset = 10
circleDiam = shortest_dim - offset

pieRect = QtCore.QRectF(
	(size.width() / 2 - circleDiam / 2),
	(size.height() / 2 - circleDiam / 2),
	circleDiam,
	circleDiam
)

innerDiamOffset = 30
innerPieRect = QtCore.QRectF(
	pieRect.x() + innerDiamOffset,
	pieRect.y() + innerDiamOffset,
	circleDiam - innerDiamOffset * 2,
	circleDiam - innerDiamOffset * 2
)

shadowRect = QtCore.QRectF(
	pieRect.x() + innerDiamOffset / 2,
	pieRect.y() + innerDiamOffset / 2,
	circleDiam - innerDiamOffset,
	circleDiam - innerDiamOffset
)


colors = [
	QtGui.QColor('#ff0'),
	QtGui.QColor('#f0f'),
	QtGui.QColor('#0ff'),
]
len_colors = len(colors)
slice_width = 360 / len_colors
fine_tune = 39
fine_tune_slice = slice_width / fine_tune

shadow_w = 10
shadowPen = QtGui.QPen(QtGui.QColor(0, 0, 0, 255 * 0.2))
shadowPen.setWidth(innerDiamOffset + shadow_w)
painter.setPen(shadowPen)
painter.drawArc(shadowRect, 0, 360*16)

shadowPen = QtGui.QPen(QtGui.QColor(0, 0, 0, 255 * 0.4))
shadowPen.setWidth(innerDiamOffset + shadow_w / 2)
painter.setPen(shadowPen)
painter.drawArc(shadowRect, 0, 360*16)

for i in range(len_colors):
	start_qcol = colors[i]
	end_qcol   = colors[(i + 1) % len_colors]
	start_color = (start_qcol.red(), start_qcol.green(), start_qcol.blue(), start_qcol.alpha())
	end_color   = (end_qcol.red(), end_qcol.green(), end_qcol.blue(), end_qcol.alpha())

	start_angle = i * slice_width
	end_angle   = start_angle + fine_tune_slice

	for j in range(0, fine_tune+1):
		path = QtGui.QPainterPath()

		path.arcMoveTo(innerPieRect, start_angle)
		curpos = path.currentPosition()

		path.arcTo(pieRect, start_angle, fine_tune_slice)
		path.arcTo(innerPieRect, end_angle, -fine_tune_slice)
		path.closeSubpath()

		color = QtGui.QColor(*gfx_utils.blend_colors(start_color, end_color, j / fine_tune))

		painter.fillPath(path, color)
		painter.strokePath(path, color)

		start_angle += fine_tune_slice
		end_angle += fine_tune_slice

#painter.setPen(QtGui.QColor("red"))
#painter.drawRect(pieRect)
