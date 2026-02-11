def calculate_average_order_value(orders):
    if not orders:
        return 0

    total = 0
    count = 0

    for order in orders:
        if order["status"] != "cancelled":
            total += order["amount"]
            count += 1

    return 0 if count == 0 else total / count

