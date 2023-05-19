#!/usr/bin/env python3

from helpers import (
    enter_name_ready, customer_incoming,
    take_request
)


if __name__ == '__main__':
    open_tables = [1, 2, 3, 4, 5]
    x = 0

    enter_name_ready()
    while x < 5:
        open_tables, new_customer = customer_incoming(open_tables)
        take_request(new_customer)
        break
        x += 1

    
    