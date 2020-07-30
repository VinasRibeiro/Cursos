#Escreva umn programa que converta uma temperatura digitada em °C e converta para °F

puts 'Insira o °C : '
c = gets.chomp.to_f

puts "O valor em °F é: #{(c*1.8)+32}"

puts 'Insira o valor de °F: '

f = gets.chomp.to_f

puts "O valor de °C é: #{(f-32)/1.8}"