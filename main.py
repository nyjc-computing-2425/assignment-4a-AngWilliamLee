nric = input('Enter the NRIC number: ').upper()

prefix = nric[0].upper()
digits = nric[1:8]
digit_list = [int(digit) for digit in digits]
suffix = nric[8:].upper()
prefix_str = "STFG"
suffix_str_1 = "JZIHGFEDCBA"
suffix_str_2 = "XWUTRQPNMLK"
invalid_nric = "NRIC is invalid."
valid_nric = "NRIC is valid."

digit_weights = [2,7,6,5,4,3,2]

total = 0


if not prefix in prefix_str:
    print(invalid_nric)

elif len(digits) != 7:
    print(invalid_nric)

elif len(suffix) != 1:
    print(invalid_nric)

elif not (digits.isdigit()):
    print(invalid_nric)

elif not suffix.isalpha():
    print(invalid_nric)

elif (suffix not in suffix_str_1) and (suffix not in suffix_str_2):
    print(invalid_nric)

else:
    for x in range (0, 6):
       total = digit_list[x] * digit_weights[x]


    if prefix in "TG":
        total = total + 4

    remainder = total % 11

    check_alpha = ''
    if prefix in "ST":
        check_alpha = suffix_str_1[remainder]
    elif prefix in "FG":
        check_alpha = suffix_str_2[remainder]

    if suffix == check_alpha:
        print(valid_nric)
    else:
        print(invalid_nric)
