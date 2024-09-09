from operator import itemgetter

numbers = list(range(1,101))

result = [ n for n in numbers if n % 5 == 0]

print (result)

#x = []

 #for i in range (5):
    #for j in range(4):
        #x[i][j] = 0

        #print (x)
x = []
n = [0] * 4
for _ in range(5):
    x.append(n)
print(x)

x = list(range(5))
z = []
for i in x:
    z.append(x)
print(z)

score = (1, 2, 2, 3, "bimbola")
list2 = [1,2,3,"bmbola",2.5]
print(list2)
list2[3] = "timothy"
print(list2)
single_tuple = (1,)
#print(score)
score = list(score)
score[4] = "chidima"
score = tuple(score)
#print(score)
print(type(score))

tuple2 = (1,2,3,[2,4,5], "priest", "10.3")
print(tuple2)
tuple2[3].extend([8,10])
print(tuple2)
print(len(tuple2))

print(tuple2)

numbers = [1,2,3,4,5]
print(1 in numbers)
print(6 not in numbers)
print(6 in range(len(numbers)))



























































































