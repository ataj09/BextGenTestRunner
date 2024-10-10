import random


def main():

    int_max = 2**63 - 1 #assume max integer size from python 2
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

