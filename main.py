from package.packing_unpacking import *

def packing_unpacking_print():
    req = {
        "username": "Joao",
        "password": "1234",
        "sum_list": [1,2,3,4,5,6,7,8,9,10]
    }
    func_args(*req["sum_list"])

def main():
    packing_unpacking_print()

if __name__ == "__main__":
    main()