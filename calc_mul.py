#!/usr/bin/python3

def calc(A,B):
    if type(A) is int and type(B) is int and 0<a and b<1000:
        ans=a*b
        return ans
    else:
        return -1
        
                
def main ():
    matchstring = ''
    while matchstring != 'end':
        A = input ('input A: ')
        B = input ('input B: ')
        print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
    main()
