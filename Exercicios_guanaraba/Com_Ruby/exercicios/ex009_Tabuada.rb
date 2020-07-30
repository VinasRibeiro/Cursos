#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuaputs 
puts 'Insira um numero: '

n = gets.chomp.to_i

# Não consegui usar o times neste caso.
=begin
10.times do
a = 1
a = a + 1
puts "#{n} x #{a} = #{n*a}"
end
=end

for item in (1...11)

    puts "#{n} x #{item} = #{n*item}"

end