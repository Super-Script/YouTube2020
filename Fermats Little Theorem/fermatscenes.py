#!/usr/bin/env python

from manimlib.imports import *

#python -m manim MITintegral\Fermat\fermatscenes.py Shifts -pl
class Shifts(Scene):
	def construct(self):
		r_dot=Dot()
		b_dot=Dot()
		b2_dot=Dot()

		scale=4

		r_dot.set_color(RED)
		b_dot.set_color(BLUE)
		b2_dot.set_color(BLUE)

		r_dot.scale(scale)
		b_dot.scale(scale)
		b2_dot.scale(scale)

		r_dot.next_to(b_dot,LEFT,1)
		b2_dot.next_to(b_dot,RIGHT,1)

		dots=VGroup(r_dot,b_dot,b2_dot)

		self.play(
			ShowCreation(r_dot),
			ShowCreation(b_dot),
			ShowCreation(b2_dot)
			)

		self.wait(3)

		def shifter(x,y,z):
			self.play(
				ApplyMethod(x.move_to,y.get_center()),
				ApplyMethod(y.move_to,z.get_center()),
				Rotating(z,radians=PI,about_point=y.get_center()),
				rate_func=smooth,run_time=1.6
			)

		shifter(r_dot,b_dot,b2_dot)
		
		self.wait(2)

		shifter(b2_dot,r_dot,b_dot)

		self.wait(2)

		shifter(b_dot,b2_dot,r_dot)

		self.wait(2)

		self.play(ApplyMethod(dots.shift,UP*1.5))

		#####
		#New set of dots

		_r_dot=Dot()
		_b_dot=Dot()
		_r2_dot=Dot()

		scale=4

		_r_dot.set_color(RED)
		_b_dot.set_color(BLUE)
		_r2_dot.set_color(RED)

		_r_dot.scale(scale)
		_b_dot.scale(scale)
		_r2_dot.scale(scale)

		_r_dot.next_to(_b_dot,LEFT,1)
		_r2_dot.next_to(_b_dot,RIGHT,1)

		_dots=VGroup(_r_dot,_b_dot,_r2_dot)

		_dots.shift(DOWN)

		self.play(
			ShowCreation(_r_dot),
			ShowCreation(_b_dot),
			ShowCreation(_r2_dot)
			)

		self.wait(3)

		shifter(_r_dot,_b_dot,_r2_dot)
		
		self.wait(2)

		shifter(_r2_dot,_r_dot,_b_dot)

		self.wait(2)

		shifter(_b_dot,_r2_dot,_r_dot)

		self.wait(2)

		self.play(ApplyMethod(dots.shift,DOWN*0.5))

		self.wait()

		reds1=Dot(color=RED)
		reds2=Dot(color=RED)
		reds3=Dot(color=RED)

		blues1=Dot(color=BLUE)
		blues2=Dot(color=BLUE)
		blues3=Dot(color=BLUE)

		reds=VGroup(reds1,reds2,reds3)
		reds.scale(4)
		reds1.next_to(reds2,LEFT,1)
		reds3.next_to(reds2,RIGHT,1)

		reds.move_to(dots.get_center()+UP*2)

		blues=VGroup(blues1,blues2,blues3)
		blues.scale(4)
		blues1.next_to(blues2,LEFT,1)
		blues3.next_to(blues2,RIGHT,1)

		blues.move_to(_dots.get_center()+DOWN*2)

		self.play(ShowCreation(reds))
		self.wait()
		self.play(ShowCreation(blues))

		self.wait(2)

		self.play(FadeOut(reds),FadeOut(blues))

		self.wait(2)

		self.play(FadeOut(_dots))

		self.wait()

		sh11=Dot(color=BLUE)
		sh12=Dot(color=RED)
		sh13=Dot(color=BLUE)

		sh11.scale(4)
		sh12.scale(4)
		sh13.scale(4)

		sh11.next_to(sh12,LEFT,1)
		sh13.next_to(sh12,RIGHT,1)

		sh1_g=VGroup(sh11,sh12,sh13)

		sh1_g.move_to(ORIGIN+DOWN)

		arr1=TextMobject("$$\\rightarrow$$")
		arr1.rotate(about_point=arr1.get_center(),angle=-PI/2)
		arr1.scale(1.9)
		c_point=VGroup(dots,sh1_g)
		arr1.move_to(c_point.get_center())

		self.wait()

		self.play(ShowCreation(arr1))

		self.play(ShowCreation(sh1_g))

		self.wait()

		sh21=Dot(color=BLUE)
		sh22=Dot(color=BLUE)
		sh23=Dot(color=RED)

		sh21.scale(4)
		sh22.scale(4)
		sh23.scale(4)

		sh21.next_to(sh22,LEFT,1)
		sh23.next_to(sh22,RIGHT,1)

		sh2_g=VGroup(sh21,sh22,sh23)

		sh2_g.move_to(ORIGIN+DOWN*3)

		self.wait()

		arr2=TextMobject("$$\\rightarrow$$")
		arr2.rotate(about_point=arr2.get_center(),angle=-PI/2)
		arr2.scale(1.9)
		c_point=VGroup(sh1_g,sh2_g)
		arr2.move_to(c_point.get_center())

		self.play(ShowCreation(arr2))

		self.play(ShowCreation(sh2_g))

		self.wait(4)

		self.play(
			FadeOut(arr1),
			FadeOut(arr2),
			FadeOut(dots),
			FadeOut(sh1_g),
			FadeOut(sh2_g)
			)
		self.wait()


#python -m manim MITintegral\Fermat\fermatscenes.py ShiftFour -pl
class ShiftFour(MovingCameraScene):
	def setup(self):
		MovingCameraScene.setup(self)
	def construct(self):
		self.camera_frame.scale(1.3)
		a=Dot(color=RED)
		b=Dot(color=RED)
		c=Dot(color=BLUE)
		d=Dot(color=BLUE)

		scale=3

		a.scale(scale)
		b.scale(scale)
		c.scale(scale)
		d.scale(scale)

		a.next_to(b,LEFT,1)
		c.next_to(b,RIGHT,1)
		d.next_to(c,RIGHT,1)

		s_dots=VGroup(a,b,c,d)

		s_dots.move_to(ORIGIN)

		s_dots.shift(UP*3)

		self.play(ShowCreation(s_dots))

		self.wait()

		arrows=[]

		dots=[]

		def shift_down(a,b,c,d):
			scale=3
			a_new=Dot(color=d.get_color())
			b_new=Dot(color=a.get_color())
			c_new=Dot(color=b.get_color())
			d_new=Dot(color=c.get_color())

			a_new.scale(3)
			b_new.scale(3)
			c_new.scale(3)
			d_new.scale(3)

			a_new.move_to(a.get_center()+DOWN*1.8)
			b_new.move_to(b.get_center()+DOWN*1.8)
			c_new.move_to(c.get_center()+DOWN*1.8)
			d_new.move_to(d.get_center()+DOWN*1.8)

			arr=TextMobject("$$\\rightarrow$$")
			arr.scale(1.9)
			arr.rotate(about_point=arr.get_center(),angle=-PI/2)
			f_g=VGroup(b,c,b_new,c_new)
			arr.move_to(f_g.get_center())

			arrows.append(arr)

			dots.append(a_new)
			dots.append(b_new)
			dots.append(c_new)
			dots.append(d_new)

			self.play(ShowCreation(arr))
			self.play(
				ShowCreation(a_new),
				ShowCreation(b_new),
				ShowCreation(c_new),
				ShowCreation(d_new)
				)


		shift_down(a,b,c,d)

		self.wait()

		shift_down(dots[0],dots[1],dots[2],dots[3])

		self.wait()

		shift_down(dots[4],dots[5],dots[6],dots[7])

		self.wait()

		shift_down(dots[8],dots[9],dots[10],dots[11])

		self.wait(2)

		self.play(
			FadeOut(dots[12]),
			FadeOut(dots[13]),
			FadeOut(dots[14]),
			FadeOut(dots[15]),
			FadeOut(arrows[3])
			)

		self.wait(3)

		self.play(
			FadeOut(a),
			FadeOut(b),
			FadeOut(c),
			FadeOut(d),
			FadeOut(dots[0]),
			FadeOut(dots[1]),
			FadeOut(dots[2]),
			FadeOut(dots[3]),
			FadeOut(dots[4]),
			FadeOut(dots[5]),
			FadeOut(dots[6]),
			FadeOut(dots[7]),
			FadeOut(dots[8]),
			FadeOut(dots[9]),
			FadeOut(dots[10]),
			FadeOut(dots[11]),
			FadeOut(arrows[0]),
			FadeOut(arrows[1]),
			FadeOut(arrows[2])
			)

		self.wait(2)


