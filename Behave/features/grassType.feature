Feature: Validar la cantidad de pokemon de tipo pasto
    Scenario: Validar que existan 151 pokemon
        Given Validar la cantidad de pokemon de la primera generación
        When Se accede a la página de pokedex
        Then Validar que existan 151 pokemon

    Scenario: Validar la cantidad de pokemon de tipo pasto
        Given Validar la cantidad de pokemon de tipo pasto de la primera generación
        When Se accede a la página de pokedex
        Then Validar que existan 14 pokemon de tipo pasto