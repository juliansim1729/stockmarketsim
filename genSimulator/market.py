class Market:

    def __init__(self):
        """
        Standard init method

        Holds information about each stock offered within the market: the name,
        the abbreviation, the price/elo, the quantity in possession of users
        Arguments:
        None
        """
        self.stockNames = []
        self.stockCodes = []
        self.stockPrices = []
        self.quants = []

    def addNewStock(self, sName, sCode, currSys, desiredDelta = 0):
        """
        Adds a new stock to the market 

        Arguments:
        sName -- stock name
        sCode -- stock code/abbreviation
        currSys -- a GeneralSimulator object
        desiredDelta -- a delta for the price on default if desired
        """
        currStartingPrice = currSys.savedSettings.stockStartingPrice

        self.stockNames.append(sName)
        self.stockCodes.append(sCode)
        self.stockPrices.append(currStartingPrice + desiredDelta)
        self.quants.append(0)
