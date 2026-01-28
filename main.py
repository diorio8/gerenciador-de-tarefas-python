# Programa de gerenciador de tarefas

# Listas de tarefas

tarefas = []
# Função para adicionar tarefas

def adicionar_tarefa(tarefa):
  """ 
  adiciona uma nova tarefa a lista de tarefas.
  parâmetro:
  tarefa (str): texto da tarefa a ser adicionada
  """
  if tarefa:    # verificar se a tarefa não está vazia
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
  else:
    print("Não é possivel adicionar uma tarefa.")
  
# chamadas da função
adicionar_tarefa("Estudar Python - funções e listas")
adicionar_tarefa("Fazer exercícios de git e github")
adicionar_tarefa("Atualizar perfil LinkedIn")
adicionar_tarefa("Planejar cronograma semanal de estudos")
adicionar_tarefa("Revisar código do projeto")
adicionar_tarefa("Testar nova funcionalidades de algum projeto novo")

# mostrar todas as tarefas
#print(tarefas)

# função para listar todas as tarefas
def listar_tarefas():
    """mostra todas as tarefas na lista"""
    if len(tarefas) == 0:
        print("Não há tarefas para listar.")
    else:
        print("lista de tarefas:")
        for i, t in enumerate(tarefas, start=1):
            print(f"{i}. {t}")

# função para listar todas as tarefas
#listar_tarefas()
