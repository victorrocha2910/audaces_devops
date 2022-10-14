from flask import Flask

from api.challenge_api import challenge_blueprint

app = Flask(__name__)
app.register_blueprint(challenge_blueprint, url_prefix='/api')
