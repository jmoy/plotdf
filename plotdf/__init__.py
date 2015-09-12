# (c) Jyotirmoy Bhattacharya [jyotirmoy@jyotirmoy.net
# Licensed under GPLv3
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
#AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
Plot phase portraits of 2D differential equations.

Example:
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
"""


import numpy as np
import scipy.integrate as scint
import matplotlib.pyplot as plt

def plotdf(f,
           xbound,ybound,
           inits=None,tbounds=[0,10],tsteps=100,
           gridsteps=10,
           parameters = dict(),
           axes = None):
  """
  Plot a direction field and optional trajectories of a planar differential
  equation system.

  Arguments
  -----

  f: A function of of the form f(x) where 'x' is a 2-element numpy
     array denoting the current state, 't' is the current time and
     we expect 'f' to return the rhs of the differential equation system.

  xbound: a two-element sequence giving the minimum and maximum values of 
     'x' to plot.

  ybound: a two-element sequence giving the minimum and maximum values of 
     'y' to plots.

  inits: if not None, gives the set of initial values to plot trajectories from.
  
  tbounds: the starting and ending time for trajectories

  nsteps: number of steps in trajectories

  gridsteps: number of steps in the x-y grid

  parameters: additional keyword arguments for 'f'

  axes: the matplot axes in which to draw the plot. If not provided
        use the current axes.

  Return Value
  ------
  A list the first element of which is the matplotlib Quiver object
  representing the arrows of the direction field and the rest are the 
  Lines2D objects representing the trajectories.
  """
  if axes is None:
    axes = plt.gca()

  x = np.linspace(xbound[0],xbound[1],gridsteps)
  y = np.linspace(ybound[0],ybound[1],gridsteps)
  xx,yy = np.meshgrid(x,y)
  uu = np.empty_like(xx)
  vv = np.empty_like(yy)
  for i in range(gridsteps):
    for j in range(gridsteps):
      res = f(np.array([xx[i,j],yy[i,j]]),**parameters)
      uu[i,j] = res[0]
      vv[i,j] = res[1]

  artists = []
  artists.append(axes.quiver(xx,yy,uu,vv,color="darkred",width=0.002))

  if inits is not None:
    def g(x,t):
      return f(x,**parameters)
    t = np.linspace(tbounds[0],tbounds[1],tsteps)
    for y0 in inits:
      traj = scint.odeint(g,y0,t)
      artists.extend(axes.plot(traj[:,0],traj[:,1],linewidth=1.2))
  plt.xlim(xbound)
  plt.ylim(ybound)
  return artists

  
