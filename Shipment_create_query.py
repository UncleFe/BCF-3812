import random

def create_shipment_query(shipment_count, orders_count):
    file_path = 'C:\\Python\\BCF-3812\\Queries\\Shipmet_sql_query.txt'

    with open(file_path, 'w') as file:
        file.write(f'"INSERT INTO Shipment (ShipmentID, OrderId, DeliveryAddress, Status) VALUES"\n')

    with open(file_path, 'a') as file:        
        statuses = ['Open', 'Ready', 'Done']
        for i in range(1, shipment_count):
            shipment_id = i
            order_id = random.randint(1, orders_count)
            delivery_address = f'Delivery address {i}'
            status = random.choice(statuses)
            if(i+1<shipment_count):
                query = f"({shipment_id}, '{order_id}', '{delivery_address}', '{status}'),\n"
            else: 
                query = f"({shipment_id}, '{order_id}', '{delivery_address}', '{status}');\n"

            file.write(query)