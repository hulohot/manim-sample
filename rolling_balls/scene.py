from manim import *

class CircleBouncing(Scene):
    def construct(self):
        # Create two circles
        circle1 = Circle(radius=2, color=BLUE).move_to(DOWN*3)
        circle2 = Circle(radius=1, color=RED).move_to(DOWN*3)
        
        # Create x-axis and move circles to (0,0) on the x-axis
        x_axis = NumberLine(x_range=[-10, 10], include_numbers=False)
        y_axis = NumberLine(x_range=[-10, 10], include_numbers=False, rotation=PI/2)
        circles = VGroup(circle1, circle2).move_to(DOWN*3 + RIGHT*3)
        
        self.add(x_axis, y_axis, circles)
        
        # Animate the circles bouncing
        self.play(
            MoveAlongPath(circle1, ArcBetweenPoints(circle1.get_center(), RIGHT*10 + UP*3, angle=0)),
            MoveAlongPath(circle2, ArcBetweenPoints(circle2.get_center(), RIGHT*10 + UP*3, angle=0)),
            run_time=4,
            rate_func=linear,
        )
