# print("Hey, its Ritviq here , new to python")
# print("Ritviq")
# print('Ritviq')
# # variable declaration 
# a=3
# print(a)
# b="Heya There!"
# print(b)
# print(f"a is {a} and b is {b}") # formatted print statement 

# # This is one of the specific advandatage of using python language that we don't need to specify the data type  of the variable it'll be determined automatically

# #Giving white spaces(Gaps) at initial lines of code is okay, perhaps giving useless indentation further in between the code will give the indentation error EX:

#  # -------------------- Error (indentation error) ------------------ #
# #  a =20 # no error if it considered to be as the first line of code
# #  print("value of a is:" a)

# #     b = 30  # gives indentation error - Unexpected indent 
# #     print("a is",a)


#  ---------------  Types of operator  ----------------------- #
# General operators 
# a=10
# b=20

# c=a+b
# print(a,"+",b,"=",c)
# c=a-b
# print(a,"-",b,"=",c)
# c=a*b
# print(a,"*",b,"=",c)
# c=a/b
# print(a,'/',b,'=',c)
# c=a%b
# print(a,"%",b,"=",c)

# Diff between / and //
# a=20
# b=30
# c=a/b
# print(a,'/',b,'=',c)
# c=a//b
# print(a,"//",b,"=",c) # floor Divison (special Type of python operator )

# Use of ** operator - Exponentiation operator (special Type of python operator )
# a=9
# b=2
# c=a**b
# print(a,"**",b,"=",c)

# -------------- bitwise operators ----------------
# Use of & - AND operator : Sets bits to 1 , if both the given bits are 1.
# a=0
# b=1
# d=1
# c=a&b 
# e=d&b
# print(a,"&",b,"=",c)
# print(b,"&",d,"=",e)

# a=24  #Now all the decimail no get converted to binary first and then same AND operations would be performed respectively to the bits
# b=10    # 24 ---> 0011000
# d=10    # 10 ---> 0001010
# c=a&b            #0001000 ---> 8
# print(a,"&",b,"=",c)

# use of | - or operator : Sets bits to 1 if any of the given bit is 1
# a=0
# b=1
# d=1
# c=a|b 
# e=d|b
# print(a,"|",b,"=",c)
# print(b,"|",d,"=",e)

a=0
b=1
c=~a
d=~b
print(a,"~","=",c)
print(b,"~","=",d)




