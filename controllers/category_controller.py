from dao.category_dao import CategoryDao
from controllers.base_controller import BaseController


class CategoryController(BaseController):
    def __init__(self) -> None:
        super().__init__(CategoryDao())
