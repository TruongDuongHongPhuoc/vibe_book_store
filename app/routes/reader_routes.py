from flask import Blueprint, request, render_template, redirect, url_for
from app.repositories.reader_repo import ReaderRepository

reader_routes = Blueprint('reader_routes', __name__)
reader_repo = ReaderRepository()

@reader_routes.route('/readers', methods=['GET'])
def list_readers():
    readers = reader_repo.get_all_readers()
    return render_template('reader/reader_list.html', readers=readers)

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
        return redirect(url_for('reader_routes.list_readers'))
    return render_template('reader/reader_create.html')

@reader_routes.route('/readers/edit/<int:reader_id>', methods=['GET', 'POST'])
def edit_reader(reader_id):
    reader = reader_repo.get_reader_by_id(reader_id)
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
        reader_repo.update_reader(reader_id, data)
        return redirect(url_for('reader_routes.list_readers'))
    return render_template('reader/reader_edit.html', reader=reader)

@reader_routes.route('/readers/delete/<int:reader_id>', methods=['GET'])
def delete_reader(reader_id):
    reader_repo.delete_reader(reader_id)
    return redirect(url_for('reader_routes.list_readers'))
