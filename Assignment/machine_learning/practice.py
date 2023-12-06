import math


fair = (3/5) * (((-1/3) * math.log2(1/3)) + ((-2/3) * math.log2(2/3)))
print(fair)

exc = (2/5) * (((-1/2) * math.log2(1/2)) + ((-1/2) * math.log2(1/2)))
print(exc)
print(fair + exc)

ent = fair + exc

print("igain: ", 0.9710 - ent)
