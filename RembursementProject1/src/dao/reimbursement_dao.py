from src.controllers.dbconfig import connectionAWS
from src.controllers.logging_setup import post_logger as lg


def find_all_reimbursements():
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute("Select * from valorant_reimbursements order by reimbursement_id")
        x = cur.fetchall()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def find_all_reimbursements_pending():
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute("Select * from valorant_reimbursements where status = 'pending' order by reimbursement_id")
        x = cur.fetchall()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def find_all_reimbursements_approved():
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute("Select * from valorant_reimbursements where status = 'approved' order by reimbursement_id")
        x = cur.fetchall()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def find_all_reimbursements_denied():
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute("Select * from valorant_reimbursements where status = 'denied' order by reimbursement_id")
        x = cur.fetchall()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def find_all_reimbursements_specified(user):
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute("Select * from valorant_reimbursements where agent_id = ? order by reimbursement_id", user)
        x = cur.fetchall()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def find_all_reimbursements_pending_specified(user):
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute(
            "Select * from valorant_reimbursements where status = 'pending' and agent_id = ? order by reimbursement_id",
            user)
        x = cur.fetchall()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def find_all_reimbursements_approved_specified(user):
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute(
            "Select * from valorant_reimbursements where"
            " status = 'approved' and agent_id = ? order by reimbursement_id",
            user)
        x = cur.fetchall()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def find_all_reimbursements_denied_specified(user):
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute(
            "Select * from valorant_reimbursements where status = 'denied' and agent_id = ? order by reimbursement_id",
            user)
        x = cur.fetchall()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def create_reimbursement(agent_id, economy, purpose, manager_id):
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute("INSERT INTO valorant_reimbursements (economy, purpose, agent_id, manager_id) "
                    "VALUES (?, ?, ?, ?)", economy, purpose, agent_id, manager_id)
        cur.commit()
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def find_reimbursements(reimbursement_id):
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute("Select * from valorant_reimbursements where reimbursement_id = ?", reimbursement_id)
        x = cur.fetchone()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def update_reimbursement(reimbursement_id, status, purpose, manager_id):
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute(
            "UPDATE valorant_reimbursements SET status = ?, manager_id = ?, approval_reason = ? WHERE "
            "reimbursement_id = ?",
            status, manager_id, purpose, reimbursement_id)
        cur.commit()
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def get_most_economy():
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute("""select first_name, last_name, sum(r.economy) economy from valorant_employees c join 
        valorant_reimbursements r
            on c.employee_id = r.agent_id group by first_name, last_name order by economy DESC
        """)
        x = cur.fetchall()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def get_most_denied():
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully closed connection to database!')
        cur.execute("""select first_name, last_name, count(status) submissions from valorant_employees c join
        valorant_reimbursements r on c.employee_id = r.agent_id where status = 'denied'
         group by first_name, last_name order by submissions DESC
        """)
        x = cur.fetchall()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')


def get_most_reimbursements():
    try:
        conn = connectionAWS()
        cur = conn.cursor()
        lg.info('Successfully connected to database!')
        cur.execute("""select first_name, last_name, count(agent_id) submissions from valorant_employees c 
        join valorant_reimbursements r on c.employee_id = r.agent_id group by
         first_name, last_name order by submissions DESC
        """)
        x = cur.fetchall()
        return x
    finally:
        conn.close()
        lg.info('Successfully closed connection to database!')
