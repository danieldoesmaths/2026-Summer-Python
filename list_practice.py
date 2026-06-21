f1_drivers = ["Max","Oscar","Lewis","Lando","Kimi"]

f1_drivers.append("George")
print(f1_drivers)
# ['Max', 'Oscar', 'Lewis', 'Lando', 'Kimi', 'George'] #

f1_drivers.remove("Max")
print(f1_drivers)
# ['Oscar', 'Lewis', 'Lando', 'Kimi', 'George'] #

print(f1_drivers.pop(0))
# Oscar #

f1_drivers.sort()
print(f1_drivers)
# ['George', 'Kimi', 'Lando', 'Lewis'] # 

f1_drivers.reverse()
print(f1_drivers)
#['Lewis', 'Lando', 'Kimi', 'George'] # 

del(f1_drivers[0])
print(f1_drivers)
# ['Lando', 'Kimi', 'George'] # 

f1_drivers.insert(0,"Franco")
print(f1_drivers)
# ['Franco', 'Lando', 'Kimi', 'George'] # 