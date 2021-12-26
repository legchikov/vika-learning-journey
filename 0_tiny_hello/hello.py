# print ("Hello, World!")
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    return parser.parse_args()
    

def hello(name):    
    strName = str(name).lower()
    if strName.islower():
        return "Hello, " + strName.title() + "!"
    else:        
        return "ERROR: Invalid Input data. Please use only string!"

def main():
    args = get_args()
    print(hello(args.name))

if __name__ == '__main__':
    main()