from flask import Flask, jsonify , request

from repositories.brands_repository import brandrepository


def get_all_brands():
    try:
        repository = brandrepository()
        data = repository.fetch_all_brands()
        return jsonify (data)
    except Exception as e:
        return jsonify({
            "error": str(e)
        })

def get_id_brand(brand_id):
    try:
        repository = brandrepository()
        data = repository.fetch_brand_by_id(brand_id)
        return jsonify (data)
    except Exception as e:
        return jsonify({
            "error": str(e)
        })


def post_brands():
    try:
        repository = brandrepository()
        new_brand = request.json
        data = repository.create_brand(new_brand["name"])
        return jsonify(data) 
    except Exception as e:
        return jsonify({
            "error": str(e)
        })
    

def update_brand(brand_id):
    try:
        repository = brandrepository()
        brand = request.json
        data = repository.update_brand_by_id(brand["name"], brand_id)
        return jsonify(data)
    except Exception as e:
        return jsonify({
            "error": str(e)
        })


def delete_brand(brand_id):
    try:
        repository = brandrepository()
        data = repository.delete_brand_by_id(brand_id)
        return jsonify(data)
    except Exception as e:
        return jsonify({
            "error": str(e)
        })
