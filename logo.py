from manim import *

class logo(Scene):
    def construct(self):

        circle = Circle(radius=1, color=BLUE, fill_opacity=0.5)

        square = Square(side_length=2, color=RED, fill_opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.5)

        triangle = Triangle(color=GREEN, fill_opacity=0.5)
        triangle.scale(0.8)
        triangle.next_to(square, RIGHT, buff=0.5)
        triangle.shift(UP * 0.5)
        self.play(Create(circle), Create(square), Create(triangle))
        self.wait(1)
        self.play(
            circle.animate.shift(LEFT * 2),
            square.animate.shift(LEFT * 2),
            triangle.animate.shift(LEFT * 2)
        )