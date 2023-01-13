import numpy as np
from scipy import optimize
f = lambda x: np.cos(x) - x
r = optimize.fsolve(f, -2)
print("r =",r)
# Verify the solution is a root
result = f(r)
print("result=", result)
     
import numpy as np #panggil library
def my_bisection(f, a, b, e):
  if np.sign(f(a)) == np.sign(f(b)):
    raise Exception('Tidak ada akar pada interval a dan b')
  m = (a + b)/2
  if np.abs(f(m)) < e:
    return m
  elif np.sign(f(a)) == np.sign(f(m)):
    return my_bisection(f, m, b, e)
  elif np.sign(f(b)) == np.sign(f(m)):
    return my_bisection(f, a, m, e)
     
import numpy as np #panggil library
f = lambda x: x**2-2

r1 = my_bisection(f, 0, 2, 0.1)
print("r1 =", r1)
print("f(r1) =", f(r1))

r01 = my_bisection(f, 0, 2, 0.01)
print("r01 =", r01)
print("f(r01) =", f(r01))

import numpy as np #panggil library
f = lambda x: x**2-2
my_bisection(f, 2, 4, 0.01)
     
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
<ipython-input-13-9db7d48a44ca> in <module>
      1 import numpy as np #panggil library
      2 f = lambda x: x**2-2
----> 3 my_bisection(f, 2, 4, 0.01)

<ipython-input-11-232ee789a6b2> in my_bisection(f, a, b, e)
      2 def my_bisection(f, a, b, e):
      3   if np.sign(f(a)) == np.sign(f(b)):
----> 4     raise Exception('Tidak ada akar pada interval a dan b')
      5   m = (a + b)/2
      6   if np.abs(f(m)) < e:

Exception: Tidak ada akar pada interval a dan b

import numpy as np #panggil library
def my_newton(f, df, x0, e):
# output is an estimation of the root of f
# using the Newton-Raphson method
# recursive implementation
  if abs(f(x0)) < e:
    return x0
  else:
    return my_newton(f, df, x0 - f(x0)/df(x0), e)
     
f = lambda x: x**2-2
f_prime = lambda x: 2*x
estimate = my_newton(f, f_prime, 1.5, 1e-6)
print("estimate =", estimate)
print("sqrt(2) =",np.sqrt(2))
     