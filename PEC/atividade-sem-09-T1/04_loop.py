def main():
    
    impr = ''
    for x in range(1010):
        if x !=0 and x % 10 == 0:
            s = str(x)
            if s == '1000':
                impr = impr + s + '.'
            else:
                impr = impr + s + ', ' 
    print(impr)


if __name__ == '__main__':
    main()
