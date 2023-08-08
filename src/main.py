import json
import os

### Utilidades ###

def indice_valido(indice, valor_maximo):
    return (indice <= 0 and indice < valor_maximo)

### Persistência em arquivos ###

def carregar_arquivo_quizzes(caminho):
    """
    Carrega os quizzes a partir de um arquivo JSON.

    Args:
        caminho (str): O caminho do arquivo JSON.

    Returns:
        list: A lista de quizzes carregados.
    """
    with open(caminho, "r") as json_file:
        quizzes = json.load(json_file)
    return quizzes

def salvar_quizzes_em_arquivo(caminho, quizzes):
    """
    Salva os quizzes em um arquivo JSON.

    Args:
        caminho (str): O caminho do arquivo JSON.
        quizzes (list): A lista de quizzes a serem salvos.
    """
    with open(caminho, "w+") as json_file:
        json.dump(quizzes, json_file, indent=4)

### Operações nos quizzes ###

def novo_quiz(quizzes, nome, tema):
    """
    Cria um novo quiz e o adiciona à lista de quizzes.

    Args:
        quizzes (list): A lista de quizzes existente.
        nome (str): O nome do novo quiz.
        tema (str): O tema do novo quiz.
    """
    quizzes.append({
        "nome": nome,
        "tema": tema,
        "flashcards": []
    })

def listar_quizzes(quizzes):
    """
    Lista todos os quizzes existentes.

    Args:
        quizzes (list): A lista de quizzes existente.
    """
    if len(quizzes) == 0:
        print("Nenhum quiz foi criado até o momento!")
        return

    print("Quizzes disponíveis:")
    for i, quiz in enumerate(quizzes):
        print(f"{i}) {quiz['nome']} ({quiz['tema']}): {len(quiz['flashcards'])} flashcards")

def listar_informacoes_quiz(quiz):
    """
    Lista informações de um quiz específico.

    Args:
        quiz (dict): O dicionário que representa o quiz.
    """
    print(f"{quiz['nome']} ({quiz['tema']}): {len(quiz['flashcards'])} flashcards")

    if len(quiz["flashcards"]) == 0:
        print("Esse quiz não tem flashcards!")
        return

    for i, flashcard in enumerate(quiz["flashcards"]):
        print(f"### PERGUNTA {i} ###")
        print(f"Pergunta: {flashcard['pergunta']}")
        print(f"Resposta: {flashcard['resposta']}")
        print()

def deletar_quiz_por_indice(quizzes, indice):
    """
    Deleta um quiz da lista de quizzes pelo índice.

    Args:
        quizzes (list): A lista de quizzes existente.
        indice (int): O índice do quiz a ser deletado.
    """
    del quizzes[indice]

def editar_nome_quiz(quiz, novo_nome):
    """
    Edita o nome de um quiz.

    Args:
        quiz (dict): O dicionário que representa o quiz.
        novo_nome (str): O novo nome para o quiz.
    """
    quiz["nome"] = novo_nome

def editar_tema_quiz(quiz, novo_tema):
    """
    Edita o tema de um quiz.

    Args:
        quiz (dict): O dicionário que representa o quiz.
        novo_tema (str): O novo tema para o quiz.
    """
    quiz["tema"] = novo_tema

def jogar_quiz(quiz):
    """
    Permite jogar um quiz. Essa função primeiro checa se temos
    mais que um flashcard nesse quiz. Se sim, partimos para a 
    parte do jogo propriamente dita, que consiste em imprimir 
    todas as perguntas presentes no quiz. A função imprime a 
    pergunta e aguarda a requisição de mostrar a resposta ou 
    abandonar o quiz. Caso o usuário tenha acertado a resposta
    ele precisa indicar pressionando a tecla [c]. Caso contrário
    , a letra [e]. Em cada repetição aumentamos o número de acertos
    conforme as respostas do usuário. Isso permite mostrar o resultado
    final.

    Args:
        quiz (dict): O dicionário que representa o quiz.
    """
    if len(quiz["flashcards"]) == 0:
        print("Não existem flashcards nesse quiz!")
        return

    print()
    respostas_corretas = 0
    for flashcard in quiz["flashcards"]:
        print(f"RESPONDA A SEGUINTE PERGUNTA: {flashcard['pergunta']}")
        comando = input("[q] - Abandonar quiz, [r] - Mostrar resposta: ")

        if comando == "q":
            print("Abandonando o quiz. Até mais!")
            return

        print(f"Resposta: {flashcard['resposta']}")
        status_resposta = input("[c] - Se você acertou, [e] - Se você errou: ")
        if status_resposta == "c":
            respostas_corretas += 1

        print()

    print(f"Fim do quiz! Você acertou {respostas_corretas} de {len(quiz['flashcards'])} perguntas!")

