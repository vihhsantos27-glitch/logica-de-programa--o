# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: vitoria santos
# Data:18/09
# Link do Repositório:
# ==============================================================================

# Lista inicial de dados brutos (Exemplo: Sistema de RH / Atendimento)
# Os dados estão no formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA (Mínimo de 3 funções)
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
    """
    FUNÇÃO 1:
    - Deve receber uma string.
    - Deve remover espaços extras das pontas (.strip()).
    - Deve converter o texto para letras MAIÚSCULAS (.upper()).
    - Retorna o texto devidamente formatado.
    """
    # Remove os espaços em branco do início e do fim da string
    texto = texto.strip()

    # Converte todos os caracteres para letras maiúsculas
    texto = texto.upper()

    return texto


def extrair_codigo_ou_ddd(dado):
    """
    FUNÇÃO 2:
    - Deve receber um dado em formato de string (ex: telefone ou CPF).
    - Deve remover espaços das pontas.
    - Deve utilizar FATIAMENTO DE STRING [x:y] para extrair os 2 primeiros
      dígitos (ex: DDD).
    - Retorna apenas os dígitos extraídos.
    """
    # Limpa os espaços antes de fatiar, para não pegar espaço no lugar do dígito
    dado = dado.strip()

    # Fatiamento de string: pega da posição 0 até a 1 (os 2 primeiros caracteres)
    codigo = dado[0:2]

    return codigo


def processar_e_exibir_cadastros(lista_dados):
    """
    FUNÇÃO 3:
    - Deve receber a lista de cadastros brutos como parâmetro.
    - Deve utilizar um laço FOR para percorrer cada item da lista.
    - Em cada iteração do for:
        1. Separar as partes usando .split(";")
        2. Chamar a Função 1 para formatar o Nome e o Cargo.
        3. Chamar a Função 2 para extrair o DDD/Código do telefone.
        4. Exibir o resultado final formatado na tela com f-string.
    - Retorna a quantidade total de registros processados.
    """
    # Contador de registros processados com sucesso
    total_processado = 0

    # Laço FOR percorrendo cada cadastro bruto da lista
    for item in lista_dados:
        # Divide a string bruta nos três campos: nome, cargo e telefone
        partes = item.split(";")

        # Validação: ignora registros incompletos para o programa não quebrar
        if len(partes) < 3:
            print(f"Registro inválido ignorado: {item.strip()}")
            continue

        # Reuso da Função 1 para formatar dois campos diferentes
        nome = limpar_e_formatar_texto(partes[0])
        cargo = limpar_e_formatar_texto(partes[1])

        # Chamada da Função 2 para extrair o DDD do telefone
        codigo = extrair_codigo_ou_ddd(partes[2])

        # Exibição do resultado final usando f-string
        print(f"Nome: {nome} | Cargo/Setor: {cargo} | DDD/Código: {codigo}")

        total_processado += 1

    return total_processado


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL (FLUXO DE EXECUÇÃO)
# ------------------------------------------------------------------------------

def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    # Chamada da Função 3 passando a lista 'dados_brutos'
    total = processar_e_exibir_cadastros(dados_brutos)

    # Mensagem final com a quantidade total de registros processados
    print(f"\nTotal de registros processados: {total}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO              ")
    print("==================================================")


# Execução do programa
if __name__ == "__main__":
    main()