from src.controllers.FlaskConfigs import app as flask
import src.controllers.routing_controller

if __name__ == '__main__':
    flask.run(debug=True)