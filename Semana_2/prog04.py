# coding=utf-8
#Listas, tupples e sets
courses = ['History', 'Math', 'Pshysics', 'CompSci'] #Cria uma lista. O que diferencia a criação de uma lista da criação de um tupple são as []. Fosse uma tupple seiram ()
empty_list = [] #Criação de uma lista vazia
empty_list = list()

empty_tupple = () #Criação de uma tupple vazia
empty_tupple = tuple()

print(courses) #print coursers
print(courses[0]) #print de um variável específica em courses
print(courses[-1]) #print do último valor da lista, independente da quantidade de itens existentes
print(courses[0:3]) #print de uma quantidade específica de intes (inlcuindo o primeiro, que o 0, e excluindo o segundo, que é o 3)

courses.append('Art') #Adiciona um item ao final

courses.insert(0, 'Quimistry') #Adiciona um item a um lugar especificado no primeiro argumento

courses_2 = ['Education', 'English']

courses.insert(0, courses_2) #Adiciona uma lista "crua" numa localização escífica
courses.remove(courses_2)

courses.extend(courses_2) #Adiciona os itens de courses_2 ao final de courses

print(courses)

courses.remove('Math') #Remove o item escrito da lista
popped = courses.pop() #Remove o último item da lista e pode adiciona-lo a uma variável

courses.reverse() #Inverte a ordem dos itens

print(courses)

print(courses.sort()) #Organiza os itens em ordem alfabética (fossem números seria ordem crescente e com a opção de fazer o print em ordem inversa inserindo o parametro reverse=True)

print(sorted(courses_2)) #Coloca a lista courses_2 em ordém alfabética, mas sem alterar a lista original

nums = [1, 2, 5, 7, 3, 10]

print(min(nums)) #print do menor número da lista
print(max(nums)) #print do maior número da lista
print(sum(nums)) #print da soma dos números da lista

print(courses.index('History')) #print da posição, na lista, do item escrito
print('Art' in courses) #Verdadeiro ou Falso para o teste de encontrar 'Art' na lista courses

for item in courses: #print dos itens da lista um por vez
    print(item)

for index, course in enumerate(courses, start=1): #print dos itens da lista e de suas posições começando por 1
    print(index, course)

courses_str = ', '.join(courses) #Junta os itens da lista courses com ', ' e insere na variável courses_str

print(courses_str)

new_list = courses_str.split(', ') #Separa a string de courses_str a partir de ', ' e os organiza em itens de uma lista inserindo em new_list

print(new_list)

# ATENÇÃO! Todos os métodos usados para alterar valores são aplicáveis somente nas listas. Tupples não podem ser alteradas, mas podem ser acessadas por métodos

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'} #Criação de um Set
art_courses = {'History', 'Math', 'Art', 'Design'}
empty_set = set() #Criação de um Set vazio. Note que ele não aceita a igualdade com {}, visto que isso seria a criação de um dicionário vazio

#Sets não armazenam seus itens por index, ou seja, suas posições são, na verdade, aleatórias.

print(cs_courses) #Print do set. Note que ele exclui itens repetidos
print(cs_courses.intersection(art_courses)) #Print do que existe de igual entre os dois Sets
print(cs_courses.difference(art_courses)) #Print do que existe de diferente entre os Sets
print(cs_courses.union(art_courses)) #Print da união entre os dois Sets

