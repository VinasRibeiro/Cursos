=begin

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

=end



puts 'Escolha um numero de 0 a 5:'

nuser = gets.chomp.to_i


nrand = rand(5)

if nuser == nrand
    ch = "acertou"
else
    ch = "errou"
end

puts "O computador escolheu #{nrand} e você #{ch}"