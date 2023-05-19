#!/usr/bin/env python3

from helpers import (
    enter_name_ready, customer_incoming,
    take_an_order, make_a_choice,
    give_the_check, go_hang_out_with_a_customer
)


if __name__ == '__main__':
    open_tables = [1, 2, 3, 4, 5]
    seated_customers = []
    stress = 0
    total_money = 0
    new_customer = None

    enter_name_ready()
    while stress < 30:
        open_tables, new_customer = customer_incoming(open_tables)
        stress += (new_customer.hunger_level + new_customer.thirst_level)
        seated_customers.append(new_customer)
        print(f'\n********** CURRENT STRESS LEVEL: {stress} **********\n')
        choice = make_a_choice()
        if (choice == 1):
            go_hang_out_with_a_customer(seated_customers)
            seated_customers.append(new_customer)
        elif (choice == 2):
            destress, order = take_an_order(seated_customers)
            stress -= destress
        elif (choice == 3):
            money = give_the_check()
        



        break
        x += 1

    
    