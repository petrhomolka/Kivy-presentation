from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty, StringProperty
from kivy.graphics import *
import numpy as np
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.config import Config

Config.set('graphics', 'width', '495')
Config.set('graphics', 'height', '550')


class MainLabels(Widget):
	pass

	def plotGraph(self, amplit):
		numAmp = float(amplit)
		self.my_output.text="graph"
		
		for plot in self.my_graph.plots:
			self.my_graph.remove_plot(plot)
		
		plot = MeshLinePlot(mode='line_strip', color=[1, 0, 0, 1])
		plot.points = [(x, 10*np.sin(0.5*x/numAmp)) for x in xrange(-0, 100)]
		self.my_graph.add_plot(plot)
		
		self.my_graph.x_ticks_major=25
		self.my_graph.y_ticks_major=25
		self.my_graph.xmin=-0
		self.my_graph.xmax=100
		self.my_graph.ymin=-25
		self.my_graph.ymax=25
		self.my_graph.xlabel='X axis'
		self.my_graph.ylabel='Y axis'

class PresentationApp(App):
	def build(self):
		return MainLabels()

if __name__ == '__main__':
	PresentationApp().run()