from manimlib.imports import *

#python -m manim MITintegral\tanint\tanint.py OpeningInt -pl
class OpeningInt(Scene):
	def construct(self):
		int1=TextMobject("$$\int x(1-x)^{2020}dx$$")
		mainint=TextMobject("$$\int_{0}^{\\frac{\pi}{2}}\\frac{1}{\\tan^{\sqrt{2020}}(x)+1} dx$$")
		int3=TextMobject("$$\int_{0}^{\infty}\\frac{1}{e^{x}+1} dx$$")
		int4=TextMobject("$$\int_{0}^{\\frac{\pi}{100}}\\frac{\sin(20x)+\sin(19x)}{\cos(20x)+\cos(19x)} dx$$")
		int5=TextMobject("$$\int \cos(\\arctan(x)) dx$$")
		int6=TextMobject("$$\int_{-\infty}^{\infty}e^{-2x^{2}-5x-3} dx$$")
		int7=TextMobject("$$\int_{0}^{\infty}\\frac{\\tanh(x)}{\exp(x)} dx$$")
		int8=TextMobject("$$\int \sqrt{x\sqrt{x\sqrt{x ...}}}dx$$")
		
		refd1=Dot()
		refd2=Dot()
		refd3=Dot()
		refd4=Dot()
		refd5=Dot()
		refd6=Dot()
		refd7=Dot()
		refd8=Dot()

		refd1.move_to(LEFT*6+UP*2.7)
		refd2.next_to(refd1,DOWN*6)
		refd3.next_to(refd2,DOWN*6)
		refd4.next_to(refd3,DOWN*6)
		refd5.move_to(RIGHT+UP*2.7)
		refd6.next_to(refd5,DOWN*6)
		refd7.next_to(refd6,DOWN*6)
		refd8.next_to(refd7,DOWN*6)

		int1.next_to(refd1)
		mainint.next_to(refd2)
		int3.next_to(refd3)
		int4.next_to(refd4)
		int5.next_to(refd5)
		int6.next_to(refd6)
		int7.next_to(refd7)
		int8.next_to(refd8)

		mit=TextMobject("MIT Integration Bee")
		mit.set_color(BLUE)
		mit.move_to(UP)
		mit.scale(2)

		students=TextMobject("16 students")
		students.next_to(mit,DOWN)
		students.scale(1.4)

		winner=TextMobject("1 winner")
		winner.next_to(students,DOWN)
		winner.scale(1.4)

		exam=TextMobject("20 question Qualifying Exam",stroke_width=1,stroke_color=BLUE)
		exam.next_to(mit,DOWN*2)
		exam.scale(1.6)

		ourfunc=TextMobject("$$\\frac{1}{\\tan^{n}(x)+1}$$")
		ourfunc.scale(2)

		circlex=Circle()
		circlex.set_color(BLUE)
		circlex.scale(0.4)
		circlex.shift(DOWN*0.65+RIGHT*0.12)

		self.play(Write(mit))
		self.wait(3)


		self.wait(3)

		self.play(FadeOut(mit))

		self.wait()

		self.play(Write(int1),run_time=0.7)
		self.play(Write(mainint),run_time=0.7)
		self.play(Write(int3),run_time=0.7)
		self.play(Write(int4),run_time=0.7)
		self.play(Write(int5),run_time=0.7)
		self.play(Write(int6),run_time=0.7)
		self.play(Write(int7),run_time=0.7)
		self.play(Write(int8),run_time=0.7)


		self.wait(4)

		group=VGroup(int1,int3,int4,int5,int6,int7,int8)

		self.play(FadeOut(group),ApplyMethod(mainint.move_to,np.array([0,0,0])))

		self.play(ApplyMethod(mainint.scale,2))
		highlight=Rectangle(height=0.8,width=2.3)
		highlight.set_color(BLUE)
		highlight.shift(DOWN*0.5+LEFT*0.37)

		self.wait(2)
		self.play(ShowCreation(highlight))
		self.wait(2)

		group1=VGroup(mainint,highlight)

		self.play(Transform(group1,ourfunc))

		self.wait(2)

		self.play(ShowCreation(circlex))
		self.wait()
		self.play(FadeOut(circlex))
		self.wait(2)

#python -m manim MITintegral\tanint\tanint.py UnitCircle -pl
class UnitCircle(GraphScene):
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
	"x_labeled_nums" :range(-3,3,1),
	"y_labeled_nums" :range(-1,2,1),
	"num_graph_anchor_points": 200,

	} 
	def construct(self):
		angle=math.radians(360)
		arc=Arc(radius=2,angle=angle)

		arcangle=Arc(radius=0.7,angle=math.radians(45))

		arm=Arrow(np.array([0,0,0]),np.array([2*np.sqrt(2)/2,2*np.sqrt(2)/2,0]),buff=0)
		arm.set_color(BLUE)

		#Reference Dot
		#REFDOT DECIDES WHERE THE TRACKERS ARE
		refd=Dot()
		refd.move_to(RIGHT*5+UP*3)
		refd2=Dot()
		refd2.next_to(refd,DOWN*1.6)

		#Sin Definition
		sin_func = lambda x: np.sin(x.get_value())

		x_value = ValueTracker(PI/4)

		sin_func_value = ValueTracker(sin_func(x_value))
		x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
		sin_func_tex = DecimalNumber(sin_func_value.get_value()).add_updater(lambda v: v.set_value(sin_func(x_value)))
		
		#Sin display
		sin_func_tex.next_to(refd,LEFT)
		#self.add(sin_func_tex)

		#Cos Definition
		cos_func = lambda x: np.cos(x.get_value())
		cos_func_value = ValueTracker(cos_func(x_value))
		x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
		cos_func_tex = DecimalNumber(cos_func_value.get_value()).add_updater(lambda v: v.set_value(cos_func(x_value)))
		
		#Tam Definition
		tan_func = lambda x: np.tan(x.get_value())
		tan_func_value = ValueTracker(tan_func(x_value))
		x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
		tan_func_tex = DecimalNumber(tan_func_value.get_value()).add_updater(lambda v: v.set_value(tan_func(x_value)))

		#Define Tip Dot
		#tip=Dot()
		#tip.move_to(np.array([2*np.sqrt(2)/2,2*np.sqrt(2)/2,0]))

		#Origin dot
		#odot=Dot()
		#odot.move_to(ORIGIN)

		#Cos display
		cos_func_tex.next_to(refd2,LEFT)
		#self.add(cos_func_tex)

		#Define braces
		#singroup=VGroup(tip,odot)
		#A BRACE THAT UPDATES (KIND OF)
		#sin=Brace(singroup,RIGHT).add_updater(lambda m: m.next_to(singroup,RIGHT),m.scale())
		sin=Brace(arm,RIGHT)
		cos=Brace(arm,DOWN)

		sin.set_color(BLUE)
		cos.set_color(RED)

		ysinlab=TextMobject("$$\sin(\\theta):$$")
		ysinlab.next_to(sin_func_tex,LEFT)
		ysinlab.set_color(BLUE)
		xcoslab=TextMobject("$$\cos(\\theta):$$")
		xcoslab.next_to(cos_func_tex,LEFT)
		xcoslab.set_color(RED)

		angletheta=TextMobject("$$\\theta$$")
		angletheta.move_to(RIGHT+UP*0.5)


		self.setup_axes(animate=True)

		#path1=self.get_graph(lambda x: np.sqrt(1-x**2),x_min=np.sqrt(2)/2,x_max=-np.sqrt(2)/2)

		self.play(ShowCreation(arc))

		x=TextMobject("$$x:$$")
		x.next_to(cos_func_tex,LEFT)
		x.set_color(RED)
		y=TextMobject("$$y:$$")
		y.next_to(sin_func_tex,LEFT)
		y.set_color(BLUE)

		#Tan display
		tan_func_tex.next_to(cos_func_tex,DOWN*2)
		tanlab=TextMobject("$$\\tan(\\theta):$$")
		tanlab.next_to(tan_func_tex,LEFT)
		yoverx=TextMobject("$$\\frac{y}{x}:$$")
		yoverx.next_to(tan_func_tex,LEFT)

		bracx=TextMobject("$$x$$")
		bracx.next_to(cos,DOWN)
		bracx.set_color(RED)
		bracy=TextMobject("$$y$$")
		bracy.next_to(sin,RIGHT)
		bracy.set_color(BLUE)

		infinity=TextMobject("$$\infty$$")
		undef=TextMobject("(undef.)")
		undef.next_to(infinity,RIGHT,0.2)
		repl=VGroup(infinity,undef)
		repl.move_to(tan_func_tex.get_center()+RIGHT*0.7)

		#Define Markers for angles
		zerodot=Dot()
		zerodot.move_to(np.array([2,0,0]))
		pifourdot=Dot()
		pifourdot.move_to(np.array([2*np.sqrt(2)/2,2*np.sqrt(2)/2,0]))
		pitwodot=Dot()
		pitwodot.move_to(np.array([0,2,0]))
		pithreefourdot=Dot()
		pithreefourdot.move_to(np.array([-2*np.sqrt(2)/2,2*np.sqrt(2)/2,0]))
		pidot=Dot()
		pidot.move_to(np.array([-2,0,0]))

		pifivefourdot=Dot()
		pifivefourdot.move_to(np.array([-2*np.sqrt(2)/2,-2*np.sqrt(2)/2,0]))
		pithreetwodot=Dot()
		pithreetwodot.move_to(np.array([0,-2,0]))
		pisevenfourdot=Dot()
		pisevenfourdot.move_to(np.array([2*np.sqrt(2)/2,-2*np.sqrt(2)/2,0]))

		#Define Labels for angles

		buff=0.5

		zerolab=TextMobject("$$0$$")
		zerolab.scale(0.65)
		zerolab.next_to(zerodot,RIGHT*buff+UP*buff)
		pifourlab=TextMobject("$$\\frac{\pi}{4}$$")
		pifourlab.scale(0.65)
		pifourlab.next_to(pifourdot,RIGHT*buff+UP*buff)
		pitwolab=TextMobject("$$\\frac{\pi}{2}$$")
		pitwolab.scale(0.65)
		pitwolab.next_to(pitwodot,RIGHT*buff+UP*buff)
		pithreefourlab=TextMobject("$$\\frac{3\pi}{4}$$")
		pithreefourlab.scale(0.65)
		pithreefourlab.next_to(pithreefourdot,LEFT*buff+UP*buff)
		pilab=TextMobject("$$\pi$$")
		pilab.scale(0.65)
		pilab.next_to(pidot,LEFT*buff+UP*buff)
		pifivefourlab=TextMobject("$$\\frac{5\pi}{4}$$")
		pifivefourlab.scale(0.65)
		pifivefourlab.next_to(pifivefourdot,LEFT*buff+DOWN*buff)
		pithreetwolab=TextMobject("$$\\frac{3\pi}{2}$$")
		pithreetwolab.scale(0.65)
		pithreetwolab.next_to(pithreetwodot,RIGHT*buff+DOWN*buff)
		pisevenfourlab=TextMobject("$$\\frac{7\pi}{4}$$")
		pisevenfourlab.scale(0.65)
		pisevenfourlab.next_to(pisevenfourdot,RIGHT*buff+DOWN*buff)



		allrads=VGroup(zerolab,pifourlab,pitwolab,pithreefourlab,pilab,pifivefourlab,pithreetwolab,pisevenfourlab)

		#self.play(ShowCreation(tip))
		#self.play(MoveAlongPath(tip,path1))

		#NONCOLORED X AND Y LABELS
		xnc=TextMobject("$$x:$$")
		xnc.next_to(cos_func_tex,LEFT)
		ync=TextMobject("$$y:$$")
		ync.next_to(sin_func_tex,LEFT)

		self.wait(2)
		self.play(ShowCreation(arm))
		self.wait()
		self.play(ShowCreation(arcangle),ShowCreation(angletheta))
		self.wait(2)

		self.play(

			Write(allrads)

			)

		self.wait(2)
		self.play(ShowCreation(sin),ShowCreation(ysinlab),ShowCreation(sin_func_tex))
		self.wait(2)
		self.play(ShowCreation(cos),ShowCreation(xcoslab),ShowCreation(cos_func_tex))
		self.wait(3)
		self.play(Transform(ysinlab,y),Transform(xcoslab,x),ShowCreation(bracy),ShowCreation(bracx))
		self.wait()
		self.play(FadeOut(sin),FadeOut(cos),FadeOut(bracx),FadeOut(bracy),
			FadeOut(arcangle),FadeOut(angletheta),Transform(ysinlab,ync),Transform(xcoslab,xnc))
		self.wait()


		self.play(
			Rotating(arm,radians=PI/2,about_point=np.array([0,0,0])),
			x_value.set_value,(3*PI)/4,rate_func=linear,run_time=2.5
			)

		sin=Brace(arm,LEFT)
		sin.set_color(BLUE)
		cos=Brace(arm,DOWN)
		cos.set_color(RED)

		bracx=TextMobject("$$x$$")
		bracx.next_to(cos,DOWN)
		bracx.set_color(RED)
		bracy=TextMobject("$$y$$")
		bracy.next_to(sin,LEFT)
		bracy.set_color(BLUE)

		self.play(ShowCreation(sin),Transform(ysinlab,y))
		self.play(ShowCreation(cos),Transform(xcoslab,x))
		self.wait(1.5)
		self.play(FadeOut(sin),FadeOut(cos),Transform(ysinlab,ync),Transform(xcoslab,xnc))

		x_value=ValueTracker((3*PI)/4)

		self.wait(2)

		self.play(
			Rotating(arm,radians=-PI/2,about_point=np.array([0,0,0])),
			x_value.set_value,PI/4,rate_func=linear,run_time=2.5
			)

		self.wait(2)

		self.play(ShowCreation(tan_func_tex),ShowCreation(tanlab))

		x_value=ValueTracker(PI/4)

		self.wait(3)

		self.play(Transform(tanlab,yoverx))

		self.wait()

		#self.play(
		#	Rotating(arm,radians=PI/2,about_point=np.array([0,0,0])),
		#	x_value.set_value,(3*PI)/4,rate_func=linear,run_time=10
		#	)

		#self.wait(4)

		#x_value=ValueTracker((3*PI)/4)

		#self.play(
		#	Rotating(arm,radians=-(3*PI)/4,about_point=np.array([0,0,0])),
		#	x_value.set_value,0,rate_func=linear,run_time=3
		#	)

		#self.wait(2)

		self.play(
			Rotating(arm,radians=-PI/4,about_point=np.array([0,0,0])),
			x_value.set_value,0,rate_func=linear,run_time=3
			)
		self.wait(3)
		x_value=ValueTracker(0)

		self.play(
			Rotating(arm,radians=PI/2,about_point=np.array([0,0,0])),
			x_value.set_value,PI/2,rate_func=linear,run_time=3
			)

		self.remove(tan_func_tex)
		self.add(repl)

		self.wait(3)

		self.remove(repl)
		self.add(tan_func_tex)

		x_value=ValueTracker(PI/2)

		self.play(
			Rotating(arm,radians=-PI/4,about_point=np.array([0,0,0])),
			x_value.set_value,PI/4,rate_func=linear,run_time=1.2
			)

		self.wait(2)

		x_value=ValueTracker(PI/4)

		self.play(
			Rotating(arm,radians=PI/2,about_point=np.array([0,0,0])),
			x_value.set_value,(3*PI)/4,rate_func=linear,run_time=2
			)

		self.wait(2)

		x_value=ValueTracker((3*PI)/4)

		self.play(
			Rotating(arm,radians=PI/2,about_point=np.array([0,0,0])),
			x_value.set_value,(5*PI)/4,rate_func=linear,run_time=2
			)

		self.wait(2)

		x_value=ValueTracker((5*PI)/4)

		self.play(
			Rotating(arm,radians=PI/2,about_point=np.array([0,0,0])),
			x_value.set_value,(7*PI)/4,rate_func=linear,run_time=2
			)

		self.wait(2)

		x_value=ValueTracker((7*PI)/4)

		self.play(
			Rotating(arm,radians=PI/2,about_point=np.array([0,0,0])),
			x_value.set_value,(9*PI)/4,rate_func=linear,run_time=2
			)

		self.wait(4)

