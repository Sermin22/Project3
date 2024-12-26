import os


def filter_orders_by_cost(file_iter, cost):
    row_head = next(file_iter) # client_id, order_id, order_cost

    rows = [row.split(",") for row in file_iter]
    client = [float(row[0].lstrip()) for row in rows]
    order = [float(row[1].lstrip()) for row in rows]
    order_cost = [float(row[2].lstrip()) for row in rows]
    indexses = [i for i, y in enumerate(order_cost)]
    indexses = list(filter(lambda x: order_cost[x] >= cost, indexses))

    return [f"{client[i]}, {order[i]}, {order_cost[i]}" for i in indexses]

if __name__ == "__main__":
    PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "orders.csv")
    with open(PATH_TO_FILE, "r") as f:
        result = filter_orders_by_cost(f, 20)

    print(result)
