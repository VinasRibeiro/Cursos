=begin

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

=end
puts 'Digite o cateto oposto: '
co = gets.chomp.to_f
puts 'Digite o cateto adjacente: '
ca = gets.chomp.to_f

hipo = (co**2 + ca**2) ** (0.5)

puts "A hipotenusa é: #{hipo.truncate(12)}"