from manim import *
import numpy as np

class sinwave(Scene):
    def construct(self):

        a = Axes(x_range=[-20,20], y_range=[-4,4])
        sin_graph = a.plot(lambda x: np.sin(x), color=BLUE)

        self.play(Create(a), run_time = 2)
        self.wait(0.5)

        self.play(Create(sin_graph), run_time = 2)
        self.wait(0.5)