import time 
start = time.time()

import sqlite3
import random
from datetime import datetime
minutes = datetime.now().strftime('%M')
minutes = int(int(minutes)/2)+1

conn = sqlite3.connect('lottoX.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS lotto (num_1 number,num_2 number,num_3 number,num_4 number,num_5 number, euro_1 number, euro_2 number)')

conn.commit()

def random_lotto():
    random_lotto = []
    for i in range(1,50):
        x = random.randint(1,50)
        random_lotto.append(x)
    #for iterator in range(1,int(minutes)):
    #    random.shuffle(random_lotto)
    return random_lotto

def random_euro():
    random_euro = []
    for i in range(1,10):
        x = random.randint(1,10)
        random_euro.append(x)
    #for iterator in range(1,int(minutes/2)):
    #    random.shuffle(random_euro)
    return random_euro

def odd(num):
    if num % 2 == 0:
        return False # Even 
    else:
        return True # Odd

def high(num):
    if num < 25:
        return False # Low
    else:
        return True # High

def picked(lotto_list,num):
    if num in lotto_list:
        return True
    else:
        return False

def count_low(lotto_list):
    count = 0 
    for num in lotto_list:
        if not high(num):
            count += 1
    return count 

def count_high(lotto_list):
    count = 0 
    for num in lotto_list:
        if high(num):
            count += 1
    return count 

def count_odd(lotto_list):
    count = 0
    for num in lotto_list:
        if odd(num):
            count += 1
    return count 

def count_even(lotto_list):
    count = 0
    for num in lotto_list:
        if not odd(num):
            count += 1
    return count 

def all_random(lotto_nums,euro_num):

    lotto_list = lotto_nums[:5]
    euro_list  = euro_num[:2]
    
    lotto_list = lotto_list + euro_list
    return (lotto_list)

def strat_low_high_even_odd(lotto_nums,euro_num):
    # 3 low 2 high
    # 3 odd 2 even
    lotto_list = []
    euro_list  = []
    for num in lotto_nums:
        if count_high(lotto_list) < 2 and picked(lotto_list,num) == False and high(num):
            if odd(num) and count_odd(lotto_list) < 3:
                lotto_list.append(num)
            elif not odd(num) and count_even(lotto_list) < 2:
                lotto_list.append(num)

        if count_low(lotto_list) < 3 and picked(lotto_list,num) == False and not high(num):
            if odd(num) and count_odd(lotto_list) < 3:
                lotto_list.append(num)
            elif not odd(num) and count_even(lotto_list) < 2:
                lotto_list.append(num)

    for num in euro_num:
        if len(euro_list) < 2 and picked(euro_list,num) == False :
            euro_list.append(num)

    lotto_list = lotto_list + euro_list
    return (lotto_list)



def strat_low_high_odd_even(lotto_nums,euro_num):
    # 3 low 2 high
    # 2 odd 3 even
    lotto_list = []
    euro_list  = []
    for num in lotto_nums:
        if count_high(lotto_list) < 2 and picked(lotto_list,num) == False and high(num):
            if odd(num) and count_odd(lotto_list) < 2:
                lotto_list.append(num)
            elif not odd(num) and count_even(lotto_list) < 3:
                lotto_list.append(num)

        if count_low(lotto_list) < 3 and picked(lotto_list,num) == False and not high(num):
            if odd(num) and count_odd(lotto_list) < 2:
                lotto_list.append(num)
            elif not odd(num) and count_even(lotto_list) < 3:
                lotto_list.append(num)

    for num in euro_num:
        if len(euro_list) < 2 and picked(euro_list,num) == False :
            euro_list.append(num)

    lotto_list = lotto_list + euro_list
    return (lotto_list)


def strat_high_low_odd_even(lotto_nums,euro_num):
    # 2 low 3 high
    # 3 odd 2 even
    lotto_list = []
    euro_list  = []
    for num in lotto_nums:
        if count_high(lotto_list) < 3 and picked(lotto_list,num) == False and high(num):
            if odd(num) and count_odd(lotto_list) < 3:
                lotto_list.append(num)
            elif not odd(num) and count_even(lotto_list) < 2:
                lotto_list.append(num)

        if count_low(lotto_list) < 2 and picked(lotto_list,num) == False and not high(num):
            if odd(num) and count_odd(lotto_list) < 3:
                lotto_list.append(num)
            elif not odd(num) and count_even(lotto_list) < 2:
                lotto_list.append(num)

    for num in euro_num:
        if len(euro_list) < 2 and picked(euro_list,num) == False :
            euro_list.append(num)

    lotto_list = lotto_list + euro_list
    return (lotto_list)

def strat_high_low_even_odd(lotto_nums,euro_num):
    # 2 low 3 high
    # 2 odd 3 even
    lotto_list = []
    euro_list  = []
    for num in lotto_nums:
        if count_high(lotto_list) < 3 and picked(lotto_list,num) == False and high(num):
            if odd(num) and count_odd(lotto_list) < 2:
                lotto_list.append(num)
            elif not odd(num) and count_even(lotto_list) < 3:
                lotto_list.append(num)

        if count_low(lotto_list) < 3 and picked(lotto_list,num) == False and not high(num):
            if odd(num) and count_odd(lotto_list) < 2:
                lotto_list.append(num)
            elif not odd(num) and count_even(lotto_list) < 3:
                lotto_list.append(num)

    for num in euro_num:
        if len(euro_list) < 2 and picked(euro_list,num) == False :
            euro_list.append(num)

    lotto_list = lotto_list + euro_list
    return (lotto_list)



for x in range(0,100000000000):

    try:
        for y in range(0,7500):
            random_lotto_list = random_lotto()
            random_euro_list = random_euro()
            lotto_list = strat_low_high_even_odd(random_lotto_list,random_euro_list)
            if len(lotto_list) == 7:
                query = 'INSERT INTO lotto VALUES (?,?,?,?,?,?,?);'
                c.execute(query, lotto_list)
            else:
                pass

        for y in range(0,7500):    
            random_lotto_list = random_lotto()
            random_euro_list = random_euro()
            lotto_list = strat_low_high_odd_even(random_lotto_list,random_euro_list)
            if len(lotto_list) == 7:
                query = 'INSERT INTO lotto VALUES (?,?,?,?,?,?,?);'
                c.execute(query, lotto_list)
            else:
                pass

        for y in range(0,7500): 
            random_lotto_list = random_lotto()
            random_euro_list = random_euro()
            lotto_list = strat_high_low_even_odd(random_lotto_list,random_euro_list)
            if len(lotto_list) == 7:
                query = 'INSERT INTO lotto VALUES (?,?,?,?,?,?,?);'
                c.execute(query, lotto_list)
            else:
                pass

        for y in range(0,7500): 
            random_lotto_list = random_lotto()
            random_euro_list = random_euro()
            lotto_list = strat_high_low_odd_even(random_lotto_list,random_euro_list)
            if len(lotto_list) == 7:
                query = 'INSERT INTO lotto VALUES (?,?,?,?,?,?,?);'
                c.execute(query, lotto_list)
            else:
                pass   

        for y in range(0,7500): 
            random_lotto_list = random_lotto()
            random_euro_list = random_euro()
            lotto_list = all_random(random_lotto_list,random_euro_list)
            if len(lotto_list) == 7:
                query = 'INSERT INTO lotto VALUES (?,?,?,?,?,?,?);'
                c.execute(query, lotto_list)
            else:
                pass  
        
        conn.commit()

    except ValueError as e:
        pass


elapsed_time_lc=(time.time()-start)
print("------------> ",elapsed_time_lc)

conn.close()
