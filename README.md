# Inventory Management System 

A robust, object-oriented Python-based **Inventory Management System** for small to medium-sized stores. Track products, manage stock, apply discounts, generate reports, and export data effortlessly. Built with clean code, custom exceptions, and modular design following OOP principles – perfect for beginners and pros alike!

##  Features
- **Product Management**: Add, remove, update stock/prices for products with validation.
- **Category Grouping**: Organize products into categories (e.g., Electronics, Books) with easy add/remove.
- **Stock & Pricing Controls**: Prevent negative stock/prices; apply category-wide discounts.
- **Reporting Dashboard**: Total inventory value, low-stock alerts, category summaries.
- **Data Export**: Save reports to JSON/CSV for backups or analysis.
- **Error Handling**: Custom exceptions for invalid operations (e.g., ProductNotFoundError).
- **CLI Interface**: Simple menu-driven console app for quick interactions.

##  Tech Stack
- **Language**: Python 3.8+
- **Libraries**: `json`, `csv`, `pandas` (for exports)
- **Design Patterns**: OOP (Classes: Product, Category, Store, Report), Exception Handling
- **No External DB**: In-memory storage for simplicity; easy to extend.

##  Installation
1. **Clone the Repo**:
2. git clone https://github.com/talibansari1914/inventory-management-system.git
cd inventory-management-system
3.pip install pandas

- Sample products (Laptop, Refrigerator, etc.) are auto-loaded for demo.

**Pro Tip**: No setup hassle! Works out-of-the-box on any Python environment.

##  Usage

### Menu Options
1. **Add Product**: Enter ID, name, price, stock, category.
2. **Remove Product**: By ID – auto-cleans from categories.
3. **Update Stock**: Add/subtract quantity (can't go negative).
4. **Update Price**: Set new price (must be positive).
5. **Apply Discount**: Percentage-based on entire category.
6. **Show Reports**: Inventory value, low-stock items (<5 stock), category counts.
7. **Export Data**: To `MiniProject.json` or `miniProject.csv`.
8. **Exit**: Graceful shutdown.

### Example Workflow
- ===============Menu Options===============
- 1.Add Product
- 2.Remove Product
- 3.Update Stock
- 4.Update Price
- 5.Apply Discount
- 6.Show Reports
- 7.Export Data
- 8.Exit

- User Input: 1
- Enter product_id: 105
- Enter product_name: Smartphone
- Enter product_price: 25000.0
- Enter stock: 3
- Enter category_name: Electronics
- 'Product(105, Smartphone, Price: 25000.0, Stock: 3, Category: Electronics)' added to the Product List..
- ===============Menu Options===============
- 1.Add Product
- 2.Remove Product
- 3.Update Stock
- 4.Update Price
- 5.Apply Discount
- 6.Show Reports
- 7.Export Data
- 8.Exit

- User Input:8
- ..exit..


##  Sample Output
### Total Inventory Report
- ========Inventory Value=========
- Total Inventory Value=659000.0  # (e.g., after adding samples)

### Low Stock Alert
- ====Low Stock Item info====
- 'Jockey' has left only '4' stock

### Category Summary
- ======Category Summary======
- Category Name='Electronics' ,Count='3'
- Category Name='Book' ,Count='1'
- Category Name='Clothes' ,Count='1'


##  Testing & Edge Cases
- **Validations**: Price/stock must be positive; discounts 0-100%.
- **Exceptions**: Handles missing products, invalid inputs gracefully.
- **Run Tests**: Extend with `unittest` (not included – add your own!).

##  Contributing
Love the project? Fork it, make improvements (e.g., GUI with Tkinter, DB integration with SQLite), and submit a PR! 
1. Fork the repo.
2. Create a feature branch (`git checkout -b feature/amazing-new-report`).
3. Commit changes (`git commit -m 'Add: GUI Dashboard'`).
4. Push & PR.

Issues? Open one with details – happy to collaborate! 


##  Author
- **Abbu Talib Ansari** | [GitHub](https://github.com/talibansari1914)
- Developed in: Spyder IDE 
- Built with  for learning OOP & Python.

---

**Star this repo if it helped!**  _Feedback welcome – let's make it even better!_
