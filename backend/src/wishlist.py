import json 
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from src.auth import login_required
from src.db import get_db
from src.row_wrapper import row_to_dict, rows_to_dict

bp = Blueprint('wishlist', __name__)

@bp.route('/create_list', methods=['POST']) 
@login_required 
def create_list(): 
    try: 
        db = get_db()
        db.execute(
            "INSERT INTO wishlist (title, max_price, author_id) VALUES (?, ?, ?)",
            (request.json['title'], request.json['max_price'], g.user['id']),
        )
        db.commit() 
    except SyntaxError: 
        abort(400, f"Error: Missing datafield(s).") 
    except db.IntegrityError:
        abort(500, f"Error inserting into database.") 
    
    return "", 201 

@bp.route('/create_item', methods=['POST']) 
@login_required 
def create_item(): 
    parent_category = request.json['parent_category'] if 'parent_category' in request.json else None 
    link = request.json['link'] if 'link' in request.json else None 
    price = request.json['price'] if 'price' in request.json else None 

    try: 
        print(parent_category) 
        db = get_db()
        db.execute(
            "INSERT INTO item (parent_wishlist, parent_category, is_category, title, link, price) VALUES (?, ?, ?, ?, ?, ?)",
            (request.json['parent_wishlist'], parent_category, request.json['is_category'], request.json['title'], link, price), 
        )
        db.commit() 
    except KeyError: 
        abort(400, f"Error: Missing datafield(s).") 
    except db.IntegrityError:
        abort(500, f"Error inserting into database.") 
    
    return "", 201 

@bp.route('/get_wishlist/<parent_wishlist>', methods=['GET']) 
@login_required 
def get_items(parent_wishlist): 
    items = [] 

    try: 
        db = get_db() 
        items = db.execute(
            'SELECT * FROM item WHERE parent_wishlist = ?', (parent_wishlist,)
        ).fetchall() 
    except: 
        abort(500, "Error retrieving from database.") 
    
    if items == []: 
        abort(404, f"Parent wishlist id {parent_wishlist} not found") 
    
    return rows_to_dict(items) 

@bp.route('/get_item/<id>', methods=['GET']) 
@login_required 
def get_item(id): 
    item = None 

    try: 
        db = get_db() 
        item = db.execute(
            'SELECT * FROM item WHERE id = ?', (id,)
        ).fetchone() 
    except: 
        abort(500, "Error retrieving from database.") 
    
    if item == None: 
        abort(404, f"Item id {id} not found") 
    
    return row_to_dict(item) 

@bp.route('/update_item/<id>', methods=['PUT']) 
@login_required 
def update_item(id): 
    title = request.json['title'] if 'title' in request.json else None 
    link = request.json['link'] if 'link' in request.json else None 
    price = request.json['price'] if 'price' in request.json else None 

    try: 
        db = get_db() 
        db.execute( 
            'UPDATE item SET title = ?, link = ?, price = ?' 
            ' WHERE id = ?', 
            (title, link, price, id) 
        ) 
        db.commit() 
    except SyntaxError: 
        abort(400, f"Error: Missing datafield(s).") 
    except db.IntegrityError:
        abort(500, f"Error inserting into database.") 
    
    return "", 200 
