from PyQt5 import QtWidgets, QtGui, QtCore

import math

import sys

import gfx_utils

class QtPlayground(QtWidgets.QWidget):
	def __init__(self, code):
		super().__init__()
		self.resize(400, 250)

		self.code = code
		self.reload_code()

	def mousePressEvent(self, event):
		self.reload_code()

	def reload_code(self):
		print("loading code from", repr(self.code))
		with open(self.code, 'r') as f:
			self.code_compile = compile(f.read(), self.code, 'exec')
		self.repaint()

	def paintEvent(self, event):
		super().paintEvent(event)

		painter = QtGui.QPainter(self)
		painter.setRenderHint(QtGui.QPainter.Antialiasing)
		size = self.size()

		shortest_dim = size.width()  if size.width() < size.height() else size.height()
		longest_dim  = size.height() if size.width() < size.height() else size.width()

		painter.save()
		painter.fillRect(QtCore.QRect(QtCore.QPoint(0,0), size), QtGui.QColor("white"))
		painter.restore()

		painter.save()
		exec(self.code_compile)
		painter.restore()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	playground = QtPlayground(sys.argv[1])
	playground.show()
	app.exec_()
