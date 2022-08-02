from functools import reduce
def main():
    lista=[0,1,2,3,4,5,6,7,8,9,10]
    res=reduce((lambda a,b: a+b),filter((lambda x: not x%2==0),lista))
    print(res)
if __name__=='__main__':
    main()