#language: pt


@temp
Funcionalidade: Login
    Para que eu possa gerenciar os filmes do catálogo NinjaFlix
    Sendo um usuário previamente cadastrado
    Posso acessar o sistema com o meu email e senha

    @login_happy
    Cenario: Acesso

        Quando faço login com "tony@stark.com" e "pwd123"
        Então devo ser autenticado
        E devo ver "Tony Stark" na área logada

    @login_unhappy
    Esquema do Cenario: Login sem sucesso

        Quando faço login com <email> e <senha>
        Então não devo ser autenticado
        E devo visualizar a mensagem de alerta <alerta>

        Exemplos:
        | email             | senha     | alerta                         |
        | "tony@stark.com"  | "1234456" | "Usuário e/ou senha inválidos" |
        | "lpwda@live.com"  | "pwd123"  | "Usuário e/ou senha inválidos" |
        | ""                | "123456"  | "Opps. Cadê o email?"          |
        | "tony@stark.com"  | ""        | "Opps. Cadê a senha?"          |