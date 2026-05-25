import json

from utils import (
    load_products,
    display_products,
    save_products_to_file,
    search_product,
    delete_product
)

while(True):
    print("---------------------------------------------------------------------")
    print('MAIN MENU')
    print('1. For Display DATA')
    print('2. For Save DATA')
    print('3. Search Product')
    print('4. Delete Product')
    print('5. Future update ::: Modify Product')
    print('6. For Exit')
    print("---------------------------------------------------------------------")

    filename = 'Product.json'

    user_choice = input("Enter >> ")
    if user_choice == '1':
        #print("option >> 1 choosed")
        products = load_products(filename)
        display_products(products)
    
    elif user_choice == '2':
        save_products_to_file(filename)

    elif user_choice == '3':
        product_id = int(input("Enter Product ID to Search:"))
        search_product(product_id,filename)

    elif user_choice == '4':
        product_id = input("Enter Product ID to delete stocks:")
        delete_product(product_id,filename)

    elif user_choice == '5':
        product_id = int(input("Work in progress:: $$$$$$$$$$$$$$$$$$$$$"))
        product_id = int(input("Enter Product ID to Modify stocks:"))
        break
        #search_product(product_id,filename)

    elif user_choice == '6':
        break

    else:
        print('Invalid Choice')
        break