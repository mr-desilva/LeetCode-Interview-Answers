class Solution:
    def romanToInt(self, s: str) -> int:
        # acceptable roman letters
        accept_char = list('IVXLCDM')
        input_char = list(s)
        value: int = 0
        input_char_len = len(s)

        # value dictionary
        roman_to_val = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }

        # check length constraints and acceptable letter constraints
        if((1 <= len(s) & len(s) <= 15) & ((set(input_char) & set(accept_char)) == set(input_char))):
            for index, roman in enumerate(input_char):
                if(index == input_char_len - 1):
                    value = value + (roman_to_val[roman])
                    return value
                    break

                if(roman_to_val[input_char[index]] < roman_to_val[input_char[index + 1]]):
                    value = value - (roman_to_val[roman])
                
                elif (roman_to_val[input_char[index]] >= roman_to_val[input_char[index + 1]]):
                    value = value + (roman_to_val[roman])

        