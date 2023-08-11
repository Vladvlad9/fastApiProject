from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form
from typing import List

from crud import CRUDPizzaMenu
from models import Menu
from schemas import PizzaMenuSchemaInDBSchema

app = FastAPI()

origins = [
    "http://localhost:3000",  # Адрес React-приложения
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/products", response_model=List[Menu])
# async def get_products():
#     products = await CRUDPizzaMenu.get_all()
#     return products


# @app.post("/products/")
# async def create_item(item: Menu) -> Menu:
#     # products = await CRUDPizzaMenu.get_all()
#     return item

@app.get("/products/{menu_id}")
async def read_items(menu_id: int, parent_id: int = 1):
    product = await CRUDPizzaMenu.get(menu_id=menu_id, parent_id=parent_id)
    return product


@app.get("/products/")
async def read_items() -> list[PizzaMenuSchemaInDBSchema]:
    products = await CRUDPizzaMenu.get_all()
    return products

