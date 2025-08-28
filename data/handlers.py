class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'


class Handlers:
    CREATE_USER = '/api/auth/register'
    LOGIN = '/api/auth/login'
    CHANGE_USER_DATA = '/api/auth/user'
    DELETE_USER = '/api/auth/user'
    MAKE_ORDER = '/api/orders'
    GET_ORDERS = '/api/orders'
    GET_ORDERS = '/api/orders'
    INGREDIENTS = '/api/ingredients'
    headers = {"Content-Type": "application/json"}

class ResponseStatusCode:
    SUCCESS_STATUS = 200
    FORBIDDEN_STATUS = 403
    UNAUTHORIZED_STATUS = 401
    BAD_REQUEST_STATUS = 400
    SERVER_ERROR_STATUS = 500
