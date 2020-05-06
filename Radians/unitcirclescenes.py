#!/usr/bin/env python

from manimlib.imports import *

#python -m manim MITintegral\UnitCircle\unitcirclescenes.py Intro -pl
class Intro(GraphScene):
    CONFIG = {
    "x_min" : -12,
    "x_max" : 12,
    "y_min" : -9,
    "y_max" : 9,
    "x_tick_frequency": 2,
    "y_tick_frequency": 2,
    "y_axis_height":9,
    "x_axis_width":12,
    "graph_origin" : ORIGIN,
    "function_color" : RED ,
    "axes_color" : GREEN,
    #"x_labeled_nums" :range(-8,8,2),
    #"y_labeled_nums" :range(-6,6,2),
    "num_graph_anchor_points": 200,

    }
    def construct(self):
        self.setup_axes(animate=False)
        self.x_axis.set_opacity(0)
        self.y_axis.set_opacity(0)

        sinlab=TextMobject("$$\sin(x)$$")
        sinlab.set_color(BLUE)
        coslab=TextMobject("$$\cos(x)$$")
        coslab.set_color(RED)

        sinlab.scale(1.5)
        coslab.scale(1.5)

        sinlab.move_to(LEFT*2.5+UP*2)
        coslab.move_to(RIGHT*2.5+UP*2)


        sin_graph=self.get_graph(self.sin,x_min=-14,x_max=14,set_color=BLUE)
        cos_graph=self.get_graph(self.cos,x_min=-14,x_max=14,stroke_color=RED)

        self.wait()

        self.play(Write(sinlab),Write(coslab))

        self.play(ShowCreation(sin_graph),run_time=1.8)
        self.play(ShowCreation(cos_graph),run_time=1.8)

        self.wait(3)

        self.play(
            ApplyMethod(sin_graph.shift,RIGHT*16),
            ApplyMethod(cos_graph.shift,RIGHT*16),
            FadeOut(sinlab),
            FadeOut(coslab),
            run_time=2
            )

        self.x_axis.set_opacity(1)
        self.y_axis.set_opacity(1)

        self.play(
            ShowCreation(self.x_axis),ShowCreation(self.y_axis),
            )

        angle=math.radians(360)
        circle=Arc(radius=2,angle=angle)

        self.play(ShowCreation(circle))

        arrow=Arrow(np.array([0,0,0]),np.array([2*np.sqrt(2)/2,2*np.sqrt(2)/2,0]),buff=0)

        arrow.set_color(BLUE)

        self.play(ShowCreation(arrow))

        self.wait()

        self.play(Rotating(arrow,radians=PI/2,about_point=ORIGIN),rate=linear,run_time=1)

        self.wait()

        coor=TextMobject("$$(\cos(\\theta),\sin(\\theta))$$")
        coor.scale(0.8)

        coor.next_to(arrow,LEFT+UP)

        self.play(Write(coor),sun_time=0.7)

        self.wait(2)

        self.play(
            FadeOut(self.x_axis),
            FadeOut(self.y_axis),
            FadeOut(circle),
            FadeOut(arrow),
            FadeOut(coor)
            )

        self.wait()

        tri=Polygon(np.array([0,0,0]),np.array([6,0,0]),np.array([6,4,0]),fill_color=BLUE,fill_opacity=0.5)
        tri.set_color(BLUE)

        dot_o=Dot()
        dot_rad=Dot()
        dot_rad.move_to(np.array([2*np.sqrt(13),0,0]))
        hypot=TextMobject("hypotenuse")
        dots=VGroup(dot_o,dot_rad)
        hyp_brac=Brace(dots,UP)
        hypot.next_to(hyp_brac,UP)

        total_hyp=VGroup(hypot,hyp_brac)

        total_hyp.rotate(angle=np.arctan(2/3),about_point=ORIGIN)

        degree=np.arctan(2/3)
        arc=Arc(radius=1,angle=degree)

        theta=TextMobject("$$\\theta$$")
        theta.next_to(arc,RIGHT)
        theta.shift(UP*0.15)

        g_tri=VGroup(tri,arc,theta,hyp_brac,hypot)
        g_tri.shift(DOWN*1.7+LEFT*3)

        tri.set_color(color=[YELLOW,BLUE])

        self.play(ShowCreation(tri))
        self.wait()
        self.play(ShowCreation(arc),Write(theta),run_time=0.3)

        self.wait(2)

        y=TextMobject("opposite")
        ybrac=Brace(tri,RIGHT)
        y.next_to(ybrac,RIGHT)
        x=TextMobject("adjacent")
        xbrac=Brace(tri,DOWN)
        x.next_to(xbrac,DOWN)

        self.play(ShowCreation(ybrac),Write(y))
        self.wait()
        self.play(ShowCreation(xbrac),Write(x))
        self.wait()
        self.play(ShowCreation(hyp_brac),Write(hypot))

        self.wait(2)

        self.play(
            FadeOut(ybrac),
            FadeOut(xbrac),
            FadeOut(x),
            FadeOut(y),
            FadeOut(g_tri)
            )

        self.wait()

        ninety=TextMobject("$$90^{\circ}\\rightarrow$$")
        ninety_t=TextMobject("$$\\frac{\pi}{2}$$")
        ninety_t.set_color(color=[BLUE,YELLOW])
        ninety_t.next_to(ninety,RIGHT,0.2)

        nine_tot=VGroup(ninety,ninety_t)
        nine_tot.move_to(ORIGIN)

        one_e=TextMobject("$$180^{\circ}\\rightarrow$$")
        one_e_t=TextMobject("$$\pi$$")
        one_e_t.next_to(one_e,RIGHT,0.2)
        one_e_t.set_color(color=[BLUE,YELLOW])

        one_tot=VGroup(one_e,one_e_t)
        one_tot.move_to(ORIGIN)

        nine_tot.scale(2)
        one_tot.scale(2)

        self.play(Write(nine_tot))

        self.wait(2)

        self.play(Transform(nine_tot,one_tot))

        self.wait(2)

        self.play(FadeOut(nine_tot))

        thr_part=TextMobject("Understanding the Unit Circle",stroke_color=BLUE,set_color=BLUE,fill_color=BLUE,fill_opacity=0.7,stroke_width=1.5)
        part_1=TextMobject("part 1: understanding radians")

        thr_part.scale(1.6)

        self.play(Write(thr_part))
        self.wait()
        self.play(ApplyMethod(thr_part.shift,2*UP))
        self.play(Write(part_1))
        self.play(ApplyMethod(part_1.scale,1.3))
        self.wait(2)

    def sin(self,x):
        return 2*np.sin(x/2)

    def cos(self,x):
        return 2*np.cos(x/2)

