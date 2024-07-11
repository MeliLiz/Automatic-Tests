Feature: Validar la cantidad de pokemon de tipo pasto
    Scenario: Validar que existan 151 pokemon
        Given Validar la cantidad de pokemon de la primera generación
        When Se accede a la página de pokedex
        Then Validar que existan 151 pokemon

    Scenario: Validar la cantidad de pokemon de tipo pasto
        Given Validar la cantidad de pokemon de tipo pasto de la primera generación
        When Se accede a la página de pokedex
        Then Validar que existan 14 pokemon de tipo pasto


    Scenario Outline: Validar la cantidad de diferentes tipos de pokemon
        Given Validar la cantidad de los diferentes tipos de pokemon de la primera generación
        When Se accede a la página de pokedex
        Then Validar que la cantidad de tipo <pokemonType> sea <n>
        Examples:
        |pokemonType|n |
        |type-grass |14|
        |type-fire  |12|
        |type-water |32|