#Crie um programa que leia dois números e mostre a soma entre eles.

puts 'Insira dois numeros: '

n1 = gets.chomp.to_i
n2 = gets.chomp.to_i 

puts 'A soma entre n1: ' + n1.to_s + ' e n2: ' + n2.to_s + ' é ' + (n1+n2).to_s
