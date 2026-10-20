class Lampadina:
    def __init__(self, clickMax):
        self.str_stato = "SPENTO"
        self.clickMax = clickMax 
        self.clicks = 0
        self.correntePresente = False

    def click(self):
        if self.clicks >= self.clickMax:
            self.str_stato = "ROTTA"
        elif self.correntePresente:   
            if self.str_stato == "SPENTO":
                self.str_stato = "ACCESO"
                self.clicks +=1
            else:
                self.str_stato = "SPENTO"
                self.clicks +=1
        else:
            self.clicks +=1

    def stato(self):
        return self.str_stato

    def spegniCorrente(self):
        self.correntePresente = False

    def riattivaCorrente(self):
        self.correntePresente = True

    def ripara(self):
        self.str_stato = "SPENTO"
        self.clicks = 0

    def toString(self):
        return f"Lampadina(stato:{self.str_stato}, click residui:{self.clickMax - self.clicks})"

class Interruttore:
    def __init__(self, lampadina = None):
        self.lampadina = lampadina

    def usa(self):
        if self.lampadina is not None:
            self.lampadina.click()

    def toString(self):
        if self.lampadina is not None:
            return f"Interruttore collegato a lampadina(stato:{self.lampadina.stato()})"
        else:
            return "Interruttore non collegato a nessuna lampadina"