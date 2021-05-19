class Market:

    def __init__(self):
        self.stockNames = []
        self.stockCodes = []
        self.stockPrices = []
        self.quants = []

    def addNewStock(self, sName, sCode, currSys, desiredDelta = 0):
        currStartingPrice = currSys.savedSettings.stockStartingPrice

        self.stockNames.append(sName)
        self.stockCodes.append(sCode)
        self.stockPrices.append(currStartingPrice + desiredDelta)
        self.quants.append(0)
