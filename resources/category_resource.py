from flask_restful import fields, marshal_with
from dao.category_dao import CategoryDao
from models.category import Category
from resources.base_resource import BaseResource


class CustomerResource(BaseResource):
    fields_base = {
        "id_": fields.Integer,
        "name": fields.String,
        "description": fields.String
    }

    def __init__(self):
        self.__dao = CategoryDao()
        self.__model_type = Category
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields_base)
    def get(self, id_: int = None):
        return super().get(id_)

    @marshal_with(fields_base)
    def post(self):
        return super().post()

    @marshal_with(fields_base)
    def put(self, id_: int):
        return super().put(id_)

    @marshal_with(fields_base)
    def delete(self, id_: int):
        return super().delete(id_)
