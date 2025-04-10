from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.repositories.reader_repo import ReaderRepository
import random  # Import the random module
import string  # Import the string module

reader_routes = Blueprint('reader_routes', __name__)
reader_repo = ReaderRepository()

# @reader_routes.route('/readers', methods=['GET'])
# def list_readers():
#     readers = reader_repo.get_all_readers()
#     return render_template('reader/reader_list.html', readers=readers)

@reader_routes.route('/readers', methods=['GET'])
def reader_list():
    page = request.args.get('page', 1, type=int)  # Get current page number from the URL, default to 1
    per_page = 10  # Number of users per page
    readers = reader_repo.getpaginated_readers(page, per_page)  # Query paginated results
    return render_template('reader/reader_list.html', readers=readers.items, pagination=readers)



@reader_routes.route('/readers/create', methods=['GET', 'POST'])
def create_reader():
    if request.method == 'POST':
        data = {
            'full_name': request.form['full_name'],
            'birthdate': request.form['birthdate'],
            'gmail': request.form['gmail'],
            'gender': request.form.get('gender') == 'true',
            'nation': request.form['nation'],
            'phone': request.form['phone'],
            'username': request.form['username'],
            'password': request.form['password'],
            'role': request.form['role']
        }
        reader_repo.add_reader(data)
        return redirect(url_for('reader_routes.reader_list'))
    return render_template('reader/reader_create.html')

@reader_routes.route('/readers/edit/<int:reader_id>', methods=['GET', 'POST'])
def update_reader(reader_id):
    reader = reader_repo.get_reader_by_id(reader_id)
    if not reader:
        return redirect(url_for('reader_routes.reader_list'))  # If reader not found, go back to list

    random_key = generate_random_key()

    if request.method == 'POST':
        # When using POST, just update the role
        role = request.form['role']
        data = {'role': role}  # Only update the role field
        reader_repo.update_reader(reader_id, data)  # Update the reader's role
        return redirect(url_for('reader_routes.reader_list'))  # Redirect to the reader list

    return render_template('reader/reader_edit.html', reader=reader, random_key=random_key)

def generate_random_key(length=6):
    """Generate a random alphanumeric key."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))



@reader_routes.route('/readers/delete/<int:reader_id>', methods=['GET'])
def delete_reader(reader_id):
    reader_repo.delete_reader(reader_id)
    return redirect(url_for('reader_routes.reader_list'))

@reader_routes.route('/readers/block/<int:reader_id>', methods=['GET'])
def toggle_block(reader_id):
    reader = reader_repo.get_reader_by_id(reader_id)
    if reader:
        # Toggle role: 4 = Blocked, 1 = User
        new_role = 1 if reader.role == 4 else 4
        reader_repo.update_reader(reader_id, {'role': new_role})
        flash(f"Reader {'unblocked' if new_role == 1 else 'blocked'} successfully.", "success")
    else:
        flash("Reader not found.", "danger")
    
    return redirect(url_for('reader_routes.reader_list'))
