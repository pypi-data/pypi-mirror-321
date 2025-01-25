==========================
GUIgenerator
==========================
GUIgenerator facilitates the process of creating simple GUI applications.

Usage
==========================
Example of running the project:
   .. code-block:: bash
   
	from gui_generator import *

	def Average(n):
		s = 0
		for x in range(n):
			s += int(g.addInput())
		return s / n

	g = GUIgenerator()
	g.create(Average, args=["How many numbers:"])
