# MATRIZ CONSTANTE por: Wanderson Junior de Oliveira Bignardi
# Matriz Constante é uma matriz quadrada de ordem n >= 3
#preenchida com 1,2,3,4,..., n ** 2
# como achar submatrizes 4x4? divida a quantidade de elementos da matriz por 16

#============================================================================================================================

def CasoUm(n:int): # Função para o Caso 1 inteiro
	m = n

	M = [[0] * n for i in range(m)]

	l = 0
	c = (len(M[0]) - 1) // 2

	int_valores = n ** 2

	for valores in range(1, int_valores + 1): #laço para preencher a matriz de ordem impar
		M[l][c] = valores
		l_bkp = l
		c_bkp = c
		l -= 1
		c += 1
		if l < 0:
			l = n - 1
		if c > n - 1:
			c = 0

		if M[l][c] != 0:
			l = l_bkp + 1
			c = c_bkp


	for i in range(m): #print final 
		for p in range(n):
			print(f"{M[i][p]}", end = "\t")
		print("")

#============================================================================================================================

def CasoDois(n:int, m:int): # Função para o Caso 2 inteiro
	m = n

	M = [[0] * n for i in range(m)]

	incrementa = 0

	for i in range(m): # laço para preencher a matriz de 1 até n ao quadrado
		for p in range(n):
			M[i][p] = 1 + incrementa
			incrementa += 1

	qnt_submatrizes = (n * n) // 16
	qnt_elementos_diagonais = (n * n) // 2

	for l_primaria in range(0, len(M), 4): # laço para alterar apenas as diagonais principais
		for c_primaria in range(0, len(M[0]), 4):
			M[l_primaria][c_primaria] = (n ** 2 + 1) - M[l_primaria][c_primaria]
			M[l_primaria+1][c_primaria+1] = (n ** 2 + 1) - M[l_primaria+1][c_primaria+1]
			M[l_primaria+2][c_primaria+2] = (n ** 2 + 1) - M[l_primaria+2][c_primaria+2]
			M[l_primaria+3][c_primaria+3] = (n ** 2 + 1) - M[l_primaria+3][c_primaria+3]


	for l_secundaria in range(0, len(M), 4):  # laço para alterar apenas as diagonais secundárias
		for c_secundaria in range(3, len(M), 4):
			M[l_secundaria][c_secundaria] = (n ** 2 + 1) - M[l_secundaria][c_secundaria]
			M[l_secundaria+1][c_secundaria-1] = (n ** 2 + 1) - M[l_secundaria+1][c_secundaria-1]
			M[l_secundaria+2][c_secundaria-2] = (n ** 2 + 1) - M[l_secundaria+2][c_secundaria-2]
			M[l_secundaria+3][c_secundaria-3] = (n ** 2 + 1) - M[l_secundaria+3][c_secundaria-3]


	for lfinal in range(m): #print final
		for cfinal in range(n):
			print(f"{M[lfinal][cfinal]}", end ="\t")
		print("")


#============================================================================================================================

def CasoTres(n:int, m:int): # Função para o Caso 3 inteiro
	# Primeira etapa do Caso 3
	l = c = (2 * m) + 1

	M = [[0] * c for i in range(l)] #matriz auxiliar de ordem 2m + 1

	qnt_l = m + 1
	qnt_u = 1
	qnt_x = m - 1

	for l_l in range(0, qnt_l):
		for c_l in range(len(M[0])):
			M[l_l][c_l] = "L"


	for l_u in range(qnt_l, qnt_l + 1):
		for c_u in range(len(M[0])):
			M[l_u][c_u] = "U"

	for l_x in range(qnt_l + 1, qnt_l + 1 + qnt_x):
		for c_x in range(len(M[0])):
			M[l_x][c_x] = "X"

	c_ucentral = (len(M) - 1) // 2

	bkp_ucentral = M[l_u][c_ucentral]
	M[l_u][c_ucentral] = M[l_u-1][c_ucentral]
	M[l_u-1][c_ucentral] = bkp_ucentral	
	#=======================================================================
	## Segunda etapa do Caso 3
	
	Matriz_Final = [[0] * n for i in range(n)]

	fim = n ** 2

	l_final = 0
	c_final = (len(Matriz_Final[0]) - 1) // 2

	l_auxiliar = l_final // 2
	c_auxiliar = c_final // 2

	for valores in range(1, fim + 1, 4):
		if M[l_auxiliar][c_auxiliar] == "L":
			Matriz_Final[l_final][c_final+1] = valores
			Matriz_Final[l_final+1][c_final] = valores + 1
			Matriz_Final[l_final+1][c_final+1] = valores + 2
			Matriz_Final[l_final][c_final]= valores + 3

		elif M[l_auxiliar][c_auxiliar] == "U":
			Matriz_Final[l_final][c_final] = valores
			Matriz_Final[l_final+1][c_final] = valores + 1
			Matriz_Final[l_final+1][c_final+1] = valores + 2
			Matriz_Final[l_final][c_final+1] = valores + 3
		
		else:
			Matriz_Final[l_final][c_final] = valores
			Matriz_Final[l_final+1][c_final+1] = valores + 1
			Matriz_Final[l_final+1][c_final] = valores + 2
			Matriz_Final[l_final][c_final+1] = valores + 3

		l_bkp = l_auxiliar
		c_bkp = c_auxiliar
		l_auxiliar -= 1
		c_auxiliar += 1

		if l_auxiliar < 0:
			l_auxiliar = len(M) - 1
		if c_auxiliar > len(M[0]) - 1:
			c_auxiliar = 0

		l_final = l_auxiliar * 2
		c_final = c_auxiliar * 2

		if Matriz_Final[l_final][c_final] != 0:
			l_auxiliar = l_bkp + 1
			c_auxiliar = c_bkp
			l_final = l_auxiliar * 2
			c_final = c_auxiliar * 2

	for linha in range(n): #print matriz final
		for coluna in range(n):
			print(f"{Matriz_Final[linha][coluna]}", end ="\t")
		print("")

#============================================================================================================================

def DescobreCaso(n:int):
	if n % 2 != 0:
		print("Caso 1:")
		CasoUm(n)
	
	elif n % 4 == 0:
		for i in range(1, n):
			if 4 * i == n:
				m = i	
				print("Caso 2:")
				#print(f"m = {m}")
				CasoDois(n, m)
				break
	
	else:
		for i in range(1, n):
			if 4 * i + 2 == n:
				m = i
				#print(f"m = {m}")
				print("Caso 3:")
				CasoTres(n,m)
				break

#============================================================================================================================

def main():
	n = int(input())
	DescobreCaso(n)


main()