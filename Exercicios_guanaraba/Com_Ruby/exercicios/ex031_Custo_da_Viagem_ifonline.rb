=begin
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagem de até 200Km
e R$0,45 para viagens mais longas

=end


puts 'Insira a quantidade de Km rodado:'

distancia = gets.chomp.to_i

if distancia >= 200
    valor = distancia * 0.45
else
    valor = distancia * 0.50
end

puts " O valor total foi de R$#{valor} reais"

valor2 = distancia <= 200 ? distancia * 0.50 : distancia * 0.45

puts "Usando if em uma linha #{valor2}"