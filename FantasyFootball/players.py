import math

def test_value(Value):
    assert isinstance(Value, int), 'Value Error: not an integer' 
    if Value<30 or Value>150:
        return False
    return True

class Player():
    def __init__ (self,name,team,position,currValue):
        #initialise player with name,position,currValue
        self.name=name
        assert position in {'GKP','DEF','MID','FWD'}, "Position Error"
        self.position=position
        assert team in teams(), "Team Error"
        self.team=team
        assert test_value(currValue),"Current Value Error: unexpected value"
        self.currValue=currValue
        self.owned=False
        self.pred_points=[2+i/100 for i in range(39)]
        self.pred_points[0]=-1

    def buy(self,buyValue=-1):
        self.owned=True
        if buyValue>0:
            assert test_value(buyValue),"Value Error: unexpected value: "+str(buyValue)
            self.buyValue=buyValue
        else:
            self.buyValue=self.currValue
        self.update_myValue()
            
    def sell(self):
        self.owned=False
        self.buyValue=-1
        
    def set_value(self,Value):
        assert test_value(Value), "Price Change Error: unexpected value"
        assert abs(Value-self.currValue)<5, "Price Change Error: too much change"
        self.currValue=Value
        if self.owned:
            self.update_myValue()
    
    def update_myValue(self):
        if self.currValue<=self.buyValue:
            self.myValue=self.currValue
        else:
            gain=math.floor((self.currValue-self.buyValue)/2)
            self.myValue=self.buyValue+gain

    def return_predicted_points(self,GW_start,GW_end):
        return self.pred_points[GW_start:GW_end+1]



def teams():
    return {"ARS","AVL","BRI","BUR","BRE","CHE","CRY","EVE","LEE","LEI","LIV","MCI","MUN","NEW","NOR","SOU","TOT","WAT","WHU","WOL"}