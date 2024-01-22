import random

def create_orders_query(orders_count, customers_count):
    file_path = 'C:\\Python\\BCF-3812\\Queries\\Orders_sql_query.txt'

    with open(file_path, 'w') as file:
        file.write(f'"INSERT INTO Categories (OrderID, CustomerID, OrderDate, Status) VALUES"\n')

    with open(file_path, 'a') as file:        
        status_list = ['Open', 'InProgress', 'Close']
        for i in range(1, orders_count):
            order_id = i
            customer_id = random.randint(1, customers_count)
            order_date = '2024-01-12'
            if i>100 and i<=200:
             order_date = '2024-01-22'
            if i>200 and i<=300:
                order_date = '2024-01-25'
            if i>300 and i<=400:
                order_date = '2024-01-28'
            if i>400 and i<=500:
                order_date = '2024-01-30'
            order_status = random.choice(status_list)

            if(i+1<orders_count):
                query = f"({order_id}, {customer_id}, {order_date}, {order_status}),\n"
            else:
                query = f"({order_id}, {customer_id}, {order_date}, {order_status});\n"
        
            file.write(query)

    print(f"File was created, file location is: {file_path}")
