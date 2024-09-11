from flask import Flask
from route_handlers.brand_route_handler import delete_brand, get_all_brands, get_id_brand, post_brands, update_brand
from route_handlers.category_route_handler import delete_category, get_all_categories, get_id_category, post_categories, update_category
from route_handlers.product_route_handler import delete_product, get_all_products, get_id_product, post_products, update_product

def register_routes(app):

    app.route('/products', methods = ['GET'])(get_all_products)
    app.route('/products/<int:product_id>', methods = ['GET'])(get_id_product)
    app.route('/products', methods = ['POST'])(post_products)
    app.route('/products/<int:product_id>', methods = ['PUT'])(update_product)
    app.route('/products/<int:product_id>', methods = ['DELETE'])(delete_product)

    app.route('/categories', methods = ['GET']) (get_all_categories)
    app.route('/categories/<int:category_id>', methods = ['GET'])(get_id_category)
    app.route('/categories', methods = ['POST'])(post_categories)
    app.route('/categories/<int:category_id>', methods = ['PUT'])(update_category)
    app.route('/categories/<int:category_id>', methods = ['DELETE'])(delete_category)

    app.route('/brands', methods = ['GET'])(get_all_brands)
    app.route('/brands/<int:brand_id>', methods = ['GET'])(get_id_brand)
    app.route('/brands', methods = ['POST'])(post_brands)
    app.route('/brands/<int:brand_id>', methods = ['PUT'])(update_brand)
    app.route('/brands/<int:brand_id>', methods = ['DELETE'])(delete_brand)