#python -m manim MITintegral\UnitCircle\unitcirclescenes.py RadiansSc -pl
class RadiansSc(GraphScene):
    CONFIG = {
    "x_min" : -3,
    "x_max" : 3,
    "y_min" : -2,
    "y_max" : 2,
    "x_tick_frequency": 2,
    "y_tick_frequency": 2,
    "y_axis_height":8,
    "x_axis_width":12,
    "graph_origin" : ORIGIN,
    "function_color" : RED ,
    "axes_color" : GREEN,
    "x_labeled_nums" :range(-2,3,1),
    "y_labeled_nums" :range(-1,2,1),
    "num_graph_anchor_points": 200,

    }
    def construct(self):
        angle=math.radians(360)
        circle=Arc(radius=2,angle=angle)

        arcangle=Arc(radius=0.7,angle=math.radians(45))

        self.add(circle)

        self.wait()

        self.setup_axes(animate=True)

        self.bring_to_back(self.x_axis)
        self.bring_to_back(self.y_axis)

        self.wait()

        radius=Line(np.array([0,0,0]),self.coords_to_point(np.sqrt(2)/2,np.sqrt(2)/2))
        radius.set_color(RED)

        radius_outside=Line(self.coords_to_point(1.5,0.5),self.coords_to_point(1.5,1.5))
        radius_outside.set_color(RED)

        self.play(ShowCreation(radius))

        self.wait(2)

        self.play(Transform(radius,radius_outside))

        self.wait(2)

        len_one=Brace(radius_outside,RIGHT)
        len_one_lab=TextMobject("1")
        len_one_lab.next_to(len_one,RIGHT)

        self.play(ShowCreation(len_one),Write(len_one_lab))

        self.wait(2)

        self.play(FadeOut(len_one),FadeOut(len_one_lab))

        self.wait(2)

        ########################################
        #First radian

        radius_arc=Arc(radius=2,angle=1)
        radius_arc.set_color(RED)

        self.play(Transform(radius,radius_arc))

        self.wait(2)

        #Angle theta for one radian
        one_rad=Arc(radius=0.55,angle=1,stroke_opacity=0.7)
        one_rad_line=Line(ORIGIN,self.coords_to_point(np.cos(1),np.sin(1)))
        one_rad_line_dashed=DashedVMobject(one_rad_line)

        self.play(ShowCreation(one_rad_line_dashed),ShowCreation(one_rad))

        theta=TextMobject("$$\\theta$$")

        theta.move_to(self.coords_to_point(0.4,0.2))
        theta.scale(0.8)

        self.play(Write(theta))

        #Theta label 1
        theta_is=TextMobject("$$\\theta=1$$")
        one_r=TextMobject("radian")
        one_r.next_to(theta_is,RIGHT,0.2)
        label1=VGroup(theta_is,one_r)

        label1.move_to(RIGHT*3.5+UP*2)
        self.play(Write(label1))

        self.wait(2)

        self.play(FadeOut(theta),FadeOut(one_rad_line_dashed),FadeOut(one_rad),FadeOut(label1))

        self.wait()

        ##################################
        #Second radian

        self.play(ShowCreation(radius_outside))

        self.wait(2)

        two_radius_arc=Arc(start_angle=1,angle=1,radius=2)
        two_radius_arc.set_color(RED)
        
        self.play(Transform(radius_outside,two_radius_arc))

        #Angle theta for two radian
        two_rad=Arc(radius=0.55,angle=2,stroke_opacity=0.7)
        two_rad_line=Line(ORIGIN,self.coords_to_point(np.cos(2),np.sin(2)))
        two_rad_line_dashed=DashedVMobject(two_rad_line)

        self.play(ShowCreation(two_rad_line_dashed),ShowCreation(two_rad))

        theta.move_to(self.coords_to_point(0.22,0.34))

        self.play(Write(theta))

        #Theta label 1
        theta_is=TextMobject("$$\\theta=2$$")
        one_r=TextMobject("radians")
        one_r.next_to(theta_is,RIGHT,0.2)
        label1=VGroup(theta_is,one_r)

        label1.move_to(RIGHT*3.5+UP*2)
        self.play(Write(label1))

        self.wait(2)

        self.play(FadeOut(theta),FadeOut(two_rad_line_dashed),FadeOut(two_rad),FadeOut(label1))

        ##################################
        #Third radian

        radius_outside_left=Line(self.coords_to_point(-1.5,1.5),self.coords_to_point(-1.5,0.5))
        radius_outside_left.set_color(RED)

        self.play(ShowCreation(radius_outside_left))

        self.wait(2)

        three_radius_arc=Arc(start_angle=2,angle=1,radius=2)
        three_radius_arc.set_color(RED)
        
        self.play(Transform(radius_outside_left,three_radius_arc))

        #Angle theta for two radian
        three_rad=Arc(radius=0.55,angle=3,stroke_opacity=0.7)
        three_rad_line=Line(ORIGIN,self.coords_to_point(np.cos(3),np.sin(3)))
        three_rad_line_dashed=DashedVMobject(three_rad_line)

        self.play(ShowCreation(three_rad_line_dashed),ShowCreation(three_rad))

        theta.move_to(self.coords_to_point(-0.22,0.4))

        self.play(Write(theta))

        #Theta label 1
        theta_is=TextMobject("$$\\theta=3$$")
        one_r=TextMobject("radians")
        one_r.next_to(theta_is,RIGHT,0.2)
        label1=VGroup(theta_is,one_r)

        label1.move_to(RIGHT*3.5+UP*2)
        self.play(Write(label1))

        self.wait(2)

        extra=Arc(start_angle=PI,angle=(3-PI),radius=2)
        extra.set_color(RED)
        extra.shift(LEFT*0.3)

        self.play(ShowCreation(extra))
        self.wait()
        self.play(ApplyMethod(extra.shift,RIGHT*0.3))
        self.wait()
        self.play(ApplyMethod(extra.shift,LEFT*0.3))

        extra_line=Line(self.coords_to_point(-2,1),self.coords_to_point(-2,1.14159))
        extra_line.set_color(RED)

        self.play(Transform(extra,extra_line))

        self.wait(2)

        approx=TextMobject("$$\\approx 0.14159...$$")
        approx.next_to(extra_line,RIGHT,0.2)

        self.play(Write(approx))

        self.wait(4)

        three_point=TextMobject("$$\\theta\\approx 3.14...$$")
        end_rad=TextMobject("radians")
        end_rad.next_to(three_point, RIGHT,0.2)

        post_add=VGroup(three_point,end_rad)
        post_add.move_to(theta_is.get_center()+RIGHT*1.3)

        pre_add=VGroup(approx,theta_is,one_r)

        self.remove(extra)
        self.add(extra_line)

        extra=Arc(start_angle=PI,angle=(3-PI),radius=2)
        extra.set_color(RED)

        fin=Line(ORIGIN,self.coords_to_point(-1,0))
        fin_dashed=DashedVMobject(fin)

        one_eight_arc=Arc(radius=0.55,angle=PI,stroke_opacity=0.7)

        self.play(
            Transform(pre_add,post_add),
            Transform(extra_line,extra),
            Transform(three_rad_line_dashed,fin_dashed),
            Transform(three_rad,one_eight_arc)
            )
        self.wait(2)

        pi_guy=TextMobject("$$\\theta=\pi$$")
        pi_guy.next_to(end_rad,LEFT,0.2)

        pi_tot=VGroup(pi_guy,end_rad)

        self.play(ReplacementTransform(pre_add,pi_tot))

        self.wait()

        pi_lab=TextMobject("$$\pi$$")
        pi_lab.move_to(self.coords_to_point(-1.15,0.13))
        self.play(ShowCreation(pi_lab))

        self.wait(2)

        #######################################
        #Define the other angles

        #Remake the arc and dashed line
        pi_arc=Arc(radius=0.55,angle=PI,stroke_opacity=0.7)
        our_line=Line(ORIGIN,self.coords_to_point(-1,0))
        our_line_dashed=DashedVMobject(fin)

        #Replace old stuff with new ones
        self.remove(three_rad)
        self.remove(three_rad_line_dashed)
        self.add(pi_arc)
        self.add(our_line_dashed)

        #Define new red arc
        outter_arc=Arc(radius=2,angle=PI)
        outter_arc.set_color(RED)

        self.remove(radius_outside,radius_outside_left,radius,extra,extra_line)
        self.add(outter_arc)

        ##################################################
        #Move to pi over two

        pi_guy_new=TextMobject("$$\\theta=\\frac{1}{2}\pi$$")
        pi_guy_new.next_to(end_rad,LEFT,0.2)

        start_at=PI
        end_at=PI/2

        angle=ValueTracker(start_at)

        corr_term=0

        def arc_update(arc):
            new_arc=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)
            pi_arc.become(new_arc)

        def outter_arc_update(arc):
            new_o_arc=Arc(radius=2,angle=angle.get_value(),stroke_color=RED)
            outter_arc.become(new_o_arc)

        self.play(
            Rotating(our_line_dashed,radians=(end_at-start_at),about_point=ORIGIN),
            UpdateFromFunc(pi_arc,arc_update),
            UpdateFromFunc(outter_arc,outter_arc_update),
            ApplyMethod(theta.move_to,self.coords_to_point(0.35,0.15)),
            Transform(pi_guy,pi_guy_new),
            angle.set_value,(end_at-corr_term),rate_func=linear,run_time=1
            )

        self.wait()

        ######
        #FIX THIS
        pi_lab1=TextMobject("$$\\frac{\pi}{2}$$")
        pi_lab1.scale(0.75)
        pi_lab1.move_to(self.coords_to_point(0.15,1.26))
        self.play(ShowCreation(pi_lab1))

        self.wait(2)

        ##################################################
        #Move to pi over four

        pi_guy_new=TextMobject("$$\\theta=\\frac{1}{4}\pi$$")
        pi_guy_new.next_to(end_rad,LEFT,0.2)

        start_at=PI/2
        end_at=PI/4

        angle=ValueTracker(start_at)

        #corr_term=0

        def arc_update(arc):
            new_arc=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)
            pi_arc.become(new_arc)

        def outter_arc_update(arc):
            new_o_arc=Arc(radius=2,angle=angle.get_value(),stroke_color=RED)
            outter_arc.become(new_o_arc)

        self.play(
            Rotating(our_line_dashed,radians=(end_at-start_at),about_point=ORIGIN),
            UpdateFromFunc(pi_arc,arc_update),
            UpdateFromFunc(outter_arc,outter_arc_update),
            Transform(pi_guy,pi_guy_new),
            angle.set_value,end_at-corr_term,rate_func=linear,run_time=1
            )

        self.wait()

        pi_lab2=TextMobject("$$\\frac{\pi}{4}$$")
        pi_lab2.scale(0.75)
        pi_lab2.move_to(self.coords_to_point(np.sqrt(2)/2+0.2,np.sqrt(2)/2+0.2))
        self.play(ShowCreation(pi_lab2))

        self.wait(2)

        ##################################################
        #Move to three pi over four

        pi_guy_new=TextMobject("$$\\theta=\\frac{3}{4}\pi$$")
        pi_guy_new.next_to(end_rad,LEFT,0.2)

        start_at=PI/4
        end_at=3*PI/4

        angle=ValueTracker(start_at)

        corr_term=0.05

        def arc_update(arc):
            new_arc=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)
            pi_arc.become(new_arc)

        def outter_arc_update(arc):
            new_o_arc=Arc(radius=2,angle=angle.get_value(),stroke_color=RED)
            outter_arc.become(new_o_arc)

        keeper_un=Line(ORIGIN,self.coords_to_point(np.sqrt(2)/2,np.sqrt(2)/2))
        keeper1=DashedVMobject(keeper_un)
        self.add(keeper1)

        self.play(
            Rotating(our_line_dashed,radians=(end_at-start_at),about_point=ORIGIN),
            UpdateFromFunc(pi_arc,arc_update),
            UpdateFromFunc(outter_arc,outter_arc_update),
            Transform(pi_guy,pi_guy_new),
            angle.set_value,end_at+corr_term,rate_func=linear,run_time=1
            )

        self.wait()

        pi_lab3=TextMobject("$$\\frac{3\pi}{4}$$")
        pi_lab3.scale(0.75)
        pi_lab3.move_to(self.coords_to_point(-np.sqrt(2)/2-0.2,np.sqrt(2)/2+0.2))
        self.play(ShowCreation(pi_lab3))

        self.wait(4)

        ##################################################
        #Move to pi

        pi_guy_new=TextMobject("$$\\theta=\\frac{4}{4}\pi$$")
        pi_guy_new.next_to(end_rad,LEFT,0.2)

        start_at=3*PI/4
        end_at=PI

        angle=ValueTracker(start_at)

        ##################
        #Redefine the correcting term
        corr_term=0.05

        def arc_update(arc):
            new_arc=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)
            pi_arc.become(new_arc)

        def outter_arc_update(arc):
            new_o_arc=Arc(radius=2,angle=angle.get_value(),stroke_color=RED)
            outter_arc.become(new_o_arc)

        keeper_un=Line(ORIGIN,self.coords_to_point(-np.sqrt(2)/2,np.sqrt(2)/2))
        keeper2=DashedVMobject(keeper_un)
        self.add(keeper2)

        self.play(
            Rotating(our_line_dashed,radians=(end_at-start_at),about_point=ORIGIN),
            UpdateFromFunc(pi_arc,arc_update),
            UpdateFromFunc(outter_arc,outter_arc_update),
            Transform(pi_guy,pi_guy_new),
            angle.set_value,end_at+corr_term,rate_func=linear,run_time=1
            )


        self.wait(2)

        ##################################################
        #Move to five pi over four

        pi_guy_new=TextMobject("$$\\theta=\\frac{5}{4}\pi$$")
        pi_guy_new.next_to(end_rad,LEFT,0.2)

        start_at=PI
        end_at=5*PI/4

        angle=ValueTracker(start_at)

        #corr_term=0.1

        def arc_update(arc):
            new_arc=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)
            pi_arc.become(new_arc)

        def outter_arc_update(arc):
            new_o_arc=Arc(radius=2,angle=angle.get_value(),stroke_color=RED)
            outter_arc.become(new_o_arc)

        #keeper_un=Line(ORIGIN,self.coords_to_point(np.sqrt(2)/2,np.sqrt(2)/2))
        #keeper=DashedVMobject(keeper_un)
        #self.add(keeper)

        self.play(
            Rotating(our_line_dashed,radians=(end_at-start_at),about_point=ORIGIN),
            UpdateFromFunc(pi_arc,arc_update),
            UpdateFromFunc(outter_arc,outter_arc_update),
            Transform(pi_guy,pi_guy_new),
            angle.set_value,end_at+corr_term,rate_func=linear,run_time=1
            )

        self.wait()

        pi_lab4=TextMobject("$$\\frac{5\pi}{4}$$")
        pi_lab4.scale(0.75)
        pi_lab4.move_to(self.coords_to_point(-np.sqrt(2)/2-0.2,-np.sqrt(2)/2-0.2))
        self.play(ShowCreation(pi_lab4))

        self.wait(2)

        ##################################################
        #Move to three pi over two

        pi_guy_new=TextMobject("$$\\theta=\\frac{6}{4}\pi$$")
        pi_guy_new.next_to(end_rad,LEFT,0.2)

        start_at=5*PI/4
        end_at=3*PI/2

        angle=ValueTracker(start_at)

        #corr_term=0.1

        def arc_update(arc):
            new_arc=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)
            pi_arc.become(new_arc)

        def outter_arc_update(arc):
            new_o_arc=Arc(radius=2,angle=angle.get_value(),stroke_color=RED)
            outter_arc.become(new_o_arc)

        keeper_un=Line(ORIGIN,self.coords_to_point(-np.sqrt(2)/2,-np.sqrt(2)/2))
        keeper3=DashedVMobject(keeper_un)
        self.add(keeper3)

        self.play(
            Rotating(our_line_dashed,radians=(end_at-start_at),about_point=ORIGIN),
            UpdateFromFunc(pi_arc,arc_update),
            UpdateFromFunc(outter_arc,outter_arc_update),
            Transform(pi_guy,pi_guy_new),
            angle.set_value,end_at+corr_term,rate_func=linear,run_time=1
            )

        self.wait()

        pi_lab5=TextMobject("$$\\frac{6\pi}{4}$$")
        pi_lab5.scale(0.75)
        pi_lab5.move_to(self.coords_to_point(0.15,-1.26))
        self.play(ShowCreation(pi_lab5))

        self.wait()

        pi_lab_corr5=TextMobject("$$\\frac{3\pi}{2}$$")
        pi_lab_corr5.scale(0.75)
        pi_lab_corr5.move_to(self.coords_to_point(0.15,-1.26))
        self.play(Transform(pi_lab5,pi_lab_corr5))

        self.wait(2)

        ##################################################
        #Move to seven pi over four

        pi_guy_new=TextMobject("$$\\theta=\\frac{7}{4}\pi$$")
        pi_guy_new.next_to(end_rad,LEFT,0.2)

        start_at=3*PI/2
        end_at=7*PI/4

        angle=ValueTracker(start_at)

        #corr_term=0.1

        def arc_update(arc):
            new_arc=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)
            pi_arc.become(new_arc)

        def outter_arc_update(arc):
            new_o_arc=Arc(radius=2,angle=angle.get_value(),stroke_color=RED)
            outter_arc.become(new_o_arc)

        #keeper_un=Line(ORIGIN,self.coords_to_point(np.sqrt(2)/2,np.sqrt(2)/2))
        #keeper=DashedVMobject(keeper_un)
        #self.add(keeper)

        self.play(
            Rotating(our_line_dashed,radians=(end_at-start_at),about_point=ORIGIN),
            UpdateFromFunc(pi_arc,arc_update),
            UpdateFromFunc(outter_arc,outter_arc_update),
            Transform(pi_guy,pi_guy_new),
            angle.set_value,end_at+corr_term,rate_func=linear,run_time=1
            )

        self.wait()

        pi_lab6=TextMobject("$$\\frac{7\pi}{4}$$")
        pi_lab6.scale(0.75)
        pi_lab6.move_to(self.coords_to_point(np.sqrt(2)/2+0.2,-np.sqrt(2)/2-0.2))
        self.play(ShowCreation(pi_lab6))

        self.wait(2)

        ##################################################
        #Move to two pi

        pi_guy_new=TextMobject("$$\\theta=\\frac{8}{4}\pi$$")
        pi_guy_new.next_to(end_rad,LEFT,0.2)

        start_at=7*PI/4
        end_at=2*PI

        angle=ValueTracker(start_at)

        #corr_term=0.1

        def arc_update(arc):
            new_arc=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)
            pi_arc.become(new_arc)

        def outter_arc_update(arc):
            new_o_arc=Arc(radius=2,angle=angle.get_value(),stroke_color=RED)
            outter_arc.become(new_o_arc)

        keeper_un=Line(ORIGIN,self.coords_to_point(np.sqrt(2)/2,-np.sqrt(2)/2))
        keeper4=DashedVMobject(keeper_un)
        self.add(keeper4)

        self.play(
            Rotating(our_line_dashed,radians=(end_at-start_at),about_point=ORIGIN),
            UpdateFromFunc(pi_arc,arc_update),
            UpdateFromFunc(outter_arc,outter_arc_update),
            Transform(pi_guy,pi_guy_new),
            angle.set_value,end_at+corr_term,rate_func=linear,run_time=1
            )

        self.wait()

        pi_lab7=TextMobject("$$\\frac{8\pi}{4}$$")
        pi_lab7.scale(0.75)
        pi_lab7.move_to(self.coords_to_point(1.22,0.2))
        self.play(ShowCreation(pi_lab7))

        self.wait()

        pi_lab_corr7=TextMobject("$$2\pi$$")
        pi_lab_corr7.move_to(self.coords_to_point(1.22,0.13))
        self.play(Transform(pi_lab7,pi_lab_corr7))

        self.wait()

        pi_lab_corr72=TextMobject("$$0$$")
        pi_lab_corr72.move_to(self.coords_to_point(1.1,0.13))
        self.play(Transform(pi_lab7,pi_lab_corr72))

        self.wait(2)

        quarter_labs=VGroup(
            pi_lab1,
            pi_lab2,
            pi_lab3,
            pi_lab4,
            pi_lab5,
            pi_lab6,
            )

        quarter_keepers=VGroup(
            keeper1,
            keeper2,
            keeper3,
            keeper4
            )

        self.play(
            FadeOut(quarter_labs),
            FadeOut(quarter_keepers),
            FadeOut(pi_arc),
            FadeOut(theta),
            FadeOut(our_line_dashed),
            FadeOut(pi_tot),
            FadeOut(outter_arc)
            )

        self.wait(4)

