=begin

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

=end



puts 'Insira um numero que mostre se ele é pra ou impar: '
num = gets.chomp.to_i

if (num % 2) == 0
    res = "Par"
else
    res = "impar"
end
    

puts "O numero #{num} é #{res}"