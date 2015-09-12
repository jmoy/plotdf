Plot phase portraits of 2D differential equations using
Python's `matplotlib` and `scipy` libraries.

Inspired by Maxima's `plotdf` function.

## Usage

To plot `dx/dt = y`, `dy/dt = -g sin(x) / l - b y/ (m l)`:

````
  from math import sin
  from plotdf import plotdf
  
  def f(x,g=1,l=1,m=1,b=1):
    return np.array([x[1],-g*sin(x[0])/l-b*x[1]/m/l])

  plotdf(f, # Function giving the rhs of the diff. eq. system
         np.array([-10,2]), # [xmin,xmax]
         np.array([-14,14]),# [ymin,ymax]
         [(1.05,-9),(0,5)], # list of initial values for trajectories (optional)
         # Additional parameters for `f` (optional)
         parameters={"g":9.8,"l":0.5,"m":0.3,"b":0.05})
````

For the full list of parameters to `plotdf`, see `help(plotdf.plotdf)`.

## Dependencies

Both Python 2 and 3 are supported. You need `matplotlib`,
`numpy` and `scipy` installed.

## Installation

The package is on PyPI so you can install it with

    $ pip install plotdf
