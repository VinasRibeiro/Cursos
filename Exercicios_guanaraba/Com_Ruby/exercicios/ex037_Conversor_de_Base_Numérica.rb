=begin

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher 
qual será a base de conversão:

-1 para binário
-2 para octal
-3 para hezadecimal

=end

n = gets.chomp.to_i

puts "#{n} em binário é #{n.to_s(2)}"
puts "#{n} em octal é #{n.to_s(8)}"
puts "#{n} em hexadecimal é #{n.to_s(16)}"
