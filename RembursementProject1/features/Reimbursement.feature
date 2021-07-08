Feature: SlayerLogin

    Scenario: A user would like to login to their account
      Given a user is on the login page of Slayer Reimbursements
      When a user enters the correct Username and password
      Then The user will be brought to the index page


    Scenario: A user is on the home page of Slayer Reimbursements and would like to submit a reimbursement
      Given A user is on the home page of Slayer Reimbursements

      When the user clicks the "Submit Request" Button, the user will be brought to the Submit Request Page
      Then the user is redirected to submit a request on the newly developed form

      Scenario: A user is on the Submit Request Page and would like to submit a reimbursement
        Given A user has accessed the Reimbursement page
        When The user enters the price/economy of their reimbursement stating why they are submitting their reimbursement with their manager
        Then they will be able to submit their request to a manager

        Scenario: A user has successfully submitted a reimbursement and would like to check the status
          Given A user has submitted their reimbursement and has clicked the "Request" Tab
          When the user clicks the request tab they are brought to the request page where they can see their history
          Then the user chooses "pending" to check to see if their request has made it in the system successfully been submitted

          Scenario: A user would like to log out of the reimbursement system
            Given The user has submitted their Reimbursement and would like to log out at the end of the day
            When The user clicks the notification symbol in the top right corner they will see a prompt for logout
            Then the user will click then button to log out of their account and the user will successfully be logged out.

            Scenario: A user would like to login to their account
              Given a manager is on the login page of Slayer Reimbursements
              When a manager enters the correct Username and password
              Then the manager is brought to the index page for managers

              Scenario: A manager is on the home page and would like to check approve pending requests
                Given The manager is on the home page and logged in
                  When The manager clicks the requests tab they will be brought to their pending page
                    Then the manager will be able to approve their pending reimbursements and the table will auto update

                Scenario: A manager would like to check the statistics of requests
                  Given The manager has recently approved a request and would like to check statistics
                    When the manager clicks the statistics tab they will be brought to the statistics page
                      Then the manager can scrolldown to see different variations of measurement and graphs