#python -m manim MITintegral\Fermat\fermatscenes.py ShiftFour2 -pl
class ShiftFour2(MovingCameraScene):
	def setup(self):
		MovingCameraScene.setup(self)
	def construct(self):
		self.camera_frame.scale(1.3)
		a=Dot(color=RED)
		b=Dot(color=BLUE)
		c=Dot(color=RED)
		d=Dot(color=BLUE)

		scale=3

		a.scale(scale)
		b.scale(scale)
		c.scale(scale)
		d.scale(scale)

		a.next_to(b,LEFT,1)
		c.next_to(b,RIGHT,1)
		d.next_to(c,RIGHT,1)

		s_dots=VGroup(a,b,c,d)

		s_dots.move_to(ORIGIN)

		s_dots.shift(UP*3)

		self.play(ShowCreation(s_dots))

		self.wait()

		arrows=[]

		dots=[]

		def shift_down(a,b,c,d):
			scale=3
			a_new=Dot(color=d.get_color())
			b_new=Dot(color=a.get_color())
			c_new=Dot(color=b.get_color())
			d_new=Dot(color=c.get_color())

			a_new.scale(3)
			b_new.scale(3)
			c_new.scale(3)
			d_new.scale(3)

			a_new.move_to(a.get_center()+DOWN*1.8)
			b_new.move_to(b.get_center()+DOWN*1.8)
			c_new.move_to(c.get_center()+DOWN*1.8)
			d_new.move_to(d.get_center()+DOWN*1.8)

			arr=TextMobject("$$\\rightarrow$$")
			arr.scale(1.9)
			arr.rotate(about_point=arr.get_center(),angle=-PI/2)
			f_g=VGroup(b,c,b_new,c_new)
			arr.move_to(f_g.get_center())

			arrows.append(arr)

			dots.append(a_new)
			dots.append(b_new)
			dots.append(c_new)
			dots.append(d_new)

			self.play(ShowCreation(arr))
			self.play(
				ShowCreation(a_new),
				ShowCreation(b_new),
				ShowCreation(c_new),
				ShowCreation(d_new)
				)


		shift_down(a,b,c,d)

		self.wait()

		shift_down(dots[0],dots[1],dots[2],dots[3])

		self.wait()

		self.wait(2)

		self.play(
			FadeOut(dots[4]),
			FadeOut(dots[5]),
			FadeOut(dots[6]),
			FadeOut(dots[7]),
			FadeOut(arrows[1])
			)

		self.wait(2)

		self.play(
			FadeOut(dots[0]),
			FadeOut(dots[1]),
			FadeOut(dots[2]),
			FadeOut(dots[3]),
			FadeOut(arrows[0])
			)
		self.play(ApplyMethod(s_dots.move_to,ORIGIN))
		self.play(ApplyMethod(self.camera_frame.scale,0.5))

		self.wait(2)

		f_g=VGroup(a,b)

		buff=0.2
		box1=Rectangle(height=a.get_height()+buff,width=f_g.get_width()+buff,stroke_color=BLUE)
		box1.move_to(f_g.get_center())

		f_g2=VGroup(c,d)

		box2=Rectangle(height=a.get_height()+buff,width=f_g.get_width()+buff,stroke_color=BLUE)
		box2.move_to(f_g2.get_center())

		self.play(ShowCreation(box1))
		self.wait()
		self.play(ShowCreation(box2))

		self.wait(2)

		g1=VGroup(a,b,box1)
		g2=VGroup(c,d,box2)

		g=VGroup(g1,g2)

		angle=ValueTracker(0)

		dist=np.abs(g2.get_center())

		self.play(
			ApplyMethod(g1.move_to,g2.get_center()),
			ApplyMethod(g2.move_to,g1.get_center()),
			)

		self.wait(2)



#python -m manim MITintegral\Fermat\fermatscenes.py ShiftNine -pl
class ShiftNine(MovingCameraScene):
	def setup(self):
		MovingCameraScene.setup(self)
	def construct(self):
		self.camera_frame.scale(1.3)
		a=Dot(color=RED)
		b=Dot(color=BLUE)
		c=Dot(color=GREEN)
		d=Dot(color=RED)
		e=Dot(color=BLUE)
		f=Dot(color=GREEN)
		g=Dot(color=RED)
		h=Dot(color=BLUE)
		i=Dot(color=GREEN)

		scale=3

		a.scale(scale)
		b.scale(scale)
		c.scale(scale)
		d.scale(scale)
		e.scale(scale)
		f.scale(scale)
		g.scale(scale)
		h.scale(scale)
		i.scale(scale)

		a.next_to(b,LEFT,1)
		c.next_to(b,RIGHT,1)
		d.next_to(c,RIGHT,1)
		e.next_to(d,RIGHT,1)
		f.next_to(e,RIGHT,1)
		g.next_to(f,RIGHT,1)
		h.next_to(g,RIGHT,1)
		i.next_to(h,RIGHT,1)

		s_dots=VGroup(a,b,c,d,e,f,g,h,i)

		s_dots.move_to(ORIGIN)

		s_dots.shift(UP*3)

		self.play(ShowCreation(s_dots))

		self.wait(2)

		buff=0.2

		f_g=VGroup(a,b,c)

		box1=Rectangle(width=f_g.get_width()+buff,height=f_g.get_height()+buff,color=BLUE)
		box1.move_to(f_g.get_center())

		box2=Rectangle(width=f_g.get_width()+buff,height=f_g.get_height()+buff,color=BLUE)
		box2.move_to(ORIGIN+UP*3)

		box3=Rectangle(width=f_g.get_width()+buff,height=f_g.get_height()+buff,color=BLUE)
		box3.move_to(UP*3+RIGHT*(ORIGIN-f_g.get_center()))

		self.play(ShowCreation(box1))

		self.wait()

		self.play(ShowCreation(box2))
		self.play(ShowCreation(box3))

		self.wait(2)

		self.play(
			FadeOut(box1),
			FadeOut(box2),
			FadeOut(box3)
			)

		arrows=[]

		dots=[]

		def shift_down(a,b,c,d,e,f,g,h,i):
			scale=3
			a_new=Dot(color=i.get_color())
			b_new=Dot(color=a.get_color())
			c_new=Dot(color=b.get_color())
			d_new=Dot(color=c.get_color())
			e_new=Dot(color=d.get_color())
			f_new=Dot(color=e.get_color())
			g_new=Dot(color=f.get_color())
			h_new=Dot(color=g.get_color())
			i_new=Dot(color=h.get_color())

			a_new.scale(3)
			b_new.scale(3)
			c_new.scale(3)
			d_new.scale(3)
			e_new.scale(3)
			f_new.scale(3)
			g_new.scale(3)
			h_new.scale(3)
			i_new.scale(3)

			a_new.move_to(a.get_center()+DOWN*1.8)
			b_new.move_to(b.get_center()+DOWN*1.8)
			c_new.move_to(c.get_center()+DOWN*1.8)
			d_new.move_to(d.get_center()+DOWN*1.8)
			e_new.move_to(e.get_center()+DOWN*1.8)
			f_new.move_to(f.get_center()+DOWN*1.8)
			g_new.move_to(g.get_center()+DOWN*1.8)
			h_new.move_to(h.get_center()+DOWN*1.8)
			i_new.move_to(i.get_center()+DOWN*1.8)

			arr=TextMobject("$$\\rightarrow$$")
			arr.scale(1.9)
			arr.rotate(about_point=arr.get_center(),angle=-PI/2)
			f_g=VGroup(e,e_new)
			arr.move_to(f_g.get_center())

			arrows.append(arr)

			dots.append(a_new)
			dots.append(b_new)
			dots.append(c_new)
			dots.append(d_new)
			dots.append(e_new)
			dots.append(f_new)
			dots.append(g_new)
			dots.append(h_new)
			dots.append(i_new)

			self.play(ShowCreation(arr))
			self.play(
				ShowCreation(a_new),
				ShowCreation(b_new),
				ShowCreation(c_new),
				ShowCreation(d_new),
				ShowCreation(e_new),
				ShowCreation(f_new),
				ShowCreation(g_new),
				ShowCreation(h_new),
				ShowCreation(i_new),
				)


		shift_down(a,b,c,d,e,f,g,h,i)

		self.wait()

		shift_down(
			dots[0],
			dots[1],
			dots[2],
			dots[3],
			dots[4],
			dots[5],
			dots[6],
			dots[7],
			dots[8]
			)

		self.wait()

		shift_down(
			dots[9],
			dots[10],
			dots[11],
			dots[12],
			dots[13],
			dots[14],
			dots[15],
			dots[16],
			dots[17]
			)

		self.wait(3)

		self.play(
			FadeOut(dots[18]),
			FadeOut(dots[19]),
			FadeOut(dots[20]),
			FadeOut(dots[21]),
			FadeOut(dots[22]),
			FadeOut(dots[23]),
			FadeOut(dots[24]),
			FadeOut(dots[25]),
			FadeOut(dots[26]),
			FadeOut(arrows[2])
			)

		self.wait(2)

		self.play(ApplyMethod(self.camera_frame.scale,50),run_time=2)

		self.wait()

