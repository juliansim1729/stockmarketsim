class RuleSettings:
    """stores setting information on the stock market simulator"""

    def __init__(self, ruleInitString = 'default'):
        pass


    """
    1: stockDeltaMethod: Setting Type: Ratings
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
    2: ratingSensitivity: Setting Type: Ratings
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
    3: useOverallScores:  Setting Type: Ratings
    """

    def getUseOverallScores(self):
        """
        Gets use game scores value
        """

        return self.useGameScores

    def setUseOverallScores(self, settingVal):
        """
        Sets whether overall game score is used or internal game score

        (Whether a game is counted as 1-0 or 4-2)
        Arguments:
        settingVal -- True/False
        """

        if settingVal.lower() not in ['t', 'true', '1', 'f', 'false', '0']:
            raise InvalidValueError("You must insert a True/False value.")
        else:
            if settingVal.lower() in ['t', 'true', '1']:
                self.useOverallScorse = True
            else:
                self.useOverallScores = False
            return True

    """
    4: useFirstTo: Setting Type: Ratings
    """

    def getUseFirstTo(self):
        """
        Gets use first to value
        """

        return self.useFirstTo

    def setUseFirstTo(self, settingVal):
        """
        Sets whether the games conclude when a side hits a certain amount of wins vs a set amount of games are played

        (First to 4 vs Everyone plays 7 games)
        Arguments:
        settingVal -- True/False
        """

        if self.useOverallScores == True:
            raise IncompatibleSettingError("Overall scores cannot be used with this setting.")
        else:
            if settingVal.lower() not in ['t', 'true', '1', 'f', 'false', '0']:
                raise InvalidValueError("You must insert a True/False value.")
            else:
                if settingVal.lower() in ['t', 'true', '1']:
                    self.useFirstTo = True
                else:
                    self.useFirstTo = False
                return True
