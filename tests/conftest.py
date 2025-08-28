import pytest

from data.user_data import User
from methods.ingredients_methods import IngredientsMethod
from methods.user_methods import UserMethods

@pytest.fixture
def user():
    user = UserMethods()
    code, response = user.register_user(User.data_correct_full)
    status, response_login = user.login_user(User.data_correct_full)

    yield {
        "register_response": response,
        "login_response": response_login,
        "access_token": response_login["accessToken"]
    }

    user.delete_user(response_login["accessToken"])

@pytest.fixture
def user_methods():
    return UserMethods()


@pytest.fixture
def ingredients():
    ingredients = IngredientsMethod()
    code, response = ingredients.get_ingredients()
    all_ids = [item["_id"] for item in response["data"][1:3]]
    return all_ids