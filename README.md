CLCalc stands for "command-line calculator".  Type an expression into the box and it will evaluate it if you can.
All functions and variables defined in the [Python "math" library] (https://docs.python.org/3/library/math.html) are available.  Some additional features:
- You can adjust the number of significant digits of the answer with the spin box, and toggle whether it is written in scientific notation or not.
- You can copy the input with Command-C, and copy the output with Shift-Command-C.
- If you capitalize the trig functions (e.g. Sin(), Cos(), ASin()) they will work in degrees, not radians.
- The constant π (press option-p) is defined as well as "pi"
- Some additional physics constants are defined in the file `constants.py`; see that file for details.


If you would like to add your own constants or functions (in Python notation), you can add them to `constants.py` or the beginning `calc.py`, and then run `make` from the command line.


The file `CLCalc.app` was built by me using `py2applet` on a computer with MacOS12.6.5.  If it works for you, great! If not, or if you want to add constants or functions, install `py2applet` if you haven't already (`brew install py2applet` for example), and then run `make`.  The file `CLCalc.app` in the main folder is the app you want.
