import math

def is_perfect_square(x: int) -> bool:
    """
    Verifica se um número é um quadrado perfeito.

    Args:
        x (int): O número a ser verificado.

    Returns:
        bool: True se o número for um quadrado perfeito, False caso contrário.
    """
    s = int(math.sqrt(x))
    return s * s == x
    
def belongs_to_fibonacci(n: int) -> bool:
    """
    Verifica se um número pertence à sequência de Fibonacci.

    A sequência de Fibonacci é composta por números em que cada número, a partir do terceiro, 
    é a soma dos dois anteriores. Um número pertence à sequência se, e somente se, 
    (5 * n^2 + 4) ou (5 * n^2 - 4) for um quadrado perfeito.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se o número pertence à sequência de Fibonacci, False caso contrário.
    """
    try:
        n = int(n)
    except ValueError:
        raise ValueError("A entrada deve ser um número inteiro ou uma string que represente um número inteiro.")
    
    if n < 0:
        return False 
        
    x1 = 5 * n**2 + 4
    x2 = 5 * n**2 - 4
    return is_perfect_square(x1) or is_perfect_square(x2)

# Testando o algoritmo:
if __name__ == "__main__":
    try:
        num = input("Digite um número para saber se ele pertence à sequência de Fibonacci:")
        if belongs_to_fibonacci(num):
            print(f"{num} pertence à sequência de Fibonacci!")
        else:
            print(f"{num} não pertence à sequência de Fibonacci!")
    except ValueError as e:
        print(f"Erro: {e}")

