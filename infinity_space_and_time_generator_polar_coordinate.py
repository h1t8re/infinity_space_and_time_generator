#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Chems eddine h1t8re 6.2.1996 After Jesus Christ'e

import math as math
import cmath as cmath
import numpy as numpy
import sympy as sympy
from mpmath import mp
import operator as operator

def infinity_space_generator(x, y, z):
	for Phi in range(0, 360):
		for Teta in range(0, 360):
			X = x*math.cos(math.radians(Phi))*math.sin(math.radians(Teta))
			Y = y*math.sin(math.radians(Phi))*math.sin(math.radians(Teta))
			Z = z*math.cos(Phi)
			r    = math.sqrt(math.pow(X, 2)+math.pow(Y, 2)+math.pow(Z, 2))
			Teta = math.atan2(y, x)
			Phi  = acos(z/r)
			yield ((X, Y, Z), (r, Teta, Phi))
			for ((x0, y0, z0), (R0, Teta0, Phi0)) in infinity_space_generator(X+1, Y, Z):
				yield ((x0, y0, z0), (R0, Teta0, Phi0))
			for ((x1, y1, z1), (R1, Teta1, Phi1)) in infinity_space_generator(X, Y+1, Z):
				yield ((x1, y1, z1), (R1, Teta1, Phi1))
			for ((x2, y2, z2), (R2, Teta2, Phi2)) in infinity_space_generator(X, Y, Z+1):
				yield ((x2, y2, z2), (R2, Teta2, Phi2))
			for ((x3, y3, z3), (R3, Teta3, Phi3)) in infinity_space_generator(X, Y, Z-1):
				yield ((x3, y3, z3), (R3, Teta3, Phi3))
			for ((x4, y4, z4), (R4, Teta4, Phi4)) in infinity_space_generator(X, Y-1, Z):
				yield ((x4, y4, z4), (R4, Teta4, Phi4))
			for ((x5, y5, z5), (R5, Teta5, Phi5)) in infinity_space_generator(X-1, Y, Z):
				yield ((x5, y5, z5), (R5, Teta5, Phi5))

def infinity_space_and_time_generator():
	t = 0
	while True:
		t = t +1
		for ((x, y, z), (R, Teta, Phi)) in infinity_space_generator(t, t, t):
			yield ((x, y, z), (R, Teta, Phi))

if __name__ == "__main__":
	main()
