from manim import *
import numpy as np

class coswave(Scene):
    def construct(self):

        a = Axes(x_range=[-20,20], y_range=[-5,5])
        cos_graph = a.plot(lambda x : np.cos(x), color=RED)

        self.play(Create(a), run_time = 2)
        self.wait(0.5)

        self.play(Create(cos_graph), run_time = 2)
        self.wait(0.5)