#python -m manim MITintegral\tanint\tanint.py NotesOnFunc -pl
class NotesOnFunc(Scene):
	def construct(self):
		ourfunc=TextMobject("$$f(x)=\\frac{1}{\\tan^{\sqrt{2020}}(x)+1}$$")
		vertline=Line(np.array([3,2,0]),np.array([3,-2,0]))
		horline=Line(np.array([2,1.5,0]),np.array([4,1.5,0]))

		fofx=TextMobject("$$f(x)$$")
		fofx.next_to(horline,UP,0.1)
		fofx.shift(0.65*RIGHT)
		xout=TextMobject("$$x$$")
		xout.next_to(horline,UP,0.1)
		xout.shift(0.4*LEFT)

		horline.shift(RIGHT*0.35)

		#Values
		#Zero
		xzero=TextMobject("$$0$$")
		fxzero=TextMobject("$$1$$")
		zeroourfunc=TextMobject("$$f(0)=\\frac{1}{\\tan^{\sqrt{2020}}(0)+1}$$")
		zeroourfuncup=TextMobject("$$f(0)=\\frac{1}{0+1}$$")
		xzero.next_to(xout,DOWN)
		fxzero.next_to(fofx,DOWN)
		zeroourfunc.shift(LEFT*2)
		zeroourfuncup.shift(LEFT*2)

		#pi over four
		xpifour=TextMobject("$$\\frac{\pi}{4}$$")
		fxpifour=TextMobject("$$\\frac{1}{2}$$")
		pifourourfunc=TextMobject("$$f(\\frac{\pi}{4})=\\frac{1}{\\tan^{\sqrt{2020}}(\\frac{\pi}{4})+1}$$")
		pifourourfuncup=TextMobject("$$f(\\frac{\pi}{4})=\\frac{1}{1+1}$$")
		xpifour.next_to(xzero,DOWN)
		fxpifour.next_to(fxzero,DOWN)
		pifourourfunc.move_to(zeroourfunc.get_center())
		pifourourfuncup.move_to(zeroourfunc.get_center())

		#pi over two
		xpitwo=TextMobject("$$\\frac{\pi}{2}$$")
		fxpitwo=TextMobject("$$\\frac{1}{\infty}$$")
		pitwoourfunc=TextMobject("$$f(\\frac{\pi}{2})=\\frac{1}{\\tan^{\sqrt{2020}}(\\frac{\pi}{2})+1}$$")
		pitwoourfuncup=TextMobject("$$f(\\frac{\pi}{2})=\\frac{1}{\infty+1}$$")
		xpitwo.next_to(xpifour,DOWN*1.8)
		fxpitwo.next_to(fxpifour,DOWN)
		pitwoourfunc.move_to(zeroourfunc.get_center())
		pitwoourfuncup.move_to(zeroourfunc.get_center())

		inftyiszero=TextMobject("$$0$$")
		inftyiszero.move_to(fxpitwo.get_center())

		self.play(Write(ourfunc))
		self.wait()
		self.play(ApplyMethod(ourfunc.shift,LEFT*2))
		self.wait()
		self.play(ShowCreation(vertline),ShowCreation(horline),Write(fofx),Write(xout))
		self.wait(2)
		self.play(Write(xzero),Transform(ourfunc,zeroourfunc))
		self.wait()
		self.play(Transform(ourfunc,zeroourfuncup))
		self.wait()
		self.play(Write(fxzero))
		self.wait()
		self.play(Write(xpifour),Transform(ourfunc,pifourourfunc))
		self.wait()
		self.play(Transform(ourfunc,pifourourfuncup))
		self.wait()
		self.play(Write(fxpifour))
		self.wait()
		self.play(Write(xpitwo),Transform(ourfunc,pitwoourfunc))
		self.wait()
		self.play(Transform(ourfunc,pitwoourfuncup))
		self.wait()
		self.play(Write(fxpitwo))
		self.wait()
		self.play(Transform(fxpitwo,inftyiszero))
		self.wait(4)

