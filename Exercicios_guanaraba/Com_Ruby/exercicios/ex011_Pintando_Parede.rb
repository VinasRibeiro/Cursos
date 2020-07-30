=begin
Faça um progrma que leia a lergura e a altura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária para pínta-la, sabendo que cada litro de tinta pinta 
uma área de 2m quadrado.

=end

puts "Insira a lergura e altura da parede"
puts 'Largura: '
larg = gets.chomp.to_f
puts 'Altura'
alt = gets.chomp.to_f

puts "Você vai precisar de #{(larg*alt)/2}lt de tinta"