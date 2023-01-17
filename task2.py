s = input()
print(isinstance(s, str))
print(isinstance(s, object))
print(isinstance(s, int))

print(isinstance(s, (str, type)))
