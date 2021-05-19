class User:
    """stores data at the user level"""

    def __init__(self, currSys):
        """
        initializes the user

        Arguments:
        currSys -- a GeneralSimulator object
        """
        self.availableCash = currSys.savedSettings.userStartingCash

        self.portfolio = []
        # portfolio is a list of [stock code, quant]s

    def liquidate(self, currMarket):
        """
        liquidates current portfolio and turns it entirely into cash

        Arguments:
        currMarket -- a Market object
        """
        portfolioWorth = 0

        for pkg in portfolio:
            portfolioWorth += pkg[1]*currMarket.returnPrice(pkg[0])
        self.availableCash += portfolioWorth
        self.portfolio = []
