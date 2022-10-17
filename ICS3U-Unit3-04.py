# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: October 2022
# ICS3U-Unit3-04.py File,
# learning if...then...elseif...else... statements in python.


def main():

    # input and variables
    input_number = int(input("Enter an integer: "))

    # process and output
    if input_number > 0:
        print("\nThe number {0:,} is positive.".format(input_number))
    elif input_number < 0:
        print("\nThe number {0:,} is negative.".format(input_number))
    else:
        print("\nThe number {0} is neutral, it's a zero.".format(input_number))

    print("\n\nDone.")


if __name__ == "__main__":
    main()
