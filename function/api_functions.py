import requests

BASE_URL = "http://127.0.0.1:8000"

def payload_user_register(username,password,email):
    return {"username": username,
            "password": password,
            "email": email
            }

def payload_blank_username():
    return {
        "password": "password123",
        "email": "new_user@example.com"
        }

def payload_login(username,password):
    return {
        "username": username,
        "password": password
    }

def payload_add_cart(book_id,quantity):
    return {
        "bookId": book_id,
        "quantity": quantity
    }

def payload_checkout(payment_method,address):
    return {
        "paymentMethod": payment_method,
        "address": address
    }

def register_user(payload):
    return requests.post(f"{BASE_URL}/users/register", json=payload)

def register_user_notfound(payload):
    return requests.post(f"{BASE_URL}/users/register/notfound", json=payload)

def login_user(payload):
    return requests.post(f"{BASE_URL}/users/login", json=payload)

def search_books(param):
    return requests.get(f"{BASE_URL}/books", params={"search": param})

def add_to_cart(payload):
    return requests.post(f"{BASE_URL}/users/user-123/cart", json=payload)

def checkout(payload):
    return requests.post(f"{BASE_URL}/users/user-123/checkout", json=payload)