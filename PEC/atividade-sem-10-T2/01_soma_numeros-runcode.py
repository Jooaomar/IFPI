def main():
    
    v = 0
    while True:

        n = int(input())            
        
        if n != 0:
            v += n
        elif n == 0: 
            print(v)
            break


if __name__ == '__main__':
    main()
