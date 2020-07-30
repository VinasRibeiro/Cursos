#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

puts 'Nota 1: '
n1 = gets.chomp.to_f
puts 'Nota 2: '
n2 = gets.chomp.to_f

puts "A média das notas é : #{(n1+n2)/2}"