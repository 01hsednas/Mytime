import time
name=input("Enter your name: ").capitalize()
timestamp=time.strftime('%H:%M:%S')

print(timestamp)

hour=int(time.strftime('%H'))

# print(hour)

if hour<=6 or hour<12:
    print("Good morning",name)
elif hour<=12 or hour<18:
    print("Good afternoon",name)
elif hour<=18 or hour<21:
    print("Good evening",name)
else:
    print("Good night",name)
