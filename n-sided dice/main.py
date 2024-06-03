import random

def main():
    number_sides = int(input("How many sides does your dice have? "))
    roll = random.randint(1 , number_sides)
    print('Your roll is ',str(roll))

if __name__ == '__main__':
    main()