=begin

Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

=end

print 'Insira seu nome: '
nome = gets.chomp.downcase

print "O seu nome contem silva? #{nome.include? "silva"}"