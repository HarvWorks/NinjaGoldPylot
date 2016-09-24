import random
import time
from system.core.controller import *
class Gold(Controller):
    """docstring for Gold."""
    def __init__(self, action):
        super(Gold, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db
    def index(self):
        if not "gold" in session:
            session['gold'] = 0
            session["activity"] = ''
        return self.load_view('index.html')
    def process(self):
        if request.form['action'] == 'farm':
            tempGold = random.randrange(10,20)
            session["gold"] += tempGold
            session["activity"] += "<p style='color:green;'>Earned " + str(tempGold) + " gold coins from farming backwheat! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
        elif request.form['action'] == 'house':
            tempGold = random.randrange(10,12)
            session["gold"] += tempGold
            session["activity"] += "<p style='color:green;'>Earned " + str(tempGold) + " gold coins from cleaning someone's filty house! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
        elif request.form['action'] == 'cave':
            tempGold = random.randrange(0,30)
            session["gold"] += tempGold
            session["activity"] += "<p style='color:green;'>Earned " + str(tempGold) + " gold coins from exploring a creepy cave! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
        elif request.form['action'] == 'seaside':
            tempGold = random.randrange(5,15)
            session["gold"] += tempGold
            session["activity"] += "<p style='color:green;'>Earned " + str(tempGold) + " gold coins from looking for sea shells! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
        elif request.form['action'] == 'gamble':
            tempGold = random.randrange(-120,100)
            session["gold"] += tempGold
            if tempGold >= 0:
                session["activity"] += "<p style='color:green;'>Earned " + str(tempGold) + " gold coins from playing blackjack! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
            else:
                session["activity"] += "<p style='color:red;'>Lost " + str(abs(tempGold)) + " gold coins from playing the slots... You should stop gambling and losing your life savings! &nbsp;&nbsp;" + time.strftime("%d %b %Y") + " &nbsp;" + time.strftime("%I:%M:%S %p") + "</p>"
        elif request.form['action'] == 'reset':
            session["gold"] = 0
            session["activity"] = ""
        return redirect('/')
