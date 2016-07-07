function drawShield(startX, startY, height, width, curveRadius) {
	ctxt.beginPath();

	ctxt.arc(startX, startY, curveRadius, 0, Math.PI/2, false);
	ctxt.lineTo(startX + curveRadius, startY+height);
	ctxt.lineTo(startX + width, startY+height);
	ctxt.lineTo(startX + curveRadius + width, startY+curveRadius);

	ctxt.arc(startX + curveRadius + width, startY, curveRadius, -3*Math.PI/2, -Math.PI, false);
	ctxt.closePath();
}

function styleShield(startX, startY, height, width, curveRadius, fills, strokes) {

	for (var i in fills) {
		ctxt.fillStyle = fills[i];
		ctxt.fill();
	}

	for (var i in strokes) {
		ctxt.strokeStyle = strokes[i][0];
		ctxt.lineWidth   = strokes[i][1];
		ctxt.stroke();
	}
}

curveRadius = 40;
startX = 200;
startY = 160;
height = 200;
width = 75;
centerX = startX + curveRadius / 2  + width / 2;

var gradient1 = ctxt.createRadialGradient(
	centerX,
	startY + curveRadius,
	0,
	centerX,
	startY + curveRadius * 2,
	120
);

gradient1.addColorStop(0,   'rgba(0, 255, 255, 1)');
gradient1.addColorStop(0.5, 'rgba(127, 0, 255, 0.2)');
gradient1.addColorStop(1,   'rgba(0, 0, 0, 0)');

var gradient2 = ctxt.createLinearGradient(
	startX,
	startY,
	startX + width + curveRadius,
	startY
);

gradient2.addColorStop(0,    'rgba(0, 0, 0, 0)');
gradient2.addColorStop(0.48, 'rgba(125, 255, 255, 0.3)');
gradient2.addColorStop(0.5,  'rgba(125, 255, 255, 0.5)');
gradient2.addColorStop(0.52, 'rgba(125, 255, 255, 0.3)');
gradient2.addColorStop(1,    'rgba(0, 0, 0, 0)');

var fills = [
	'#116',
	gradient1,
	gradient2,
];


var strokes = [
	['#41b', 4],
	['#5ff', 1],
];

ctxt.scale(0.5, 0.5);
ctxt.translate(250, 500);

ctxt.save();
for (var i = 0; i < 5; i++) {
	ctxt.translate(250, 250);
	ctxt.rotate(72.0 / 180.0 * Math.PI);
	ctxt.translate(-250, -250);
	drawShield(startX, startY, height, width, curveRadius);
	styleShield(startX, startY, height, width, curveRadius, fills, strokes);
}
ctxt.restore();