#python -m manim MITintegral\UnitCircle\unitcirclescenes.py RadiansSc2 -pl
class RadiansSc2(GraphScene):
    CONFIG = {
    "x_min" : -3,
    "x_max" : 3,
    "y_min" : -2,
    "y_max" : 2,
    "x_tick_frequency": 2,
    "y_tick_frequency": 2,
    "y_axis_height":8,
    "x_axis_width":12,
    "graph_origin" : ORIGIN,
    "function_color" : RED ,
    "axes_color" : GREEN,
    "x_labeled_nums" :range(-2,3,1),
    "y_labeled_nums" :range(-1,2,1),
    "num_graph_anchor_points": 200,

    }
    def construct(self):

        corr_term=0

        self.setup_axes(animate=False)
        circle=Arc(radius=2,angle=2*PI)
        self.add(circle)
        pi_lab=TextMobject("$$\pi$$")
        pi_lab.move_to(self.coords_to_point(-1.15,0.13))
        zero=TextMobject("$$0$$")
        zero.move_to(self.coords_to_point(1.1,0.13))
        self.add(pi_lab)
        self.add(zero)
        self.wait(3)

        upper_arc=Arc(radius=2,angle=PI)
        upper_arc.set_color(RED)

        self.play(ShowCreation(upper_arc))

        third1=Arc(radius=2,angle=PI/3)
        third2=Arc(radius=2,start_angle=PI/3,angle=PI/3)
        third3=Arc(radius=2,start_angle=2*PI/3,angle=PI/3)

        top_thirds=VGroup(third1,third2,third3)
        top_thirds.set_color(RED)

        self.remove(upper_arc)
        self.add(top_thirds)

        #distance the thirds should move
        dist=0.5

        self.wait(2)

        sep1_un=Line(ORIGIN,self.coords_to_point(0.5,np.sqrt(3)/2))
        sep1=DashedVMobject(sep1_un)
        sep2_un=Line(ORIGIN,self.coords_to_point(-0.5,np.sqrt(3)/2))
        sep2=DashedVMobject(sep2_un)

        self.play(
            ShowCreation(sep1),
            ShowCreation(sep2)
            )

        self.wait()

        self.play(
            ApplyMethod(third1.shift,(RIGHT+UP)*dist),
            ApplyMethod(third2.shift,UP*np.sqrt(2*np.power(dist,2))),
            ApplyMethod(third3.shift,(LEFT+UP)*dist),
            )
        self.wait(2)
        self.play(
            ApplyMethod(third1.shift,(LEFT+DOWN)*dist),
            ApplyMethod(third2.shift,DOWN*np.sqrt(2*np.power(dist,2))),
            ApplyMethod(third3.shift,(RIGHT+DOWN)*dist),
            )
        self.wait(4)

        angle=ValueTracker(0)

        def arc_update(arc):
            new_arc=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)
            pi_arc.become(new_arc)

        def upper_arc_update(arc):
            new_o_arc=Arc(radius=2,angle=angle.get_value(),stroke_color=RED)
            upper_arc.become(new_o_arc)

        pi_arc=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)

        self.add(pi_arc)

        theta=TextMobject("$$\\theta$$")
        theta.scale(0.8)
        theta.move_to(self.coords_to_point(0.35,0.15))

        #Pi over 3
        self.play(
            UpdateFromFunc(pi_arc,arc_update),
            ShowCreation(theta),
            angle.set_value,PI/3,rate_func=linear,run_time=1
            )

        self.wait()

        pi_th=TextMobject("$$\\frac{\pi}{3}$$")
        pi_th.scale(0.75)
        pi_th.move_to(self.coords_to_point(0.7,(np.sqrt(3)/2)+0.2))

        upper_lab=TextMobject("$$\\theta=$$")
        upper_lab.move_to(RIGHT*3.2+UP*2)
        pi_th_l=TextMobject("$$\\frac{\pi}{3}$$")
        radians=TextMobject("radians")

        pi_th_l.next_to(upper_lab,RIGHT,0.2)
        radians.next_to(pi_th_l,RIGHT,0.2)
        lab_group=VGroup(upper_lab,pi_th_l,radians)

        self.play(ShowCreation(pi_th),ShowCreation(lab_group))

        self.wait(2)

        #2Pi over 3

        tpi_th=TextMobject("$$\\frac{2\pi}{3}$$")
        tpi_th.scale(0.75)
        tpi_th.move_to(self.coords_to_point(-0.7,(np.sqrt(3)/2)+0.2))

        tpi_th_l=TextMobject("$$\\frac{2\pi}{3}$$")
        tpi_th_l.next_to(upper_lab,RIGHT,0.2)

        self.play(
            UpdateFromFunc(pi_arc,arc_update),

            ShowCreation(tpi_th),
            Transform(pi_th_l,tpi_th_l),
            ApplyMethod(radians.next_to,tpi_th_l,RIGHT,0.2),

            angle.set_value,2*PI/3,rate_func=linear,run_time=1
            )

        self.wait(2)

        #3Pi over 3

        thpi_th_l=TextMobject("$$\\frac{3\pi}{3}$$")
        thpi_th_l.next_to(upper_lab,RIGHT,0.2)

        dashed_un=Line(ORIGIN,self.coords_to_point(-1,0))
        dashed=DashedVMobject(dashed_un)

        self.play(
            UpdateFromFunc(pi_arc,arc_update),
            Transform(pi_th_l,thpi_th_l),
            ApplyMethod(radians.next_to,thpi_th_l,RIGHT,0.2),
            angle.set_value,PI,rate_func=linear,run_time=1
            )
        self.play(ShowCreation(dashed))
        self.wait(2)

        ####################################
        #Rest of the angles

        corr_term=0.05

        #Four############################################
        self.remove(third1,third2,third3)
        self.add(upper_arc)

        fpi_th_l=TextMobject("$$\\frac{4\pi}{3}$$")
        fpi_th_l.next_to(upper_lab,RIGHT,0.2)

        self.play(
            UpdateFromFunc(upper_arc,upper_arc_update),
            UpdateFromFunc(pi_arc,arc_update),
            Transform(pi_th_l,fpi_th_l),
            ApplyMethod(radians.next_to,fpi_th_l,RIGHT,0.2),
            Rotating(dashed,about_point=ORIGIN,radians=PI/3),
            angle.set_value,4*PI/3+corr_term,rate_func=linear,run_time=1
            )

        label1=TextMobject("$$\\frac{4\pi}{3}$$")
        label1.scale(0.8)
        label1.move_to(self.coords_to_point(-0.7,-(np.sqrt(3)/2)-0.2))

        self.wait()

        self.play(ShowCreation(label1))

        self.wait(3)

        #Five############################################

        fipi_th_l=TextMobject("$$\\frac{5\pi}{3}$$")
        fipi_th_l.next_to(upper_lab,RIGHT,0.2)

        keeper_un=Line(ORIGIN,self.coords_to_point(-0.5,-np.sqrt(3)/2))
        keeper=DashedVMobject(keeper_un)

        self.add(keeper)

        self.play(
            UpdateFromFunc(upper_arc,upper_arc_update),
            UpdateFromFunc(pi_arc,arc_update),
            Transform(pi_th_l,fipi_th_l),
            ApplyMethod(radians.next_to,fipi_th_l,RIGHT,0.2),
            Rotating(dashed,about_point=ORIGIN,radians=PI/3),
            angle.set_value,5*PI/3+corr_term,rate_func=linear,run_time=1
            )

        label2=TextMobject("$$\\frac{5\pi}{3}$$")
        label2.scale(0.8)
        label2.move_to(self.coords_to_point(0.7,-(np.sqrt(3)/2)-0.2))

        self.wait()

        self.play(ShowCreation(label2))

        self.wait(3)

        #DONE###########################

        spi_th_l=TextMobject("$$2\pi$$")
        spi_th_l.next_to(upper_lab,RIGHT,0.2)

        keeper_un=Line(ORIGIN,self.coords_to_point(0.5,-np.sqrt(3)/2))
        keeper1=DashedVMobject(keeper_un)

        self.add(keeper1)

        self.play(
            UpdateFromFunc(upper_arc,upper_arc_update),
            UpdateFromFunc(pi_arc,arc_update),
            Transform(pi_th_l,spi_th_l),
            ApplyMethod(radians.next_to,spi_th_l,RIGHT,0.2),
            Rotating(dashed,about_point=ORIGIN,radians=PI/3),
            angle.set_value,2*PI+corr_term,rate_func=linear,run_time=1
            )

        self.wait(4)

        self.remove(tpi_th_l)

        self.play(
            FadeOut(upper_arc),
            FadeOut(keeper),
            FadeOut(keeper1),
            FadeOut(pi_th_l),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(lab_group),
            FadeOut(sep1),
            FadeOut(sep2),
            FadeOut(dashed),
            FadeOut(theta),
            FadeOut(pi_th),
            FadeOut(tpi_th),
            FadeOut(pi_arc),
            FadeOut(radians),
            FadeOut(upper_lab)
            )

        self.wait(4)

