class RuleSettings:
    '''stores setting information on the stock market simulator'''

    def __init__(self, ruleInitString = 'default'):
        pass


    """
    1: stockDeltaMethod
    """

    def getStockDeltaMethod(self):
        """
        Gets stock delta method
        """
        return self.stockDeltaMethod

    def setStockDeltaMethod(self, settingVal):
        """
        Sets the stock delta method to the specified option

        For further information, please check the wiki.
        Arguments:
        setting -- can take on the following values: manual, elo, glicko, dwz
        """
        if settingVal not in ['manual', 'elo', 'glicko', 'dwz']:
            raise InvalidValueError("You must choose between the following options: manual, elo, glicko, dwz")
        else:
            self.stockDeltaMethod = settingVal
            return True

    """
    2: ratingSensitivity
    """

    def getRatingSensitivity(self):
        """
        Gets rating sensitivity
        """
        return self.ratingSensitivity

    def setRatingSensitivity(self, settingVal):
        """
        Sets the sensitivity of the delta method to the specified value

        For further information, please check the wiki.
        Arguments:
        settingVal -- any positive number
        """

        # internal note: refine number past positive number into a spec. range once relative scale established

        if float(settingVal) <= 0:
            raise InvalidValueError("You must insert a positive number!")
        else:
            self.ratingSensitivity = settingVal
            return True

    """
    3: useGameScores
    """

    def getUseGameScores(self):
        """
        Gets use game scores value
        """
        return self.useGameScores

    def setUseGameScores(self, settingVal):

        if settingVal.lower() not in ['t', 'true', '1', 'f', 'false', '0']:
            raise InvalidValueError("You must insert a True/False value.")
        else:
            if settingVal.lower() in ['t', 'true', '1']:
                self.useGameScores = True
            else:
                self.useGameScores = False
            return True
