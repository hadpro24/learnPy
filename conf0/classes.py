class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def tracer(self):
		print("Je trace une ligne")
	def __str__(self):
		return "Je suis l'object Point"

p = Point(3, 5)
print(p.x)
print(p.y)
p.tracer()

