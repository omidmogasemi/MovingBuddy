from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from src.auth import login_required
from src.db import get_db

bp = Blueprint('wishlist', __name__)

@bp.route('/create_list', methods=['POST']) 
@login_required 
def create_list(): 
    title = request.json['title'] 
    max_price = request.json['max_price'] 
    db = get_db() 
    error = None 

    db.execute(
        "INSERT INTO wishlist (title, max_price, author_id) VALUES (?, ?, ?)",
        (title, max_price, g.user['id']),
    )
    db.commit()

    return {'a': 'b'}, 201 
