import unittest
from unittest import mock
from src.controllers.dbconfig import connectionAWS
from src.controllers import dbconfig
from pyodbc import connect


def mock_connection():
    test_connect = connect("DRIVER=PostgreSQL UNICODE(x64); SERVER=localhost; PORT=5432; DATABASE=postgres; "
                           "UID=postgres; PWD=postgres")
    dbconfig.get_connection = mock.Mock(return_value=test_connect)


def test_get_all_reimbursements():
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute("Select * from test_valorant_reimbursements")
    x = cur.fetchall()
    return x

def test_get_all_reimbursements_pending():
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute("Select count(status) from test_valorant_reimbursements where status = 'pending'")
    x = cur.fetchone()
    return x

def test_get_all_reimbursements_approved():
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute("Select count(status) from test_valorant_reimbursements where status = 'approved'")
    x = cur.fetchone()
    return x

def test_get_all_reimbursements_denied():
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute("Select count(status) from test_valorant_reimbursements where status = 'denied'")
    x = cur.fetchone()
    return x

def test_find_all_users_specified(user):
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute("select agent_id from test_valorant_reimbursements where agent_id = ?", user)
    x = cur.fetchone()
    return x

def test_find_all_users_specified_pending(user):
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute(
        "Select count(status) from test_valorant_reimbursements where status = 'pending' and agent_id = ?",
        user)
    x = cur.fetchone()
    return x

def test_find_all_users_specified_approved(user):
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute(
        "Select count(status) from test_valorant_reimbursements where status = 'approved' and agent_id = ?",
        user)
    x = cur.fetchone()
    return x

def test_find_all_users_specified_denied(user):
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute(
        "Select count(status) from test_valorant_reimbursements where status = 'denied' and agent_id = ?",
        user)
    x = cur.fetchone()
    return x

def test_get_most_eco():
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute("""select first_name, last_name, sum(r.economy) economy from test_valorant_employees c join 
           test_valorant_reimbursements r
               on c.employee_id = r.agent_id group by first_name, last_name order by economy DESC
           """)
    x = cur.fetchone()
    return x

def test_get_most_denied():
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute("""select first_name, last_name, count(status) submissions from test_valorant_employees c join
    test_valorant_reimbursements r on c.employee_id = r.agent_id where status = 'denied'
     group by first_name, last_name order by submissions DESC
    """)
    x = cur.fetchone()
    return x

def test_get_most_approved():
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute("""select first_name, last_name, count(status) submissions from test_valorant_employees c join
    test_valorant_reimbursements r on c.employee_id = r.agent_id where status = 'approved'
     group by first_name, last_name order by submissions DESC
    """)
    x = cur.fetchone()
    return x

def test_insert_reimbursements(agent_id):
    mock_connection()
    conn = dbconfig.get_connection()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO test_valorant_reimbursements (reimbursement_id, agent_id, economy, purpose, transaction_time, 
        status) 
        VALUES (default, ?, 2500, 'weapons', default, default)""", agent_id)
    conn.commit()
