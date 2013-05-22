from math import sqrt
n = 10
sq_5 = sqrt(5)
e1 = ((1.0 + sq_5)/2)**n
e2 = ((1.0 - sq_5)/2)**n
f_n = (e1 - e2)/sq_5
print "fib(",n,") = ", f_n