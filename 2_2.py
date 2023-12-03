def main():

    power_sum = 0
    try:
        while(True):
            line = input() 

            # split off game header
            parts = line.split(':')

            # break up reveals
            reveals = parts[1].split(';')
    
            colors_max = {'red':0,'green':0,'blue':0}
            for run in reveals:
                parts = run.split(',')
                for value in parts:
                   num, color = value.strip().split(' ')
                   num = int(num)
                   if num > colors_max[color]:
                       colors_max[color] = num
            power = 1
            for color in colors_max.keys():
                power *= colors_max[color]
            power_sum += power


    except EOFError:
        print(f"Your good game power sums is: {power_sum}")
        pass
if __name__ == "__main__":
    main()
