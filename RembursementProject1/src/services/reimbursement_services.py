from flask import request, jsonify
from src.controllers.logging_setup import post_logger as lg
from src.models.reimbursement_model import Reimbursement
from src.models.reimbursement_model import Economy
from src.models.reimbursement_model import Resubmit
from src.dao import reimbursement_dao as rdao


def get_all_reimbursement():
    reimbursements = rdao.find_all_reimbursements()

    x = {}

    for val in reimbursements:
        x[val[0]] = Reimbursement(val[0], val[1], str(val[2]), val[3], val[4], val[5], val[6], val[7])

    return x


def get_pending_reimbursement():
    reimbursements = rdao.find_all_reimbursements_pending()

    x = {}

    for val in reimbursements:
        x[val[0]] = Reimbursement(val[0], val[1], str(val[2]), val[3], val[4], val[5], val[6], val[7])

    return x


def get_denied_reimbursement():
    reimbursements = rdao.find_all_reimbursements_denied()

    x = {}

    for val in reimbursements:
        x[val[0]] = Reimbursement(val[0], val[1], str(val[2]), val[3], val[4], val[5], val[6], val[7])

    return x


def get_approved_reimbursement():
    reimbursements = rdao.find_all_reimbursements_approved()

    x = {}

    for val in reimbursements:
        x[val[0]] = Reimbursement(val[0], val[1], str(val[2]), val[3], val[4], val[5], val[6], val[7])

    return x


def get_all_reimbursement_specified(username):
    reimbursements = rdao.find_all_reimbursements_specified(username)

    x = {}

    for val in reimbursements:
        x[val[0]] = Reimbursement(val[0], val[1], str(val[2]), val[3], val[4], val[5], val[6], val[7])

    return x


def get_pending_reimbursement_specified(username):
    reimbursements = rdao.find_all_reimbursements_pending_specified(username)

    x = {}

    for val in reimbursements:
        x[val[0]] = Reimbursement(val[0], val[1], str(val[2]), val[3], val[4], val[5], val[6], val[7])

    return x


def get_denied_reimbursement_specified(username):
    reimbursements = rdao.find_all_reimbursements_denied_specified(username)

    x = {}

    for val in reimbursements:
        x[val[0]] = Reimbursement(val[0], val[1], str(val[2]), val[3], val[4], val[5], val[6], val[7])

    return x


def get_approved_reimbursement_specified(username):
    reimbursements = rdao.find_all_reimbursements_approved_specified(username)

    x = {}

    for val in reimbursements:
        x[val[0]] = Reimbursement(val[0], val[1], str(val[2]), val[3], val[4], val[5], val[6], val[7])

    return x


def get_most_eco():
    reimbursements = rdao.get_most_economy()

    x = {}

    for val in reimbursements:
        x[val[0]] = Economy(val[0], val[1], str(val[2]))

    return x


def get_most_reimbursements():
    reimbursements = rdao.get_most_reimbursements()

    x = {}

    for val in reimbursements:
        x[val[0]] = Resubmit(val[0], val[1], val[2])

    return x


def get_most_denied():
    reimbursements = rdao.get_most_denied()

    x = {}

    for val in reimbursements:
        x[val[0]] = Resubmit(val[0], val[1], val[2])

    return x


def create_reimbursement(agent_id, economy, purpose, manager_id):
    rdao.create_reimbursement(agent_id, economy, purpose, manager_id)


def update_status(reimbursement_id, status, purpose, manager_id):
    rdao.update_reimbursement(reimbursement_id, status, purpose, manager_id)
