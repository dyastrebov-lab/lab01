#!/usr/bin/env python3
import sys,os
import json

WHO="appsec"

def Say_Hello( ):
    name = input("Enter your name: ")
    print ("Hello "+WHO+" world from @"+name)
    sys.stdout.write("Hello %s world from @%s\n" % (WHO, name))
    print("Hello {} world from @{}".format(WHO, name))
    print(f"Hello {WHO} world from @{name}")

Say_Hello()
