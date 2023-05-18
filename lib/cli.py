#!/usr/bin/env python3

from helpers import (
    enter_name, customer_incoming
)


if __name__ == '__main__':
    user_name = ''
    open_tables = [1, 2, 3, 4, 5]

    print('Welcome to the Taghkonic Diner Adventure Game!')
    user_name = enter_name(user_name)
    customer_incoming(open_tables)
    
    