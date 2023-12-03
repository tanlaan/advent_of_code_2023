def main():
    colors = {'red':12,'green':13,'blue':14}

    id_sum = 0
    try:
        while(True):
            line = input() 

            # split off game header
            parts = line.split(':')
            # parse num for future
            game_num = int(parts[0].split(' ')[1])

            # break up reveals
            reveals = parts[1].split(';')
            valid_game = True
            for run in reveals:
                if not valid_game: break

                parts = run.split(',')
                for value in parts:
                   if not valid_game: break

                   num, color = value.strip().split(' ')
                   if(int(num) > colors[color]):
                       valid_game = False
            if valid_game:
                id_sum += game_num
            


    except EOFError:
        print(f"Your good game ID sums is: {id_sum}")
        pass
if __name__ == "__main__":
    main()
