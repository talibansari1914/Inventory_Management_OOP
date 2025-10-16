# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Handles reports and data export.

Step-by-step Instructions:
1. Define Report class with methods:
   - generate_inventory_summary(store)
     → Show all products, stock, total value
   - generate_category_summary(store)
     → Group products by category
2. Export options (optional extended scope):
   - Export to JSON
   - Export to CSV

TODO for Students:
- Implement Report class.
- Write clean tabular output using print.
- Optionally, add export to a file.
"""


# Generates reports for inventory.
# TODO: Implement this file
# Reporting functions to analyze inventory.
# Also include file export for CSV/JSON.

import json
import csv
import pandas as pd
class Report:
    def __init__(self, store):
        self.store = store

    def total_inventory_value(self):
        # TODO: Calculate total value of inventory
        print("========Inventory Value=========")
        total_value=0
        for product in self.store.products.values():
            value=product.price*product.stock
            total_value+=value
        print(f"Total Inventory Value={total_value}")
        return f"Total Inventory Value={total_value}"

    def low_stock_items(self, threshold=5):
        # TODO: Return list of items with stock < threshold
        low_stock=[]
        for product in self.store.products.values():
            
            if product.stock < threshold:
                print(f" '{product.name}' has left only '{product.stock}' stock")
                low_stock.append(product.stock)
                
        if not low_stock:
            print(f"  All Products has sufficient stock")
            
      

    def category_summary(self):
        # TODO: Show product count per category
        print("======Category Summary======")
        
        if not self.store.categories:
            print("No categories found .")
            return {}
        
        category_count={}
        for category_name,product in self.store.categories.items():
            
            category_count[category_name]=len(product)
        
        
        for  name,count in category_count.items():
            print(f"Category Name='{name}' ,Count='{count}' ")

    def export_to_json(self, filename):
        # TODO: Export product details into JSON file
        print("======Exporting Data into json file======")
        data=[{"ID":product.product_id,"name":product.name,"price":product.price,"stock":product.stock,"category":product.category}
              for product in self.store.products.values()]
        
        with open(filename,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=2,ensure_ascii=False)
        print("Data Exported to the json file")

    def export_to_csv(self, filename):
        # TODO: Export product details into CSV file
        
        print("=====Exporting Data To The Csv File=====")
        data=[
            {"ID":product.product_id,"name":product.name,"price":product.price,"stock":product.stock,"category":product.category}
            for product in self.store.products.values()]
        df=pd.DataFrame(data)
        df.to_csv(filename,index=False,encoding="utf-8")
        print("Data Exported to the csv file")
