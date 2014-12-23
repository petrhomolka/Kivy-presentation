# <This File is part of Kivy-Presentation.>
# Copyright (C) <2014>  <Petr Homolka>
#
# Kivy-Presentation is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Kivy-Presentation is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# <Kivy-Presentation>  Copyright (C) <2014>  <Petr Homolka>
#
# Kivy-Presentation comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; type `show c' for details.

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