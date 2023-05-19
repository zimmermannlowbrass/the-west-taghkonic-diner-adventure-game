#!/usr/bin/env python3

from helpers import (
    enter_name_ready, customer_incoming,
    take_an_order, choose_a_task,
    give_the_check, go_hang_out_with_a_customer
)


if __name__ == '__main__':
    open_tables = [1, 2, 3, 4, 5]
    seated_customers = []
    stress = 0
    total_money = 0

    user_name = enter_name_ready()

    while stress < 50 and len(seated_customers) < 5:
        print(f'\n********** CURRENT STRESS LEVEL: {stress} **********\n')

        open_tables, new_customer = customer_incoming(open_tables, seated_customers)
        stress += (new_customer.hunger_level + new_customer.thirst_level)

        print(f'\n********** CURRENT STRESS LEVEL: {stress} **********\n')
        choice = choose_a_task()
        if (choice == 1):
            go_hang_out_with_a_customer(seated_customers)
        elif (choice == 2):
            destress, order = take_an_order(seated_customers)
            stress -= destress
        elif (choice == 3):
            earned_money, destress = give_the_check(open_tables, seated_customers)
            total_money += earned_money
            stress -= destress
    print(f'\n\n\n********** GAME OVER!!!**********\n\n\nIt looks like you made a total of ${total_money}\n\n')
        

    
    