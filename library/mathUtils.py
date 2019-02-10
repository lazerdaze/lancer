def setRange(value, oldMin, oldMax, newMin, newMax):
	value = float(value)
	oldMin = float(oldMin)
	oldMax = float(oldMax)
	newMin = float(newMin)
	newMax = float(newMax)
	return newMin + (((value - oldMin) / (oldMax - oldMin)) * (newMax - newMin))


def percentage(value, min, max):
	return setRange(value, min, max, 0, 1) * 100

