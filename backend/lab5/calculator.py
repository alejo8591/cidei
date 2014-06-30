class Calculator(object):

	def add(self, a, b):

		number_types = (int, long, float, complex)

		if isinstance(a, number_types) and isinstance(b, number_types):
			return a + b
		else:
			raise ValueError