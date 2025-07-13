from manim import *
import numpy as np

class tanwave(Scene):
    def construct(self):
        
        a = Axes(x_range=[-5,6], y_range=[-1.5,1.5])
        tan_graph = a.plot(lambda x: np.tan(x), color=RED)

        self.add(tan_graph, a)