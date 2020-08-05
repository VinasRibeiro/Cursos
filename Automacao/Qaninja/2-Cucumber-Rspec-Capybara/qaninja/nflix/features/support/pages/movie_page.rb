class MoviePage
    include Capybara::DSL

    def initialize
        @movie_list_css = "table tbody tr"
    end

    def form
        MovieAdd.new
    end

    def sweet_alert
        SweetAlert.new
    end

    def add
        find(".movie-add").click
    end       

    def movie_tr(title)
        #Este comando busca elementos em uma tabela html pelo titulo do filme
        #E retorna os dados da linha correspondente ao titulo
        find(@movie_list_css, text: title)
    end

    def remove(title)
        #esta função aproveita o retorno de movie_tr e procura o botão excluir dentro da linha  e clica nele
       movie_tr(title).find(".btn-trash").click
    end

    def has_no_movie(title)
        page.has_no_css?(@movie_list_css, text: title)
    end

    def has_movie(title)
        page.has_css?(@movie_list_css, text: title)
    end
end