import json

def load_data(file_path):
    """
    Carrega os dados de faturamento a partir de um arquivo JSON.

    :param file_path: Caminho para o arquivo JSON.
    :return: Lista de dicionários com os dados de faturamento.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def filter_valid_billings(billing):
    """
    Filtra os valores de faturamento, removendo dias com faturamento igual a zero.

    :param billing: Lista de dicionários com os dados de faturamento.
    :return: Lista de valores de faturamento válidos.
    """
    return [day['valor'] for day in billing if day['valor'] > 0]

def calculate_min_value(valid_billings):
    """
    Calcula o menor valor de faturamento diário.

    :param valid_billings: Lista de valores de faturamento válidos.
    :return: Menor valor de faturamento.
    """
    return min(valid_billings)

def calculate_max_value(valid_billings):
    """
    Calcula o maior valor de faturamento diário.

    :param valid_billings: Lista de valores de faturamento válidos.
    :return: Maior valor de faturamento.
    """
    return max(valid_billings)

def calculate_days_above_average(valid_billings):
    """
    Calcula o número de dias com faturamento superior à média mensal.

    :param valid_billings: Lista de valores de faturamento válidos.
    :return: Número de dias com faturamento acima da média.
    """
    monthly_average = sum(valid_billings) / len(valid_billings)
    return sum(1 for value in valid_billings if value > monthly_average)

# Testando:
if __name__ == "__main__":
    file_path = 'dados.json'
    billing = load_data(file_path)
    valid_billings = filter_valid_billings(billing)

    menor_valor = calculate_min_value(valid_billings)
    maior_valor = calculate_max_value(valid_billings)
    dias_acima_da_media = calculate_days_above_average(valid_billings)

    print(f"Menor valor de faturamento diário: {menor_valor}")
    print(f"Maior valor de faturamento diário: {maior_valor}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
