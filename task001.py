x=True
y=10
z=10.0
s='abdo'
y=float(y)


'''
Yes,We can convert the string numbers to integer 
for example if we used input method to get numbers from the user 
we will recieve the input in stringtype we can convert it to int again by using int(thenumber)
'''


lss=list(range(1, 6))
lss2=list(range(10, 16))
lss2=tuple(lss2)
d={'mohamed':'25','ali':'27','khaled':'20'}


'''
Yes,We can use semicolon ; in python to seperate statements 
if you are including more than one statement in the line
'''



'''
I thought python is Interpreted but i just did some research and foundout that it's actually both interpreted or compiled
'''



'''
Low-Level Language means it's kind of close to the machine
more hard to code and also understand like Machine language and also assembly

High-Level Language means it's more like the normal language
with it's syntax and so on and it's easy to learn and code also understand 
like python c# and most of the popular languages 
'''



'''
= means equal or assign like assign this number to a varible x=10 
== it's more like asking a question like if x==10 and it return T or F 
'''



'''
!= = means equal & ! means not so != means not equal
'''



'''
It is something that determines the order of operations 
for example some operators have higher precedence than others like 
"*" cames before the "+" operation
'''


x=10
x+=15
x/=5
x*=10
x%=3
print(11%4)
print(2**3)
11/3


'''yes we can use int(11/3) or use 11//3 '''

x=10
if x>15 :
    print("10 is bigger")
else: print("x is smaller than 15")


'''
if we want to make sure all the cases is true
'''


'''
"all" check that all conditions or elements is true if one is false it will not operate 
"and" is used if you want to make sure only two conditions is true
it can do the same as all but only if me made a squence of and this will create an 'all' so 'and' it's used for comparing two elements most of the time 
and 'all' is usually used to compare a squence of elements 
'''


'''
both the same but 'or' is used for compare between two elements and it can do like 'any' if we made a squence of it 
so 'or' it's used for comparing two elements most of the time  
and 'any' is usually used to compare a squence of elements 
'''



'''
we will use all
'''



'''
if is used only for one condition the first case actually but 
elif is used for all the conditions but not for the first case 
else is used as the default value if all conditions did not operate 
also used for the last condition 
'''



'''
yes we can use more than elif
'''


'''
no we only use one else 
'''

s=20 if 25<10 else print("Py")

'''
Which one is true and it will choose the last one true to operate
'''

'''
the default value if all elif is false
'''


x=2,y=4,z=5
lst=[2,4,6,8,10]

if 4 in lst:
    print("yes here")

elif 4 and 6 in lst:
	print("both here")

elif 4 or 6 in lst:
	print("one of them or maybe both here")

elif all([x==2,y==4,z==5]) in lst:
	print("all is here")
