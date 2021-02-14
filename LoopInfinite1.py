# Infinite Look were the command will be executed till you get the right input
def main():
    i = get_positive_int("i: ")
    print(i)

def get_positive_int(prompt):
    while True: 
         n = int(input(prompt))
         if n > 0:
            break
    return n

if __name__ == "__main__":
    main()