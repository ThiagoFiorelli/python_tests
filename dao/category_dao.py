from models.category import Category
from dao.base_dao import BaseDao


class CategoryDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Category)