#python -m manim MITintegral\Fermat\fermatscenes.py ShiftFive -pl
class ShiftFive(MovingCameraScene):
	def setup(self):
		MovingCameraScene.setup(self)
	def construct(self):
		self.camera_frame.scale(1.3)
		a=Dot(color=RED)
		b=Dot(color=BLUE)
		c=Dot(color=BLUE)
		d=Dot(color=RED)
		e=Dot(color=BLUE)

		scale=3

		a.scale(scale)
		b.scale(scale)
		c.scale(scale)
		d.scale(scale)
		e.scale(scale)

		a.next_to(b,LEFT,1)
		c.next_to(b,RIGHT,1)
		d.next_to(c,RIGHT,1)
		e.next_to(d,RIGHT,1)

		s_dots=VGroup(a,b,c,d,e)

		s_dots.move_to(ORIGIN)

		s_dots.shift(UP*3)

		self.play(ShowCreation(s_dots))

		self.wait(2)

		buff=0.2

		f_g=VGroup(a,b,c)

		box1=Rectangle(width=f_g.get_width()+buff,height=f_g.get_height()+buff,color=BLUE)
		box1.move_to(f_g.get_center())

		box2=Rectangle(width=f_g.get_width()+buff,height=f_g.get_height()+buff,color=BLUE)
		box2.move_to(e.get_center())

		self.play(ShowCreation(box1))

		self.wait()

		self.play(ShowCreation(box2))

		self.wait(2)

		self.play(
			FadeOut(box1),
			FadeOut(box2),
			)

		f_g=VGroup(a,b)

		box1=Rectangle(width=f_g.get_width()+buff,height=f_g.get_height()+buff,color=BLUE)
		box1.move_to(f_g.get_center())

		f_g=VGroup(c,d)

		box2=Rectangle(width=f_g.get_width()+buff,height=f_g.get_height()+buff,color=BLUE)
		box2.move_to(f_g.get_center())

		self.play(ShowCreation(box1))
		self.play(ShowCreation(box2))

		self.wait(2)

		self.play(
			FadeOut(box1),
			FadeOut(box2)
			)

		self.wait(2)

		arrows=[]

		dots=[]

		def shift_down(a,b,c,d,e):
			scale=3
			a_new=Dot(color=e.get_color())
			b_new=Dot(color=a.get_color())
			c_new=Dot(color=b.get_color())
			d_new=Dot(color=c.get_color())
			e_new=Dot(color=d.get_color())

			a_new.scale(3)
			b_new.scale(3)
			c_new.scale(3)
			d_new.scale(3)
			e_new.scale(3)

			a_new.move_to(a.get_center()+DOWN*1.8)
			b_new.move_to(b.get_center()+DOWN*1.8)
			c_new.move_to(c.get_center()+DOWN*1.8)
			d_new.move_to(d.get_center()+DOWN*1.8)
			e_new.move_to(e.get_center()+DOWN*1.8)

			arr=TextMobject("$$\\rightarrow$$")
			arr.scale(1.9)
			arr.rotate(about_point=arr.get_center(),angle=-PI/2)
			f_g=VGroup(c,c_new)
			arr.move_to(f_g.get_center())

			arrows.append(arr)

			dots.append(a_new)
			dots.append(b_new)
			dots.append(c_new)
			dots.append(d_new)
			dots.append(e_new)

			self.play(ShowCreation(arr))
			self.play(
				ShowCreation(a_new),
				ShowCreation(b_new),
				ShowCreation(c_new),
				ShowCreation(d_new),
				ShowCreation(e_new),
				)


		shift_down(a,b,c,d,e)

		self.wait()

		shift_down(
			dots[0],
			dots[1],
			dots[2],
			dots[3],
			dots[4]
			)

		self.wait()

		shift_down(
			dots[5],
			dots[6],
			dots[7],
			dots[8],
			dots[9]
			)

		self.wait()

		shift_down(
			dots[10],
			dots[11],
			dots[12],
			dots[13],
			dots[14]
			)

		self.wait(2)

		self.play(ApplyMethod(self.camera_frame.scale,50),
			rate_func=smooth,run_time=2)

		self.wait()

