Feature: In the MIT website, search all the websites about son quantum topic (search 'quantum'), check that 'A new way for quantum computing systems to keep their cool' exists and open it
    Scenario: Search all the websites about quantum
        Given Open the MIT website
        When Search for wbsites about "quantum"
        Then Verify the results