Feature: Google Search
  Scenario: User searches for a term in Google
    Given the user is on the Google homepage
    When the user enters the search term
    And clicks the search button
    Then search results should be displayed