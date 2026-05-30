tasks =  {}
last_index = 0

def add_task():
    """ajouter une tâche
    """
    titre = ''
    status = ''
    global last_index
    
    while len(titre) < 3:
        titre = input('Veuillez renseigner la tâche (au moins 3 caractères): ')
        
    while status not in ('oui', 'o', 'non', 'n'):
        status = input('Veuillez renseigner le status (oui ou non): ').lower()
        status = status in ('oui', 'o')


    tasks[last_index+1] = {
        "title": titre,
        "done": status
    }
    last_index += 1


def show_tasks():
    print('Liste des tâches')

    if not tasks:
        print('Aucune tâche.')
        return
    
    else:
        for position, datas in tasks.items():
            print(f'[{position}] {datas['title']} --- {"ok" if datas['done'] == True else "non ok"}')


def ask_ids():

    """Demande à l'user de renseigner les indices des tâches sur lesquelles effectuer des opérations

    Returns:
        l_ids (list[str]): contient les indices dans une liste
    """
    ids = ''
    while len(ids) < 1:
        ids = input('Veuillez saisir les positions des tâches (séparées par une virgule): ')

    l_ids = ids.split(',')
    return l_ids


def remove_task(*args):
    
    ids = []
    for arg in args:
        try:
            #tente un typecasting
            ids.append(int(arg)) #si fonctionne on rajoute l'argument au format integer

        except ValueError:
            print("Tâche introuvable")
            
    global tasks
    tasks = dict(
        filter(lambda t: t[0] not in ids, tasks.items())  ## tasks.items() returns a list of tuples. To access an element in list, we need to provide an index (integer)
        )
    #print(tasks)


def mark_completed(*args):

    for arg in args:
        try:
            arg = int(arg)
            tasks[arg][1] = True

        except KeyError: # dans le cas où `tasks[arg]` n'existe
            print("Tâche introuvable")
            

while True:
    action = input("""1. Ajouter une tâche
2. Voir les tâches
3. Marquer comme terminée
4. Supprimer une tâche
5. Quitter
""")
    
    match action:
        case '1':
            add_task()

        case '2':
            show_tasks()

        case '3':
            mark_completed(*ask_ids())
        
        case '4':
            remove_task(*ask_ids())

        case '5':
            break