#python -m manim MITintegral\UnitCircle\unitcirclescenes.py RadiansScSix -pl
class RadiansScSix(GraphScene):
    CONFIG = {
    "x_min" : -3,
    "x_max" : 3,
    "y_min" : -2,
    "y_max" : 2,
    "x_tick_frequency": 2,
    "y_tick_frequency": 2,
    "y_axis_height":8,
    "x_axis_width":12,
    "graph_origin" : ORIGIN,
    "function_color" : RED ,
    "axes_color" : GREEN,
    "x_labeled_nums" :range(-2,3,1),
    "y_labeled_nums" :range(-1,2,1),
    "num_graph_anchor_points": 200,

    }
    def construct(self):

        upper_lab=TextMobject("$$\\theta=$$")
        upper_lab.move_to(RIGHT*3.2+UP*2)
        labt_1=TextMobject("$$\\frac{\pi}{6}$$")
        labt_1.next_to(upper_lab,RIGHT,0.2)
        radians=TextMobject("radians")
        radians.next_to(labt_1,RIGHT,0.2)

        corr_term=0

        theta=TextMobject("$$\\theta$$")
        theta.scale(0.8)

        self.setup_axes(animate=False)
        circle=Arc(radius=2,angle=2*PI)
        self.add(circle)
        pi_lab=TextMobject("$$\pi$$")
        pi_lab.move_to(self.coords_to_point(-1.15,0.13))
        zero=TextMobject("$$0$$")
        zero.move_to(self.coords_to_point(1.1,0.13))
        self.add(pi_lab)
        self.add(zero)
        self.wait(3)

        #Sixth arcs
        upper_half=Arc(radius=2,angle=PI,stroke_color=RED)
        self.play(ShowCreation(upper_half))

        six1=Arc(radius=2,angle=PI/6,stroke_color=RED)
        six2=Arc(radius=2,start_angle=PI/6,angle=PI/6,stroke_color=RED)
        six3=Arc(radius=2,start_angle=2*PI/6,angle=PI/6,stroke_color=RED)
        six4=Arc(radius=2,start_angle=3*PI/6,angle=PI/6,stroke_color=RED)
        six5=Arc(radius=2,start_angle=4*PI/6,angle=PI/6,stroke_color=RED)
        six6=Arc(radius=2,start_angle=5*PI/6,angle=PI/6,stroke_color=RED)

        sixths=VGroup(
            six1,
            six2,
            six3,
            six4,
            six5,
            six6
            )

        self.remove(upper_half)
        self.add(sixths)

        #Sixths dividers
        div_un=Line(ORIGIN,self.coords_to_point(np.sqrt(3)/2,0.5))
        div1=DashedVMobject(div_un)
        div_un=Line(ORIGIN,self.coords_to_point(0.5,np.sqrt(3)/2))
        div2=DashedVMobject(div_un)
        div_un=Line(ORIGIN,self.coords_to_point(-0.5,np.sqrt(3)/2))
        div4=DashedVMobject(div_un)
        div_un=Line(ORIGIN,self.coords_to_point(-np.sqrt(3)/2,0.5))
        div3=DashedVMobject(div_un)

        dividers=VGroup(div1,div2,div4,div3)

        self.wait(2)

        self.play(ShowCreation(dividers))

        self.wait()

        #Move sixths
        dist=0.5

        self.play(
            ApplyMethod(six1.shift,dist*np.array([np.cos(PI/12),np.sin(PI/12),0])),
            ApplyMethod(six2.shift,dist*np.array([np.cos(PI/12+PI/6),np.sin(PI/12+PI/6),0])),
            ApplyMethod(six3.shift,dist*np.array([np.cos(PI/12+2*PI/6),np.sin(PI/12+2*PI/6),0])),
            ApplyMethod(six4.shift,dist*np.array([np.cos(PI/12+3*PI/6),np.sin(PI/12+3*PI/6),0])),
            ApplyMethod(six5.shift,dist*np.array([np.cos(PI/12+4*PI/6),np.sin(PI/12+4*PI/6),0])),
            ApplyMethod(six6.shift,dist*np.array([np.cos(PI/12+5*PI/6),np.sin(PI/12+5*PI/6),0])),
            )

        self.wait(2)

        self.play(
            ApplyMethod(six1.shift,-dist*np.array([np.cos(PI/12),np.sin(PI/12),0])),
            ApplyMethod(six2.shift,-dist*np.array([np.cos(PI/12+PI/6),np.sin(PI/12+PI/6),0])),
            ApplyMethod(six3.shift,-dist*np.array([np.cos(PI/12+2*PI/6),np.sin(PI/12+2*PI/6),0])),
            ApplyMethod(six4.shift,-dist*np.array([np.cos(PI/12+3*PI/6),np.sin(PI/12+3*PI/6),0])),
            ApplyMethod(six5.shift,-dist*np.array([np.cos(PI/12+4*PI/6),np.sin(PI/12+4*PI/6),0])),
            ApplyMethod(six6.shift,-dist*np.array([np.cos(PI/12+5*PI/6),np.sin(PI/12+5*PI/6),0])),
            )

        self.wait(2)

        angle=ValueTracker(0)

        theta_arc=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)

        self.add()

        theta.move_to(self.coords_to_point(0.35,0.09))

        def theta_update(arc):
            new_theta=Arc(radius=0.55,angle=angle.get_value(),stroke_opacity=0.7)
            theta_arc.become(new_theta)

        self.play(
            UpdateFromFunc(theta_arc,theta_update),
            Write(theta),
            angle.set_value,PI/6,rate_func=linear,run_time=1
            )

        self.wait()

        self.play(ShowCreation(upper_lab),ShowCreation(labt_1),ShowCreation(radians))

        self.wait()

        lab1=TextMobject("$$\\frac{\pi}{6}$$")
        lab1.scale(0.75)
        lab1.move_to(self.coords_to_point(np.sqrt(3)/2+0.2,0.54))
        self.play(Write(lab1))

        self.wait(2)

        #############################################
        #Move theta to pi over 3
        to_angle=2*PI/6

        #Label at the top
        labt_2=TextMobject("$$\\frac{2\pi}{6}$$")
        labt_2.move_to(labt_1.get_center())

        #Label on the circle
        lab2_a=TextMobject("$$\\frac{2\pi}{6}$$")
        lab2_a.move_to(self.coords_to_point(0.5+0.1,0.2+np.sqrt(3)/2))
        lab2_a.scale(0.75)
        lab2=TextMobject("$$\\frac{\pi}{3}$$")
        lab2.move_to(lab2_a.get_center())
        lab2.scale(0.75)

        self.play(
            UpdateFromFunc(theta_arc,theta_update),
            Transform(labt_1,labt_2),
            ApplyMethod(radians.next_to,labt_2,RIGHT,0.2),
            angle.set_value,to_angle,rate_func=linear,run_time=1
            )

        self.play(Write(lab2_a))
        self.wait()
        self.play(Transform(lab2_a,lab2))

        self.wait(2)

        #############################################
        #Move theta to pi over 2
        to_angle=PI/2

        #Label at the top
        labt_3=TextMobject("$$\\frac{3\pi}{6}$$")
        labt_3.move_to(labt_1.get_center())

        #Label on the circle
        lab3_a=TextMobject("$$\\frac{3\pi}{6}$$")
        lab3_a.move_to(self.coords_to_point(0.15,1.26))
        lab3_a.scale(0.75)
        lab3=TextMobject("$$\\frac{\pi}{2}$$")
        lab3.move_to(lab3_a.get_center())
        lab3.scale(0.75)

        self.play(
            UpdateFromFunc(theta_arc,theta_update),
            Transform(labt_1,labt_3),
            ApplyMethod(radians.next_to,labt_3,RIGHT,0.2),
            angle.set_value,to_angle,rate_func=linear,run_time=1
            )

        self.play(Write(lab3_a))
        self.wait()
        self.play(Transform(lab3_a,lab3))

        self.wait(2)

        #############################################
        #Move theta to 2 pi over 3
        to_angle=2*PI/3

        #Label at the top
        labt_4=TextMobject("$$\\frac{4\pi}{6}$$")
        labt_4.move_to(labt_1.get_center())

        #Label on the circle
        lab4_a=TextMobject("$$\\frac{4\pi}{6}$$")
        lab4_a.move_to(self.coords_to_point(-0.5-0.1,0.2+np.sqrt(3)/2))
        lab4_a.scale(0.75)
        lab4=TextMobject("$$\\frac{2\pi}{3}$$")
        lab4.move_to(lab4_a.get_center())
        lab4.scale(0.75)

        self.play(
            UpdateFromFunc(theta_arc,theta_update),
            Transform(labt_1,labt_4),
            ApplyMethod(radians.next_to,labt_4,RIGHT,0.2),
            angle.set_value,to_angle,rate_func=linear,run_time=1
            )

        self.play(Write(lab4_a))
        self.wait()
        self.play(Transform(lab4_a,lab4))

        self.wait(2)

        #############################################
        #Move theta to 5 pi over 6
        to_angle=5*PI/6

        #Label at the top
        labt_5=TextMobject("$$\\frac{5\pi}{6}$$")
        labt_5.move_to(labt_1.get_center())

        #Label on the circle
        lab5_a=TextMobject("$$\\frac{5\pi}{6}$$")
        lab5_a.move_to(self.coords_to_point(-np.sqrt(3)/2-0.2,0.54))
        lab5_a.scale(0.75)
        lab5=TextMobject("$$\\frac{2\pi}{3}$$")
        lab5.move_to(lab5_a.get_center())
        lab5.scale(0.75)

        self.play(
            UpdateFromFunc(theta_arc,theta_update),
            Transform(labt_1,labt_5),
            ApplyMethod(radians.next_to,labt_5,RIGHT,0.2),
            angle.set_value,to_angle,rate_func=linear,run_time=1
            )

        self.play(Write(lab5_a))

        self.wait(2)

        #############################################
        #Move theta to 2 pi over 3
        to_angle=PI

        #Label at the top
        labt_6=TextMobject("$$\\frac{6\pi}{6}$$")
        labt_6.move_to(labt_1.get_center())

        #Label on the circle
        #lab4_a=TextMobject("$$\\frac{4\pi}{6}$$")
        #lab4_a.move_to(self.coords_to_point(-0.5-0.1,0.2+np.sqrt(3)/2))
        #lab4_a.scale(0.75)
        #lab4=TextMobject("$$\\frac{2\pi}{3}$$")
        #lab4.move_to(lab4_a.get_center())
        #lab4.scale(0.75)

        self.play(
            UpdateFromFunc(theta_arc,theta_update),
            Transform(labt_1,labt_6),
            ApplyMethod(radians.next_to,labt_5,RIGHT,0.2),
            angle.set_value,to_angle,rate_func=linear,run_time=1
            )

        #self.play(Write(lab4_a))
        #self.wait()
        #self.play(Transform(lab4_a,lab4))

        self.wait(2)

        ##############################
        #Add in red arc
        lower_half=Arc(radius=2,start_angle=0,angle=angle.get_value(),stroke_color=RED)
        self.add(lower_half)

        def low_update(arc):
            new_low_arc=Arc(radius=2,start_angle=0,angle=angle.get_value(),stroke_color=RED)
            lower_half.become(new_low_arc)

        line_un=Line(ORIGIN,self.coords_to_point(-1,0))
        line=DashedVMobject(line_un)
        self.play(ShowCreation(line))
        ##############################
        corr_term=0.05
        #Move theta to 7 pi over 6
        to_angle=7*PI/6

        #Label at the top
        labt_7=TextMobject("$$\\frac{7\pi}{6}$$")
        labt_7.move_to(labt_1.get_center())

        #Label on the circle
        lab7_a=TextMobject("$$\\frac{7\pi}{6}$$")
        lab7_a.move_to(self.coords_to_point(-np.sqrt(3)/2-0.2,-0.54))
        lab7_a.scale(0.75)
        #lab7=TextMobject("$$\\frac{2\pi}{3}$$")
        #lab7.move_to(lab4_a.get_center())
        #lab7.scale(0.75)

        self.play(
            #Move theta bit
            UpdateFromFunc(theta_arc,theta_update),
            Transform(labt_1,labt_7),
            ApplyMethod(radians.next_to,labt_7,RIGHT,0.2),

            #Move red bit and line
            UpdateFromFunc(lower_half,low_update),
            Rotating(line,about_point=ORIGIN,radians=PI/6),

            angle.set_value,to_angle+corr_term,rate_func=linear,run_time=1
            )

        self.play(Write(lab7_a))

        self.wait(2)

        ##########################################
        #Move theta to 4 pi over 3
        to_angle=8*PI/6

        #Label at the top
        labt_8=TextMobject("$$\\frac{8\pi}{6}$$")
        labt_8.move_to(labt_1.get_center())

        #Label on the circle
        lab8_a=TextMobject("$$\\frac{8\pi}{6}$$")
        lab8_a.move_to(self.coords_to_point(-0.5-0.1,-0.25-np.sqrt(3)/2))
        lab8_a.scale(0.75)
        lab8=TextMobject("$$\\frac{4\pi}{3}$$")
        lab8.move_to(lab8_a.get_center())
        lab8.scale(0.75)

        #Keeper
        keeper_un=Line(ORIGIN,self.coords_to_point(-np.sqrt(3)/2,-0.5))
        keeper1=DashedVMobject(keeper_un)
        self.add(keeper1)

        self.play(
            #Move theta bit
            UpdateFromFunc(theta_arc,theta_update),
            Transform(labt_1,labt_8),
            ApplyMethod(radians.next_to,labt_8,RIGHT,0.2),

            #Move red bit and line
            UpdateFromFunc(lower_half,low_update),
            Rotating(line,about_point=ORIGIN,radians=PI/6),

            angle.set_value,to_angle+corr_term,rate_func=linear,run_time=1
            )

        self.play(Write(lab8_a))

        self.wait()

        self.play(Transform(lab8_a,lab8))

        self.wait(2)

        ##########################################
        #Move theta to 3 pi over 2
        to_angle=3*PI/2

        #Label at the top
        labt_9=TextMobject("$$\\frac{9\pi}{6}$$")
        labt_9.move_to(labt_1.get_center())

        #Label on the circle
        lab9_a=TextMobject("$$\\frac{9\pi}{6}$$")
        lab9_a.move_to(self.coords_to_point(0.15,-1.26))
        lab9_a.scale(0.75)
        lab9=TextMobject("$$\\frac{3\pi}{2}$$")
        lab9.move_to(lab9_a.get_center())
        lab9.scale(0.75)

        #Keeper
        keeper_un=Line(ORIGIN,self.coords_to_point(-0.5,-np.sqrt(3)/2))
        keeper2=DashedVMobject(keeper_un)
        self.add(keeper2)

        self.play(
            #Move theta bit
            UpdateFromFunc(theta_arc,theta_update),
            Transform(labt_1,labt_9),
            ApplyMethod(radians.next_to,labt_9,RIGHT,0.2),

            #Move red bit and line
            UpdateFromFunc(lower_half,low_update),
            Rotating(line,about_point=ORIGIN,radians=PI/6),

            angle.set_value,to_angle+corr_term,rate_func=linear,run_time=1
            )

        self.play(Write(lab9_a))

        self.wait()

        self.play(Transform(lab9_a,lab9))

        self.wait(2)

        ##########################################
        #Move theta to 5 pi over 3
        to_angle=5*PI/3

        #Label at the top
        labt_10=TextMobject("$$\\frac{10\pi}{6}$$")
        labt_10.move_to(labt_1.get_center())

        #Label on the circle
        lab10_a=TextMobject("$$\\frac{10\pi}{6}$$")
        lab10_a.move_to(self.coords_to_point(+0.5+0.1,-0.25-np.sqrt(3)/2))
        lab10_a.scale(0.75)
        lab10=TextMobject("$$\\frac{5\pi}{3}$$")
        lab10.move_to(lab10_a.get_center())
        lab10.scale(0.75)

        #Keeper
        #keeper_un=Line(ORIGIN,self.coords_to_point(-0.5,-np.sqrt(3)/2))
        #keeper2=DashedVMobject(keeper_un)
        #self.add(keeper2)

        self.play(
            #Move theta bit
            UpdateFromFunc(theta_arc,theta_update),
            Transform(labt_1,labt_10),
            ApplyMethod(radians.next_to,labt_10,RIGHT,0.2),

            #Make theta move appropriately
            ApplyMethod(upper_lab.next_to,labt_10,LEFT,0.2),

            #Move red bit and line
            UpdateFromFunc(lower_half,low_update),
            Rotating(line,about_point=ORIGIN,radians=PI/6),

            angle.set_value,to_angle+corr_term,rate_func=linear,run_time=1
            )

        self.play(Write(lab10_a))

        self.wait()

        self.play(Transform(lab10_a,lab10))

        self.wait(2)

        ##########################################
        #Move theta to 11 pi over 6
        to_angle=11*PI/6

        #Label at the top
        labt_11=TextMobject("$$\\frac{11\pi}{6}$$")
        labt_11.move_to(labt_1.get_center())

        #Label on the circle
        lab11_a=TextMobject("$$\\frac{11\pi}{6}$$")
        lab11_a.move_to(self.coords_to_point(0.2+np.sqrt(3)/2,-0.6))
        lab11_a.scale(0.75)
        #lab11=TextMobject("$$\\frac{5\pi}{3}$$")
        #lab11.move_to(lab10_a.get_center())
        #lab11.scale(0.75)

        #Keeper
        keeper_un=Line(ORIGIN,self.coords_to_point(0.5,-np.sqrt(3)/2))
        keeper3=DashedVMobject(keeper_un)
        self.add(keeper3)

        self.play(
            #Move theta bit
            UpdateFromFunc(theta_arc,theta_update),
            Transform(labt_1,labt_11),
            ApplyMethod(radians.next_to,labt_11,RIGHT,0.2),

            #Move red bit and line
            UpdateFromFunc(lower_half,low_update),
            Rotating(line,about_point=ORIGIN,radians=PI/6),

            angle.set_value,to_angle+corr_term,rate_func=linear,run_time=1
            )

        self.play(Write(lab11_a))

        #self.wait()

        #self.play(Transform(lab10_a,lab10))

        self.wait(2)

        ##########################################
        #Move theta to 2 pi
        to_angle=2*PI

        #Label at the top
        labt_12=TextMobject("$$2\pi$$")
        labt_12.next_to(upper_lab,RIGHT,0.2)

        #Label on the circle
        #lab12_a=TextMobject("$$\\frac{12\pi}{6}$$")
        #lab12_a.move_to(self.coords_to_point(1.1,))
        #lab12_a.scale(0.75)
        #lab11=TextMobject("$$2\pi$$")
        #lab11.move_to(lab10_a.get_center())
        #lab11.scale(0.75)

        #Keeper
        keeper_un=Line(ORIGIN,self.coords_to_point(np.sqrt(3)/2,-0.5))
        keeper4=DashedVMobject(keeper_un)
        self.add(keeper4)

        self.play(
            #Move theta bit
            UpdateFromFunc(theta_arc,theta_update),
            Transform(labt_1,labt_12),
            ApplyMethod(radians.next_to,labt_12,RIGHT,0.2),


            #Move red bit and line
            UpdateFromFunc(lower_half,low_update),
            Rotating(line,about_point=ORIGIN,radians=PI/6),

            angle.set_value,to_angle+corr_term,rate_func=linear,run_time=1
            )

        #self.play(Write(lab11_a))

        #self.wait()

        #self.play(Transform(lab10_a,lab10))

        self.wait(4)

