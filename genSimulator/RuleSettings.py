class RuleSettings:
    '''stores setting information on the stock market simulator'''

    def __init__(self, ruleInitString = 'default'):
        pass
        
    def setStockDeltaMethod(self, setting):
        """
        Sets the stock delta method to the requested setting

        For further information, please check the wiki.
        Arguments:
        setting -- can take on the following values: manual, elo, glicko, dwz
        """
        if setting not in ['manual', 'elo', 'glicko', 'dwz']:
            raise InvalidValueError("You must choose between the following options: manual, elo, glicko, dwz")
        else:
            self.stockDeltaMethod = setting
