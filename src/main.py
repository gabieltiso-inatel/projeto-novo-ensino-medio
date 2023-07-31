import json
import os

operations = {
        "Novo quiz": 0,
        "Listar quizzes": 1,
        "Listar informações de um quiz": 2,
        "Deletar quiz": 3,
        "Editar nome do quiz": 4,
        "Editar tema do quiz": 5,
        "Jogar quiz": 6,
        "Novo flashcard": 7,
        "Deletar flashcard": 8,
        "Editar pergunta do flashcard": 9,
        "Editar resposta do flashcard": 10,
        "Sair": 11
}

# Operações com arquivos, salvar e carregar os quizzes
def load_quizzes_file(path):
    with open(path, "r") as json_file:
        quizzes = json.load(json_file)

    return quizzes

def save_quizzes_to_file(path, quizzes):
    with open(path, "w+") as json_file:
        json.dump(quizzes, json_file, indent=4)

# Operações nos quizzes:
def new_quiz(quizzes, name, theme):
    quizzes.append({
        "name": name,
        "theme": theme,
        "flashcards": []
    })

def list_quizzes(quizzes):
    if len(quizzes) == 0:
        print("Nenhum quiz foi criado até o momento!")
        return

    print("Quizzes disponíveis: ")
    for i in range(len(quizzes)):
        quiz = quizzes[i]
        print(f"{i}) {quiz['name']} ({quiz['theme']}): {len(quiz['flashcards'])} flashcards")

def list_quiz_info(quiz):
    print(f"{quiz['name']} ({quiz['theme']}): {len(quiz['flashcards'])} flashcards")

    if len(quiz["flashcards"]) == 0:
        print("Esse quiz não tem flashcards!")
        return

    for i in range(len(quiz["flashcards"])):
        flashcard = quiz["flashcards"][i]
        print(f"{i})") 
        print(f"Pergunta: {flashcard['question']}")
        print(f"Resposta: {flashcard['answer']}")

def delete_quiz_by_name(quizzes, name):
    for i in range(len(quizzes)):
        if (quizzes[i]["name"]).lower() == name.lower():
            del quizzes[i]
            break

def delete_quiz_by_index(quizzes, index):
    del quizzes[index]

def edit_quiz_name(quiz, new_name):
    quiz["name"] = new_name

def edit_quiz_theme(quiz, new_theme):
    quiz["theme"] = new_theme

def play_quiz(quiz):
    if len(quiz["flashcards"]) == 0:
        print("Não existem flashcards nesse quiz!")
        return

    correct_answers = 0
    for flashcard in quiz["flashcards"]:
        print(f"{flashcard['question']}")
        command = input("[q] - Abandonar quiz, [r] - Mostrar resposta: ")

        if command == "q":
            print("Abandonando o quiz. Até mais!")
            return

        print(f"Resposta: {flashcard['answer']}")
        answer_status = input("[c] - Se você acertou, [e] - Se você errou: ")
        if answer_status == "c":
            correct_answers += 1

    print(f"Fim do quiz! Você acertou {correct_answers} de {len(quiz['flashcards'])} perguntas!")

# Operações nos flashcards
def new_flashcard(quiz, question, answer):
    quiz["flashcards"].append({
        "question": question,
        "answer": answer 
    })

def delete_flashcard(quiz, index):
    del quiz["flashcards"][index]

def edit_flashcard_question(quiz, index, new_question):
    selected_flashcard = quiz["flashcards"][index]
    selected_flashcard["question"] = new_question

def edit_flashcard_answer(quiz, index, new_answer):
    selected_flashcard = quiz["flashcards"][index]
    selected_flashcard["answer"] = new_answer

def main():
    if os.path.exists("quizzes.json"):
        quizzes = load_quizzes_file("quizzes.json")
    else:
        quizzes = []

    while True:
        print()
        for operation_name, operation_index in operations.items():
            print(f"{operation_index}) {operation_name}")
        selected_operation = int(input("Selecione a operação desejada: "))
        print()

        if selected_operation == 0:
            name = input("Nome do quiz: ")
            theme = input("Tema geral do quiz: ")
            new_quiz(quizzes, name, theme)
            print("Quiz criado com sucesso!")
        elif selected_operation == 1:
            list_quizzes(quizzes)
        elif selected_operation == 2:
            index = int(input("Digite o índice do quiz que você deseja listar as informações: "))
            list_quiz_info(quizzes[index])
        elif selected_operation == 3:
            index = int(input("Digite o índice do quiz que você deseja deletar: "))
            delete_quiz_by_index(quizzes, index)
        elif selected_operation == 4:
            index = int(input("Digite o índice do quiz que você deseja deletar: "))
            new_name = input("Digite um novo nome para o quiz: ")
            edit_quiz_name(quizzes[index], new_name)
        elif selected_operation == 5:
            index = int(input("Digite o índice do quiz que você deseja deletar: "))
            new_theme = input("Digite um novo tema para o quiz: ")
            edit_quiz_theme(quizzes[index], new_theme)
        elif selected_operation == 6:
            index = int(input("Digite o índice do quiz que você deseja praticar: "))
            play_quiz(quizzes[index])
        elif selected_operation == 7:
            index = int(input("Digite o índice do quiz que conterá o flashcard: "))
            question = input("Pergunta do flashcard: ")
            answer = input("Resposta do flashcard: ")
            new_flashcard(quizzes[index], question, answer)
        elif selected_operation == 8:
            quiz_index = int(input("Digite o índice do quiz em que o flashcard está presente: "))
            flashcard_index = int(input("Digite o índice do flashcard que você deseja deletar: "))
            delete_flashcard(quizzes[quiz_index], flashcard_index)
        elif selected_operation == 9:
            quiz_index = int(input("Digite o índice do quiz em que o flashcard está presente: "))
            flashcard_index = int(input("Digite o índice do flashcard cuja pergunta você deseja alterar: "))
            new_question = input("Digite a nova pergunta do flashcard: ")
            edit_flashcard_question(quizzes[quiz_index], flashcard_index, new_question)
        elif selected_operation == 10:
            quiz_index = int(input("Digite o índice do quiz em que o flashcard está presente: "))
            flashcard_index = int(input("Digite o índice do flashcard cuja resposta você deseja alterar: "))
            new_answer = input("Digite a nova resposta do flashcard: ")
            edit_flashcard_answer(quizzes[quiz_index], flashcard_index, new_answer)
        elif selected_operation == 11:
            save_quizzes_to_file("quizzes.json", quizzes)
            print("Até mais!")
            break
        else:
            print("Operação não suportada")

if __name__ == "__main__":
    main() 
