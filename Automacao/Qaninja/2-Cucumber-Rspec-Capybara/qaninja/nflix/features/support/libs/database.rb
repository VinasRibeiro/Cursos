require "pg"

class DataBase
    def delete_movie(title)
        connection = PG.connect(host: 'localhost', dbname: 'ninjaflix', user: 'postgres', password: 'qaninja')
        connection.exec("DELETE from public.movies where title = '#{title}';")
        
    end
end
