def percentage_difference(customer_sales, regional_sales):
    # Check if regional sales is not zero to avoid division by zero
    if regional_sales != 0:
        return round(abs((customer_sales - regional_sales) / regional_sales) * 100, 2)
    else:
        # Return None or an appropriate value if regional sales is zero
        return None
    

"""
This Python file is dedicated to defining User-Defined Functions (UDFs), allowing the application to execute custom, 
complex operations on data within Snowflake. These functions enhance the app’s analytical and processing capabilities, 
making it possible to tailor data operations to specific needs.
"""