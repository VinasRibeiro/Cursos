=begin

Crie um programa que leia o nome completo de uma pessoa e mostre:
>O nome com todas as letras maiúsculas e minúsculas.
>Quantas letras ao todo (sem considerar espaços).
>Quantoas letras tem o primeiro nome.

nome = 'vinicius rodrigues ribeiro'

nomesplit = nome.split

print "#{nomesplit} \n"
print nomesplit.join(" ")


=end
print 'Digite seu nome completo: '
nome = gets.chomp

puts "Seu nome em maiuscula é: #{nome.upcase} "
puts "Seu nome em minúsculas é: #{nome.downcase} "
puts "Seu nome tem ao todo: #{((nome.split).join).length} letras"
puts "Seu primeiro nome é #{(nome.split)[0]} e ele tem #{(nome.split)[0].length} letras"

