from players import Player
from squads import Squad

Me=Squad()
with open('Python/FantasyFootball/Team.txt') as f:
    for line in f.readlines():
        [name,team,POS,currValue,buyValue]=[x for x in line.split()]
        Me.add_to_available(Player(name,team,POS,int(currValue)))
        Me.buy(POS,name,int(buyValue))

with open('Python/FantasyFootball/Available.txt') as f:
    for line in f.readlines():
        [name,team,POS,currValue]=[x for x in line.split()]
        Me.add_to_available(Player(name,team,POS,int(currValue)))



Me.show_team_n_predicted_points(2)
