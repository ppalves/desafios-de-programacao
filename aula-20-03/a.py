def enqueue(element, database, teamQueues, teamOrder):
    team = database[element]
    if team in teamQueues:
        teamQueues[team].append(element)
    else:
        teamQueues[team] = [element]
        teamOrder.append(team)

def dequeue(teamQueues, teamOrder):
    teamOrdernew = teamOrder.copy()
    for team in teamOrder:
        if len(teamQueues[team]) == 0:
            teamOrdernew.remove(team)
        else:
            print(teamQueues[team].pop(0))
            break
    teamOrder = teamOrdernew
            



cenario = 1
number_of_teams = int(input())

while number_of_teams != 0:
    print("Scenario #" + str(cenario))

    database = {}

    teamQueues = {}

    teamOrder = []

    for i in range(number_of_teams):
        for element in input().split()[1:]:
            database[int(element)] = i + 1

    command = input().split()

    while command[0] != "STOP":
        if command[0] == "ENQUEUE":
            enqueue(int(command[1]), database, teamQueues, teamOrder)
        
        elif command[0] == "DEQUEUE":
            dequeue(teamQueues, teamOrder)
        
        command = input().split()

    number_of_teams = int(input())
    cenario += 1
    print()