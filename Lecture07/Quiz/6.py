def hash(data):
    return data % 10

nums = [4322, 1334, 1471, 9679, 1989, 6171,6173, 4199]
m = {}
for i in nums:
    m[i] = hash(i)

print(m)