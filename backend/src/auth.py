import functools 

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from src.db import get_db 

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    db = get_db()
    response = None 
    error = None

    if not email:
        error = 'Email is required.'

    if error is None:
        try:
            db.execute(
                "INSERT INTO user (email) VALUES (?)",
                (email,),
            )
            db.commit()
        except db.IntegrityError:
            error = f"Email {email} is already registered."
        else:
            return "", 201

    flash(error)


    return "", 200

@bp.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    db = get_db()
    error = None
    user = db.execute(
        'SELECT * FROM user WHERE email = ?', (email,)
    ).fetchone()

    if user is None:
        error = 'Not a valid email.'

    if error is None:
        session.clear()
        session['user_id'] = user['id']
        response = {'a': 'b'} 
        return response, 201 

    flash(error)

    response = {'a': 'b'} 
    return response, 202 

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))