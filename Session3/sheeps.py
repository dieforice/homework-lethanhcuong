sizes = [5,7,300,90,24,50,75]
for i in range(1,4):
    print("hello1","my name is Hiep and these are my sheeps' sizes:",sizes)
    print("now my biggest sheep has the size", max(sizes),"let's shear it")
    index = sizes.index(max(sizes))
    sizes[index]=8
    print("after shearing, the sizes of my sheeps are",sizes)
    sizes = [x+50 for x in sizes]
    print("Month", i)
    print("one month has passed and here is the size of my new flock", sizes)
sum = sum(sizes)
print("The total size of my final flock is",sum)
cash = sum * 2
print("I would get", str(cash)+"$")
