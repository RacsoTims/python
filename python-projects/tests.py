standing = {"A": [0, 0, 10],"B": [0, 0, 12], "C": [0, 0, 6], "D": [0, 0, 6]}
standing1 = {}

keys_list = list(standing.keys())
lst = []

while keys_list:
	next_key = keys_list.pop()
	if len(lst) == 0:
		lst.append(next_key)
	else:
		relative_size = 0
		for item in lst:
			if standing[item][-1] > standing[next_key][-1]:
				relative_size += 1
		lst.insert(relative_size, next_key)

print(lst)
for item in lst:
	standing1[item] = standing[item]
print(standing1)