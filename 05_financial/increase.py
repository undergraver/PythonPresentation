#!/usr/bin/env python

import sys

# raise in percent
raise_applied=6
raise_desired=40

# we compute:
#
# NOTE: the raise is computed annually
#
# 1. the number of years to reach the desired raise with the applied raise
# 2. money lost if the desired raise is applied instantly and no other raise is done

salary_now=100

desired_salary=salary_now*(1+raise_desired/100.0)

year_count=0
money_lost=0

while salary_now < desired_salary:
    year_count+=1
    salary_now=salary_now*(1+raise_applied/100.0)
    money_lost += (desired_salary-salary_now)*12.0
    
    
print("You will reach desired salary in:%d years" % (year_count))
print("By that time you will lose:%f" % (money_lost))
if year_count > 0:
    print("Average year loss is:%f" % (money_lost/year_count))
