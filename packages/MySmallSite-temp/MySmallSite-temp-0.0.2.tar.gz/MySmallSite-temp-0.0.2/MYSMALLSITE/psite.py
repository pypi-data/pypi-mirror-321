from .gener import read, write, wither, o, w
from os.path import splitext as _split_ext #_spt..._spt..._spt... ohhhh fuck I want to import but you use `underscore`!! OMG ToT
from json import load, dump
from os.path import join as _join_path
from sys import argv as _a

__doc__ = '''
# [[MySmallSite]] `psite.py`

using [MyParamSites](https://github.com/H-E1P/MySmallSite) to make JS.

## PSI file (JSONic)

```
{
    "MSPV" : [[string value or list value ('cause it's an path ;)]]
    "LOAD" : [[STR LIST THAT WILL IMPORT]]
    "*.js" : [[js file path]]
    "sav2" : [[path2save]]
}
```

 - MSPV : MyParamSites Ver ; as MPS url is formed as `https://raw.githubusercontent.com/H-E1P/MyParamSite/*PATHS*/pageApp.js`, it's that path; for example; `refs/heads/main`.

## CLI MENUALS

python -m MYSMALLSITE.psite *.PSI to build PSI Project
python -m MYSMALLSITE.psite to see menual

# Inner Systems

## LAMBDAS
RUList(x) = isinstance(x, list)
BReguarly(x) = make path list to str to make regularly (x is str or list)

## FUNCTIONS
 - getJ : get JSON
 - setJ : set ~ (same)
 - reget : see `help(reget)`
'''

 RUList = lambda x : isinstance(x, list)
 BReguarly = lambda x : _join_path(x) if RUList(x) else x

getJ, setJ = wither(o)(load), wither(w)(dump)

def reget(fn : str):
    '''
    PSI to JS
    '''
    file = getJ(fn)
    MSPV = (lambda x : '/'.join(x) if RUList(x) else x)(x['MSPV']) ##LLAST FIX ;)
    MJSF, SAVE_TO = (lambda x : map(BRegularly, (x['*.js'], x['sav2'])))(file)
    write(SAVE_TO, f'''\
import {{{', '.join(file['LOAD'])}}} from "https://raw.githubusercontent.com/H-E1P/MyParamSite/{MSPV}/pageApp.js";

{read(JSF)}\
''')

'''
rueghioeqwfuweifrwi;jwifijwjkdjkdjkffjfnTLQKF!!!!!!!!

def simple_matchtypec(type : bool = True):
    varptr = []
    def simple_matchtypec(type : bool = True):
        varptr = []
        class SimpleMatchType:
            __slots__ = ("__type", )
            def __init__(self, type : bool = True):
                self.__type = type
        
            def __mot__(self, v):
                ret = (True, varptr.append(v))[0] if self.__type else ((True, varptr.pop())[0] if _ = v else varptr[-1] == v)
                _ = (v, )[0] #set _
                return ret
    
        return SimpleMatchType(type = type)
    return simple_matchtypec(type = type)

match = simple_matchtype()
case = simple_matchtype(False)

def main(*argv, _a = _a):
    if match*len(argv):
        if case*0: main(*_a)
        if case*1: print(__doc__)
        if case*2: reget(argv[-1])
        if case*_: #oh tlqk hoxy frame....
            print("oh no, I don't know what to do, becuase I allow param MAX 2, see not-input-param to see menual")
'''

def main(*argv, _a = _a):
    matchs = len(argv)
    if 1:
        if matchs == 0: main(*_a)
        elif matchs == 1: print(__doc__)
        elif matchs == 2: reget(argv[-1])
        else:
            print("oh no, I don't know what to do, becuase I allow param MAX 2, see not-input-param to see menual")

if __name__ == "__main__" : main()
