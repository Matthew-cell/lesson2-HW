# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:24:26 2021

@author: USER
"""

math= input('數學成績?')
math= int(math)
eng= input('英文成績?')
eng= int (eng)


if math>=90 and eng>= 90:
    print('有獎學金')
elif math==100 or eng == 100:
    print('有獎學金')
else:
    print('沒講學金')