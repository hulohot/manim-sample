from manim import *


class Pith(Scene):
    def construct(self):
        sq = RoundedRectangle(
            corner_radius=0.5,
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=WHITE,
            stroke_width=5,
            height=4,
            width=4
        )

        self.play(Create(sq))
        self.wait()


class Testing(Scene):
    def construct(self):

        name = Text("Ethan").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5, fill_opacity=0.5,
                    fill_color=GREEN).shift(LEFT*3)
        tri = Triangle().scale(0.5).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq))
        self.play(Create(tri))
        self.wait()

        self.play(name.animate.to_edge(UR))
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)
        self.wait()


class FadeInScene(Scene):
    def construct(self):
        c = Circle(radius=1, color=RED, fill_color=BLUE, fill_opacity=0.5)
        p = VGroup(c, c.copy().shift(UP), c.copy().shift(DOWN),
                   c.copy().shift(LEFT), c.copy().shift(RIGHT))
        self.play(ShowIncreasingSubsets(p))
        self.wait()


class Getters(Scene):
    def construct(self):

        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)

        circ = Circle().to_edge(DOWN)

        arrow = always_redraw(
            lambda: Line(start=rect.get_bottom(), end=circ.get_top(), buff=0.2).add_tip())

        g = VGroup(rect, circ, arrow)

        self.play(Create(g))
        self.wait()
        self.play(rect.animate.to_edge(UR),
                  circ.animate.scale(0.5), run_time=4)


class Updaters(Scene):
    def construct(self):

        num = always_redraw(lambda:  MathTex("ln(2)"))
        box = always_redraw(lambda: SurroundingRectangle(
            num, color=BLUE, fill_opacity=0.4, buff=0.5))

        name = Tex("Ethan").next_to(box, DOWN, buff=0.25)

        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT*2), run_time=2)
        self.wait()


class ValueTrackers(Scene):
    def construct(self):

        k = ValueTracker(0)

        num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))

        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(10), run_time=3, rate_func=smooth)
        self.wait()


class Graphing(Scene):
    def construct(self):

        plane = NumberPlane(
            x_range=[-4, 4, 2], x_length=7, y_range=[0, 16, 4], y_length=5
        ).to_edge(DOWN).add_coordinates()

        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

        parab = plane.plot(lambda x: x**2, x_range=[-4, 4], color=RED)
        func_label = MathTex("f(x)={x}^{2}").scale(
            0.6).next_to(parab, RIGHT, buff=0.25)

        area = plane.get_riemann_rectangles(
            graph=parab, x_range=[-2, 3], dx=0.2, stroke_width=0.1, stroke_color=WHITE)

        self.play(DrawBorderThenFill(plane))
        self.play(Write(VGroup(labels, parab, func_label)), run_time=2)
        self.play(Create(area), run_time=2)
        self.wait()


class UpdaterGraphing(Scene):
    def construct(self):

        k = ValueTracker(-4)

        ax = (Axes(x_range=[-4, 4, 1], y_range=[-2, 16, 2],
                   x_length=10, y_length=8).to_edge(DOWN).add_coordinates()
              ).set_color(WHITE)
        func = ax.plot(lambda x: x**2, x_range=[-4, 4], color=BLUE)
        slope = always_redraw(lambda: ax.get_secant_slope_group(
            x=k.get_value(), graph=func, dx=0.01, secant_line_color=GREEN, secant_line_length=3
        ))

        pt = always_redraw(lambda: Dot().move_to(
            ax.c2p(k.get_value(), k.get_value()**2)))

        self.add(ax, func, slope, pt)
        self.wait()
        self.play(k.animate.set_value(4), run_time=3)


class SVGs(Scene):
    def construct(self):

        svg_path = "/Users/ethan/Documents/workspace/repos/manim-sample/learn_manim_course/assets/images/youtube.svg"

        icon = SVGMobject(svg_path)

        self.play(Write(icon))
        self.wait()


class CircleVsSpiral(Scene):
    def construct(self):
        circ_plane = (
            NumberPlane(x_range=[-2, 2], y_range=[-2, 2],
                        x_length=5, y_length=5)
            .to_edge(LEFT)
            .add_coordinates()
        )

        spiral_plane = (
            NumberPlane(x_range=[-2, 2], y_range=[-2, 2],
                        x_length=5, y_length=5)
            .to_edge(RIGHT)
            .add_coordinates()
        )

        r = ValueTracker(1)
        e = ValueTracker(0.01)

        circle = always_redraw(
            lambda: circ_plane.plot_parametric_curve(
                lambda t: np.array(
                    [
                        r.get_value() * np.cos(t),
                        r.get_value() * np.sin(t)
                    ]
                ),
                t_range=[0, e.get_value()],
            ).set_color([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE_E, PURPLE_A])
        )
        circ_dot = always_redraw(lambda: Dot().move_to(circle.get_end()))

        spiral = always_redraw(
            lambda: spiral_plane.plot_parametric_curve(
                lambda t: np.array(
                    [
                        (r.get_value() / (2 * PI)) * t * np.cos(t),
                        (r.get_value() / (2 * PI)) * t * np.sin(t),
                    ]
                ),
                t_range=[0, e.get_value()],
            ).set_color([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE_E, PURPLE_A]),
        )

        spiral_dot = always_redraw(lambda: Dot().move_to(spiral.get_end()))

        circle_equ = (
            MathTex("c(t) = [rcost(t), rsin(t)]").scale(
                0.7).next_to(circ_plane, DOWN)
        )

        spiral_equ = (
            MathTex(
                "s(t) = [\\frac{r}{2\\pi}tcos(t), \\frac{r}{2\\pi}tsin(t)]")
            .scale(0.7)
            .next_to(spiral_plane, DOWN)
        )

        circle_title = Tex("Circle").next_to(circ_plane, UP)
        spiral_title = Tex("Spiral").next_to(spiral_plane, UP)

        time_text = Tex("Timer: ").scale(0.7).shift(LEFT * 0.3)
        timer_num = always_redraw(
            lambda: DecimalNumber().set_value(
                e.get_value()).scale(0.7).next_to(time_text, RIGHT)
        )

        plane_group = VGroup(spiral_plane, circ_plane)
        equ_group = VGroup(spiral_equ, circle_equ)
        title_group = VGroup(spiral_title, circle_title)

        self.play(LaggedStart(
            DrawBorderThenFill(plane_group),
            Write(equ_group),
            Write(title_group),
            lag_ratio=0.75
        ))
        self.wait()
        self.add(circle, circ_dot, spiral, spiral_dot, time_text, timer_num)

        self.play(e.animate.set_value(4 * PI),
                  run_time=4 * PI, rate_func=smooth)
        self.wait()
        self.play(r.animate.set_value(0.5), run_time=2)
        self.play(r.animate.set_value(2), run_time=2)
        self.play(r.animate.set_value(1), run_time=2)
        self.wait()
