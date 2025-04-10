from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import reader_model
from app.models.currentReader import currentReader
from app.models.reader_model import Reader
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from datetime import datetime

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        birthdate = request.form['birthdate']
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
        gmail = request.form['gmail']
        gender = True if request.form['gender'] == 'male' else False
        nation = request.form['nation']
        phone = request.form['phone']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if the password and confirm password match
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('auth_routes.register'))

        # Hash the password before saving
        hashed_password = generate_password_hash(password)

        # Check if the username or email already exists
        existing_reader = Reader.query.filter((Reader.username == username) | (Reader.gmail == gmail)).first()
        if existing_reader:
            flash('Username or Email already exists!', 'danger')
            return redirect(url_for('auth_routes.register'))

        new_reader = Reader(full_name=full_name, birthdate=birthdate, gmail=gmail, gender=gender,
                            nation=nation, phone=phone, username=username, password=hashed_password, role=1)
        db.session.add(new_reader)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('auth_routes.login'))

    return render_template('auth/register.html')


# Route for login
@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form['identifier']  # This will be username, phone, or email
        password = request.form['password']

        # Check if the identifier is a phone number or email
        reader = Reader.query.filter(
            (Reader.username == identifier) |
            (Reader.phone == identifier) |
            (Reader.gmail == identifier)
        ).first()

        if reader:
            if reader.role == 4:
                flash('Your account has been blocked. Please contact support.', 'danger')
                return redirect(url_for('auth_routes.login'))

            if check_password_hash(reader.password, password):
                flash('Login successful!', 'success')
                currentReader.id = reader.id
                currentReader.role = reader.role
                return redirect(url_for('book_routes.list_books'))  # Change this to your homepage or dashboard
            else:
                flash('Incorrect password.', 'danger')
        else:
            flash('User not found.', 'danger')

    return render_template('auth/login.html')

# Route for forgot password
@auth_routes.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username_or_email = request.form['username_or_email']
        
        # For simplicity, we assume the user knows either their username or email
        reader = Reader.query.filter((Reader.username == username_or_email) | (Reader.gmail == username_or_email)).first()
        
        if reader:
            # Normally, you would send an email with a reset link here. 
            # Since we're keeping it simple, let's just flash a success message.
            flash(f'Password reset instructions sent to {reader.gmail}', 'info')
        else:
            flash('No account found with that username/email', 'danger')
        return redirect(url_for('auth_routes.login'))

    return render_template('auth/forgot_password.html')