#python -m manim MITintegral\tanint\tanint.py GraphGuess -pl
class GraphGuess(GraphScene,MovingCameraScene):
	CONFIG = {
	"x_min" : -3,
	"x_max" : 3,
	"y_min" : -2,
	"y_max" : 2,
	"x_tick_frequency": 1,
	"y_tick_frequency": 2,
	"y_axis_height":8,
	"x_axis_width":12,
	"graph_origin" : ORIGIN,
	"function_color" : RED ,
	"axes_color" : GREEN,
	"y_labeled_nums" :range(-1,2,1),
	"num_graph_anchor_points": 200,

	} 

	def setup(self):
		GraphScene.setup(self)
		MovingCameraScene.setup(self)

	def construct(self):


		bar1=Line(np.array([2,-10,0]),np.array([2,10,0]),stroke_color=GREEN,stroke_opacity=0.5)
		bar2=Line(np.array([4,-10,0]),np.array([4,10,0]),stroke_color=GREEN,stroke_opacity=0.5)
		bar3=Line(np.array([-2,-10,0]),np.array([-2,10,0]),stroke_color=GREEN,stroke_opacity=0.5)
		bar4=Line(np.array([-4,-10,0]),np.array([-4,10,0]),stroke_color=GREEN,stroke_opacity=0.5)

		bars=VGroup(bar1,bar2,bar3,bar4)

		pi=TextMobject("$$\pi$$")
		#pi.scale(0.5)
		pi.move_to(np.array([2,0,0])+0.3*UP+0.5*RIGHT)
		npi=TextMobject("$$-\pi$$")
		#npi.scale(0.5)
		npi.move_to(np.array([-2,0,0])+0.3*UP+0.5*RIGHT)
		tpi=TextMobject("$$2\pi$$")
		#tpi.scale(0.5)
		tpi.move_to(np.array([4,0,0])+0.3*UP+0.5*RIGHT)
		ntpi=TextMobject("$$-2\pi$$")
		#ntpi.scale(0.5)
		ntpi.move_to(np.array([-4,0,0])+0.3*UP+0.5*RIGHT)

		labels=VGroup(pi,npi,ntpi,tpi)

		oneup=Line(np.array([-20,2,0]),np.array([20,2,0]),stroke_color=GREEN,stroke_opacity=0.5)
		onedown=Line(np.array([-20,-2,0]),np.array([20,-2,0]),stroke_color=GREEN,stroke_opacity=0.5)
		cross=VGroup(oneup,onedown)
		cross.set_color(GREEN)

		zerodot1=Dot()
		zerodot1.move_to(np.array([0,2,0]))
		zerodot2=Dot()
		zerodot2.move_to(np.array([2,2,0]))
		zerodot3=Dot()
		zerodot3.move_to(np.array([-2,2,0]))
		zerodot4=Dot()
		zerodot4.move_to(np.array([4,2,0]))
		zerodot5=Dot()
		zerodot5.move_to(np.array([-4,2,0]))

		zerodots=VGroup(zerodot1,zerodot2,zerodot3,zerodot4,zerodot5)
		zerodots.set_color(BLUE)

		pidot1=Dot()
		pidot1.move_to(np.array([1,0,0]))
		pidot2=Dot()
		pidot2.move_to(np.array([3,0,0]))
		pidot3=Dot()
		pidot3.move_to(np.array([-1,0,0]))
		pidot4=Dot()
		pidot4.move_to(np.array([-3,0,0]))
		pidot5=Dot()
		pidot5.move_to(np.array([5,0,0]))

		pidots=VGroup(pidot1,pidot2,pidot3,pidot4,pidot5)
		pidots.set_color(BLUE)

		middot1=Dot()
		middot1.move_to(np.array([0.5,1,0]))
		middot2=Dot()
		middot2.move_to(np.array([2.5,1,0]))
		middot3=Dot()
		middot3.move_to(np.array([4.5,1,0]))
		middot4=Dot()
		middot4.move_to(np.array([-1.5,1,0]))
		middot5=Dot()
		middot5.move_to(np.array([-3.5,1,0]))

		middots=VGroup(middot1,middot2,middot3,middot4,middot5)
		middots.set_color(BLUE)




		self.setup_axes(animate=True)

		func_graph_r1=self.get_graph(self.thefunc,x_min=0,x_max=0.5)
		func_graph_r2=self.get_graph(self.thefunc,x_min=1,x_max=1.5)
		func_graph_r3=self.get_graph(self.thefunc,x_min=2,x_max=2.5)
		func_graph_r4=self.get_graph(self.thefunc,x_min=-1,x_max=-0.5)
		func_graph_r5=self.get_graph(self.thefunc,x_min=-2,x_max=-1.5)

		func_graph2_r1=self.get_graph(self.thefunc2,x_min=0,x_max=0.5)
		func_graph2_r2=self.get_graph(self.thefunc2,x_min=1,x_max=1.5)
		func_graph2_r3=self.get_graph(self.thefunc2,x_min=2,x_max=2.5)
		func_graph2_r4=self.get_graph(self.thefunc2,x_min=-1,x_max=-0.5)
		func_graph2_r5=self.get_graph(self.thefunc2,x_min=-2,x_max=-1.5)

		func_graph3_r1=self.get_graph(self.thefunc3,x_min=0,x_max=0.5)
		func_graph3_r2=self.get_graph(self.thefunc3,x_min=1,x_max=1.5)
		func_graph3_r3=self.get_graph(self.thefunc3,x_min=2,x_max=2.5)
		func_graph3_r4=self.get_graph(self.thefunc3,x_min=-1,x_max=-0.5)
		func_graph3_r5=self.get_graph(self.thefunc3,x_min=-2,x_max=-1.5)

		func_graph4_r1=self.get_graph(self.thefunc4,x_min=0,x_max=0.5)
		func_graph4_r2=self.get_graph(self.thefunc4,x_min=1,x_max=1.5)
		func_graph4_r3=self.get_graph(self.thefunc4,x_min=2,x_max=2.5)
		func_graph4_r4=self.get_graph(self.thefunc4,x_min=-1,x_max=-0.5)
		func_graph4_r5=self.get_graph(self.thefunc4,x_min=-2,x_max=-1.5)

		region1=Rectangle(width=1,height=20,fill_color=BLUE,fill_opacity=0.2,stroke_color=BLUE,stroke_opacity=0.6)
		region1.shift(RIGHT*0.5+RIGHT*1)
		region2=Rectangle(width=1,height=20,fill_color=BLUE,fill_opacity=0.2,stroke_color=BLUE,stroke_opacity=0.6)
		region2.shift(RIGHT*0.5+RIGHT*3)
		region3=Rectangle(width=1,height=20,fill_color=BLUE,fill_opacity=0.2,stroke_color=BLUE,stroke_opacity=0.6)
		region3.shift(RIGHT*0.5+RIGHT*5)
		region4=Rectangle(width=1,height=20,fill_color=BLUE,fill_opacity=0.2,stroke_color=BLUE,stroke_opacity=0.6)
		region4.shift(RIGHT*0.5+LEFT*1)
		region5=Rectangle(width=1,height=20,fill_color=BLUE,fill_opacity=0.2,stroke_color=BLUE,stroke_opacity=0.6)
		region5.shift(RIGHT*0.5+LEFT*3)

		regions=VGroup(region1,region2,region3,region4,region5)

		piover2lab=TextMobject("$$\\frac{\pi}{2}$$")
		piover2lab.move_to(np.array([1,0,0])+0.4*DOWN)
		piover2lab.scale(0.35)

		primeregion=Rectangle(width=1,height=2,stroke_color=BLUE,stroke_opacity=0.6)
		primeregion.shift(RIGHT*0.5+UP)

		finreg=Rectangle(width=1,height=1,stroke_color=BLUE,stroke_opacity=0.6)
		finreg.shift(RIGHT*0.5+UP*0.5)


		self.wait()
		self.play(ShowCreation(labels))
		self.wait()
		self.play(ShowCreation(bars))
		self.play(ShowCreation(cross))
		self.wait()
		self.play(ShowCreation(zerodots))
		self.wait(2)
		self.play(ShowCreation(pidots))
		self.wait(2)
		self.play(
			ShowCreation(func_graph_r1),
			ShowCreation(func_graph_r2),
			ShowCreation(func_graph_r3),
			ShowCreation(func_graph_r4),
			ShowCreation(func_graph_r5)
			)
		self.wait(2)
		self.play(
			Transform(func_graph_r1,func_graph2_r1),
			Transform(func_graph_r2,func_graph2_r2),
			Transform(func_graph_r3,func_graph2_r3),
			Transform(func_graph_r4,func_graph2_r4),
			Transform(func_graph_r5,func_graph2_r5)
			)
		self.wait(2)
		self.play(
			Transform(func_graph_r1,func_graph3_r1),
			Transform(func_graph_r2,func_graph3_r2),
			Transform(func_graph_r3,func_graph3_r3),
			Transform(func_graph_r4,func_graph3_r4),
			Transform(func_graph_r5,func_graph3_r5)
			)
		

		self.wait(4)

		self.play(ShowCreation(middots))
		self.wait(2)
		self.play(
			Transform(func_graph_r1,func_graph4_r1),
			Transform(func_graph_r2,func_graph4_r2),
			Transform(func_graph_r3,func_graph4_r3),
			Transform(func_graph_r4,func_graph4_r4),
			Transform(func_graph_r5,func_graph4_r5)
			)
		self.wait(2)
		self.play(ShowCreation(regions))
		self.wait(2)
		self.play(FadeOut(regions))
		self.wait(2)
		self.play(

			self.camera_frame.scale,0.45,
			self.camera_frame.move_to,RIGHT+UP,

			ApplyMethod(middot1.scale,0.45),
			ApplyMethod(middot2.scale,0.45),
			ApplyMethod(middot3.scale,0.45),
			ApplyMethod(middot4.scale,0.45),
			ApplyMethod(middot5.scale,0.45),

			ApplyMethod(zerodot1.scale,0.45),
			ApplyMethod(zerodot2.scale,0.45),
			ApplyMethod(zerodot3.scale,0.45),
			ApplyMethod(zerodot4.scale,0.45),
			ApplyMethod(zerodot5.scale,0.45),


			ApplyMethod(pidot1.scale,0.45),
			ApplyMethod(pidot2.scale,0.45),
			ApplyMethod(pidot3.scale,0.45),
			ApplyMethod(pidot4.scale,0.45),
			ApplyMethod(pidot5.scale,0.45),

			ApplyMethod(pi.scale,0.45),
			ApplyMethod(npi.scale,0.45),
			ApplyMethod(ntpi.scale,0.45),
			ApplyMethod(tpi.scale,0.45),

			
			ApplyMethod(pi.scale,0.45),
			ApplyMethod(npi.scale,0.45),
			Write(piover2lab),

			FadeOut(cross),

			FadeOut(bars)

			)

		self.play(
			ApplyMethod(pi.shift,LEFT*0.2+DOWN*0.1),
			ApplyMethod(npi.shift,LEFT*0.2+DOWN*0.1),
			run_time=0.5
			)

		self.wait(2)


		#Area Stuff
		flat_graph=self.get_graph(self.flat,x_min=0,x_max=0.5)
		top_graph=self.get_graph(self.thefuncshifted,x_min=2,x_max=2.5)


		flat_graph_area=self.get_area(flat_graph,0,0.25)
		graph_area=self.get_area(func_graph4_r1,0.25,0.5)
		top_graph_area=self.get_area(top_graph,2,2.25)

		top_graph_area.shift(LEFT*4+UP)


		self.play(ShowCreation(primeregion))
		self.wait(2)

		self.play(
			ShowCreation(flat_graph_area),
			ShowCreation(graph_area),
			ShowCreation(top_graph_area))
		self.wait(2)

		self.play(ApplyMethod(func_graph4_r1.set_color,YELLOW))

		self.wait()

		self.play(ApplyMethod(func_graph4_r1.set_color,BLUE))

		self.wait()

		self.play(
			Rotating(top_graph_area,radians=-PI,about_point=primeregion.get_center()),
			rate_func=linear,run_time=1.5
			)

		self.wait(2)

		self.play(Transform(primeregion,finreg))

		area_width=VGroup(flat_graph_area,graph_area)

		width_brace=Brace(area_width,DOWN)
		width_lab=TextMobject("$$w$$")
		w_tot=VGroup(width_brace,width_lab)
		w_tot.set_color(BLUE)

		height_brace=Brace(top_graph_area,RIGHT)
		height_lab=TextMobject("$$h$$")
		h_tot=VGroup(height_brace,height_lab)
		h_tot.set_color(BLUE)

		self.wait()
		self.play(ShowCreation(width_brace))
		self.wait()
		self.play(ShowCreation(height_brace))

		self.wait(4)

	def thefunc(self,x):
		return 1/(np.tan(x*PI)+1)

	def thefunc2(self,x):
		return 1/(np.power(np.tan(x*PI),5)+1)

	def thefunc3(self,x):
		return 1/(np.tan(x*PI)*3+1)

	def thefunc4(self,x):
		return 1/(np.tan(x*PI)+1)

	def flat(self,x):
		return 0.5

	def thefuncshifted(self,x):
		return 1/(np.tan(x*PI)+1)-0.5