### Operações nos flashcards ###

def novo_flashcard(quiz, pergunta, resposta):
    """
    Cria um novo flashcard e o adiciona ao quiz.

    Args:
        quiz (dict): O dicionário que representa o quiz.
        pergunta (str): A pergunta do flashcard.
        resposta (str): A resposta do flashcard.
    """
    quiz["flashcards"].append({
        "pergunta": pergunta,
        "resposta": resposta
    })

def deletar_flashcard(quiz, indice):
    """
    Deleta um flashcard do quiz pelo índice.
    O primeiro par de colchetes indica que estamos 
    acessando o campo `flashcards` do dicionário 
    quiz. Sabemos que esse campo consiste em uma 
    lista de dicionários. portanto o segundo par 
    de colchetes indica a posição desse dicionário
    na lista.

    Args:
        quiz (dict): O dicionário que representa o quiz.
        indice (int): O índice do flashcard a ser deletado.
    """
    del quiz["flashcards"][indice]

def editar_pergunta_flashcard(quiz, indice, nova_pergunta):
    """
    Edita a pergunta de um flashcard.

    Args:
        quiz (dict): O dicionário que representa o quiz.
        indice (int): O índice do flashcard.
        nova_pergunta (str): A nova pergunta para o flashcard.
    """
    quiz["flashcards"][indice]["pergunta"] = nova_pergunta

def editar_resposta_flashcard(quiz, indice, nova_resposta):
    """
    Edita a resposta de um flashcard.

    Args:
        quiz (dict): O dicionário que representa o quiz.
        indice (int): O índice do flashcard.
        nova_resposta (str): A nova resposta para o flashcard.
    """
    quiz["flashcards"][indice]["resposta"] = nova_resposta

def imprimir_opcoes():
    """
    Imprime as opções do menu.
    """
    print("Escolha uma opção:")
    print("1) Novo quiz")
    print("2) Listar quizzes")
    print("3) Listar informações de um quiz")
    print("4) Deletar quiz")
    print("5) Editar nome do quiz")
    print("6) Editar tema do quiz")
    print("7) Jogar quiz")
    print("8) Novo flashcard")
    print("9) Deletar flashcard")
    print("10) Editar pergunta do flashcard")
    print("11) Editar resposta do flashcard")
    print("12) Sair")

