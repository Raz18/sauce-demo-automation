Feature: Products Page Functionality
  As a logged-in user
  I want to view and interact with products
  So that I can browse the inventory

  Background:
    Given I am on the Sauce Demo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should be redirected to the products page

  Scenario: Verify product listing is displayed
    Then the products page should display inventory items
    And all product names should not be empty
    And all product prices should be greater than 0

  Scenario: Sort products by price low to high
    When I sort products by "Price (low to high)"
    Then products should be sorted by price in ascending order

  Scenario: Sort products by price high to low
    When I sort products by "Price (high to low)"
    Then products should be sorted by price in descending order
