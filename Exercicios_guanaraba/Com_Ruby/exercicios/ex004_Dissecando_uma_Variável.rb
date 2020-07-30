#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
#o tipo de uma variável é definido no momento em que a ela recebe o valor


=begin

Comparações
O tipo de primitivo desse valor é :
Só tem espaços? :
È um numero? :
È alfabético? :
É alfanumérico? :
Está em maiúscula? :
Está em minúsculas? :
Está capitalizado? :

=end

def isalpha(str)
  return false if str.empty?
  !str.match(/[^A-Za-z]/)
end

def isint(str)
  return false if str.empty?
  !str.match(/[^0-9]/)
end


def isalphanum (str)

  if ((str =~ /[0-9]/) != nil) and ((str =~ /[a-zA-Z]/) != nil)
    return true
  else
    return false
  end
  
end


def isupper(str)
  return false if str.empty?
  !str.match(/[^A-Z]/)
  
end

def islower(str)
  return false if str.empty?
  !str.match(/[^a-z]/)
end

def isCapt(str)
  if (str[0] =~ /[A-Z]/) == 0
    return true
  else
    return false
  end
   
end


puts 'Digite algo: '
var1 = gets.chomp

puts "O tipo primitivo dessa variável é : #{var1.class.to_s}"

puts "È um numero?: #{isint(var1)} "

puts "É alfabético?: #{isalpha(var1)}"

puts "Espaços vazios? : #{var1.strip.empty?}"

puts "È alfanumérico? : #{isalphanum(var1)}"

puts "Está em maiúscula? : #{isupper(var1)}"

puts "Está em minuscula? : #{islower(var1)}" 

puts "Esta captalizada? : #{isCapt(var1)}" 