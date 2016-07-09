import math

def blend_colors(s1, s2, blend_factor):
	for c1, c2 in zip(s1, s2):
		yield math.sqrt((1- blend_factor)* c1**2 + blend_factor*c2**2)
