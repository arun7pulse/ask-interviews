# Author ArunSK
# Integer to Roman program. 
# Roman numerals have been written with Addition notation and Subtraction notation using symbols. 
# Subtractive notation is used for 4 (IV), 9 (IX) 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# These are the only subtractive forms in standard use. These are included along with base 10 representation in the decimal_dict
# Addition notation is used in general and the smallest and largest can be represented are 1 and 3999.  

def integer_to_roman(number):
    base = number 
    decimal_dict = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 
                    'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000 }
    if number == 0: 
        return "ERROR: Zero represented as None in Roman"
    elif number > 0 and number < 4000:
        result = ""
        # Loop through all the decimal values from big number to small
        for key, val in reversed(decimal_dict.items()): 
            # Until we decode from left to right decimal places when value is more than and assign the letter. 
            while number - val >= 0:
                number -= val
                result += key       
        return f"INTEGER {base} To ROMAN: {str(result)}"
    else :
        return "ERROR: The largest number that can be represented in this Roman notation is 3999"

if __name__ == '__main__':
    print(integer_to_roman(156))
