
from flask import Flask
from logging import FileHandler, INFO
from flask_session import Session
from flask_cors import CORS
from datetime import timedelta
from src.controllers.logging_setup import post_logger as lg


app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.secret_key = "valorant"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_USE_SIGNER"] = True
app.permanent_session_lifetime = timedelta(minutes=5)
file_handler = FileHandler('ReinbursementLogs.txt')
file_handler.setLevel(INFO)
app.logger.addHandler(file_handler)
Session(app)
CORS(app)
