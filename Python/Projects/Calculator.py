
        
def adding():
    print(num1 + num2)

def removeing():
    print(num1 - num2)

def multiple():
    print(num1 * num2)

def divide():
    print(num1 / num2)



print("Welcome to my calc script")
print("there is 4 options are here"
    "1. Adding",
    "2. removing",
    "3. Multiple",
    "4. Divide"
)

while True:
    Choice = input("Enter your choice(1/2/3/4): ")

    if Choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first digit: "))
        num2 = float(input("Enter second digit: "))

        if Choice == '1':
            adding()
        elif Choice == '2':
            removeing()
        elif Choice =='3':
            multiple()
        elif Choice == '4':
            divide()
        else:print("Sorry there is no Choice that you typed.")
    #else:
        #print("Sorry there is no Choice that you typed.")




# #all the loops for that.
# def option_selection():
#     print("select one of them you went to do: " , input())
#     if input == 1:
#         firstoption()


# #call outs
# welcome()
# options()
# option_selection()



"""
plan
it will take input from the user 
then give solution of it.
all will be in int() to help me.
second will be subtraction.
third will be multipication.
forth will be division.
that's it for now.

"""