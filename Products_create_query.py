import random

def create_products_query(products_count, categories_count, suppliers_count):
    file_path = 'C:\\Python\\BCF-3812\\Queries\\Products_sql_query.txt'

    with open(file_path, 'w') as file:
        file.write(f'INSERT INTO Products (ProductID, CategoryID, SupplierID, Name, Description, Price) VALUES\n')

    with open(file_path, 'a') as file:        
        for i in range (1, products_count):
            product_id = i
            category_id = random.randint(1, categories_count-1)
            supplier_id = random.randint(1, suppliers_count-1)
            name = f'Product Name {i}'
            description = f'Description for Product {i}'
            price =1.5
            price *= i

            if(i+1<products_count):
                query = f"({product_id}, {category_id}, {supplier_id}, '{name}', '{description}', {price}),\n"
            else:
                query = f"({product_id}, {category_id}, {supplier_id}, '{name}', '{description}', {price});\n"

            file.write(query)
    print(f"File was created, file location is: {file_path}")

