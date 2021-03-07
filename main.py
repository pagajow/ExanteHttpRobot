import sys
from exante.ExanteApi import ExanteApi

if __name__ == "__main__":

    args = sys.argv
    if len(args) >= 3:
        eapi = ExanteApi(applicationID=args[1], accessKey=args[2])
        eapi.start()
    else:
        print("Too few arguments, applicationID and accessKey are missing: {}".format(args))
