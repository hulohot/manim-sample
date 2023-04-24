from manim import *


class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)


class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)


class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin
        circle.move_to(LEFT * 2)
        # place the square to the left of the circle
        square.next_to(circle, LEFT, buff=0.1)
        # align the left border of the triangle to the left border of the circle
        triangle.align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)


class MobjectStyling(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(circle, square, triangle)
        self.wait(1)


class SomeAnimations(Scene):
    def construct(self):
        square = Square()

        # some animations display mobjects, ...
        self.play(FadeIn(square))

        # ... some move or rotate mobjects around...
        self.play(Rotate(square, PI/4))

        # some animations remove mobjects from the screen
        self.play(FadeOut(square))

        self.wait(1)


class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # animate the change of color
        self.play(square.animate.set_fill(WHITE))
        self.wait(1)

        # animate the change of position and the rotation at the same time
        self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)
        self.play(square.animate.shift(DOWN).rotate(-PI / 3))
        self.wait(1)


class RunTime(Scene):
    def construct(self):
        square = Square()
        circle = Circle(color=BLUE, fill_opacity=0.5)
        circle.next_to(square, UP)
        self.add(square)
        self.play(ReplacementTransform(square, circle), run_time=1)
        self.wait(1)


class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)

        self.wait()


class MobjectExample(Scene):
    def construct(self):
        p1 = [-1, -1, 0]
        p2 = [1, -1, 0]
        p3 = [1, 1, 0]
        p4 = [-1, 1, 0]
        a = Line(p1, p2).append_points(
            Line(p2, p3).points).append_points(Line(p3, p4).points)

        dot = Dot(a.get_start()).set_color(PURPLE).scale(1.2)
        point_start = a.get_start()
        point_end = a.get_end()
        point_center = a.get_center()
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(
            UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24).next_to(
            self.mobjects[-1], DOWN).set_color(RED))
        dot_position_center = Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24).next_to(
            self.mobjects[-1], DOWN).set_color(BLUE)
        self.add(dot_position_center)
        dot_position_title = Text(f"dot position = {np.round(dot.get_center(),2).tolist()}", font_size=24).next_to(
            dot_position_center, DOWN).set_color(WHITE)
        self.add(dot_position_title)

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)

        self.add(dot)
        self.wait(1)
        self.play(dot.animate.move_to(p2))
        dot_position_title_p2 = Text(f"dot position = {np.round(p2,1).tolist()}", font_size=24).next_to(
            dot_position_center, DOWN).set_color(WHITE)
        self.play(FadeOut(dot_position_title), FadeIn(dot_position_title_p2))
        self.wait(1)
        self.play(dot.animate.move_to(p3))
        dot_position_title_p3 = Text(f"dot position = {np.round(p3,1).tolist()}", font_size=24).next_to(
            dot_position_center, DOWN).set_color(WHITE)
        self.play(FadeOut(dot_position_title_p2),
                  FadeIn(dot_position_title_p3))
        self.wait(1)
        self.play(dot.animate.move_to(p4))
        dot_position_title_p4 = Text(f"dot position = {np.round(p4,1).tolist()}", font_size=24).next_to(
            dot_position_center, DOWN).set_color(WHITE)
        self.play(FadeOut(dot_position_title_p3),
                  FadeIn(dot_position_title_p4))


class CircleBox(Scene):
    def construct(self):
        # Create four points to form a box
        points = [
            [-3, -2, 0],
            [-3, 2, 0],
            [3, 2, 0],
            [3, -2, 0]
        ]
        box = VGroup(
            *[Dot(point, color=WHITE) for point in points],
            *[Line(points[i], points[(i+1) % 4], color=WHITE) for i in range(4)]
        )

        # Create a circle to move around the box
        circle = Circle(radius=0.5, color=YELLOW).move_to(points[0])

        # Create text to show the current position of the circle
        text = Tex("Current position: ").to_corner(UR)
        current_position = DecimalNumber(
            0, num_decimal_places=1).next_to(text, RIGHT)

        # Add everything to the scene
        self.add(box, circle, text, current_position)

        # Animate the circle moving around the box
        for i in range(4):
            next_point = points[(i+1) % 4]
            self.play(
                MoveAlongPath(circle, Line(circle.get_center(),
                              next_point), rate_func=linear),
                current_position.animate.set_value(i+1),
                run_time=2
            )
