import sys
sys.path.append('.')
from flask import Flask, render_template, request, redirect
from controllers.category_controller import CategoryController
from models.category import Category


app = Flask(__name__)
category_controller_ = CategoryController()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/categories')
def category():
    categories = category_controller_.read_all()
    return render_template('categories.html', categories = categories)


@app.route('/category/create', methods=['GET','POST'])
def create_category():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        category = Category(name, description)
        category_controller_.create(category)
        return redirect('/categories')
    return render_template('create_category.html')


@app.route('/category/update/<int:id_>', methods=['GET', 'POST'])
def update_category(id_):
    category = category_controller_.read_by_id(id_)
    if request.method == 'POST':
        category.name = request.form.get('name')
        category.description = request.form.get('description')
        category_controller_.update(category)
        return redirect('/categories')
    return render_template('create_category.html', category = category, update = True)


@app.route('/category/delete/<int:id_>')
def delete_category(id_):
    category = category_controller_.read_by_id(id_)
    category_controller_.delete(category)
    return redirect('/categories')


app.run(debug=True)
