
size = 1e5

#1e4 - 2 seconds
#1e5 - 40 seconds

p_count = 0

if False :
    for x in range (1, int(size)):
        #If x != 1 
        is_x_prime = x != 1
        
        #print ("X: %d, prime %d" % (x, is_x_prime))
        
        for n in range (2, x):
            if (x % n) == 0:
                is_x_prime = False
                break

        if is_x_prime:
            print (x)    

#######################################
#1e4 - 1 seconds
#1e5 - 7 seconds

print()
print ('#'*50)

prime_l = [2, 3, 5, 7]

for x in range (2, int(size)):
    is_x_prime = True

    for n in prime_l:
        if x != n:
            #print ('x = %d, n = %d' % (x, n))
            if (x % n) == 0:
                is_x_prime = False
                break

    if is_x_prime:
        p_count += 1
        prime_l.append(x)

#Result        
#print ('Prime numbers of size %d is %f percents' % (size , (p_count / size) * 100))
#or
s= ('Prime numbers of size {} is {}%'.format(size , (p_count / size) * 100))
print(s)

#Array of found numbers
#print (prime_l)
