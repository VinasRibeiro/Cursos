=begin

Faça um programa que leia uma frase pelo teclado e mostre:
-Quantas vezes aparece a letra "A".
-Em que posição ela aparece a primeira vez?.
-Em que posição ela aparece a última vez?.

=end


#No ruby todas as funções devem estar definidas antes


def retornaposicao (busca,palavra)
  if busca.length > 1
      puts 'A busca deve ter apenas 1 caracter'       
  else
  
      i = 0
      pri = nil
      ult = 0
      while i < palavra.length
          
          if palavra[i] == busca
             
              if pri == nil
                  pri = i
              end
              ult = i        
          end   
          i = i + 1
      end
  end
  return pri,ult
end

def count_em(string, substring)
    string.scan(/(?=#{substring})/).count
end


puts 'Insira a palavra completa: '
palavra = gets.chomp.downcase

puts 'Insira o conteudo a ser buscado: '
busca = gets.chomp.downcase


achado = count_em(palavra, busca)
print "A busca por #{busca} aparece #{achado} vezes \n"

res = retornaposicao(busca,palavra)

puts "A primeira busca de #{busca}, esta na posição #{res[0]}"

puts "A ultima busca por #{busca} foi na posição #{res[1]}"



=begin

Para buscar uma string em outra string eu achei uma solução no stackoverflow
https://stackoverflow.com/questions/25938430/ruby-how-to-count-the-number-of-times-a-string-appears-in-another-string/25938828

def count_em(string, substring)
  string.scan(/(?=#{substring})/).count
end

count_em(string,"aa")
 #=> 5

=end