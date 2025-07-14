from manim import *

class animation3(Scene):
    def construct(self):
        
        github_logo = SVGMobject("github-mark.svg")
        github_logo.set_height(2)
        github_logo.set_fill(WHITE, opacity=1)            
        github_logo.set_stroke(WHITE, width=4)            

       
        self.play(FadeIn(github_logo, scale=0.8))
        self.wait(1)

        
        name_text = Text("Manim Projects", font="JetBrainsMono NF", font_size=64)
        name_text.move_to(github_logo.get_center())

        # Transform logo into name
        self.play(Transform(github_logo, name_text))
        self.wait(2)
