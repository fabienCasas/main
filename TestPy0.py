'''
Created on Jan 5, 2019

@author: fab
'''
import argparse
from tf_test0 import tf_test



def run(arg1, opt1=None):
    print(arg1, " ", opt1)



def main():
    print("Hello Python world")
    parser = argparse.ArgumentParser()
    parser.add_argument("arg1", help="arg1")
    parser.add_argument("--opt1", "-o1", help="opt1", action="store_true")
    args = parser.parse_args()
    run(args.arg1, args.opt1)
    
    
    
if __name__ == "__main__":
    main()