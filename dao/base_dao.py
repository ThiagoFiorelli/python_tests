from models.base_model import BaseModel
from dao.session import Session


class BaseDao:
    def __init__(self, typemodel: object) -> None:
        self.__typemodel = typemodel

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__typemodel).order_by('id').all()
        return result

    def read_by_id(self, id_: int) -> BaseModel:
        with Session() as session:
            result = session.query(self.__typemodel).filter_by(id_=id_).first()
        return result

    def save(self, model: BaseModel) -> BaseModel:
        with Session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model

    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()
