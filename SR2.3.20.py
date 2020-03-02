
car = ("name", " DeLorean DMC-12", "motor_pos", "rear", "n_of_wheels", 4, "n_of_passengers", 2, "weight", 1.230, "height", 1.140, "length", 4.216, "width", 1.857, "max_speed", 177)
lst = list(car)
print(type(lst))
ls = lst[5::2]
lol = ls[2::]
lil = lol[:-1:]
print(sum(lil))