############################
#SVG PNG CODE
#saved in assets in the main manim directory
#python -m manim MITintegral\UnitCircle\unitcirclescenes.py Pythagoras -pl
class Pythagoras(GraphScene,MovingCameraScene):


    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):


        pyth=ImageMobject("pyth_free")
        pyth.scale(3)
        pyth.move_to(DOWN+RIGHT*3)
        self.play(FadeIn(pyth))
        self.wait(2)

        bubble=SVGMobject("thought_bubble",fill_opacity=0)
        bubble.move_to(LEFT*4.1+UP*2.5)
        bubble.scale(3.2)
        self.play(ShowCreation(bubble))
        self.wait()

        circle=Circle(radius=1,stroke_color=BLUE,fill_color=BLUE,fill_opacity=0.2)
        circle.move_to(LEFT*3.3+UP*1.44)

        #Main scale
        circle.scale(1.4)
        self.play(ShowCreation(circle))

        stroke=5

        #Quarters
        line1=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line1.rotate(about_point=LEFT*3.3+UP*1.44,angle=0)

        line2=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line2.rotate(about_point=LEFT*3.3+UP*1.44,angle=PI/2)

        line3=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line3.rotate(about_point=LEFT*3.3+UP*1.44,angle=PI)

        line4=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line4.rotate(about_point=LEFT*3.3+UP*1.44,angle=3*PI/2)

        self.wait()

        #Play quarters
        self.play(
            ShowCreation(line1),
            ShowCreation(line2),
            ShowCreation(line3),
            ShowCreation(line4),
            )

        self.wait(2)

        #Highlights

        #90
        self.play(
            ApplyMethod(line1.set_color,YELLOW),
            ApplyMethod(line2.set_color,YELLOW),
            )
        self.wait()
        self.play(
            ApplyMethod(line1.set_color,WHITE),
            ApplyMethod(line2.set_color,WHITE),
            )

        #180
        self.play(
            ApplyMethod(line1.set_color,YELLOW),
            ApplyMethod(line3.set_color,YELLOW),
            )
        self.wait()
        self.play(
            ApplyMethod(line1.set_color,WHITE),
            ApplyMethod(line3.set_color,WHITE),
            )

        #270
        self.play(
            ApplyMethod(line1.set_color,YELLOW),
            ApplyMethod(line4.set_color,YELLOW),
            )
        self.wait()
        self.play(
            ApplyMethod(line1.set_color,WHITE),
            ApplyMethod(line4.set_color,WHITE),
            )

        self.wait(4)

        #Twelves
        line5=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line5.rotate(about_point=LEFT*3.3+UP*1.44,angle=PI/6)

        line6=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line6.rotate(about_point=LEFT*3.3+UP*1.44,angle=PI/3)

        line7=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line7.rotate(about_point=LEFT*3.3+UP*1.44,angle=2*PI/3)

        line8=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line8.rotate(about_point=LEFT*3.3+UP*1.44,angle=5*PI/6)

        line9=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line9.rotate(about_point=LEFT*3.3+UP*1.44,angle=7*PI/6)

        line10=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line10.rotate(about_point=LEFT*3.3+UP*1.44,angle=8*PI/6)

        line11=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line11.rotate(about_point=LEFT*3.3+UP*1.44,angle=10*PI/6)

        line12=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        line12.rotate(about_point=LEFT*3.3+UP*1.44,angle=11*PI/6)

        self.wait()

        self.play(
            ShowCreation(line5),
            ShowCreation(line6),
            ShowCreation(line7),
            ShowCreation(line8),
            ShowCreation(line9),
            ShowCreation(line10),
            ShowCreation(line11),
            ShowCreation(line12),
            )

        #Highlights

        self.wait(2)

        #30
        self.play(
            ApplyMethod(line1.set_color,YELLOW),
            ApplyMethod(line5.set_color,YELLOW),
            )
        self.wait()
        self.play(
            ApplyMethod(line1.set_color,WHITE),
            ApplyMethod(line5.set_color,WHITE),
            )

        #60
        self.play(
            ApplyMethod(line1.set_color,YELLOW),
            ApplyMethod(line6.set_color,YELLOW),
            )
        self.wait()
        self.play(
            ApplyMethod(line1.set_color,WHITE),
            ApplyMethod(line6.set_color,WHITE),
            )

        #90
        self.play(
            ApplyMethod(line1.set_color,YELLOW),
            ApplyMethod(line2.set_color,YELLOW),
            )
        self.wait()
        self.play(
            ApplyMethod(line1.set_color,WHITE),
            ApplyMethod(line2.set_color,WHITE),
            )

        self.wait(2)

        #finals
        o1line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o1line.rotate(about_point=LEFT*3.3+UP*1.44,angle=PI/12)

        o2line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o2line.rotate(about_point=LEFT*3.3+UP*1.44,angle=3*PI/12)

        o3line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o3line.rotate(about_point=LEFT*3.3+UP*1.44,angle=5*PI/12)

        o4line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o4line.rotate(about_point=LEFT*3.3+UP*1.44,angle=7*PI/12)

        o5line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o5line.rotate(about_point=LEFT*3.3+UP*1.44,angle=11*PI/12)

        o6line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o6line.rotate(about_point=LEFT*3.3+UP*1.44,angle=13*PI/12)

        o7line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o7line.rotate(about_point=LEFT*3.3+UP*1.44,angle=17*PI/12)

        o8line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o8line.rotate(about_point=LEFT*3.3+UP*1.44,angle=19*PI/12)

        o9line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o9line.rotate(about_point=LEFT*3.3+UP*1.44,angle=23*PI/12)

        o91line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o91line.rotate(about_point=LEFT*3.3+UP*1.44,angle=3*PI/4)

        o92line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o92line.rotate(about_point=LEFT*3.3+UP*1.44,angle=5*PI/4)

        o93line=Line(LEFT*3.3+UP*1.44,LEFT*3.3+UP*1.44+RIGHT*1.4,stroke_width=stroke)
        o93line.rotate(about_point=LEFT*3.3+UP*1.44,angle=7*PI/4)


        self.play(ShowCreation(o2line))

        self.wait(2)

        self.play(
            ShowCreation(o1line),
            ShowCreation(o3line),
            ShowCreation(o4line),
            ShowCreation(o5line),
            ShowCreation(o6line),
            ShowCreation(o7line),
            ShowCreation(o8line),
            ShowCreation(o9line),
            ShowCreation(o91line),
            ShowCreation(o92line),
            ShowCreation(o93line),
            )

        self.wait(4)

        opacity=0.25

        q_mark=TextMobject("?",fill_color=BLUE,fill_opacity=0.4,stroke_color=BLUE,stroke_width=2)
        q_mark.scale(4)
        q_mark.move_to(LEFT*3.28+UP*1.5)

        self.play(
            ApplyMethod(line1.set_opacity,opacity),
            ApplyMethod(line2.set_opacity,opacity),
            ApplyMethod(line3.set_opacity,opacity),
            ApplyMethod(line4.set_opacity,opacity),
            ApplyMethod(line5.set_opacity,opacity),
            ApplyMethod(line6.set_opacity,opacity),
            ApplyMethod(line7.set_opacity,opacity),
            ApplyMethod(line8.set_opacity,opacity),
            ApplyMethod(line9.set_opacity,opacity),
            ApplyMethod(line10.set_opacity,opacity),
            ApplyMethod(line11.set_opacity,opacity),
            ApplyMethod(line12.set_opacity,opacity),
            ApplyMethod(o1line.set_opacity,opacity),
            ApplyMethod(o2line.set_opacity,opacity),
            ApplyMethod(o3line.set_opacity,opacity),
            ApplyMethod(o4line.set_opacity,opacity),
            ApplyMethod(o5line.set_opacity,opacity),
            ApplyMethod(o6line.set_opacity,opacity),
            ApplyMethod(o7line.set_opacity,opacity),
            ApplyMethod(o8line.set_opacity,opacity),
            ApplyMethod(o9line.set_opacity,opacity),
            ApplyMethod(o91line.set_opacity,opacity),
            ApplyMethod(o92line.set_opacity,opacity),
            ApplyMethod(o93line.set_opacity,opacity),
            ApplyMethod(circle.set_opacity,opacity),
            Write(q_mark)
            )

        self.wait(2)

        zoom=0.7

        self.play(
            self.camera_frame.scale,zoom,
            self.camera_frame.move_to,circle.get_center(),
            FadeOut(bubble),
            ApplyMethod(circle.set_color,WHITE),
            ApplyMethod(circle.set_opacity,1),
            FadeOut(q_mark),
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(line3),
            FadeOut(line4),
            FadeOut(line5),
            FadeOut(line6),
            FadeOut(line7),
            FadeOut(line8),
            FadeOut(line9),
            FadeOut(line10),
            FadeOut(line11),
            FadeOut(line12),
            FadeOut(o1line),
            FadeOut(o2line),
            FadeOut(o3line),
            FadeOut(o4line),
            FadeOut(o5line),
            FadeOut(o6line),
            FadeOut(o7line),
            FadeOut(o8line),
            FadeOut(o9line),
            FadeOut(o91line),
            FadeOut(o92line),
            FadeOut(o93line),
            FadeOut(pyth)
            )

        self.wait()

        unit=Arc(radius=2*zoom,angle=2*PI)
        unit.move_to(circle.get_center())
        self.play(ShowCreation(unit),FadeOut(circle))

        self.wait(4)

        angle=ValueTracker(0)

        red_arc=Arc(radius=2*zoom,angle=angle.get_value(),stroke_color=RED)
        red_arc.move_to(circle.get_center())

        def arc_update(arc):
            new_arc=Arc(radius=2*zoom,angle=angle.get_value(),arc_center=circle.get_center(),stroke_color=RED)
            red_arc.become(new_arc)


        self.add(red_arc)

        corr_term=0.0

        #Move Examples

        angle_arm=Line(circle.get_center(),circle.get_center()+RIGHT*1.4)
        dashed_arm=DashedVMobject(angle_arm)

        angle_arm_copy=Line(circle.get_center(),circle.get_center()+RIGHT*1.4)
        dashed_arm_copy=DashedVMobject(angle_arm)

        self.play(ShowCreation(dashed_arm))
        self.add(dashed_arm_copy)

        move_to=PI/4

        self.play(
            UpdateFromFunc(red_arc,arc_update),
            Rotating(dashed_arm,about_point=circle.get_center(),radians=move_to-angle.get_value()),
            angle.set_value,move_to+corr_term,rate_func=smooth,run_time=1
            )

        self.wait()

        move_to=2*PI/3

        self.play(
            UpdateFromFunc(red_arc,arc_update),
            Rotating(dashed_arm,about_point=circle.get_center(),radians=move_to-angle.get_value()),
            angle.set_value,move_to+corr_term,rate_func=smooth,run_time=1
            )

        self.wait()

        move_to=5*PI/4

        self.play(
            UpdateFromFunc(red_arc,arc_update),
            Rotating(dashed_arm,about_point=circle.get_center(),radians=move_to-angle.get_value()),
            angle.set_value,move_to+corr_term,rate_func=smooth,run_time=1
            )

        self.wait()

        move_to=7*PI/4

        self.play(
            UpdateFromFunc(red_arc,arc_update),
            Rotating(dashed_arm,about_point=circle.get_center(),radians=move_to-angle.get_value()),
            angle.set_value,move_to+corr_term,rate_func=smooth,run_time=1
            )

        self.wait()

        move_to=0

        self.play(
            UpdateFromFunc(red_arc,arc_update),
            Rotating(dashed_arm,about_point=circle.get_center(),radians=move_to-angle.get_value()),
            angle.set_value,move_to-corr_term,rate_func=smooth,run_time=1
            )

        self.wait()

        self.play(
            FadeOut(dashed_arm),
            FadeOut(dashed_arm_copy),
            FadeOut(red_arc)
            )

        self.wait(4)

