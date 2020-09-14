
FOR LOOP
In [60]: for i in range(len(nba_teams)):
    ...:     each_team = nba_teams[i]
    ...:     print(nba_teams[i])
Lakers
Nuggets
Celtics
Clippers

In [59]: for i in range(len(nba_teams)):
    ...:     each_team = nba_teams[i]
    ...:     print(i)
    ...:
0
1
2
3
---------------------------------------------------
In [56]: for i in range(0,15):
    ...:     print(i)
    ...:
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
-------------------------------------------------
WHILE LOOP 
In [54]: while number < 10:
    ...:     number+= 1
    ...:     print (number)
    ...:
1
2
3
4
5
6
7
8
9
10

FUNCTION
In [46]: vip = True

In [47]: food_place = "busy"

In [48]: def the_spot(vip, food_place, location="Bay Area"):
    ...:     if (food_place == "full" and not vip):
    ...:         print("Sorry, we have no room tonight at this {} loaction".form
    ...: at(location))
    ...:     elif(
    ...:     food_place == "busy" and not vip):
    ...:         print("Please wait 30 mins for a table at this {} location".for
    ...: mat(location))
    ...:     else:
    ...:         print("Welcome! Come sit down right away")
    ...:
--------------------------------------------------
In [49]: the_spot(vip, food_place)
Welcome! Come sit down right away

In [50]: the_spot(False, food_place)
Please wait 30 mins for a table at this Bay Area location

In [51]: the_spot(False, food_place, "Los Angeles")
Please wait 30 mins for a table at this Los Angeles location

In [44]: def legal_age(age):
    ...:     if(age < 21):
    ...:         return "Sorry your too young."
    ...:     elif (age == 21):
    ...:         return"You made it. Welcome to adulthood"
    ...:     else:
    ...:         return "Your free to pass. Enjoy"
    ...:

In [45]: legal_age(32)
Out[45]: 'Your free to pass. Enjoy'
---------------------------
In [36]: def add_numbers(num1, num2):
    ...:     result = num1 + num2
    ...:     return result
    ...:

In [37]: add_numbers
Out[37]: <function __main__.add_numbers(num1, num2)>

In [38]: add_numbers(5,5)
Out[38]: 10
----------------------------


In [18]: dog = {
    ...: "name": "Rocco",
    ...: "age": "7",
    ...: "location": "Los Angeles"
    ...: }


In [30]: my_message = f"{dog['name']} lives in {dog['location']}."

In [31]: my_message
Out[31]: 'Rocco lives in Los Angeles.'

--------------------------------
In [14]: arr_of_numbers = [1] * 3

In [15]: arr_of_numbers
Out[15]: [1, 1, 1]
