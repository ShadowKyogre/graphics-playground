import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk
import cairo
import math

import sys

import gfx_utils

class CairoPlayground(Gtk.DrawingArea):
	def __init__(self, code):
		super().__init__()
		if Gtk.check_version (3, 0, 0) is None:
			self.connect ("draw", self.draw)
		else:
			self.connect ("expose_event", self.draw)

		self.add_events (Gdk.EventMask.BUTTON_PRESS_MASK)
		self.connect("button-press-event", self.reload_code)
		self.set_size_request(400, 250)

		self.code = code
		self.reload_code(None, None)

	def reload_code(self, widget, event):
		print("loading code from", repr(self.code))
		with open(self.code, 'r') as f:
			self.code_compile = compile(f.read(), self.code, 'exec')
		self.queue_draw()

	def draw(self, widget, ctxt):
		size = self.get_allocation()
		shortest_dim = size.width  if size.width < size.height else size.height
		longest_dim  = size.height if size.width < size.height else size.width

		ctxt.save()
		ctxt.set_source_rgb(1.0, 1.0, 1.0)
		ctxt.rectangle(0.0, 0.0, size.width, size.height)
		ctxt.fill()
		ctxt.restore()

		ctxt.save()
		exec(self.code_compile)
		ctxt.restore()

if __name__ == "__main__":
	win = Gtk.Window(title="Cairo Canvas")
	win.add(CairoPlayground(sys.argv[1]))
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()