#python -m manim MITintegral\UnitCircle\unitcirclescenes.py Applications -pl
class Applications(GraphScene,MovingCameraScene):
    CONFIG = {
    "x_min" : -12,
    "x_max" : 12,
    "y_min" : -8,
    "y_max" : 8,
    "x_tick_frequency": 2,
    "y_tick_frequency": 2,
    "y_axis_height":8,
    "x_axis_width":12,
    "graph_origin" : ORIGIN,
    "function_color" : RED ,
    "axes_color" : GREEN,
    "num_rects":300,
    "area_opacity":0.6,
    "default_riemann_start_color":BLUE,
    "default_riemann_end_color":GREEN,
    "x_labeled_nums" :range(-12,12,4),
    "y_labeled_nums" :range(-8,8,4),
    "num_graph_anchor_points": 200,

    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):

        self.setup_axes(animate=False)
        self.x_axis.set_opacity(0)
        self.y_axis.set_opacity(0)

        rad=10

        arc_swath=self.get_graph(self.arc,x_min=0,x_max=10-0.0001)

        arc_area=self.get_area(arc_swath,0,10-0.0001)

        b_line_u=Line(ORIGIN,self.coords_to_point(rad,0))
        b_line=DashedVMobject(b_line_u)

        m_line_u=Line(ORIGIN,self.coords_to_point(rad,0))
        m_line=DashedVMobject(m_line_u)

        angle=ValueTracker(0)

        arc=Arc(radius=5,angle=angle.get_value(),stroke_color=YELLOW)

        t_arc=Arc(radius=1,angle=angle.get_value(),stroke_color=GREY)


        #############
        #Shift amount
        #############
        sh=DOWN+LEFT*2
        #############

        def arc_up(arc):
            n_arc=Arc(radius=5,angle=angle.get_value(),arc_center=sh,stroke_color=YELLOW)
            arc.become(n_arc)

        def t_up(arc):
            n_t_arc=Arc(radius=1,angle=angle.get_value(),arc_center=sh,stroke_color=GREY)
            t_arc.become(n_t_arc)

        theta=TextMobject("$$\\theta$$")
        theta.shift(1.2*RIGHT+0.5*UP)

        r=TextMobject("$$r$$")
        r.next_to(b_line,DOWN,0.2)

        ###
        #second shift
        ssh=RIGHT*2+DOWN
        ###

        whole=VGroup(
            m_line,
            b_line,
            arc,
            t_arc,
            theta,
            r
            )

        whole.shift(sh)

        arc_area.shift(sh+ssh)

        self.play(ShowCreation(b_line))
        self.add(m_line)

        self.play(
            UpdateFromFunc(arc,arc_up),
            UpdateFromFunc(t_arc,t_up),
            Rotating(m_line,about_point=ORIGIN+sh,radians=PI/4),
            angle.set_value,PI/4,run_time=1,rate_func=smooth
            )

        self.play(Write(theta))
        self.wait()
        self.play(Write(r))

        self.wait(2)

        radians=TextMobject("radians")
        degrees=TextMobject("degrees")

        degrees.move_to(LEFT*5.3+UP*2.8)
        radians.next_to(degrees,RIGHT,1.5)
        radians.shift(UP*0.08)

        self.play(
            Write(degrees),
            ApplyMethod(whole.shift,ssh)
            )

        self.wait()

        l1=TextMobject("$$L=$$",stroke_color=YELLOW)
        l1.set_color(YELLOW)
        l1.next_to(degrees,DOWN)
        l1.shift(LEFT*0.5+DOWN*0.4)
        l2=TextMobject("$$L=$$",stroke_color=YELLOW)
        l2.set_color(YELLOW)
        l2.move_to(l1.get_center())
        l2.align_to(radians,LEFT)

        l_deg=TextMobject("$$\\frac{\\theta \pi r}{180}$$")
        l_rad=TextMobject("$$\\theta r$$")

        l_deg.next_to(l1,RIGHT,0.15)
        l_rad.next_to(l2,RIGHT,0.15)

        self.play(
            Write(l1),
            Write(l_deg)
            )

        self.wait(2)

        self.play(Write(radians))
        self.wait()
        self.play(Write(l2),Write(l_rad))

        self.wait(2)


        self.play(ShowCreation(arc_area))

        self.wait()

        a1=TextMobject("$$A=$$")
        a2=TextMobject("$$A=$$")
        a1.set_color(GREEN)
        a2.set_color(GREEN)
        a1.next_to(l1,DOWN,1)
        a2.next_to(l2,DOWN,1)

        a_deg=TextMobject("$$\\frac{\\theta\pi r^{2}}{360}$$")
        a_rad=TextMobject("$$\\frac{1}{2}\\theta r^{2}$$")

        a_deg.next_to(a1,RIGHT,0.15)
        a_rad.next_to(a2,RIGHT,0.15)

        self.play(Write(a1))
        self.wait()
        self.play(Write(a_deg))
        self.wait(2)
        self.play(Write(a2))
        self.wait()
        self.play(Write(a_rad))

        self.wait(4)

        self.play(
            self.camera_frame.scale,0.1
            )

    def arc(self,x):
        if x>=10*(np.sqrt(2)/2):
            return np.sqrt(100-x**2)
        if x<10*(np.sqrt(2)/2):
            return x

