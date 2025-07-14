from manim import *

class SineDerivativeTransform(Scene):
    def construct(self):
        axes = Axes(x_range=[-PI, PI], y_range=[-1.5, 1.5], axis_config={"include_tip": False},)
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE, stroke_width=3)
        sin_label = MathTex("y=\\sin(x)").next_to(sin_graph, UP)

        cos_graph = axes.plot(lambda x: np.cos(x), color=GREEN, stroke_width=3)
        cos_label = MathTex("y=\\cos(x)").next_to(cos_graph, UP)

        self.play(Create(axes), Write(labels))
        self.play(Create(sin_graph), Write(sin_label))
        self.wait(1)

        self.play(Transform(sin_graph, cos_graph), Transform(sin_label, cos_label))
        self.wait(1)

        self.play(
            FadeOut(axes),
            FadeOut(labels),
            FadeOut(sin_graph),
            FadeOut(sin_label)
        )

        title = Text("Manim Projects", font_size=72, color=RED)
        self.play(Write(title))
        self.wait(2)