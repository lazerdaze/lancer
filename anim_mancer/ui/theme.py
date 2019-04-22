# Project Modules
from anim_mancer.utils import Path


def stylesheet_from_path(filepath=Path.theme, is_debug=False):
	data = None
	
	with open(filepath, 'r') as readFile:
		data = readFile.read()
		if is_debug:
			print data
	
	readFile.close()
	return data