#python -m manim MITintegral\UnitCircle\unitcirclescenes.py NewIntro -pl
class NewIntro(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):

        angle=ValueTracker(0)

        arc=Arc(radius=3,angle=angle.get_value(),stroke_width=9)

        arc.set_color(color=[YELLOW,BLUE])

        def arc_up(arc):
            new=Arc(radius=3,angle=angle.get_value(),stroke_width=9)
            new.set_color(color=[YELLOW,BLUE])
            arc.become(new)

        #dot=Dot()
        #dot.scale(1.5)
        #dot.set_color(GREEN)
        #dot.move_to(RIGHT*3)

        self.add(arc)

        self.play(
            UpdateFromFunc(arc,arc_up),
            #Rotating(dot,about_point=ORIGIN,radians=10*PI),
            angle.set_value,10*PI+0.2,rate_func=linear,run_time=10
            )

        #self.play(FadeOut(dot))


        self.play(
            arc.scale,0.4,
            arc.shift,LEFT*4.3
            )

        self.wait()

        noth=TextMobject("")


        sup=TextMobject("Super",fill_color=[YELLOW,BLUE],stroke_color=BLUE,stroke_width=2,fill_opacity=0.8)
        scr=TextMobject("$$Script$$",fill_color=[YELLOW,BLUE],stroke_color=BLUE,stroke_width=2,fill_opacity=0.8)

        scr.next_to(sup,RIGHT,0.1)

        sup_scr=VGroup(sup,scr)

        sup_scr.scale(3)

        sup_scr.next_to(arc,RIGHT,0.2)
        sup_scr.shift(DOWN*0.1)

        #sup_scr.set_color(color=[YELLOW,BLUE])

        self.play(Write(sup_scr))

        self.wait(2)

        logo=VGroup(arc,sup_scr)

        self.play(
            Rotating(arc,about_point=arc.get_center(),radians=8*PI),
            self.camera_frame.scale,0.05,
            self.camera_frame.move_to,arc.get_center(),rate_func=smooth,run_time=1
            )

        self.wait(2)

#python -m manim MITintegral\UnitCircle\unitcirclescenes.py Apps2 -pl
class Apps2(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):

        angle=ValueTracker(0)

        arc=Arc(radius=3,angle=angle.get_value())

        arc.set_color(color=[YELLOW,BLUE])

        def arc_up(arc):
            new=Arc(radius=3,angle=angle.get_value())
            new.set_color(color=[YELLOW,BLUE])
            arc.become(new)

        dot=Dot()
        dot.scale(1.5)
        dot.set_color(GREEN)
        dot.move_to(3*RIGHT*np.cos(-PI/24)+3*UP*np.sin(-PI/24))

        time=5

        self.add(arc)

        self.play(ShowCreation(dot))

        self.play(
            UpdateFromFunc(arc,arc_up),
            Rotating(dot,about_point=ORIGIN,radians=3*PI),
            angle.set_value,3*PI,rate_func=linear,run_time=3
            )

        self.play(
            Rotating(dot,about_point=ORIGIN,radians=time*PI),
            rate_func=linear,run_time=time
            )

        self.play(
            Rotating(dot,about_point=ORIGIN,radians=1*PI),
            self.camera_frame.scale,1.5,
            self.camera_frame.move_to,LEFT*4,
            rate_func=linear,run_time=1
            )

        self.play(
            Rotating(dot,about_point=ORIGIN,radians=3*PI),
            rate_func=linear,run_time=3
            )

        l=TextMobject("$$L$$")
        l.set_color(YELLOW)
        rad=TextMobject("$$=r\\theta$$")
        rad.next_to(l,RIGHT,0.1)

        arc_form=VGroup(l,rad)
        arc_form.scale(2.3)

        arc_form.shift(LEFT*10+UP*3)

        self.play(
            Rotating(dot,about_point=ORIGIN,radians=1*PI),
            Write(arc_form),
            rate_func=linear,run_time=1
            )

        self.play(
            Rotating(dot,about_point=ORIGIN,radians=3*PI),
            rate_func=linear,run_time=3
            )

        v=TextMobject("$$v$$")
        v.set_color(BLUE)
        v.next_to(l,DOWN,2.5)
        v.shift(RIGHT*0.75)
        dd=TextMobject("$$=\\frac{\mathrm{d}L }{\mathrm{d} t}$$")
        dd.next_to(v,RIGHT,0.2)
        v1=VGroup(v,dd)
        v1.scale(2.3)

        self.play(
            Rotating(dot,about_point=ORIGIN,radians=1*PI),
            Write(v1),
            rate_func=linear,run_time=1
            )

        self.play(
            Rotating(dot,about_point=ORIGIN,radians=3*PI),
            rate_func=linear,run_time=3
            )

        dd2=TextMobject("$$=r\\frac{\mathrm{d}\\theta }{\mathrm{d} t}$$")
        dd2.scale(2.3)
        dd2.next_to(v,RIGHT,0.3)

        self.play(
            Rotating(dot,about_point=ORIGIN,radians=.8*PI),
            Transform(dd,dd2),
            rate_func=linear,run_time=.8
            )

        self.play(
            Rotating(dot,about_point=ORIGIN,radians=3*PI),
            rate_func=linear,run_time=3
            )

        dd3=TextMobject("$$=r\omega$$")
        dd3.scale(2.3)
        dd3.next_to(v,RIGHT,0.3)

        self.play(
            Rotating(dot,about_point=ORIGIN,radians=.8*PI),
            Transform(dd,dd3),
            rate_func=linear,run_time=.8
            )

        self.play(
            Rotating(dot,about_point=ORIGIN,radians=10*PI),
            rate_func=linear,run_time=10
            )

        self.wait(2)

