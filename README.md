
# Automated Billing Software

## Overview
Created by the students of CSE - C 1st year, this Python-based billing system uses pandas (2.2.3) to manage CSV files, which serves as a database. In also includes error handling for some cases where certain database files which do not exist.  This system uses a menu-driven interface, where the users can choose the options to perform different functions.  The admin and employee functions handle user authentication and authorization, ensuring only authorized users can access specific features. The code uses pandas library to manage data storage and retrieval. Split into assmodule1.py (backend) and assignment.py (CLI).  The assmodule1 module is likely a custom module that contains function for data management such as add_data, update_data, del_data, display_data, check_admin and check_employee.  Overall this code provides a basic framework for managing data and user authentication in a simple database system.Run with Python 3.13.3 and pandas.  See README to contribute.

## Features
- **Admins:** Add employees, manage products (add, update, delete, view).
- **Employees:** Add, update, and view products.
- **Customers:** Browse products, add to cart, generate bills (18% tax, 10% discount for totals over ₹1000).
- **Data Storage:** Uses CSV files (`database.csv`, `admin.csv`, `employee.csv`).
- **Modular Design:** Backend (`assmodule1.py`) and CLI (`assignment.py`).

## Requirements
- Python 3.13.3
- pandas 2.2.3

## Installation
1. Clone the repository:
   ```
   [git clone https://github.com/your-username/Automated-Billing-Software.git](https://github.com/mrlucifer006/Automated-billing-software-backend)
   ```
2. Install dependencies:
   ```
   pip install pandas==2.2.3
   ```
3. Ensure Python 3.13.3 is installed.

## Usage
1. Run the main script:
   ```
   python assignment.py
   ```
2. Choose a user type (Admin/Employee/Customer) and follow the prompts to interact with the system.

## Contributing
- Fork the repository and create a pull request with your changes.
- Report issues or suggest features via the Issues tab.
- Ensure code follows Python best practices and includes comments for clarity.

## License
MIT License - feel free to use, modify, and distribute this project.
