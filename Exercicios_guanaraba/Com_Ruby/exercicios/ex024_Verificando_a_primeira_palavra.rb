=begin

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 
'Santo'.

=end

palavra = 'Santo'

print 'Digite o nome completo'
user = gets.chomp

#A função split do ruby remove os espaços em branco
novonome = user.split(" ")
puts novonome[0]

if novonome[0].upcase == palavra.upcase
    puts "O nome digitado começa com #{palavra}"
else
    puts "O nome digitado não começa com #{palavra}"
end