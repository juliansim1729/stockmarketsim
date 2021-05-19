class User:
    """stores data at the user level"""

    def __init__(self, currSys):
        """
        initializes the user

        Arguments:
        currSys -- a GeneralSimulator object
        """
        self.errorMessage = ""

        self.availableCash = currSys.savedSettings.userStartingCash
        self.pfCodes = []
        self.pfQuants = []

    def liquidate(self, currMarket):
        """
        liquidates current portfolio and turns it entirely into cash

        Arguments:
        currMarket -- a Market object
        """
        portfolioWorth = 0

        for i in range(len(pfCodes)):
            portfolioWorth += pfQuants[i]*currMarket.returnPrice(pfCodes[i])
        self.availableCash += portfolioWorth
        self.pfCodes = []
        self.pfQuants = []

    def buy(self, stock, quant, currMarket):
        """
        buys a certain quantity of stock

        Arguments:
        stock -- stock code for desired item
        quant -- quantity desired to buy (integer or "max")
        currMarket -- a Market object
        Returns:
        Boolean based on whether process completed successfully
        """
        try:
            if quant == "max":
                # parse max into valid number
                quant = self.availableCash // returnPrice(stock)
            if int(quant) > 0:
                if int(quant)*returnPrice(stock) <= self.availableCash:
                    if stock not in self.pfCodes:
                        self.pfCodes.append(stock)
                        self.pfQuants.append(quant)
                    else:
                        ind = self.pfCodes.index(stock)
                        self.pfQuants[ind] = self.pfQuants[ind] + quant
                    self.availableCash -= int(quant)*returnPrice(stock)
                    return True
                else:
                    raise InsufficientFundsError()
            else:
                raise InvalidValueError()
        except ValueError:
            self.errorMessage = "You must insert a positive integer value."
            return False
        except InsufficientFundsError:
            self.errorMessage = "You don't have sufficient funds to complete this transaction."
            return False
        except InvalidValueError:
            self.errorMessage = "You must insert a positive integer value."
            return False

    def sell(self, stock, quant, currMarket):
        """
        sells a certain quantity of stock

        Arguments:
        stock -- stock code for desired item
        quant -- quantity desired to sell (integer or "max")
        currMarket -- a Market object
        Returns:
        Boolean based on whether process completed successfully
        """
        try:
            availQuant = self.pfQuants[self.pfCodes.index(stock)]
            if quant == "max":
                quant = availQuant
            if int(quant) > 0:
                if int(quant) < availQuant:
                    self.pfQuants[self.pfCodes.index(stock)] = availQuant - int(quant)
                    self.availableCash += int(quant) * currMarket.returnPrice(stock)
                    return True
                elif int(quant) == availQuant:
                    self.pfQuants.pop(self.pfCodes.index(stock))
                    self.pfCodes.remove(stock)
                    self.availableCash += availQuant * currMarket.returnPrice(stock)
                    return True
                else:
                    raise NotEnoughAssetsError()
            else:
                raise InvalidValueError()
        except ValueError:
            self.errorMessage = "You must insert a positive integer value."
            return False
        except NotEnoughAssetsError:
            self.errorMessage = "You don't have sufficient assets to complete this transaction."
            return False
        except InvalidValueError:
            self.errorMessage = "You must insert a positive integer value."
            return False
