import random

def create_inventory_query(products_count):
    file_path = 'C:\\Python\\BCF-3812\\Queries\\Inventory_sql_query.txt'

    with open(file_path, 'w') as file:
        file.write(f'"INSERT INTO Inventory (ProductID, Quantity) VALUES"\n')

    with open(file_path, 'a') as file:
        for i in range(1, products_count):
            products_id = i
            quantity = random.randint(0, 1500)

            if(i+1<products_count):
             query = f"({products_id}, {quantity}),\n"
            else:
                query = f"({products_id}, {quantity});\n"

            file.write(query)

    print(f"File was created, file location is: {file_path}")