mystring = "Hello World"

#indexing characters

print(mystring[0])

print(mystring[8])

print(mystring[9])

#reverse indexing

print(mystring[-2])

#last letter of any string is [-1]

#slicing

mystring = 'abcdefghijk'
print(mystring)

print(mystring[2])

#from c to the end

print(mystring[2:])

#print everything up to a particular index

print(mystring[:3])

#stop index (up to but not including)

print(mystring[3:6])

print(mystring[1:3])

#print all
print(mystring[::])

#step size

print(mystring[::2])
print(mystring[::3])
print(mystring[2:7:2])

#reverse string

print(mystring[::-1])
mystring=mystring[::-1]
print(mystring)