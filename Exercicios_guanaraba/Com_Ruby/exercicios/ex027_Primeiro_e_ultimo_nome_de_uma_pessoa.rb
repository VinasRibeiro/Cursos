=begin

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza

=end

nome = gets.chomp

nome2 = nome.split

puts "O primeiro nome é #{nome2[0]} ."
puts "O ultimo nome é #{nome2[(nome2.length) - 1]}. "