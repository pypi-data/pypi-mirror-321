python-x256-numpy
=================

Quickly find the nearest xterm 256 color index of an RGB.

NumPy version of
`python-x256-offline <https://pypi.org/project/x256offline/>`__.

Installation
------------

.. code:: shell

   python -m pip install x256numpy

Simple Example
--------------

.. code:: python

   import x256numpy as x256

   c0 = 0x297331
   b, g, r = c0 & 0xff, (c0 >> 8) & 0xff, (c0 >> 16) & 0xff
   x0e = x256.from_rgb(r, g, b, weighted=False, n_color=232)
   x0w = x256.from_rgb(r, g, b, weighted=True, n_color=232)
   x1e = x256.from_rgb(r, g, b, weighted=False, n_color=256)
   x1w = x256.from_rgb(r, g, b, weighted=True, n_color=256)

   print('%06x %d %06x %d %06x %d %06x %d %06x' % (
       c0,
       x0e, x256.to_rgb(x0e),
       x0w, x256.to_rgb(x0w),
       x1e, x256.to_rgb(x1e),
       x1w, x256.to_rgb(x1w)
   ))
   # 297331 23 005f5f 2 008000 238 444444 239 4e4e4e
