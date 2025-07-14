from manim import *

class animation22(Scene):
    def construct(self):

        c = Circle(2, color = RED, fill_opacity = 0.1)

        self.play(DrawBorderThenFill(c), run_time = 0.2)

        title = Text("Zabir", font_size = 63).shift(UP * 0.3)
        subtitle = Text("Hasan", font_size = 45).shift(DOWN * 0.5)
        self.play(Write(title), Write(subtitle))

        a = Arc(2.2, TAU * 1 / 4, -TAU * 1 / 4, color = BLUE, stroke_width=15)
        self.play(Create(a))

        self.wait(3)