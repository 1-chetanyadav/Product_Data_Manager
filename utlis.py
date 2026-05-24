import json

def display_products(products):
    for product in products:
        print(json.dumps(product, indent=4))

def save_products_to_file(filename):
    with open(filename, 'r') as file:
        products = json.load(file)
        last_product = products[-1]
        last_product_id = int(last_product['id'])

    new_product = {}
    new_product_id = int(last_product_id + 1)
    print(f"New Product ID: {new_product_id}")
    new_product_name = input("Enter Product Name: ")
    new_product_category = input("Enter Product Category: ")
    new_product_rating = input("Enter Product Rating: ")
    new_product_price = input("Enter Product Price: ")
    new_product_stock = input("Enter Product Stock: ")

    new_product = {
        "id": int(new_product_id), 
        "name": new_product_name, 
        "category": new_product_category, 
        "rating": float(new_product_rating), 
        "price": float(new_product_price), 
        "stock": int(new_product_stock)
        }
        
    products.append(new_product)
    
    with open(filename, 'w') as file:
        json.dump(products, file, indent=4)

def load_products(filename):
    with open(filename,'r') as readfile:
        productss = json.load(readfile)   
        return productss
           
def search_product(get_product_id,filename):
    products = load_products(filename)
    for product in products:
        if product['id'] == get_product_id:
            print(f"Name: {product['name']}\nPrice: {product['price']}\nStock: {product['stock']}")
    # print(products)

# def load_file(filename):
#     with open(filename,'r') as file:
#         Products = json.load(file)
#         return Products


def delete_product(get_product_id,filename):
    print("in function")
    print(get_product_id)

    products = load_products(filename)
    print("pro load")
    for index, product in enumerate (products):
        print(f"{product['id']}")
        if product['id'] == int(get_product_id):
            print("match found")
            products.remove(product)
            # products.pop(index)
            print(f"Delete done {product['id']}")
    with open(filename,'w') as file:
        json.dump(products,file,indent=4)

