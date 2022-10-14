import os

from app import app

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    PORT = int(os.environ.get('SERVER_PORT', '5000'))
    app.debug = True
    app.run(HOST, PORT)
