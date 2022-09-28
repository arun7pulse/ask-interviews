#!/usr/bin/env python3 
import sys
from card_validator import is_luhn_valid

data_dict = {}

def data_processor(line):
    global data_dict
    sline = line.split()
    # print(sline, len(sline))
    if len(sline) != 0:
        if sline[0].lower() == "add" and len(sline) != 0: 
            if is_luhn_valid(sline[2]): 
                data_dict[sline[1]] = {"card" : sline[2], "bal" : 0 , "status": "valid"}
                data_dict[sline[1]]['bal'] += int(sline[3].strip('$'))
                # print("valid", sline)
                # pprint(data_dict)
            else: 
                # print("else", sline, "\n", data_dict)
                if sline[0].lower() == "add": 
                    data_dict[sline[1]] = {"card" : sline[2], "bal" : "error", "status": "invalid"}
                # print("invalid", sline)
                # pprint(data_dict)

        elif sline[0].lower() == "charge" and sline[1] in data_dict.keys():
            if data_dict[sline[1]]['status'] == 'valid':
                balance = data_dict[sline[1]]['bal']
                data_dict[sline[1]]["bal"] = balance + int(sline[2].strip('$'))
                # print("aftercharge", sline)
                # pprint(data_dict)
        elif sline[0].lower() == "credit" and sline[1] in data_dict.keys():
            if data_dict[sline[1]]['status'] == 'valid':
                balance = data_dict[sline[1]]['bal']
                data_dict[sline[1]]["bal"] =  balance - int(sline[2].strip('$'))
                # print("aftercredit", sline) 
                # pprint(data_dict)
    

if __name__ == '__main__':
    """ Prgram to do the card processing """
    # print("arg0", sys.argv[0], "Length", len(sys.argv))
    # print("atty", sys.stdin.isatty())

    if len(sys.argv) == 1 :
        if sys.stdin.isatty(): 
            print("Please provide input file name or pipe input")
            print("ex1. python myprogram.py input.txt")
            print("ex2. python myprogram.py < input.txt")
            quit()
        # print("************\nSTDIN Processing\n************")
        for line in sys.stdin:
            if 'Exit' == line.rstrip():
                break
            data_processor(line.lower())


    if len(sys.argv) == 2: 
        with open(sys.argv[1], 'r') as f:
            contents = f.readlines()
            # print("************\nFILE Processing\n************")
            for line in contents:
                # print(line)
                data_processor(line.lower())

    # pprint(data_dict)
    sorted_dict = dict(sorted(data_dict.items()))
    # pprint(sorted_dict)
    # print("\nSummary after the Transactions\n")
    for user, values in sorted_dict.items():
        balance =  f"${str(values['bal'])}" if isinstance(values['bal'], int) else values['bal']
        print(f"{user}: {balance}")
