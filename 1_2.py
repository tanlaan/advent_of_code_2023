import sys

def main():
    cal = 0
    left = 0
    right = 0
    digit_words = ['one','two','three','four','five','six','seven','eight','nine','zero']
    digit_vals = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}

    try:
        while(True):
            line = input()
            nums = []
            i = 0
            while i < len(line):
                # from left to right identify every digit and word
                # append them in their int format to nums in order 
                if(line[i].isdigit()): 
                    nums.append(int(line[i]))
                else: 
                    for word in digit_words:
                        if(line[i:i+len(word)] == word):
                            nums.append(digit_vals[word])
                            break
                i += 1


            left = nums[0]
            right = nums[-1]
            temp = (left * 10) + right
            print(temp)
            cal += temp
    except EOFError:
        print(f"Your calibration value is : {cal}")

if __name__ == "__main__":
    main()


