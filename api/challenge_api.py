from flask import Blueprint, request
from werkzeug.exceptions import abort

from controller import math as math_controller

version = 'v1'
challenge_blueprint = Blueprint('challenge_blueprint', __name__)


@challenge_blueprint.route(f'/{version}/sum/')
def math_sum():
    try:
        a = request.args.get('a', 1)
        b = request.args.get('b', 2)
        result = math_controller.sum_values(int(a), int(b))
        return f'Sum of {a}+{b} is: {result}'
    except ValueError:
        return abort(400)
    except Exception as Ex:
        raise


