class RuleSettings:
    """stores setting information on the stock market simulator"""

    def __init__(self, ruleInitString = 'default'):
        pass



    """
    1: stockDeltaMethod: Setting Type: Ratings
    """

    def getStockDeltaMethod(self):
        """
        Returns stockDeltaMethod
        """
        return self.stockDeltaMethod

    def setStockDeltaMethod(self, settingVal):
        """
        Sets the stock delta method to the specified option

        The available methods are manual which allows for manual editing of
        'stock' values, elo which uses Arpaud Elo's chess rating system,
        glicko which uses the GLICKO-2 rating system, and dwz which uses the
        Deutsche Wertunszahl. The latter are both theoretical improvements on
        the elo system.

        Arguments:
        setting -- can take on the following values: manual, elo, glicko, dwz
        Returns:
        Boolean based on whether process completed successfully
        """
        try:
            if settingVal not in ['manual', 'elo', 'glicko', 'dwz']:
                raise InvalidValueError()
            else:
                self.stockDeltaMethod = settingVal
                return True
        except InvalidValueError:
             self.errorMessage = "You must choose between the following options: manual, elo, glicko, dwz."
             return False

    """
    2: ratingSensitivity: Setting Type: Ratings
    """

    def getRatingSensitivity(self):
        """
        Returns ratingSensitivity
        """
        return self.ratingSensitivity

    def setRatingSensitivity(self, settingVal):
        """
        Sets the sensitivity of the delta method to the specified value

        A higher sensitivity will correlate to a stronger effect of recency
        on the overall rating. Therefore, higher sensitivity results in
        more spikes and larger spikes in the data whereas lower sensitivity
        creates more stable data, but much less reactive to temporal swings.

        Arguments:
        settingVal -- any positive number
        Returns:
        Boolean based on whether process completed successfully
        """

        # internal note: refine number past positive number into a spec. range once relative scale established

        try:
            if float(settingVal) <= 0:
                raise InvalidValueError()
            else:
                self.ratingSensitivity = float(settingVal)
                return True
        except InvalidValueError:
            self.errorMessage = "You must insert a positive number."
            return False

    """
    3: useOverallScores:  Setting Type: Ratings
    """

    def getUseOverallScores(self):
        """
        returns useOverallScores
        """
        return self.useOverallScores

    def setUseOverallScores(self, settingVal):
        """
        Sets whether overall game score is used or internal game score

        When this setting is True, the overall game score is used, the match is
        counted as a 1-0 win or a 0-1 loss. Otherwise, the score within the
        match is used, such as a 4-2 win, or a 1-3 loss.

        Arguments:
        settingVal -- True/False
        Returns:
        Boolean based on whether process completed successfully
        """
        try:
            if settingVal.lower() not in ['t', 'true', '1', 'f', 'false', '0']:
                raise InvalidValueError()
            else:
                if settingVal.lower() in ['t', 'true', '1']:
                    self.useOverallScores = True
                else:
                    self.useOverallScores = False
                return True
        except InvalidValueError:
            self.errorMessage = "You must insert a True/False value."
            return False

    """
    4: useFirstTo: Setting Type: Ratings
    """

    def getUseFirstTo(self):
        """
        Gets useFirstTo value
        """

        return self.useFirstTo

    def setUseFirstTo(self, settingVal):
        """
        Sets the game format type

        For example, when this setting is True, a match is considered won when a
        side first reaches game X amount of wins, whereas when the setting is False,
        a game is considered won when Y games are completed. This is used in
        combination with the rating system and a binomial probability distr.

        Arguments:
        settingVal -- True/False
        Returns:
        Boolean based on whether process completed successfully
        """
        try:
            if self.useOverallScores == True:
                raise IncompatibleSettingError()
            else:
                if settingVal.lower() not in ['t', 'true', '1', 'f', 'false', '0']:
                    raise InvalidValueError()
                else:
                    if settingVal.lower() in ['t', 'true', '1']:
                        self.useFirstTo = True
                    else:
                        self.useFirstTo = False
                    return True
        except IncompatibleSettingError:
            self.errorMessage = "Overall scores cannot be used with this setting."
            return False
        except InvalidValueError:
            self.errorMessage = "You must insert a True/False value."
            return False

    """
    5: userStartingCash: Setting Type: User Customization
    """

    def getUserStartingCash(self):
        """
        gets userStartingCash
        """

        return self.userStartingCash

    def setUserStartingCash(self, settingVal):
        """
        Sets the amount of starting cash for a user

        Arguments:
        settingVal -- non-negative Value
        Returns:
        Boolean based on whether process completed successfully
        """
        try:
            if float(settingVal) < 0:
                raise InvalidValueError()
            else:
                self.userStartingCash = float(settingVal)
                return True
        except InvalidValueError:
            self.errorMessage = "You must insert a non-negative value."
            return False
