from flask import Blueprint, render_template, request, redirect, url_for
from app.repositories.test_repo import TestRepository
# Create a Blueprint for test routes
test_routes = Blueprint('test_routes', __name__)

# Initialize TestRepository
test_repo = TestRepository()

@test_routes.route('/tests', methods=['GET'])
def list_tests():
    tests = test_repo.get_all_tests()
    return render_template('test/test_list.html', tests=tests)

@test_routes.route('/tests/create', methods=['GET', 'POST'])
def create_test():
    if request.method == 'POST':
        test_data = {
            'name': request.form['name']
        }
        test_repo.add_test(test_data)
        return redirect(url_for('test_routes.list_tests'))
    return render_template('test/test_create.html')

@test_routes.route('/tests/edit/<int:test_id>', methods=['GET', 'POST'])
def edit_test(test_id):
    test = test_repo.get_test_by_id(test_id)
    if not test:
        return redirect(url_for('test_routes.list_tests'))  # If test not found, go back to list

    if request.method == 'POST':
        test_data = {
            'name': request.form['name']
        }
        test_repo.update_test(test_id, test_data)
        return redirect(url_for('test_routes.list_tests'))

    return render_template('test/test_edit.html', test=test)

@test_routes.route('/tests/delete/<int:test_id>', methods=['GET'])
def delete_test(test_id):
    test_repo.delete_test(test_id)
    return redirect(url_for('test_routes.list_tests'))
