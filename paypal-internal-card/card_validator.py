#!/usr/bin/env python3

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        # print(d, sum(digits_of(d*2)))
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    if len(str(card_number)) > 1 and len(str(card_number)) <= 19:
        return luhn_checksum(card_number) == 0
    else : 
        # print("i am in false")
        return False 

if __name__ == '__main__':
    """ Prgram to do the card validation """
    card_num = 4532015112830366
    result = is_luhn_valid(card_num)
    print('Correct:' + str(result))
    
    result = is_luhn_valid(4624748233249080)
    print('Correct:' + str(result))
    result = is_luhn_valid(4624748233249780)
    print('Correct:' + str(result))

    result = is_luhn_valid(9566871780)
    print('Correct:' + str(result))

# def validate_card(card_num):
#     """ This is the card validator function using luhn 10 method. """
#     ndigit = len(card_num)
#     nsum = 0
#     is_second = False
#     for i in range(ndigit -1, -1, -1) : 
#         d = ord(card_num[i] - ord('0'))
#         if (is_second == True) : 
#             d = d * 2
#         nsum += d //10 
#         nsum += d % 10
#         is_second =  not is_second
#     if (nsum % 10 == 10 ): 
#         return True
#     else :
#         return False 
