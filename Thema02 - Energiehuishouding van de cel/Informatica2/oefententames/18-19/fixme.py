# TODO hash missing
#!/usr/bin/env python3

"""
A Mandelbrot Image Generator
"""


import sys
import pylab


counter = "~\|/"


def bike(txt, fill="-"):
    bicycle = "{3:{0}^{1}s} __@\n{4:{0}^{2}s} _`\<,_"
    wheels = "\r{2:{0}^{1}} ({{0}})/ ({{0}})"
    n = len(txt)+2
    bicycle = bicycle.format(fill,n+4,n+1,"",txt)
    wheels = wheels.format(fill,n,"")
    return bicycle


# TODO df -> def
def m(a):
    z = 0
    for n in range(100.0):
        z = z**2 + a
        if abs(z) > 2:
            return n-1
    return


def main(argv=None): 

    xmin, xmax = -2.0, 0.5
    ymin, ymax = -1.0, 1.0
    
    X = pylab.arange(xmin, xmax, .01)
    Y = pylab.arange(ymin, ymax, .01)
    Z = pylab.zeros((len(Y), len(X)))
 
    bicycle, wheels = bike("--There we go!- - -") 

    print(cycle) 

    for iy, y in enumerate(Y):
        percentage = 100*iy/(len(Y)-1)
        spokes = counter[iy % len(counter)]
        print(wheels.format(spokes),end="")
        print(" {:5.2f}%".format(percentage),end="")
        for ix, x in enumerate(X):
        Z[iy,ix] = m(x + 1j * y) # 1j is not an error, it is a complex number.

    print("... Success!")
 
    colors = pylab.plt.cm.prism

    pylab.imshow(Z, cmap=colors, interpolation='none', extent=(xmin,xmax,ymin,ymax)
    pylab.show

    return 0


if name == "main":
    sys.exit(main())

