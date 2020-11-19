#coding=utf-8

os = ['windows','linux','macos','solaris', 'android','ios']

print('\n')
print("="*20)
print('While loop')
print("="*20)
print('\n')

n = len(os)
while n > 0:
    #print(n)
    if os[n-1] != 'solaris':
        print(os[n-1])
        f = open('os_list_while.txt','a')
        f.write(os[n-1]+'\n')
        f.close()
    n -= 1
    

print('\n')
print("="*20)
print('For loop')
print("="*20)
print('\n')

for oss in os:
    if oss != 'solaris':
        print(oss)
        f = open('os_list_for.txt','a')
        f.write(oss+'\n')
        f.close()