#python -m manim MITintegral\UnitCircle\unitcirclescenes.py End -pl
class End(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        circle=Arc(radius=2,angle=2*PI)
        circle.set_color(color=[RED,BLUE])
        self.play(ShowCreation(circle))

        base_u=Line(ORIGIN,RIGHT*2)
        base=DashedVMobject(base_u)

        mase_u=Line(ORIGIN,RIGHT*2)
        mase=DashedVMobject(mase_u)

        s=TextMobject("$$\\sin(\\theta)$$")
        s.set_color(BLUE)
        c=TextMobject("$$\\cos(\\theta)$$")
        c.set_color(RED)
        s.move_to(LEFT*4+UP*2.2)
        c.next_to(s,DOWN,0.3)

        self.play(
            Write(s),
            Write(c)
            )

        self.play(ShowCreation(base))
        self.add(mase)

        self.play(
            Rotating(mase,about_point=ORIGIN,radians=PI/2),
            rate_func=smooth,run_time=1
            )

        self.wait()

        self.play(
            Rotating(mase,about_point=ORIGIN,radians=7*PI/6),
            rate_func=smooth,run_time=1
            )

        self.wait()

        self.play(
            Rotating(mase,about_point=ORIGIN,radians=-3*PI/5),
            rate_func=smooth,run_time=1
            )

        self.wait()

        self.play(
            Rotating(mase,about_point=ORIGIN,radians=-4*PI/6),
            rate_func=smooth,run_time=1
            )

        self.wait(4)

#python -m manim MITintegral\UnitCircle\unitcirclescenes.py IntroAdd -pl
class IntroAdd(GraphScene,MovingCameraScene):
    CONFIG = {
    "x_min" : -12,
    "x_max" : 12,
    "y_min" : -9,
    "y_max" : 9,
    "x_tick_frequency": 2,
    "y_tick_frequency": 2,
    "y_axis_height":9,
    "x_axis_width":12,
    "graph_origin" : ORIGIN,
    "function_color" : RED ,
    "axes_color" : GREEN,
    #"x_labeled_nums" :range(-8,8,2),
    #"y_labeled_nums" :range(-6,6,2),
    "num_graph_anchor_points": 200,

    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):

        self.setup_axes(animate=True)

        exp_graph=self.get_graph(self.exp,x_min=-12,x_max=12)
        exp_graph.set_color(BLUE)

        add=ValueTracker(-10)

        start=8

        tan_line=Line(self.coords_to_point(start,np.exp((start)/6)),self.coords_to_point(start+add.get_value(),np.exp((start+add.get_value())/6)),stroke_width=3)

        tan_line.set_color(RED)

        tan_line.scale(30/add.get_value())

        r_dot=Dot()
        r_dot.set_color(YELLOW)
        r_dot.move_to(self.coords_to_point(start,np.exp(start/6)))

        l_dot=Dot()
        l_dot.set_color(YELLOW)
        l_dot.move_to(self.coords_to_point(start+add.get_value(),np.exp((start+add.get_value())/6)))



        def line_up(line):
            new_line=Line(self.coords_to_point(start,np.exp((start)/6)),self.coords_to_point(start+add.get_value(),np.exp((start+add.get_value())/6)),stroke_width=3)
            new_line.set_color(RED)
            new_line.scale(30/add.get_value())
            tan_line.become(new_line)

        def dot_up(dot):
            new_dot=Dot()
            new_dot.set_color(YELLOW)
            new_dot.move_to(self.coords_to_point(start+add.get_value(),np.exp((start+add.get_value())/6)))
            l_dot.become(new_dot)

        self.play(
            ShowCreation(exp_graph)
            )

        self.wait()

        self.play(
            ShowCreation(tan_line),
            ShowCreation(r_dot),
            ShowCreation(l_dot)
            )
        self.wait()

        self.remove(l_dot)

        self.play(
            UpdateFromFunc(tan_line,line_up),
            UpdateFromFunc(l_dot,dot_up),
            add.set_value,0.1,rate_func=linear,run_time=3
            )

        self.wait()

        calculus=TextMobject("calculus",fill_color=WHITE,fill_opacity=0.5,stroke_color=BLUE,stroke_width=2)
        calculus.move_to(UP*6)
        calculus.scale(3)

        self.play(
            self.camera_frame.scale,2,
            self.camera_frame.move_to,LEFT*7+UP*1.5,
            Write(calculus)
            )


        self.wait()

        arrow=TextMobject("$$\\rightarrow$$",stroke_width=3)
        arrow.move_to(LEFT*7.8)
        arrow.set_color(color=[YELLOW,GREEN])
        arrow.scale(4)

        self.play(Write(arrow))

        self.wait()

        circle=Arc(radius=4,angle=2*PI)
        circle.set_color(color=[YELLOW,BLUE])
        circle.move_to(LEFT*14)
        arm=Arrow(circle.get_center(),circle.get_center()+4.2*RIGHT)
        arm.set_color(BLUE)

        unit=TextMobject("unit circle",fill_color=WHITE,fill_opacity=0.5,stroke_color=BLUE,stroke_width=2)
        unit.move_to(circle.get_center()+UP*6)
        unit.scale(3)

        self.play(
        	ShowCreation(circle),
        	Write(unit)
        	)

        self.play(ShowCreation(arm))

        self.play(
            Rotating(arm,about_point=circle.get_center(),radians=7*PI),
            run_time=10,rate_func=linear
            )

    def exp(self,x):
        return np.exp(x/6)

#python -m manim MITintegral\UnitCircle\unitcirclescenes.py Thumbnailv1 -ps
class Thumbnailv1(Scene):

    def construct(self):


        pyth=ImageMobject("divinciman")
        pyth.scale(5.5)
        #pyth.move_to(2*DOWN+RIGHT*5.6)

        #pyth.rotate(angle=-PI/10)

        what_are=TextMobject("\\textsl{what are}",fill_color=[YELLOW,RED],fill_opacity=.9,stroke_color=WHITE,stroke_width=6)
        radians=TextMobject("\\textbf{RADIANS}",fill_color=[YELLOW,RED],fill_opacity=.9,stroke_color=WHITE,stroke_width=3)

        what_are.move_to(UP*2)
        what_are.scale(6.5)
        #radians.move_to(DOWN)
        radians.scale(5.2)
        radians.move_to(DOWN)

        #q=TextMobject("?",stroke_width=3,stroke_color=BLUE,stroke_opacity=0.8,fill_color=BLUE,fill_opacity=0.3)

        #q.scale(18)

        #self.add(q)

        self.add(what_are)
        self.add(radians)

        self.add(pyth)

        self.bring_to_back(pyth)

#python -m manim MITintegral\UnitCircle\unitcirclescenes.py Thumbnailv2 -ps
class Thumbnailv2(Scene):

    def construct(self):

        circle=Arc(radius=5,angle=2*PI,stroke_opacity=0.6,stroke_width=10)

        circle2=Arc(radius=7,angle=2*PI,stroke_opacity=0.3,stroke_width=10)

        #theta=Arc(radius=2,angle=6*PI/3,stroke_width=8,stroke_opacity=0.6,stroke_color=GREY)

        circle.set_color(color=[BLUE,YELLOW])
        circle2.set_color(color=[BLUE,YELLOW])

        thick=12

        arm1=DashedLine(ORIGIN,RIGHT*5,stroke_opacity=0.5,stroke_width=thick)
        arm1.rotate(about_point=ORIGIN,angle=0)

        arm2=DashedLine(ORIGIN,RIGHT*5,stroke_opacity=0.5,stroke_width=thick)
        arm2.rotate(about_point=ORIGIN,angle=PI/3)

        arm3=DashedLine(ORIGIN,RIGHT*5,stroke_opacity=0.5,stroke_width=thick)
        arm3.rotate(about_point=ORIGIN,angle=2*PI/3)

        arm4=DashedLine(ORIGIN,RIGHT*5,stroke_opacity=0.5,stroke_width=thick)
        arm4.rotate(about_point=ORIGIN,angle=PI)

        arm5=DashedLine(ORIGIN,RIGHT*5,stroke_opacity=0.5,stroke_width=thick)
        arm5.rotate(about_point=ORIGIN,angle=4*PI/3)

        arm6=DashedLine(ORIGIN,RIGHT*5,stroke_opacity=0.5,stroke_width=thick)
        arm6.rotate(about_point=ORIGIN,angle=5*PI/3)

        what_are=TextMobject("\\textsl{what are}",fill_color=[BLUE,YELLOW],fill_opacity=.9,stroke_color=WHITE,stroke_width=6)
        radians=TextMobject("\\textbf{RADIANS}",fill_color=[YELLOW,RED],fill_opacity=.9,stroke_color=WHITE,stroke_width=3)

        what_are.move_to(UP*2)
        what_are.scale(5.5)
        #radians.move_to(DOWN)
        radians.scale(5.2)
        radians.move_to(DOWN*0.8)

        #q=TextMobject("?",stroke_width=3,stroke_color=BLUE,stroke_opacity=0.8,fill_color=BLUE,fill_opacity=0.3)

        #q.scale(18)

        #self.add(q)

        self.add(
        	arm1,
        	arm2,
        	arm3,
        	arm4,
        	arm5,
        	arm6
        	)

        self.add(circle)
        self.add(circle2)

        #self.add(theta)

        self.add(what_are)
        self.add(radians)
