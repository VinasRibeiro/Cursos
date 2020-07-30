=begin

Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem deizendo que ele doi multado.
A multa vai custar R$7,00 por cada Km acima do limite.

=end



puts 'Insira a velocidade atingida: '

velocidade = gets.chomp.to_i

multa = (velocidade - 80) * 7

if velocidade > 80
    puts "Você foi multado em R$#{multa}"
else
    puts 'VocÊ esta no limite permitido'
end