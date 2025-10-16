# -*- coding: utf-8 -*-

# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Main entry point of the Inventory Management System.

Step-by-step Instructions:
1. Import classes: Product, Category, Store, Report.
2. Create a Store object (this will hold all products and categories).
3. Implement a simple menu system:
   a. Add product
   b. Remove product
   c. Update stock
   d. Generate report
   e. Exit
4. Use input() to interact with the user.
5. Call appropriate Store methods based on the menu choice.

TODO for Students:
- Implement the menu logic.
- Make sure invalid choices are handled using try/except.
- Provide clean output for the user.
"""
# TODO: Import required classes here
# from product import Product
# from store import Store
# from report import Report


# Entry point for the system.
# TODO: Implement this file

# Entry point (menu-driven interface).
# Students will implement CLI to test functionality.

from store import Store
from product import Product
from report import Report

def main():
    # TODO: Create Store instance
    # TODO: Add some sample products
    # TODO: Menu options:
    #   1. Add Product
    #   2. Remove Product
    #   3. Update Stock
    #   4. Update Price
    #   5. Apply Discount
    #   6. Show Reports
    #   7. Export Data
  
   store = Store("Sam Global Store")
   prod1 = Product(101, 'Laptop', 70000, 5, 'Electronics')
   prod2=Product(102,'Refrigerator',40000,7,'Electronics')
   prod3=Product(103,'Notebook',100,10,'Book')
   prod4=Product(104,'Jockey',500,4,'Clothes')
   
   for prod in [prod1,prod2,prod3,prod4]:
       store.add_product(prod)
   
   while True:
       print("\n===============Menu Options===============")
       print("1.Add Product")
       print("2.Remove Product")
       print("3.Update Stock")
       print("4.Update Price")
       print("5.Apply Discount")
       print("6.Show Reports")
       print("7.Export Data")
       print("8.Exit")
       
       try:
           user_input=int(input("\nUser Input:"))
   
           if user_input==1:
              product_id=int(input("Enter product_id:"))
              name=input("Enter product_name:")
              price=float(input("Enter product_price:"))
              stock=int(input("Enter stock:"))
              category=input("Enter category_name:")
              new_product=Product(product_id,name,price,stock,category)
              store.add_product(new_product)
              print(f" '{new_product}' added to the Product List..")

   
           elif user_input==2:
               product_id=int(input("Enter product_id(remove):"))
               store.remove_product(product_id)
               print(f"\nProduct of given product_id '{product_id}' has been removed.")
    
           elif user_input==3:
               product_id=int(input("Enter product_id(update_stock):"))
               new_stock=int(input("Enter new_stock:"))
               updated_stock=store.update_stock(product_id, new_stock)
               print(f"\n For Product Id '{product_id}' Stock has Updated which is ={new_stock} ")
        
           elif user_input==4:
               product_id=int(input("Enter product_id(update_price):"))
               new_price=float(input("Enter new_price:"))
               updated_price=store.update_price(product_id, new_price)
               print(f"\nFor Product Id '{product_id}' Price has Updated which is={new_price} rs")
        
           elif user_input==5:
               # print(store.list_all_products())
               category_name=input("Enter category_name:")
               percent=int(input("Enter percent:"))
               store.apply_discount_to_category(category_name, percent)
              
       
           elif user_input==6:
               # Show reports
               report=Report(store)
               print("\n")
               report.total_inventory_value()
       
              
               report.category_summary()
       
               print("\n====Low Stock Itme info====")
               report.low_stock_items()
       
           elif user_input==7:
               report=Report(store)
        
               report.export_to_json("MiniProject.json")
               report.export_to_csv("miniProject.csv")
               
           elif user_input==8:
               print("....Exit...")
               break
           else:
               print("Invalid Number !please enter number between(1 to 8)")
       except ValueError as v:
               print(f"Error:",v)
       #except (ProductNotFoundError,InvalidOperationError) as e:
           #print(e)
        

if __name__ == "__main__":
    main()
