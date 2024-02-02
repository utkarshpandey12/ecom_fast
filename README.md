# ecom_fast

### Build Stack

- To Clone:

      $ git clone
      $ cd ecom_fast
      $ python3 -m venv .venv
      $ source .venv/bin/activate
      $ $ pip install requirements.txt

### Run the Stack

- Install MongoDB community and run locally:

      $ brew install mongodb-community@7.0

- To run **app**, use this command:

      $ uvicorn app:app --reload


- To download **mongo shell**, :

      https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh


### Check database records and data

- To find **Database entries**, use this command from mongo shell :

      $ db.products.find({'price':22.47})


### Setup Product seed data

- Use this curl to setup init data:

      curl --location 'http://127.0.0.1:8000/post_products' \
        --header 'Content-Type: application/json' \
        --data '{

        "name" : "DEF",
        "price" : 22.50,
        "qty" : 10

       }'


### Service Links & Ports

- App Available on:

      http://127.0.0.1:8000

- API Documentation:

      http://127.0.0.1:8000/docs


### Folder Structure

- Detail Folder Structure:

        .
        └── ecom_fast/
            ├── 
            ├── 
            ├── requirements.txt
            ├── app.py (API lives here)
            ├── .gitignore
            ├── README.md
            ├── models.py (schmes/models)
            └── 
