from src.controllers.dbconfig import connectionAWS
from flask import request, jsonify
from src.controllers.logging_setup import post_logger as lg


def test_tester_query():
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        cur.execute("Select first_name from valorant_employees where tier = 'gold'")
        x = cur.fetchall()
        return x
    finally:
        conn.close()


def check_credential(password, user):
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        cur.execute(""" SELECT employee_password, employee_username from valorant_employees where employee_password = ? and employee_username = ?
        """, password, user)
        x = cur.fetchall()
        return x
    finally:
        conn.close()


def grab_id(username):
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        cur.execute(""" SELECT employee_id from valorant_employees where employee_username = ?
        """, username)
        x = cur.fetchone()
        return x
    finally:
        conn.close()


def grab_managers():
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        cur.execute("Select employee_id from valorant_employees where ismanager = '1' order by employee_id asc")
        x = cur.fetchall()
        return x
    finally:
        conn.close()

def grab_managers_bool(username):
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        cur.execute("Select ismanager from valorant_employees where employee_username = ? ", username)
        x = cur.fetchall()
        return x
    finally:
        conn.close()