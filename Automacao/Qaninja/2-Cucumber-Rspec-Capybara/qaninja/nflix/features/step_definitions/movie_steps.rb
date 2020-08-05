#A string passada pelo arquivo cadastro de filmes.feature vira movie_code para ser usada no arquivo ruby

# O comando File.join(Dir.pwd, 'feaures/support/fixtures/movies.yaml') 
# busca só o caminho do arquivo a partir da raiz do projeto
# E:/RepoGit/Cursos/Automacao/Qaninja/2-Cucumber-Rspec-Capybara/qaninja/nflix/feaures/support/fixtures/movies.yaml
# Independente do local do projeto ele vai busar o arquivo seguido de feaures/support/fixtures/movies.yaml

#Para pegar o arquivo yaml se usa esse comando YAML.load_file()
# YAML.load_file(File.join(Dir.pwd, 'feaures/support/fixtures/movies.yaml'))
# Assim ele carrega o conteudo do arquivo e não o caminho
    

Dado('que {string} é um novo filme') do |movie_code|
    file = YAML.load_file(File.join(Dir.pwd, 'features/support/fixtures/movies.yaml'))
    @movie = file[movie_code]
    
    #Este comando apaga o filme da vez pra garantir que
    #Na step Quando faço cadastro deste filme ele não exista
    DataBase.new.delete_movie(@movie["title"])
end

Dado('este filme já existe no catálogo') do
   DataBase.new.insert_movie(@movie)
end

Quando('eu faço o cadastro deste filme') do
    @movie_page.add
    @movie_page.form.create(@movie)
end

Então('devo ver o novo filme na lista') do
    result = @movie_page.movie_tr(@movie["title"])
    expect(result).to have_text @movie["title"]
    expect(result).to have_text @movie["status"]
end

Então('devo visualizar a notificação {string}') do |expect_alert|
    expect(@movie_page.form.alert).to eql expect_alert
end

Dado('que {string} está no catálogo') do |movie_code|   
    #Isto se chama dinamic step, ele reutiliza steps já criados
    # O 'E' abaixo é a mesma coisa que Mas e vem sempre depois do Dado e antes do quando.
    steps %{
        Dado que "#{movie_code}" é um novo filme
        E este filme já existe no catálogo
    }
end                                                                          
                                                                            
Quando('eu solicito a exclusão') do    
    #A variável @movie_page está disponivél por causa do contexto do step que ela é usada
    #No caso é o step acima                                   
    @movie_page.remove(@movie["title"])
end                                                                          
                                                                            
Quando('confirmo a socilitação') do                                          
   @movie_page.sweet_alert.confirm
end                                                                          
                                                                            
Então('este item deve ser removido do catálogo') do                          
    expect(@movie_page.has_no_movie(@movie["title"])).to be true
end          

Quando('cancelo a solicitação') do
    @movie_page.sweet_alert.cancel
end

Então('este item deve permanecer no catálogo') do
    expect(@movie_page.has_movie(@movie["title"])).to be true
end