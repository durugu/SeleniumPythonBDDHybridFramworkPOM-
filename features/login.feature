Feature: Login Functionality

  @login @only
  Scenario Outline: Login with valid credentials
    Given I navigated to login page
    When I enter Valid email as "<email>" and valid password as "<password>" into the fields
    When I click on Login button
    Then I should get logged in
    Examples:
    |email                        |password   |
    |amotoorisampleone@gmail.com  |secondone  |
    |amotoorisampletwo@gmail.com  |secondtwo  |
    |amotoorisamplethree@gmail.com|secondthree|
    |marunm@gmail.com             |12345      |

  @login
  Scenario: Login with invalid email and valid password
    Given I navigated to login page
    When I enter invalid email and valid password say "12345" into the fields
    When I click on Login button
    Then I should get a proper warning message

  @login
   Scenario: Login with valid email and invalid password
    Given I navigated to login page
    When I enter valid email say "motooricap99@gmail.com" and invalid password say "12345@@" into the fields
    When I click on Login button
    Then I should get a proper warning message

  @login
   Scenario: Login with invalid credentials
    Given I navigated to login page
    When I enter invalid email and invalid password say "12345!!" into the fields
    When I click on Login button
    Then I should get a proper warning message

  @login
   Scenario: Login without entering any credentials
    Given I navigated to login page
    When I dont enter anything into email and password fields
    When I click on Login button
    Then I should get a proper warning message
