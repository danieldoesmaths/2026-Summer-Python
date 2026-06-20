python = int(input("How many hours of Python have you done? :"))
maths = int(input("How many hours of Maths have you done? :"))
gym_sessions = int(input("How many Gym Sessions have you completed? :"))

score = python + maths + gym_sessions

print(f"Your summer score is {score}")

if score >20:
    print("Great Progress!")
else:
    print("Keep Working!")
