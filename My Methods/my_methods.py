from manimlib.constants import *
from manimlib.imports import *
from manimlib.mobject.svg.tex_mobject import SingleStringTexMobject
from manimlib.mobject.types.vectorized_mobject import VMobject

#This class is my "personal methods", hence the name "pers"
#acces by using pers."method"
class pers(Scene):

	#This method was an early test,it paints and prints a passed mobject
	def print_col(self,x):
		x.set_color(BLUE)
		self.play(ShowCreation(x))

	#this method is passed two mobjects. it arranges them as if they were exponents
	#NOTE: textmobjects must be of equal size when passed
	def sep_exp(base,exp):
		exp.scale(0.75)
		exp.move_to(base.get_center()+UP*0.67*exp.get_height())
		exp.align_to(base,RIGHT)
		buff=0.1
		exp.shift(RIGHT*(exp.get_width()+buff*exp.get_width()))
		return exp

	#Takes between 3 and 6 colors and makes nicely spaced dots of them
	#returns the group of dots
	#make sure the colors passed ar either "r","g", or "b"
	def construct_dots(a,b,c,d,e,f):

		scale=4

		if a=="r":
			an=Dot(color=RED)
		if a=="g":
			an=Dot(color=GREEN)
		if a=="b":
			an=Dot(color=BLUE)

		if b=="r":
			bn=Dot(color=RED)
		if b=="g":
			bn=Dot(color=GREEN)
		if b=="b":
			bn=Dot(color=BLUE)

		if c=="r":
			cn=Dot(color=RED)
		if c=="g":
			cn=Dot(color=GREEN)
		if c=="b":
			cn=Dot(color=BLUE)

		if d=="r":
			dn=Dot(color=RED)
		if d=="g":
			dn=Dot(color=GREEN)
		if d=="b":
			dn=Dot(color=BLUE)
		if d==0:
			dn=0

		if e=="r":
			en=Dot(color=RED)
		if e=="g":
			en=Dot(color=GREEN)
		if e=="b":
			en=Dot(color=BLUE)
		if e==0:
			en=0

		if f=="r":
			fn=Dot(color=RED)
		if f=="g":
			fn=Dot(color=GREEN)
		if f=="b":
			fn=Dot(color=BLUE)
		if f==0:
			fn=0

		an.scale(scale)
		bn.scale(scale)
		cn.scale(scale)
		if dn!=0:
			dn.scale(scale)
		if en!=0:
			en.scale(scale)
		if fn!=0:
			fn.scale(scale)

		an.next_to(bn,LEFT,1)
		cn.next_to(bn,RIGHT,1)
		if dn!=0:
			dn.next_to(cn,RIGHT,1)
		if en!=0:
			en.next_to(dn,RIGHT,1)
		if fn!=0:
			fn.next_to(en,RIGHT,1)

		if fn!=0:
			dots=VGroup(an,bn,cn,dn,en,fn)
		if fn==0 and en!=0:
			dots=VGroup(an,bn,cn,dn,en)
		if en==0 and dn!=0:
			dots=VGroup(an,bn,cn,dn)
		if dn==0:
			dots=VGroup(an,bn,cn)

		dots.move_to(ORIGIN)

		return dots

	#Makes an arrow between the centers of x and y (color included)
	def arrow_maker(x,y,color):
		group=VGroup(x,y)
		arrow=TextMobject("$$\\rightarrow$$")
		arrow.scale(2)
		arrow.set_color(color)
		arrow.move_to(group.get_center())
		return arrow

	#Gets modulus of an array
	def abs(arr):
		length=len(arr)
		n=0
		tot=0

		x=1
		while True:
			tot+=np.power(arr[n],2)
			n+=1
			if n>=length:
				break
		return np.sqrt(tot)