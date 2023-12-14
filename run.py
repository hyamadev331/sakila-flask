from __init__ import create_app
from config import Config
from route import routes

app = create_app()
app.register_blueprint(routes)
if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
