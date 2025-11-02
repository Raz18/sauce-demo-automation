Feature: Login Functionality
  As a user of Sauce Demo
  I want to login with different credentials
  So that I can access the application

  Background:
    Given I am on the Sauce Demo login page

  Scenario Outline: Login with valid users
    When I login with username "<username>" and password "<password>"
    Then I should be redirected to the products page
    And the products page should display inventory items

    Examples:
      | username                | password     |
      | standard_user           | secret_sauce |
      | performance_glitch_user | secret_sauce |

  Scenario Outline: Login with invalid credentials
    When I login with username "<username>" and password "<password>"
    Then I should see an error message
    And I should see an error message containing "Username and password do not match any user in this service"
    And I should remain on the login page

    Examples:
      | username      | password        |
      | invalid_user  | wrong_password  |
      | standard_user | wrong_password  |

  Scenario: Login with locked out user
    When I login with username "locked_out_user" and password "secret_sauce"
    Then I should see an error message containing "Sorry, this user has been locked out"
    And I should remain on the login page
