# ფუნქციები რომლებიც ერთი მონაცემთა ტიპიდან გადაყვათ მეორეში 
# ამ შემთხვევაში int(),str() და float() ქვიათ მექანიკური მონაცემთა ტიპის შეცვლა
# მექანიკურში ვგულისხმობ იმას რომ ჩვენ ჩვენი ხელით გარდავქმნით ერთი ტიპიდან მეორეში

# int() ეს ფუნქცია გვეხმარება იმაში რომ მნიშვნელობა გარდავქმნათ ინტეჯერად ანუ მთელ რიცხვად.
print(int(5.9))
print(int("5") + 5)

# float() ეს ფუნქცია გვეხმარება იმაში რომ მნიშვნელობა გარდავქმნათ ათწილად რიცხვად.
print(float("5.6"))
print(float(3))

# str() ეს ფუნქცია გვეხმარება იმაში რომ ნებისმიერი მნიშვნელობა გარდავქმნათ სტრინგად.
print(str(5) + "5")
print(str(3.4) + "1")

# type() ეს ფუნქცია გვეხმარება იმაში რომ გავიგოთ კონკრეტული მნიშვნელობა რა ტიპის არის.
print(type(3.1))
print(type(5))
print(type("აკაკი"))
print(10 / 3) # მიბრუნებს ზუსტ გაყოფის შედეგს
print(5 // 2) # მიბრუნებს შედეგს თუ რამდენჯერ მოთავსდება გამყოფი გასაყოფში
print(5 % 2) # მიბრუნებს ნაშთს
print("luka" * 100)
print ("5 == 3")

(And=False) (Or=True)

#print არის ფუნქცია რომელსაც გადაეცემა არგუმენტები რამდენიც გინდა prints გამოაქ გამოსახულება.

#debug შეცდომის აღმოჩემა პროგრამაში

#ცვლადი ინახავს ინფორმაციას name = ინფორმაცია name არის ცვლადი

#stringi არის 


# f"" არის f სთრინგი რომელიც გვიმარტივებს ჩვენ ცვლადებზე მუშაობს, როდესაც მათი გამოტანის - output-ის დრო არის. ჩვენ შეგვიძლია, რომ დავწეროთ f, შემდეგ ჩვეულებრივად ბრჭყალები, რათა ტექსტი შევიტანოთ ცვლადებთან ერთად. ბრჭყალებში როდესაც დაგვჭირდება ცვლადის შემოტანა გავხსნით დაკლაკნილ ფრჩხილებს {} და მას გადავცემთ ცვლადის სახელს.

--------------------------------------------------------------------------------------------------------------------------------------------

num5 = int(input("enter your first number: "))
num6 = int(input("enter your second number: "))
sum = 0
if num5 > num6:
    for i in range(num6 , num5 + 1):
        sum += i
elif num6 > num5:
    for i in range(num5 , num6 + 1):
        sum += i 
else:
    print(f"{num5}={num6}")
print(sum)

--------------------------------------------------------------------------------------------------------------------------------------------



#         0    1          2
#                        0    1
_tuple = (1 , 50, ['daviti', 'guja'])
#        1      2
_arr = ['დათვი', 'თეთრი დათვი', 'შავი დათვი']

_arr[0] = 'ზებრა'

_tuple[2][1] = 'lamborgini'

print(_tuple)


--------------------------------------------------------------------------------------------------------------------------------------------




#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 77
b = 77
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

#ExampleGet your own Python Server
#Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Booleans represent one of two values: True or False.

In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two answers, True or False.
When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)
print(10 != 5) არ უდრის