#python -m manim MITintegral\Fermat\fermatscenes.py ProbExp -pl
class ProbExp(Scene):
	def construct(self):
		r1=Dot(color=RED)
		r2=Dot(color=RED)
		r3=Dot(color=RED)
		b1=Dot(color=BLUE)
		b2=Dot(color=BLUE)
		b3=Dot(color=BLUE)

		scale=4
		r1.scale(scale)
		r2.scale(scale)
		r3.scale(scale)
		b1.scale(scale)
		b2.scale(scale)
		b3.scale(scale)

		buff=.8

		r1.move_to(RIGHT*3.8+UP*2)
		r2.next_to(r1,RIGHT,buff)
		r3.next_to(r1,DOWN,buff)
		b1.next_to(r2,DOWN,buff)
		b2.next_to(r3,LEFT,buff)
		b3.next_to(r1,LEFT,buff)

		dots=VGroup(
			r1,
			r2,
			r3,
			b1,
			b2,
			b3
			)

		self.play(ShowCreation(dots))

		self.wait(3)

		box_b=0.2

		box1=Rectangle(width=r1.get_width()+box_b,height=r1.get_height()+box_b)
		box2=Rectangle(width=r1.get_width()+box_b,height=r1.get_height()+box_b)
		box3=Rectangle(width=r1.get_width()+box_b,height=r1.get_height()+box_b)

		box1.move_to(LEFT*3.7+DOWN*0.8)
		box2.next_to(box1,RIGHT,1)
		box3.next_to(box2,RIGHT,1)

		boxes=VGroup(box1,box2,box3)

		self.play(ShowCreation(boxes))

		self.wait(3)

		#markers for dot positions
		oo=Dot()
		ot=Dot()
		oth=Dot()
		to=Dot()
		tt=Dot()
		tth=Dot()

		oo.move_to(r2.get_center())
		ot.move_to(r1.get_center())
		oth.move_to(b3.get_center())
		to.move_to(b1.get_center())
		tt.move_to(r3.get_center())
		tth.move_to(b2.get_center())

		#move exp takes in three dots
		def move_exp(d1,d2,d3):
			c1=d1.get_center()
			c2=d2.get_center()
			c3=d3.get_center()

			self.play(ApplyMethod(d1.move_to,box1.get_center()))
			self.play(ApplyMethod(d2.move_to,box2.get_center()))
			self.play(ApplyMethod(d3.move_to,box3.get_center()))
			self.wait()
			self.play(
				ApplyMethod(d1.move_to,c1),
				ApplyMethod(d2.move_to,c2),
				ApplyMethod(d3.move_to,c3)
				)

		move_exp(r1,b2,b3)

		self.wait()

		move_exp(r3,b1,b3)

		self.wait()

		move_exp(r2,r3,r1)

		self.wait(3)

		self.play(ApplyMethod(boxes.move_to,dots.get_center()+DOWN*2.5))

		self.wait(3)

		self.play(ApplyMethod(box1.set_color,YELLOW))
		self.play(ApplyMethod(box1.set_color,WHITE))

		self.play(ApplyMethod(r1.move_to,box1.get_center()))
		self.wait(0.6)
		self.play(
			ApplyMethod(r1.move_to,ot.get_center()),
			ApplyMethod(b1.move_to,box1.get_center())
			)
		self.wait(0.6)
		self.play(ApplyMethod(b1.move_to,to.get_center()))

		self.wait(3)

		rop1=Dot(color=RED)
		bop1=Dot(color=BLUE)

		rop1.move_to(LEFT*5+UP*2)
		bop1.move_to(LEFT*5+DOWN*2)

		rop1.scale(2)
		bop1.scale(2)

		lines=[]

		self.play(ShowCreation(rop1),ShowCreation(bop1))

		#branch takes in a dot, and the angle and length of the lines 
		#wished to be created
		def branchup(dot,angle,leng):
			buf=0.15
			up_line=Line(
				#from
				dot.get_center()+RIGHT*buf*np.cos(angle)+UP*buf*np.sin(angle),
				#to
				dot.get_center()+RIGHT*buf*np.cos(angle)+UP*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+UP*leng*np.sin(angle)
				)
			red=Dot(color=RED)
			red.scale(2)
			red.move_to(dot.get_center()+RIGHT*buf*np.cos(angle)+UP*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+UP*leng*np.sin(angle)+RIGHT*buf*np.cos(angle)+UP*buf*np.sin(angle))
			lines.append(up_line)
			self.play(ShowCreation(red),ShowCreation(up_line))
			return red

		def branchdown(dot,angle,leng):
			buf=0.15
			down_line=Line(
				#from
				dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle),
				#to
				dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+DOWN*leng*np.sin(angle)
				)
			blue=Dot(color=BLUE)
			blue.scale(2)
			blue.move_to(dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+DOWN*leng*np.sin(angle)+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle))
			lines.append(down_line)
			self.play(ShowCreation(blue),ShowCreation(down_line))
			return blue

		self.wait(2)

		self.play(ApplyMethod(box2.set_color,YELLOW))
		self.play(ApplyMethod(box2.set_color,WHITE))

		self.play(ApplyMethod(r1.move_to,box2.get_center()))
		self.wait(0.6)
		self.play(
			ApplyMethod(r1.move_to,ot.get_center()),
			ApplyMethod(b1.move_to,box2.get_center())
			)
		self.wait(0.6)
		self.play(ApplyMethod(b1.move_to,to.get_center()))

		rop1_u=branchup(rop1,PI/6,1.4)
		rop1_d=branchdown(rop1,PI/6,1.4)

		self.wait(2)

		bop1_u=branchup(bop1,PI/6,1.4)
		bop1_d=branchdown(bop1,PI/6,1.4)

		self.wait(2)

		####
		#Third round

		self.play(ApplyMethod(box3.set_color,YELLOW))
		self.play(ApplyMethod(box3.set_color,WHITE))

		self.play(ApplyMethod(r1.move_to,box3.get_center()))
		self.wait(0.6)
		self.play(
			ApplyMethod(r1.move_to,ot.get_center()),
			ApplyMethod(b1.move_to,box3.get_center())
			)
		self.wait(0.6)
		self.play(ApplyMethod(b1.move_to,to.get_center()))

		self.wait(2)

		an=PI/9
		l=0.8

		rop1_u_u=branchup(rop1_u,an,l)
		rop1_u_d=branchdown(rop1_u,an,l)

		rop1_d_u=branchup(rop1_d,an,l)
		rop1_d_d=branchdown(rop1_d,an,l)

		bop1_u_u=branchup(bop1_u,an,l)
		bop1_u_d=branchdown(bop1_u,an,l)

		bop1_d_u=branchup(bop1_d,an,l)
		bop1_d_d=branchdown(bop1_d,an,l)

		self.wait(3)

		#separaters

		group1=VGroup(rop1,bop1)
		sep1=Rectangle(width=rop1.get_width()+box_b,height=group1.get_height()+box_b,stroke_color=BLUE)
		sep1.move_to(group1.get_center())
		self.play(ShowCreation(sep1))

		self.wait(2)

		two1=TextMobject("2")
		two1.scale(1.7)
		two1.next_to(box1,DOWN*0.5)
		self.play(Write(two1))

		self.wait()

		group2=VGroup(rop1_u,bop1_d)
		sep2=Rectangle(width=rop1.get_width()+box_b,height=group2.get_height()+box_b,stroke_color=BLUE)
		sep2.move_to(group2.get_center())
		self.play(ShowCreation(sep2))

		self.wait(2)

		two2=TextMobject("2")
		two2.scale(1.7)
		two2.next_to(box2,DOWN*0.5)

		times=TextMobject("$$\\times$$")
		f_g=VGroup(two1,two2)
		times.move_to(f_g.get_center())

		self.play(Write(times),Write(two2))

		self.wait()

		group3=VGroup(rop1_u_u,bop1_d_d)
		sep3=Rectangle(width=rop1.get_width()+box_b,height=group3.get_height()+box_b,stroke_color=BLUE)
		sep3.move_to(group3.get_center())
		self.play(ShowCreation(sep3))

		self.wait(2)

		two3=TextMobject("2")
		two3.scale(1.7)
		two3.next_to(box3,DOWN*0.5)

		times2=TextMobject("$$\\times$$")
		f_g2=VGroup(two2,two3)
		times2.move_to(f_g2.get_center())

		self.play(Write(times2),Write(two3))

		self.wait(2)

		all_=VGroup(two1,two2,two3,times,times2)
		two_cu=TextMobject("$$2^{3}$$")
		two_cu.scale(1.7)
		two_cu.next_to(box2,DOWN,0.6)

		self.play(Transform(all_,two_cu))

		self.wait(3)

		self.play(
			FadeOut(all_),
			FadeOut(sep1),
			FadeOut(sep2),
			FadeOut(sep3)
			)

		self.wait()

		######################
		#Fourth box stuff

		dist=box3.get_center()-box2.get_center()

		self.play(ApplyMethod(boxes.shift,LEFT*dist))

		box4=Rectangle(width=r1.get_width()+box_b,height=r1.get_height()+box_b)

		box4.next_to(box3,RIGHT,1)

		self.play(ShowCreation(box4))

		self.wait()

		self.play(ApplyMethod(box4.set_color,YELLOW))
		self.play(ApplyMethod(box4.set_color,WHITE))

		self.play(ApplyMethod(r1.move_to,box4.get_center()))
		self.wait(0.6)
		self.play(
			ApplyMethod(r1.move_to,ot.get_center()),
			ApplyMethod(b1.move_to,box4.get_center())
			)
		self.wait(0.6)
		self.play(ApplyMethod(b1.move_to,to.get_center()))

		self.wait(3)

		an=PI/14.5
		l=0.5

		rop1_u_u_u=branchup(rop1_u_u,an,l)
		rop1_u_u_d=branchdown(rop1_u_u,an,l)

		rop1_u_d_u=branchup(rop1_u_d,an,l)
		rop1_u_d_d=branchdown(rop1_u_d,an,l)

		rop1_d_u_u=branchup(rop1_d_u,an,l)
		rop1_d_u_d=branchdown(rop1_d_u,an,l)

		rop1_d_d_u=branchup(rop1_d_d,an,l)
		rop1_d_d_d=branchdown(rop1_d_d,an,l)

		bop1_u_u_u=branchup(bop1_u_u,an,l)
		bop1_u_u_d=branchdown(bop1_u_u,an,l)

		bop1_u_d_u=branchup(bop1_u_d,an,l)
		bop1_u_d_d=branchdown(bop1_u_d,an,l)

		bop1_d_u_u=branchup(bop1_d_u,an,l)
		bop1_d_u_d=branchdown(bop1_d_u,an,l)

		bop1_d_d_u=branchup(bop1_d_d,an,l)
		bop1_d_d_d=branchdown(bop1_d_d,an,l)

		self.wait(2)

		two1=TextMobject("2")
		two1.scale(1.7)
		two1.next_to(box2,DOWN*0.5)
		two2=TextMobject("2")
		two2.scale(1.7)
		two2.next_to(box3,DOWN*0.5)

		times=TextMobject("$$\\times$$")
		f_g=VGroup(two1,two2)
		times.move_to(f_g.get_center())
		two3=TextMobject("2")
		two3.scale(1.7)
		two3.next_to(box4,DOWN*0.5)

		times2=TextMobject("$$\\times$$")
		f_g2=VGroup(two2,two3)
		times2.move_to(f_g2.get_center())
		all_=VGroup(two1,two2,two3,times,times2)

		two0=TextMobject("2")
		two0.scale(1.7)
		two0.next_to(box1,DOWN*0.5)

		times0=TextMobject("$$\\times$$")
		f_g0=VGroup(two0,two1)
		times0.move_to(f_g0.get_center())

		all2_=VGroup(
			two0,
			times0,
			all_
			)

		self.play(Write(all2_))

		two_f=TextMobject("$$2^{4}$$")
		two_f.scale(1.7)
		f_g3=VGroup(two1,two2)
		two_f.move_to(f_g3.get_center())

		self.wait()

		self.play(Transform(all2_,two_f))

		self.wait(3)

		self.play(FadeOut(two_f),FadeOut(all2_))

		self.play(FadeOut(box4))

		self.play(ApplyMethod(boxes.shift,RIGHT*dist))

		self.play(
			FadeOut(lines[0]),
			FadeOut(lines[1]),
			FadeOut(lines[2]),
			FadeOut(lines[3]),
			FadeOut(lines[4]),
			FadeOut(lines[5]),
			FadeOut(lines[6]),
			FadeOut(lines[7]),
			FadeOut(lines[8]),
			FadeOut(lines[9]),
			FadeOut(lines[10]),
			FadeOut(lines[11]),
			FadeOut(lines[12]),
			FadeOut(lines[13]),
			FadeOut(lines[14]),
			FadeOut(lines[15]),
			FadeOut(lines[16]),
			FadeOut(lines[17]),
			FadeOut(lines[18]),
			FadeOut(lines[19]),
			FadeOut(lines[20]),
			FadeOut(lines[21]),
			FadeOut(lines[22]),
			FadeOut(lines[23]),
			FadeOut(lines[24]),
			FadeOut(lines[25]),
			FadeOut(lines[26]),
			FadeOut(lines[27]),
			FadeOut(rop1_u),
			FadeOut(rop1_d),
			FadeOut(rop1_u_u),
			FadeOut(rop1_u_d),
			FadeOut(rop1_d_u),
			FadeOut(rop1_d_d),
			FadeOut(rop1_u_u_u),
			FadeOut(rop1_u_d_u),
			FadeOut(rop1_d_u_u),
			FadeOut(rop1_d_d_u),
			FadeOut(rop1_u_u_d),
			FadeOut(rop1_u_d_d),
			FadeOut(rop1_d_u_d),
			FadeOut(rop1_d_d_d),
			FadeOut(bop1_u),
			FadeOut(bop1_d),
			FadeOut(bop1_u_u),
			FadeOut(bop1_u_d),
			FadeOut(bop1_d_u),
			FadeOut(bop1_d_d),
			FadeOut(bop1_u_u_u),
			FadeOut(bop1_u_d_u),
			FadeOut(bop1_d_u_u),
			FadeOut(bop1_d_d_u),
			FadeOut(bop1_u_u_d),
			FadeOut(bop1_u_d_d),
			FadeOut(bop1_d_u_d),
			FadeOut(bop1_d_d_d),
			)

		self.wait(3)

		self.play(ApplyMethod(r1.set_color,GREEN),ApplyMethod(b1.set_color,GREEN))

		self.play(ApplyMethod(r2.move_to,box1.get_center())),

		self.play(
			ApplyMethod(r2.move_to,oo.get_center()),
			ApplyMethod(b2.move_to,box1.get_center())
			)

		self.play(
			ApplyMethod(b2.move_to,tth.get_center()),
			ApplyMethod(r1.move_to,box1.get_center())
			)
		self.play(ApplyMethod(r1.move_to,ot.get_center()))

		self.wait(3)

		gop1=Dot(color=GREEN)
		gop1.scale(2)
		ops=VGroup(rop1,bop1)
		gop1.move_to(ops.get_center())

		self.play(ShowCreation(gop1))

		self.wait(2)

		def branchmid(dot,angle,leng):
			buf=0.15
			down_line=Line(
				#from
				dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle),
				#to
				dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+DOWN*leng*np.sin(angle)
				)
			green=Dot(color=GREEN)
			green.scale(2)
			green.move_to(dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+DOWN*leng*np.sin(angle)+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle))
			lines.append(down_line)
			self.play(ShowCreation(green),ShowCreation(down_line))
			return green

		an=PI/8
		l=1.4

		rop1_u=branchup(rop1,an,l)
		rop1_m=branchmid(rop1,0,np.cos(an)*l)
		rop1_d=branchdown(rop1,an,l)

		gop1_u=branchup(gop1,an,l)
		gop1_m=branchmid(gop1,0,np.cos(an)*l)
		gop1_d=branchdown(gop1,an,l)

		bop1_u=branchup(bop1,an,l)
		bop1_m=branchmid(bop1,0,np.cos(an)*l)
		bop1_d=branchdown(bop1,an,l)

		self.wait(3)

		def branchup(dot,angle,leng):
			buf=0.15
			up_line=Line(
				#from
				dot.get_center()+RIGHT*buf*np.cos(angle)+UP*buf*np.sin(angle),
				#to
				dot.get_center()+RIGHT*buf*np.cos(angle)+UP*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+UP*leng*np.sin(angle)
				)
			red=Dot(color=RED)
			red.scale(1)
			red.move_to(dot.get_center()+RIGHT*buf*np.cos(angle)+UP*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+UP*leng*np.sin(angle)+RIGHT*buf*np.cos(angle)+UP*buf*np.sin(angle))
			lines.append(up_line)
			self.play(ShowCreation(red),ShowCreation(up_line))
			return red

		def branchdown(dot,angle,leng):
			buf=0.15
			down_line=Line(
				#from
				dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle),
				#to
				dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+DOWN*leng*np.sin(angle)
				)
			blue=Dot(color=BLUE)
			blue.scale(1)
			blue.move_to(dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+DOWN*leng*np.sin(angle)+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle))
			lines.append(down_line)
			self.play(ShowCreation(blue),ShowCreation(down_line))
			return blue

		def branchmid(dot,angle,leng):
			buf=0.15
			down_line=Line(
				#from
				dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle),
				#to
				dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+DOWN*leng*np.sin(angle)
				)
			green=Dot(color=GREEN)
			green.scale(1)
			green.move_to(dot.get_center()+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle)+RIGHT*leng*np.cos(angle)+DOWN*leng*np.sin(angle)+RIGHT*buf*np.cos(angle)+DOWN*buf*np.sin(angle))
			lines.append(down_line)
			self.play(ShowCreation(green),ShowCreation(down_line))
			return green

		an=PI/18
		l=1

		rop1_u_u=branchup(rop1_u,an,l)
		rop1_u_m=branchmid(rop1_u,0,np.cos(an)*l)
		rop1_u_d=branchdown(rop1_u,an,l)

		rop1_m_u=branchup(rop1_m,an,l)
		rop1_m_m=branchmid(rop1_m,0,np.cos(an)*l)
		rop1_m_d=branchdown(rop1_m,an,l)

		rop1_d_u=branchup(rop1_d,an,l)
		rop1_d_m=branchmid(rop1_d,0,np.cos(an)*l)
		rop1_d_d=branchdown(rop1_d,an,l)


		gop1_u_u=branchup(gop1_u,an,l)
		gop1_u_m=branchmid(gop1_u,0,np.cos(an)*l)
		gop1_u_d=branchdown(gop1_u,an,l)

		gop1_m_u=branchup(gop1_m,an,l)
		gop1_m_m=branchmid(gop1_m,0,np.cos(an)*l)
		gop1_m_d=branchdown(gop1_m,an,l)

		gop1_d_u=branchup(gop1_d,an,l)
		gop1_d_m=branchmid(gop1_d,0,np.cos(an)*l)
		gop1_d_d=branchdown(gop1_d,an,l)


		bop1_u_u=branchup(bop1_u,an,l)
		bop1_u_m=branchmid(bop1_u,0,np.cos(an)*l)
		bop1_u_d=branchdown(bop1_u,an,l)

		bop1_m_u=branchup(bop1_m,an,l)
		bop1_m_m=branchmid(bop1_m,0,np.cos(an)*l)
		bop1_m_d=branchdown(bop1_m,an,l)

		bop1_d_u=branchup(bop1_d,an,l)
		bop1_d_m=branchmid(bop1_d,0,np.cos(an)*l)
		bop1_d_d=branchdown(bop1_d,an,l)

		self.wait(3)

		self.play(ShowCreation(sep1))
		self.wait()
		th1=TextMobject("3")
		th1.scale(1.7)
		th1.next_to(box1,DOWN,0.2)
		self.play(ShowCreation(th1))

		self.wait(2)

		sep2_pos=VGroup(rop1_u,bop1_d)
		sep2.move_to(sep2_pos.get_center())
		self.play(ShowCreation(sep2))
		self.wait()
		th2=TextMobject("3")
		th2.scale(1.7)
		th2.next_to(box2,DOWN,0.2)
		times2=TextMobject("$$\\times$$")
		f_g4=VGroup(th1,th2)
		times2.move_to(f_g4.get_center())

		self.play(ShowCreation(th2),ShowCreation(times2))

		self.wait(2)

		sep3_pos=VGroup(rop1_u_u,bop1_d_d)
		sep3.move_to(sep3_pos.get_center())
		self.play(ShowCreation(sep3))
		self.wait()
		th3=TextMobject("3")
		th3.scale(1.7)
		th3.next_to(box3,DOWN,0.2)
		times3=TextMobject("$$\\times$$")
		f_g5=VGroup(th2,th3)
		times3.move_to(f_g5.get_center())
		self.play(ShowCreation(th3),ShowCreation(times3))

		self.wait(3)

		th_cu=TextMobject("$$3^{3}$$")
		th_cu.scale(1.7)

		th_cu.next_to(box2,DOWN,0.6)

		threes_plus=VGroup(th1,th2,th3,times3,times2)

		self.play(Transform(threes_plus,th_cu))

		self.wait(4)


