=begin
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
=end


puts 'Digite um número qualquer: '
n = gets.chomp.to_f
i = n.to_i
puts "O numero inteiro é #{i} e o resto é #{(n-i).truncate(4)}"

# outro metodo seria
#Usando o truncate() ele aredonda o numero e elimina p zero.



=begin
puts 'Digite um número qualquer: '
n = gets.chomp.to_f
i = n-n.truncate(0)
puts "O numero inteiro é #{n.truncate(0)} e o resto é #{i}"
=end
