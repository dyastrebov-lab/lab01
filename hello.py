#!/usr/bin/env python3
import sys,os
import json

WHO="appsec"

def Say_Hello( ):
    print ("Hello "+WHO+" world")
    sys.stdout.write("Hello %s world\n" % WHO)
    print("Hello {} world".format(WHO))
    print(f"Hello {WHO} world")

Say_Hello()
