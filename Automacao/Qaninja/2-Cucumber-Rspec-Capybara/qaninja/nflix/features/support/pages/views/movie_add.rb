class MovieAdd
    include Capybara::DSL

    #O parâmetro movie aqui é um array de dados que veio do arquivo yaml
    def create(movie)
        find('input[name=title]').set movie["title"]

        select_status(movie["status"]) unless movie["status"].empty?


        find('input[name=year]').set movie["year"]
        find('input[name=release_date]').set movie["release_date"]

        add_cast(movie["cast"])

        find("textarea[name=overview]").set movie["overview"]
        
        #O unless esexuta se for falso o .empty? retorna verdadeiro ou falso para vazio ou não
        upload(movie["cover"]) unless movie["cover"].empty?

        find("#create-movie").click
    end

    def alert
        find(".alert").text
    end

    def upload(file)
        #Aqui o ruby pega o caminho completo da imagem na pasta cover, usando o nome do arquivo .yaml
        #Com a variável @movie["cover"] do movie que veio como parâmetro nessa função.
        cover_file = File.join(Dir.pwd, "features/support/fixtures/cover/" + file) 

        #O caminho com / não é entendido pelo windows e o capybara não vai encontrar
        #Então é preciso usar o comando tr("","") para transformar todas as barra / para baras \\
        #Utilizando a biblioteca gem OS vc pode fazer um if para executar quando for windows 
        #E para não executar quando for sistema Unix como linux e Mac
        cover_file = cover_file.tr("/","\\") if OS.windows?

        
        #Nesta situação o upcover esta com status display none, então o capybara vai ignorar
        #Para ele não ser ignorado é necessário esse parametro do proprio capybara
        Capybara.ignore_hidden_elements = false
        #Este comando é do capybara, é usado para enviar arquivos

        #Ele encontra o campo upcover e envia o arquivo.
        attach_file("upcover", cover_file)
        Capybara.ignore_hidden_elements = true

        #Após o comando enviar arquivo ser usado, é importante reativar esta função
    end

    def add_cast(cast)
        #Este parte o programa busca um array com os nomes dos atores
        #E usando o each do com o cast ele insere os nomes nos campos tipo tags na pagina
        actor = find('.input-new-tag')
        cast.each do |a|
            actor.set a 
            actor.send_keys :tab
        end
    end

    def select_status(status)
        find('input[placeholder=Status]').click
        find('.el-select-dropdown__item', text: status).click
    end
end 