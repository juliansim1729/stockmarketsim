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

        """
