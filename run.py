import pi

print "How many digits of pi would you like to see? (max. 100,000)"
while True:
    nth = raw_input("> ")
    if not nth.isdigit() or int(nth) > 100000:
        print "Please type an integer less than or equal to 100,000."
    else:
        break

nth = int(nth)
pi = pi.x
pi = list(pi)
pi2 = pi[:(nth+1)]
pi3 = ''.join(pi2)
print pi3
