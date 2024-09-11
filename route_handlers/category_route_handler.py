from flask import jsonify, request
import json
from repositories.categories_repository import categoryrepository

def get_all_categories():
    try:
        repository = categoryrepository()
        data = repository.fetch_all_categories()
        return jsonify (data)
    except Exception as e:
        return jsonify({
            "error": str(e)
        })

def get_id_category(category_id):
    try:
        repository=categoryrepository()
        data = repository.fetch_category_by_id(category_id)
        return jsonify (data)
    except Exception as e:
        return jsonify({
            "error" :str(e)
        })
    
def post_categories():
    try:
        repository = categoryrepository()
        new_category = request.json
        data = repository.create_category(new_category["name"])
        return jsonify(data)
    except Exception as e:
        return jsonify({
            "error" :str(e)
        }) 

def update_category(category_id):
    try:
        repository = categoryrepository()
        category = request.json
        data = repository.update_category_by_id(category["name"], category_id)
        return jsonify(data)
    except Exception as e:
        return jsonify({
            "error" :str(e)
        })

def delete_category(category_id):
    try:
        repository = categoryrepository()
        data = repository.delete_category_by_id(category_id)
        return jsonify(data)
    except Exception as e:
        return jsonify({
            "error" :str(e)
        })