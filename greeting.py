import time

t = time.localtime()
print(t)
hour = int(time.strftime("%H"))
print(hour)
def greet():
    if hour >= 6 and hour < 12:
        print("Good Morning!")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
    elif hour >= 18 and hour < 22:
        print("Good Evening!")
    else:
        print("Good Night!")

greet()