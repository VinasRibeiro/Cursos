#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela 
#pode comprar.
#Considere US$1.00 = R$3,27

puts 'Quanto dinheiro você tem na carteira? R$: '
dinheiro = gets.chomp.to_f

puts "Você tem U$#{dinheiro/4.07} dolares"