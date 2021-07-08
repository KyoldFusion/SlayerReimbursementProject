import unittest
from unittest import mock
import dao_mock_testing_functions as dmock
from src.controllers import dbconfig
from pyodbc import connect


def mock_connection():
    test_connect = connect("DRIVER=PostgreSQL UNICODE(x64); SERVER=localhost; PORT=5432; DATABASE=postgres; "
                           "UID=postgres; PWD=postgres")
    dbconfig.get_connection = mock.Mock(return_value=test_connect)


class employee_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_submit_reimbursements(self):
        mock_connection()
        testing_result = dmock.test_insert_reimbursements(2)
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("Select * from test_valorant_reimbursements WHERE reimbursement_id = 1")
        c = cur.fetchone()
        self.assertEqual(testing_result, c)

    def test_get_all_reimbursements(self):
        mock_connection()
        testing_result = dmock.test_get_all_reimbursements()
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("Select * from test_valorant_reimbursements")
        c = cur.fetchall()
        self.assertEqual(testing_result, c)

    def test_find_pending(self):
        mock_connection()
        testing_result = dmock.test_get_all_reimbursements_pending()
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("Select COUNT(status) from test_valorant_reimbursements WHERE status = 'pending'")
        c = cur.fetchone()
        self.assertEqual(testing_result[0], c[0])

    def test_find_approved(self):
        mock_connection()
        testing_result = dmock.test_get_all_reimbursements_approved()
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("Select COUNT(status) from test_valorant_reimbursements WHERE status = 'approved'")
        c = cur.fetchone()
        self.assertEqual(testing_result[0], c[0])

    def test_find_denied(self):
        mock_connection()
        testing_result = dmock.test_get_all_reimbursements_denied()
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("Select COUNT(status) from test_valorant_reimbursements WHERE status = 'denied'")
        c = cur.fetchone()
        self.assertEqual(testing_result[0], c[0])

    def test_find_specific_user(self):
        mock_connection()
        testing_result = dmock.test_find_all_users_specified(2)
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("Select agent_id from test_valorant_reimbursements where agent_id = 2")
        c = cur.fetchone()
        self.assertEqual(testing_result, c)

    def test_find_specified_approved(self):
        mock_connection()
        testing_result = dmock.test_find_all_users_specified_approved(2)
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("Select count(status) from test_valorant_reimbursements where agent_id = 2 and status = 'approved'")
        c = cur.fetchone()
        self.assertEqual(testing_result, c)

    def test_find_specified_denied(self):
        mock_connection()
        testing_result = dmock.test_find_all_users_specified_denied(2)
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("Select count(status) from test_valorant_reimbursements where agent_id = 2 and status = 'denied'")
        c = cur.fetchone()
        self.assertEqual(testing_result, c)

    def test_find_specified_approved(self):
        mock_connection()
        testing_result = dmock.test_find_all_users_specified_pending(2)
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("Select count(status) from test_valorant_reimbursements where agent_id = 2 and status = 'pending'")
        c = cur.fetchone()
        self.assertEqual(testing_result, c)

    def test_find_most_eco(self):
        mock_connection()
        testing_result = dmock.test_get_most_eco()
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("""select first_name, last_name, sum(r.economy) economy from test_valorant_employees c join 
                   test_valorant_reimbursements r
                       on c.employee_id = r.agent_id group by first_name, last_name order by economy DESC
                   """)
        c = cur.fetchone()
        self.assertEqual(testing_result, c)

    def test_find_most_approved(self):
        mock_connection()
        testing_result = dmock.test_get_most_approved()
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("""select first_name, last_name, count(status) submissions from test_valorant_employees c join
            test_valorant_reimbursements r on c.employee_id = r.agent_id where status = 'approved'
             group by first_name, last_name order by submissions DESC
            """)
        x = cur.fetchone()
        self.assertEqual(testing_result, x)

    def test_find_most_approved(self):
        mock_connection()
        testing_result = dmock.test_get_most_denied()
        conn = dbconfig.get_connection()
        cur = conn.cursor()
        cur.execute("""select first_name, last_name, count(status) submissions from test_valorant_employees c join
            test_valorant_reimbursements r on c.employee_id = r.agent_id where status = 'denied'
             group by first_name, last_name order by submissions DESC
            """)
        x = cur.fetchone()
        self.assertEqual(testing_result, x)


    def tearDown(self):
        # mock_connection()
        # conn = dbconfig.get_connection()
        # cur = conn.cursor()
        # cur.execute(""" TRUNCATE TABLE test_valorant_reimbursements """)
        # conn.commit()
        pass