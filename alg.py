import classes
import math

def leitura():
	linha = 1
	numVertice=0
	numMediana=0
	numSolucao=0
	listaVertice = []
	with open ("SJC1.txt", "r") as arquivo:
		for line in arquivo:
			auxVertice=classes.Vertice()
			palavra=0
			for i in line.split():			
				if linha is 1:
					if palavra is 0:
						numVertice = i
					else:
						numMediana = i
						numSolucao = int(math.log(float(numVertice))*17.5)		
				else:
					auxVertice.indice=linha-2
					if palavra is 0:
						auxVertice.x = i
					elif palavra is 1:
						auxVertice.y = i
					elif palavra is 2:
						auxVertice.capacidade = i
					elif palavra is 3:
						auxVertice.demanda = i
				palavra+=1
			linha+=1
			if (auxVertice.x) is  None:   #tira a primeira linha da lista.
				continue
			listaVertice.append(auxVertice)
	arquivo.close()
	for i in listaVertice:
		print(i)
	return numVertice,numSolucao,numMediana,listaVertice

def main(): 									
	leitura()
if __name__ == '__main__':
    main()