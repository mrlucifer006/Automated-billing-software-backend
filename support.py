import pandas as pd

'''Add a new item to the database with the specified name and price and
if the database does not exist,create a new DataFrame with columns for "item_name" and "price".'''
def add_data(name, price):
    #Try to read the existing database
    try:
        df = pd.read_csv("database.csv", index_col=0)
        #If the database does not exist,create a new DataFrame
    except FileNotFoundError:
        df = pd.DataFrame(columns=["item_name", "price"])
        #Add the new data to the DataFrame

    new_index = len(df)
    df.loc[new_index] = [name, price]
    #save the DataFrame to the database
    df.to_csv("database.csv", index=True)

'''Delete an item from the database based on the specified name andif 
the database does not exist,create a new DataFrame with columns for "item_name" and "price".
if the "item name" matches the specified name remove the row from the DataFrame'''
def del_data(name):
    #Try to read the existing database
    try:
        df = pd.read_csv("database.csv", index_col=0)
        # If the database does not exist,create a new DataFrame
    except FileNotFoundError:
        df = pd.DataFrame(columns=["item_name", "price"])
        #Remove the data with specified name
    df = df[df["item_name"] != name]
    #Save the updated DataFrame to the database
    df.to_csv("database.csv", index=True)


'''Update the price of an item in the database on the specified name and
the database does not exist,create a new DataFrame with columns for "item_name" and "price".
Update the price of an item in the DataFrame where the "item_name" 
matches specified upd_name to the new price upd_prc '''
def update_data(upd_name, upd_prc):
    #Try to read the existing database
    try:
        df = pd.read_csv("database.csv", index_col=0)
        # If the database does not exist,create a new DataFrame
    except FileNotFoundError:
        df = pd.DataFrame(columns=["item_name", "price"])
        #Update the price of the specifird item
    df.loc[df["item_name"] == upd_name, "price"] = upd_prc
    #Save the updated DataFrame to the database
    df.to_csv("database.csv", index=True)

'''Display all the item in the database including their index,name and price'''
def display_data():
    #Try to read the existing database
    try:
        df = pd.read_csv("database.csv", index_col=0)
        # If the database does not exist,create a new DataFrame
    except FileNotFoundError:
        df = pd.DataFrame(columns=["item_name", "price"])
        #Print each item in the data base
    for idx in df.index:
        #Display the item index,name and price
        print(f"{idx}  : {df.loc[idx, 'item_name']} - ₹{df.loc[idx, 'price']}")

'''Verify the credentials of an administrator and  If the admin database does not exist,print
 an error message and returns None'''
def check_admin (uid,pas):
    #Try to read the admin database
    try:
        df = pd.read_csv("admin.csv",index_col=0)
        # If the admin database does not exist,print an error message
    except FileNotFoundError:
        print("Some important resources are missing ...")
        print("Please contact the developer....")
        #Check if the credentials match any admin
    for ind in df.index:
        if df.loc[ind,"admin_id"] == uid:
            if df.loc[ind,"admin_pass"] == pas:
                #Return "verified" if the credentials are valid
                return "verified"
            # Return None if the credentials are invalid
            return None
        else:
            return "not_valid"
    return None


'''Verify the credentials of an employee . It checks if the provided employee ID(uid)
 and password(pas) match any employee credentials in the database'''
def check_employee (uid,pas):
    #Try to read the employee database
    try:
        df = pd.read_csv("employee.csv",index_col=0)
        # If the employee database does not exist,print an error message
    except FileNotFoundError:
        print("Some important resources are missing ...")
        print("Please contact the admin....")
        # Check if the credentials match any employee
    for ind in df.index:
        if df.loc[ind,"emp_id"] == uid:
            if df.loc[ind,"emp_pas"] == pas:
                # Return "verified" if the credentials are valid
                return "verified"
            # Return None if the credentials are invalid
            else:
                return "not_valid"
        return None
    return None


'''View all the employee details,including their index,ID and password and
If the employee database does not exist,create a new DataFrame'''
def view_employee ():
    # Try to read the employee database
    try:
        df = pd.read_csv("employee.csv",index_col=0)
        # If the employee database does not exist,create a new DataFrame
    except FileNotFoundError:
        df = pd.DataFrame(columns=['emp_id','emp_pas'])
        df.to_csv('employee.csv',index=True)
        print("The file does not exists..")
        print("Contact the developer ....")
        return
    #Print each employee
    for ind in df.index:
        #Display the employee index,ID and the password
        print(f"{ind} : {df.loc[ind,"emp_id"]} - {df.loc[ind,"emp_pas"]}")


''' This function adds a new employee to the employee database and
if the employee database does not exist,create a new DataFrame,
Add the new employee to the DataFrame with provided new_id, new_pas.'''
def add_employee(new_id,new_pas):
    # Try to read the employee database
    try:
        df = pd.read_csv("employee.csv", index_col=0)
    # If the employee database does not exist,create a new DataFrame
    except FileNotFoundError:
        print("error")

#Add the new employee to the DataFrame
    new_index = len(df)
    df.loc[new_index] = [new_id, new_pas]
    #save the updated DataFrame to the employee database
    df.to_csv("employee.csv", index=True)
