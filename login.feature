Feature: Login functionality on Guvi site

  Scenario: Successful login with valid credentials
    Given I am on the Guvi Zen portal login page
    When I enter valid credentials
    And I click on the login button
    Then I should login successful

  Scenario: Unsuccessful login with invalid credentials
    Given I am on the Guvi Zen portal login page
    When I enter invalid credentials
    And I click on the login button
    Then I should see an error message