# p=2piNT/ 60 10.20 3.45 float 10 20 1 2 3 int


import math

torque = float(input("Enter torque in Nm: "))
rpm = float(input("Enter RPM: "))

power = (2 * math.pi * rpm * torque) / 60

print("Power =", power, "Watts")