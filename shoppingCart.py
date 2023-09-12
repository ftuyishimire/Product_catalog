import json
#use JSON to represent a user's shopping cart, store the products, quantities, and subtotal for each item
# the shopping cart will represent every user with items added
shopping = {
    #main list of the users 
    "users": [
            #starting the identification of the first user
                {
                "user_id": "userABC",

                "items": [
                        #identifying product A for first user
                            {
                            "product_id": 1,
                            "quantity": 2,
                            "subtotal": 39.98
                            },
                        #identifying product B for first user
                            {
                            "product_id": 2,
                            "quantity": 1,
                            "subtotal": 29.99
                            }
                        ]
                }, #end of the first user identification

                {
                    # second user identification
                "user_id": "userDEF",
                "items": [
                        #identifying product A for second user
                            {
                            "product_id": 1,
                            "quantity": 3,
                            "subtotal": 59.97
                            },
                        #identifying product B for second user
                            {
                            "product_id": 2,
                            "quantity": 2,
                            "subtotal": 49.98
                            }
                        ]
                }
    ]
}

#displaying the information in the cart user with item added
for users in shopping:
    for user in shopping['users']:
        print(f"User: {user['user_id']} information:")
        print()
        print("\t ITEMS:")
        print('-------------------')
        for items in shopping['users']:
            for item in user['items']:
                print(f"product: {item['product_id']}")
                print(f"quantity: {item['quantity']}")
                print(f"subtotal: {item['subtotal']}")
                print()
        print()
        
