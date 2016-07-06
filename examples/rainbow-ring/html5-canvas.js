function drawMultiRadiantCircle(xc, yc, r, sw, radientColors) {
	var partLength = (2 * Math.PI) / radientColors.length;
	var start = 0;
	var gradient = null;
	var startColor = null,
		endColor = null;

	for (var i = 0; i < radientColors.length; i++) {
		startColor = radientColors[i];
		endColor = radientColors[(i + 1) % radientColors.length];

		// x start / end of the next arc to draw
		var xStart = xc + Math.cos(start) * r;
		var xEnd = xc + Math.cos(start + partLength) * r;
		// y start / end of the next arc to draw
		var yStart = yc + Math.sin(start) * r;
		var yEnd = yc + Math.sin(start + partLength) * r;

		ctxt.beginPath();

		gradient = ctxt.createLinearGradient(xStart, yStart, xEnd, yEnd);
		gradient.addColorStop(0, startColor);
		gradient.addColorStop(1.0, endColor);

		ctxt.strokeStyle = gradient;
		ctxt.arc(xc, yc, r, start, start + partLength);
		ctxt.lineWidth = sw;
		ctxt.stroke();
		ctxt.closePath();

		start += partLength;
	}
}

var someColors = [
	'#ff0',
	'#0ff',
	'#f0f'
];

var sw = 30;

ctxt.beginPath();
ctxt.arc(c.width / 2, c.height / 2, 100, 0, Math.PI * 2, false);

ctxt.lineWidth = sw + 10;
ctxt.strokeStyle = 'rgba(0, 0, 0, 0.2)';
ctxt.stroke();

ctxt.lineWidth = sw + 5;
ctxt.strokeStyle = 'rgba(0, 0, 0, 0.4)';
ctxt.stroke();

drawMultiRadiantCircle(c.width / 2, c.height / 2, 100, sw, someColors);
