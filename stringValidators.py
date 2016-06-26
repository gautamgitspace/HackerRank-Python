#use of inbuilt function - any
input = raw_input()
if any(alphabet.isalnum() for alphabet in input):
    print 'True'
else:
    print 'False'
if any(alphabet.isalpha() for alphabet in input):
    print 'True'
else:
    print 'False'
if any(alphabet.isdigit() for alphabet in input):
    print 'True'
else:
    print 'False'
if any(alphabet.islower() for alphabet in input):
    print 'True'
else:
    print 'False'
if any(alphabet.isupper() for alphabet in input):
    print 'True'
else:
    print 'False'
