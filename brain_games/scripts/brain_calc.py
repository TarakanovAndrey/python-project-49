#!/usr/bin/env python3


import prompt
from brain_games.library.greet import show_greet_and_get_name
from brain_games.library.task_brain_calc import show_task
from brain_games.library.calculation_result import calculation_result

def brain_calculator():
    name = show_greet_and_get_name()
    show_task()
    for i in range(3):
        right_answer = calculation_result()
        answer = prompt.string('Your answer: ')
        if answer == str(right_answer):
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {name}!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{right_answer}".')
            print(f"Let's try again, {name}!")
            break
            
            
def main():
    brain_calculator()
    
    
if __name__ == '__main__':
    main()
