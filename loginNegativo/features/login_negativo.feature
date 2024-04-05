Feature: Login Negativo

    Scenario: Login email invalido
        Given que entro no site Cacau Show
        When preencho o campo de email sergio_gustavo_martins@athos.srv.b 
        Then recebo uma mensagem de erro

    Scenario Outline: Login Negativo
        Given que entro no site Cacau Show
        When preencho o campo de email <email>
        Then preencho o campo de senha <senha> e recebo uma <mensagem> de erro 

        Examples:
        | id | email                               | senha        | mensagem                                                     |
        | 01 | sergio_gustavo_martins@athos.srv.br | YIFZ5mBRx    | Epic sadface: Este campo é obrigatorio                       |
        | 02 | sergio_gustavo_martins@athos.srv.br |              | Epic sadface: Este campo é obrigatorio                       | 
