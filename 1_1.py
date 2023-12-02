import sys

def main():
    cal = 0
    left = 0
    right = 0

    try:
        while(True):
            line = input()
            for char in line:
                if char.isdigit():
                    left = int(char)
                    break
            for char in line[::-1]:
                if char.isdigit():
                    right = int(char)
                    break
            temp = (left * 10) + right
            print(temp)
            cal += temp
    except EOFError:
        print(f"Your calibration value is : {cal}")

if __name__ == "__main__":
    main()


