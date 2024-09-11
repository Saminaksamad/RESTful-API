from flask import Flask, jsonify , request
from repositories.products_repository import productrepository


def get_all_products():
    try:
        repository = productrepository()
        data = repository.fetch_all_products()
        return jsonify(data)
    except Exception as e:
        return jsonify ({
            "error" : str(e)
        })

def get_id_product(product_id):
    try:
        repository = productrepository()
        data = repository.fetch_product_by_id(product_id)
        return jsonify(data)
    except Exception as e:
        return jsonify ({
            "error" : str(e)
        })


def post_products():
    try:
        repository = productrepository()
        new_product = request.json    
        data = repository.create_product(new_product)
        return jsonify (data) 
    except Exception as e:
        return jsonify ({
            "error" : str(e)
        })

def update_product(product_id):
    try:
        repository = productrepository()
        new_product = request.json    
        data = repository.update_product_by_id (new_product,product_id)
        return jsonify(data)
    except Exception as e:
        return jsonify ({
            "error" : str(e)
        })

def delete_product(product_id):
    try:
        repository = productrepository()
        data = repository.delete_product_by_id(product_id)
        return jsonify(data)
    except Exception as e:
        return jsonify ({
            "error" : str(e)
        })