#python -m manim MITintegral\Fermat\fermatscenes.py IntroClips -pl
class IntroClips(Scene):
	def construct(self):
		fermat=TextMobject("Fermat's")
		fermat.scale(1.6)
		little=TextMobject("little")
		little.scale(1.2)
		little.set_color(BLUE)
		theorem=TextMobject("theorem")
		theorem.scale(1.6)
		fermat.next_to(little,LEFT,0.5)
		theorem.next_to(little,RIGHT,0.5)

		title=VGroup(fermat,little,theorem)
		title.move_to(ORIGIN)

		self.play(Write(title))

		self.wait(4)

		self.play(FadeOut(title))

		a=TextMobject("$$a$$")
		po=TextMobject("$$p$$")
		a.scale(2)
		po.scale(2)

		pers.sep_exp(a,po)
		po.set_color(BLUE)

		th1=VGroup(a,po)

		min_a=TextMobject("$$-a$$")
		min_a.scale(2)
		min_a.next_to(th1,RIGHT,0.1)
		min_a.align_to(th1,DOWN)

		th=VGroup(th1,min_a)

		bar=Line(ORIGIN,RIGHT*(0.2+th.get_width()),stroke_width=3)

		bar.next_to(th,DOWN,0.13)

		p=TextMobject("$$p$$")
		p.set_color(BLUE)

		p.scale(2)

		p.next_to(bar,DOWN,0.13)

		whole=VGroup(th,bar,p)

		whole.move_to(ORIGIN)

		po.scale(2)

		self.play(Write(po))
		self.wait()
		self.play(ApplyMethod(po.scale,0.5))

		self.play(Write(a))

		self.wait(2)

		self.play(Write(min_a))

		self.wait()

		self.play(ShowCreation(bar))

		self.play(Write(p))

		self.wait(3)

		self.play(FadeOut(whole))

		self.wait(2)

