#!/usr/bin/env python3

# denominator values
den_values = set(range(1,10))

# numerator values
num_values = set(range(10))

# a/b + c/d + e/f

def compute(a,b,c,d,e,f):
    return a/b + c/d + e/f

def check_all_possibilities():
    max_val=0

    used_digits = set()
    values = ()

    for a in num_values:
        used_digits.add(a)
        for b in den_values - used_digits - set(range(a)):  # make sure b > a
            used_digits.add(b)
            for c in num_values - used_digits:
                used_digits.add(c)
                for d in den_values - used_digits - set(range(c)): # make sure d > c
                    used_digits.add(d)
                    for e in num_values - used_digits:
                        used_digits.add(e)
                        for f in den_values - used_digits - set(range(e)): # make sure f > e
                            val = compute(a,b,c,d,e,f)
                            if val > max_val and val < 1.0-0.00000001:
                                max_val = val
                                values = (a,b,c,d,e,f)
                        used_digits.remove(e)
                    used_digits.remove(d)
                used_digits.remove(c)
            used_digits.remove(b)
        used_digits.remove(a)
                                
    print(max_val)
    print(values)

if __name__ == "__main__":
    check_all_possibilities()
