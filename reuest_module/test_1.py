import requests

def test_create_product_logic():
    url = "https://fakestoreapi.com/products"
    
    new_product = {
        "title": "Professional Wireless Mouse",
        "price": 49.99,
        "description": "High-precision optical sensor",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    }

    response = requests.post(url, json=new_product)
    print(response,"response----")

    if response.status_code == 200 or response.status_code == 201:
        print(f"Status Code Check: PASSED ({response.status_code})")
    else:
        raise Exception(f"CRITICAL FAIL: Server rejected request with {response.status_code}")

    product_data = response.json()
    print("product",product_data)

test_create_product_logic()