#this is the main file where the function will run

from die import Die

def main():
    six_side: Die = Die()
    ten_side: Die = Die(10)
    twenty_side: Die = Die(20)

    print("Rolling 6-sided die: ")
    for i in range(10):
        six_side.roll_die()

    print("------------------------")
   
    print("Rolling 10-sided die: ")
    for i in range(10):
        ten_side.roll_die()

    print("------------------------")

    print("Rolling 20-sided die: ")
    for i in range(10):
        twenty_side.roll_die()

    print("------------------------")


if __name__ == "__main__":
    main()