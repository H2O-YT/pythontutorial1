from manim import *
from manim_revealjs import *
import datetime


config.video_dir = "videos"
config.images_dir = "images"
config.tex_dir = "tex"
config.text_dir = "text"
config.background_color = WHITE
VMobject.set_default(stroke_color=BLACK, background_stroke_color=WHITE)
Tex.set_default(background_stroke_width=5)


class BoldTex(Tex):
    def __init__(self, *tex_strings, arg_separator="", tex_environment="center", **kwargs):
        if len(tex_strings) == 1:
            bold_tex_strings = ["\\textbf{" + tex_strings[0] + "}"]
        elif len(tex_strings) == 2:
            bold_tex_strings = ["\\textbf" + tex_strings[0], tex_strings[1] + "}"]
        else:
            bold_tex_strings = ["\\textbf" + tex_strings[0], *tex_strings[1:-1], tex_strings[-1] + "}"]
        super().__init__(*bold_tex_strings, arg_separator=arg_separator, tex_environment=tex_environment, **kwargs)


class MonospacedTex(Tex):
    def __init__(self, *tex_strings, arg_separator="", tex_environment="center", **kwargs):
        if len(tex_strings) == 1:
            bold_tex_strings = ["\\texttt{" + tex_strings[0] + "}"]
        elif len(tex_strings) == 2:
            bold_tex_strings = ["\\texttt" + tex_strings[0], tex_strings[1] + "}"]
        else:
            bold_tex_strings = ["\\texttt" + tex_strings[0], *tex_strings[1:-1], tex_strings[-1] + "}"]
        super().__init__(*bold_tex_strings, arg_separator=arg_separator, tex_environment=tex_environment, **kwargs)



class Thumbnail(Scene):
    def construct(self):
        title = BoldTex("Curso de Python").set_color(BLUE_E).scale(2).to_edge(UP)
        text = Tex("Elementos básicos").scale(1.5).to_edge(DOWN)
        python_logo = ImageMobject("python_tutorial.png").scale(0.5)
        self.add(title, text, python_logo)


class TitleSlide(PresentationScene):
    def construct(self):
        title = BoldTex("Curso de Python").set_color(BLUE_E).scale(1.5)
        subtitle = Tex("Elementos básicos").set_color(BLUE_E)
        author = Tex("H2O en español").set_color(BLACK)
        python_logo = ImageMobject("python_tutorial.png").scale(0.3)
        date = Tex(datetime.datetime.now().strftime("%d/%m/%Y")).to_edge(DOWN)
        group = VGroup(title, subtitle, author).arrange(DOWN)
        all_group = Group(group, python_logo, date).arrange(DOWN, buff=1)
        self.add(*all_group)
        self.end_fragment()


class Tarea(PresentationScene):

    def construct_teach_part(self):
        pass

    def construct_demo_part(self):
        pass

    def construct_instructions_part(self, *instructions):
        blist = BulletedList(*instructions).set_color(TEAL)
        for item in blist:
            self.play(Create(item))
            self.end_fragment()


class Tarea1(Tarea):

    def construct(self):
        self.construct_demo_part()
        self.construct_instructions_part("Crear una función que tome dos números.", "La función debe devolver el mayor de ellos.")
    
    def construct_demo_part(self):
        import tarea1
        title = BoldTex("Crear función \\texttt{max2}").scale(1.5).to_edge(UP)
        self.add(title)
        self.end_fragment()
        pares = [["5", "-7"], ["1", "3"], ["-1", "-2"], ["-2.5", "1/3"]]
        group = VGroup()
        for par in pares:
            partial_group = VGroup()
            tex1 = MonospacedTex("max2("+", ".join(par)+")").set_color(BLUE_E)
            output = str(tarea1.max2(*[eval(numero) for numero in par]))
            tex2 = MonospacedTex(output)
            partial_group.add(tex1, tex2)
            partial_group.arrange(DOWN)
            group.add(partial_group)
        group.arrange(DOWN)
        for part in group:
            self.play(Write(part[0]))
            self.end_fragment()
            self.play(Create(part[1]))
            self.end_fragment()
        self.play(FadeOut(group))
        self.end_fragment()


class Tarea2(Tarea):

    def construct(self):
        self.construct_teach_part()
        self.construct_demo_part()
        self.construct_instructions_part("\\texttt{factorial(n)} debe ser igual a $n!$")
    
    def construct_teach_part(self):
        title = BoldTex("Crear función \\texttt{factorial}").scale(1.5).to_edge(UP)
        self.add(title)
        self.end_fragment()
        text = Tex("$n!$ es el producto de los $n$ primeros enteros positivos.")
        ejemplo = MathTex("3!", "=3\\cdot 2\\cdot 1", "=6")
        ejemplo2 = MathTex("1!", "=1")
        g = VGroup(text, ejemplo, ejemplo2).arrange(DOWN)
        for i in range(len(g)):
            if i == 0:
                self.play(Write(g[i]))
                self.end_fragment()
            else:
                for tex_string in g[i]:
                    self.play(Write(tex_string))
                    self.end_fragment()
        self.play(FadeOut(g))
        self.end_fragment()
    
    def construct_demo_part(self):
        import tarea2
        lst = ["1", "3", "13", "15"]
        group = VGroup()
        for i in lst:
            partial_group = VGroup()
            tex = MonospacedTex(i.join(["factorial(", ")"])).set_color(BLUE_E)
            tex2 = MonospacedTex(str(tarea2.factorial(int(i))))
            partial_group.add(tex, tex2)
            partial_group.arrange(DOWN)
            group.add(partial_group)
        group.arrange(DOWN)
        for part in group:
            self.play(Write(part[0]))
            self.end_fragment()
            self.play(Create(part[1]))
            self.end_fragment()
        self.play(FadeOut(group))
        self.end_fragment()