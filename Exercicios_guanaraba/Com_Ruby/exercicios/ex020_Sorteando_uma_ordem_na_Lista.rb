=begin
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
=end

nomes = []

for nome in (0...4)
    nomes[nome] = gets.chomp
end

puts "Organizado em ordem alfabética #{nomes.sort}"
puts "Sorteado aleatóriamente #{nomes.shuffle}"