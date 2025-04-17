from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['user_email']
        username = request.form['user_username']
        password = request.form['user_password']

    return render_template('signup.html')