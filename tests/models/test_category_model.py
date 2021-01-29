import sys
sys.path.append('.')


from models.category import Category
import pytest


def test_category_instance():
    category = Category('Name test', 'Description test')

    assert isinstance(category, Category)


def test_category_name_empty():
    with pytest.raises(ValueError):
        category = Category('', 'Description test')


def test_category_name_len():
    with pytest.raises(ValueError):
        category = Category('Name test' * 100, 'Description test')


def test_category_name_int():
    with pytest.raises(TypeError):
        category = Category(100, 'Description test')


def test_category_description_len():
    with pytest.raises(ValueError):
        category = Category('Name test', 'Description test' * 500)


def test_category_description_int():
    with pytest.raises(TypeError):
        category = Category('Name test', 10)