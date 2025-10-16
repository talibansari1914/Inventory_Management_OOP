# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Defines the Category class.

Step-by-step Instructions:
1. Create Category class with attributes:
   - category_id (int)
   - name (str)
   - products (list of Product objects)
2. Add methods:
   - add_product(product)
   - remove_product(product_id)
   - list_products() → return all products in this category
3. Ensure duplicate products are not added.

TODO for Students:
- Implement Category class.
- Link products properly.
- Use exceptions for invalid operations.
"""


# Handles product categories.
# TODO: Implement this file

# Category class groups products (e.g., Electronics, Clothing).
# It can track all products under that category.

class Category:
    def __init__(self, name):
        # TODO: Initialize category with name and product list
        self.name=name
        self.category_id=0
        self.products={}
        

    def add_product(self, product):
        # TODO: Add product object to category list
        
        if product.product_id in self.products:
            raise Exception(f"Product with Product_id '{product.product_id}' already exists in Category '{self.name}'.")
            
        self.products[product.product_id]=product
        return f"Product Object '{product}' added in the Category '{self.name}'."
        

    def remove_product(self, product_id):
        # TODO: Remove product by ID from category list
        
        if product_id not in self.products:
            raise Exception(f"Product_id '{product_id}' not found in Category '{self.name}'. ")
            
        removed_product=self.products.pop(product_id)
        return f" '{removed_product.name}' Product has been removed from the Category '{self.name}'."
        

    def list_products(self):
        # TODO: Return all products in this category
        if not self.products:
            return f"Category '{self.name}' has no product."
            
        print(f"Products of the category '{self.name}' :")
        return list(self.products.values())
        
        

    def __str__(self):
        # TODO: String representation → Category name + product count
        product_count=len(self.products)
        return f"Category '{self.name}' has '{product_count}' Products."
