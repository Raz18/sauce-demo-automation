Feature: Shopping Cart Functionality
  As a logged-in user
  I want to manage items in my cart
  So that I can prepare for checkout

  Background:
    Given I am on the Sauce Demo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should be redirected to the products page

  Scenario: Add products to cart
    When I add 3 products to the cart
    Then the cart badge should show 3 items
    When I navigate to the cart page
    Then the cart should contain 3 items

  Scenario: Remove product from cart
    When I add 3 products to the cart
    Then the cart badge should show 3 items
    When I navigate to the cart page
    And I remove 1 product from the cart
    Then the cart should contain 2 items

  Scenario: Cart badge updates correctly
    When I add 1 products to the cart
    Then the cart badge should show 1 items
    When I add 2 products to the cart
    Then the cart badge should show 3 items
    When I remove 1 product from the cart
    Then the cart badge should show 2 items
