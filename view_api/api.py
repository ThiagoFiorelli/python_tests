import sys
sys.path.append('.')
from flask import Flask
from flask_restful import Api
from resources.category_resource import CustomerResource


app = Flask(__name__)
api = Api(app)
api.add_resource(CustomerResource, '/api/category', endpoint='categories')
api.add_resource(CustomerResource, '/api/category/<int:id_>', endpoint='category')


@app.route('/')
def index():
    return 'Bem Vindo!'


app.run(debug=True)
