from flask import Blueprint, render_template, request, redirect, url_for
from app.repositories.category_repo import CategoryRepository

category_routes = Blueprint('category_routes', __name__)
repo = CategoryRepository()

@category_routes.route('/categories')
def list_categories():
    categories = repo.get_all_categories()
    return render_template('category/list.html', categories=categories)

@category_routes.route('/categories/create', methods=['GET', 'POST'])
def create_category():
    if request.method == 'POST':
        data = {'name': request.form['name']}
        repo.add_category(data)
        return redirect(url_for('category_routes.list_categories'))
    return render_template('category/create.html')

@category_routes.route('/categories/edit/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    category = repo.get_category_by_id(id)
    if request.method == 'POST':
        data = {'name': request.form['name']}
        repo.update_category(id, data)
        return redirect(url_for('category_routes.list_categories'))
    return render_template('category/edit.html', category=category)

@category_routes.route('/categories/delete/<int:id>', methods=['GET'])
def delete_category(id):
    repo.delete_category(id)
    return redirect(url_for('category_routes.list_categories'))
