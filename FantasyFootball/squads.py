class Squad():
    def __init__(self):
        self.team={'GKP':{},'DEF':{},'MID':{},'FWD':{}}
        self.available={'GKP':{},'DEF':{},'MID':{},'FWD':{}}
        self.ITB=0
        self.GW=1
        self.fixtures={team:[i for i in range(39)] for team in teams()}

    def add_to_available(self,player):
        assert player.name not in self.team[player.position], "Error: player already in team"        
        assert player.name not in self.available[player.position], "Error: player already in available"
        self.available[player.position][player.name]=player

    def buy(self,POS,player_in,buyValue=-1):
        assert player_in not in self.team[POS], "Player already in team"
        assert player_in in self.available[POS], "Player not in available"
        p_in=self.available[POS].pop(player_in)
        p_in.buy(buyValue)
        self.team[POS][player_in]=p_in

    def transfer(self,POS,player_in,player_out):
        assert player_out in self.team[POS], "Player out not in team"
        assert player_in in self.available[POS], "Player in not in available"
        myValue=self.team[POS][player_out].myValue
        newValue=self.available[POS][player_in].currValue
        loss=newValue-myValue
        p_out=self.team[POS].pop(player_out)
        p_in=self.available[POS].pop(player_in)
        p_out.sell()
        p_in.buy()
        self.team[POS][player_in]=p_in
        self.available[POS][player_out]=p_out
        self.ITB-=loss
    
    def update_ITB(self,itb):
        assert isinstance(itb, int), 'Error: ITB not an integer' 
        if itb<0:
            print('Warning: ITB negative\n')
        if itb>1000:
            print('Warning: ITB too large\n')
        self.ITB=itb

    def update_fixtures(self,team,GW,new):
        self.fixtures[team][GW]=new

    def show_fixtures(self,teams,GW_start,GW_end):
        for team in teams:
            print(team+":")
            print(self.fixtures[team][GW_start:GW_end+1])

    def show_n_fixtures(self,teams,n):
        for team in teams:
            print(team+":")
            print(self.fixtures[team][self.GW:self.GW+n])

    def show_team_predicted_points(self,GW_start,GW_end):
        for POS in self.team:
            for name,player in self.team[POS].items():
                print(name)
                print(player.return_predicted_points(GW_start,GW_end))

    def show_team_n_predicted_points(self,n):
        for POS in self.team:
            for name,player in self.team[POS].items():
                print(name)
                print(player.return_predicted_points(self.GW,self.GW+n-1))
            
    def show_predicted_points(self,players,GW_start,GW_end):
        for POS in self.team:
            for name,player in self.team[POS].items():
                if name in players:
                    print(name)
                    print(player.return_predicted_points(GW_start,GW_end))
        for POS in self.available:
            for name,player in self.available[POS].items():
                if name in players:
                    print(name)
                    print(player.return_predicted_points(GW_start,GW_end))
    
    def show_n_predicted_points(self,players,n):
        for POS in self.team:
            for name,player in self.team[POS].items():
                if name in players:
                    print(name)
                    print(player.return_predicted_points(self.GW,self.GW+n-1))
        for POS in self.available:
            for name,player in self.available[POS].items():
                if name in players:
                    print(name)
                    print(player.return_predicted_points(self.GW,self.GW+n-1))

    def check_valid_team(self):
        count=teams()
        for POS in self.team:
            for name,player in self.team[POS].items():
                count[player.team]+=1
        for team,n in count.items():
            if n>3:
                print("Too many players from",team)
                return False
        if len(self.team["GKP"])!=2:
            print("Incorrect number of GKP")
            return False
        if len(self.team["DEF"])!=5:
            print("Incorrect number of DEF")
            return False
        if len(self.team["MID"])!=5:
            print("Incorrect number of MID")
            return False
        if len(self.team["FWD"])!=3:
            print("Incorrect number of FWD")
            return False
        return True
        
    def print_all(self):
        self.print_team()
        self.print_squad_value()
        self.print_available()

    def print_squad_value(self):
        print("Squad Value:")
        total=0
        for POS in self.team:
            curr=0
            for player in self.team[POS]:
                curr+=self.team[POS][player].myValue
            print(POS+':',curr)
            total+=curr
        print ('Total:',total)
        print("ITB:",self.ITB)
        print("")

    def print_team(self):
        print('Current Team:')
        for POS in self.team:
            print(POS+':',{player for player in self.team[POS].keys()})
        print("")
    
    def print_team_with_values(self):
        print('Current Team:')
        for POS in self.team:
            print(POS+':',{name:[player.currValue,player.myValue,player.buyValue] for name,player in self.team[POS].items()})
        print("")
    

    def print_available(self):
        print('Available Players:')
        for POS in self.available:
            print(POS+':',{player for player in self.available[POS].keys()})
        print("")

def teams():
    return {"ARS":0,"AVL":0,"BRI":0,"BUR":0,"BRE":0,"CHE":0,"CRY":0,"EVE":0,"LEE":0,"LEI":0,"LIV":0,"MCI":0,"MUN":0,"NEW":0,"NOR":0,"SOU":0,"TOT":0,"WAT":0,"WHU":0,"WOL":0}