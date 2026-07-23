Feature: User Authentication
  As an ecommerce customer
  I want secure access to my account
  So that I can view orders and manage my profile

  Background:
    Given a registered user exists with password "ValidPass123!"

  @smoke @auth
  Scenario: Successful login with valid credentials
    When the user logs in with valid credentials
    Then the user sees their account dashboard
    And the user redirects to the dashboard page

  @auth @negative
  Scenario: Failed login with wrong password
    When the user logs in with password "WrongPass"
    Then the user sees an authentication error
    And the user remains on the login page

  @smoke @auth
  Scenario: User logout from dashboard
    Given the user is logged in
    When the user logs out
    Then the user sees the login page
    And the user cannot access the dashboard