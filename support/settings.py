import os

mode = os.environ.get("SUPPORT_PROFILE")
print(mode)

if mode == "develop":
    from support.develop import *
elif mode == "beta":
    from support.beta import *
else:
    from support.product import *
