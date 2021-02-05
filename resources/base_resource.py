from flask import request
from flask_restful import Resource
from typing import Type
from dao.base_dao import BaseDao


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: Type):
        self.__model_type = model_type
        self.__dao = dao

    def get(self, id_: int = None):
        if id_:
            return self.__dao.read_by_id(id_)
        return self.__dao.read_all()

    def post(self) -> None:
        data = request.json
        item = self.__model_type(**data)
        self.__dao.save(item)
        return item, 201

    def put(self, id_: int):
        data = request.json
        if data['id_'] == id_:
            item = self.__dao.read_by_id(id_)
            if item:
                for key, value in data.items():
                    setattr(item, key, value)
                return self.__dao.save(item), 201
        return None, 404

    def delete(self, id_: int):
        item = self.__dao.read_by_id(id_)
        if item:
            self.__dao.delete(item)
            return None, 204
        return None, 404