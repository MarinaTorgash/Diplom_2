import allure
import pytest

from helpers import data_for_user
from data.user_data import User
from data.handlers import ResponseStatusCode


class TestUserMethods:

    @allure.title("Тесты на успешную регистрацию пользователя")
    def test_register_user_success(self, user_methods):
        data = data_for_user()
        code, response = user_methods.register_user(data)
        expected = {
            "user": {
                "email": data["email"],
                "name": data["name"],
            }
        }
        assert (
            code == ResponseStatusCode.SUCCESS_STATUS
            and expected["user"].items() == response["user"].items()
            and "accessToken" in response
            and "refreshToken" in response
        )

    @allure.title("Тесты на регистрацию существующего пользователя")
    def test_register_exists_user(self, user, user_methods):
        code, response = user_methods.register_user(User.data_correct_full)
        assert code == 403 and response == {
            "success": False,
            "message": "User already exists",
        }

    @pytest.mark.parametrize(
        "data",
        [
            User.data_without_name,
            User.data_without_password,
            User.data_without_email,
        ],
    )
    def test_register_user_without_one_field(self, user_methods, data):
        allure.dynamic.title("Тестируем регистрацию без одного обязательного поля")
        code, response = user_methods.register_user(data)
        assert code == ResponseStatusCode.FORBIDDEN_STATUS and response == {
            "success": False,
            "message": "Email, password and name are required fields",
        }

    @allure.title("Тесты на успешный логин")
    def test_login_user_success(self, user, user_methods):
        code, response = user_methods.login_user(User.data_correct_full)
        assert (
            code == ResponseStatusCode.SUCCESS_STATUS
            and "accessToken" in response
            and "refreshToken" in response
        )

    @pytest.mark.parametrize(
        "data",
        [
            User.data_without_password,
            User.data_without_email,
        ],
    )
    def test_login_with_invalid_data(self, user, user_methods, data):
        allure.dynamic.title("Тестируем логин без одного обязательного поля")
        code, response = user_methods.login_user(data)
        assert code == ResponseStatusCode.UNAUTHORIZED_STATUS and response == {
            "success": False,
            "message": "email or password are incorrect",
        }

    @pytest.mark.parametrize(
        "data",
        [
            User.data_updated_email,
            User.data_updated_name,
        ],
    )
    def test_update_user_with_authorization(self, user, user_methods, data):
        allure.dynamic.title("Тестируем редактирование юзера с авторизацией")
        code, response = user_methods.update_user(data, user["access_token"])
        key = list(data.keys())[0]
        assert (
            code == ResponseStatusCode.SUCCESS_STATUS
            and response["user"][key] == data[key]
        )

    @pytest.mark.parametrize(
        "data",
        [
            User.data_updated_email,
            User.data_updated_name,
        ],
    )
    def test_update_user_without_authorization(self, user_methods, data):
        allure.dynamic.title("Тестируем редактирование юзера без авторизации")
        code, response = user_methods.update_user(data, token="")
        assert code == ResponseStatusCode.UNAUTHORIZED_STATUS and response == {
            "success": False,
            "message": "You should be authorised",
        }
