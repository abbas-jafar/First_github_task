#defining functions
def print_code():
    print("Hi World")
    print("Hi World")
    print("Hi World")

print_code()

# 2nd way

def a_code():
    text = "hi jaf: how are you"
    print(text)
    print(text)

a_code()

#3rd way for function
#text1= "hello world"
def b_code(text1):
    print(text1)
    print(text1)

b_code("hello world")

#4th way with elseif condition

def school_cal(age):
    if age ==5:
        print("ali can join school")
    elif age>5:
        print("ali must go to high school")
    else:
        print("ali is a baby")

school_cal(15)


#another function for future

def future_age(age):
    new_age=age+15
    return new_age
    print(new_age)

future_predicted_age= future_age(20)
print(future_predicted_age)