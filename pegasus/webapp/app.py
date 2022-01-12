from flask import Flask, g
from pegasus.webapp.equity.views import grants


app = Flask(__name__)
app.register_blueprint(grants)
app.config["SECRET_KEY"] = "asjdahfsiahfa 0u    t aihgpiwdN"


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
