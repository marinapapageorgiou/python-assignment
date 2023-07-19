#Marina Papageorgiou, A.M. 4757

import random
messages=['Put One', 'Take Two','Put All Players','Take One','Put Two','Take Them All']
number_of_players=int(input('Give the number of players:'))
number_of_beans=int(input('Give the number of beans per player:'))
players_beans = []

for player in range(number_of_players):
    players_beans.append((player+1,number_of_beans))

current_player = random.randrange(0, number_of_players)
print('First Player:', current_player+1)

Pot=0
Round=0

while True:  
    print('------------------------------------------------')
    Round=Round+1
    print('Round',Round,'begins: everyone puts 1')

    for i in  range (0,number_of_players):
        pb=players_beans[i]
        if (pb[1]!='eliminated'):
            pb=players_beans.pop(i)
            player=pb[0]
            npb=pb[1]-1
            if (npb>-1):
                Pot=Pot+1
                players_beans.insert(i,(player,npb))
            else:
                players_beans.insert(i,(player,'eliminated'))
           
           
    while (Pot>0):
        pb=players_beans[current_player]  
        if (pb[1]!='eliminated'):
            print('Current state:')
            print('Pot:',Pot)
            for pb in players_beans:
                print('Player',pb[0],'`s budget:',pb[1])
            print('\n')
        
            spinned=random.randrange(0,6)
            print('Player', current_player+1,'spinned',messages[spinned])

            if (spinned==2):
                for i in  range (0,number_of_players):
                    pb=players_beans[i]
                    if (pb[1]!='eliminated'):
                        pb=players_beans.pop(i)
                        player=pb[0]
                        npb=pb[1]-1
                        if (npb>-1):
                            Pot=Pot+1
                            players_beans.insert(i,(player,npb))
                        else:
                            players_beans.insert(i,(player,'eliminated'))
            else:
                if (spinned==0):
                    profit=-1
                else:
                    if (spinned==1):
                        profit=2
                    else:
                        if (spinned==3):
                            profit=1
                        else:
                            if (spinned==4):
                                profit=-2
                            else:
                                profit=Pot
                pb=players_beans.pop(current_player)
                player=pb[0]
                npb=pb[1]+profit
                if (npb>-1):
                    Pot=Pot-profit
                    players_beans.insert(current_player,(player,npb))
                else:
                    players_beans.insert(current_player,(player,'eliminated'))
        
        current_player=current_player+1
        if (current_player + 1>number_of_players):
            current_player=0
            
        if (Pot==0):
            print('Current state:')
            print('Pot:',Pot)
            for i in  range (0,number_of_players):
                pb=players_beans[i]   
                if (pb[1]!='eliminated'):
                    print('Player',pb[0],'`s budget:',pb[1])
                else:
                    print('Player',pb[0],' is eliminated')
            print('Pot is zero: round ends  ')
            
        players_with_beans=0
        for i in  range (0,number_of_players):
            pb=players_beans[i]
            if (pb[1]!='eliminated'):
                players_with_beans=players_with_beans+1
        
        if (players_with_beans==1):
            break

      
    if (players_with_beans==1):
        for i in  range (0,number_of_players):
            pb=players_beans[i]
            if (pb[1]!='eliminated'):
                print('Game fished: Player',pb[0],'wins.')
        break    
