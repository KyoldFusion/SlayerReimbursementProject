from src.controllers.logging_setup import post_logger as lg
from flask import request, render_template, redirect, session
from src.controllers.FlaskConfigs import app
from src.services import reimbursement_services as rservice
from src.services import employee_services as eservice
import json
from src.models.reimbursement_model import *


@app.route('/')
def landing():
    return redirect('/login')


@app.route('/logout')
def logout():
    session.pop("user", None)
    lg.info("successfully logged out")
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        content = request.get_json()
        username = content["username"]
        password = content['password']
        check_user = eservice.grab_id(str(username))
        session["agent_id"] = check_user
        session["ismanager"] = eservice.grab_managers_specify(str(username))
        session.permanent = False
        x = eservice.credentials_pass(password, username)
        lg.info("successfully passed valid credentials")
        return x
    else:
        return render_template('login.html')


@app.route('/index')
def home():
    if session.get('agent_id'):
        if session["agent_id"] and session["ismanager"][0] == "1":
            lg.info(str(session["agent_id"]) + " is a manager.")
            # my_var = session.get("user", None)
            return render_template('index.html')
        if session["agent_id"] and session["ismanager"][0] == "0":
            lg.info(str(session["agent_id"])+ "is not a manager.")
            return render_template('index_employee.html')
    else:
        return redirect('/login')


@app.route('/statistics')
def statistics():
    if session.get('agent_id'):
        if session["agent_id"]:
            # my_var = session.get("user", None)
            return render_template('statistics.html')
    else:
        return redirect('/login')


@app.route('/pending', methods=['GET', 'POST'])
def pending_request():
    if session.get('agent_id'):
        if session["agent_id"] and session["ismanager"][0] == "1":
            if request.method == 'POST':
                try:
                    reimbursement_id = request.form.get("ReimbursementID")
                    manager_id = session["agent_id"][0]
                    purpose = request.form.get("purpose")
                    if request.form['submit-button'] == "approved":
                        status = "approved"
                    if request.form['submit-button'] == "denied":
                        status = "denied"
                    if request.form['submit-button'] == "pending":
                        status = "pending"
                    rservice.update_status(reimbursement_id, status, purpose, manager_id)
                    return redirect('/pending')
                except:
                    return redirect('/pending')

            else:
                return render_template('Pending_Request.html')

        if session["agent_id"] and session["ismanager"][0] == "0":
            return render_template('Pending_Request_Employee.html')
    else:
        return redirect('/login')


@app.route('/All_Reimbursements_Table')
def all_reimbursements_table():
    if session.get('agent_id'):
        if session["agent_id"] and session["ismanager"][0] == "1":
            data = rservice.get_all_reimbursement()
            t = json.dumps(data, cls=reimbursementEncoder)
            lg.info("data successfully converted to json")
            return t
        if session["agent_id"] and session["ismanager"][0] == "0":
            x = session["agent_id"]
            data = rservice.get_all_reimbursement_specified(x)
            t = json.dumps(data, cls=reimbursementEncoder)
            lg.info("data successfully converted to json")
            return t


@app.route('/Pending_Table')
def pending_table():
    if session.get('agent_id'):
        if session["agent_id"] and session["ismanager"][0] == "1":
            data = rservice.get_pending_reimbursement()
            t = json.dumps(data, cls=reimbursementEncoder)
            lg.info("data successfully converted to json")
            return t
        if session["agent_id"] and session["ismanager"][0] == "0":
            x = session["agent_id"]
            data = rservice.get_pending_reimbursement_specified(x)
            t = json.dumps(data, cls=reimbursementEncoder)
            lg.info("data successfully converted to json")
            return t


@app.route('/Approved_Table')
def approved_table():
    if session.get('agent_id'):
        if session["agent_id"] and session["ismanager"][0] == "1":
            data = rservice.get_approved_reimbursement()
            t = json.dumps(data, cls=reimbursementEncoder)
            lg.info("data successfully converted to json")
            return t

        if session["agent_id"] and session["ismanager"][0] == "0":
            x = session["agent_id"]
            data = rservice.get_approved_reimbursement_specified(x)
            t = json.dumps(data, cls=reimbursementEncoder)
            lg.info("data successfully converted to json")
            return t


@app.route('/Denied_Table')
def denied_table():
    if session.get('agent_id'):
        if session["agent_id"] and session["ismanager"][0] == "1":
            data = rservice.get_denied_reimbursement()
            t = json.dumps(data, cls=reimbursementEncoder)
            lg.info("data successfully converted to json")
            return t
        if session["agent_id"] and session["ismanager"][0] == "0":
            x = session["agent_id"]
            data = rservice.get_denied_reimbursement_specified(x)
            t = json.dumps(data, cls=reimbursementEncoder)
            lg.info("data successfully converted to json")
            return t


@app.route('/Most_Spent')
def most_spent_table():
    if session.get('agent_id'):
        if session["agent_id"] and session["ismanager"][0] == "1":
            data = rservice.get_most_eco()
            t = json.dumps(data, cls=economyEncoder)
            lg.info("data successfully converted to json")
            return t


@app.route('/Most_Requested')
def most_requested():
    if session.get('agent_id'):
        if session["agent_id"] and session["ismanager"][0] == "1":
            data = rservice.get_most_reimbursements()
            t = json.dumps(data, cls=resubmitEncoder)
            lg.info("data successfully converted to json")
            return t


@app.route('/Most_Denied')
def most_denied():
    if session.get('agent_id'):
        if session["agent_id"] and session["ismanager"][0] == "1":
            data = rservice.get_most_denied()
            t = json.dumps(data, cls=resubmitEncoder)
            lg.info("data successfully converted to json")
            return t


@app.route('/submit_request', methods=['GET', 'POST'])
def submit_request():
    if session.get('agent_id'):
        if session["agent_id"] and session["ismanager"][0] == "1":
            if request.method == 'POST':
                try:
                    agent_id = session["agent_id"][0]
                    economy = request.form.get("economy")
                    purpose = request.form.get("purpose")
                    manager_id = request.form.get("manager_id")
                    rservice.create_reimbursement(agent_id, economy, purpose, manager_id)
                    lg.info("successfully submitted reimbursements")
                    return redirect('/submit_request')
                except:
                    return redirect('/submit_request')
            else:
                return render_template('Submit_Request.html')

        if session["agent_id"] and session["ismanager"][0] == "0":
            if request.method == 'POST':
                try:
                    agent_id = session["agent_id"][0]
                    economy = request.form.get("economy")
                    purpose = request.form.get("purpose")
                    manager_id = request.form.get("manager_id")
                    rservice.create_reimbursement(agent_id, economy, purpose, manager_id)
                    lg.info("successfully submitted reimbursements")
                    return redirect('/submit_request')
                except:
                    return redirect('/submit_request')
            else:
                return render_template('Submit_Request_Employee.html')
    else:
        return redirect('/login')


@app.route('/valid_managers')
def valid_managers():
    data = eservice.grab_managers()
    t = {"employee_id": data}
    lg.info("successfully converted data to JSON")
    return t
