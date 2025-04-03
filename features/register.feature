Feature: Register Account Functionality

  @register
  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter below details into mandatory fields
       |first_name|last_name|telephone |password|
       |Arun      |Motoori  |1234567890|12345   |
    When I select Privacy Policy option
    When I click on Continue button
    Then Account should get created

  @register
  Scenario: Register with all fields
    Given I navigate to Register Page
    When I enter below details into all fields
       |first_name|last_name|telephone |password|
       |Motoori   |Arun     |1234567890|12345   |
    When I select Privacy Policy option
    When I click on Continue button
    Then Account should get created

  @register @only1
  Scenario: Register with a duplicate email address
    Given I navigate to Register Page
    When I enter below details into all fields except email field
       |first_name|last_name|telephone |password|
       |Motoori   |Arun     |1234567890|12345   |
    When I enter existing accounts email into email field
    When I select Privacy Policy option
    When I click on Continue button
    Then Proper warning message informing about duplicate account should be displayed

  @register
  Scenario: Register with all fields
    Given I navigate to Register Page
    When I dont enter anything into fields
    When I click on Continue button
    Then Proper warning message for every mandatory fields should be displayed
