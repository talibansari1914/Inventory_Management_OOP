# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Defines the Store class.

Step-by-step Instructions:
1. Create Store class with attributes:
   - name (str)
   - products (dict → product_id: Product)
   - categories (dict → category_id: Category)
2. Methods:
   - add_product(product)
   - remove_product(product_id)
   - update_stock(product_id, qty)
   - get_product(product_id) → return Product object
   - list_all_products()
3. Ensure error handling:
   - Invalid product IDs
   - Negative stock updates

TODO for Students:
- Implement Store class methods.
- Maintain consistent product and category mappings.
- Use custom exceptions for errors.
"""


# Handles the Store class and product operations.
# TODO: Implement this file
# Store class manages all products and categories.
# Acts like a central manager.

from product import Product
from category import Category
from exceptions import ProductNotFoundError, InvalidOperationError

class Store:
    def __init__(self,name):
        # TODO: Maintain dict of products (id → Product)
        # TODO: Maintain dict of categories (name → Category)
        self.name=name
        self.products={}
        self.categories={}
        

    def add_product(self, product):
        # TODO: Add new product to inventory
        # Also add product into its category
        if product.product_id in self.products:
            raise InvalidOperationError(f" '{product.product_id}' already exists in Products.")
            
        self.products[product.product_id]=product
        print(f"Product '{product.name}' added  in the Product List. ")
        
        category_name=product.category
        if category_name not in self.categories:
            self.categories[category_name]=[]
        self.categories[category_name].append(product)
        print(f"Catgeory '{category_name}' added to the Categories.")

    def remove_product(self, product_id):
        # TODO: Remove product safely
        # Remove from both inventory and category
        
        if product_id not in self.products:
            raise ProductNotFoundError("Product Not Found !")
            
        removed_product=self.products.pop(product_id)
        print( f" Product '{removed_product.name}' has been removed from the List.")
        
        category_name=removed_product.category
        
        if category_name in self.categories:
            self.categories[category_name]=[p for p in self.categories[category_name] if p.product_id !=product_id]
            
            if not self.categories[category_name]:
                self.categories.pop(category_name)
        print(f"Product with ID '{product_id}' has been removed from the category.")
    
        
        

    def update_stock(self, product_id, qty):
        # TODO: Update stock by calling Product.update_stock()
        if product_id not in self.products:
            raise ProductNotFoundError("Product Not Found !")
            
        if not isinstance(qty,(int,float)):
            raise InvalidOperationError(f" '{qty}' can not be added.")
            
        product=self.products[product_id]
        product.update_stock(qty)
        return product.stock
        
    

    def update_price(self, product_id, new_price):
        # TODO: Update product price
        if product_id not in self.products:
            raise ProductNotFoundError("Product Not Found !")
        if new_price<=0:
            raise InvalidOperationError(f" Price Should not be Negative.")
            
        product=self.products[product_id]
        
        product.update_price(new_price)
        return product.price
        


    def apply_discount_to_category(self, category_name, percent):
        # TODO: Apply discount to all products in category
        discounted_price=0
        if category_name not in self.categories:
            raise ProductNotFoundError("Category not Found !")
            
        if percent <=0 or percent>100:
            raise InvalidOperationError(f" '{percent}' not valid !")
            
        for discount in self.categories[category_name]:
            discounted_price=discount.apply_discount(percent) 
            
        print(f"{percent} % Discount applied to the '{category_name}' & {discounted_price}")
        


    def list_all_products(self):
        # TODO: Return all products in store
        return list(self.products.values())
        
    

    def find_product(self, product_id):
        # TODO: Find product by ID, raise ProductNotFoundError if missing
        if product_id not in self.products:
            raise ProductNotFoundError("Product Not Found !")
            
        return self.products[product_id]
        

        

