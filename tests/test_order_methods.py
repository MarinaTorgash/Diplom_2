from json import loads
import allure

from data.handlers import ResponseStatusCode
from data.ingredients_data import  Ingredient
from helpers import is_valid_json
from methods.order_methods import OrderMethods
from orders_json_schemas import order_schema_unauthenticated, order_schema_authenticated


class TestOrderMethods:

    @allure.title('Тесты на создание ордера с авторизованным пользователем')
    def test_create_order_with_authorization(self, ingredients, user_login):
        order = OrderMethods()
        code, response = order.create_order({'ingredients': ingredients}, user_login)
        dict_response = loads(response)
        assert (code == ResponseStatusCode.SUCCESS_STATUS and dict_response['success'] == True
                and is_valid_json(instance=dict_response, schema=order_schema_authenticated))


    @allure.title('Тесты на создание ордера без авторизации')
    def test_create_order_without_authorization(self, ingredients):
        order = OrderMethods()
        code, response = order.create_order({'ingredients': ingredients}, token='')
        dict_response = loads(response)
        assert (code == ResponseStatusCode.SUCCESS_STATUS and dict_response['success'] == True
                and is_valid_json(instance=dict_response, schema=order_schema_unauthenticated))


    @allure.title('Тесты на создание ордера без ингредиентов')
    def test_create_order_without_ingredients(self):
        order = OrderMethods()
        code, response = order.create_order({'ingredients': []}, token='')
        assert code == ResponseStatusCode.BAD_REQUEST_STATUS and loads(response) == {
            "success": False,
            "message": "Ingredient ids must be provided"
        }

    @allure.title('Тесты на создание ордера с невалидным хэшем ингредиентов')
    def test_create_order_with_invalid_ingredients(self):
        order = OrderMethods()
        code, response = order.create_order({'ingredients': Ingredient.incorrect_ingredients_data}, token='')
        assert code == ResponseStatusCode.BAD_REQUEST_STATUS


    @allure.title('Тесты на получение списка ордеров по юзеру без авторизации')
    def test_get_list_user_orders_without_authorization(self):
        order = OrderMethods()
        code, response = order.get_list_user_orders(token='')
        assert code == ResponseStatusCode.UNAUTHORIZED_STATUS and response == {
            "success": False,
            "message": "You should be authorised"
        }

    @allure.title('Тесты на получение списка ордеров по юзеру с авторизацией')
    def test_get_list_user_orders_with_authorization(self, user_login):
        order = OrderMethods()
        code, response = order.get_list_user_orders(user_login)

        print("Код ответа при логине:", code)
        print("Тело ответа при логине:", response)

        type_order_field = type(response['orders'])
        assert code == ResponseStatusCode.SUCCESS_STATUS and response['success'] == True and type_order_field == list

