import random


def main():

    int_max = 2**8 - 1 #assume max integer size as uint8
    while True:
        command = input().strip()

        if command == "Hi":
            print("Hi")

        elif command == "GetRandom":
            print(random.randint(0, int_max))

        elif command == "Shutdown":
            print("Shutting down...")
            break
    return
if __name__ == "__main__":
    main()

