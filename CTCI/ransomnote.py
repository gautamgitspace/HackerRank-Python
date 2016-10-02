#!/usr/bin/env python
def validate(mag_words, ransome_words, mag, ran):
    count_mag = {}
    count_ran = {}
    for item in mag:
        if item not in count_mag:
            count_mag[item] = 1
        else:
            count_mag[item] = count_mag[item] + 1
    print 'MAG: ', count_mag
    for item in ran:
        if item not in count_ran:
            count_ran[item] = 1
        else:
            count_ran[item] = count_ran[item] + 1
    print 'RAN ', count_ran
    for key,value in count_ran.items():
        if key not in count_mag or count_mag[key] < value:
            return False
    else:
        return True


mag_words, ransome_words = map(int, raw_input().split(' '))
mag_string = "give me one grand tonight or tomorrow".split()
ransome_string = "give me one grand tonight or give me tomorrow".split()
print validate(mag_words, ransome_words, mag_string, ransome_string)
