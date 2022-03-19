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


class Tarea1(PresentationScene):

    def construct(self):
        self.title = BoldTex("Calculadora de factoriales").scale(1.5).to_edge(UP)
        self.add(self.title)
        self.get_teach_factorials_part()
        self.get_demo_part()
        self.get_requirements_part()
    
    def get_teach_factorials_part(self):
        tex = MathTex("1!=1")
        tex2 = MathTex("\\forall n\\in\\mathbb{N}-\\{1\\} \\left(n!=n(n-1)!\\right)")
        g = VGroup(tex, tex2).arrange(DOWN)
        self.play(Write(tex))
        self.end_fragment()
        self.play(Write(tex2))
        self.end_fragment()
        self.play(FadeOut(g))
        self.end_fragment()

    def get_demo_part(self):
        demos = VGroup()
        i = 0

        while i < 4:
            demo = self.generate_demo_for()
            demos.add(demo)
            i += 1
        
        demos.arrange(DOWN)
        
        for demo in demos:
            self.play(Write(demo[0]))
            self.end_fragment()
            self.play(Create(demo[1]))
            self.end_fragment()
        
        self.play(FadeOut(demos))
        self.end_fragment()
    
    def get_requirements_part(self):
        blist = BulletedList(
            "La interfaz de usuario debe ser de tipo CLI", "Deben haber mensajes explícitos",
            "Deben haber errores explícitos"
        ).set_color(TEAL_E)
        for part in blist:
            self.play(Create(part))
            self.end_fragment()

    def generate_demo_for(self):
        self.error_string1 = "¡El valor ingresado es un texto, no un número!"
        self.error_string2 = "¡El valor ingresado no es un entero positivo!"
        string = "Inserte número para calcular su factorial: "
        numero = input(string)
        demo = Tex(string+numero).set_color(RED_E)
        resultado = self.factorial(numero)
        if resultado != self.error_string1 and resultado != self.error_string2:
            tex = Tex("El resultado es: "+str(resultado))
        else:
            tex = Tex(resultado).set_color(BLUE_E)
        group = VGroup(demo, tex).arrange(DOWN)
        return group
    
    def factorial(self, value) -> int | str:
        try:
            float(value)
        except:
            return self.error_string1
        
        value = float(value)
        
        try:
            if not value.is_integer():
                raise
        except:
            return self.error_string2

        value = int(value)

        try:
            if value <= 0:
                raise
        except:
            return self.error_string2

        if value == 1:
            return 1
        else:
            return value*self.factorial(value-1)