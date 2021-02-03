import sys
sys.path.append('.')

import pytest
from models.category import Category
from controllers.base_controller import BaseController
from controllers.category_controller import CategoryController


@pytest.fixture
def create_model():
    category = Category('Naaame', 'Description')
    return category


@pytest.fixture
def create_controller():
    category_controller = CategoryController()
    return category_controller


def test_instance(create_controller):
    assert isinstance(create_controller, CategoryController)


def test_inheritance(create_controller):
    assert isinstance(create_controller, BaseController)


def test_save(create_controller, create_model):
    global model
    model = create_controller.create(create_model)
    assert model is create_model


def test_update(create_controller):
    model.name = 'Name'
    model_ = create_controller.update(model)
    assert model_.name == model.name


def test_read_all(create_controller):
    rows = create_controller.read_all()
    assert isinstance(rows, list)


def test_read_by_id(create_controller):
    model_ = create_controller.read_by_id(model.id_)
    assert model_ is not None


def test_delete(create_controller):
    create_controller.delete(model)
    model_ = create_controller.read_by_id(model.id_)
    assert model_ is None
