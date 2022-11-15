import re
def just_do_it(text):
    # return text.capitalize()
    # return text.title()
    
    # from string import capwords
    # return capwords(text)

    if text:
        lastCharIsEmpty = False
        result = ""
        for i in range(0, len(text)):
            currentChar = text[i]
            if currentChar.isspace():
                result += currentChar
                lastCharIsEmpty = True
                continue
            elif re.match("\W",currentChar):
                result += currentChar
                if i == 0:
                    lastCharIsEmpty = True
                    continue
                else:
                    lastCharIsEmpty = False
                    continue
            elif currentChar.isalpha():
                if i == 0:
                    result += currentChar.upper()
                else:
                    if lastCharIsEmpty:
                        result += currentChar.upper()
                    else:
                        result += currentChar.lower()
                lastCharIsEmpty = False
                continue
            else:
                result += currentChar
                lastCharIsEmpty = False
                continue
        return result
    else:
        return text