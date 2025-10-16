# -*- coding: utf-8 -*-

# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Defines the Product class.

Step-by-step Instructions:
1. Define a Product class with attributes:
   - product_id (int)
   - name (str)
   - price (float)
   - stock (int)
2. Add __init__ method to initialize attributes.
3. Add __str__ method to return a nice string representation.
4. Add update_stock method to increase or decrease stock.
   - Ensure stock cannot go below 0.
5. Add apply_discount method (optional extended scope).

TODO for Students:
- Implement Product class fully.
- Ensure validations (e.g., price >= 0, stock >= 0).
- Raise exceptions for invalid inputs.
"""

# Handles the Product class.
# TODO: Implement this file

# Product class represents a single store item.
# Each product has: id, name, price, stock, and category.

from utils import validate_price,validate_stock
class Product:
    def __init__(self, product_id, name, price, stock, category):
        
        validate_price(price)
        validate_stock(stock)
        self.product_id=product_id
        self.name=name
        self.price=price
        self.stock=stock
        self.category=category
       

    def update_stock(self, quantity):
        try:
            if not isinstance(quantity, (int,float)):
                raise TypeError('Provide the valid data')
                
            if self.stock+quantity < 0:
                raise ValueError('Stock cannot be less than 0')
                
            self.stock += quantity 
            
        except Exception as e:
            return f'Error : {e}'
       
    def update_price(self, new_price):
        try:
            if not isinstance(new_price, (int,float)):
                raise TypeError('Provide the valid data')
            if new_price < 0:
                raise ValueError('Price is not less then 0')
                
            self.price = new_price
            
        except Exception as e:
            return f'Error : {e}'

    def apply_discount(self, percent):
        try:
            if not isinstance(percent,(int,float)):
                raise TypeError('Provide the valid data')
                
            if not (0 <= percent <=100):
                raise ValueError('Discount percent must be between 0 and 100')
                 
            discounted_price= self.price - (self.price * percent/100)
            return f"After Discount Price will be={discounted_price}"
        
        except Exception as e:
            return f'Error: {e}'

    def __str__(self):
       return f"Product({self.product_id}, {self.name}, Price: {self.price}, Stock: {self.stock}, Category: {self.category})"
