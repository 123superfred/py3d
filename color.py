Color = Union[tuple[int, int, int], list[int]]


def addition(*color : Color) -> Color:
	"""add two or more color
	e.g: 
	(0, 255, 128) + (255, 128, 127) 
	= (255, 255, 255)"""
	r = []
	g = []
	b = []
	for col in color:
		r.append(col[0])
		g.append(col[1])
		b.append(col[2])
	r, g, b = sum(r), sum(g), sum(b)
	if r > 255:
		r = 255
	if g > 255:
		g = 255
	if b > 255:
		b = 255
	result = (r, g, b)
	return result

def mix(*color : Color) -> Color:
	r = []
	g = []
	b = []
	for col in color:
		r.append(col[0])
		g.append(col[1])
		b.append(col[2])
	r = sum(r) / len(r)
	g = sum(g) / len(g)
	b = sum(b) / len(b)
	result = (int(r), int(g), int(b))
	return result

def darker(color : Color, percent : int) -> Color:
	r, g, b = color