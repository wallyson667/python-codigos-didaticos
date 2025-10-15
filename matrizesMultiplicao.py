def mat_mul (A, B):
# A palavra-chave "DEF" declara uma função; os argumentos vão entre parênteses. As funções podem retornar valores e tipos básicos (lista...)
    num_linhas_A, num_colunas_A = len(A), len(A[0])
# A função "LEN", quando aplicada a um string, retorna o número de caracteres no string (ou seja, o seu comprimento).
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_colunas_A == num_linhas_B
# Python "ASSERT" é basicamente um auxiliar de depuração que testa a condição de auto-verificação interna do seu código

    C = []
    for linha in range(num_linhas_A):
        # começando uma nova linha
        C.append([])
        for coluna in range(num_colunas_B):
            # adicionando uma nova coluna na linha
            C[linha].append(0)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    print(mat_mul (A, B))
    

# "FOR" Enquanto percorremos a lista de valores, a variável indicada no for receberá, a cada iteração, um item da coleção. A instrução for percorre...
# "IN" O operador in verifica se o operando a sua esquerda, está contido na lista a sua direita...
# "RANGE" é utilizada como auxiliar da função for. Em Python, podemos repetir uma ação por um número específico de vezes usando um loop for com a função range...
# "APPEND" append (x) Adiciona um item ao fim da lista...
# "RETURN" A mesma funciona também para finalizar a execução do bloco de instrução da função, retornado assim, o valor que estiver a sua frente...
# "IF" Utilizamos o comando if para verificar uma expressão e executar um bloco de código caso a condição definida seja verdadeira...

                
