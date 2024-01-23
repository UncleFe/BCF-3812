import random

def create_order_details_query(orders_count):
    file_path = 'C:\\Python\\BCF-3812\\Queries\\OrderDetails_sql_query.txt'

    with open(file_path, 'w') as file:
        file.write(f'INSERT INTO OrderDetails (OrderID, ProductID, EmployeeID, Quantity, Price) VALUES\n')

    with open(file_path, 'a') as file:
        for i in range(1, orders_count):
            order_id = i
            product_id = random.randint(1, 1000)
            employee_id = random.randint(2, 4)
            quantity = random.randint(1, 10)
            price = 1.67*quantity
            price *=i/2
            if (i+1<orders_count):
                query = f"({order_id}, {product_id}, {employee_id}, {quantity}, {price}),\n"
            else:
                query = f"({order_id}, {product_id}, {employee_id}, {quantity}, {price});\n"
        
            file.write(query)

    print(f"File was created, file location is: {file_path}")