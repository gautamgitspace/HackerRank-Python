input = raw_input().split(' ')
#print input
#print type(input)
#countWord = 0
#countNotWord = 0
output = []

for word in input:
    if word:
        #countWord = countWord + 1
        #print 'word: ', countWord
        output.append(word[0].upper() + word[1:].lower())
    else:
        #countNotWord = countNotWord +1
        #print 'not word: ', countNotWord
        output.append('')

print ' '.join(output)