import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? Can choose add, sub, mul, or div')
    args = parser.parse_args()
    operation = calc(args)
    print(operation)
    
def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y
    
if __name__ == '__main__':
    main()
    
# def calc(x, y, operation):
#     if operation == 'add':
#         return x + y
#     elif operation == 'sub':
#         return x - y
#     elif operation == 'mul':
#         return x * y
#     elif operation == 'div':
#         return x / y

# operation = calc(7,3,'div')
# print(operation)