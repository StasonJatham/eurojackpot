# eurojackpot
Okay so I read an article on how to win the lottery. Apparently there are some statistical tactics you can use like 2 low 3 high and 2 odd and 3 even... etc. <br> 

I wrote a Python script to automate the number picking. So it calculates random numbers (pseudo random, shutup nerds :,D). <br> You get 5 Lotto Numbers and 2 Euro Numbers, when querying with SQL below i added "hit", this shows you how many times the same number combination was calculated. 

So in theory the more times we get the same number combination, the more likely it is that those will be the winning numbers. <br> Now let us snap back to reality..hehe..this probably will not work and the numbers we get here probably will not help us win, but they make us feel like we are playing with a strategy so we can sleep at night.




## Usage 

 - First you wanna run the **lottnumber.py** script, this creates a sqlite db named "lottoX.db". <br>Format:
 ```num_1 number,num_2 number,num_3 number,num_4 number,num_5 number, euro_1 number, euro_2 number``` <br> A real DB would be much better.

 - Next you can run a simple SQL Query from the DB to get some winning numbers like:
```SQL
SELECT *, count(*) as hit  
FROM lotto
GROUP BY num_1, num_2, num_3, num_4, num_5
ORDER BY hit DESC
LIMIT 100;
```
- If you have an account at https://www.lotto24.de you can enter you creds in "enter_lotto24.py":
```python
# Enter the number of tickets you wanna play at line 6 (1 ticktet = 8 fields)
NUMBER_TICKETS = 4

# line 38 and 39
username.send_keys("<YOUR-EMAIL>")
password.send_keys("<YOUR-PASSWORD>")
```
If you run it, it will open a browser
