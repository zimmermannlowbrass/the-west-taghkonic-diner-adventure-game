#!/usr/bin/env python3

from helpers_main import (
    customer_incoming, take_an_order,
    give_the_check, assess_customer_hunger_thirst,
)

from helpers_begin_end import enter_name_ready, choose_a_task, game_over


from helper_helpers import take_down_data, print_stress


if __name__ == '__main__':
    open_tables = [1, 2, 3, 4, 5]
    seated_customers = []
    stress = 0
    total_money = 0

    user_name = enter_name_ready()
    while stress < 50 and len(seated_customers) < 5:
        print_stress(stress)
        open_tables, added_stress = customer_incoming(open_tables, seated_customers)
        stress += added_stress
        choice = choose_a_task()
        if (choice == 1):
            assess_customer_hunger_thirst(seated_customers)
        elif (choice == 2):
            destress, order = take_an_order(seated_customers)
            stress -= destress
        elif (choice == 3):
            earned_money, destress = give_the_check(open_tables, seated_customers)
            total_money += earned_money
            stress -= destress
        elif (choice == 4):
            stress += 100
        take_down_data(user_name, total_money, stress, seated_customers, choice)
    game_over(user_name, total_money, stress, seated_customers)
            