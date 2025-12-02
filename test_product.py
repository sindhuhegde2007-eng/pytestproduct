from product import product_details

def test_product_details():
    expected_output=(
        "Product Name:TV\n"
        "Product ID:S2345\n"
        "Quantity:1\n" 
        "Price:40000"
    )
    assert product_details("TV","S2345",1,40000)==expected_output