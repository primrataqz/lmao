from manimlib import *

class MKC(InteractiveScene):
    def construct(self):
        # Setup
        axes = NumberPlane(
            (-4, 4), (0, 1.5, 0.5),
            width=14, height=5,
            background_line_style=dict(
                stroke_color=GREY_C,
                stroke_width=2,
                stroke_opacity=0.5
            )
        )
        axes.x_axis.add_numbers(font_size=24)
        axes.y_axis.add_numbers(num_decimal_places=1, excluding=[0])
        axes.to_edge(DOWN)
        graph = axes.get_graph(lambda x: np.exp(-x**2))
        graph.set_stroke(BLUE, 3)

        t2c = {"x": BLUE}
        graph_label = Tex("e^{-x^2}", font_size=72, t2c=t2c)
        graph_label.next_to(graph.pfp(0.6), UR)

        self.add(axes)
        self.play(ShowCreation(graph))
        self.play(Write(graph_label))
        self.wait()