#python -m manim MITintegral\tanint\tanint.py ZoomPractice -pl
class ZoomPractice(MovingCameraScene):
	def construct(self):
		dot1=Dot()
		dot2=Dot()
		dot2.shift(RIGHT)

		self.play(ShowCreation(dot1),ShowCreation(dot2))
		self.play(

			self.camera_frame.scale,0.5,
			self.camera_frame.move_to,dot2.get_center()
			)
		self.wait(2)
		self.play(ApplyMethod(dot1.set_color,RED))
		self.wait(4)

#python -m manim MITintegral\tanint\tanint.py OddFunctions -pl
class OddFunctions(GraphScene,MovingCameraScene):
	CONFIG = {
	"x_min" : -9,
	"x_max" : 9,
	"y_min" : -6,
	"y_max" : 6,
	"x_tick_frequency": 1,
	"y_tick_frequency": 2,
	"y_axis_height":8,
	"x_axis_width":12,
	"graph_origin" : ORIGIN,
	"function_color" : RED ,
	"axes_color" : WHITE,
	#"x_labeled_nums" :range(-9,9,3),
	#"y_labeled_nums" :range(-6,6,2),
	"num_graph_anchor_points": 200,
	"always_update_mobjects": True,
    "always_continually_update": True,

	} 

	def setup(self):
		GraphScene.setup(self)
		MovingCameraScene.setup(self)

	def construct(self):
		odd=TextMobject("Odd")
		functions=TextMobject("Functions")
		functions.next_to(odd,RIGHT)
		odd_functions=VGroup(odd,functions)
		odd_functions.move_to(ORIGIN)
		odd_functions.scale(2)
		nothing=TextMobject("")

		#Dots
		dotr=Dot()
		dotl=Dot()
		dotr.set_color(GREEN)
		dotl.set_color(GREEN)

		self.play(Write(odd_functions))
		self.wait(2)
		self.play(ApplyMethod(odd.set_color,BLUE),run_time=0.3)
		self.wait(2)
		self.play(FadeOut(odd_functions),run_time=0.5)
		#self.play(Transform(odd_functions,nothing))
		#self.play(ApplyMethod(odd_functions.scale,0.5))
		#self.play(ApplyMethod(odd_functions.shift,RIGHT*3+UP*2))

		self.setup_axes(animate=True)

		odd1_graph=self.get_graph(self.odd1,x_min=-9,x_max=9)
		odd2_graph=self.get_graph(self.odd2,x_min=-9,x_max=9)
		odd3_graph=self.get_graph(self.odd3,x_min=-9,x_max=9)
		odd4_graph=self.get_graph(self.odd4,x_min=-9,x_max=9)

		self.play(ShowCreation(odd1_graph),run_time=3)
		self.wait(1.5)
		self.play(Transform(odd1_graph,odd2_graph))
		self.wait(1.5)
		self.play(Transform(odd1_graph,odd3_graph))
		self.wait(1.5)
		self.play(Transform(odd1_graph,odd4_graph))

		self.wait(4)

		#DASHED LINE STUFF

		#Origins of the dotted line (right and left respectively)
		Origin=self.coords_to_point(2,0)
		Origin2=self.coords_to_point(-2,0)

		#Create the dots
		Point1=Dot(color=RED)
		Point2=Dot(color=RED)

		#Create the dots at the ORIGIN and move them to the origins of the dotted lines
		self.play(
			ShowCreation(Point1),
			ShowCreation(Point2)
			)

		self.play(
			ApplyMethod(Point1.move_to,self.coords_to_point(2,0)),
			ApplyMethod(Point2.move_to,self.coords_to_point(-2,0))
			)

		#Define lines that go from the origins of the lines to the dots
		line=DashedLine(Origin,Point1)
		line2=DashedLine(Origin2,Point2)

		#Define functions that re-define the line as new_line
		def update_line(line):
			new_line=DashedLine(Origin,Point1)
			line.become(new_line)

		def update_line2(line):
			new_line2=DashedLine(Origin2,Point2)
			line2.become(new_line2)

		#Add in the lines
		self.add(line,line2)

		#Move the dots the their first position
		self.play(

			#Use UpdateFromFunc to say "turn line into new line"
			UpdateFromFunc(line,update_line),

			#Move the point to the coordinates defined by the function
			ApplyMethod(Point1.move_to,self.coords_to_point(2,7*np.arctan((2)/3)*np.exp(-np.power((2)/3,2)))),

			UpdateFromFunc(line2,update_line2),
			ApplyMethod(Point2.move_to,self.coords_to_point(-2,7*np.arctan((-2)/3)*np.exp(-np.power((-2)/3,2)))),

			rate_func=smooth,
			run_time=2,
		)
		self.wait(2)

		#Move the dots back to the number line
		self.play(

			#Use UpdateFromFunc to say "turn line into new line"
			UpdateFromFunc(line,update_line),

			#Move the point to the coordinates defined by the function
			ApplyMethod(Point1.move_to,self.coords_to_point(2,0)),

			UpdateFromFunc(line2,update_line2),
			ApplyMethod(Point2.move_to,self.coords_to_point(-2,0)),

			rate_func=smooth,
			run_time=2,
		)

		#Remove the lines
		self.remove(line,line2)

		#Move dots to their new starting position
		self.play(
			ApplyMethod(Point1.move_to,self.coords_to_point(4,0)),
			ApplyMethod(Point2.move_to,self.coords_to_point(-4,0)),
			run_time=0.7
			)

		#Re-define the starting position of the dotted lines
		Origin=self.coords_to_point(4,0)
		Origin2=self.coords_to_point(-4,0)

		#Add in the lines again
		self.add(line,line2)

		#Move the dots the the graph in position 2
		self.play(

			#Use UpdateFromFunc to say "turn line into new line"
			UpdateFromFunc(line,update_line),

			#Move the point to the coordinates defined by the function
			ApplyMethod(Point1.move_to,self.coords_to_point(4,7*np.arctan((4)/3)*np.exp(-np.power((4)/3,2)))),

			UpdateFromFunc(line2,update_line2),
			ApplyMethod(Point2.move_to,self.coords_to_point(-4,7*np.arctan((-4)/3)*np.exp(-np.power((-4)/3,2)))),

			rate_func=smooth,
			run_time=1,
		)

		self.wait(2)

		pospos=TextMobject("$$(+,+)$$")
		negneg=TextMobject("$$(-,-)$$")

		pospos.move_to(self.coords_to_point(4,7*np.arctan((4)/3)*np.exp(-np.power((4)/3,2)))+RIGHT+UP*0.5)
		negneg.move_to(self.coords_to_point(-4,7*np.arctan((-4)/3)*np.exp(-np.power((-4)/3,2)))+LEFT+DOWN*0.5)

		pospos.set_color(GREEN)
		negneg.set_color(RED)

		self.play(Write(pospos))
		self.wait()
		self.play(Write(negneg))

		self.wait(2)

		left_f=TextMobject("$$f($$")
		left_f_x=TextMobject("$$+x$$")
		left_f_par=TextMobject("$$)=$$")
		left_f_x_neg=TextMobject("$$-x$$")
		left_f_x_neg.set_color(RED)

		right_f=TextMobject("$$f(x)$$")
		right_f_pos=TextMobject("$$+$$")
		right_f_neg=TextMobject("$$-$$")
		right_f_neg.set_color(RED)

		left_f.move_to(LEFT*3+UP*2)
		left_f_x.next_to(left_f,RIGHT,0.08)
		left_f_x_neg.next_to(left_f,RIGHT,0.08)
		left_f_par.next_to(left_f_x,RIGHT,0.08)

		right_f_neg.next_to(left_f_par,RIGHT,0.08)
		right_f_pos.next_to(left_f_par,RIGHT,0.08)
		right_f.next_to(right_f_neg,RIGHT,0.08)

		whole_eq=VGroup(left_f,left_f_x,left_f_par,left_f_x_neg,right_f,right_f_neg,right_f_pos)

		whole_eq.shift(LEFT*1.4)

		pos_group=VGroup(left_f,left_f_x,left_f_par,right_f,right_f_pos)
		self.play(Write(pos_group))

		self.wait(2)

		self.play(ApplyMethod(left_f_x.set_color,GREEN))
		self.wait()
		self.play(ApplyMethod(right_f_pos.set_color,GREEN))
		self.wait(2)
		self.play(Transform(left_f_x,left_f_x_neg))
		self.wait()
		self.play(Transform(right_f_pos,right_f_neg))

		self.wait(2)

		center=Dot()
		center.set_color(YELLOW)

		self.play(ShowCreation(center))

		self.wait(2)

		tanfunc_graph=self.get_graph(self.tanfunc,x_min=0,x_max=2)

		#self.play(
			#self.camera_frame.scale,0.45,
			#self.camera_frame.move_to,RIGHT+UP,
			#FadeOut(center),
			#FadeOut(odd1_graph)
			#)

		self.play(
			FadeOut(odd1_graph),
			FadeOut(pospos),
			FadeOut(negneg),
			FadeOut(Point1),
			FadeOut(Point2),
			FadeOut(line),
			FadeOut(line2)
			)

		#labels
		pi=TextMobject("$$\\frac{\pi}{2}$$")
		tpi=TextMobject("$$\pi$$")
		thpi=TextMobject("$$\\frac{3\pi}{2}$$")
		fpi=TextMobject("$$2\pi$$")
		npi=TextMobject("$$-\\frac{\pi}{2}$$")
		ntpi=TextMobject("$$-\pi$$")
		nthpi=TextMobject("$$-\\frac{3\pi}{2}$$")
		nfpi=TextMobject("$$-2\pi$$")
		one=TextMobject("$$\\frac{1}{2}$$")
		two=TextMobject("$$1$$")
		none=TextMobject("$$-\\frac{1}{2}$$")
		ntwo=TextMobject("$$-1$$")

		#Move Labelspi
		pi.move_to(self.coords_to_point(2,0)+DOWN*0.5)
		tpi.move_to(self.coords_to_point(4,0)+DOWN*0.5)
		thpi.move_to(self.coords_to_point(6,0)+DOWN*0.5)
		fpi.move_to(self.coords_to_point(8,0)+DOWN*0.5)
		npi.move_to(self.coords_to_point(-2,0)+DOWN*0.5)
		ntpi.move_to(self.coords_to_point(-4,0)+DOWN*0.5)
		nthpi.move_to(self.coords_to_point(-6,0)+DOWN*0.5)
		nfpi.move_to(self.coords_to_point(-8,0)+DOWN*0.5)
		one.move_to(self.coords_to_point(0,2)+LEFT*0.25)
		two.move_to(self.coords_to_point(0,4)+LEFT*0.25)
		none.move_to(self.coords_to_point(0,-2)+LEFT*0.5)
		ntwo.move_to(self.coords_to_point(0,-4)+LEFT*0.5)

		#Scale labels
		pi.scale(0.7)
		tpi.scale(0.7)
		thpi.scale(0.7)
		fpi.scale(0.7)
		npi.scale(0.7)
		ntpi.scale(0.7)
		nthpi.scale(0.7)
		nfpi.scale(0.7)
		one.scale(0.7)
		two.scale(0.7)
		none.scale(0.7)
		ntwo.scale(0.7)

		#gather labels
		pilabels=VGroup(pi,tpi,thpi,npi,ntpi,nthpi,one,two,none,ntwo,fpi,nfpi)

		self.play(ShowCreation(pilabels))

		self.wait()

		self.play(ApplyMethod(center.move_to,self.coords_to_point(1,2)))

		self.play(ShowCreation(tanfunc_graph))

		self.wait(2)

		self.play(ApplyMethod(tanfunc_graph.move_to,self.coords_to_point(1,0)),
			ApplyMethod(center.move_to,self.coords_to_point(1,0)))

		self.wait()

		self.play(ApplyMethod(tanfunc_graph.move_to,self.coords_to_point(0,0)),
			ApplyMethod(center.move_to,self.coords_to_point(0,0)))

		self.wait(2)

		mainint=TextMobject("$$\\frac{1}{\\tan^{\sqrt{2020}}(x)+1}$$")
		mainint.move_to(RIGHT*3.6+UP*2)
		half=TextMobject("$$-\\frac{1}{2}$$")
		half.next_to(mainint,RIGHT,0.1)
		#half.set_color(BLUE)
		mainint_shift=TextMobject("$$\\frac{1}{\\tan^{\sqrt{2020}}(x+\\frac{\pi}{4})+1}$$")
		mainint_shift.next_to(half,LEFT,0.1)

		mainint.shift(DOWN*0.08)
		mainint_shift.shift(DOWN*0.08)

		half.shift(UP*0.04)

		self.play(ShowCreation(mainint))
		self.wait()
		self.play(ShowCreation(half))
		self.wait()
		self.play(Transform(mainint,mainint_shift))
		self.wait(4)




	def odd1(self,x):
		return np.power((x)/3,3)

	def odd2(self,x):
		return -np.power(x,3)+3*x

	def odd3(self,x):
		return np.sin(x)*np.power(x,2)

	def odd4(self,x):
		return 7*np.arctan((x)/3)*np.exp(-np.power((x)/3,2))

	def tanfunc(self,x):
		return 4/(np.power(np.tan((x/4)*PI),2)+1)

