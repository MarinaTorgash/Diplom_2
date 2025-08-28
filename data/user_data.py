class User:
    data_correct = {
        "email": 'test_diplom@yandex.ru',
        "password": "test_diplom@yandex.ru"
    }
    data_correct_full = {
        "email": 'test_diplom@yandex.ru',
        "password": "test_diplom@yandex.ru",
        "name": "test_diplom"
    }

    data_negative = {
        "email": 'test_diplom222222@yandex.ru',
        "password": "password"}

    data_double = {
        "email": 'test_diplom@yandex.ru',
        "password": "password",
        "name": "Username"}

    data_without_email = {
        "email": '',
        "password": "password",
        "name": "Username"}

    data_without_password = {
        "email": 'test_diplom@yandex.ru',
        "password": "",
        "name": "Username"}

    data_without_name = {
        "email": 'test_diplom@yandex.ru',
        "password": "password",
        "name": ""}

    data_updated_email = {
         "email": "test_diplo3333m@yandex.ru"}

    data_updated_name= {
         "name": "test_diplom123123"}