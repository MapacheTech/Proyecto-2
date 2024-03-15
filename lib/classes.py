class nodo():
    def __init__(self, valor,):
        self.valor = valor
        self.izq = None
        self.der = None
        pass
    
    def __str__(self):        
        return f"Valor:{self.valor}"
    
    def getArbol(self):
        strOut = ""
        strOut += f"NP[{self.valor}] "
        if type(self.izq) != type(None):
            strOut += f"Iz[{self.valor}]->[{self.izq}]"
        if self.der is not None:
            strOut += f"Dr[{self.valor}]->[{self.der}]"
                
        return strOut
    
    
    
    
pass