import argparse
from helper import add
parser = argparse.ArgumentParser()
parser.add_argument("int1",help = "input 1st number",type = int)
parser.add_argument("int2",help = "input second number",type = int)
args = parser.parse_args()
print (add(args.int1,args.int2))