def ler_operacao():
    """
    Lê a operação selecionada pelo usuário.

    Returns:
        int: A operação selecionada.
    """
    while True:
        try:
            operacao_selecionada = int(input("Digite o número da operação desejada: "))
            if operacao_selecionada not in range(1, 13):
                print("Operação não suportada")
            else:
                return operacao_selecionada
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def ler_inteiro(mensagem):
    """
    Lê a operação selecionada pelo usuário.

    Returns:
        int: A operação selecionada.
    """
    while True:
        try:
            operacao_selecionada = int(input(f"{mensagem}: "))
            return operacao_selecionada
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def limpar_tela():
    """
    Limpa a tela do terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    if os.path.exists("quizzes.json"):
        quizzes = carregar_arquivo_quizzes("quizzes.json")
    else:
        quizzes = []

    while True:
        limpar_tela()
        imprimir_opcoes()
        operacao_selecionada = ler_operacao()
        limpar_tela()

        if operacao_selecionada == 1:
            nome = input("Nome do quiz: ")
            tema = input("Tema geral do quiz: ")
            novo_quiz(quizzes, nome, tema)
            print("Quiz criado com sucesso!")
        elif operacao_selecionada == 2:
            listar_quizzes(quizzes)
        elif operacao_selecionada == 3:
            indice = ler_inteiro("Digite o índice do quiz que você deseja listar as informações")
            if indice_valido(indice, len(quizzes)):
                listar_informacoes_quiz(quizzes[indice])
            else:
                print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
        elif operacao_selecionada == 4:
            indice = ler_inteiro("Digite o índice do quiz que você deseja deletar")
            if indice_valido(indice, len(quizzes)):
                deletar_quiz_por_indice(quizzes, indice)
            else:
                print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
        elif operacao_selecionada == 5:
            indice = ler_inteiro("Digite o índice do quiz que você deseja editar")
            if indice_valido(indice, len(quizzes)):
                novo_nome = input("Digite um novo nome para o quiz: ")
                editar_nome_quiz(quizzes[indice], novo_nome)
            else:
                print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
        elif operacao_selecionada == 6:
            indice = ler_inteiro("Digite o índice do quiz que você deseja editar")
            if indice_valido(indice, len(quizzes)):
                novo_tema = input("Digite um novo tema para o quiz: ")
                editar_tema_quiz(quizzes[indice], novo_tema)
            else:
                print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
        elif operacao_selecionada == 7:
            indice = ler_inteiro("Digite o índice do quiz que você deseja praticar")
            if indice_valido(indice, len(quizzes)):
                jogar_quiz(quizzes[indice])
            else:
                print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
        elif operacao_selecionada == 8:
            indice = ler_inteiro("Digite o índice do quiz em que o flashcard será criado")
            if indice_valido(indice, len(quizzes)):
                pergunta = input("Pergunta do flashcard: ")
                resposta = input("Resposta do flashcard: ")
                novo_flashcard(quizzes[indice], pergunta, resposta)
            else:
                print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
        elif operacao_selecionada == 9:
            indice_quiz = ler_inteiro("Digite o índice do quiz em que o flashcard está presente")

            if indice_valido(indice_quiz, len(quizzes)):
                indice_flashcard = ler_inteiro("Digite o índice do flashcard que você deseja deletar")
                quiz = quizzes[indice_quiz]
                if indice_valido(indice_flashcard, len(quiz["flashcards"])):
                    deletar_flashcard(quizzes[indice_quiz], indice_flashcard)
                else:
                    print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
            else:
                print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
        elif operacao_selecionada == 10:
            indice_quiz = ler_inteiro("Digite o índice do quiz em que o flashcard está presente")

            if indice_valido(indice_quiz, len(quizzes)):
                indice_flashcard = ler_inteiro("Digite o índice do flashcard cuja pergunta você deseja alterar")
                quiz = quizzes[indice_quiz]
                if indice_valido(indice_flashcard, len(quiz["flashcards"])):
                    nova_pergunta = input("Digite a nova pergunta do flashcard: ")
                    editar_pergunta_flashcard(quizzes[indice_quiz], indice_flashcard, nova_pergunta)
                else:
                    print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
            else:
                print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
        elif operacao_selecionada == 11:
            indice_quiz = ler_inteiro("Digite o índice do quiz em que o flashcard está presente")

            if indice_valido(indice_quiz, len(quizzes)):
                indice_flashcard = ler_inteiro("Digite o índice do flashcard cuja resposta você deseja alterar")
                quiz = quizzes[indice_quiz]
                if indice_valido(indice_flashcard, len(quiz["flashcards"])):
                    nova_resposta = input("Digite a nova resposta do flashcard: ")
                    editar_resposta_flashcard(quizzes[indice_quiz], indice_flashcard, nova_resposta)
                else:
                    print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
            else:
                print("Esse índice não é válido! Talvez você tenha digitado um valor maior do que o comprimento da lista, ou até mesmo um número negativo.")
        elif operacao_selecionada == 12:
            salvar_quizzes_em_arquivo("quizzes.json", quizzes)
            print("Até mais!")
            break

        _ = input("Digite qualquer coisa para continuar: ")

if __name__ == "__main__":
    main()

