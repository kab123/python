import argparse
parser = argparse.ArgumentParser()
parser.add_argument("int1",help = "input 1st number",type = int)
parser.add_argument("int2",help = "input second number",type = int)
args = parser.parse_args()

print (args.int1 + args.int2)