#The following scene represents how I can call on a personal method from the 
#file: my_methods.py, located in manimlib. NOTE: since the method I am using
#uses a "self.play" in the function, it must be passed self (and the method must
#be written to accept self). 

#python -m manim MITintegral\Fermat\fermatscenes.py Calling_Method -pl
class Calling_Method(Scene):
	def construct(self):
		seven=TextMobject("7")
		pers.print_col(self,seven)

		self.wait(2)

#python -m manim MITintegral\Fermat\fermatscenes.py test -pl
class test(Scene):
	def construct(self):

		th=TextMobject("$$3$$")
		five=TextMobject("$$5$$")

		whole=VGroup(th,five)

		whole.scale(3)


		pers.sep_exp(th,five)

		self.play(Write(th),Write(five))

		self.wait(2)

		five.set_color(BLUE)

		self.wait(3)

#python -m manim MITintegral\Fermat\fermatscenes.py ProbCont -pl
class ProbCont(Scene):
	def construct(self):
		base=TextMobject("$$\#\mbox{ colors}$$")
		exp=TextMobject("$$\#\mbox{ boxes}$$")
		min_a=TextMobject("$$-a$$")
		exp.set_color(BLUE)
		base.scale(2)
		exp.scale(2)

		pers.sep_exp(base,exp)

		state=VGroup(base,exp)

		self.play(Write(state))

		self.wait(2)

		a=TextMobject("$$a$$")
		a.move_to(base.get_center())
		a.scale(2)
		self.play(Transform(base,a))

		p=TextMobject("$$p$$")
		p.scale(2)
		p.set_color(BLUE)

		pers.sep_exp(a,p)

		self.wait(2)

		self.play(Transform(exp,p))

		self.wait(3)

		f_g=VGroup(a,p)

		min_a.scale(2)

		min_a.next_to(f_g,RIGHT,0.1)

		min_a.align_to(f_g,DOWN)

		self.play(Write(min_a))

		self.wait(2)

		noth=TextMobject("")

		all_=VGroup(min_a,base,exp)

		self.play(Transform(all_,noth))

		self.wait()

#python -m manim MITintegral\Fermat\fermatscenes.py NoahIntro -pl
class NoahIntro(MovingCameraScene):
	def setup(self):
		MovingCameraScene.setup(self)
	def construct(self):
		treble=SVGMobject("treble_svg",fill_color=BLUE,fill_opacity=0,stroke_width=3,stroke_color=YELLOW)
		treble.scale(3)
		noah=TextMobject("\\textit{NOAH FORBES}",fill_color=WHITE,stroke_width=4,stroke_color=BLUE,fill_opacity=1)
		#noah.set_color(BLUE)
		noah.shift(DOWN)

		music=TextMobject("MUSIC",fill_color=WHITE,stroke_width=2,stroke_color=BLUE)
		music.scale(2)
		notes=TextMobject("NOTES",fill_color=WHITE,stroke_width=2,stroke_color=BLUE)
		notes.scale(2)
		with_=TextMobject("WITH",fill_color=WHITE,stroke_width=2,stroke_color=BLUE)
		with_.shift(UP*0.8)
		with_.scale(1.5)

		music.move_to(UP*2+LEFT*3.4)
		notes.move_to(UP*2+RIGHT*3.4)

		self.bring_to_back(treble)
		self.remove(treble)

		self.wait(2)

		self.play(Write(music))
		self.wait()
		self.play(Write(notes))
		self.wait()
		self.play(Write(with_))
		self.add_foreground_mobjects(with_)
		self.wait()

		noah.scale(3.7)
		self.wait()
		self.play(ShowCreation(treble))
		self.wait()
		self.play(Write(noah))
		self.wait(2)

		self.play(
			ApplyMethod(self.camera_frame.scale,0.006)
			)

		self.wait()

#python -m manim MITintegral\Fermat\fermatscenes.py PrimeShifts -pl
class PrimeShifts(Scene):
	def construct(self):
		r1=Dot(color=RED)
		b1=Dot(color=BLUE)
		r2=Dot(color=RED)

		dots=VGroup(r1,b1,r2)

		dots.scale(2)

		r1.next_to(b1,LEFT)
		r2.next_to(b1,RIGHT)

		self.play(ShowCreation(dots))

		self.wait()

