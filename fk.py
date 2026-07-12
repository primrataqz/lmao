from manimlib import *

class Template(InteractiveScene):
    def construct(self):
        logo = Tex(R"\langle \phi \rangle")
        logo.set_color(PURPLE_A)
        logo.scale(0.6)
        logo.to_edge(UL, buff=MED_SMALL_BUFF)
        self.add(logo)

        v_line = Line(UP, DOWN)
        v_line.set_height(logo.get_height()*1.7)
        v_line.next_to(logo, RIGHT)
        v_line.insert_n_curves(10)
        v_line.set_stroke(width=[0.5, 1, 1, 0.5])
        self.add(v_line)

        h_line = Line(LEFT, RIGHT)
        h_line.set_width(FRAME_WIDTH - 1)
        h_line.to_edge(DOWN)
        h_line.insert_n_curves(10)
        h_line.set_stroke(width=[0.5, 1.0, 1.0, 0.5])
        self.add(h_line)

        page_no = Integer(1)
        cir = Circle(radius=0.1)
        cir.set_stroke(WHITE, 1.0)
        cir.set_fill("#191919")
        page_no.set_height(cir.get_height()*0.5)
        page_no.move_to(cir)
        vgroup = VGroup(cir, page_no)
        vgroup.next_to(h_line, DOWN, buff=SMALL_BUFF)
        self.add(vgroup)

        title = Tex(R"\text{Taylor Series}", font_size=40)
        title.next_to(v_line, RIGHT)
        self.add(title)