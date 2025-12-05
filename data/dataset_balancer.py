import json
import random

# --- CONFIGURAÇÕES ---
INPUT_FILE = 'dataset.json'  # Seu arquivo original
OUTPUT_FILE = 'dataset_teste_balanceado.json'
TOTAL_SAMPLES = 200  # Tamanho total do teste (dividido igualmente entre as classes)

def balance_dataset():
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo {INPUT_FILE} não encontrado.")
        return

    # 1. Separar as classes
    misoginos = [item for item in data if item['output'] == 'misogino']
    nao_misoginos = [item for item in data if item['output'] == 'nao_misogino']

    print(f"Total encontrado no original: {len(misoginos)} Misóginos, {len(nao_misoginos)} Não-Misóginos.")

    # 2. Calcular quantidade por classe
    samples_per_class = TOTAL_SAMPLES // 2
    
    # Validação de quantidade
    if len(misoginos) < samples_per_class or len(nao_misoginos) < samples_per_class:
        print(f"AVISO: Você pediu {TOTAL_SAMPLES} amostras, mas não há dados suficientes.")
        min_available = min(len(misoginos), len(nao_misoginos))
        samples_per_class = min_available
        print(f"Ajustando para {samples_per_class * 2} amostras totais.")

    # 3. Amostragem Aleatória
    selected_misoginos = random.sample(misoginos, samples_per_class)
    selected_nao_misoginos = random.sample(nao_misoginos, samples_per_class)

    # 4. Combinar e Embaralhar (Shuffle)
    final_dataset = selected_misoginos + selected_nao_misoginos
    random.shuffle(final_dataset)

    # 5. Salvar
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_dataset, f, indent=2, ensure_ascii=False)

    print(f"✅ Sucesso! Novo dataset criado em '{OUTPUT_FILE}' com {len(final_dataset)} itens.")

if __name__ == "__main__":
    balance_dataset()