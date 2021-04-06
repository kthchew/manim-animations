from manim import *
import math

config.frame_x_radius = 12


class BoltzmannDistribution(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=3,
            y_min=0,
            y_max=2,
            x_axis_label='Molecular energy',
            y_axis_label='Number of molecules',
            graph_origin=[-10.0, -2.5, 0.0],
            num_rects=150,
            **kwargs)

    def construct(self):
        self.setup_axes()
        a = 0.4
        activation_energy = 1.2
        curve1 = self.get_graph(lambda x: math.sqrt(2 / math.pi) * (x ** 2 * math.exp(-x ** 2 / (2 * a ** 2)) / a ** 3),
                                x_min=0, x_max=3, color=GREEN)
        line1 = self.get_vertical_line_to_graph(activation_energy, curve1, DashedLine, color=YELLOW)
        activation_energy_label = Tex('$E_a$ [no catalyst]', color=YELLOW).next_to(line1, DOWN)
        activation_energy_label.add_updater(
            lambda m: m.next_to(line1, DOWN)
        )
        area1 = self.get_area(curve1, activation_energy, 4)
        title = Tex("Boltzmann distribution").move_to(self.coords_to_point(1.5, 2.5))
        self.add(title, curve1, line1, area1, activation_energy_label)

        # tempGraph = TemperatureGraph()
        # self.add(tempGraph)
        temp = 0.5
        temp_graph = Axes(
            x_min=0,
            x_max=1,
            x_axis_width=1,
            x_axis_label='',
            x_axis_config={
                "unit_size": 4
            },
            y_min=0,
            y_max=1,
            y_axis_height=1,
            y_axis_config={
                "unit_size": 7
            },
        ).move_to([9.0, -4.0, 0.0], aligned_edge=DOWN)
        temp_title = Tex('Temperature').next_to(temp_graph, UP)
        temp_bar = Rectangle(height=temp, width=2.5, fill_color=RED, fill_opacity=1).move_to(
            temp_graph.coords_to_point(0.5, 0), aligned_edge=DOWN)
        self.add(temp_graph, temp_title, temp_bar)

        a += 0.2
        new_curve = self.get_graph(
            lambda x: math.sqrt(2 / math.pi) * (x ** 2 * math.exp(-x ** 2 / (2 * a ** 2)) / a ** 3), x_min=0, x_max=3,
            color=GREEN)
        new_line = self.get_vertical_line_to_graph(activation_energy, new_curve, DashedLine, color=YELLOW)
        new_area = self.get_area(new_curve, activation_energy, 4)
        temp = 6.0
        new_temp_bar = Rectangle(height=temp, width=2.5, fill_color=RED, fill_opacity=1).move_to(
            temp_graph.coords_to_point(0.5, 0), aligned_edge=DOWN)
        self.play(Transform(curve1, new_curve), Transform(line1, new_line), Transform(area1, new_area),
                  Transform(temp_bar, new_temp_bar), run_time=8)

        a -= 0.2
        new_curve = self.get_graph(
            lambda x: math.sqrt(2 / math.pi) * (x ** 2 * math.exp(-x ** 2 / (2 * a ** 2)) / a ** 3), x_min=0, x_max=3,
            color=GREEN)
        new_line = self.get_vertical_line_to_graph(activation_energy, new_curve, DashedLine, color=YELLOW)
        new_area = self.get_area(new_curve, activation_energy, 4)
        temp = 0.5
        new_temp_bar = Rectangle(height=temp, width=2.5, fill_color=RED, fill_opacity=1).move_to(
            temp_graph.coords_to_point(0.5, 0), aligned_edge=DOWN)
        self.play(Transform(curve1, new_curve), Transform(line1, new_line), Transform(area1, new_area),
                  Transform(temp_bar, new_temp_bar), run_time=8)

        activation_energy = 0.85
        new_line = self.get_vertical_line_to_graph(activation_energy, curve1, DashedLine, color=RED)
        new_area = self.get_area(curve1, activation_energy, 4)
        new_ae_label = Tex('$E_a$ [w/ catalyst]', color=RED).next_to(new_line, DOWN)
        self.play(ReplacementTransform(line1, new_line), ReplacementTransform(area1, new_area),
                  ReplacementTransform(activation_energy_label, new_ae_label))
        self.wait(1)


class TemperatureGraph(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=1,
            x_axis_width=1,
            x_axis_label='',
            x_axis_config={
                "unit_size": 4
            },
            y_min=0,
            y_max=1,
            y_axis_height=1,
            y_axis_label='Temperature',
            y_axis_config={
                "unit_size": 7
            },
            graph_origin=[3.0, -2.5, 0.0],
            **kwargs)

    def construct(self):
        self.setup_axes()
        temp = 0.5
        temperature = Rectangle(height=temp, width=2.5, fill_color=RED, fill_opacity=1)
        temperature.move_to(self.coords_to_point(0.5, 0), aligned_edge=DOWN)
        self.add(temperature)

        temp = 6
        new_temperature = Rectangle(height=temp, width=2.5, fill_color=RED, fill_opacity=1)
        new_temperature.move_to(self.coords_to_point(0.5, 0), aligned_edge=DOWN)
        self.play(Transform(temperature, new_temperature), run_time=8)

        temp = 0.5
        new_temperature = Rectangle(height=temp, width=2.5, fill_color=RED, fill_opacity=1)
        new_temperature.move_to(self.coords_to_point(0.5, 0), aligned_edge=DOWN)
        self.play(Transform(temperature, new_temperature), run_time=8)
