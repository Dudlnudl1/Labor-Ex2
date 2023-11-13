import uncertainties as u
import numpy as np


breite1 = u.ufloat(3.97 , 0.01)
breite2 =u.ufloat(3.97 , 0.01)
breite3 =u.ufloat(3.97 , 0.01)
breite4 =u.ufloat(3.96 , 0.01)
breite5 =u.ufloat(3.96 , 0.01)
hoehe1 =u.ufloat(3.97 , 0.01)
hoehe2 =u.ufloat(3.97 , 0.01)
hoehe3 =u.ufloat(3.96, 0.01)
hoehe4 =u.ufloat(3.96 , 0.01)
hoehe5 =u.ufloat(3.96 , 0.01)

height=(hoehe1+hoehe2+hoehe3+hoehe4+hoehe5)/5
print(height)
width=(breite5+breite4+breite3+breite2+breite1)/5
print(width)

Abreite1 = u.ufloat(2.10 , 0.01)
Abreite2 =u.ufloat(2.80 , 0.01)
Abreite3 =u.ufloat(2.80 , 0.01)
Abreite4 =u.ufloat(2.80 , 0.01)
Abreite5 =u.ufloat(2.80 , 0.01)
Ahoehe1 =u.ufloat(9.93 , 0.01)
Ahoehe2 =u.ufloat(9.93 , 0.01)
Ahoehe3 =u.ufloat(9.93, 0.01)
Ahoehe4 =u.ufloat(9.94 , 0.01)
Ahoehe5 =u.ufloat(9.96 , 0.01)

Aheight = (Ahoehe5+Ahoehe4+Ahoehe3+Ahoehe2+Ahoehe1)/5
Awidth = (Abreite5+Abreite4+Abreite3+Abreite2+Abreite1)/5
print(Aheight)
print(Awidth)

durchmesser1 = u.ufloat(5.98 , 0.01)
durchmesser2 =u.ufloat(5.98 , 0.01)
durchmesser3 =u.ufloat(5.98 , 0.01)
durchmesser4 =u.ufloat(5.98 , 0.01)
durchmesser5 =u.ufloat(5.98 , 0.01)
durchmesser6 =u.ufloat(5.98 , 0.01)
durchmesser7 =u.ufloat(5.98 , 0.01)
durchmesser8 =u.ufloat(5.98, 0.01)
durchmesser9 =u.ufloat(5.97 , 0.01)
durchmesser10 =u.ufloat(5.97 , 0.01)

durchmesser = (durchmesser1+durchmesser2+durchmesser3+durchmesser4+durchmesser5+durchmesser6+durchmesser7+durchmesser8+durchmesser9+durchmesser10)/10
print(durchmesser)

traegheitStahl = (np.pi*(durchmesser**4))/64
print(traegheitStahl)

traegheitAlu = (Aheight*(Awidth**3))/12
print(traegheitAlu)

traegheitMessing = (width*(height**3))/12
print(traegheitMessing)

L = u.ufloat(500, 1)
kStahl = u.ufloat(0.00280, 0.00014)
kAlu = u.ufloat(0.050, 0.004)
kMessing = u.ufloat(0.01539, 0.00016)
g = 9.81
EStahl = (g*(L**3))/(48*kStahl*traegheitStahl)
print(EStahl)
EMessing = (g*(L**3))/(48*kMessing*traegheitMessing)
print(EMessing)
EAlu = (g*(L**3))/(48*kAlu*traegheitAlu)
print(EAlu)

mStahl = u.ufloat(420.8, 2)
mMessing = u.ufloat(420.8, 2)
mAlu = u.ufloat(105.2, 2)

sigmaSthal = (mStahl*g*L/2*durchmesser/2)/(4*traegheitStahl)
print(sigmaSthal)
sigmaMessing = (mMessing*g*L/2*height/2)/(4*traegheitMessing)
print(sigmaMessing)
sigmaAlu = (mAlu*g*L/2*Aheight/2)/(4*traegheitAlu)
print(sigmaAlu)