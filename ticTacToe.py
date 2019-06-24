# programm for the tic-tac-toe game
import random
import sys


def print_matrix() :
    #function to print matrix on the screen
    print("-------------")
    print("|"+matrix[1]+"|"+matrix[2]+"|"+matrix[3]+"|")
    print("|---|---|---|")
    print("|"+matrix[4]+"|"+matrix[5]+"|"+matrix[6]+"|")
    print("|---|---|---|")
    print("|"+matrix[7]+"|"+matrix[8]+"|"+matrix[9]+"|")
    print("-------------")

def menu():
    global user_sign
    global cpu_sign
    print("Hello from TicTacToe Game!")
    start=random.randint(0,1)
    if (start == 1):
        user_sign="X"
        cpu_sign="O"
        print("You use "+user_sign+" so computer start first")
        cpu_run()
        for i in range(4):
            usr_run()
            cpu_run()
    else:
        user_sign="O"
        cpu_sign="X"
        print("You use "+user_sign+" so you start first")
        usr_run()
        for i in range(4):
            cpu_run()
            usr_run()
    
def usr_run():
    print("Please indicate where you would like insert (1,2,3,..,9):",end=" ")
    position=int(input())
    while busy_box(position):
        print("Position busy, please indicate where you would like insert (1,2,3,..,9):",end=" ")
        position=int(input())
    matrix[position]=" "+user_sign+" "
    print_matrix() 
    if(check_win(position,user_sign)):
        print("USR WIN!")
        sys.exit( )

def cpu_run():
    print("Cpu run!")
    input()
    cpu_number=random.randint(1,9)
    print("cpu_number: ",cpu_number)
    while busy_box(cpu_number):
        cpu_number=random.randint(1,9)
    matrix[cpu_number]=" "+cpu_sign+" "
    print_matrix()
    if(check_win(cpu_number,cpu_sign)):
        print("CPU WIN!")
        sys.exit( )
    
def check_win(position,sign):
    if ((position == 1)or(position == 4)or(position == 7)):
        if ((matrix[position] == " "+sign+" ") and (matrix[position+1] == " "+sign+" ") and (matrix[position+2] == " "+sign+" ")):
            return True
    if ((position == 2)or(position == 5)or(position == 8)):
        if ((matrix[position] == " "+sign+" ") and (matrix[position-1] == " "+sign+" ") and (matrix[position+1] == " "+sign+" ")):
            return True
    if ((position == 3)or(position == 6)or(position == 9)):
        if ((matrix[position] == " "+sign+" ") and (matrix[position-1] == " "+sign+" ") and (matrix[position-2] == " "+sign+" ")):
            return True
    if ((position == 1)or(position == 2)or(position == 3)):
        if ((matrix[position] == " "+sign+" ") and (matrix[position+3] == " "+sign+" ") and (matrix[position+6] == " "+sign+" ")):
            return True
    if ((position == 4)or(position == 5)or(position == 6)):
        if ((matrix[position] == " "+sign+" ") and (matrix[position-3] == " "+sign+" ") and (matrix[position+3] == " "+sign+" ")):
            return True
    if ((position == 7)or(position == 8)or(position == 9)):
        if ((matrix[position] == " "+sign+" ") and (matrix[position-3] == " "+sign+" ") and (matrix[position-6] == " "+sign+" ")):
            return True
    if ((position == 1)or(position == 5)or(position == 9)):
        if ((matrix[1] == " "+sign+" ") and (matrix[5] == " "+sign+" ") and (matrix[9] == " "+sign+" ")):
            return True
    if ((position == 3)or(position == 5)or(position == 7)):
        if ((matrix[3] == " "+sign+" ") and (matrix[5] == " "+sign+" ") and (matrix[7] == " "+sign+" ")):
            return True

def busy_box(position):
    if matrix[position] == "   ":
        return False
    else:
        return True


matrix = {1:"   ", 2:"   ", 3:"   ",
          4:"   ", 5:"   ", 6:"   ",
          7:"   ", 8:"   ", 9:"   "
         }

menu()

