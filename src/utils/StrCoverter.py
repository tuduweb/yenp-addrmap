import re

class YenpBasicNumber(object):
    numberString = ""

    def str_coverter(self, input_str: str):
        pass
    pass

def StrCoverter(input_str : str) -> tuple:
    num_str = input_str
    num_result = 0
    num_type = "d"
    num_valid = True

    if num_str.startswith("'"):
        num_str = num_str[1:]
        if num_str.startswith("h"):
            num_type = "h"
            num_str = num_str[1:]
    elif num_str.startswith("h"):
        num_type = "h"
        num_str = num_str[1:]
    elif num_str.startswith("0x"):
        num_type = "h"
        num_str = num_str[2:]
    else:
        # regex
        pass
    # print(num_str)

    try:
        if num_type == "h":
            num_result = int(num_str, 16)
        elif num_type == "d":
            num_result = int(num_str, 10)
    except:
        num_valid = False
        pass
    return num_valid, num_result

# from Internet
def E_trans_to_C(string):
    E_pun = u',.!?[]()<>"\';:'
    C_pun = u'，。！？【】（）《》“‘；：'
    table= {ord(f):ord(t) for f,t in zip(E_pun,C_pun)}
    return string.translate(table)

def RangeStrConvert(range_str) -> tuple:
    msb, lsb = (0, 0)
    # comments covert .. 
    # range_str.replace(chr(65306), chr(58)) # not work
    print(range_str)

    # "a:b" style
    if range_str.isdigit():
        msb, lsb = (int(range_str), ) * 2
    elif re.match(r"\d+:\d+", range_str):
        range_nums = [int(num) for num in range_str.split(":")]
        # reverse
        range_nums = range_nums[::-1]
        print(range_nums)

        msb, lsb = range_nums[0], range_nums[1]

    return msb, lsb


if __name__ == "__main__":
    import argparse


    testStrings = [
        "h00",
        "'h33",
        "0x03",
        "h1_0",
        "h1__0"
    ]

    for idx, testItem in enumerate(testStrings):
        print(idx, testItem, StrCoverter(testItem))

    t0 = RangeStrConvert("3")
    t1 = RangeStrConvert("102:222")
    t2 = RangeStrConvert("-102:222")

    print(t0, t1, t2)