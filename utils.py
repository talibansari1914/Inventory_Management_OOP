# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Utility functions (helper code).

Step-by-step Instructions:
1. Implement data validation helpers:
   - validate_price(price) → raise error if < 0
   - validate_stock(stock) → raise error if < 0
2. Implement file helpers (optional):
   - save_to_json(data, filename)
   - load_from_json(filename)

TODO for Students:
- Add at least 2 validation functions.
- Optionally, implement file handling for persistence.
"""


# Utility/helper functions.
# TODO: Implement this file

# Utility functions for validation and file operations.

def validate_price(price):
    # TODO: Ensure price > 0
    if not isinstance(price,(int,float)):
        raise TypeError("Price Type should be '(int)' or '(float)' .")
        
    if price<=0:
        raise ValueError("Price should be greater than 0")
    

def validate_stock(stock):
    # TODO: Ensure stock >= 0
    if not isinstance(stock,(int)):
        raise TypeError("Stock Type should be '(int)'.")
        
    if stock<0:
        raise ValueError("Stock Should be positive.")
    
