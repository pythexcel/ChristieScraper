import argparse, os

from scrap import ScraperBot
from orders import OrderItems


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--Make", "-m",  help="Please enter the Make: -m MakeName")
    parser.add_argument("--Model", "-d",  help="Please enter the Model: -d ModelName")
    args = parser.parse_args()
    Make = args.Make
    Model = args.Model

    if not Make :
        print("Please include Make using the -m in the cammand section of this script.")
        quit()
    elif not Model:
        print("Please include Model using the -d in the cammand section of this script.")
        quit()
    else:
        try:
            OrderItems(Make=Make,Model=Model)
        except Exception as error:
            print(str(error))

if __name__ == "__main__":
    main()


