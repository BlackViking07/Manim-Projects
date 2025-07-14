from manim import *

class waves(Scene):
    def construct(self):
      
        sine_wave = FunctionGraph(lambda x: np.sin(x), x_range=[-PI, PI], color=BLUE, stroke_width=4)
        cosine_wave = FunctionGraph(lambda x: np.cos(x), x_range=[-PI, PI], color=GREEN, stroke_width=4)

        
        self.play(Create(sine_wave), run_time=2)
        self.wait(0.5)

       
        self.play(Create(cosine_wave), run_time=2)
        self.wait(0.5)

        combined_wave = FunctionGraph(lambda x: np.sin(x) + np.cos(x), x_range=[-PI, PI], color=YELLOW, stroke_width=4)
        self.play(Transform(sine_wave, combined_wave), Transform(cosine_wave, combined_wave), run_time=2)
        self.wait(1)

    
        self.play(FadeOut(sine_wave), FadeOut(cosine_wave), FadeOut(combined_wave), run_time=1)

        
        final_text = Text("Manim Projects", font="Monospace", font_size=72, color=WHITE)
        self.play(FadeIn(final_text, scale=0.8), run_time=2)
        self.wait(2)
