import time
import  random

def scrabble_score_COUNT():
    # DICTIONARY DESIGNED TO ASSIGN VALUES

    score_1 = {"a": 1, "b": 3, "c": 3, "e": 1, "g": 2,
               "i": 1, "k": 5, "j": 8, "m": 3,
               "l": 1, "o": 1, "n": 1, "p": 3, "s": 1,
               "r": 1, "u": 1, "t": 1,
               "x": 8, "q": 10, "z": 10, "d": 2, "f": 4, "h": 4, "v": 4, "y": 4, "w": 4, }
    rand_num1 = random.randint(5, 9)# random value generator
    print("Word should be  limit", rand_num1)
    user_inp = input("enter now")# word from user
    flag = 1# to check status for length of word
    if len(user_inp) != rand_num1:
        print("Enter only specified length for word")
        exit()
    else:
        flag=1


    # to length of  word entered by user input
    flag1=0

    words = { 0:'CABBAGE',1: 'Cabbage', 2:'cabbage',3: 'programs',
                 4:'python',5: 'player',6: 'condition',
                 7:'reversed', 8:'water', 9:'board', 10:'geeks'}
    if(flag==1):
            for i in words:
                if (user_inp == words[i]):
                    flag1=1
    else:
        print("Enter only dictionary word")
        exit()
    total_1 = 0
    time_sec=5
    if(flag1==1):
        if(len(user_inp)<6):
        #user_inp="Cabbage CABBAGE cabbage"
                while time_sec:
                     mins_1, secs_1 = divmod(time_sec, 60)
                     timeformat_1 = '{:02d}:{:02d}'.format(mins_1, secs_1)
                     print(timeformat_1)
                     time.sleep(1)
                     time_sec -= 1

        print("Timed out  ")
        try:
             if  user_inp.isalpha():
                 for X in user_inp:
                      total_1 = total_1+score_1[X.lower()]
             else:
                raise ValueError("Invalid Input .....Accept only Characters")
    #return  total_1G
        except ValueError as e:
            print("Information for User",e)
            total_1="No result"
            return total_1
        else:
            return total_1

def main():
    """Print the latest tutorial from Real Python"""
    tic = time.perf_counter()
    print("value is::::",scrabble_score_COUNT())
    toc = time.perf_counter()
    print(f"Code is working in {toc - tic:0.4f} seconds")


if __name__ == '__main__':
    main()
