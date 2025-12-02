import pytest
def product_details(name,product_id,quantity,price):
    result=(
        f"Product Name:{name}\n"
        f"Product ID:{product_id}\n"
        f"Quantity:{quantity}\n"
        f"Price:{price}"
    )
    return result
if __name__=="__main__":
    name="TV"
    product_id="S2345"
    quantity=1
    price=40000
    print(product_details(name,product_id,quantity,price))