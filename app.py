from flask import Flask, render_template
# from controllers.distilleries_controller import distilleries_blueprint
from controllers.whiskies_controller import whiskies_blueprint
# from controllers.users_controller import users_blueprint
# from controllers.reviews_controller import reviews_blueprint

app = Flask(__name__)

# app.register_blueprint(distilleries_blueprint)
app.register_blueprint(whiskies_blueprint)
# app.register_blueprint(users_blueprint)
# app.register_blueprint(reviews_blueprint)

@app.route("/")
def main():
     return render_template("index.html")

if __name__ == "__main__":
    app.run()