#python -m manim MITintegral\tanint\tanint.py NegXAttempt -pl
class NegXAttempt(Scene):
	def construct(self):
		mainint=TextMobject("$$\\frac{1}{\\tan^{\sqrt{2020}}(x+\\frac{\pi}{4})+1}-\\frac{1}{2}$$")
		#mainint_not=TextMobject("$$\\frac{1}{\Big(\\tan(x+\\frac{\pi}{4})\Big)^{n}+1}-\\frac{1}{2}$$")
		fofx=TextMobject("$$f(x)=$$")
		fofx.shift(UP*0.1)
		fofx.scale(0.8)
		mainint.scale(0.8)
		#mainint_not.scale(0.8)
		fofx.next_to(mainint,LEFT,0.1)

		total=VGroup(mainint,fofx)
		#total2=VGroup(mainint_not,fofx)
		#mainint.shift(RIGHT*0.4)
		total.move_to(np.array([0,0,0]))
		#total2.move_to(np.array([0,0,0]))

		#JUST ADDED
		mainint.shift(DOWN*0.08)

		self.play(Write(fofx))
		self.play(
			Write(mainint)
			)
		self.wait()
		#mainint_not.shift(RIGHT*0.5)
		#self.play(
		#	Transform(mainint,mainint_not),
		#	ApplyMethod(fofx.shift,LEFT*0.4+UP*0.2)
		#	)

		self.wait(4)

		fofx_wneg=TextMobject("$$f(-x)=$$")
		fofx_wneg.scale(0.8)
		fofx_wneg.move_to(fofx.get_center()+LEFT*0.15)
		mainint_not_neg=TextMobject("$$\\frac{1}{\\tan^{\sqrt{2020}}(-x+\\frac{\pi}{4})+1}-\\frac{1}{2}$$")
		mainint_not_neg.scale(0.8)
		mainint_not_neg.move_to(mainint.get_center()+RIGHT*0.2)

		self.play(Transform(fofx,fofx_wneg),Transform(mainint,mainint_not_neg))

		self.wait(2)

		everything=VGroup(
			mainint,
			#mainint_not,
			#mainint_not_neg,
			fofx,
			#fofx_wneg
			)

		self.play(ApplyMethod(everything.shift,LEFT*2.6))

		mainint_l=TextMobject("$$=-\Bigg(\\frac{1}{\\tan^{\sqrt{2020}}(x+\\frac{\pi}{4})+1}-\\frac{1}{2}\Bigg)$$")
		mainint_l.scale(0.8)
		mainint_l.next_to(mainint,RIGHT,0.15)

		#JUST ADDED
		mainint_l.shift(UP*0.08)
		
		#mainint_l.shift(UP*0.2)

		question_mark=TextMobject("?")
		question_mark.shift(RIGHT*0.8+UP*0.38)

		self.play(Write(mainint_l),Write(question_mark))

		self.wait(2)

		everything_fr=VGroup(
			mainint,
			mainint_not_neg,
			fofx,
			fofx_wneg,
			mainint_l
			)

		self.play(FadeOut(everything),FadeOut(mainint_l),FadeOut(question_mark))
		tangent_pos=TextMobject("$$\\tan(x+\\frac{\pi}{4})$$")
		tangent_neg=TextMobject("$$\\tan(-x+\\frac{\pi}{4})$$")

		self.play(Write(tangent_pos))
		self.wait()
		self.play(Transform(tangent_pos,tangent_neg))

		self.wait(4)

