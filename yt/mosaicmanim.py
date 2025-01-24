from manim import *
from numpy import array, cos, sin

# global colors
b = "#005F73" # 
a = "#0A9396" # t_{n,m}
c = "#94D2BD" # 
d = "#E9D8A6" # tile boarder
e = "#EE9B00" # p_{n,m}
f = "#CA6702" # 
g = "#BB3E03" # 
h = "#AE2012" # tile 
i = "#9B2226" # 

# Introduction
class Section1(Scene):
    def construct(self):
        self.camera.background_color = "#181818"

        e1 = Tex(r"This video is intended for people with at least on course in calculus, and especially for high school students considering a major in mathematics.")
        e1.scale(0.6)

        self.wait(1)
        self.play(FadeIn(e1), run_time=1)
        self.wait(4)
        self.play(FadeOut(e1), run_time=1)
        self.wait(1)

# Backburner Problems
class Section2(Scene):
    def construct(self):
        self.camera.background_color = "#181818"

        # a = "#005F73" # 
        # b = "#0A9396" # 
        # c = "#94D2BD" # 
        # d = "#E9D8A6" # tile boarder
        # e = "#EE9B00" # 
        # f = "#CA6702" # 
        # g = "#BB3E03" # 
        # h = "#AE2012" # tile 
        # i = "#9B2226" # 

        e1 = Tex(r"Backburner Problems").scale(1.5)

        self.wait(1)
        self.play(Write(e1), run_time=1)
        self.wait(1)
        self.play(FadeOut(e1))
        self.wait(1)

        # WSJ
        # https://www.youtube.com/watch?v=Y5K49dtOKmo
        # ilmango
        # https://www.youtube.com/watch?v=H3bCCANEbbQ&t=589s
        # veritasium
        # https://www.youtube.com/watch?v=S2xHZPH5Sng&t=893s

        x_ob = Tex(r"$\times$").set_color(i)
        cx_ob = x_ob.copy().shift(RIGHT*-4).shift(UP*-2).scale(1.5)
        ccx_ob = x_ob.copy().shift(RIGHT*0).shift(UP*-2).scale(1.5)
        check_ob = Tex(r"\checkmark").set_color(GREEN).shift(RIGHT*4).shift(UP*-1.9).scale(1.2)

        matrix = Matrix([[1,1],[1,0]]).shift(RIGHT*-4).shift(UP*0.5)

        zeta = Tex(r"$\zeta(s)$").shift(UP*0.5).scale(2)
        zeta[0][2].set_color(d)

        heart = ParametricFunction(lambda t: array([((1-cos(t))*(cos(t))), ((1-cos(t))*(sin(t))), 0]), t_range = array([0,TAU])).set_color(i).shift(RIGHT*4.8).rotate(PI/2).scale(0.7).shift(UP*0.5)

        self.play(Write(matrix))
        self.play(Write(cx_ob))
        self.wait(1)

        self.play(Write(zeta))
        self.play(Write(ccx_ob))
        self.wait(1)

        self.play(Write(heart))
        self.play(Write(check_ob))
        self.wait(1)

        self.play(FadeOut(cx_ob),FadeOut(ccx_ob),FadeOut(check_ob),FadeOut(matrix),FadeOut(zeta),FadeOut(heart))
        self.wait(1)

        ytbottomlocale = -6
        joed = ImageMobject(filename_or_array="./joed.png").shift(UP*ytbottomlocale).scale(0.6)
        joed.generate_target()
        joed.target.shift(UP*(-ytbottomlocale+2.3))

        mango = ImageMobject(filename_or_array="./ilmango.png").shift(UP*ytbottomlocale).scale(0.6)
        mango.generate_target()
        mango.target.shift(UP*(-ytbottomlocale+0))

        verit = ImageMobject(filename_or_array="./verit.png").shift(UP*ytbottomlocale).scale(0.6)
        verit.generate_target()
        verit.target.shift(UP*(-ytbottomlocale+-2.3))


        analysis = ImageMobject(filename_or_array="./elem.jpg").scale(1.5).shift(UP*-3).shift(RIGHT*12)
        analysis.generate_target()
        analysis.target.shift(RIGHT*-12)

        self.play(MoveToTarget(joed),FadeIn(analysis))
        self.play(MoveToTarget(mango))
        self.play(MoveToTarget(verit))
        self.wait(1)

        ytvids = Group(joed,
                        mango,
                        verit)

        ytvids.generate_target()
        ytvids.target.shift(RIGHT*-14)

        self.play(MoveToTarget(ytvids),MoveToTarget(analysis))
        self.play(FadeOut(ytvids))
        self.wait(1)

        generaltheorem1 = Tex(r"\textbf{Theorem 8.} Take").scale(0.9).shift(RIGHT*-4.5).shift(UP*0.035)
        generaltheorem2 = Tex(r"a").scale(0.9).shift(RIGHT*-2.25)
        generaltheorem3 = Tex(r"function $f$ on $\mathbb{R}$ yadda yadda yadda \dots").scale(0.9).shift(RIGHT*2)

        bettertheorem2 = Tex(r"\textit{your}").scale(0.9).shift(RIGHT*-2).shift(UP*-0.05)
        bettertheorem2[0].set_color(e)

        generaltheorem1.generate_target()
        generaltheorem3.generate_target()
        generaltheorem1.target.shift(RIGHT*-0.05)
        generaltheorem3.target.shift(RIGHT*0.5)

        analysis.target.shift(RIGHT*-12)
        self.play(MoveToTarget(analysis))
        self.wait(1)
        self.play(Write(generaltheorem1))
        self.play(Write(generaltheorem2))
        self.play(Write(generaltheorem3))
        self.wait(1)
        self.play(MoveToTarget(generaltheorem1),MoveToTarget(generaltheorem3), Transform(generaltheorem2,bettertheorem2))
        self.wait(1)
        self.play(FadeOut(generaltheorem1),FadeOut(generaltheorem2),FadeOut(generaltheorem3))
        self.wait(1)

        back = Tex(r"Backburner problems").shift(UP*2.6)

        self.play(Write(back),run_time=0.9)
        self.wait(1)
        self.play(FadeOut(back))
        self.wait(1)

