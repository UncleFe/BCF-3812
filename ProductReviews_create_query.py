import random

def create_product_reviews_query(product_reviews_count, products_count, customers_count):
    file_path = 'C:\\Python\\BCF-3812\\Queries\\ProductReviews_sql_query.txt'

    with open(file_path, 'w') as file:
            file.write(f'INSERT INTO ProductReviews (ReviewID, ProductID, CustomerID, ReviewText) VALUES\n')

    with open(file_path, 'a') as file:      
        for i in range(1, product_reviews_count):
            review_id = i
            product_id = random.randint(1, products_count)
            customer_id = random.randint(1, customers_count)
            review_text = f'Review text {i}'
        
            if(i+1<product_reviews_count):
                query = f"({review_id}, {product_id}, {customer_id}, '{review_text}'),\n"
            else:
                query = f"({review_id}, {product_id}, {customer_id}, '{review_text}');\n"

            file.write(query)

    print(f"File was created, file location is: {file_path}")
