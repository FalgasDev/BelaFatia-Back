from config.database import app, db
from controllers.cake_controller import cake_blueprint
from controllers.costumer_controller import custumer_blueprint

app.register_blueprint(cake_blueprint)
app.register_blueprint(custumer_blueprint)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )
