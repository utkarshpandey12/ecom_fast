# A Bare Bones Slack API
# Illustrates basic usage of FastAPI w/ MongoDB
from pymongo import MongoClient
from fastapi import FastAPI, status,Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import models as schema_models

DB = "ecom"
PRODUCT_COLLECTION = "products"
ORDER_COLLECTION = "orders"
DB_URL = "mongodb://localhost:27017"

# Instantiate the FastAPI
app = FastAPI()


@app.get("/status")
def get_status():
    """Get status of server.
     Can be used for doing health check of the service"""
    return {"status": "running"}


@app.post("/post_products", status_code=status.HTTP_201_CREATED ,response_model=schema_models.CatalogProduct)
def post_products(product: schema_models.Catalog):
    """Post a new product !!"""
    with MongoClient(DB_URL) as client:

        product_doc = product.dict()
        product_collection = client[DB][PRODUCT_COLLECTION]
        new_product = product_collection.insert_one(product.model_dump())

        product_in_db = schema_models.CatalogProduct(id=str(new_product.inserted_id),**product_doc)

        return product_in_db
        

@app.get("/products/", response_model=schema_models.PaginationProducts)
def list_products(
    limit: int = Query(10, gt=0),
    offset: int = Query(0, ge=0),
    min_price: float = None,
    max_price: float = None,
):
    """Get filtered products paginated response"""

    filters_applicable = {}
    if min_price is not None:
        filters_applicable["price"] = {"$gte": min_price}
    if max_price is not None:
        filters_applicable.setdefault("price", {})["$lte"] = max_price

    with MongoClient(DB_URL) as client:

        total_count = client[DB][PRODUCT_COLLECTION].count_documents(filters_applicable)

        cursor = client[DB][PRODUCT_COLLECTION].find(filters_applicable).skip(offset).limit(limit)

        products = [schema_models.CatalogProduct(id=str(product["_id"]), **product) for product in cursor]

        next_offset_value = offset + limit if offset + limit < total_count else None
        prev_offset_value = offset - limit if offset - limit >= 0 else None

        page_info = {
            "limit": limit,
            "nextOffset": next_offset_value,
            "prevOffset": prev_offset_value,
            "total": total_count,
        }

        return schema_models.PaginationProducts(data=products, page=page_info)
    


@app.post("/orders/", response_model=schema_models.ProductsOrder)
def create_order(order: schema_models.ProductsOrder):

    """Create a new order"""
    
    with MongoClient(DB_URL) as client:
        order_doc = jsonable_encoder(order)
        order_collection = client[DB][ORDER_COLLECTION]
        result = order_collection.insert_one(order_doc)
        return order