import random

def main():
    print("Khansole Academy")
    number_1 = random.randint(10, 99)
    number_2 = random.randint(10, 99)
    print('what is ' + str(number_1) + '+' + str(number_2) +'?')
    answer = int(input('Your answer: '))
    if answer == number_1 + number_2 :
        print('Correct!')
    else:
        print('Incorrect.')
        print('The expected answer is ', str(number_1 + number_2))
    
    
if __name__ == '__main__':
    main()