#python -m manim MITintegral\tanint\tanint.py UnitCircle2 -pl
class UnitCircle2(GraphScene):
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
	"x_labeled_nums" :range(-3,3,1),
	"y_labeled_nums" :range(-1,2,1),
	"num_graph_anchor_points": 200,

	} 
	def construct(self):
		angle=math.radians(360)
		arc=Arc(radius=2,angle=angle)

		x_value = ValueTracker(PI/3)

		#Positive arm
		arm=Arrow(np.array([0,0,0]),np.array([1,2*np.sqrt(3)/2,0]),buff=0)
		arm.set_color(GREEN)

		#Central arm
		arm_c=Arrow(np.array([0,0,0]),np.array([1,2*np.sqrt(3)/2,0]),buff=0)
		arm_c.set_color(BLUE)

		#Central arm negative
		arm_c_n=Arrow(np.array([0,0,0]),np.array([1,-2*np.sqrt(3)/2,0]),buff=0)
		arm_c_n.set_color(BLUE)

		#Negative arm
		arm_n=Arrow(np.array([0,0,0]),np.array([1,-2*np.sqrt(3)/2,0]),buff=0)
		arm_n.set_color(RED)

		#Reference Dot
		#REFDOT DECIDES WHERE THE TRACKERS ARE
		refd=Dot()
		refd.move_to(RIGHT*5+UP*3)
		refd2=Dot()
		refd2.next_to(refd,DOWN*1.6)

		#Tan Definition
		tan_func = lambda x: np.tan(x.get_value())
		tan_func_value = ValueTracker(tan_func(x_value))
		x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
		tan_func_tex = DecimalNumber(tan_func_value.get_value()).add_updater(lambda v: v.set_value(tan_func(x_value)))

		self.setup_axes(animate=True)

		self.play(ShowCreation(arc))

		#Tan display
		tan_func_tex.move_to(RIGHT*4.2+UP*2)
		tanlab=TextMobject("$$\\tan(\\theta):$$")
		tanlab.next_to(tan_func_tex,LEFT)
		yoverx=TextMobject("$$\\frac{y}{x}:$$")
		yoverx.next_to(tan_func_tex,LEFT)

		#Define Markers for angles
		zerodot=Dot()
		zerodot.move_to(np.array([2,0,0]))
		pifourdot=Dot()
		pifourdot.move_to(np.array([2*np.sqrt(2)/2,2*np.sqrt(2)/2,0]))
		pitwodot=Dot()
		pitwodot.move_to(np.array([0,2,0]))
		pithreefourdot=Dot()
		pithreefourdot.move_to(np.array([-2*np.sqrt(2)/2,2*np.sqrt(2)/2,0]))
		pidot=Dot()
		pidot.move_to(np.array([-2,0,0]))

		pifivefourdot=Dot()
		pifivefourdot.move_to(np.array([-2*np.sqrt(2)/2,-2*np.sqrt(2)/2,0]))
		pithreetwodot=Dot()
		pithreetwodot.move_to(np.array([0,-2,0]))
		pisevenfourdot=Dot()
		pisevenfourdot.move_to(np.array([2*np.sqrt(2)/2,-2*np.sqrt(2)/2,0]))

		#Define Labels for angles

		buff=0.5

		zerolab=TextMobject("$$0$$")
		zerolab.scale(0.65)
		zerolab.next_to(zerodot,RIGHT*buff+UP*buff)
		pifourlab=TextMobject("$$\\frac{\pi}{4}$$")
		pifourlab.scale(0.65)
		pifourlab.next_to(pifourdot,RIGHT*buff+UP*buff)
		pitwolab=TextMobject("$$\\frac{\pi}{2}$$")
		pitwolab.scale(0.65)
		pitwolab.next_to(pitwodot,RIGHT*buff+UP*buff)
		pithreefourlab=TextMobject("$$\\frac{3\pi}{4}$$")
		pithreefourlab.scale(0.65)
		pithreefourlab.next_to(pithreefourdot,LEFT*buff+UP*buff)
		pilab=TextMobject("$$\pi$$")
		pilab.scale(0.65)
		pilab.next_to(pidot,LEFT*buff+UP*buff)
		pifivefourlab=TextMobject("$$\\frac{5\pi}{4}$$")
		pifivefourlab.scale(0.65)
		pifivefourlab.next_to(pifivefourdot,LEFT*buff+DOWN*buff)
		pithreetwolab=TextMobject("$$\\frac{3\pi}{2}$$")
		pithreetwolab.scale(0.65)
		pithreetwolab.next_to(pithreetwodot,RIGHT*buff+DOWN*buff)
		pisevenfourlab=TextMobject("$$\\frac{7\pi}{4}$$")
		pisevenfourlab.scale(0.65)
		pisevenfourlab.next_to(pisevenfourdot,RIGHT*buff+DOWN*buff)



		allrads=VGroup(zerolab,pifourlab,pitwolab,pithreefourlab,pilab,pifivefourlab,pithreetwolab,pisevenfourlab)

		#self.play(ShowCreation(tip))
		#self.play(MoveAlongPath(tip,path1))

		pos_theta=TextMobject("$$+\\theta$$")
		neg_theta=TextMobject("$$-\\theta$$")
		pos_theta.set_color(BLUE)
		neg_theta.set_color(BLUE)

		pos_theta.move_to(RIGHT*3.5+UP*2.4)
		neg_theta.next_to(pos_theta,DOWN,0.6)

		plus_pi_green=TextMobject("$$+\\frac{\pi}{4}$$")
		plus_pi_green.set_color(GREEN)
		plus_pi_green.next_to(pos_theta,RIGHT,0.1)
		plus_pi_green.scale(0.8)
		plus_pi_red=TextMobject("$$+\\frac{\pi}{4}$$")
		plus_pi_red.set_color(RED)
		plus_pi_red.next_to(neg_theta,RIGHT,0.1)
		plus_pi_red.scale(0.8)


		self.wait()
		self.play(ShowCreation(arm),ShowCreation(arm_c),
			ShowCreation(arm_n),ShowCreation(arm_c_n),
			ShowCreation(pos_theta),
			ShowCreation(neg_theta)
			#ShowCreation(tan_func_tex)
			)
		self.wait()

		self.play(

			Write(allrads)

			)

		self.wait()

		self.play(

			ShowCreation(plus_pi_red),

			ShowCreation(plus_pi_green),

			Rotating(arm,radians=PI/4,about_point=np.array([0,0,0])),

			Rotating(arm_n,radians=PI/4,about_point=np.array([0,0,0])),

			run_time=1.4

			)

		self.wait(2)

		tan_of_pos=TextMobject("$$\\tan(\\theta+\\frac{\pi}{4})=$$")
		tan_of_neg=TextMobject("$$\\tan(-\\theta+\\frac{\pi}{4})=$$")

		tan_of_pos.scale(0.8)
		tan_of_neg.scale(0.8)

		tan_of_pos.move_to(LEFT*5+UP*2.7)
		tan_of_neg.next_to(tan_of_pos,DOWN,0.4)

		tan_of_pos.set_color(GREEN)
		tan_of_neg.set_color(RED)

		frac_bar1=Line(np.array([-0.3,0,0]),np.array([0.3,0,0]))
		frac_bar2=Line(np.array([-0.3,0,0]),np.array([0.3,0,0]))

		frac_bar1.next_to(tan_of_pos,RIGHT,0.1)
		frac_bar2.next_to(tan_of_neg,RIGHT,0.1)

		self.play(
			ShowCreation(tan_of_pos),
			ShowCreation(tan_of_neg),
			ShowCreation(frac_bar1),
			ShowCreation(frac_bar2)
			)

		self.wait(2)

		#######################################################
		#FIRST POSITION
		#Define braces for the green arrow at first position
		x_g_1=Brace(arm,DOWN)
		x_g_1_lab=TextMobject("$$\\mbox{-}x$$")
		x_g_1_lab.next_to(x_g_1,DOWN,0.1)
		y_g_1=Brace(arm,LEFT)
		y_g_1_lab=TextMobject("$$y$$")
		y_g_1_lab.next_to(y_g_1,LEFT,0.1)

		self.play(
			ShowCreation(x_g_1),
			ShowCreation(x_g_1_lab)
			)

		self.wait(2)

		self.play(
			ShowCreation(y_g_1),
			ShowCreation(y_g_1_lab)
			)

		self.wait(2)

		self.play(
			ApplyMethod(x_g_1_lab.move_to,frac_bar1.get_center()+DOWN*0.3),
			ApplyMethod(y_g_1_lab.move_to,frac_bar1.get_center()+UP*0.3)
			)

		self.wait(2)

		#Define braces for the red arrow at first position
		x_r_1=Brace(arm_n,RIGHT)
		x_r_1_lab=TextMobject("$$\\mbox{-}x$$")
		x_r_1_lab.next_to(x_r_1,RIGHT,0.1)
		y_r_1=Brace(arm_n,UP)
		y_r_1_lab=TextMobject("$$y$$")
		y_r_1_lab.next_to(y_r_1,UP,0.1)

		self.play(Transform(x_g_1,x_r_1),ShowCreation(x_r_1_lab))
		self.wait()
		self.play(Transform(y_g_1,y_r_1),ShowCreation(y_r_1_lab))

		self.wait(2)

		self.play(
			ApplyMethod(x_r_1_lab.move_to,frac_bar2.get_center()+UP*0.3)
			)

		self.wait()

		self.play(
			ApplyMethod(y_r_1_lab.move_to,frac_bar2.get_center()+DOWN*0.3)
			)

		self.wait(2)

		#Fadeout position one elements
		self.play(
			FadeOut(x_g_1),
			FadeOut(y_g_1),
			FadeOut(x_g_1_lab),
			FadeOut(y_g_1_lab),
			FadeOut(x_r_1_lab),
			FadeOut(y_r_1_lab)
			)

		self.wait()

		theta_by=math.radians(30)

		self.play(
			Rotating(arm,radians=-theta_by,about_point=np.array([0,0,0])),

			Rotating(arm_c,radians=-theta_by,about_point=np.array([0,0,0])),

			Rotating(arm_c_n,radians=theta_by,about_point=np.array([0,0,0])),

			Rotating(arm_n,radians=theta_by,about_point=np.array([0,0,0])),

			run_time=1.4

			)

		self.wait(2)
		##########################################################
		#Second position bracket and label elements

		#Define braces for the green arrow at second position
		x_g_1=Brace(arm,DOWN)
		x_g_1_lab=TextMobject("$$x$$")
		x_g_1_lab.next_to(x_g_1,DOWN,0.1)
		y_g_1=Brace(arm,LEFT)
		y_g_1_lab=TextMobject("$$y$$")
		y_g_1_lab.next_to(y_g_1,LEFT,0.1)

		#Add brackets pos two
		self.play(
			ShowCreation(x_g_1),
			ShowCreation(x_g_1_lab)
			)

		self.wait(2)

		self.play(
			ShowCreation(y_g_1),
			ShowCreation(y_g_1_lab)
			)

		self.wait(2)

		#Add labels pos two
		self.play(
			ApplyMethod(x_g_1_lab.move_to,frac_bar1.get_center()+DOWN*0.3),
			ApplyMethod(y_g_1_lab.move_to,frac_bar1.get_center()+UP*0.3)
			)

		self.wait(2)

		#Define elements and stuff for red arrow pos two
		x_r_1=Brace(arm_n,RIGHT)
		x_r_1_lab=TextMobject("$$x$$")
		x_r_1_lab.next_to(x_r_1,RIGHT,0.1)
		y_r_1=Brace(arm_n,DOWN)
		y_r_1_lab=TextMobject("$$y$$")
		y_r_1_lab.next_to(y_r_1,DOWN,0.1)

		self.play(Transform(x_g_1,x_r_1),ShowCreation(x_r_1_lab))
		self.wait()
		self.play(Transform(y_g_1,y_r_1),ShowCreation(y_r_1_lab))

		self.wait(2)

		self.play(
			ApplyMethod(x_r_1_lab.move_to,frac_bar2.get_center()+UP*0.3)
			)

		self.wait()

		self.play(
			ApplyMethod(y_r_1_lab.move_to,frac_bar2.get_center()+DOWN*0.3)
			)

		self.wait(2)


		#Fadeout position two elements
		self.play(
			FadeOut(x_g_1),
			FadeOut(y_g_1),
			FadeOut(x_g_1_lab),
			FadeOut(y_g_1_lab),
			FadeOut(x_r_1_lab),
			FadeOut(y_r_1_lab)
			)

		self.wait()

		theta_by=math.radians(-80)

		self.play(
			Rotating(arm,radians=-theta_by,about_point=np.array([0,0,0])),

			Rotating(arm_c,radians=-theta_by,about_point=np.array([0,0,0])),

			Rotating(arm_c_n,radians=theta_by,about_point=np.array([0,0,0])),

			Rotating(arm_n,radians=theta_by,about_point=np.array([0,0,0])),

			run_time=2

			)

		self.wait()

		##########################################################
		#THIRD position bracket and label elements

		#Define braces for the green arrow at third position
		x_g_1=Brace(arm,DOWN)
		x_g_1_lab=TextMobject("$$\\mbox{-}x$$")
		x_g_1_lab.next_to(x_g_1,DOWN,0.1)
		y_g_1=Brace(arm,LEFT)
		y_g_1_lab=TextMobject("$$y$$")
		y_g_1_lab.next_to(y_g_1,LEFT,0.1)

		#Add brackets pos 3
		self.play(
			ShowCreation(x_g_1),
			ShowCreation(x_g_1_lab)
			)

		self.wait(2)

		self.play(
			ShowCreation(y_g_1),
			ShowCreation(y_g_1_lab)
			)

		self.wait(2)

		#Add labels pos 3
		self.play(
			ApplyMethod(x_g_1_lab.move_to,frac_bar1.get_center()+DOWN*0.3),
			ApplyMethod(y_g_1_lab.move_to,frac_bar1.get_center()+UP*0.3)
			)

		self.wait(2)

		#Define elements and stuff for red arrow pos 3
		x_r_1=Brace(arm_n,RIGHT)
		x_r_1.shift(LEFT*0.15)
		x_r_1_lab=TextMobject("$$\\mbox{-}x$$")
		x_r_1_lab.next_to(x_r_1,RIGHT,0.1)
		y_r_1=Brace(arm_n,UP)
		y_r_1_lab=TextMobject("$$y$$")
		y_r_1_lab.next_to(y_r_1,UP,0.1)

		self.play(Transform(x_g_1,x_r_1),ShowCreation(x_r_1_lab))
		self.wait()
		self.play(Transform(y_g_1,y_r_1),ShowCreation(y_r_1_lab))

		self.wait(2)

		self.play(
			ApplyMethod(x_r_1_lab.move_to,frac_bar2.get_center()+UP*0.3)
			)

		self.wait()

		self.play(
			ApplyMethod(y_r_1_lab.move_to,frac_bar2.get_center()+DOWN*0.3)
			)

		self.wait(4)

