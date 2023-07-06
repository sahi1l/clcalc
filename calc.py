#/usr/bin/env python3
from math import *
from random import random,randrange
from constants import *
import subprocess
import sys
π=pi
degrees=π/180
def Sin(x):
    return sin(degrees*x)
def Cos(x):
    return cos(degrees*x)
def Tan(x):
    return tan(degrees*x)
def ASin(x):
    return asin(x)/degrees
def ACos(x):
    return acos(x)/degrees
def ATan(x):
    return atan(x)/degrees

def calc(_A, exp=False, sigfig=3):
    _EXP=exp
    #    _S=' '.join(_A)
    _S = _A
    if _S[0]=='=':
       _S=_S[1:]
    prefix=_S.split(":",1)[0]
    if prefix=="E":
       _EXP=True
       _S=_S.split(":",1)[1]
    elif prefix=="U":
        if " to " in _S:
            _U=_S.split(":",1)[1].split(" to ")
        elif " as " in _S:
            _U=_S.split(":",1)[1].split(" as ")
        try:
            duh=subprocess.run(["units","-q",_U[0],_U[1]],
                            stdout=subprocess.PIPE)
            val=duh.stdout.decode(encoding='UTF-8').split('\n')[0].strip('\t* ')
            print(f"%.6g %s"%(float(val),_U[1]))
            exit()
        except Exception as ex:
            return "Units Error"
            exit()
         #Do stuff with units
    #Use proper exponentiation
    _S=_S.replace("^","**")
    _S=_S.replace("°","*degrees")

    #Evaluate
    try:
        result=eval(_S)
        if _EXP:
            return f"%.{sigfig}e"%(result,)
        else:
            return f"%.{sigfig}g"%(result,)
    except SyntaxError:
        return "Syntax Error"
    except OverflowError:
        return "Overflow Error"
    except:
        return "Other Error"
    #IDEA: Add unit conversion
