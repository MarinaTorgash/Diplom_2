import random
import string
from jsonschema import validate, ValidationError

def is_valid_json(instance: dict, schema: dict) -> bool:
    try:
        validate(instance=instance, schema=schema)
        return True
    except ValidationError:
        return False


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['example.com', 'testmail.com', 'mail.io'])
    return f"{username}@{domain}"

def generate_random_name():
    return ''.join(random.choices(string.ascii_letters, k=6)).capitalize()

def data_for_user():
    return {
        "email": generate_random_email(),
        "name": generate_random_name(),
        "password": "TestPass123!"
    }
