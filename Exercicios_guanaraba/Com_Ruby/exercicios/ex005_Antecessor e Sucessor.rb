#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

puts 'Digite um número: '
numero = gets.chomp.to_i


puts "O antecessor é #{numero-1}"
puts "O sucessor é #{numero+1}"
