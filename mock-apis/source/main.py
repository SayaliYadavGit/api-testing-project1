from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class UserRegisterRequest(BaseModel):
    username: str
    password: str
    email: str

class UserRegisterResponse(BaseModel):
    userId: str
    message: str

class UserLoginRequest(BaseModel):
    username: str
    password: str

class UserLoginResponse(BaseModel):
    token: str
    message: str

class Book(BaseModel):
    bookId: str
    title: str
    author: str
    description: str
    price: float

class AddToCartRequest(BaseModel):
    bookId: str
    quantity: int

class AddToCartResponse(BaseModel):
    cartId: str
    message: str

class CheckoutRequest(BaseModel):
    paymentMethod: str
    address: str

class CheckoutResponse(BaseModel):
    orderId: str
    message: str

@app.post("/users/register", response_model=UserRegisterResponse)
async def register_user(request: UserRegisterRequest):
    if request.username == "existing_user":
        raise HTTPException(status_code=404, detail="User already exists")
    if request.username == "":
        raise HTTPException(status_code=422, detail="Field required")
    return UserRegisterResponse(userId="user-123", message="User registered successfully")


@app.post("/users/login", response_model=UserLoginResponse)
async def login_user(request: UserLoginRequest):
    if request.username != "valid_user" or request.password != "valid_password":
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return UserLoginResponse(token="token-123", message="Login successful")

@app.get("/books", response_model=List[Book])
async def search_books(search: str):
    if search == "unknown":
        raise HTTPException(status_code=404, detail="No books found")
    return [
        Book(bookId="book-123", title="Sample Book", author="Author Name", description="Book description", price=29.99)
    ]

@app.post("/users/{userId}/cart", response_model=AddToCartResponse)
async def add_to_cart(userId: str, request: AddToCartRequest):
    if request.bookId != "book-123":
        raise HTTPException(status_code=404, detail="Book not found")
    return AddToCartResponse(cartId="cart-123", message="Book added to cart")

@app.post("/users/{userId}/checkout", response_model=CheckoutResponse)
async def checkout(userId: str, request: CheckoutRequest):
    if request.paymentMethod != "valid_method":
        raise HTTPException(status_code=402, detail="Payment declined")
    return CheckoutResponse(orderId="order-123", message="Checkout successful")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
