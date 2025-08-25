from json import loads
from allure import step
import requests

from data.handlers import Urls, Handlers


class OrderMethods:

    @step('Создаем ордер')
    def create_order(self, params, token):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.MAKE_ORDER}', json=params, headers={'Authorization': f'{token}'})
        return response.status_code, response.text


    @step('Получаем список ордеров по юзеру')
    def get_list_user_orders(self,token):
        response = requests.get(f'{Urls.MAIN_URL}{Handlers.MAKE_ORDER}', headers={'Authorization': f'{token}'})
        return response.status_code, loads(response.text)