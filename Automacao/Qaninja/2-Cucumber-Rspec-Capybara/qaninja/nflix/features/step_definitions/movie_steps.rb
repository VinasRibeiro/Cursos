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
end

Quando('eu faço o cadastro deste filme') do
    @movie_page.add
    @movie_page.create(@movie)
end

Então('devo ver o novo filme na lista') do

end