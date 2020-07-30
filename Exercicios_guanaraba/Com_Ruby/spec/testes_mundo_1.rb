class EXMundo1

    attr_accessor :nome
end






describe EXMundo1 do

    it'Deve retornar o nome digitado'do

        pessoa = EXMundo1.new

        pessoa.nome = 'Spiderman'
        expect(pessoa.nome).to_enum 'Spiderman'

    end
    

end