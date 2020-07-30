=begin

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem
ou não formar um triângulo.

=end

puts "Insira os 3 valores de medidas: "
n1 = gets.chomp.to_f
n2 = gets.chomp.to_f
n3 = gets.chomp.to_f

if n1 < n2 + n3 && n2 < n1 + n3 && n3 < n2 + n1
  puts "O triangulo é possivél"
else
  puts "O triangulo NÂO é possivél"
end
