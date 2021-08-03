CREATE TABLE valorant_employees (
	employee_id bigserial PRIMARY KEY,
	first_name varchar  not null,
	last_name varchar  not null,
	tiers varchar not null,
	employee_password varchar  not null,
	employee_username varchar  not null,
	email varchar  not null,
	isManager varchar 
)

CREATE TABLE valorant_reimbursements(
	reimbursement_id bigserial,
	agent_id int,
	economy money not null,
	purpose varchar not null,
	transaction_time timestamp DEFAULT CURRENT_TIMESTAMP,
	status varchar DEFAULT 'pending',
	manager_id int,
	approval_reason varchar DEFAULT 'none',
	primary key (reimbursement_id),
	foreign key (agent_id)
	REFERENCES valorant_employees(employee_id)
)

INSERT INTO valorant_employees (first_name, last_name, tiers, employee_password, employee_username, email, isManager) 
VALUES ('phoenix', 'fire', 'radiant', 'gutted', 'hotboy', 'hotboy@gmail.com', '1')

INSERT INTO valorant_reimbursements (reimbursement_id, agent_id, economy, purpose, transaction_time, 
        status, manager_id, approval_reason) 
        VALUES (default, 1, 2500, 'weapons', default, default, 1, default)

