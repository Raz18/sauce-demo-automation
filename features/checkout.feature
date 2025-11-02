Feature: Checkout Functionality
  As a logged-in user
  I want to complete the checkout process
  So that I can purchase products

  Background:
    Given I am on the Sauce Demo login page
    When I login with username "standard_user" and password "secret_sauce"

  Scenario: Complete checkout with valid information
    When I add 3 products to the cart
    And I navigate to the cart page
    And I proceed to checkout
    And I fill checkout information with data from CSV
    And I continue to checkout overview
    Then the subtotal should equal the sum of item prices
    And the total should equal subtotal plus tax
    When I finish the checkout
    Then I should see the order success message

  Scenario: Checkout with empty cart (Negative)
    When I navigate to the cart page
    Then the cart should be empty
    When I proceed to checkout
    Then I should be on the checkout information page
