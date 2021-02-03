import sys
sys.path.append('.')

import pytest
from models.category import Category
from dao.base_dao import BaseDao
from dao.category_dao import CategoryDao


@pytest.fixture
def create_model():
    category = Category('Name', 'Description')
    return category


@pytest.fixture
def create_dao():
    category_dao = CategoryDao()
    return category_dao


def test_instance(create_dao):
    assert isinstance(create_dao, CategoryDao)


def test_inheritance(create_dao):
    assert isinstance(create_dao, BaseDao)


def test_save(create_dao, create_model):
    global model
    model = create_dao.save(create_model)
    assert model is create_model


def test_read_all(create_dao):
    rows = create_dao.read_all()
    assert isinstance(rows, list)


def test_read_by_id(create_dao):
    model_ = create_dao.read_by_id(model.id_)
    assert model_ is not None


def test_delete(create_dao):
    create_dao.delete(model)
    model_ = create_dao.read_by_id(model.id_)
    assert model_ is None
