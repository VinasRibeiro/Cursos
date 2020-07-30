#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

puts "Insira seu salario: "
salario = gets.chomp.to_f
novosal = salario +(salario * 15 / 100)
puts "Seu salario com 15% de aumento foi para : #{novosal}"