# Introducing My Problem
class Section3(Scene):
    def construct(self):
        self.camera.background_color = "#181818"

        # a = "#005F73" # 
        # b = "#0A9396" # 
        # c = "#94D2BD" # 
        # d = "#E9D8A6" # tile boarder
        # e = "#EE9B00" # 
        # f = "#CA6702" # 
        # g = "#BB3E03" # 
        # h = "#AE2012" # tile 
        # i = "#9B2226" # 

        hilight_color = "#C4A484"

        e = MathTex(r"\text{Introducing My Problem}").scale(1.5)

        self.wait(1)
        self.play(Write(e), run_time=1)
        self.wait(1)
        self.play(FadeOut(e))
        self.wait(1)

        square0 = Square(side_length=1,color=d)
        dsquare0 = Square(side_length=1,color=d)
        line0 = Line(start=square0.get_edge_center(DOWN),end=square0.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        vtile0 = VGroup(square0)
        vline0 = VGroup(line0,dsquare0)
        vtile0.shift(LEFT*5)
        vline0.shift(LEFT*5)
        
        square1 = Square(side_length=1,color=d)
        dsquare1 = Square(side_length=1,color=d)
        line1 = Line(start=square1.get_edge_center(DOWN),end=square1.get_edge_center(LEFT), stroke_width=8).set_color(i)
        vtile1 = VGroup(square1)
        vline1 = VGroup(line1,dsquare1)
        vtile1.shift(LEFT*3)
        vline1.shift(LEFT*3)

        square2 = Square(side_length=1,color=d)
        dsquare2 = Square(side_length=1,color=d)
        line2 = Line(start=square2.get_edge_center(LEFT),end=square2.get_edge_center(UP), stroke_width=8).set_color(i)
        vtile2 = VGroup(square2)
        vline2 = VGroup(line2,dsquare2)
        vtile2.shift(LEFT*1)
        vline2.shift(LEFT*1)

        square3 = Square(side_length=1,color=d)
        dsquare3 = Square(side_length=1,color=d)
        line3 = Line(start=square3.get_edge_center(UP),end=square3.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        vtile3 = VGroup(square3)
        vline3 = VGroup(line3,dsquare3)
        vtile3.shift(RIGHT*1)
        vline3.shift(RIGHT*1)

        square4 = Square(side_length=1,color=d)
        dsquare4 = Square(side_length=1,color=d)
        line4 = Line(start=square4.get_edge_center(DOWN),end=square4.get_edge_center(UP), stroke_width=8).set_color(i)
        vtile4 = VGroup(square4)
        vline4 = VGroup(line4,dsquare4)
        vtile4.shift(RIGHT*3)
        vline4.shift(RIGHT*3)

        square5 = Square(side_length=1,color=d)
        dsquare5 = Square(side_length=1,color=d)
        line5 = Line(start=square5.get_edge_center(LEFT),end=square5.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        vtile5 = VGroup(square5)
        vline5 = VGroup(line5,dsquare5)
        vtile5.shift(RIGHT*5)
        vline5.shift(RIGHT*5)


        
        self.play(Write(vtile0), Write(vtile1), Write(vtile2),Write(vtile3),Write(vtile4),Write(vtile5),  run_time=1)
        self.wait(1)
        self.play(Write(vline0), Write(vline1), Write(vline2),Write(vline3),Write(vline4),Write(vline5), run_time=1)
        self.wait(1)
        tile0 = vtile0 + vline0
        tile1 = vtile1 + vline1
        tile2 = vtile2 + vline2
        tile3 = vtile3 + vline3
        tile4 = vtile4 + vline4
        tile5 = vtile5 + vline5

        tile0.generate_target()
        tile0.target.shift(UP*2).shift(LEFT*0.5)
        
        tile1.generate_target()
        tile1.target.shift(LEFT*2.5)

        tile2.generate_target()
        tile2.target.shift(DOWN*2).shift(LEFT*4.5)

        tile3.generate_target()
        tile3.target.shift(DOWN*2).shift(LEFT*4.5)

        tile4.generate_target()
        tile4.target.shift(LEFT*6.5)

        tile5.generate_target()
        tile5.target.shift(UP*2).shift(LEFT*8.5)

        self.play(MoveToTarget(tile0), \
                MoveToTarget(tile1), \
                MoveToTarget(tile2), \
                MoveToTarget(tile3), \
                MoveToTarget(tile4), \
                MoveToTarget(tile5))

        grid = Rectangle(width=7, height=5, grid_xstep=1, grid_ystep=1,color=d)
        grid.shift(RIGHT*2)
        self.wait(1)
        self.play(FadeIn(grid))

        # tile copy and move
        def tcam(tilecode,shiftrightval=0,shiftupval=0):
            conversion_dict = {
                0:(tile0,0,0), 
                1:(tile1,0,2), 
                2:(tile2,0,4), 
                3:(tile3,2,4), 
                4:(tile4,2,2), 
                5:(tile5,2,0)
            }
            res = conversion_dict[tilecode]
            tile_copy = res[0].copy()
            tile_copy.generate_target()
            tile_copy.target.shift(RIGHT*(shiftrightval-res[1])).shift(UP*(shiftupval+res[2]))
            return tile_copy
        
        # tile copy and shift
        def tcas(tilecode,shiftrightval=0,shiftupval=0):
            conversion_dict = {
                0:(tile0,0,0), 
                1:(tile1,0,2), 
                2:(tile2,0,4), 
                3:(tile3,2,4), 
                4:(tile4,2,2), 
                5:(tile5,2,0)
            }
            res = conversion_dict[tilecode]
            tile_copy = res[0].copy()
            tile_copy.shift(RIGHT*(shiftrightval-res[1])).shift(UP*(shiftupval+res[2]))
            return tile_copy

        fillgridlst = [
            # row 1
            tcam(0,shiftrightval=4.5,shiftupval=0),
            tcam(0,shiftrightval=5.5,shiftupval=0),
            tcam(1,shiftrightval=6.5,shiftupval=0),
            tcam(5,shiftrightval=7.5,shiftupval=0),
            tcam(3,shiftrightval=8.5,shiftupval=0),
            tcam(4,shiftrightval=9.5,shiftupval=0),
            tcam(2,shiftrightval=10.5,shiftupval=0),
            # row 2
            tcam(0,shiftrightval=4.5,shiftupval=-1),
            tcam(2,shiftrightval=5.5,shiftupval=-1),
            tcam(4,shiftrightval=6.5,shiftupval=-1),
            tcam(3,shiftrightval=7.5,shiftupval=-1),
            tcam(4,shiftrightval=8.5,shiftupval=-1),
            tcam(4,shiftrightval=9.5,shiftupval=-1),
            tcam(1,shiftrightval=10.5,shiftupval=-1),
            # row 3
            tcam(4,shiftrightval=4.5,shiftupval=-2),
            tcam(1,shiftrightval=5.5,shiftupval=-2),
            tcam(1,shiftrightval=6.5,shiftupval=-2),
            tcam(5,shiftrightval=7.5,shiftupval=-2),
            tcam(4,shiftrightval=8.5,shiftupval=-2),
            tcam(5,shiftrightval=9.5,shiftupval=-2),
            tcam(3,shiftrightval=10.5,shiftupval=-2),
            # row 4
            tcam(4,shiftrightval=4.5,shiftupval=-3),
            tcam(5,shiftrightval=5.5,shiftupval=-3),
            tcam(5,shiftrightval=6.5,shiftupval=-3),
            tcam(2,shiftrightval=7.5,shiftupval=-3),
            tcam(1,shiftrightval=8.5,shiftupval=-3),
            tcam(0,shiftrightval=9.5,shiftupval=-3),
            tcam(2,shiftrightval=10.5,shiftupval=-3),
            # row 5
            tcam(0,shiftrightval=4.5,shiftupval=-4),
            tcam(2,shiftrightval=5.5,shiftupval=-4),
            tcam(0,shiftrightval=6.5,shiftupval=-4),
            tcam(0,shiftrightval=7.5,shiftupval=-4),
            tcam(5,shiftrightval=8.5,shiftupval=-4),
            tcam(4,shiftrightval=9.5,shiftupval=-4),
            tcam(3,shiftrightval=10.5,shiftupval=-4)
        ]
                    
        for j in fillgridlst: self.play(MoveToTarget(j),run_time=0.25)
        self.wait(1)

        vgrp = VGroup()
        for j in fillgridlst: vgrp += j

        fullgrid2 = [
            # row 1
            tcas(3,shiftrightval=4.5,shiftupval=0),
            tcas(4,shiftrightval=5.5,shiftupval=0),
            tcas(5,shiftrightval=6.5,shiftupval=0),
            tcas(2,shiftrightval=7.5,shiftupval=0),
            tcas(0,shiftrightval=8.5,shiftupval=0),
            tcas(0,shiftrightval=9.5,shiftupval=0),
            tcas(0,shiftrightval=10.5,shiftupval=0),
            # row 2
            tcas(0,shiftrightval=4.5,shiftupval=-1),
            tcas(3,shiftrightval=5.5,shiftupval=-1),
            tcas(4,shiftrightval=6.5,shiftupval=-1),
            tcas(5,shiftrightval=7.5,shiftupval=-1),
            tcas(5,shiftrightval=8.5,shiftupval=-1),
            tcas(2,shiftrightval=9.5,shiftupval=-1),
            tcas(3,shiftrightval=10.5,shiftupval=-1),
            # row 3
            tcas(2,shiftrightval=4.5,shiftupval=-2),
            tcas(2,shiftrightval=5.5,shiftupval=-2),
            tcas(3,shiftrightval=6.5,shiftupval=-2),
            tcas(0,shiftrightval=7.5,shiftupval=-2),
            tcas(1,shiftrightval=8.5,shiftupval=-2),
            tcas(4,shiftrightval=9.5,shiftupval=-2),
            tcas(5,shiftrightval=10.5,shiftupval=-2),
            # row 4
            tcas(2,shiftrightval=4.5,shiftupval=-3),
            tcas(3,shiftrightval=5.5,shiftupval=-3),
            tcas(5,shiftrightval=6.5,shiftupval=-3),
            tcas(4,shiftrightval=7.5,shiftupval=-3),
            tcas(5,shiftrightval=8.5,shiftupval=-3),
            tcas(5,shiftrightval=9.5,shiftupval=-3),
            tcas(0,shiftrightval=10.5,shiftupval=-3),
            # row 5
            tcas(2,shiftrightval=4.5,shiftupval=-4),
            tcas(2,shiftrightval=5.5,shiftupval=-4),
            tcas(1,shiftrightval=6.5,shiftupval=-4),
            tcas(0,shiftrightval=7.5,shiftupval=-4),
            tcas(1,shiftrightval=8.5,shiftupval=-4),
            tcas(1,shiftrightval=9.5,shiftupval=-4),
            tcas(3,shiftrightval=10.5,shiftupval=-4)
        ]

        vgrp2 = VGroup()
        for j in fullgrid2: vgrp2 += j
        
        self.play(FadeOut(vgrp))
        self.play(FadeIn(vgrp2))
        self.wait(1)

        vgrp2.generate_target()
        vgrp2.target.shift(UP*-1)

        grid.generate_target()
        grid.target.shift(UP*-1)

        mosaics_text = Tex(r"mosaics").shift(UP*2.1).shift(RIGHT*2)

        self.play(MoveToTarget(vgrp2),MoveToTarget(grid))
        self.wait(1)
        self.play(Write(mosaics_text))
        self.wait(1)
        vgrp2.target.shift(UP*1)
        grid.target.shift(UP*1)
        self.play(FadeOut(mosaics_text))
        self.play(MoveToTarget(vgrp2),MoveToTarget(grid))
        self.wait(1)


        grid3 = [
            # row 1
            tcas(0,shiftrightval=4.5,shiftupval=0),
            tcas(1,shiftrightval=5.5,shiftupval=0),
            tcas(5,shiftrightval=6.5,shiftupval=0),
            tcas(2,shiftrightval=7.5,shiftupval=0),
            tcas(3,shiftrightval=8.5,shiftupval=0),
            tcas(0,shiftrightval=9.5,shiftupval=0),
            tcas(1,shiftrightval=10.5,shiftupval=0),
            # row 2
            tcas(3,shiftrightval=4.5,shiftupval=-1),
            tcas(4,shiftrightval=5.5,shiftupval=-1),
            tcas(2,shiftrightval=6.5,shiftupval=-1),
            tcas(2,shiftrightval=7.5,shiftupval=-1),
            tcas(1,shiftrightval=10.5,shiftupval=-1),
            # row 3
            tcas(3,shiftrightval=4.5,shiftupval=-2),
            tcas(5,shiftrightval=5.5,shiftupval=-2),
            tcas(2,shiftrightval=6.5,shiftupval=-2),
            tcas(4,shiftrightval=7.5,shiftupval=-2),
            tcas(1,shiftrightval=10.5,shiftupval=-2),
            # row 4
            tcas(1,shiftrightval=4.5,shiftupval=-3),
            tcas(1,shiftrightval=5.5,shiftupval=-3),
            tcas(1,shiftrightval=6.5,shiftupval=-3),
            tcas(0,shiftrightval=7.5,shiftupval=-3),
            tcas(3,shiftrightval=10.5,shiftupval=-3),
            # row 5
            tcas(3,shiftrightval=4.5,shiftupval=-4),
            tcas(0,shiftrightval=5.5,shiftupval=-4),
            tcas(1,shiftrightval=6.5,shiftupval=-4),
            tcas(0,shiftrightval=7.5,shiftupval=-4),
            
            tcas(3,shiftrightval=10.5,shiftupval=-4)  
        ]

        sap3 = [
            tcas(0,shiftrightval=8.5,shiftupval=-1),
            tcas(1,shiftrightval=9.5,shiftupval=-1),
            tcas(4,shiftrightval=8.5,shiftupval=-2),
            tcas(4,shiftrightval=9.5,shiftupval=-2),
            tcas(4,shiftrightval=8.5,shiftupval=-3),
            tcas(4,shiftrightval=9.5,shiftupval=-3),
            tcas(3,shiftrightval=8.5,shiftupval=-4),
            tcas(2,shiftrightval=9.5,shiftupval=-4)
        ]

        vgrp3 = VGroup()
        for j in grid3: vgrp3 += j

        vsap3 = VGroup()
        for j in sap3: vsap3 += j

        ssquare0 = Square(side_length=1, fill_color=hilight_color, fill_opacity=0.8, color=d)
        sline0 = Line(start=ssquare0.get_edge_center(DOWN),end=ssquare0.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        dssquare0 = Square(side_length=1,color=d)
        ssquare1 = Square(side_length=1, fill_color=hilight_color, fill_opacity=0.8, color=d)
        sline1 = Line(start=ssquare1.get_edge_center(DOWN),end=ssquare1.get_edge_center(LEFT), stroke_width=8).set_color(i)
        dssquare1 = Square(side_length=1,color=d)
        ssquare2 = Square(side_length=1, fill_color=hilight_color, fill_opacity=0.8, color=d)
        sline2 = Line(start=ssquare2.get_edge_center(LEFT),end=ssquare2.get_edge_center(UP), stroke_width=8).set_color(i)
        dssquare2 = Square(side_length=1,color=d)
        ssquare3 = Square(side_length=1, fill_color=hilight_color, fill_opacity=0.8, color=d)
        sline3 = Line(start=ssquare3.get_edge_center(UP),end=ssquare3.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        dssquare3 = Square(side_length=1,color=d)
        ssquare4 = Square(side_length=1, fill_color=hilight_color, fill_opacity=0.8, color=d)
        sline4 = Line(start=ssquare4.get_edge_center(DOWN),end=ssquare4.get_edge_center(UP), stroke_width=8).set_color(i)
        dssquare4 = Square(side_length=1,color=d)
        ssquare5 = Square(side_length=1, fill_color=hilight_color, fill_opacity=0.8, color=d)
        sline5 = Line(start=ssquare5.get_edge_center(LEFT),end=ssquare5.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        dssquare5 = Square(side_length=1,color=d)

        stile0 = VGroup(ssquare0,sline0,dssquare0)
        stile1 = VGroup(ssquare1,sline1,dssquare1)
        stile2 = VGroup(ssquare2,sline2,dssquare2)
        stile3 = VGroup(ssquare3,sline3,dssquare3)
        stile4 = VGroup(ssquare4,sline4,dssquare4)
        stile5 = VGroup(ssquare5,sline5,dssquare5)

        cstile0 = stile0.copy()
        cstile0.shift(RIGHT*3).shift(UP*1)

        cstile1 = stile1.copy()
        cstile1.shift(RIGHT*4).shift(UP*1)

        cstile4 = stile4.copy()
        cstile4.shift(RIGHT*3)

        ccstile4 = stile4.copy()
        ccstile4.shift(RIGHT*4)

        cccstile4 = stile4.copy()
        cccstile4.shift(RIGHT*3).shift(UP*-1)

        ccccstile4 = stile4.copy()
        ccccstile4.shift(RIGHT*4).shift(UP*-1)

        cstile3 = stile3.copy()
        cstile3.shift(RIGHT*3).shift(UP*-2)

        cstile2 = stile2.copy()
        cstile2.shift(RIGHT*4).shift(UP*-2)

        shsap = VGroup()
        shsap += cstile0 + cstile1 + cstile4 + ccstile4 + cccstile4 + ccccstile4 + cstile3 + cstile2

        self.play(FadeOut(vgrp2))
        self.wait(1)
        self.play(FadeIn(vgrp3),FadeIn(vsap3))
        self.wait(1)
        self.play(FadeIn(shsap))
        # self.wait(1)
        self.play(FadeOut(shsap))
        self.wait(1)
        self.play(FadeOut(vgrp3,vsap3))
        
        grid4 = [
            # row 1
            tcas(3,shiftrightval=4.5,shiftupval=0),
            tcas(0,shiftrightval=9.5,shiftupval=0),
            tcas(0,shiftrightval=10.5,shiftupval=0),
            # row 2
            
            tcas(4,shiftrightval=6.5,shiftupval=-1),
            tcas(5,shiftrightval=7.5,shiftupval=-1),
            tcas(3,shiftrightval=10.5,shiftupval=-1),
            # row 3
            
            tcas(5,shiftrightval=7.5,shiftupval=-2),
            tcas(1,shiftrightval=8.5,shiftupval=-2),
            tcas(5,shiftrightval=10.5,shiftupval=-2),
            # row 4
            tcas(2,shiftrightval=4.5,shiftupval=-3),
            tcas(3,shiftrightval=5.5,shiftupval=-3),
            tcas(0,shiftrightval=10.5,shiftupval=-3),
            # row 5
            tcas(5,shiftrightval=4.5,shiftupval=-4),
            tcas(2,shiftrightval=5.5,shiftupval=-4),
            tcas(1,shiftrightval=6.5,shiftupval=-4),
            tcas(0,shiftrightval=7.5,shiftupval=-4),
            tcas(1,shiftrightval=8.5,shiftupval=-4),
            tcas(1,shiftrightval=9.5,shiftupval=-4),
            tcas(3,shiftrightval=10.5,shiftupval=-4)
        ]

        sap4 = [
            tcas(0,shiftrightval=5.5,shiftupval=0), #
            tcas(5,shiftrightval=6.5,shiftupval=0), #
            tcas(5,shiftrightval=7.5,shiftupval=0), #
            tcas(1,shiftrightval=8.5,shiftupval=0), #

            tcas(0,shiftrightval=4.5,shiftupval=-1), #
            tcas(2,shiftrightval=5.5,shiftupval=-1), #
            tcas(3,shiftrightval=8.5,shiftupval=-1), #
            tcas(1,shiftrightval=9.5,shiftupval=-1), #

            tcas(3,shiftrightval=4.5,shiftupval=-2), #
            tcas(5,shiftrightval=5.5,shiftupval=-2), #
            tcas(1,shiftrightval=6.5,shiftupval=-2), #
            tcas(4,shiftrightval=9.5,shiftupval=-2), #

            tcas(3,shiftrightval=6.5,shiftupval=-3), #
            tcas(5,shiftrightval=7.5,shiftupval=-3), #
            tcas(5,shiftrightval=8.5,shiftupval=-3), #
            tcas(2,shiftrightval=9.5,shiftupval=-3), #
        ]

        ztile0 = stile0.copy()
        ztile0.shift(RIGHT*0).shift(UP*2)
        ztile5 = stile5.copy()
        ztile5.shift(RIGHT*1).shift(UP*2)
        zztile5 = stile5.copy()
        zztile5.shift(RIGHT*2).shift(UP*2)
        ztile1 = stile1.copy()
        ztile1.shift(RIGHT*3).shift(UP*2)
        
        zztile0 = stile0.copy()
        zztile0.shift(RIGHT*-1).shift(UP*1)
        ztile2 = stile2.copy()
        ztile2.shift(RIGHT*0).shift(UP*1)
        ztile3 = stile3.copy()
        ztile3.shift(RIGHT*3).shift(UP*1)
        zztile1 = stile1.copy()
        zztile1.shift(RIGHT*4).shift(UP*1)

        zztile3 = stile3.copy()
        zztile3.shift(RIGHT*-1).shift(UP*0)
        zzztile5 = stile5.copy()
        zzztile5.shift(RIGHT*0).shift(UP*0)
        zzztile1 = stile1.copy()
        zzztile1.shift(RIGHT*1).shift(UP*0)
        ztile4 = stile4.copy()
        ztile4.shift(RIGHT*4).shift(UP*0)

        zzztile3 = stile3.copy()
        zzztile3.shift(RIGHT*1).shift(UP*-1)
        zzzztile5 = stile5.copy()
        zzzztile5.shift(RIGHT*2).shift(UP*-1)
        zzzzztile5 = stile5.copy()
        zzzzztile5.shift(RIGHT*3).shift(UP*-1)
        zztile2 = stile2.copy()
        zztile2.shift(RIGHT*4).shift(UP*-1)

        vgrp4 = VGroup()
        for j in grid4: vgrp4 += j

        vsap4 = VGroup()
        for j in sap4: vsap4 += j

        

        shsap4 = VGroup()
        shsap4 += ztile0 + ztile5 + zztile5 + ztile1 + zztile0 + ztile2 + \
            ztile3 + zztile1 + zztile3 + zzztile5 + zzztile1 + ztile4 + zzztile3 + \
            zzzztile5 + zzzzztile5 + zztile2

        self.wait(1)
        self.play(FadeIn(vgrp4), FadeIn(vsap4))
        self.wait(1)
        self.play(FadeIn(shsap4))
        # self.wait(1)
        # self.play(FadeOut(vgrp4), FadeOut(vsap4), FadeOut(shsap4))
        self.play(FadeOut(shsap4))
        self.wait(1)
        self.play(FadeOut(vgrp4), \
                  FadeOut(vsap4), \
                  FadeOut(grid), \
                  FadeOut(tile0), \
                  FadeOut(tile1), \
                  FadeOut(tile2), \
                  FadeOut(tile3), \
                  FadeOut(tile4), \
                  FadeOut(tile5))
        
        finalquestions = Tex(r"What is the probability that when you make an $n$ by $m$ mosaic, \\ you get at least one connected shape?").scale(0.8)

        self.play(Write(finalquestions))
        self.wait(1)
        self.play(FadeOut(finalquestions))
        self.wait(1)

# My Initial Work
class Section4(Scene):
    def construct(self):
        self.camera.background_color = "#181818"

        title = Tex(r"My Initial Work").scale(1.5)

        self.wait(1)
        self.play(Write(title),run_time=1)
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        e1 = Tex(r"Let's have $p_{n,m}$ be the probability that we get \\ at least one connected shape in an $n \times m$ mosaic.")
        e1[0][9].set_color(e)
        e1.scale(0.8)

        e2 = Tex(r"$p_{n,m} = \frac{\text{\# of mosaics with connected shapes}}{\text{\# of mosaics}}$")
        e2[0][0].set_color(e)
        e2.scale(1.2).shift(UP*-1)


        e2c = Tex(r"$p_{n,m} = \frac{t_{n,m}}{6^{nm}}$")
        e2c[0][0].set_color(e)
        e2c[0][5].set_color(a)
        e2c.scale(1.2).shift(UP*-1)

        square0 = Square(side_length=1,color=d)
        line0 = Line(start=square0.get_edge_center(DOWN),end=square0.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        tile0 = VGroup(square0,line0,square0)
        tile0.shift(LEFT*5).shift(UP*2).shift(LEFT*0.5)

        square1 = Square(side_length=1,color=d)
        line1 = Line(start=square1.get_edge_center(DOWN),end=square1.get_edge_center(LEFT), stroke_width=8).set_color(i)
        tile1 = VGroup(square1,line1,square1)
        tile1.shift(LEFT*3).shift(LEFT*2.5)

        square2 = Square(side_length=1,color=d)
        line2 = Line(start=square2.get_edge_center(LEFT),end=square2.get_edge_center(UP), stroke_width=8).set_color(i)
        tile2 = VGroup(square2,line2,square2)
        tile2.shift(LEFT*1).shift(DOWN*2).shift(LEFT*4.5)

        square3 = Square(side_length=1,color=d)
        line3 = Line(start=square3.get_edge_center(UP),end=square3.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        tile3 = VGroup(square3,line3,square3)
        tile3.shift(RIGHT*1).shift(DOWN*2).shift(LEFT*4.5)

        square4 = Square(side_length=1,color=d)
        line4 = Line(start=square4.get_edge_center(DOWN),end=square4.get_edge_center(UP), stroke_width=8).set_color(i)
        tile4 = VGroup(square4,line4,square4)
        tile4.shift(RIGHT*3).shift(LEFT*6.5)

        square5 = Square(side_length=1,color=d)
        line5 = Line(start=square5.get_edge_center(LEFT),end=square5.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        tile5 = VGroup(square5,line5,square5)
        tile5.shift(RIGHT*5).shift(UP*2).shift(LEFT*8.5)

        grid = Rectangle(width=7, height=5, grid_xstep=1, grid_ystep=1,color=d)
        grid.shift(RIGHT*2)

        self.wait(1)
        self.play(Write(e1),run_time=1)

        e1.generate_target()
        e1.target.shift(UP*1)

        self.wait(1)
        self.play(MoveToTarget(e1))
        self.play(Write(e2),run_time=1)
        self.wait(1)
        self.play(ReplacementTransform(e2,e2c))
        self.wait(1)

        self.play(FadeOut(e1),FadeOut(e2c))
        self.wait(0.8)

        # n_label = Tex(r"n").shift(UP*).shift(RIGHT*)
        # m_label = Tex(r"m").shift(UP*).shift(RIGHT*)

        self.play(FadeIn(tile0),FadeIn(tile1),FadeIn(tile2),FadeIn(tile3),FadeIn(tile4),FadeIn(tile5),FadeIn(grid))
        self.wait(1)
        self.play(Indicate(grid))
        self.wait(1)

        # tile copy and move
        def tcam(tilecode,shiftrightval=0,shiftupval=0):
            conversion_dict = {
                0:(tile0,0,0), 
                1:(tile1,0,2), 
                2:(tile2,0,4), 
                3:(tile3,2,4), 
                4:(tile4,2,2), 
                5:(tile5,2,0)
            }
            res = conversion_dict[tilecode]
            tile_copy = res[0].copy()
            tile_copy.generate_target()
            tile_copy.target.shift(RIGHT*(shiftrightval-res[1])).shift(UP*(shiftupval+res[2]))
            return tile_copy
        
        trysquare = [
            tcam(0,shiftrightval=4.5,shiftupval=0),
            tcam(1,shiftrightval=4.5,shiftupval=0),
            tcam(2,shiftrightval=4.5,shiftupval=0),
            tcam(5,shiftrightval=4.5,shiftupval=0),
            tcam(4,shiftrightval=4.5,shiftupval=0),
            tcam(3,shiftrightval=4.5,shiftupval=0)
        ]

        for j in trysquare: 
            self.play(MoveToTarget(j),run_time=0.25)
            self.play(FadeOut(j),run_time=0.1)
        
        self.wait(1)
        self.play(FadeOut(tile0),FadeOut(tile1),FadeOut(tile2),FadeOut(tile3),FadeOut(tile4),FadeOut(tile5),FadeOut(grid))
        self.wait(1)

        explantex = Tex(r"We will focus on $t_{n,m}$ for the rest of this video.")
        explantex[0][13].set_color(a)
        self.play(Write(explantex),run_time=1)
        self.wait(1)
        self.play(FadeOut(explantex))
        self.wait(1)

        onebyone = Rectangle(width=1,height=1,grid_xstep=1,grid_ystep=1).set_color(d)
        onebyone.z_index = 1

        self.play(Write(onebyone))
        

        line0 = Line(start=onebyone.get_edge_center(DOWN),end=onebyone.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        line0.z_index = 0
        self.play(Create(line0),run_time=0.5)

        line1 = Line(start=onebyone.get_edge_center(DOWN),end=onebyone.get_edge_center(LEFT), stroke_width=8).set_color(i)
        line1.z_index = 0
        self.play(Uncreate(line0),Create(line1), run_time=0.5)

        line2 = Line(start=onebyone.get_edge_center(LEFT),end=onebyone.get_edge_center(UP), stroke_width=8).set_color(i)
        line2.z_index = 0
        self.play(Uncreate(line1),Create(line2), run_time=0.5)

        line3 = Line(start=onebyone.get_edge_center(UP),end=onebyone.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        line3.z_index = 0
        self.play(Uncreate(line2),Create(line3), run_time=0.5)

        line4 = Line(start=onebyone.get_edge_center(DOWN),end=onebyone.get_edge_center(UP), stroke_width=8).set_color(i)
        line4.z_index = 0
        self.play(Uncreate(line3),Create(line4), run_time=0.5)

        line5 = Line(start=onebyone.get_edge_center(LEFT),end=onebyone.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        line5.z_index = 0
        self.play(Uncreate(line4),Create(line5), run_time=0.5)
        self.play(Uncreate(line5),run_time=0.5)

        self.wait(1)
        labelonebyone = Tex(r"$t_{1,1} = 0$").shift(DOWN*1.3)
        labelonebyn = Tex(r"$t_{n,1} = 0$").shift(DOWN*1.3)
        self.play(FadeIn(labelonebyone))
        self.wait(1)


        onebytwo = Rectangle(width=2,height=1,grid_xstep=1,grid_ystep=1,color=d)
        onebythree = Rectangle(width=3,height=1,grid_xstep=1,grid_ystep=1,color=d)
        onebyfour = Rectangle(width=4,height=1,grid_xstep=1,grid_ystep=1,color=d)
        onebyfive = Rectangle(width=5,height=1,grid_xstep=1,grid_ystep=1,color=d)
        onebysix = Rectangle(width=6,height=1,grid_xstep=1,grid_ystep=1,color=d)
        onebyseven = Rectangle(width=7,height=1,grid_xstep=1,grid_ystep=1,color=d)

        
        

        square0 = Square(side_length=1,color=d)
        line0 = Line(start=square0.get_edge_center(DOWN),end=square0.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        dsquare0 = Square(side_length=1,color=d)
        tile0 = VGroup(square0,line0,dsquare0)

        square1 = Square(side_length=1,color=d)
        line1 = Line(start=square1.get_edge_center(DOWN),end=square1.get_edge_center(LEFT), stroke_width=8).set_color(i)
        dsquare1 = Square(side_length=1,color=d)
        tile1 = VGroup(square1,line1,dsquare1)

        square2 = Square(side_length=1,color=d)
        line2 = Line(start=square2.get_edge_center(LEFT),end=square2.get_edge_center(UP), stroke_width=8).set_color(i)
        dsquare2 = Square(side_length=1,color=d)
        tile2 = VGroup(square2,line2,dsquare2)

        square3 = Square(side_length=1,color=d)
        line3 = Line(start=square3.get_edge_center(UP),end=square3.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        dsquare3 = Square(side_length=1,color=d)
        tile3 = VGroup(square3,line3,dsquare3)

        square4 = Square(side_length=1,color=d)
        line4 = Line(start=square4.get_edge_center(DOWN),end=square4.get_edge_center(UP), stroke_width=8).set_color(i)
        dsquare4 = Square(side_length=1,color=d)
        tile4 = VGroup(square4,line4,dsquare4)

        square5 = Square(side_length=1,color=d)
        line5 = Line(start=square5.get_edge_center(LEFT),end=square5.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        dsquare5 = Square(side_length=1,color=d)
        tile5 = VGroup(square5,line5,dsquare5)

        self.play(TransformMatchingTex(labelonebyone, labelonebyn),ReplacementTransform(onebyone,onebytwo),run_time=0.5)
        self.play(ReplacementTransform(onebytwo,onebythree),run_time=0.5)
        self.play(ReplacementTransform(onebythree,onebyfour),run_time=0.5)
        self.play(ReplacementTransform(onebyfour,onebyfive),run_time=0.5)
        self.play(ReplacementTransform(onebyfive,onebysix),run_time=0.5)
        self.play(ReplacementTransform(onebysix,onebyseven),run_time=0.5)
        self.wait(1)

        rawr = VGroup(tile5.copy().shift(RIGHT*-3) , \
                        tile4.copy().shift(RIGHT*-2), \
                        tile4.copy().shift(RIGHT*-1), \
                        tile0.copy().shift(RIGHT*0), \
                        tile2.copy().shift(RIGHT*1), \
                        tile1.copy().shift(RIGHT*2), \
                        tile1.copy().shift(RIGHT*3))
        
        self.play(FadeIn(rawr))
        self.wait(1)
        self.play(FadeOut(rawr))
        self.wait(1)

        twobytwo = Rectangle(width=2,height=2,grid_xstep=1,grid_ystep=1,color=d)

        labeltwobytwo = Tex(r"$t_{2,2} = 1$").shift(DOWN*1.6)

        self.play(ReplacementTransform(onebyseven,twobytwo), FadeOut(labelonebyn))
        self.wait(1)

        sap2x2 = tile0.copy().shift(UP*0.5).shift(RIGHT*-0.5) + tile1.copy().shift(UP*0.5).shift(RIGHT*0.5) + \
            tile2.copy().shift(UP*-0.5).shift(RIGHT*0.5) + tile3.copy().shift(UP*-0.5).shift(RIGHT*-0.5)
            
        
        self.play(FadeIn(sap2x2))
        self.wait(1)
        self.play(FadeIn(labeltwobytwo))
        self.wait(1)
        self.play(FadeOut(labeltwobytwo,sap2x2))
        self.wait(1)

        twobythree = Rectangle(width=2,height=3,grid_xstep=1,grid_ystep=1,color=d)
        twobythree.z_index = 1

        self.play(ReplacementTransform(twobytwo,twobythree))
        self.wait(1)
        
        twobythreeleft = twobythree.copy()
        twobythreeleft.generate_target()
        twobythreeleft.z_index = 2
        twobythreeleft.target.shift(LEFT*3.5)
        twobythreeright = twobythree.copy()
        twobythreeright.generate_target()
        twobythreeright.z_index = 3
        twobythreeright.target.shift(RIGHT*3.5)
        self.play(MoveToTarget(twobythreeleft), MoveToTarget(twobythreeright))

        sap2x3_1 = tile0.copy().shift(UP*1).shift(RIGHT*-4) +\
                    tile1.copy().shift(UP*1).shift(RIGHT*-3) +\
                    tile4.copy().shift(UP*0).shift(RIGHT*-4) +\
                    tile4.copy().shift(UP*0).shift(RIGHT*-3) +\
                    tile3.copy().shift(UP*-1).shift(RIGHT*-4) +\
                    tile2.copy().shift(UP*-1).shift(RIGHT*-3)
        
        twobythreelabel_1 = Tex(r"$1$").shift(UP*-2).shift(RIGHT*-3.5)

        self.wait(1)
        self.play(FadeIn(sap2x3_1))
        self.wait(1)
        self.play(FadeIn(twobythreelabel_1))
        self.wait(1)

        sap2x3_2 = tile0.copy().shift(UP*1).shift(RIGHT*-0.5) +\
                    tile1.copy().shift(UP*1).shift(RIGHT*0.5) +\
                    tile3.copy().shift(UP*0).shift(RIGHT*-0.5) +\
                    tile2.copy().shift(UP*0).shift(RIGHT*0.5)
        
        twobythreelabel_2 = Tex(r"$6^2$").shift(UP*-1.97)
        
        self.wait(1)
        self.play(FadeIn(sap2x3_2))
        self.wait(1)

        base1  = Rectangle(width=1,height=1,grid_xstep=1,grid_ystep=1,color=d).shift(RIGHT*-0.5).shift(UP*-1)
        zline0 = VGroup(Line(start=base1.get_edge_center(DOWN),end=base1.get_edge_center(RIGHT), stroke_width=8).set_color(i), base1.copy())
        zline1 = VGroup(Line(start=base1.get_edge_center(DOWN),end=base1.get_edge_center(LEFT), stroke_width=8).set_color(i), base1.copy())
        zline2 = VGroup(Line(start=base1.get_edge_center(LEFT),end=base1.get_edge_center(UP), stroke_width=8).set_color(i), base1.copy())
        zline3 = VGroup(Line(start=base1.get_edge_center(UP),end=base1.get_edge_center(RIGHT), stroke_width=8).set_color(i), base1.copy())
        zline4 = VGroup(Line(start=base1.get_edge_center(DOWN),end=base1.get_edge_center(UP), stroke_width=8).set_color(i), base1.copy())
        zline5 = VGroup(Line(start=base1.get_edge_center(LEFT),end=base1.get_edge_center(RIGHT), stroke_width=8).set_color(i), base1.copy())

        base2  = Rectangle(width=1,height=1,grid_xstep=1,grid_ystep=1,color=d).shift(RIGHT*0.5).shift(UP*-1)
        uhzline0 = VGroup(Line(start=base2.get_edge_center(DOWN),end=base2.get_edge_center(RIGHT), stroke_width=8).set_color(i), base2.copy())
        uhzline1 = VGroup(Line(start=base2.get_edge_center(DOWN),end=base2.get_edge_center(LEFT), stroke_width=8).set_color(i), base2.copy())
        uhzline2 = VGroup(Line(start=base2.get_edge_center(LEFT),end=base2.get_edge_center(UP), stroke_width=8).set_color(i), base2.copy())
        uhzline3 = VGroup(Line(start=base2.get_edge_center(UP),end=base2.get_edge_center(RIGHT), stroke_width=8).set_color(i), base2.copy())
        uhzline4 = VGroup(Line(start=base2.get_edge_center(DOWN),end=base2.get_edge_center(UP), stroke_width=8).set_color(i), base2.copy())
        uhzline5 = VGroup(Line(start=base2.get_edge_center(LEFT),end=base2.get_edge_center(RIGHT), stroke_width=8).set_color(i), base2.copy())

        

        self.play(Create(zline0),Create(uhzline5),run_time=0.5)
        self.play(Uncreate(zline0),Create(zline1),Uncreate(uhzline5),Create(uhzline4),run_time=0.5)
        self.play(Uncreate(zline1),Create(zline2),Uncreate(uhzline4),Create(uhzline3),run_time=0.5)
        self.play(Uncreate(zline2),Create(zline3),Uncreate(uhzline3),Create(uhzline2),run_time=0.5)
        self.play(Uncreate(zline3),Create(zline4),Uncreate(uhzline2),Create(uhzline1),run_time=0.5)
        self.play(Uncreate(zline4),Create(zline5),Uncreate(uhzline1),Create(uhzline0),run_time=0.5)
        self.play(Uncreate(zline5),Uncreate(uhzline0),run_time=0.5)

        self.play(FadeIn(twobythreelabel_2))
        self.wait(1)

        sap2x3_3 = tile0.copy().shift(UP*0).shift(RIGHT*3) +\
                    tile1.copy().shift(UP*0).shift(RIGHT*4) +\
                    tile3.copy().shift(UP*-1).shift(RIGHT*3) +\
                    tile2.copy().shift(UP*-1).shift(RIGHT*4)

        twobythreelabel_3 = Tex(r"$6^2$").shift(UP*-1.97).shift(RIGHT*3.5)

        self.wait(1)
        self.play(FadeIn(sap2x3_3))
        self.wait(1)

        base1.shift(UP*2).shift(RIGHT*3.5)
        base2.shift(UP*2).shift(RIGHT*3.5)

        czline0 = VGroup(Line(start=base1.get_edge_center(DOWN),end=base1.get_edge_center(RIGHT), stroke_width=8).set_color(i), base1.copy())
        czline1 = VGroup(Line(start=base1.get_edge_center(DOWN),end=base1.get_edge_center(LEFT), stroke_width=8).set_color(i), base1.copy())
        czline2 = VGroup(Line(start=base1.get_edge_center(LEFT),end=base1.get_edge_center(UP), stroke_width=8).set_color(i), base1.copy())
        czline3 = VGroup(Line(start=base1.get_edge_center(UP),end=base1.get_edge_center(RIGHT), stroke_width=8).set_color(i), base1.copy())
        czline4 = VGroup(Line(start=base1.get_edge_center(DOWN),end=base1.get_edge_center(UP), stroke_width=8).set_color(i), base1.copy())
        czline5 = VGroup(Line(start=base1.get_edge_center(LEFT),end=base1.get_edge_center(RIGHT), stroke_width=8).set_color(i), base1.copy())

        cczline0 = VGroup(Line(start=base2.get_edge_center(DOWN),end=base2.get_edge_center(RIGHT), stroke_width=8).set_color(i), base2.copy())
        cczline1 = VGroup(Line(start=base2.get_edge_center(DOWN),end=base2.get_edge_center(LEFT), stroke_width=8).set_color(i), base2.copy())
        cczline2 = VGroup(Line(start=base2.get_edge_center(LEFT),end=base2.get_edge_center(UP), stroke_width=8).set_color(i), base2.copy())
        cczline3 = VGroup(Line(start=base2.get_edge_center(UP),end=base2.get_edge_center(RIGHT), stroke_width=8).set_color(i), base2.copy())
        cczline4 = VGroup(Line(start=base2.get_edge_center(DOWN),end=base2.get_edge_center(UP), stroke_width=8).set_color(i), base2.copy())
        cczline5 = VGroup(Line(start=base2.get_edge_center(LEFT),end=base2.get_edge_center(RIGHT), stroke_width=8).set_color(i), base2.copy())

        self.play(Create(czline0),Create(cczline5),run_time=0.5)
        self.play(Uncreate(czline0),Create(czline1),Uncreate(cczline5),Create(cczline4),run_time=0.5)
        self.play(Uncreate(czline1),Create(czline2),Uncreate(cczline4),Create(cczline3),run_time=0.5)
        self.play(Uncreate(czline2),Create(czline3),Uncreate(cczline3),Create(cczline2),run_time=0.5)
        self.play(Uncreate(czline3),Create(czline4),Uncreate(cczline2),Create(cczline1),run_time=0.5)
        self.play(Uncreate(czline4),Create(czline5),Uncreate(cczline1),Create(cczline0),run_time=0.5)
        self.play(Uncreate(czline5),Uncreate(cczline0),run_time=0.5)

        self.play(FadeIn(twobythreelabel_3))
        self.wait(1)

        twobythreelabel_1.generate_target()
        twobythreelabel_1.target.shift(RIGHT*2.5)
        twobythreelabel_3.generate_target()
        twobythreelabel_3.target.shift(RIGHT*-2.5)

        plus = Tex(r"$+$")
        cplus = plus.copy()
        plus.shift(UP*-2).shift(RIGHT*-0.55)
        cplus.shift(UP*-2).shift(RIGHT*0.5)

        equals = Tex(r"$t_{2,3}=$")
        cequals = Tex(r"$=73$")
        equals.shift(UP*-2.03).shift(RIGHT*-1.9)
        cequals.shift(UP*-1.95).shift(RIGHT*1.9)

        self.play(MoveToTarget(twobythreelabel_1),MoveToTarget(twobythreelabel_3), FadeIn(plus), FadeIn(cplus))
        self.wait(1)
        self.play(FadeIn(equals))
        self.wait(1)
        self.play(FadeIn(cequals))
        self.wait(1)

        twobythreealllabels = VGroup(equals) + \
                    VGroup(cequals) + \
                    VGroup(plus) + \
                    VGroup(cplus) + \
                    VGroup(twobythreelabel_1) + \
                    VGroup(twobythreelabel_2) + \
                    VGroup(twobythreelabel_3)

        self.play(FadeOut(twobythreealllabels))
        self.wait(1)

        square6 = Square(side_length=1,color=d)
        dot = Dot().set_color(i)
        opentile = VGroup(square6,dot,square6.copy())
        tile6 = opentile.copy()

        twobythreeopens = VGroup(opentile.copy().shift(UP*-1).shift(RIGHT*-0.5)) + \
                        VGroup(opentile.copy().shift(UP*-1).shift(RIGHT*0.5)) + \
                        VGroup(opentile.copy().shift(UP*1).shift(RIGHT*3)) + \
                        VGroup(opentile.copy().shift(UP*1).shift(RIGHT*4))
        
        openstext = Tex(r"an open").shift(UP*-2)
        
        self.play(FadeIn(twobythreeopens))
        self.play(Write(openstext),run_time=1)
        self.wait(1)

        twobythreeall = VGroup(sap2x3_1) + \
                        VGroup(sap2x3_2) + \
                        VGroup(sap2x3_3) + \
                        VGroup(twobythree) + \
                        VGroup(twobythreeleft) + \
                        VGroup(twobythreeright) + \
                        VGroup(twobythreeopens)
        
        self.play(FadeOut(openstext),FadeOut(twobythreeall))
        self.wait(1)

        twobyfour = Rectangle(width=2,height=4,grid_xstep=1,grid_ystep=1,color=d).scale(0.8)

        twobyfour_1 = twobyfour.copy()
        twobyfour_2 = twobyfour.copy()
        twobyfour_3 = twobyfour.copy()
        twobyfour_4 = twobyfour.copy()
        twobyfour_5 = twobyfour.copy()
        twobyfour_6 = twobyfour.copy()

        twobyfour_1.generate_target()
        twobyfour_1.target.shift(LEFT*2)

        twobyfour_2.generate_target()
        twobyfour_2.target.shift(LEFT*4)

        twobyfour_3.generate_target()
        twobyfour_3.target.shift(LEFT*6)

        twobyfour_4.generate_target()
        twobyfour_4.target.shift(LEFT*-2)

        twobyfour_5.generate_target()
        twobyfour_5.target.shift(LEFT*-4)

        twobyfour_6.generate_target()
        twobyfour_6.target.shift(LEFT*-6)

        self.play(Create(twobyfour))
        self.wait(1)
        self.play(MoveToTarget(twobyfour_1), \
                  MoveToTarget(twobyfour_2), \
                  MoveToTarget(twobyfour_3), \
                  MoveToTarget(twobyfour_4), \
                  MoveToTarget(twobyfour_5), \
                  MoveToTarget(twobyfour_6))
        self.wait(1)

        twobyfoursap_1=(VGroup(tile0.copy().shift(RIGHT*-6.5).shift(UP*1.5)) + \
                        VGroup(tile1.copy().shift(RIGHT*-5.5).shift(UP*1.5)) + \
                        VGroup(tile4.copy().shift(RIGHT*-6.5).shift(UP*0.5)) + \
                        VGroup(tile4.copy().shift(RIGHT*-5.5).shift(UP*0.5)) + \
                        VGroup(tile4.copy().shift(RIGHT*-6.5).shift(UP*-0.5)) + \
                        VGroup(tile4.copy().shift(RIGHT*-5.5).shift(UP*-0.5)) + \
                        VGroup(tile3.copy().shift(RIGHT*-6.5).shift(UP*-1.5)) + \
                        VGroup(tile2.copy().shift(RIGHT*-5.5).shift(UP*-1.5))).scale(0.8)

        twobyfoursap_2=(VGroup(tile0.copy().shift(RIGHT*-4.5).shift(UP*1.5)) + \
                        VGroup(tile1.copy().shift(RIGHT*-3.5).shift(UP*1.5)) + \
                        VGroup(tile4.copy().shift(RIGHT*-4.5).shift(UP*0.5)) + \
                        VGroup(tile4.copy().shift(RIGHT*-3.5).shift(UP*0.5)) + \
                        VGroup(tile3.copy().shift(RIGHT*-4.5).shift(UP*-0.5)) + \
                        VGroup(tile2.copy().shift(RIGHT*-3.5).shift(UP*-0.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*-4.5).shift(UP*-1.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*-3.5).shift(UP*-1.5))).scale(0.8)

        twobyfoursap_3=(VGroup(tile6.copy().shift(RIGHT*-2.5).shift(UP*1.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*-1.5).shift(UP*1.5)) + \
                        VGroup(tile0.copy().shift(RIGHT*-2.5).shift(UP*0.5)) + \
                        VGroup(tile1.copy().shift(RIGHT*-1.5).shift(UP*0.5)) + \
                        VGroup(tile4.copy().shift(RIGHT*-2.5).shift(UP*-0.5)) + \
                        VGroup(tile4.copy().shift(RIGHT*-1.5).shift(UP*-0.5)) + \
                        VGroup(tile3.copy().shift(RIGHT*-2.5).shift(UP*-1.5)) + \
                        VGroup(tile2.copy().shift(RIGHT*-1.5).shift(UP*-1.5))).scale(0.8)
        
        twobyfoursap_4=(VGroup(tile0.copy().shift(RIGHT*-0.5).shift(UP*1.5)) + \
                        VGroup(tile1.copy().shift(RIGHT*0.5).shift(UP*1.5)) + \
                        VGroup(tile3.copy().shift(RIGHT*-0.5).shift(UP*0.5)) + \
                        VGroup(tile2.copy().shift(RIGHT*0.5).shift(UP*0.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*-0.5).shift(UP*-0.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*0.5).shift(UP*-0.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*-0.5).shift(UP*-1.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*0.5).shift(UP*-1.5))).scale(0.8)
        
        twobyfoursap_5=(VGroup(tile6.copy().shift(RIGHT*1.5).shift(UP*1.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*2.5).shift(UP*1.5)) + \
                        VGroup(tile0.copy().shift(RIGHT*1.5).shift(UP*0.5)) + \
                        VGroup(tile1.copy().shift(RIGHT*2.5).shift(UP*0.5)) + \
                        VGroup(tile3.copy().shift(RIGHT*1.5).shift(UP*-0.5)) + \
                        VGroup(tile2.copy().shift(RIGHT*2.5).shift(UP*-0.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*1.5).shift(UP*-1.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*2.5).shift(UP*-1.5))).scale(0.8)
        
        twobyfoursap_6=(VGroup(tile6.copy().shift(RIGHT*3.5).shift(UP*1.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*4.5).shift(UP*1.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*3.5).shift(UP*0.5)) + \
                        VGroup(tile6.copy().shift(RIGHT*4.5).shift(UP*0.5)) + \
                        VGroup(tile0.copy().shift(RIGHT*3.5).shift(UP*-0.5)) + \
                        VGroup(tile1.copy().shift(RIGHT*4.5).shift(UP*-0.5)) + \
                        VGroup(tile3.copy().shift(RIGHT*3.5).shift(UP*-1.5)) + \
                        VGroup(tile2.copy().shift(RIGHT*4.5).shift(UP*-1.5))).scale(0.8)
        
        twobyfoursap_7=(VGroup(tile0.copy().shift(RIGHT*5.5).shift(UP*1.5)) + \
                        VGroup(tile1.copy().shift(RIGHT*6.5).shift(UP*1.5)) + \
                        VGroup(tile3.copy().shift(RIGHT*5.5).shift(UP*0.5)) + \
                        VGroup(tile2.copy().shift(RIGHT*6.5).shift(UP*0.5)) + \
                        VGroup(tile0.copy().shift(RIGHT*5.5).shift(UP*-0.5)) + \
                        VGroup(tile1.copy().shift(RIGHT*6.5).shift(UP*-0.5)) + \
                        VGroup(tile3.copy().shift(RIGHT*5.5).shift(UP*-1.5)) + \
                        VGroup(tile2.copy().shift(RIGHT*6.5).shift(UP*-1.5))).scale(0.8)

        self.play(FadeIn(twobyfoursap_1), \
                  FadeIn(twobyfoursap_2), \
                  FadeIn(twobyfoursap_3), \
                  FadeIn(twobyfoursap_4), \
                  FadeIn(twobyfoursap_5), \
                  FadeIn(twobyfoursap_6), \
                  FadeIn(twobyfoursap_7))

        self.wait(1)

        twobyfoursaplabel_1 = Tex(r"$1$").shift(UP*-2.1).shift(RIGHT*-6)
        twobyfoursaplabel_2 = Tex(r"$6^2$").shift(UP*-2.1).shift(RIGHT*-4)
        twobyfoursaplabel_3 = Tex(r"$6^2$").shift(UP*-2.1).shift(RIGHT*-2)
        twobyfoursaplabel_4 = Tex(r"$6^4$").shift(UP*-2.1).shift(RIGHT*0)
        twobyfoursaplabel_5 = Tex(r"$6^4$").shift(UP*-2.1).shift(RIGHT*2)
        twobyfoursaplabel_6 = Tex(r"$6^4$").shift(UP*-2.1).shift(RIGHT*4)
        twobyfoursaplabel_7 = Tex(r"$1$").shift(UP*-2.1).shift(RIGHT*6)

        twobyfourplus1 = Tex(r"$+$").shift(UP*-2.1).shift(RIGHT*-5)
        twobyfourplus2 = Tex(r"$+$").shift(UP*-2.1).shift(RIGHT*-3)
        twobyfourplus3 = Tex(r"$+$").shift(UP*-2.1).shift(RIGHT*-1)
        twobyfourplus4 = Tex(r"$+$").shift(UP*-2.1).shift(RIGHT*1)
        twobyfourplus5 = Tex(r"$+$").shift(UP*-2.1).shift(RIGHT*3)
        twobyfourplus6 = Tex(r"$+$").shift(UP*-2.1).shift(RIGHT*5)

        self.play(FadeIn(twobyfoursaplabel_1), \
                  FadeIn(twobyfoursaplabel_2), \
                  FadeIn(twobyfoursaplabel_3), \
                  FadeIn(twobyfoursaplabel_4), \
                  FadeIn(twobyfoursaplabel_5), \
                  FadeIn(twobyfoursaplabel_6), \
                  FadeIn(twobyfoursaplabel_7), \
                  FadeIn(twobyfourplus1), \
                  FadeIn(twobyfourplus2), \
                  FadeIn(twobyfourplus3), \
                  FadeIn(twobyfourplus4), \
                  FadeIn(twobyfourplus5), \
                  FadeIn(twobyfourplus6))
                
        
        self.wait(1)

        twobyfoursap_4.generate_target()
        twobyfoursap_4.target.shift(RIGHT*-2)
        twobyfoursap_6.generate_target()
        twobyfoursap_6.target.shift(RIGHT*-4) 
        twobyfoursap_7.generate_target()
        twobyfoursap_7.target.shift(RIGHT*-4) 

        self.play(FadeOut(twobyfoursaplabel_1), \
                    FadeOut(twobyfoursaplabel_2), \
                    FadeOut(twobyfoursaplabel_3), \
                    FadeOut(twobyfoursaplabel_4), \
                    FadeOut(twobyfoursaplabel_5), \
                    FadeOut(twobyfoursaplabel_6), \
                    FadeOut(twobyfoursaplabel_7), \
                    FadeOut(twobyfour), \
                    FadeOut(twobyfour_1), \
                    FadeOut(twobyfour_2), \
                    FadeOut(twobyfour_3), \
                    FadeOut(twobyfour_4), \
                    FadeOut(twobyfour_5), \
                    FadeOut(twobyfour_6), \
                    FadeOut(twobyfoursap_1), \
                    FadeOut(twobyfoursap_2), \
                    FadeOut(twobyfoursap_3), \
                    FadeOut(twobyfoursap_5), \
                    FadeOut(twobyfourplus1), \
                    FadeOut(twobyfourplus2), \
                    FadeOut(twobyfourplus3), \
                    FadeOut(twobyfourplus4), \
                    FadeOut(twobyfourplus5), \
                    FadeOut(twobyfourplus6))
                    
        self.play(MoveToTarget(twobyfoursap_4) , \
                    MoveToTarget(twobyfoursap_6) , \
                    MoveToTarget(twobyfoursap_7))

        self.wait(1)

        fadesap1 = twobyfoursap_7.copy().shift(RIGHT*-4)
        fadesap2 = twobyfoursap_7.copy().shift(RIGHT*-2)

        stupid = twobyfoursap_4.copy()
        stupid1 = twobyfoursap_6.copy()

        self.play(ReplacementTransform(twobyfoursap_4,fadesap1))
        self.wait(1)
        self.play(ReplacementTransform(fadesap1,stupid))
        self.wait(1)
        self.play(ReplacementTransform(twobyfoursap_6,fadesap2))
        self.wait(1)
        self.play(ReplacementTransform(fadesap2,stupid1))
        self.wait(1)
        self.play(Indicate(twobyfoursap_7))
        self.wait(1)

        stupid.generate_target()
        stupid.target.shift(RIGHT*2)
        stupid1.generate_target()
        stupid1.target.shift(RIGHT*4)
        twobyfoursap_7.generate_target()
        twobyfoursap_7.target.shift(RIGHT*4) 

        self.play(MoveToTarget(stupid) , \
                    MoveToTarget(stupid1) , \
                    MoveToTarget(twobyfoursap_7))
        
        self.play(FadeIn(twobyfour), \
                    FadeIn(twobyfour_1), \
                    FadeIn(twobyfour_2), \
                    FadeIn(twobyfour_3), \
                    FadeIn(twobyfour_4), \
                    FadeIn(twobyfour_5), \
                    FadeIn(twobyfour_6), \
                    FadeIn(twobyfoursap_1), \
                    FadeIn(twobyfoursap_2), \
                    FadeIn(twobyfoursap_3), \
                    FadeIn(twobyfoursap_5))
        
        self.play(FadeIn(twobyfoursaplabel_1), \
                    FadeIn(twobyfoursaplabel_2), \
                    FadeIn(twobyfoursaplabel_3), \
                    FadeIn(twobyfoursaplabel_4), \
                    FadeIn(twobyfoursaplabel_5), \
                    FadeIn(twobyfoursaplabel_6), \
                    FadeIn(twobyfoursaplabel_7), \
                    FadeIn(twobyfourplus1), \
                    FadeIn(twobyfourplus2), \
                    FadeIn(twobyfourplus3), \
                    FadeIn(twobyfourplus4), \
                    FadeIn(twobyfourplus5), \
                    FadeIn(twobyfourplus6))
            
        self.wait(1)

        twobyfourminus6 = Tex(r"$-$").shift(UP*-2.1).shift(RIGHT*5)

        self.play(Transform(twobyfourplus6,twobyfourminus6))
        self.wait(1)

        twobyfoursaplabel_1.generate_target()
        twobyfoursaplabel_1.target.shift(RIGHT*3)
        twobyfoursaplabel_2.generate_target() 
        twobyfoursaplabel_2.target.shift(RIGHT*2) 
        twobyfoursaplabel_3.generate_target() 
        twobyfoursaplabel_3.target.shift(RIGHT*1) 
        twobyfoursaplabel_4.generate_target() 
        twobyfoursaplabel_4.target.shift(RIGHT*0) 
        twobyfoursaplabel_5.generate_target() 
        twobyfoursaplabel_5.target.shift(RIGHT*-1) 
        twobyfoursaplabel_6.generate_target() 
        twobyfoursaplabel_6.target.shift(RIGHT*-2) 
        twobyfoursaplabel_7.generate_target() 
        twobyfoursaplabel_7.target.shift(RIGHT*-3) 

        twobyfourplus1.generate_target()
        twobyfourplus1.target.shift(RIGHT*2.45)
        twobyfourplus2 .generate_target()
        twobyfourplus2 .target.shift(RIGHT*1.5)
        twobyfourplus3 .generate_target()
        twobyfourplus3 .target.shift(RIGHT*0.5)
        twobyfourplus4 .generate_target()
        twobyfourplus4 .target.shift(RIGHT*-0.5)
        twobyfourplus5 .generate_target()
        twobyfourplus5 .target.shift(RIGHT*-1.5)
        twobyfourplus6.generate_target()
        twobyfourplus6.target.shift(RIGHT*-2.45)

        self.play(MoveToTarget(twobyfoursaplabel_1), \
                    MoveToTarget(twobyfoursaplabel_2), \
                    MoveToTarget(twobyfoursaplabel_3), \
                    MoveToTarget(twobyfoursaplabel_4), \
                    MoveToTarget(twobyfoursaplabel_5), \
                    MoveToTarget(twobyfoursaplabel_6), \
                    MoveToTarget(twobyfoursaplabel_7), \
                    MoveToTarget(twobyfourplus1), \
                    MoveToTarget(twobyfourplus2), \
                    MoveToTarget(twobyfourplus3), \
                    MoveToTarget(twobyfourplus4), \
                    MoveToTarget(twobyfourplus5), \
                    MoveToTarget(twobyfourplus6))
        
        self.wait(1)
        
        finalexpr1 = Tex(r"$t_{2,4} = $").shift(UP*-2.15).shift(RIGHT*-3.9)
        finalexpr2 = Tex(r"$ = 3960$").shift(UP*-2.1).shift(RIGHT*4)

        self.play(FadeIn(finalexpr1))
        self.wait(1)
        self.play(FadeIn(finalexpr2))
        self.wait(1)

        self.play(FadeOut(twobyfour), \
                    FadeOut(twobyfour_1), \
                    FadeOut(twobyfour_2), \
                    FadeOut(twobyfour_3), \
                    FadeOut(twobyfour_4), \
                    FadeOut(twobyfour_5), \
                    FadeOut(twobyfour_6), \
                    FadeOut(twobyfoursap_1), \
                    FadeOut(twobyfoursap_2), \
                    FadeOut(twobyfoursap_3), \
                    FadeOut(stupid), \
                    FadeOut(stupid1),\
                    FadeOut(twobyfoursap_5), \
                    FadeOut(twobyfoursap_7), \
                    FadeOut(finalexpr1), \
                    FadeOut(finalexpr2), \
                    FadeOut(twobyfoursaplabel_1), \
                    FadeOut(twobyfoursaplabel_2), \
                    FadeOut(twobyfoursaplabel_3), \
                    FadeOut(twobyfoursaplabel_4), \
                    FadeOut(twobyfoursaplabel_5), \
                    FadeOut(twobyfoursaplabel_6), \
                    FadeOut(twobyfoursaplabel_7), \
                    FadeOut(twobyfourplus1), \
                    FadeOut(twobyfourplus2), \
                    FadeOut(twobyfourplus3), \
                    FadeOut(twobyfourplus4), \
                    FadeOut(twobyfourplus5), \
                    FadeOut(twobyfourplus6))
        
        self.wait(1)

        inclexcl = Tex(r"Inclusion-Exclusion Principle")

        self.play(Write(inclexcl),run_time=0.8)
        self.wait(1)

        inclexcl.generate_target()
        inclexcl.target.shift(UP*3)

        self.play(MoveToTarget(inclexcl))
        self.wait(1)

        # inclexclexpr = Tex(r"$$|\bigcup_{i=1}^n A_i|= \sum_{\emptyset \neq A \subseteq \{ 1,\dots,n\}}(-1)^{|J|+1}|\bigcap_{j \in J}A_j|$$").shift(UP*-2.5)
        inclexclexpr = Tex(r"$$\left\lvert\bigcup_{i=1}^n A_i\right\rvert= \sum_{\emptyset \neq J \subseteq \{ 1,\dots,n\}}(-1)^{|J|+1}\left\lvert\bigcap_{j \in J}A_j\right\rvert$$").shift(UP*-2.5)

        self.play(Write(inclexclexpr))
        self.wait(1)
        self.play(FadeOut(inclexcl),FadeOut(inclexclexpr))

        uhtablelabel = MathTex(r"\mathbf{t_{n,m}}")
        uhtablelabel[0][0].set_color(a)
        uhtable = MathTable(
            [
            ["","","",""],
            ["","","",""],
            ["","","",""],
            ["","","",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=uhtablelabel
        ).scale(0.65)

        tablelabel = MathTex(r"\mathbf{t_{n,m}}")
        tablelabel[0][0].set_color(a)
        table = MathTable(
            [
            [0,0,0,0],
            [0,"","",""],
            [0,"","",""],
            [0,"","",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=tablelabel
        ).scale(0.65)


        table03label = MathTex(r"\mathbf{t_{n,m}}")
        table03label[0][0].set_color(a)
        table03 = MathTable(
            [
            [0,0,0,0],
            [0,1,"",""],
            [0,"","",""],
            [0,"","",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=table03label
        ).scale(0.65)

        table06label = MathTex(r"\mathbf{t_{n,m}}")
        table06label[0][0].set_color(a)
        table06 = MathTable(
            [
            [0,0,0,0],
            [0,1,73,""],
            [0,"","",""],
            [0,"","",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=table06label
        ).scale(0.65)

        table1label = MathTex(r"\mathbf{t_{n,m}}")
        table1label[0][0].set_color(a)
        table1 = MathTable(
            [
            [0,0,0,0],
            [0,1,73,3960],
            [0,"","",""],
            [0,"","",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=table1label
        ).scale(0.65)

        table2label = MathTex(r"\mathbf{t_{n,m}}")
        table2label[0][0].set_color(a)
        table2 = MathTable(
            [
            [0,0,0,0],
            [0,1,73,3960],
            [0,73,"",""],
            [0,3960,"",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=table2label
        ).scale(0.65)

        table3label = MathTex(r"\mathbf{t_{n,m}}")
        table3label[0][0].set_color(a)
        table3 = MathTable(
            [
            [0,0,0,0],
            [0,1,73,3960],
            [0,73,31998,""],
            [0,3960,"",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=table3label
        ).scale(0.65)

        table4label = MathTex(r"\mathbf{p_{n,m}}")
        table4label[0][0].set_color(e)
        table4 = MathTable(
            [
            [0.0000,0.0000,0.0000,0.0000],
            [0.0000,0.0008,0.0016,0.0024],
            [0.0000,0.0016,0.0032,""],
            [0.0000,0.0024,"",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=table4label
        ).scale(0.65)

        self.wait(1)
        self.play(Write(uhtable))
        self.wait(1)
        self.play(ReplacementTransform(uhtable, table))
        self.wait(1)
        self.play(Transform(table,table03))
        self.wait(1)
        self.play(Transform(table,table06))
        self.wait(1)
        self.play(Transform(table,table1))
        self.wait(1)

        table.generate_target()
        table.target.shift(RIGHT*-3.9)

        bij = Tex(r"$\longleftrightarrow$").shift(UP*0).shift(RIGHT*2)
        trelat = Tex(r"$t_{n,m} = t_{m,n}$").shift(UP*-2).shift(RIGHT*2)
        examplemosaic = VGroup(tile0.copy().shift(UP*1).shift(RIGHT*-0.5), \
                               tile1.copy().shift(UP*1).shift(RIGHT*0.5), \
                               tile3.copy().shift(UP*0).shift(RIGHT*-0.5), \
                               tile2.copy().shift(UP*0).shift(RIGHT*0.5), \
                               tile4.copy().shift(UP*-1).shift(RIGHT*-0.5), \
                               tile2.copy().shift(UP*-1).shift(RIGHT*0.5)).scale(0.8).shift(RIGHT*0.4)
        
        examplemosaicT = VGroup(tile5.copy().shift(UP*0.5).shift(RIGHT*0), \
                               tile0.copy().shift(UP*0.5).shift(RIGHT*1), \
                               tile1.copy().shift(UP*0.5).shift(RIGHT*2), \
                               tile3.copy().shift(UP*-0.5).shift(RIGHT*0), \
                               tile3.copy().shift(UP*-0.5).shift(RIGHT*1), \
                               tile2.copy().shift(UP*-0.5).shift(RIGHT*2)).scale(0.8).shift(RIGHT*3)

        self.play(MoveToTarget(table))
        self.play(Write(examplemosaic),run_time=0.8)
        self.play(Write(bij),run_time=0.8)
        self.play(Write(examplemosaicT),run_time=0.8)
        self.play(Write(trelat),run_time=0.8)
        table.target.shift(RIGHT*3.9)
        self.play(FadeOut(examplemosaic),FadeOut(bij),FadeOut(examplemosaicT),FadeOut(trelat))
        self.play(MoveToTarget(table))

        self.play(Transform(table,table2))
        self.wait(1)
        self.play(Transform(table,table3))
        self.wait(1)
        self.play(Transform(table,table4))
        self.wait(1)
        self.play(ReplacementTransform(table,table3))
        self.wait(1)
        self.play(FadeOut(table3))
        self.wait(1)

# Course I: Probability
class Section5(Scene):
    def construct(self):
        self.camera.background_color = "#181818"

        title = Tex(r"Course I: Probability").scale(1.5)

        self.wait(1)
        self.play(Write(title),run_time=1)
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        inclexcl = Tex(r"Inclusion-Exclusion Principle").shift(UP*1.5)
        inclexclexpr = Tex(r"$$\left\lvert\bigcup_{i=1}^n A_i\right\rvert= \sum_{\emptyset \neq J \subseteq \{ 1,\dots,n\}}(-1)^{|J|+1}\left\lvert\bigcap_{j \in J}A_j\right\rvert$$").shift(UP*-1.5)
        benefits = Tex(r"The benefits of a backburner problem were already appearing!").shift(UP*-1.5)

        self.play(Write(inclexcl),Write(inclexclexpr),run_time=1)
        self.wait(1)
        self.play(Indicate(inclexclexpr))
        self.wait(1)
        self.play(Transform(inclexclexpr,benefits))
        self.wait(1)
        self.play(FadeOut(inclexcl),FadeOut(inclexclexpr))
        self.wait(1)

# Course II: Intro to Programming
class Section6(Scene):
    def construct(self):
        self.camera.background_color = "#181818"

        # a = "#005F73" # 
        # b = "#0A9396" # 
        # c = "#94D2BD" # 
        # d = "#E9D8A6" # tile boarder
        # e = "#EE9B00" # 
        # f = "#CA6702" # 
        # g = "#BB3E03" # 
        # h = "#AE2012" # tile 
        # i = "#9B2226" # 

        title = Tex(r"Course II: Intro to Programming").scale(1.5)

        self.wait(1)
        self.play(Write(title),run_time=1)
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        pretablelabel0 = MathTex(r"\mathbf{t_{n,m}}")
        pretablelabel0[0][0].set_color(a)
        pretable0 = MathTable(
            [
            [0,0,0,0],
            [0,1,73,3960],
            [0,73,31998,""],
            [0,3960,"",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=pretablelabel0
        ).scale(0.65)

        tablelabel = MathTex(r"\mathbf{t_{n,m}}")
        tablelabel[0][0].set_color(a)
        table = MathTable(
            [
            [0,0,0,0],
            [0,1,73,3960],
            [0,73,31998,"?"],
            [0,3960,"?","?"]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=tablelabel
        ).scale(0.65)

        self.wait(1)
        self.play(Write(pretable0),run_time=1)
        self.wait(1)
        
        alg_str = '''def mosaics(h,w):
    plane = zeros((h,w))
    saps_list, memoize = [], []
    return mosaics_help(plane, memoize, saps_list, h*w, 0, h, w)

def mosaics_help(plane, memoize, saps_list, opens, depth, h, w):
    return_val = 0
    for i in range(h-1):
        for j in range(w-1):
            if plane[i][j] == 0: 
                workingsaps = saps(plane,i,j,h,w)
                    if len(workingsaps) == 0: plane[i][j] = 1
                    else:
                        for sap in workingsaps:
                    ...'''

        self.play(ReplacementTransform(pretable0,table))
        self.wait(1)
        
        table.generate_target()
        table.target.shift(UP*1.8)

        alg = Code(code=alg_str,tab_width=4, background="window", language="Python", font="Monospace").scale(0.8).shift(UP*-7)
        alg.generate_target()
        alg.target.shift(UP*4.45)

        self.play(FadeOut(table))
        self.wait(1)
        self.play(FadeIn(table))
        self.wait(1)

        self.play(MoveToTarget(table),MoveToTarget(alg))
        self.wait(1)

        table.target.shift(UP*-2)
        alg.target.shift(UP*-4.45)

        self.play(MoveToTarget(table),MoveToTarget(alg))
        self.wait(1)        

        table1label = MathTex(r"\mathbf{t_{n,m}}")
        table1label[0][0].set_color(a)
        table1 = MathTable(
            [
            [0,0,0,0],
            [0,1,73,3960],
            [0,73,31998,10414981],
            [0,3960,10414981,20334816290]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=table1label
        ).scale(0.65)

        posttablelabel = MathTex(r"\mathbf{t_{n,m}}")
        posttablelabel[0][0].set_color(a)
        posttable = MathTable(
            [
            [0,0,0,0,""],
            [0,1,73,3960,""],
            [0,73,31998,10414981,""],
            [0,3960,10414981,20334816290,""],
            ["","","","",""]
            ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(1,6)],
            row_labels=[Tex(str(n)) for n in range(1,6)],
            top_left_entry=posttablelabel
        ).scale(0.65)
        posttable.shift(UP*-(abs(posttable.height - table1.height))/2).shift(RIGHT*0.5)

        self.play(ReplacementTransform(table,table1))
        self.wait(1)
        self.play(FadeIn(posttable))
        self.wait(1)
        
        q1 = Tex(r"What else could I do?").shift(UP*2.5)

        q2 = Tex(r"Enumerating $t_{n,m}$ may be too tricky.").shift(UP*2.5)

        self.play(Write(q1),run_time=1)
        self.wait(1)
        self.play(ReplacementTransform(q1,q2),FadeOut(posttable))
        self.wait(1)
        self.play(Indicate(table1.get_rows()[2]))
        self.wait(1)
        self.play(FadeOut(table1),FadeOut(q2))
        self.wait(1)

# Course III: Combinatorics
class Section7(Scene):
    def construct(self):
        self.camera.background_color = "#181818"

        title = Tex(r"Course III: Combinatorics").scale(1.5)

        self.wait(1)
        self.play(Write(title),run_time=1)
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        twobyfour = Rectangle(width=4,height=2,grid_xstep=1,grid_ystep=1,color=d)
        twobyfive = Rectangle(width=5,height=2,grid_xstep=1,grid_ystep=1,color=d)
        twobysix = Rectangle(width=6,height=2,grid_xstep=1,grid_ystep=1,color=d)
        twobyseven = Rectangle(width=7,height=2,grid_xstep=1,grid_ystep=1,color=d)

        nbytwo = Tex(r"The $n \times 2$ case").shift(UP*-2)

        twobyseven.generate_target()
        twobyseven.target.shift(UP*7)
        linrecur = Tex(r"Linear Recurrence Relations").shift(UP*2).scale(1.5)

        self.play(Write(twobyfour),Write(nbytwo))
        self.play(ReplacementTransform(twobyfour,twobyfive),run_time=0.5)
        self.play(ReplacementTransform(twobyfive,twobysix),run_time=0.5)
        self.play(ReplacementTransform(twobysix,twobyseven),run_time=0.5)
        self.play(MoveToTarget(twobyseven),ReplacementTransform(nbytwo,linrecur))
        self.wait(1)

        linrecurdefi = Tex(r"Example: $f(k) = $").shift(UP*-1.75).shift(RIGHT*-2.2)
        linrecurdefii = Tex(r"$2f(k-1) - f(k-3)$").shift(UP*-1.75).shift(RIGHT*2.2)
        linrecurdefi[0][10].set_color(d)
        linrecurdefii[0][3].set_color(d)
        linrecurdefii[0][10].set_color(d)
        self.play(Write(linrecurdefi),run_time=1)
        self.wait(1)
        self.play(Write(linrecurdefii),run_time=1)
        self.wait(1)

        self.play(FadeOut(linrecur),FadeOut(linrecurdefi),FadeOut(linrecurdefii))
        self.wait(1)

        twobytwo = Rectangle(width=2,height=2,grid_xstep=1,grid_ystep=1,color=d)
        twobythree = Rectangle(width=3,height=2,grid_xstep=1,grid_ystep=1,color=d)
        twobyfour = Rectangle(width=4,height=2,grid_xstep=1,grid_ystep=1,color=d)
        
        twobytwolabel = Tex(r"$t_{2,2} = 1$").scale(0.8)
        twobytwolabel[0][0].set_color(a)
        twobythreelabel = Tex(r"$t_{3,2} = 73$").scale(0.8)
        twobythreelabel[0][0].set_color(a)
        twobyfourlabel = Tex(r"$t_{4,2} = 3960$").scale(0.8)
        twobyfourlabel[0][0].set_color(a)

        twobytwo.shift(RIGHT*-4.5)
        twobythree.shift(RIGHT*-1.25)
        twobyfour.shift(RIGHT*3)

        twobytwolabel.shift(UP*-1.5).shift(RIGHT*-4.5)
        twobythreelabel.shift(UP*-1.5).shift(RIGHT*-1.25)
        twobyfourlabel.shift(UP*-1.5).shift(RIGHT*3)

        twobyfour.generate_target()
        twobyfour.target.shift(RIGHT*-3)

        self.play(FadeIn(twobytwo), \
                  FadeIn(twobythree), \
                  FadeIn(twobyfour),\
                  FadeIn(twobytwolabel) ,\
                  FadeIn(twobythreelabel) ,\
                  FadeIn(twobyfourlabel))
        
        self.wait(1)
        self.play(FadeOut(twobytwo), \
                  FadeOut(twobythree), \
                  FadeOut(twobytwolabel) ,\
                  FadeOut(twobythreelabel) ,\
                  FadeOut(twobyfourlabel))
        self.play(MoveToTarget(twobyfour))
        
        self.wait(1)

        twobyfour.target.shift(RIGHT*-0.5)

        twobyfive = Rectangle(width=5,height=2,grid_xstep=1,grid_ystep=1,color=d)
        addition = Rectangle(width=1,height=2,grid_xstep=1,grid_ystep=1,color=f).shift(RIGHT*3)

        addition.generate_target()
        addition.target.shift(RIGHT*-1)

        # self.play(ReplacementTransform(twobyfour,twobyfive))
        self.play(Create(addition))
        self.play(MoveToTarget(twobyfour),MoveToTarget(addition))
        self.wait(1)

        # hilight = Rectangle(width=1,height=2,grid_xstep=1,grid_ystep=1,color=f).shift(RIGHT*2)
        # hilighttwobyfive = VGroup(twobyfive,hilight)
        # self.play(FadeIn(hilight))
        # self.wait(1)

        square0 = Square(side_length=1,color=d)
        line0 = Line(start=square0.get_edge_center(DOWN),end=square0.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        tile0 = VGroup(square0,line0,square0.copy())

        square1 = Square(side_length=1,color=d)
        line1 = Line(start=square1.get_edge_center(DOWN),end=square1.get_edge_center(LEFT), stroke_width=8).set_color(i)
        tile1 = VGroup(square1,line1,square1.copy())

        square2 = Square(side_length=1,color=d)
        line2 = Line(start=square2.get_edge_center(LEFT),end=square2.get_edge_center(UP), stroke_width=8).set_color(i)
        tile2 = VGroup(square2,line2,square2.copy())

        square3 = Square(side_length=1,color=d)
        line3 = Line(start=square3.get_edge_center(UP),end=square3.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        tile3 = VGroup(square3,line3,square3.copy())

        square4 = Square(side_length=1,color=d)
        line4 = Line(start=square4.get_edge_center(DOWN),end=square4.get_edge_center(UP), stroke_width=8).set_color(i)
        tile4 = VGroup(square4,line4,square4.copy())

        square5 = Square(side_length=1,color=d)
        line5 = Line(start=square5.get_edge_center(LEFT),end=square5.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        tile5 = VGroup(square5,line5,square5.copy())

        square6 = Square(side_length=1,color=d)
        dot = Dot().set_color(i)
        tile6 = VGroup(square6,dot,square6.copy())

        bsquare0 = Square(side_length=1, color=f)
        bline0 = Line(start=square0.get_edge_center(DOWN),end=square0.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        btile0 = VGroup(bsquare0,bline0,bsquare0.copy())

        bsquare1 = Square(side_length=1, color=f)
        bline1 = Line(start=square1.get_edge_center(DOWN),end=square1.get_edge_center(LEFT), stroke_width=8).set_color(i)
        btile1 = VGroup(bsquare1,bline1,bsquare1.copy())

        bsquare2 = Square(side_length=1)
        bsquare2.color = f
        bline2 = Line(start=square2.get_edge_center(LEFT),end=square2.get_edge_center(UP), stroke_width=8).set_color(i)
        btile2 = VGroup(bsquare2,bline2,bsquare2.copy())

        bsquare3 = Square(side_length=1, color=f)
        bline3 = Line(start=square3.get_edge_center(UP),end=square3.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        btile3 = VGroup(bsquare3,bline3,bsquare3.copy())

        bsquare4 = Square(side_length=1, color=f)
        bline4 = Line(start=square4.get_edge_center(DOWN),end=square4.get_edge_center(UP), stroke_width=8).set_color(i)
        btile4 = VGroup(bsquare4,bline4,bsquare4.copy())

        bsquare5 = Square(side_length=1, color=f)
        bline5 = Line(start=square5.get_edge_center(LEFT),end=square5.get_edge_center(RIGHT), stroke_width=8).set_color(i)
        btile5 = VGroup(bsquare5,bline5,bsquare5.copy())

        bsquare6 = Square(side_length=1)
        bdot = Dot().set_color(i)
        btile6 = VGroup(bsquare6,bdot,bsquare6.copy())

        sapuno = (VGroup(tile6.copy().shift(RIGHT*-2).shift(UP*0.5)) + \
                VGroup(tile0.copy().shift(RIGHT*-1).shift(UP*0.5)) + \
                VGroup(tile1.copy().shift(RIGHT*0).shift(UP*0.5)) + \
                VGroup(tile6.copy().shift(RIGHT*-2).shift(UP*-0.5)) + \
                VGroup(tile3.copy().shift(RIGHT*-1).shift(UP*-0.5)) + \
                VGroup(tile2.copy().shift(RIGHT*0).shift(UP*-0.5)))

        dotuno = Dot().set_color(i).shift(UP*0.5).shift(RIGHT*1)
        dotdos = Dot().set_color(i).shift(UP*-0.5).shift(RIGHT*1)

        self.play(FadeIn(sapuno),FadeIn(dotuno),FadeIn(dotdos))

        firstpart1 = Tex(r"$t_{4,2}$").shift(UP*-2.1).shift(RIGHT*-0.4)
        firstpart1[0][0].set_color(a)
        firstpart2 = Tex(r"$\times$").shift(UP*-2).shift(RIGHT*0.8)
        firstpart3 = Tex(r"$6^2$").shift(UP*-2).shift(RIGHT*2)

        self.play(FadeIn(firstpart1))
        self.wait(1)
        
        dottres = Dot().set_color(i).shift(UP*0.5).shift(RIGHT*2)
        dotquatro = Dot().set_color(i).shift(UP*-0.5).shift(RIGHT*2)
        self.play(FadeIn(dottres),FadeIn(dotquatro))
        
        self.play(FadeIn(firstpart2),FadeIn(firstpart3))
        self.wait(1)

        equationparti = VGroup(firstpart1, firstpart2, firstpart3)
        equationpartii = Tex(r"$$t_{5,2} \geq 6^2 t_{4,2}$$").shift(UP*2.2)
        equationpartii[0][0].set_color(a)
        equationpartii[0][7].set_color(a)

        self.play(ReplacementTransform(equationparti,equationpartii))
        self.wait(1)

        q = Tex(r"Are there more mosaics in $t_{5,2}$?").shift(UP*-2)
        q[0][21].set_color(a)
        answer = Tex(r"Yes!").shift(UP*-2)
        self.play(Write(q),run_time=0.7)
        self.wait(1)
        self.play(Transform(q,answer))        
        self.wait(1)
        self.play(FadeOut(sapuno), \
                  FadeOut(dotuno), \
                  FadeOut(dotdos), \
                  FadeOut(dottres), \
                  FadeOut(dotquatro), \
                  FadeOut(q))
        self.wait(1)

        brace_left = Brace(mobject = twobyfour, direction=DOWN, buff=0.2)
        self.play(Write(brace_left),run_time=1)
        self.wait(1)
        self.play(FadeOut(brace_left))
        self.wait(1)
        self.play(Indicate(addition))
        self.wait(1)

        sapdos = (VGroup(tile0.copy().shift(RIGHT*1).shift(UP*0.5)) + \
                VGroup(btile1.copy().shift(RIGHT*2).shift(UP*0.5)) + \
                VGroup(tile3.copy().shift(RIGHT*1).shift(UP*-0.5)) + \
                VGroup(btile2.copy().shift(RIGHT*2).shift(UP*-0.5)))
        
        self.play(FadeIn(sapdos))
        self.wait(1)

        smallestlabel1 = Tex(r"$$(6^{3*2} - t_{3,2})$$").shift(UP*-2).shift(RIGHT*-1)
        smallestlabel1[0][6].set_color(a)
        smallestlabel2 = Tex(r"$\times$").shift(UP*-2).shift(RIGHT*0.85)
        smallestlabel3 = Tex(r"$1$").shift(UP*-2).shift(RIGHT*1.5)

        self.play(FadeIn(smallestlabel3))

        nosapdos = (VGroup(tile4.copy().shift(RIGHT*-2).shift(UP*0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*-1).shift(UP*0.5)) + \
                VGroup(tile0.copy().shift(RIGHT*0).shift(UP*0.5)) + \
                VGroup(tile0.copy().shift(RIGHT*-2).shift(UP*-0.5)) + \
                VGroup(tile3.copy().shift(RIGHT*-1).shift(UP*-0.5)) + \
                VGroup(tile2.copy().shift(RIGHT*0).shift(UP*-0.5)))

        self.wait(1)
        self.play(FadeIn(nosapdos))
        self.wait(1)
        self.play(FadeIn(smallestlabel2),FadeIn(smallestlabel1))
        self.wait(1)
        equationpartiii = Tex(r"$$t_{5,2} \geq 6^2 t_{4,2} + (6^{3*2} - t_{3,2})$$").shift(UP*2.2)
        equationpartiii[0][0].set_color(a)
        equationpartiii[0][7].set_color(a)
        equationpartiii[0][18].set_color(a)

        self.play(ReplacementTransform(equationpartii,equationpartiii))
        self.wait(1)

        self.play(FadeOut(sapdos), \
                  FadeOut(nosapdos), \
                  FadeOut(smallestlabel1), \
                  FadeOut(smallestlabel2), \
                  FadeOut(smallestlabel3))
        
        self.wait(1)

        saptres = (VGroup(tile0.copy().shift(RIGHT*0).shift(UP*0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*1).shift(UP*0.5)) + \
                VGroup(btile1.copy().shift(RIGHT*2).shift(UP*0.5)) + \
                VGroup(tile3.copy().shift(RIGHT*0).shift(UP*-0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*1).shift(UP*-0.5)) + \
                VGroup(btile2.copy().shift(RIGHT*2).shift(UP*-0.5)))

        nosaptres = (VGroup(tile5.copy().shift(RIGHT*-2).shift(UP*0.5)) + \
                        VGroup(tile2.copy().shift(RIGHT*-1).shift(UP*0.5)) + \
                        VGroup(tile2.copy().shift(RIGHT*-2).shift(UP*-0.5)) + \
                        VGroup(tile3.copy().shift(RIGHT*-1).shift(UP*-0.5)))
        
        sapquatro = (VGroup(tile0.copy().shift(RIGHT*-1).shift(UP*0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*0).shift(UP*0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*1).shift(UP*0.5)) + \
                VGroup(btile1.copy().shift(RIGHT*2).shift(UP*0.5)) + \
                VGroup(tile3.copy().shift(RIGHT*-1).shift(UP*-0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*0).shift(UP*-0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*1).shift(UP*-0.5)) + \
                VGroup(btile2.copy().shift(RIGHT*2).shift(UP*-0.5)))

        nosapquatro = (VGroup(tile3.copy().shift(RIGHT*-2).shift(UP*0.5)) + \
                        VGroup(tile2.copy().shift(RIGHT*-2).shift(UP*-0.5)))
        
        sapfive = (VGroup(tile0.copy().shift(RIGHT*-2).shift(UP*0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*-1).shift(UP*0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*0).shift(UP*0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*1).shift(UP*0.5)) + \
                VGroup(btile1.copy().shift(RIGHT*2).shift(UP*0.5)) + \
                VGroup(tile3.copy().shift(RIGHT*-2).shift(UP*-0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*-1).shift(UP*-0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*0).shift(UP*-0.5)) + \
                VGroup(tile5.copy().shift(RIGHT*1).shift(UP*-0.5)) + \
                VGroup(btile2.copy().shift(RIGHT*2).shift(UP*-0.5)))


        treslabel1 = Tex(r"$(6^{2*2} - t_{2,2})$").shift(UP*-2).shift(RIGHT*-1)
        treslabel1[0][6].set_color(a)
        treslabel2 = Tex(r"$\times$").shift(UP*-2).shift(RIGHT*0.65)
        treslabel3 = Tex(r"$1$").shift(UP*-2).shift(RIGHT*1.2)
        treslabels = VGroup(treslabel1, \
                            treslabel2, \
                            treslabel3)
        equationpartiiii = Tex(r"$$t_{5,2} \geq 6^2 t_{4,2} + \sum_{i=2}^{3}(6^{2i} - t_{i,2})$$").shift(UP*2.2)
        equationpartiiii[0][0].set_color(a)
        equationpartiiii[0][7].set_color(a)
        equationpartiiii[0][22].set_color(a)
        self.play(FadeIn(saptres),FadeIn(nosaptres),FadeIn(treslabels))
        self.play(TransformMatchingTex(equationpartiii,equationpartiiii))
        self.play(FadeOut(saptres),FadeOut(nosaptres),FadeOut(treslabels))

        quatrolabel1 = Tex(r"$(6^{1*2})$").shift(UP*-2).shift(RIGHT*-1)
        quatrolabel2 = Tex(r"$\times$").shift(UP*-2).shift(RIGHT*0.3)
        quatrolabel3 = Tex(r"$1$").shift(UP*-2).shift(RIGHT*1)
        quatrolabels = VGroup(quatrolabel1, \
                            quatrolabel2, \
                            quatrolabel3)
        equationpartv = Tex(r"$$t_{5,2} \geq 6^2 t_{4,2} + \sum_{i=2}^{4}(6^{2i} - t_{i,2})$$").shift(UP*2.2)
        equationpartv[0][0].set_color(a)
        equationpartv[0][7].set_color(a)
        equationpartv[0][22].set_color(a)
        self.play(FadeIn(sapquatro),FadeIn(nosapquatro),FadeIn(quatrolabels))
        self.play(TransformMatchingTex(equationpartiiii,equationpartv))
        self.play(FadeOut(sapquatro),FadeOut(nosapquatro),FadeOut(quatrolabels))

        fivelabels = Tex(r"$1$").shift(UP*-2)
        equationpartvi = Tex(r"$$t_{5,2} = 6^2 t_{4,2} + \sum_{i=2}^{5}(6^{2i} - t_{i,2})$$").shift(UP*2.2)
        equationpartvi[0][0].set_color(a)
        equationpartvi[0][7].set_color(a)
        equationpartvi[0][22].set_color(a)
        self.play(FadeIn(sapfive),FadeIn(fivelabels))
        self.play(TransformMatchingTex(equationpartv,equationpartvi))
        self.play(FadeOut(sapfive),FadeOut(fivelabels),FadeOut(twobyfour),FadeOut(addition))

        equationpartvi.generate_target()
        equationpartvi.target.shift(UP*-2)

        self.play(MoveToTarget(equationpartvi))
        self.wait(1)

        equationpartvi.target.shift(RIGHT*-1.5)
        equationpartvi2 = Tex(r"= 190,475").shift(RIGHT*2.75).shift(UP*0.15)

        self.play(MoveToTarget(equationpartvi))
        self.play(FadeIn(equationpartvi2))
        self.wait(1)
        self.play(FadeOut(equationpartvi2),run_time=0.25)

        twobynreq = Tex(r"$$t_{n,2} = 36t_{n-1,2} + \sum_{i=2}^n (6^{2(n-i)} - t_{n-i,2})$$")
        twobynreq[0][0].set_color(a)
        twobynreq[0][7].set_color(a)
        twobynreq[0][28].set_color(a)

        self.play(ReplacementTransform(equationpartvi,twobynreq))
        self.wait(1)

        twobynreq.generate_target()
        twobynreq.target.shift(UP*1.2)

        howdowe = Tex(r"How do we get a formula for $t_{n,2}$?").shift(UP*-1.5)
        howdowe[0][21].set_color(a)

        self.play(MoveToTarget(twobynreq), Write(howdowe))
        self.wait(1)
        self.play(FadeOut(twobynreq),FadeOut(howdowe))
        self.wait(1)

        introtogen = Tex(r"generating functions")

        self.play(Write(introtogen))
        self.wait(1)        
        self.play(FadeOut(introtogen))
        self.wait(1)        

        gen = Tex(r"GENERATING").shift(UP*1).shift(RIGHT*-2.7).scale(1.5)
        func = Tex(r"FUNCTIONS").shift(UP*1).shift(RIGHT*2.7).scale(1.5)
        are = Tex(r"ARE").shift(UP*-1).shift(RIGHT*-2.7).scale(1.5)
        confus = Tex(r"CONFUSING").shift(UP*-1).shift(RIGHT*1.7).scale(1.5)

        self.wait(1)
        self.add(gen)
        self.wait(1)
        self.add(func)
        self.wait(1)
        self.add(are)
        self.wait(1)
        self.add(confus)
        self.wait(1)
        self.remove(gen).remove(func).remove(are).remove(confus)

        bootables = VGroup(Tex(r"Power Series").shift(UP*2.5).shift(RIGHT*-3.5).scale(1.2),
                Tex(r"Generating Functions").shift(UP*2.5).shift(RIGHT*3.5).scale(1.2),
                Line(start=[-0.35,-3.25,0], end=[-0.35,3.25,0]),
                Line(start=[-6.5,1.75,0], end=[6.5,1.75,0]))

        careone = Tex(r"-care about convergence").shift(UP*1).shift(RIGHT*-3.5)
        dontcareone = Tex(r"-don't care about convergence").shift(UP*1).shift(RIGHT*3.5)
        caretwo = Tex(r"-care about input").shift(UP*0).shift(RIGHT*-4.2)
        dontcaretwo = Tex(r"-don't care about input").shift(UP*0).shift(RIGHT*2.8)
        carethree = Tex(r"-care about value").shift(UP*-1).shift(RIGHT*-4.2)
        dontcarethree = Tex(r"-don't care about value").shift(UP*-1).shift(RIGHT*2.8)
        carefour = Tex(r"-care about coefficients")
        dontcarefour = carefour.copy().shift(UP*-2).shift(RIGHT*2.8)
        carefour.shift(UP*-2).shift(RIGHT*-3.6)

        self.play(Write(bootables),run_time=1)
        self.wait(1)
        self.add(careone)
        self.wait(1)
        self.add(caretwo)
        self.wait(1)
        self.add(carethree)
        self.wait(1)
        self.add(dontcareone)
        self.wait(1)
        self.add(dontcaretwo)
        self.wait(1)
        self.add(dontcarethree)
        self.wait(1)
        self.add(carefour)
        self.wait(1)
        self.add(dontcarefour)
        self.wait(1)
        self.play(FadeOut(bootables,careone,dontcareone,caretwo,dontcaretwo,carethree,dontcarethree,carefour,dontcarefour))
        self.wait(1)

        recurse0 = Tex(r"$t_{n,2}= 6^{2n} - \frac{1}{\beta-\alpha}((36\beta-35)\beta^{-n+1} - (36\alpha - 35)\alpha^{-n+1})$")
        recurse0[0][0].set_color(a)
        twobyeq = recurse0.shift(UP*0.5).scale(1.05)

        alpha_color = "#D9ED92"
        beta_color =  "#99D98C"
        gamma_color = "#52B69A"

        alpha_color2 = beta_color
        beta_color2 = alpha_color
        
        twobyeq[0][13].set_color(alpha_color)
        twobyeq[0][32].set_color(alpha_color)
        twobyeq[0][37].set_color(alpha_color)

        twobyeq[0][11].set_color(beta_color)
        twobyeq[0][18].set_color(beta_color)
        twobyeq[0][23].set_color(beta_color)

        twobyeqgreek = Tex(r" \\ $\alpha = \frac{1}{2} + \frac{1}{2}\sqrt{\frac{33}{37}}$ \\ $\beta = \frac{1}{2} - \frac{1}{2}\sqrt{\frac{33}{37}}$").shift(UP*-1.2)
        twobyeqgreek[0][0].set_color(alpha_color)
        twobyeqgreek[0][16].set_color(beta_color)

        twobyeqp1 = Tex(r"$\frac{t_{n,2}}{6^{2n}}= \frac{6^{2n}}{6^{2n}} - \frac{1}{(\beta-\alpha)6^{2n}}((36\beta-35)\beta^{-n+1} - (36\alpha - 35)\alpha^{-n+1})$").shift(UP*0.5).scale(1.05)
        twobyeqp1[0][0].set_color(a)

        twobyeqp1[0][22].set_color(alpha_color)
        twobyeqp1[0][45].set_color(alpha_color)
        twobyeqp1[0][50].set_color(alpha_color)

        twobyeqp1[0][20].set_color(beta_color)
        twobyeqp1[0][31].set_color(beta_color)
        twobyeqp1[0][36].set_color(beta_color)
        
        twobyeqp2 = Tex(r"$p_{n,2}= 1 - \frac{1}{(\beta-\alpha)6^{2n}}((36\beta-35)\beta^{-n+1} - (36\alpha - 35)\alpha^{-n+1})$").shift(UP*0.5).scale(1.05)

        twobyeqp2[0][0].set_color(e)

        twobyeqp2[0][12].set_color(alpha_color)
        twobyeqp2[0][35].set_color(alpha_color)
        twobyeqp2[0][40].set_color(alpha_color)

        twobyeqp2[0][10].set_color(beta_color)
        twobyeqp2[0][21].set_color(beta_color)
        twobyeqp2[0][26].set_color(beta_color)

        self.play(Write(twobyeq))
        self.wait(1)
        self.play(Write(twobyeqgreek))
        self.wait(1)
        self.play(Transform(twobyeq,twobyeqp1))
        self.wait(1)
        self.play(ReplacementTransform(twobyeq,twobyeqp2))
        self.wait(1)

        twobyeqp2.generate_target()
        twobyeqp2.target.shift(UP*1)

        self.play(MoveToTarget(twobyeqp2),FadeOut(twobyeqgreek))
        self.wait(1)

        twobyeqp25 = Tex(r"$p_{5,2}= 1 - \frac{1}{(\beta-\alpha)6^{10}}((36\beta-35)\beta^{-4} - (36\alpha - 35)\alpha^{-4})$").shift(UP*1.5).scale(1.05)
        twobyeqp25[0][0].set_color(e)

        twobyeqp25[0][12].set_color(alpha_color)
        twobyeqp25[0][33].set_color(alpha_color)
        twobyeqp25[0][38].set_color(alpha_color)

        twobyeqp25[0][10].set_color(beta_color)
        twobyeqp25[0][21].set_color(beta_color)
        twobyeqp25[0][26].set_color(beta_color)
        
        twobyeqp26 = Tex(r"$p_{6,2}= 1 - \frac{1}{(\beta-\alpha)6^{12}}((36\beta-35)\beta^{-5} - (36\alpha - 35)\alpha^{-5})$").shift(UP*1.5).scale(1.05)
        twobyeqp26[0][0].set_color(e)

        twobyeqp26[0][12].set_color(alpha_color)
        twobyeqp26[0][33].set_color(alpha_color)
        twobyeqp26[0][38].set_color(alpha_color)

        twobyeqp26[0][10].set_color(beta_color)
        twobyeqp26[0][21].set_color(beta_color)
        twobyeqp26[0][26].set_color(beta_color)

        twobyeqp27 = Tex(r"$p_{7,2}= 1 - \frac{1}{(\beta-\alpha)6^{14}}((36\beta-35)\beta^{-6} - (36\alpha - 35)\alpha^{-6})$").shift(UP*1.5).scale(1.05)
        twobyeqp27[0][0].set_color(e)

        twobyeqp27[0][12].set_color(alpha_color)
        twobyeqp27[0][33].set_color(alpha_color)
        twobyeqp27[0][38].set_color(alpha_color)

        twobyeqp27[0][10].set_color(beta_color)
        twobyeqp27[0][21].set_color(beta_color)
        twobyeqp27[0][26].set_color(beta_color)

        twobyeqp28 = Tex(r"$p_{8,2}= 1 - \frac{1}{(\beta-\alpha)6^{16}}((36\beta-35)\beta^{-7} - (36\alpha - 35)\alpha^{-7})$").shift(UP*1.5).scale(1.05)
        twobyeqp28[0][0].set_color(e)

        twobyeqp28[0][12].set_color(alpha_color)
        twobyeqp28[0][33].set_color(alpha_color)
        twobyeqp28[0][38].set_color(alpha_color)

        twobyeqp28[0][10].set_color(beta_color)
        twobyeqp28[0][21].set_color(beta_color)
        twobyeqp28[0][26].set_color(beta_color)
        
        twobyeqp29 = Tex(r"$p_{9,2}= 1 - \frac{1}{(\beta-\alpha)6^{18}}((36\beta-35)\beta^{-8} - (36\alpha - 35)\alpha^{-8})$").shift(UP*1.5).scale(1.05)
        twobyeqp29[0][0].set_color(e)

        twobyeqp29[0][12].set_color(alpha_color)
        twobyeqp29[0][33].set_color(alpha_color)
        twobyeqp29[0][38].set_color(alpha_color)

        twobyeqp29[0][10].set_color(beta_color)
        twobyeqp29[0][21].set_color(beta_color)
        twobyeqp29[0][26].set_color(beta_color)

        twobyeqp210 = Tex(r"$p_{10,2}= 1 - \frac{1}{(\beta-\alpha)6^{20}}((36\beta-35)\beta^{-9} - (36\alpha - 35)\alpha^{-9})$").shift(UP*1.5).scale(1.05)
        twobyeqp210[0][0].set_color(e)

        twobyeqp210[0][13].set_color(alpha_color)
        twobyeqp210[0][34].set_color(alpha_color)
        twobyeqp210[0][39].set_color(alpha_color)

        twobyeqp210[0][11].set_color(beta_color)
        twobyeqp210[0][22].set_color(beta_color)
        twobyeqp210[0][27].set_color(beta_color)

        table4label = MathTex(r"\mathbf{p_{n,m}}")
        table4label[0][0].set_color(e)
        table4 = MathTable(
            [
            ["","","","","",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(5,11)],
            row_labels=[Tex(str(2))],
            top_left_entry=table4label
        ).scale(0.65).shift(UP*-1.5)

        table5label = MathTex(r"\mathbf{p_{n,m}}")
        table5label[0][0].set_color(e)
        table5 = MathTable(
            [
            [0.0032,"","","","",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(5,11)],
            row_labels=[Tex(str(2))],
            top_left_entry=table5label
        ).scale(0.65).shift(UP*-1.5)

        table6label = MathTex(r"\mathbf{p_{n,m}}")
        table6label[0][0].set_color(e)
        table6 = MathTable(
            [
            [0.0032,0.0039,"","","",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(5,11)],
            row_labels=[Tex(str(2))],
            top_left_entry=table6label
        ).scale(0.65).shift(UP*-1.5)

        table7label = MathTex(r"\mathbf{p_{n,m}}")
        table7label[0][0].set_color(e)
        table7 = MathTable(
            [
            [0.0032,0.0039,0.0047,"","",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(5,11)],
            row_labels=[Tex(str(2))],
            top_left_entry=table7label
        ).scale(0.65).shift(UP*-1.5)

        table8label = MathTex(r"\mathbf{p_{n,m}}")
        table8label[0][0].set_color(e)
        table8 = MathTable(
            [
            [0.0032,0.0039,0.0047,0.0055,"",""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(5,11)],
            row_labels=[Tex(str(2))],
            top_left_entry=table8label
        ).scale(0.65).shift(UP*-1.5)

        table9label = MathTex(r"\mathbf{p_{n,m}}")
        table9label[0][0].set_color(e)
        table9 = MathTable(
            [
            [0.0032,0.0039,0.0047,0.0055,0.0063,""]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(5,11)],
            row_labels=[Tex(str(2))],
            top_left_entry=table9label
        ).scale(0.65).shift(UP*-1.5)

        table10label = MathTex(r"\mathbf{p_{n,m}}")
        table10label[0][0].set_color(e)
        table10 = MathTable(
            [
            [0.0032,0.0039,0.0047,0.0055,0.0063,0.0071]
             ],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(5,11)],
            row_labels=[Tex(str(2))],
            top_left_entry=table10label
        ).scale(0.65).shift(UP*-1.5)

        def twobyn(n):
            terms = [0,0,1]
            prob = [0,0,1/(6**4)]

            if n >= 3:
                for j in range(3,n+1):
                    sum = 0
                    for i in range(2,j+1):
                        sum += ((36**(j-i)) - terms[j-i])

                    val = 36*terms[j-1] + sum
                    terms.append(val)
                    prob.append(round((val/(36**j)), 4))
            return prob
        
        length = 890
        longboy = twobyn(length)[5:]
        print("Array calculated.")

        table11label = MathTex(r"\mathbf{p_{n,m}}")
        table11label[0][0].set_color(e)
        table11 = MathTable(
            [longboy],
            include_outer_lines=True,
            col_labels=[Tex(str(n)) for n in range(5,length+1)],
            row_labels=[Tex(str(2))],
            top_left_entry=table11label
        ).scale(0.65).shift(UP*-1.5)
        table11.shift(RIGHT*abs(table10.width - table11.width)/2)
        table11.add_highlighted_cell((2, 871), color=e)

        self.play(FadeIn(table4))
        self.wait(1)
        self.play(Transform(table4,table5),ReplacementTransform(twobyeqp2,twobyeqp25))
        self.wait(1)
        self.play(Transform(table4,table6),TransformMatchingTex(twobyeqp25,twobyeqp26))
        self.wait(1)
        self.play(Transform(table4,table7),TransformMatchingTex(twobyeqp26,twobyeqp27))
        self.wait(1)
        self.play(Transform(table4,table8),TransformMatchingTex(twobyeqp27,twobyeqp28))
        self.wait(1)
        self.play(Transform(table4,table9),TransformMatchingTex(twobyeqp28,twobyeqp29))
        self.wait(1)
        self.play(ReplacementTransform(table4,table10),TransformMatchingTex(twobyeqp29,twobyeqp210))
        self.wait(1)

        self.play(FadeIn(table11),FadeOut(table10))
        self.wait(1)

        table11.generate_target()
        table11.target.shift(RIGHT*-length*1.65).shift(RIGHT*(-2.8))

        self.play(MoveToTarget(table11),run_time=3.5)
        self.wait(1)
        self.play(FadeOut(table11),FadeOut(twobyeqp210))
        self.wait(1)
        
        introtex = Tex(r"$t_{n,3}$")

        threebyn1 = Tex(r"$$t_{n,3} = 6^{3n} - f(n) + 12f(n-1) - 34f(n-2)$$").scale(1.1).shift(UP*2)
        threebyn2 = Tex(r"$f(n) = \frac{\alpha^{n+2}}{(\alpha-\beta)(\alpha-\gamma)} + \frac{\beta^{n+2}}{(\beta-\alpha)(\beta-\gamma)} + \frac{\gamma^{n+2}}{(\gamma-\alpha)(\gamma-\beta)}$")

        threebyn2[0][5].set_color(alpha_color2)
        threebyn2[0][11].set_color(alpha_color2)
        threebyn2[0][16].set_color(alpha_color2)
        threebyn2[0][29].set_color(alpha_color2)
        threebyn2[0][45].set_color(alpha_color2)

        threebyn2[0][13].set_color(beta_color2)
        threebyn2[0][21].set_color(beta_color2)
        threebyn2[0][27].set_color(beta_color2)
        threebyn2[0][32].set_color(beta_color2)
        threebyn2[0][50].set_color(beta_color2)

        threebyn2[0][18].set_color(gamma_color)
        threebyn2[0][34].set_color(gamma_color)
        threebyn2[0][37].set_color(gamma_color)
        threebyn2[0][43].set_color(gamma_color)
        threebyn2[0][48].set_color(gamma_color)

        threebyn3 = Tex(r"where $\alpha$, $\beta$, and $\gamma$ are the reciprocals \\ of the roots of $1-228x+2699x^2 - 7758x^3$").shift(UP*-1.8)

        threebyn3[0][5].set_color(beta_color2)
        threebyn3[0][7].set_color(alpha_color2)
        threebyn3[0][12].set_color(gamma_color)

        self.play(Write(threebyn1))
        self.play(Write(threebyn2),run_time=1)
        self.play(Write(threebyn3),run_time=1)
        self.wait(1)
        self.play(FadeOut(threebyn1), \
                  FadeOut(threebyn2), \
                  FadeOut(threebyn3))
        self.wait(1)

        threebyngf = Tex(r"$$\sum_{n \geq 2}t_{n,3}x^n = \frac{(73-414x)x^2}{(1-216x)(1-228x+2699x^2 - 7758x^3)}$$").scale(1.1)
        threebyngf[0][4].set_color(a)

        self.play(Write(threebyngf))
        self.wait(1)
        self.play(FadeOut(threebyngf))
        self.wait(1)

        whatabout = Tex(r"What about more rows?")
        self.play(Write(whatabout),run_time=1)
        self.wait(1)
        sometimesyou = Tex(r"That's ok!").shift(UP*2.2)
        self.play(ReplacementTransform(whatabout,sometimesyou))
        self.wait(1)
        self.play(FadeOut(sometimesyou))
        self.wait(1)

# Further Questions
class Section8(Scene):
    def construct(self):
        self.camera.background_color = "#181818"
        hilight_color = "#C4A484"
        hilight_text = "#9b5de5"

        title = Tex(r"Further Questions").scale(1.5)

        self.wait(1)
        self.play(Write(title),run_time=1)
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        limit = Tex(r"$$\lim_{n,m \to \infty}p_{n,m} = 1$$")
        limit[0][8].set_color(e)
        self.play(Write(limit),run_time=1)
        self.wait(1)
        self.play(FadeOut(limit))
        self.wait(1)

        square0 = Square(side_length=1,color=d)
        line0 = Line(start=square0.get_edge_center(DOWN),end=square0.get_edge_center(RIGHT), stroke_width=8).set_color(h)
        vsquare0 = VGroup(square0)
        vline0 = VGroup(line0,square0.copy())
        svsquare0 = vsquare0.copy().shift(LEFT*6)
        svline0 = vline0.copy().shift(LEFT*6)
        
        square1 = Square(side_length=1,color=d)
        line1 = Line(start=square1.get_edge_center(DOWN),end=square1.get_edge_center(LEFT), stroke_width=8).set_color(h)
        vsquare1 = VGroup(square1)
        vline1 = VGroup(line1,square1.copy())
        svsquare1 = vsquare1.copy().shift(LEFT*4)
        svline1 = vline1.copy().shift(LEFT*4)

        square2 = Square(side_length=1,color=d)
        line2 = Line(start=square2.get_edge_center(LEFT),end=square2.get_edge_center(UP), stroke_width=8).set_color(h)
        vsquare2 = VGroup(square2)
        vline2 = VGroup(line2,square2.copy())
        svsquare2 = vsquare2.copy().shift(LEFT*2)
        svline2 = vline2.copy().shift(LEFT*2)

        square3 = Square(side_length=1,color=d)
        line3 = Line(start=square3.get_edge_center(UP),end=square3.get_edge_center(RIGHT), stroke_width=8).set_color(h)
        vsquare3 = VGroup(square3)
        vline3 = VGroup(line3,square3.copy())
        svsquare3 = vsquare3.copy().shift(RIGHT*0)
        svline3 = vline3.copy().shift(RIGHT*0)

        square4 = Square(side_length=1,color=d)
        line4 = Line(start=square4.get_edge_center(DOWN),end=square4.get_edge_center(UP), stroke_width=8).set_color(h)
        vsquare4 = VGroup(square4)
        vline4 = VGroup(line4,square4.copy())
        svsquare4 = vsquare4.copy().shift(RIGHT*2)
        svline4 = vline4.copy().shift(RIGHT*2)

        square5 = Square(side_length=1,color=d)
        line5 = Line(start=square5.get_edge_center(LEFT),end=square5.get_edge_center(RIGHT), stroke_width=8).set_color(h)
        vsquare5 = VGroup(square5)
        vline5 = VGroup(line5,square5.copy())
        svsquare5 = vsquare5.copy().shift(RIGHT*4)
        svline5 = vline5.copy().shift(RIGHT*4)

        square6 = Square(side_length=1,color=d)
        line6 = Line(start=square6.get_edge_center(LEFT),end=square6.get_edge_center(RIGHT), stroke_width=8).set_color(h)
        vsquare6 = VGroup(square6)
        vline6 = VGroup(line6)
        svsquare6 = vsquare6.copy().shift(RIGHT*6)
        svline6 = vline6.copy().shift(RIGHT*6)

        tile0 = vsquare0 + vline0
        tile1 = vsquare1 + vline1
        tile2 = vsquare2 + vline2
        tile3 = vsquare3 + vline3
        tile4 = vsquare4 + vline4
        tile5 = vsquare5 + vline5

        infinitesaps = VGroup(
            # row 1
            tile0.copy().shift(UP*3.5).shift(RIGHT*-7.5), \
            tile4.copy().shift(UP*3.5).shift(RIGHT*-6.5), \
            tile4.copy().shift(UP*3.5).shift(RIGHT*-5.5), \
            tile2.copy().shift(UP*3.5).shift(RIGHT*-4.5), \
            tile3.copy().shift(UP*3.5).shift(RIGHT*-3.5), \
            tile4.copy().shift(UP*3.5).shift(RIGHT*-2.5), \
            tile5.copy().shift(UP*3.5).shift(RIGHT*-1.5), \
            tile2.copy().shift(UP*3.5).shift(RIGHT*-0.5), \
            tile0.copy().shift(UP*3.5).shift(RIGHT*0.5), \
            tile0.copy().shift(UP*3.5).shift(RIGHT*1.5), \
            tile3.copy().shift(UP*3.5).shift(RIGHT*2.5), \
            tile4.copy().shift(UP*3.5).shift(RIGHT*3.5), \
            tile5.copy().shift(UP*3.5).shift(RIGHT*4.5), \
            tile0.copy().shift(UP*3.5).shift(RIGHT*5.5), \
            tile2.copy().shift(UP*3.5).shift(RIGHT*6.5), \
            tile3.copy().shift(UP*3.5).shift(RIGHT*7.5), \
            # row 2
            tile3.copy().shift(UP*2.5).shift(RIGHT*-7.5), \
            tile2.copy().shift(UP*2.5).shift(RIGHT*-6.5), \
            tile0.copy().shift(UP*2.5).shift(RIGHT*-5.5), \
            tile5.copy().shift(UP*2.5).shift(RIGHT*-4.5), \
            tile0.copy().shift(UP*2.5).shift(RIGHT*-3.5), \
            tile5.copy().shift(UP*2.5).shift(RIGHT*-2.5), \
            tile0.copy().shift(UP*2.5).shift(RIGHT*-1.5), \
            tile3.copy().shift(UP*2.5).shift(RIGHT*-0.5), \
            tile2.copy().shift(UP*2.5).shift(RIGHT*0.5), \
            tile1.copy().shift(UP*2.5).shift(RIGHT*1.5), \
            tile1.copy().shift(UP*2.5).shift(RIGHT*2.5), \
            tile0.copy().shift(UP*2.5).shift(RIGHT*3.5), \
            tile4.copy().shift(UP*2.5).shift(RIGHT*4.5), \
            tile3.copy().shift(UP*2.5).shift(RIGHT*5.5), \
            tile4.copy().shift(UP*2.5).shift(RIGHT*6.5), \
            tile4.copy().shift(UP*2.5).shift(RIGHT*7.5), \
            # row 3
            tile1.copy().shift(UP*1.5).shift(RIGHT*-7.5), \
            tile2.copy().shift(UP*1.5).shift(RIGHT*-6.5), \
            tile0.copy().shift(UP*1.5).shift(RIGHT*-5.5), \
            tile4.copy().shift(UP*1.5).shift(RIGHT*-4.5), \
            tile0.copy().shift(UP*1.5).shift(RIGHT*-3.5), \
            tile5.copy().shift(UP*1.5).shift(RIGHT*-2.5), \
            tile5.copy().shift(UP*1.5).shift(RIGHT*-1.5), \
            tile4.copy().shift(UP*1.5).shift(RIGHT*-0.5), \
            tile3.copy().shift(UP*1.5).shift(RIGHT*0.5), \
            tile0.copy().shift(UP*1.5).shift(RIGHT*1.5), \
            tile3.copy().shift(UP*1.5).shift(RIGHT*2.5), \
            tile2.copy().shift(UP*1.5).shift(RIGHT*3.5), \
            tile1.copy().shift(UP*1.5).shift(RIGHT*4.5), \
            tile1.copy().shift(UP*1.5).shift(RIGHT*5.5), \
            tile1.copy().shift(UP*1.5).shift(RIGHT*6.5), \
            tile0.copy().shift(UP*1.5).shift(RIGHT*7.5), \
            # row 4
            tile4.copy().shift(UP*0.5).shift(RIGHT*-7.5), \
            tile5.copy().shift(UP*0.5).shift(RIGHT*-6.5), \
            tile5.copy().shift(UP*0.5).shift(RIGHT*-5.5), \
            tile3.copy().shift(UP*0.5).shift(RIGHT*-4.5), \
            tile0.copy().shift(UP*0.5).shift(RIGHT*-3.5), \
            tile3.copy().shift(UP*0.5).shift(RIGHT*-2.5), \
            tile0.copy().shift(UP*0.5).shift(RIGHT*-1.5), \
            tile0.copy().shift(UP*0.5).shift(RIGHT*-0.5), \
            tile2.copy().shift(UP*0.5).shift(RIGHT*0.5), \
            tile1.copy().shift(UP*0.5).shift(RIGHT*1.5), \
            tile3.copy().shift(UP*0.5).shift(RIGHT*2.5), \
            # fadein nosap
            # fadein sap
            tile1.copy().shift(UP*0.5).shift(RIGHT*5.5), \
            tile3.copy().shift(UP*0.5).shift(RIGHT*6.5), \
            tile2.copy().shift(UP*0.5).shift(RIGHT*7.5), \
            # row 5
            tile2.copy().shift(UP*-0.5).shift(RIGHT*-7.5), \
            tile3.copy().shift(UP*-0.5).shift(RIGHT*-6.5), \
            tile4.copy().shift(UP*-0.5).shift(RIGHT*-5.5), \
            tile0.copy().shift(UP*-0.5).shift(RIGHT*-4.5), \
            tile4.copy().shift(UP*-0.5).shift(RIGHT*-3.5), \
            tile5.copy().shift(UP*-0.5).shift(RIGHT*-2.5), \
            tile4.copy().shift(UP*-0.5).shift(RIGHT*-1.5), \
            tile2.copy().shift(UP*-0.5).shift(RIGHT*-0.5), \
            tile1.copy().shift(UP*-0.5).shift(RIGHT*0.5), \
            tile1.copy().shift(UP*-0.5).shift(RIGHT*1.5), \
            tile2.copy().shift(UP*-0.5).shift(RIGHT*2.5), \
            tile0.copy().shift(UP*-0.5).shift(RIGHT*3.5), \
            tile3.copy().shift(UP*-0.5).shift(RIGHT*4.5), \
            tile2.copy().shift(UP*-0.5).shift(RIGHT*5.5), \
            tile1.copy().shift(UP*-0.5).shift(RIGHT*6.5), \
            tile0.copy().shift(UP*-0.5).shift(RIGHT*7.5), \
            # row 6
            tile3.copy().shift(UP*-1.5).shift(RIGHT*-7.5), \
            tile2.copy().shift(UP*-1.5).shift(RIGHT*-6.5), \
            tile0.copy().shift(UP*-1.5).shift(RIGHT*-5.5), \
            tile4.copy().shift(UP*-1.5).shift(RIGHT*-4.5), \
            tile5.copy().shift(UP*-1.5).shift(RIGHT*-3.5), \
            tile5.copy().shift(UP*-1.5).shift(RIGHT*-2.5), \
            tile4.copy().shift(UP*-1.5).shift(RIGHT*-1.5), \
            tile2.copy().shift(UP*-1.5).shift(RIGHT*-0.5), \
            tile3.copy().shift(UP*-1.5).shift(RIGHT*0.5), \
            tile1.copy().shift(UP*-1.5).shift(RIGHT*1.5), \
            tile1.copy().shift(UP*-1.5).shift(RIGHT*2.5), \
            tile0.copy().shift(UP*-1.5).shift(RIGHT*3.5), \
            tile3.copy().shift(UP*-1.5).shift(RIGHT*4.5), \
            tile2.copy().shift(UP*-1.5).shift(RIGHT*5.5), \
            tile4.copy().shift(UP*-1.5).shift(RIGHT*6.5), \
            tile5.copy().shift(UP*-1.5).shift(RIGHT*7.5), \
            # row 7
            tile4.copy().shift(UP*-2.5).shift(RIGHT*-7.5), \
            tile5.copy().shift(UP*-2.5).shift(RIGHT*-6.5), \
            tile0.copy().shift(UP*-2.5).shift(RIGHT*-5.5), \
            tile5.copy().shift(UP*-2.5).shift(RIGHT*-4.5), \
            tile2.copy().shift(UP*-2.5).shift(RIGHT*-3.5), \
            tile1.copy().shift(UP*-2.5).shift(RIGHT*-2.5), \
            tile2.copy().shift(UP*-2.5).shift(RIGHT*-1.5), \
            tile2.copy().shift(UP*-2.5).shift(RIGHT*-0.5), \
            tile3.copy().shift(UP*-2.5).shift(RIGHT*0.5), \
            tile1.copy().shift(UP*-2.5).shift(RIGHT*1.5), \
            tile4.copy().shift(UP*-2.5).shift(RIGHT*2.5), \
            tile2.copy().shift(UP*-2.5).shift(RIGHT*3.5), \
            tile1.copy().shift(UP*-2.5).shift(RIGHT*4.5), \
            tile0.copy().shift(UP*-2.5).shift(RIGHT*5.5), \
            tile5.copy().shift(UP*-2.5).shift(RIGHT*6.5), \
            tile5.copy().shift(UP*-2.5).shift(RIGHT*7.5), \
            # row 8
            tile5.copy().shift(UP*-3.5).shift(RIGHT*-7.5), \
            tile4.copy().shift(UP*-3.5).shift(RIGHT*-6.5), \
            tile5.copy().shift(UP*-3.5).shift(RIGHT*-5.5), \
            tile3.copy().shift(UP*-3.5).shift(RIGHT*-4.5), \
            tile2.copy().shift(UP*-3.5).shift(RIGHT*-3.5), \
            tile4.copy().shift(UP*-3.5).shift(RIGHT*-2.5), \
            tile1.copy().shift(UP*-3.5).shift(RIGHT*-1.5), \
            tile2.copy().shift(UP*-3.5).shift(RIGHT*-0.5), \
            tile0.copy().shift(UP*-3.5).shift(RIGHT*0.5), \
            tile2.copy().shift(UP*-3.5).shift(RIGHT*1.5), \
            tile2.copy().shift(UP*-3.5).shift(RIGHT*2.5), \
            tile4.copy().shift(UP*-3.5).shift(RIGHT*3.5), \
            tile0.copy().shift(UP*-3.5).shift(RIGHT*4.5), \
            tile4.copy().shift(UP*-3.5).shift(RIGHT*5.5), \
            tile5.copy().shift(UP*-3.5).shift(RIGHT*6.5), \
            tile3.copy().shift(UP*-3.5).shift(RIGHT*7.5), \
        )

        infinitesapcell = VGroup(tile0.copy().shift(UP*0.5).shift(RIGHT*4.5))
        infinitenosapcell = VGroup(tile4.copy().shift(UP*0.5).shift(RIGHT*3.5))
        
        hisquare3 = Square(side_length=1,color=d,fill_color=hilight_color,fill_opacity=0.8)
        shisquare3 = Square(side_length=1,color=d)
        hiline3 = Line(start=square3.get_edge_center(DOWN),end=square3.get_edge_center(RIGHT), stroke_width=8).set_color(h)
        cellhilight1 = VGroup(hisquare3, hiline3,shisquare3).shift(UP*0.5).shift(RIGHT*4.5)

        hiisquare3 = Square(side_length=1,color=d,fill_color=hilight_color,fill_opacity=0.8)
        shiisquare3 = Square(side_length=1,color=d)
        hiiline3 = Line(start=square3.get_edge_center(UP),end=square3.get_edge_center(DOWN), stroke_width=8).set_color(h)
        cellhilight2 = VGroup(hiisquare3, hiiline3,shiisquare3).shift(UP*0.5).shift(RIGHT*3.5)

        self.play(FadeIn(infinitesaps),FadeIn(infinitesapcell),FadeIn(infinitenosapcell))
        self.wait(1)
        self.play(FadeIn(cellhilight1))
        self.wait(1)
        self.play(FadeOut(cellhilight1),FadeIn(cellhilight2))
        self.wait(1)
        self.play(FadeOut(cellhilight2))
        self.wait(1)
        self.play(FadeOut(infinitesaps),FadeOut(infinitesapcell),FadeOut(infinitenosapcell))
        self.wait(1)

        seqtext = Tex(r"Let $a_n$ be the number of \\ shapes of perimeter $2n$ (A002931)").shift(UP*1.5)

        seq = Tex(r"$$\sum_{\text{even } n \geq 4} \frac{n a_{n}}{6^{n}}$$").shift(UP*-1.5)
        seq1 = Tex(r"$$ = 0.003382\dots$$").shift(UP*-1.26).shift(RIGHT*2.05)

        seqtext[0][3].set_color(hilight_text)
        seq[0][9].set_color(hilight_text)

        seq.generate_target()
        seq.target.shift(RIGHT*-0.9)

        self.play(FadeIn(seqtext))
        self.wait(1)
        self.play(FadeIn(seq))
        self.wait(1)
        self.play(MoveToTarget(seq))
        self.play(FadeIn(seq1))
        self.wait(1)
        self.play(FadeOut(seq),FadeOut(seqtext),FadeOut(seq1))
        self.wait(1)

        infinitesaps2 = VGroup(
            # row 1
            tile0.copy().shift(UP*3.5).shift(RIGHT*-7.5), \
            tile4.copy().shift(UP*3.5).shift(RIGHT*-6.5), \
            tile4.copy().shift(UP*3.5).shift(RIGHT*-5.5), \
            tile2.copy().shift(UP*3.5).shift(RIGHT*-4.5), \
            tile3.copy().shift(UP*3.5).shift(RIGHT*-3.5), \
            tile4.copy().shift(UP*3.5).shift(RIGHT*-2.5), \
            tile5.copy().shift(UP*3.5).shift(RIGHT*-1.5), \
            tile2.copy().shift(UP*3.5).shift(RIGHT*-0.5), \
            tile0.copy().shift(UP*3.5).shift(RIGHT*0.5), \
            tile0.copy().shift(UP*3.5).shift(RIGHT*1.5), \
            tile0.copy().shift(UP*3.5).shift(RIGHT*2.5), \
            tile1.copy().shift(UP*3.5).shift(RIGHT*3.5), \
            tile5.copy().shift(UP*3.5).shift(RIGHT*4.5), \
            tile0.copy().shift(UP*3.5).shift(RIGHT*5.5), \
            tile2.copy().shift(UP*3.5).shift(RIGHT*6.5), \
            tile3.copy().shift(UP*3.5).shift(RIGHT*7.5), \
            # row 2
            tile3.copy().shift(UP*2.5).shift(RIGHT*-7.5), \
            tile2.copy().shift(UP*2.5).shift(RIGHT*-6.5), \
            tile0.copy().shift(UP*2.5).shift(RIGHT*-5.5), \
            tile5.copy().shift(UP*2.5).shift(RIGHT*-4.5), \
            tile0.copy().shift(UP*2.5).shift(RIGHT*-3.5), \
            tile5.copy().shift(UP*2.5).shift(RIGHT*-2.5), \
            tile0.copy().shift(UP*2.5).shift(RIGHT*-1.5), \
            tile3.copy().shift(UP*2.5).shift(RIGHT*-0.5), \
            tile0.copy().shift(UP*2.5).shift(RIGHT*0.5), \
            tile5.copy().shift(UP*2.5).shift(RIGHT*1.5), \
            tile2.copy().shift(UP*2.5).shift(RIGHT*2.5), \
            tile3.copy().shift(UP*2.5).shift(RIGHT*3.5), \
            tile1.copy().shift(UP*2.5).shift(RIGHT*4.5), \
            tile3.copy().shift(UP*2.5).shift(RIGHT*5.5), \
            tile4.copy().shift(UP*2.5).shift(RIGHT*6.5), \
            tile4.copy().shift(UP*2.5).shift(RIGHT*7.5), \
            # row 3
            tile1.copy().shift(UP*1.5).shift(RIGHT*-7.5), \
            tile2.copy().shift(UP*1.5).shift(RIGHT*-6.5), \
            tile0.copy().shift(UP*1.5).shift(RIGHT*-5.5), \
            tile4.copy().shift(UP*1.5).shift(RIGHT*-4.5), \
            tile0.copy().shift(UP*1.5).shift(RIGHT*-3.5), \
            tile5.copy().shift(UP*1.5).shift(RIGHT*-2.5), \
            tile1.copy().shift(UP*1.5).shift(RIGHT*-1.5), \
            tile4.copy().shift(UP*1.5).shift(RIGHT*-0.5), \
            tile4.copy().shift(UP*1.5).shift(RIGHT*0.5), \
            tile0.copy().shift(UP*1.5).shift(RIGHT*1.5), \
            tile5.copy().shift(UP*1.5).shift(RIGHT*2.5), \
            tile1.copy().shift(UP*1.5).shift(RIGHT*3.5), \
            tile3.copy().shift(UP*1.5).shift(RIGHT*4.5), \
            tile1.copy().shift(UP*1.5).shift(RIGHT*5.5), \
            tile1.copy().shift(UP*1.5).shift(RIGHT*6.5), \
            tile0.copy().shift(UP*1.5).shift(RIGHT*7.5), \
            # row 4
            tile4.copy().shift(UP*0.5).shift(RIGHT*-7.5), \
            tile5.copy().shift(UP*0.5).shift(RIGHT*-6.5), \
            tile5.copy().shift(UP*0.5).shift(RIGHT*-5.5), \
            tile3.copy().shift(UP*0.5).shift(RIGHT*-4.5), \
            tile0.copy().shift(UP*0.5).shift(RIGHT*-3.5), \
            tile3.copy().shift(UP*0.5).shift(RIGHT*-2.5), \
            tile0.copy().shift(UP*0.5).shift(RIGHT*-1.5), \
            tile0.copy().shift(UP*0.5).shift(RIGHT*-0.5), \
            tile4.copy().shift(UP*0.5).shift(RIGHT*0.5), \
            tile4.copy().shift(UP*0.5).shift(RIGHT*1.5), \
            
            # tile3.copy().shift(UP*0.5).shift(RIGHT*2.5), \
            
            tile4.copy().shift(UP*0.5).shift(RIGHT*3.5), \
            tile0.copy().shift(UP*0.5).shift(RIGHT*4.5), \
            tile4.copy().shift(UP*0.5).shift(RIGHT*5.5), \
            tile3.copy().shift(UP*0.5).shift(RIGHT*6.5), \
            tile2.copy().shift(UP*0.5).shift(RIGHT*7.5), \
            # row 5
            tile2.copy().shift(UP*-0.5).shift(RIGHT*-7.5), \
            tile3.copy().shift(UP*-0.5).shift(RIGHT*-6.5), \
            tile4.copy().shift(UP*-0.5).shift(RIGHT*-5.5), \
            tile0.copy().shift(UP*-0.5).shift(RIGHT*-4.5), \
            tile4.copy().shift(UP*-0.5).shift(RIGHT*-3.5), \
            tile5.copy().shift(UP*-0.5).shift(RIGHT*-2.5), \
            tile4.copy().shift(UP*-0.5).shift(RIGHT*-1.5), \
            tile2.copy().shift(UP*-0.5).shift(RIGHT*-0.5), \
            tile4.copy().shift(UP*-0.5).shift(RIGHT*0.5), \
            tile3.copy().shift(UP*-0.5).shift(RIGHT*1.5), \
            tile5.copy().shift(UP*-0.5).shift(RIGHT*2.5), \
            tile2.copy().shift(UP*-0.5).shift(RIGHT*3.5), \
            tile4.copy().shift(UP*-0.5).shift(RIGHT*4.5), \
            tile4.copy().shift(UP*-0.5).shift(RIGHT*5.5), \
            tile1.copy().shift(UP*-0.5).shift(RIGHT*6.5), \
            tile0.copy().shift(UP*-0.5).shift(RIGHT*7.5), \
            # row 6
            tile3.copy().shift(UP*-1.5).shift(RIGHT*-7.5), \
            tile2.copy().shift(UP*-1.5).shift(RIGHT*-6.5), \
            tile0.copy().shift(UP*-1.5).shift(RIGHT*-5.5), \
            tile4.copy().shift(UP*-1.5).shift(RIGHT*-4.5), \
            tile5.copy().shift(UP*-1.5).shift(RIGHT*-3.5), \
            tile5.copy().shift(UP*-1.5).shift(RIGHT*-2.5), \
            tile4.copy().shift(UP*-1.5).shift(RIGHT*-1.5), \
            tile2.copy().shift(UP*-1.5).shift(RIGHT*-0.5), \
            tile4.copy().shift(UP*-1.5).shift(RIGHT*0.5), \
            tile0.copy().shift(UP*-1.5).shift(RIGHT*1.5), \
            tile5.copy().shift(UP*-1.5).shift(RIGHT*2.5), \
            tile5.copy().shift(UP*-1.5).shift(RIGHT*3.5), \
            tile5.copy().shift(UP*-1.5).shift(RIGHT*4.5), \
            tile2.copy().shift(UP*-1.5).shift(RIGHT*5.5), \
            tile4.copy().shift(UP*-1.5).shift(RIGHT*6.5), \
            tile5.copy().shift(UP*-1.5).shift(RIGHT*7.5), \
            # row 7
            tile4.copy().shift(UP*-2.5).shift(RIGHT*-7.5), \
            tile5.copy().shift(UP*-2.5).shift(RIGHT*-6.5), \
            tile0.copy().shift(UP*-2.5).shift(RIGHT*-5.5), \
            tile5.copy().shift(UP*-2.5).shift(RIGHT*-4.5), \
            tile2.copy().shift(UP*-2.5).shift(RIGHT*-3.5), \
            tile1.copy().shift(UP*-2.5).shift(RIGHT*-2.5), \
            tile2.copy().shift(UP*-2.5).shift(RIGHT*-1.5), \
            tile2.copy().shift(UP*-2.5).shift(RIGHT*-0.5), \
            tile3.copy().shift(UP*-2.5).shift(RIGHT*0.5), \
            tile2.copy().shift(UP*-2.5).shift(RIGHT*1.5), \
            tile4.copy().shift(UP*-2.5).shift(RIGHT*2.5), \
            tile2.copy().shift(UP*-2.5).shift(RIGHT*3.5), \
            tile1.copy().shift(UP*-2.5).shift(RIGHT*4.5), \
            tile0.copy().shift(UP*-2.5).shift(RIGHT*5.5), \
            tile5.copy().shift(UP*-2.5).shift(RIGHT*6.5), \
            tile5.copy().shift(UP*-2.5).shift(RIGHT*7.5), \
            # row 8
            tile5.copy().shift(UP*-3.5).shift(RIGHT*-7.5), \
            tile4.copy().shift(UP*-3.5).shift(RIGHT*-6.5), \
            tile5.copy().shift(UP*-3.5).shift(RIGHT*-5.5), \
            tile3.copy().shift(UP*-3.5).shift(RIGHT*-4.5), \
            tile2.copy().shift(UP*-3.5).shift(RIGHT*-3.5), \
            tile4.copy().shift(UP*-3.5).shift(RIGHT*-2.5), \
            tile1.copy().shift(UP*-3.5).shift(RIGHT*-1.5), \
            tile2.copy().shift(UP*-3.5).shift(RIGHT*-0.5), \
            tile0.copy().shift(UP*-3.5).shift(RIGHT*0.5), \
            tile2.copy().shift(UP*-3.5).shift(RIGHT*1.5), \
            tile2.copy().shift(UP*-3.5).shift(RIGHT*2.5), \
            tile4.copy().shift(UP*-3.5).shift(RIGHT*3.5), \
            tile0.copy().shift(UP*-3.5).shift(RIGHT*4.5), \
            tile4.copy().shift(UP*-3.5).shift(RIGHT*5.5), \
            tile5.copy().shift(UP*-3.5).shift(RIGHT*6.5), \
            tile3.copy().shift(UP*-3.5).shift(RIGHT*7.5), \
        )

        infinitesapcell = VGroup(tile3.copy().shift(UP*0.5).shift(RIGHT*2.5))


        hsquare3 = Square(side_length=1,fill_color=hilight_color,fill_opacity=0.8)
        shsquare3 = Square(side_length=1,color=d)
        hline3 = Line(start=square3.get_edge_center(UP),end=square3.get_edge_center(RIGHT), stroke_width=8).set_color(h)
        cellhilight = VGroup(hsquare3, hline3,shsquare3).shift(UP*0.5).shift(RIGHT*2.5)
        
        self.play(FadeIn(infinitesaps2),FadeIn(infinitesapcell))
        self.wait(1)
        self.play(FadeIn(cellhilight))
        self.wait(1)
        self.play(FadeOut(cellhilight))
        self.wait(1)
        self.play(FadeOut(infinitesaps2),FadeOut(infinitesapcell))
        self.wait(1)

# Favorite Comment, Sources, & Outro
class Section9(Scene):
    def construct(self):
        self.camera.background_color = "#181818"

        title = Tex(r"Outro").scale(1.5)

        self.play(Write(title),run_time=1)
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        myBaseTemplate = TexTemplate(
            documentclass="\documentclass[preview]{standalone}"
        )
        myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")

        readings = Tex(r"\textbf{Suggested Reading}").scale(1.1).shift(UP*3).shift(RIGHT*-3.4)

        reading1str = r'\justifying{Mikl\'{o}s B\'{o}na. \textit{A Walk Through Combinatorics: An Introduction to Enumeration and Graph Theory}. 2006.}'
        reading1 = Tex(reading1str,tex_template=myBaseTemplate)
        reading1.scale(0.65).shift(UP*2).shift(RIGHT*0)

        reading2str = r'\justifying{Anthony J. Guttmann. \textit{Polygons, Polyominoes and Polycubes}. 1st. Springer Publishing Company, Incorporated, 2009.}'
        reading2 = Tex(reading2str,tex_template=myBaseTemplate)
        reading2.scale(0.65).shift(UP*1).shift(RIGHT*0)

        source = Tex(r"\textbf{Sources}").scale(1.1).shift(UP*0).shift(RIGHT*-5)

        source1str = r'\justifying{Kyungpyo Hong and Seungsang Oh.  ``\textit{Bounds on Multiple Self-avoiding Polygons}". In: Canadian Mathematical Bulletin 61.3 (Sept.2018),pp. 518-530.}'
        source1 = Tex(source1str,tex_template=myBaseTemplate)
        source1.scale(0.65).shift(UP*-1).shift(RIGHT*0)

        source2str = r'\justifying{Neil J. A. Sloane and The OEIS Foundation Inc. \textit{The Online encyclopedia of integer sequences}}'
        source2 = Tex(source2str,tex_template=myBaseTemplate)
        source2.scale(0.65).shift(UP*-2).shift(RIGHT*0)

        divider = Line(start=array([-7,-2.7,0]),end=array([7,-2.7,0]))

        self.play(Write(readings), run_time=1)
        self.play(Write(reading1), run_time=1)
        self.play(Write(reading2), run_time=1)

        self.play(Write(source), run_time=1)
        self.play(Write(source1), run_time=1)
        self.play(Write(source2), run_time=1)

        self.wait(1)
        self.play(FadeIn(divider))

        moveurg = VGroup(readings,\
                        reading1, \
                        reading2, \
                        source, \
                        source1, \
                        source2,
                        divider)
        
        moveurg.generate_target()
        moveurg.target.shift(UP*3.5)

        ohccomment = ImageMobject(filename_or_array="./ohccomm.png").scale(1.2).shift(UP*-5).shift(RIGHT*-0.7)
        ohccomment.generate_target()
        ohccomment.target.shift(UP*4.5)

        riskcomment = ImageMobject(filename_or_array="./riskcomm.png").scale(1.2).shift(UP*-5).shift(RIGHT*-0.55)
        riskcomment.generate_target()
        riskcomment.target.shift(UP*2.5)

        self.play(MoveToTarget(moveurg))
        self.play(MoveToTarget(ohccomment))
        self.play(MoveToTarget(riskcomment))
        self.wait(1)
        self.play(FadeOut(moveurg),FadeOut(ohccomment),FadeOut(riskcomment))

        thankskim = Tex(r"\justifying{My sincerest thanks to my girlfriend Kimberly \\ who provided the hand-drawn animations!}",tex_template=myBaseTemplate)
        # thankskim = Tex(r"My sincerest thanks to my girlfriend Kimberly \\ who procided the hand-drawn animations!")
        self.play(Write(thankskim),run_time=1)
        self.wait(1)
        self.play(FadeOut(thankskim))
        self.wait(1)

        thanks = Tex(r"Thank you all for watching!")
        self.play(Write(thanks),run_time=1)
        self.wait(1)
        self.play(FadeOut(thanks))
        self.wait(1)

# Thumbnail Render
class Thumbnail(Scene):
    def construct(self):

        square0 = Square(side_length=1, stroke_width=7)
        esquare0 = Square(side_length=1, stroke_width=7)
        line0 = Line(start=square0.get_edge_center(DOWN),end=square0.get_edge_center(RIGHT), stroke_width=8).set_color(RED)
        vtile0 = VGroup(square0,line0,esquare0)
        vtile0.shift(LEFT*2).shift(UP*1)
        
        square1 = Square(side_length=1, stroke_width=7)
        esquare1 = Square(side_length=1, stroke_width=7)
        line1 = Line(start=square1.get_edge_center(DOWN),end=square1.get_edge_center(LEFT), stroke_width=8).set_color(RED)
        vtile1 = VGroup(square1,line1,esquare1)
        vtile1.shift(LEFT*2).shift(UP*-1)

        square2 = Square(side_length=1, stroke_width=7)
        esquare2 = Square(side_length=1, stroke_width=7)
        line2 = Line(start=square2.get_edge_center(LEFT),end=square2.get_edge_center(UP), stroke_width=8).set_color(RED)
        vtile2 = VGroup(square2,line2,esquare2)
        vtile2.shift(LEFT*0).shift(UP*1)

        square3 = Square(side_length=1, stroke_width=7)
        esquare3 = Square(side_length=1, stroke_width=7)
        line3 = Line(start=square3.get_edge_center(UP),end=square3.get_edge_center(RIGHT), stroke_width=8).set_color(RED)
        vtile3 = VGroup(square3,line3,esquare3)
        vtile3.shift(RIGHT*0).shift(UP*-1)

        square4 = Square(side_length=1, stroke_width=7)
        esquare4 = Square(side_length=1, stroke_width=7)
        line4 = Line(start=square4.get_edge_center(DOWN),end=square4.get_edge_center(UP), stroke_width=8).set_color(RED)
        vtile4 = VGroup(square4,line4,esquare4)
        vtile4.shift(RIGHT*2).shift(UP*1)

        square5 = Square(side_length=1, stroke_width=7)
        esquare5 = Square(side_length=1, stroke_width=7)
        line5 = Line(start=square5.get_edge_center(LEFT),end=square5.get_edge_center(RIGHT), stroke_width=8).set_color(RED)
        vtile5 = VGroup(square5,line5,esquare5)
        vtile5.shift(RIGHT*2).shift(UP*-1)

        thumb = vtile0 + \
                vtile1 + \
                vtile2 + \
                vtile3 + \
                vtile4 + \
                vtile5

        self.play(FadeIn(thumb))

# Test Scene
class Test(Scene):
    def construct(self):
        self.camera.background_color = "#181818"

        #color palette test
        colors = VGroup(Square(side_length=1).shift(UP*1).shift(RIGHT*-3).set_color(a) , \
                        Square(side_length=1).shift(UP*1).shift(RIGHT*-1).set_color(b) , \
                        Square(side_length=1).shift(UP*1).shift(RIGHT*1).set_color(c) , \
                        Square(side_length=1).shift(UP*1).shift(RIGHT*3).set_color(d) , \
                        Square(side_length=1).shift(UP*-1).shift(RIGHT*-3).set_color(e) , \
                        Square(side_length=1).shift(UP*-1).shift(RIGHT*-1).set_color(f) , \
                        Square(side_length=1).shift(UP*-1).shift(RIGHT*1).set_color(g) , \
                        Square(side_length=1).shift(UP*-1).shift(RIGHT*3).set_color(h))
        
        tablelabel = MathTex(r"\mathbf{t_{n,m}}")
        tablelabel[0][0].set_color(a)
        table = MathTable(
            [
            [0,0,0,0],
            [0,"","",""],
            [0,"","",""],
            [0,"","",""]
             ],
            # column_labels=[[MathTex(r"n")],[MathTex(r"\lambda(n)")]],
            include_outer_lines=True,
            # element_to_mobject_config={"num_decimal_places":0},
            col_labels=[Tex(str(n)) for n in range(1,5)],
            row_labels=[Tex(str(n)) for n in range(1,5)],
            top_left_entry=tablelabel
        ).scale(0.65)
        # table.get_vertical_lines()[2].set_color(a)
        # table.get_horizontal_lines()[2].set_color(a)

        # trial = VGroup(Text("You can...",font='Latin Modern Sans Demi Cond'), \
        trial = VGroup(Text("You can...",font="Latin Modern Math"), \
                Text(" - ask a professor or peer",font="Latin Modern Math"), \
                Text(" - search online",font="Latin Modern Math"), \
                Text(" - make one up",font="Latin Modern Math")
            ).arrange(DOWN, aligned_edge=LEFT)

        # self.play(Create(trial))
        # self.play(ShowIncreasingSubsets(trial))
        # self.play(Write(colors))
        # self.wait(1)

        t = Table(
          [["Red", "."   , "."   ],
          ["."  ,"Green", "X"   ],
          ["."  ,"."    , "Blue"]],
          row_labels=[Text("R1"), Text("R2"), Text("R3")],
          col_labels=[Text("C1"), Text("C2"), Text("C3")],
          top_left_entry=Text("TOP")
        )

        t.add_highlighted_cell((2, 2), color=PURE_RED)    # opacity of 1
        t.add_highlighted_cell((3, 3), color=PURE_GREEN)  # opacity of 0.25
        t.add_highlighted_cell((4, 4), color=PURE_BLUE)   # opacity of 0.5
        t.add_highlighted_cell((3, 4), color=YELLOW)      # opacity of 0.2
        # the t[i] represents the ith add_highlighted_cell call in reverse
        # order. So, the last highlighted cell will have index 0, the second
        t[0].set_opacity(0.2)   # yellow
        t[1].set_opacity(0.25)  # blue
        t[2].set_opacity(0.5)   # green
        t[3].set_opacity(1)     # red

        # self.add(t)
        # # fades out the selection with a duration of five seconds
        # self.play(t[3].animate.set_opacity(0),run_time=5)
        # t.add_highlighted_cell((3, 2), color=YELLOW)  
        # self.wait()

        gen = Tex(r"GENERATING").shift(UP*1).shift(RIGHT*-2.7).scale(1.5)
        func = Tex(r"FUNCTIONS").shift(UP*1).shift(RIGHT*2.7).scale(1.5)
        are = Tex(r"ARE").shift(UP*-1).shift(RIGHT*-2.7).scale(1.5)
        confus = Tex(r"CONFUSING").shift(UP*-1).shift(RIGHT*1.7).scale(1.5)

        # self.wait(1)
        # self.add(gen)
        # self.wait(1)
        # self.add(func)
        # self.wait(1)
        # self.add(are)
        # self.wait(1)
        # self.add(confus)
        # self.wait(1)
        # self.remove(gen).remove(func).remove(are).remove(confus)

        bootables = VGroup(Tex(r"Power Series").shift(UP*2.5).shift(RIGHT*-3.5).scale(1.2),
                Tex(r"Generating Functions").shift(UP*2.5).shift(RIGHT*3.5).scale(1.2),
                Line(start=[-0.35,-3.25,0], end=[-0.35,3.25,0]),
                Line(start=[-6.5,1.75,0], end=[6.5,1.75,0]))

        careone = Tex(r"-care about convergence").shift(UP*1).shift(RIGHT*-3.5)
        dontcareone = Tex(r"-don't care about convergence").shift(UP*1).shift(RIGHT*3.5)
        caretwo = Tex(r"-care about input").shift(UP*0).shift(RIGHT*-4.2)
        dontcaretwo = Tex(r"-don't care about input").shift(UP*0).shift(RIGHT*2.8)
        carethree = Tex(r"-care about value").shift(UP*-1).shift(RIGHT*-4.2)
        dontcarethree = Tex(r"-don't care about value").shift(UP*-1).shift(RIGHT*2.8)
        carefour = Tex(r"-care about coefficients")
        dontcarefour = carefour.copy().shift(UP*-2).shift(RIGHT*2.8)
        carefour.shift(UP*-2).shift(RIGHT*-3.6)

        # self.play(Write(bootables),run_time=1)
        # self.wait(1)
        # self.add(careone)
        # self.wait(1)
        # self.add(dontcareone)
        # self.wait(1)
        # self.add(caretwo)
        # self.wait(1)
        # self.add(dontcaretwo)
        # self.wait(1)
        # self.add(carethree)
        # self.wait(1)
        # self.add(dontcarethree)
        # self.wait(1)
        # self.add(carefour)
        # self.wait(1)
        # self.add(dontcarefour)
        # self.wait(1)
        # self.play(FadeOut(bootables,careone,dontcareone,caretwo,dontcaretwo,carethree,dontcarethree,carefour,dontcarefour))
        # self.wait(1)

        finalquestions = Tex(r"What is the probability that when you make an $n$ by $m$ mosaics, \\ you get at least one connected shape?").scale(0.8)

        # self.play(Write(finalquestions))
        # self.wait(1)
        # self.play(FadeOut(finalquestions))
        # self.wait(1)

        self.play(Write(table))
        self.wait(1)
        self.play(Indicate(table.get_rows()[1]))
        self.wait(1)




# python3 -m manim -qh -t --format=png mosaicmanim.py Thumbnail

# python3 -m manim -ql -v WARNING OHCmanim.py Equation1
