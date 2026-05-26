from colorama import init, Fore
from database import create_db, insert_task, select, update, delete, dash_pendentes_concluidas

init(autoreset=True)


def cad_tasks():
    t = input("Título: ")
    d = input("Descrição: ")
    p = input("Prioridade (Baixa/Média/Alta): ") or "Média"

    insert_task(t, d, p)
    print(Fore.GREEN + "\nTarefa cadastrada com sucesso!\n")


def lista_tasks():
    tasks = select()

    if not tasks:
        print(Fore.RED + "Nenhuma tarefa cadastrada.\n")
        return

    for t in tasks:
        print(f"""
ID: {t[0]}
Título: {t[1]}
Descrição: {t[2]}
Prioridade: {t[3]}
Status: {t[4]}
Criada em: {t[5]}
Concluída em: {t[6]}
""")
        print("-" * 30)


def atualiza_tasks():
    lista_tasks()

    try:
        id_task = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print(Fore.RED + "ID inválido!")
        return

    nv_status = input(
        "Novo Status (Pendente/Concluída): "
    ).strip()

    update(id_task, nv_status)

    print(Fore.GREEN + "\nTarefa atualizada com sucesso!\n")

def delete_task():
    id = int(input("Digite o ID da tarefa:"))
    confirm = input("Confirma a exclusão? (S/N): ").strip().upper()

    if confirm.upper == "S":
        delete(id)
        print("Tarefa excluida com sucesso")
    else:
        print("Exclusão Cancelada")


def relatorio():
    retorno = dash_pendentes_concluidas()
    if retorno:
        total = sum([r[1] for r in retorno])
        print('\n=== RELATÓRIO DE TAREFAS===')
        for status, count in retorno:
            percent = (count/total) * 100
            print(f'{status}: {count} tarefas ({percent:.1f}%)')
            print(f"Total de tarefas {total}\n")
    else:
        print("nenhuma tarefa cadastrada\n")

def menu():
    create_db()

    while True:
        print("\n=====================================")
        print("ANOTA TASK - GERENCIADOR DE TAREFAS")
        print("=====================================\n")

        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Atualizar tarefa")
        print("4 - Excluir tarefa")
        print("5 - Relatório")
        print("6 - Sair")

        op = input("\nDigite a opção desejada: ")

        match op:
            case "1":
                print(15*'-')
                print("Cadastrar Tarefa")
                print(15*'-')
                cad_tasks()

            case "2":
                print(15*'-')
                print("Listar Tarefa")
                print(15*'-')
                lista_tasks()

            case "3":
                print(15*'-')
                print("Atualizar Tarefa")
                print(15*'-')
                atualiza_tasks()

            case "4":
                print(15*'-')
                print("Deletar Tarefa")
                print(15*'-')
                delete_task()

            case "5":
                relatorio()

            case "6":
                print("Saindo...")
                break

            case _:
                print(Fore.RED + "Opção inválida")


if __name__ == "__main__":
    menu()