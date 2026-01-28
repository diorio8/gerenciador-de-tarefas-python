# Programa de gerenciador de tarefas

# Listas de tarefas

tarefas = []

# função para salvar as tarefas no arquivo tarefas.txt
def salvar_tarefas():
  """salva todas as tarefas no arquivo tarefas.txt"""
  with open("tarefas.txt", "w", encoding="utf-8") as f:
    for t in tarefas:
      f.write(t + "\n")
      
#ler as tarefas que ja estavam salvas no arquivo
try:
  with open("tarefas.txt", "r", encoding="utf-8") as f:
    tarefas = [linha.strip() for linha in f.readlines()]
except FileNotFoundError:
  tarefas = []

# função para adicionar uma nova tarefa
def adicionar_tarefa(tarefa):
  """adiciona uma nova tarefa à lista, se não estiver duplicada"""
  if tarefa not in tarefas:
    tarefas.append(tarefa)
    salvar_tarefas()
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
  else:
    print(f"Tarefa '{tarefa}' já existe.")

#tarefas iniciais
tarefas_iniciais = [
"estudar Python - funções e listas",
"fazer exercícios de git e github",
"atualizar perfil LinkedIn",
"planejar cronograma semanal de estudos",
"revisar código do projeto",
"testar nova funcionalidades de algum projeto novo",
]

# adicionar as tarefas iniciais só se não estiverem na lista
for t in tarefas_iniciais:
  adicionar_tarefa(t)

# função para listar todas as tarefas
def listar_tarefas():
    """mostra todas as tarefas na lista"""
    if len(tarefas) == 0:
        print("Não há tarefas para listar.")
    else:
        print("lista de tarefas:")
        for i, t in enumerate(tarefas, start=1):
            print(f"{i}. {t}")

# chamada da função para listar todas as tarefas
#listar_tarefas()
def marcar_concluida(numero): # função para marcar uma tarefa como concluída
    if numero < 1 or numero > len(tarefas): # verificar se o número da tarefa é válido  
        print("Número de tarefa inválido.")
    else: # se o número da tarefa é válido, marcar a tarefa como concluída
        tarefa = tarefas[numero - 1] # obter a tarefa a partir do número
        if tarefa.startswith("✓"): # verificar se a tarefa já está concluída
          print(f"A tarefa '{tarefa}'já está concluída.")
        else: # se a tarefa não está concluída, marcar a tarefa como concluída
          tarefas[numero - 1] = tarefa + " ✓" # adicionar o símbolo de check à tarefa  
          salvar_tarefas() # salva alteração no arquivo
          print(f"Tarefa '{tarefa}' marcada como concluída.") # mostrar a tarefa concluída
      
#testando o codigo
listar_tarefas()
marcar_concluida()
