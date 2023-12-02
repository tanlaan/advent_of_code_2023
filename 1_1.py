import sys

def main():
    try:
        while(True):
            line = input()
            print(line)
            
    except EOFError:
        print("Merry XMAS")

if __name__ == "__main__":
    main()