#python -m manim MITintegral\tanint\tanint.py StatingProperty -pl
class StatingProperty(Scene):
	def construct(self):
		tan_prop=TextMobject("$$\\tan(-\\theta+\\frac{\pi}{4})=\\frac{1}{\\tan(\\theta+\\frac{\pi}{4})}$$")

		integrand=TextMobject("$$\\frac{1}{\\tan^{n}(x+\\frac{\pi}{4})+1}-\\frac{1}{2}$$")

		int_1_frac=TextMobject("$$\\frac{2}{2(\\tan^{n}(x+\\frac{\pi}{4})+1)}-\\frac{\\tan^{n}(x+\\frac{\pi}{4})+1}{2(\\tan^{n}(x+\\frac{\pi}{4})+1)}$$")

		int_1_frac_f=TextMobject("$$\\frac{1-\\tan^{n}(x+\\frac{\pi}{4})}{2(\\tan^{n}(x+\\frac{\pi}{4})+1)}$$")

		self.play(Write(tan_prop))

		self.wait(2)

		self.play(FadeOut(tan_prop))

		self.play(Write(integrand))

		self.wait(2)

		self.play(Transform(integrand,int_1_frac))

		self.wait(2)

		self.wait()

		self.play(Transform(integrand,int_1_frac_f))

		self.wait(2)

		self.play(ApplyMethod(integrand.shift,LEFT*3.5+UP*2.3))

		self.wait()

		neg_inp=TextMobject("$$\\frac{1-\\tan^{n}(-x+\\frac{\pi}{4})}{2(\\tan^{n}(-x+\\frac{\pi}{4})+1)}$$")

		self.play(Write(neg_inp))

		self.wait(2)

		neg_inp_num=TextMobject("$$\\frac{1-\\frac{1}{\\tan^{n}(x+\\frac{\pi}{4})}} {2(\\tan^{n}(-x+\\frac{\pi}{4})+1)}$$")

		self.play(Transform(neg_inp,neg_inp_num))

		self.wait(2)

		neg_inp_den=TextMobject("$$\\frac{1-\\frac{1}{\\tan^{n}(x+\\frac{\pi}{4})}} {2(\\frac{1}{\\tan^{n}(x+\\frac{\pi}{4})}+1)}$$")

		self.play(Transform(neg_inp,neg_inp_den))

		self.wait(3)

		neg_inp_num_2=TextMobject("$$\\frac{\\frac{\\tan^{n}(x+\\frac{\pi}{4})}{\\tan^{n}(x+\\frac{\pi}{4})}-\\frac{1}{\\tan^{n}(x+\\frac{\pi}{4})}} {2(\\frac{1}{\\tan^{n}(x+\\frac{\pi}{4})}+1)}$$")

		self.play(Transform(neg_inp,neg_inp_num_2))

		neg_inp_den_2=TextMobject("$$\\frac{\\frac{\\tan^{n}(x+\\frac{\pi}{4})}{\\tan^{n}(x+\\frac{\pi}{4})}-\\frac{1}{\\tan^{n}(x+\\frac{\pi}{4})}} {2(\\frac{1}{\\tan^{n}(x+\\frac{\pi}{4})}+\\frac{\\tan^{n}(x+\\frac{\pi}{4})}{\\tan^{n}(x+\\frac{\pi}{4})})}$$")

		self.wait(2)

		self.play(Transform(neg_inp,neg_inp_den_2))

		self.wait(2)

		neg_inp_comb=TextMobject("$$\\frac{\\frac{\\tan^{n}(x+\\frac{\pi}{4})-1}{\\tan^{n}(x+\\frac{\pi}{4})}}{2(\\frac{1+\\tan^{n}(x+\\frac{\pi}{4})}{\\tan^{n}(x+\\frac{\pi}{4})})}$$")

		self.play(Transform(neg_inp,neg_inp_comb))

		self.wait(2)

		recip=TextMobject("$$\\frac{\\tan^{n}(x+\\frac{\pi}{4})-1}{\\tan^{n}(x+\\frac{\pi}{4})}\cdot\\frac{\\tan^{n}(x+\\frac{\pi}{4})}{2(1+\\tan^{n}(x+\\frac{\pi}{4}))}$$")

		self.play(Transform(neg_inp,recip))

		self.wait(2)

		cancel1=Line(np.array([-1.3,0,0]),np.array([1.3,0,0]))
		cancel2=Line(np.array([-1.3,0,0]),np.array([1.3,0,0]))
		cancel1.set_color(RED)
		cancel2.set_color(RED)

		cancel1.move_to(RIGHT*1.95+UP*0.38)
		cancel2.move_to(LEFT*2.32+DOWN*0.35)

		self.play(ShowCreation(cancel2),ShowCreation(cancel1))

		final_frac=TextMobject("$$\\frac{\\tan^{n}(x+\\frac{\pi}{4})-1}{2(\\tan^{n}(x+\\frac{\pi}{4})+1)}$$")

		self.wait(2)
		self.play(FadeOut(cancel1),FadeOut(cancel2),run_time=0.5)
		self.play(Transform(neg_inp,final_frac))

		self.wait(2)

		swap=TextMobject("$$\\frac{-(1-\\tan^{n}(x+\\frac{\pi}{4}))}{2(\\tan^{n}(x+\\frac{\pi}{4})+1)}$$")

		self.play(Transform(neg_inp,swap))

		self.wait(2)

		times_neg=TextMobject("$$\\times -1=$$")

		self.play(
			ApplyMethod(neg_inp.shift,RIGHT*3.3),
			ApplyMethod(integrand.move_to,neg_inp.get_center()+LEFT*3.3),
			ShowCreation(times_neg)
			)

		self.wait(4)


