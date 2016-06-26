input = raw_input()
outputString = ""
for alphabet in input:
    if alphabet.isupper() is True:
        alphabet=alphabet.lower()
        #print alphabet
        outputString=outputString+alphabet
    else:
        alphabet=alphabet.upper()
        outputString=outputString+alphabet
print outputString