from json import loads
from allure import step
import requests

from data.handlers import Urls, Handlers


class IngredientsMethod:

    @step('Получаем список ингредиентов')
    def get_ingredients(self):
        response = requests.get(f'{Urls.MAIN_URL}{Handlers.INGREDIENTS}')
        return response.status_code, loads(response.text)