#python -m manim MITintegral\tanint\tanint.py Recap -pl
class Recap(GraphScene,MovingCameraScene):
	CONFIG = {
	"x_min" : -9,
	"x_max" : 9,
	"y_min" : -6,
	"y_max" : 6,
	"x_tick_frequency": 1,
	"y_tick_frequency": 2,
	"y_axis_height":8,
	"x_axis_width":12,
	"graph_origin" : ORIGIN,
	"function_color" : RED ,
	"axes_color" : WHITE,
	#"x_labeled_nums" :range(-9,9,3),
	#"y_labeled_nums" :range(-6,6,2),
	"num_graph_anchor_points": 200,
	"always_update_mobjects": True,
    "always_continually_update": True,

	}

	def setup(self):
		GraphScene.setup(self)
		MovingCameraScene.setup(self)

	def construct(self):

		self.setup_axes(animate=True)

		#labels
		pi=TextMobject("$$\\frac{\pi}{2}$$")
		tpi=TextMobject("$$\pi$$")
		thpi=TextMobject("$$\\frac{3\pi}{2}$$")
		fpi=TextMobject("$$2\pi$$")
		npi=TextMobject("$$-\\frac{\pi}{2}$$")
		ntpi=TextMobject("$$-\pi$$")
		nthpi=TextMobject("$$-\\frac{3\pi}{2}$$")
		nfpi=TextMobject("$$-2\pi$$")
		one=TextMobject("$$\\frac{1}{2}$$")
		two=TextMobject("$$1$$")
		none=TextMobject("$$-\\frac{1}{2}$$")
		ntwo=TextMobject("$$-1$$")

		#Move Labelspi
		pi.move_to(self.coords_to_point(2,0)+DOWN*0.5)
		tpi.move_to(self.coords_to_point(4,0)+DOWN*0.5)
		thpi.move_to(self.coords_to_point(6,0)+DOWN*0.5)
		fpi.move_to(self.coords_to_point(8,0)+DOWN*0.5)
		npi.move_to(self.coords_to_point(-2,0)+DOWN*0.5)
		ntpi.move_to(self.coords_to_point(-4,0)+DOWN*0.5)
		nthpi.move_to(self.coords_to_point(-6,0)+DOWN*0.5)
		nfpi.move_to(self.coords_to_point(-8,0)+DOWN*0.5)
		one.move_to(self.coords_to_point(0,2)+LEFT*0.25)
		two.move_to(self.coords_to_point(0,4)+LEFT*0.25)
		none.move_to(self.coords_to_point(0,-2)+LEFT*0.5)
		ntwo.move_to(self.coords_to_point(0,-4)+LEFT*0.5)

		#Scale labels
		pi.scale(0.7)
		tpi.scale(0.7)
		thpi.scale(0.7)
		fpi.scale(0.7)
		npi.scale(0.7)
		ntpi.scale(0.7)
		nthpi.scale(0.7)
		nfpi.scale(0.7)
		one.scale(0.7)
		two.scale(0.7)
		none.scale(0.7)
		ntwo.scale(0.7)

		#gather labels
		pilabels=VGroup(pi,tpi,thpi,npi,ntpi,nthpi,one,two,none,ntwo,fpi,nfpi)

		self.play(ShowCreation(pilabels),run_time=1)

		tanfunc_graph=self.get_graph(self.tanfunc,x_min=0,x_max=2)
		top_graph=self.get_graph(self.top,x_min=0,x_max=2)
		block_graph=self.get_graph(self.block,x_min=0,x_max=2)

		tanfunc_graph.move_to(np.array([0,0,0]))

		integrand=TextMobject("$$\\frac{1}{\\tan^{n}(x+\\frac{\pi}{4})+1}-\\frac{1}{2}$$")
		integrand_nsh=TextMobject("$$\\frac{1}{\\tan^{n}(x)+1}$$")

		integrand.move_to(LEFT*3.4+UP*2)
		integrand.scale(0.8)

		integrand_nsh.move_to(integrand.get_center())
		integrand_nsh.scale(0.8)

		self.play(ShowCreation(tanfunc_graph),Write(integrand))

		self.wait(3)

		self.play(ApplyMethod(tanfunc_graph.move_to,self.coords_to_point(1,0)),run_time=0.7)
		self.play(ApplyMethod(tanfunc_graph.move_to,self.coords_to_point(1,2)),
			Transform(integrand,integrand_nsh),run_time=0.7)

		self.wait()

		tan_area=self.get_area(tanfunc_graph,1,2)
		top_area=self.get_area(top_graph,0,1)
		top_area.shift(self.coords_to_point(0,2))
		block_area=self.get_area(block_graph,0,1)

		self.play(
			ShowCreation(block_area),
			ShowCreation(top_area),
			ShowCreation(tan_area)
			)

		self.wait(2)

		self.play(
			Rotating(top_area,radians=-PI,about_point=self.coords_to_point(1,2)),
			rate_func=linear,run_time=1.5
			)

		self.wait(2)

		aarea=TextMobject("$$A=$$")
		aarea.shift(RIGHT*3.1+UP*2.2)
		self.play(Write(aarea))
		self.wait()


		half=Brace(top_area,RIGHT)
		area=VGroup(block_area,tan_area)
		pitwo=Brace(area,DOWN)

		pitwolab=TextMobject("$$\\frac{\pi}{2}$$")
		pitwolab.next_to(aarea,RIGHT,0.1)

		halflab=TextMobject("$$\cdot\\frac{1}{2}$$")
		halflab.next_to(pitwolab,RIGHT,0.2)
		halflab.shift(UP*0.02)

		pioverfour=TextMobject("$$\\frac{\pi}{4}$$")
		pioverfour.next_to(aarea,RIGHT,0.25)

		self.play(ShowCreation(pitwo),Write(pitwolab))
		self.wait()
		self.play(ShowCreation(half),Write(halflab))

		prod=VGroup(halflab,pitwolab)

		self.wait()
		self.play(Transform(prod,pioverfour))

		self.wait(4)


	def tanfunc(self,x):
		return 4/(np.power(np.tan((x/4)*PI),2)+1)

	def top(self,x):
		return 4/(np.power(np.tan((x/4)*PI),2)+1)-2

	def block(self,x):
		return 2

#python -m manim MITintegral\tanint\tanint.py Finale -pl
class Finale(Scene):
	def construct(self):
		mainint=TextMobject("$$\int_{0}^{\\frac{\pi}{2}}\\frac{1}{\\tan^{\sqrt{2020}}(x)+1} dx$$")
		equals=TextMobject("$$=\\frac{\pi}{4}$$")
		equals.next_to(mainint,RIGHT,0.2)
		whole=VGroup(mainint,equals)
		whole.move_to(np.array([0,0,0]))

		self.play(Write(whole))

		self.wait(3)

		self.play(FadeOut(equals),ApplyMethod(mainint.move_to,ORIGIN))

		mainint_t=TextMobject("$$\int_{0}^{\\frac{\pi}{2}}\\frac{1}{\\tan^{t}(x)+1} dx$$")

		self.wait()

		self.play(Transform(mainint,mainint_t))

		self.wait(2)

		ddt=TextMobject("$$\\frac{\mathrm{d} }{\mathrm{d} t}$$")
		ddt.next_to(mainint,LEFT,0.23)



		self.play(ShowCreation(ddt))

		
		mainint_part=TextMobject("$$\int_{0}^{\\frac{\pi}{2}}\\frac{\partial}{\partial t}\\frac{1}{\\tan^{t}(x)+1} dx$$")
		
		zero=TextMobject("$$=0$$")
		zero.next_to(mainint,RIGHT,0.2)

		self.play(ShowCreation(zero))
		
		self.wait(2)

		group=VGroup(mainint,ddt)

		self.play(Transform(group,mainint_part),ApplyMethod(zero.shift,RIGHT*0.4))

		group2=VGroup(mainint,zero)

		self.wait(2)

		self.play(FadeOut(group2))

		final_solve_1=TextMobject("$$\int_{0}^{\\frac{\pi}{2}}\\frac{1}{\\tan^{t}(x)+1} dx$$")
		final_solve_2=TextMobject("$$\int_{0}^{\\frac{\pi}{2}}\\frac{1}{\\tan^{\pi}(x)+1} dx$$")
		final_solve_3=TextMobject("$$\int_{0}^{\\frac{\pi}{2}}\\frac{1}{\\tan^{e}(x)+1} dx$$")
		final_solve_4=TextMobject("$$\int_{0}^{\\frac{\pi}{2}}\\frac{1}{\\tan^{2}(x)+1} dx$$")

		final_solve_sec=TextMobject("$$\int_{0}^{\\frac{\pi}{2}}\\frac{1}{\\sec^{2}(x)} dx$$")

		final_solve_cos=TextMobject("$$\int_{0}^{\\frac{\pi}{2}} \\cos^{2}(x) dx$$")

		self.wait()

		self.play(Write(final_solve_1))
		self.wait()
		self.play(Transform(final_solve_1,final_solve_2))
		self.wait()
		self.play(Transform(final_solve_1,final_solve_3))

		self.wait(2)

		self.play(Transform(final_solve_1,final_solve_4))

		self.wait(2)

		self.play(Transform(final_solve_1,final_solve_sec))

		self.wait(2)

		self.play(Transform(final_solve_1,final_solve_cos))

		self.wait(4)

class Test(Scene):
	def construct(self):
		p=TextMobject("-")
		q=TextMobject("$$\\mbox{-}x$$")
		p.next_to(q,LEFT,0.1)

		self.play(ShowCreation(p),ShowCreation(q))

		self.wait(4)


#python -m manim MITintegral\tanint\tanint.py Thumbnail -ps
class Thumbnail(GraphScene,MovingCameraScene):
	CONFIG = {
	"x_min" : -9,
	"x_max" : 9,
	"y_min" : -6,
	"y_max" : 6,
	"x_tick_frequency": 1,
	"y_tick_frequency": 2,
	"y_axis_height":8,
	"x_axis_width":12,
	"graph_origin" : ORIGIN,
	"function_color" : RED ,
	"axes_color" : WHITE,
	#"x_labeled_nums" :range(-9,9,3),
	#"y_labeled_nums" :range(-6,6,2),
	"num_graph_anchor_points": 200,
	"always_update_mobjects": True,
    "always_continually_update": True,

	} 

	def setup(self):
		GraphScene.setup(self)
		MovingCameraScene.setup(self)

	def construct(self):
		

		self.setup_axes(animate=False)


		odd4_graph=self.get_graph(self.odd4,x_min=-9,x_max=9,fill_opacity=0.3,stroke_opacity=0.5,stroke_color=WHITE)

		self.add(odd4_graph)
		#DASHED LINE STUFF

		#Origins of the dotted line (right and left respectively)
		Origin=self.coords_to_point(2,0)
		Origin2=self.coords_to_point(-2,0)

		#Create the dots
		Point1=Dot(color=RED)
		Point2=Dot(color=RED)

		#Create the dots at the ORIGIN and move them to the origins of the dotted lines
		

		Point1.move_to(self.coords_to_point(2,7*np.arctan((2)/3)*np.exp(-np.power((2)/3,2))))
		Point2.move_to(self.coords_to_point(-2,7*np.arctan((-2)/3)*np.exp(-np.power((-2)/3,2))))

		#Define lines that go from the origins of the lines to the dots
		line=DashedLine(Origin,Point1)
		line2=DashedLine(Origin2,Point2)

		#Define functions that re-define the line as new_line
		

		#Add in the lines
		self.add(line,line2,Point1,Point2)

		rad_twtw=TextMobject("$$\sqrt{2020}$$",set_color=BLUE,fill_color=BLUE,fill_opacity=0.7,stroke_color=WHITE,stroke_width=6)



		rad_twtw.scale(9)

		rad_twtw.shift(LEFT*1)

		self.add(rad_twtw)

	def odd4(self,x):
		return 12*np.arctan((x)/5)*np.exp(-np.power((x)/5,2))