#python -m manim MITintegral\Fermat\fermatscenes.py PieceTogether -pl
class PieceTogether(MovingCameraScene):
	def setup(self):
		MovingCameraScene.setup(self)
	def construct(self):

		arr_sc=2.5

		self.camera_frame.scale(1.5)

		r_dot=Dot(color=RED)
		b_dot=Dot(color=BLUE)
		b2_dot=Dot(color=BLUE)

		scale=4

		r_dot.scale(scale)
		b_dot.scale(scale)
		b2_dot.scale(scale)

		r_dot.next_to(b_dot,LEFT,1)
		b2_dot.next_to(b_dot,RIGHT,1)

		dots=VGroup(r_dot,b_dot,b2_dot)

		self.play(ShowCreation(dots))

		self.wait(2)

		self.play(ApplyMethod(dots.move_to,LEFT*7.5+UP*2))

		r_dot2=Dot(color=RED)
		r2_dot2=Dot(color=RED)
		b_dot2=Dot(color=BLUE)

		r_dot2.scale(scale)
		r2_dot2.scale(scale)
		b_dot2.scale(scale)

		r_dot2.next_to(r2_dot2,LEFT,1)
		b_dot2.next_to(r2_dot2,RIGHT,1)

		_dots=VGroup(r_dot2,r2_dot2,b_dot2)

		_dots.move_to(LEFT*7.5+DOWN*2)

		self.play(ShowCreation(_dots))

		self.wait(2)

		r_dot_u2=Dot(color=BLUE)
		b_dot_u2=Dot(color=RED)
		b2_dot_u2=Dot(color=BLUE)

		scale=4

		r_dot_u2.scale(scale)
		b_dot_u2.scale(scale)
		b2_dot_u2.scale(scale)

		r_dot_u2.next_to(b_dot_u2,LEFT,1)
		b2_dot_u2.next_to(b_dot_u2,RIGHT,1)

		dots_u2=VGroup(r_dot_u2,b_dot_u2,b2_dot_u2)

		dots_u2.shift(UP*2)

		arr_u1=TextMobject("$$\\rightarrow$$")
		arr_u1.scale(arr_sc)
		u_f_g=VGroup(dots,dots_u2)
		arr_u1.move_to(u_f_g.get_center())

		self.play(ShowCreation(arr_u1))

		self.play(ShowCreation(dots_u2))

		self.wait()

		r_dot2_d2=Dot(color=BLUE)
		r2_dot2_d2=Dot(color=RED)
		b_dot2_d2=Dot(color=RED)

		r_dot2_d2.scale(scale)
		r2_dot2_d2.scale(scale)
		b_dot2_d2.scale(scale)

		r_dot2_d2.next_to(r2_dot2_d2,LEFT,1)
		b_dot2_d2.next_to(r2_dot2_d2,RIGHT,1)

		_dots_d2=VGroup(r_dot2_d2,r2_dot2_d2,b_dot2_d2)

		_dots_d2.move_to(DOWN*2)

		arr_d1=TextMobject("$$\\rightarrow$$")
		arr_d1.scale(arr_sc)
		d_f_g=VGroup(_dots,_dots_d2)
		arr_d1.move_to(d_f_g.get_center())

		self.play(ShowCreation(arr_d1))

		self.play(ShowCreation(_dots_d2))

		self.wait(2)

		r_dot_u3=Dot(color=BLUE)
		b_dot_u3=Dot(color=BLUE)
		b2_dot_u3=Dot(color=RED)

		scale=4

		r_dot_u3.scale(scale)
		b_dot_u3.scale(scale)
		b2_dot_u3.scale(scale)

		r_dot_u3.next_to(b_dot_u3,LEFT,1)
		b2_dot_u3.next_to(b_dot_u3,RIGHT,1)

		dots_u3=VGroup(r_dot_u3,b_dot_u3,b2_dot_u3)

		dots_u3.shift(UP*2+RIGHT*(ORIGIN-(dots.get_center()+DOWN*2)))

		arr_u2=TextMobject("$$\\rightarrow$$")
		arr_u2.scale(arr_sc)
		u_f_g=VGroup(dots_u2,dots_u3)
		arr_u2.move_to(u_f_g.get_center())

		self.play(ShowCreation(arr_u2))

		self.play(ShowCreation(dots_u3))

		self.wait()

		r_dot2_d3=Dot(color=RED)
		r2_dot2_d3=Dot(color=BLUE)
		b_dot2_d3=Dot(color=RED)

		r_dot2_d3.scale(scale)
		r2_dot2_d3.scale(scale)
		b_dot2_d3.scale(scale)

		r_dot2_d3.next_to(r2_dot2_d3,LEFT,1)
		b_dot2_d3.next_to(r2_dot2_d3,RIGHT,1)

		_dots_d3=VGroup(r_dot2_d3,r2_dot2_d3,b_dot2_d3)

		_dots_d3.move_to(DOWN*2+RIGHT*(ORIGIN-(dots.get_center()+DOWN*2)))

		arr_d2=TextMobject("$$\\rightarrow$$")
		arr_d2.scale(arr_sc)
		d_f_g=VGroup(_dots_d2,_dots_d3)
		arr_d2.move_to(d_f_g.get_center())

		self.play(ShowCreation(arr_d2))

		self.play(ShowCreation(_dots_d3))

		self.wait(3)

		buff=0.35

		f_g=VGroup(dots,_dots)
		box1=Rectangle(width=dots.get_width()+buff,height=f_g.get_height()+buff,color=BLUE)
		box1.move_to(f_g.get_center())

		box2=Rectangle(width=dots.get_width()+buff,height=f_g.get_height()+buff,color=BLUE)
		box2.move_to(ORIGIN)

		box3=Rectangle(width=dots.get_width()+buff,height=f_g.get_height()+buff,color=BLUE)
		box3.move_to(RIGHT*(ORIGIN-f_g.get_center()))

		self.play(ShowCreation(box1))
		self.play(ShowCreation(box2))
		self.play(ShowCreation(box3))

		self.wait(3)

		self.play(FadeOut(box1),FadeOut(box2),FadeOut(box3))

		exr1=Dot(color=RED)
		exr2=Dot(color=RED)
		exr3=Dot(color=RED)

		exb1=Dot(color=BLUE)
		exb2=Dot(color=BLUE)
		exb3=Dot(color=BLUE)

		exr1.scale(scale)
		exr2.scale(scale)
		exr3.scale(scale)
		exb1.scale(scale)
		exb2.scale(scale)
		exb3.scale(scale)

		exr1.next_to(exr2,LEFT,1)
		exr3.next_to(exr2,RIGHT,1)

		exb1.next_to(exb2,LEFT,1)
		exb3.next_to(exb2,RIGHT,1)

		exr=VGroup(exr1,exr2,exr3)
		exb=VGroup(exb1,exb2,exb3)

		exr.shift(LEFT*4+DOWN*4)

		exb.shift(RIGHT*4+DOWN*4)

		self.play(ShowCreation(exr),ShowCreation(exb))

		self.wait(2)

		self.play(FadeOut(exr),FadeOut(exb))

		self.wait(3)

		a=TextMobject("$$a$$")
		a.scale(3)

		p=TextMobject("$$p$$",color=BLUE)
		p.scale(3)

		pers.sep_exp(a,p)

		ap=VGroup(a,p)
		min_a=TextMobject("$$-a$$")
		min_a.scale(3)
		min_a.next_to(ap,RIGHT,0.1)
		min_a.align_to(ap,DOWN)

		exp=VGroup(a,p,min_a)

		exp.move_to(ORIGIN)

		self.play(Write(ap))
		self.wait()
		self.play(Write(min_a))

		self.wait(3)

