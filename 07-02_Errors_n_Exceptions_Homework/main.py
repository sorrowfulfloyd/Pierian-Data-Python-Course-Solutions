# Problem 1

# Handle the exception thrown by the code below by using try and except blocks.

def bruh1():
    while True:
        try:
            for i in ['a','b','c']:
                print(i**2)
        except (TypeError, ValueError, NameError) as e:
            print(e)
            break
        except:
            print('Unknown error has occured. BRUH')
            break

# Problem 2

# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

def divide():
    x = 5; y = 0
    try:
        return x/y
    except ZeroDivisionError as e:
        print('Error ', end='')
        print (e, end='')
        print(' not supported around here.')
    finally:
        print('Im done here')

# Problem 3

# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask_for_an_int():
    while True:
        try:
            bruh = int(input('Enter an int\n>'))
        except (ValueError, TypeError) as e:
            print(e)
            continue
        else:
            print(f'Many thanks. You succeeded to not suck for now! Num u entered was: {bruh}')
            break
    print('Your number squared is:', bruh**2)

def main():
    bruh1()
    divide()
    ask_for_an_int()

if __name__ == "__main__":
    main()