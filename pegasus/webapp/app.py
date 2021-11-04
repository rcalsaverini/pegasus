from flask import Flask, g
from pegasus.webapp.views import grants


app = Flask(__name__)
app.register_blueprint(grants)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
