import pathlib
import sys

def rename(path,ori,targ):
    for p in pathlib.Path(path).iterdir():
        targ_filename=p.name.replace(ori,targ)
        p.rename(p.parent.joinpath(targ_filename))

if __name__ == '__main__':
    args = sys.argv
    if len(args)==3:
        rename(".",args[1],args[2])
    elif len(args)==4:
        rename(args[1],args[2],args[3])
    else:
        print("args error.")