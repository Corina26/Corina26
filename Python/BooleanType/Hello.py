
print('Hello world')
# print "\python\"
print('\\python\\') 

# make a finbonaci sequence and log
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)

# make a function that returns a list of the numbers of the fibonacci sequence
# print 10 times 'Corina I love you'
def MESSAGE ():
    print('- Corina I love you- ' * 10)
    # create a file and write the message to it
    f = open('kjfkjf.txt', 'w')
    f.write('- Corina I love you- ' * 10)
    f.close()
    # read the file


 


MESSAGE()