#python -m manim MITintegral\Fermat\fermatscenes.py IssueFour -pl
class IssueFour(MovingCameraScene):
	def setup(self):
		MovingCameraScene.setup(self)
	def construct(self):

		set1=pers.construct_dots("r","r","b","b",0,0)

		self.play(ShowCreation(set1))

		self.wait(2)

		self.play(ApplyMethod(set1.scale,0.5))

		self.play(ApplyMethod(set1.move_to,LEFT*5+UP*2))

		self.wait(2)

		set2=pers.construct_dots("r","b","r","b",0,0)
		set2.scale(0.5)
		set2.move_to(LEFT*5+UP*1.33333*0.5)

		set3=pers.construct_dots("r","r","r","b",0,0)
		set3.scale(0.5)
		set3.move_to(LEFT*5+DOWN*1.3333*0.5)

		set4=pers.construct_dots("b","b","b","r",0,0)
		set4.scale(0.5)
		set4.move_to(LEFT*5+DOWN*2)

		self.play(ShowCreation(set2))
		self.play(ShowCreation(set3))
		self.play(ShowCreation(set4))

		self.wait(3)

		####
		#Row1

		set11=pers.construct_dots("b","r","r","b",0,0)
		set11.move_to(UP*2)
		set11.scale(0.5)

		arr1=pers.arrow_maker(set1,set11,WHITE)

		self.play(ShowCreation(arr1))
		self.play(ShowCreation(set11))

		self.wait(2)

		elli=TextMobject("...")
		elli.scale(4)
		elli.move_to(RIGHT*5+UP*2)

		arr11=pers.arrow_maker(set11,elli,WHITE)
		arr11.shift(RIGHT*0.8)

		self.play(ShowCreation(arr11))
		self.play(ShowCreation(elli))

		self.wait(3)

		#####
		#Row 3

		set31=pers.construct_dots("b","r","r","r",0,0)
		set31.scale(0.5)
		set31.move_to(DOWN*0.5*1.3333)
		arr3=pers.arrow_maker(set3,set31,WHITE)

		self.play(ShowCreation(arr3))
		self.play(ShowCreation(set31))

		self.wait()

		elli3=TextMobject("...")
		elli3.scale(4)
		elli3.move_to(RIGHT*5+DOWN*0.5*1.3333)

		arr31=pers.arrow_maker(set31,elli3,WHITE)
		arr31.shift(RIGHT*0.8)

		self.play(ShowCreation(arr31))
		self.play(ShowCreation(elli3))

		#####
		#Row 4

		set41=pers.construct_dots("r","b","b","b",0,0)
		set41.scale(0.5)
		set41.move_to(DOWN*2)
		arr4=pers.arrow_maker(set4,set41,WHITE)

		self.play(ShowCreation(arr4))
		self.play(ShowCreation(set41))

		self.wait()

		elli4=TextMobject("...")
		elli4.scale(4)
		elli4.move_to(RIGHT*5+DOWN*2)

		arr41=pers.arrow_maker(set41,elli4,WHITE)
		arr41.shift(RIGHT*0.8)

		self.play(ShowCreation(arr41))
		self.play(ShowCreation(elli4))

		self.wait(3)

		set21=pers.construct_dots("b","r","b","r",0,0)
		set21.scale(0.5)
		set21.move_to(UP*0.5*1.33333)

		arr2=pers.arrow_maker(set2,set21,WHITE)

		self.play(ShowCreation(arr2))
		self.play(ShowCreation(set21))

		self.wait(3)

		buff=0.35
		col1=VGroup(set1,set4)
		box1=Rectangle(width=col1.get_width()+buff,height=col1.get_height()+buff,color=BLUE)
		box1.move_to(col1.get_center())

		box2=Rectangle(width=col1.get_width()+buff,height=col1.get_height()+buff,color=BLUE)

		box3=Rectangle(width=elli.get_width()+buff,height=elli.get_height()+buff,color=BLUE)
		box3.move_to(elli.get_center())

		ellis=VGroup(elli3,elli4)
		box4=Rectangle(width=ellis.get_width()+buff,height=ellis.get_height()+buff,color=BLUE)
		box4.move_to(ellis.get_center())

		self.play(ShowCreation(box1))
		self.play(ShowCreation(box2))

		self.wait(2)

		self.play(ShowCreation(box3),ShowCreation(box4))
		
		self.wait(3)

		self.play(
			FadeOut(box1),
			FadeOut(box2),
			FadeOut(box3),
			FadeOut(box4)
			)

		self.play(
			ApplyMethod(set1.shift,UP),
			ApplyMethod(set2.shift,UP),
			ApplyMethod(set3.shift,DOWN),
			ApplyMethod(set4.shift,DOWN),

			ApplyMethod(set11.shift,UP),
			ApplyMethod(set21.shift,UP),
			ApplyMethod(set31.shift,DOWN),
			ApplyMethod(set41.shift,DOWN),

			ApplyMethod(arr1.shift,UP),
			ApplyMethod(arr2.shift,UP),
			ApplyMethod(arr3.shift,DOWN),
			ApplyMethod(arr4.shift,DOWN),

			ApplyMethod(arr11.shift,UP),
			ApplyMethod(arr31.shift,DOWN),
			ApplyMethod(arr41.shift,DOWN),

			ApplyMethod(elli.shift,UP),
			ApplyMethod(elli3.shift,DOWN),
			ApplyMethod(elli4.shift,DOWN)

			)

		self.wait()

		a=TextMobject("$$a$$")
		a.scale(3)

		p=TextMobject("$$p$$",color=BLUE)
		p.scale(3)

		pers.sep_exp(a,p)

		ap=VGroup(a,p)
		min_a=TextMobject("$$-a$$")
		min_a.scale(3)
		min_a.next_to(ap,RIGHT,0.1)
		min_a.align_to(ap,DOWN)

		exp=VGroup(a,p,min_a)

		exp.move_to(ORIGIN)

		self.play(Write(ap))
		self.wait()
		self.play(Write(min_a))

		self.wait(3)

#python -m manim MITintegral\Fermat\fermatscenes.py Primes -pl
class Primes(MovingCameraScene):
	def setup(self):
		MovingCameraScene.setup(self)
	def construct(self):
		a=TextMobject("$$2,$$")
		b=TextMobject("$$3,$$")
		c=TextMobject("$$5,$$")
		d=TextMobject("$$7,$$")
		e=TextMobject("$$11,$$")
		f=TextMobject("$$13,$$")
		g=TextMobject("$$17,$$")
		h=TextMobject("$$...$$")

		scale=2
		a.scale(2)
		b.scale(2)
		c.scale(2)
		d.scale(2)
		e.scale(2)
		f.scale(2)
		g.scale(2)
		h.scale(2)

		buff=0.4

		b.next_to(a,RIGHT,buff)
		c.next_to(b,RIGHT,buff)
		d.next_to(c,RIGHT,buff)
		e.next_to(d,RIGHT,buff)
		f.next_to(e,RIGHT,buff)
		g.next_to(f,RIGHT,buff)
		h.next_to(g,RIGHT,buff)

		group=VGroup(a,b,c,d,e,f,g,h)

		group.move_to(ORIGIN)

		self.play(Write(a))
		self.play(Write(b))
		self.play(Write(c))
		self.play(Write(d))
		self.play(Write(e))
		self.play(Write(f))
		self.play(Write(g))
		self.play(Write(h))

		self.wait(2)

		i=TextMobject("$$+1$$")
		j=TextMobject("$$+2$$")
		k=TextMobject("$$+2$$")
		l=TextMobject("$$+4$$")
		m=TextMobject("$$+2$$")
		n=TextMobject("$$+4$$")

		i.scale(scale)
		j.scale(scale)
		k.scale(scale)
		l.scale(scale)
		m.scale(scale)
		n.scale(scale)

		buf=0.3

		i.next_to(a,UP,buf)
		j.next_to(b,UP,buf)
		k.next_to(c,UP,buf)
		l.next_to(d,UP,buf)
		m.next_to(e,UP,buf)
		n.next_to(f,UP,buf)

		adds=VGroup(i,j,k,l,m,n)

		adds.shift(RIGHT*0.15)

		self.play(ShowCreation(i))

		self.play(Transform(i,j))
		self.play(Transform(i,k))
		adds.shift(RIGHT*0.1)
		self.play(Transform(i,l))
		self.play(Transform(i,m))
		self.play(Transform(i,n))

		self.wait(3)

#python -m manim MITintegral\Fermat\fermatscenes.py Test -pl
class Test(Scene):
	def construct(self):
		dot=Dot()
		dot.move_to(RIGHT+UP)
		grace=0.1
		if pers.abs(dot.get_center())<(np.sqrt(2)+grace) and pers.abs(dot.get_center())>(np.sqrt(2)-grace):
			self.play(ShowCreation(dot))

		self.wait(2)