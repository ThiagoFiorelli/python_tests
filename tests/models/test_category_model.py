import sys
sys.path.append('.')
import re
from models.category import Category


name_ = 'Bar'
description_ = 'Bar com petiscos, bebidas, jogos e apostas'
obj_ = Category(name_, description_)

def test_category_model_instace():
    assert isinstance(obj_, Category), 'Category must be a Category instance'

def test_category_model_types():
    assert isinstance(obj_.name, str), 'Name must be a string'
    assert isinstance(obj_.description, str), 'Description must be a string'

def test_category_model_values():
    assert obj_.name == name_, 'Category name must match the name entered'
    assert obj_.description == description_, 'Category name must match the description entered'
    assert obj_.name != '' and obj_.name is not None, 'Category name cannot be empty'
    assert len(obj_.name) <= 100, 'Name must be 100 or less characters'
    assert re.match(r'^[a-zà-úA-ZÀ-Ú0-9,. ]+$', obj_.name), 'Name cannot have special characters!'
    assert len(obj_.description) <= 255, 'Description must be 255 or less characters!'

def test_category_model_name_type_exception():
    try:
        obj = Category(0, description_)
        raise NotImplementedError('Exception not raised!')
    except Exception as e:
        assert isinstance(e, TypeError), 'The exception must be of type TypeError'
        assert e.args == ('Name must be a string!',), 'The exception message does not match'

def test_category_model_empty_name_exception():
    try:
        obj = Category('', description_)
        raise NotImplementedError('Exception not raised!')
    except Exception as e:
        assert isinstance(e, ValueError), 'The exception must be of type ValueError'
        assert e.args == ('Name cannot be empty!',), 'The exception message does not match'

def test_category_model_special_character_in_name_exception():
    try:
        obj = Category('@', description_)
        raise NotImplementedError('Exception not raised!')
    except ValueError as e:
        assert isinstance(e, ValueError), 'The exception must be of type ValueError'
        assert e.args == ('Name cannot have special characters!',), 'The exception message does not match'

def test_category_model_name_lenght_exception():
    try:
        obj = Category('n' * 101, description_)
        raise NotImplementedError('Exception not raised!')
    except ValueError as e:
        assert isinstance(e, ValueError), 'The exception must be of type ValueError'
        assert e.args == ('Name must be 100 or less characters!',), 'The exception message does not match'

def test_category_model_description_type_exception():
    try:
        obj = Category(name_, 0)
        raise NotImplementedError('Exception not raised!')
    except Exception as e:
        assert isinstance(e, TypeError), 'The exception must be of type TypeError'
        assert e.args == ('Description must be a string!',), 'The exception message does not match'

def test_category_model_description_lenght_exception():
    try:
        obj = Category(name_, 'n' * 256)
        raise NotImplementedError('Exception not raised!')
    except ValueError as e:
        assert isinstance(e, ValueError), 'The exception must be of type ValueError'
        assert e.args == ('Description must be 255 or less characters!',), 'The exception message does not match'