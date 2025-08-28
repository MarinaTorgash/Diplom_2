from json import loads
import requests
from allure import step
from data.handlers import Urls, Handlers


class UserMethods:

    @step('Регистрируем юзера')
    def register_user(self, params):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', json=params)
        return response.status_code, loads(response.text)


    @step('Логин пользвателя')
    def login_user(self, params):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', json=params)
        return response.status_code, loads(response.text)


    @step('обновляем данные пользователя')
    def update_user(self, params, token):
        response = requests.patch(f'{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}', json=params, headers={'Authorization': f'{token}'})
        return response.status_code, loads(response.text)


    @step('Удаляем юзера')
    def delete_user(self, token):
        response = requests.delete(f'{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}', headers={'Authorization': f'{token}'})
        return response.status_code, loads(response.text)


