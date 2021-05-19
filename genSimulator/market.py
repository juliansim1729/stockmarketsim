class Market:

    def __init__(self):
        """
        Standard init method

        Holds information about each stock offered within the market: the name,
        the abbreviation, the price/elo, the quantity in possession of users
        Arguments:
        None
        """
        self.errorMessage = ""

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

    def removeStock(self, stock):
        """
        Removes a stock from the market

        Arguments:
        stock -- a stock to be removed, prefers CODE, then NAME, then Index (from 0)
        Returns:
        The Code of the Removed Stock, False if error happened
        """
        removedStock = ""
        sIndex = -1
        try:
            if stock in self.stockCodes:
                sIndex = self.stockCodes.index(stock)
            elif stock in self.stockNames:
                sIndex = self.stockNames.index(stock)
            elif int(stock) < len(self.stockCodes):
                sIndex = int(stock)
            else:
                raise StockNotFoundError
        except StockNotFoundError:
            self.errorMessage = "Stock not found! Please insert a valid stock."
            return False
        except ValueError:
            self.errorMessage = "You must insert a valid stock code, name, or index (from 0)."
            return False

        if sIndex > -1:
            removedStock = self.stockCodes.pop(sIndex)
            self.stockNames.pop(sIndex)
            self.stockPrices.pop(sIndex)
            self.quants.pop(sIndex)
            return removedStock
