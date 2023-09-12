import json
#storing the product information in the json format. Each product can be represented on json
#object with attribute like name
#description , price , stock availability and images of the product stored in the stock.
#create a JSON array to tore multiple product object.abs

Products_catalog = [
    {
        "id": 1,
        "product_name": "product A",
        "description": "product description for produc A",
        "price": 19.99,
        "stock": 100,
        "images": ["image1.jpg", "image2.jpg", "image3.jpg"]
    },

    {
        "id": 2,
        "product_name": "product B",
        "description": "product description for produc B",
        "price": 20.99,
        "stock": 50,
        "images": ["image1.jpg", "image2.jpg", "image3.jpg"]
    },

       {
        "id": 3,
        "product_name": "product C",
        "description": "product description for produc C",
        "price": 60.99,
        "stock": 80,
        "images": ["image1.jpg", "image2.jpg", "image3.jpg"]
    }
]

# Loop through each product and print its information
for product in Products_catalog:
    print(f"Product {product['id']} Information:")
    print(f"Name: {product['product_name']}")
    print(f"Description: {product['description']}")
    print(f"Price: frw{product['price']:.2f}")
    print(f"Stock: {product['stock']} units")
    print("Images:")
    for image in product['images']:
        print(f"  - {image}")
    print()