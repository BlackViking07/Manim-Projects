from manim import *
import numpy as np

class sinwave(Scene):
    def construct(self):

        a = Axes(x_range=[-20,20], y_range=[-4,4])
        sin_graph = a.plot(lambda x: np.sin(x), color=BLUE)

        self.add(sin_graph, a)