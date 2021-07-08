from json import JSONEncoder


class Reimbursement:

    def __init__(self, reimbursement_id, agent_id, economy, purpose, transaction_time, status, manager_id,
                 approval_reason):
        self._reimbursement_id = reimbursement_id,
        self._agent_id = agent_id,
        self._economy = str(economy),
        self._purpose = purpose
        self._transaction_time = str(transaction_time)
        self._status = status,
        self._manager_id = manager_id,
        self._approval_reason = approval_reason


class reimbursementEncoder(JSONEncoder):
    # override default method
    def default(self, account):
        if isinstance(account, Reimbursement):
            return account.__dict__
        else:
            # if anything weird happens, use default parent implementation
            return super().default(account)


class Economy:

    def __init__(self, first_name, last_name, economy):
        self._first_name = first_name,
        self._last_name = last_name,
        self._economy = str(economy)


class Resubmit:

    def __init__(self, first_name, last_name, reimbursements):
        self._first_name = first_name,
        self._last_name = last_name,
        self._reimbursements = reimbursements


class resubmitEncoder(JSONEncoder):
    # override default method
    def default(self, account):
        if isinstance(account, Resubmit):
            return account.__dict__
        else:
            # if anything weird happens, use default parent implementation
            return super().default(self, account)


class economyEncoder(JSONEncoder):
    # override default method
    def default(self, account):
        if isinstance(account, Economy):
            return account.__dict__
        else:
            # if anything weird happens, use default parent implementation
            return super().default(self, account)
