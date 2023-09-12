import json
#store user information in JSON format including user details, shipping address and order history
# use JSON object to represent individual users and an array to store multiple user profiles

users = [
    {
        "username": "user1",
        "email": "user1@example.com",
        "name": "fablo",
        "address": [
            {
                "street": "remera",
                "city":"kigali"
            }
                    ],
        "orders":[
            {
                "order_id": "order1",
                "date": "2023-09-12",
                "total": 500,
                "status": "shipped"
            }
                ]       
    },

    {
        "username": "user2",
        "email": "user2@example.com",
        "name": "Answer",
        "address": [
            {
                "street": "buswazi",
                "city":"kigali"
            }
                    ],
        "orders":[
            {
                "order_id": "order1",
                "date": "2023-09-12",
                "total": 200,
                "status": "pending"
            }
                ]       
    }
        ]

#displaying the list of users in easy way for reading
for user in users:
    print(f"{user['username']} information:")
    print(f"Username: {user['username']}")
    print(f"Email:{user['email']}")
    print(f"Name: {user['name']}")
    print()
    print(f"\t Address:")
    print('-------------------------')
    for address in user['address']:
        print(f"Street: {address['street']}")
        print(f"City: {address['city']}")
        print()
    print(f"\t Orders:")
    print('-------------------------')
    for order in user['orders']:
        print(f"Order: {order['order_id']}")
        print(f"Date: {order['date']}")
        print(f"Total: {order['total']}")
        print(f"Status: {order['status']}")
    print()


