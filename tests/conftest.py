import random

import pytest

from data.user_data import User
from methods.ingredients_methods import IngredientsMethod
from methods.user_methods import UserMethods

@pytest.fixture
def user():
    user = UserMethods()
    code, response = user.register_user(User.data_correct_full)
    yield response
    status, response_login = user.login_user(User.data_correct_full)
    user.delete_user(response_login['accessToken'])


@pytest.fixture
def user_login():
    user = UserMethods()
    _response = user.register_user(User.data_correct_full)
    code, response = user.login_user(User.data_correct_full)
    yield response['accessToken']
    user.delete_user(response['accessToken'])


@pytest.fixture
def ingredients():
    ingredients = IngredientsMethod()
    code, response = ingredients.get_ingredients()
    all_ids = [item["_id"] for item in response["data"][1:3]]
    return all_ids