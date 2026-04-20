#%%
def main(a,b):
        c= a+b
        return c
if __name__ == '__main__':
    print(main(1,2))
#%%
def main(a,b):
        c= a+b
        return c
if __name__ == '__main__':
    main(1,'a')
# TypeError: unsupported operand type(s) for +: ‘int’ and ‘str’
#%%
def main(a,b):
    try:
        c= a+b
        return c
    except:
        print('please input int')
if __name__ == '__main__':
    main(1,'a')
# please input int
#%%
def main(a,b):
    try:
        c= a+b
        return c
    except TypeError:
        print( 'please input int')
    except:
        print('other error')
if __name__ == '__main__':
    main(1,'a')

#%%
def main(a,b):
    try:
        c= a+b
        if c>10:
            raise Exception('c is too big')
        print(c)
    except TypeError:
        print( 'please input int')
if __name__ == '__main__':
    main(1,11)
# Exception: c is too big
#%%
def main(a,b):
    try:
        c= a+b
        if c>10:
            raise Exception('c is too big')
        print(c)
    except TypeError:
        print( 'please input int')
    finally:
        print('終於結束啦～～')
if __name__ == '__main__':
    main(1,2)
# 3
# 終於結束啦～～