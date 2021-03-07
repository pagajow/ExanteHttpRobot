import pandas as pd


class YahooFile:
    DATE = "Date"
    OPEN = "Open"
    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"
    ADJ_CLOSE = "Adj Close"
    VOLUME = "Volume"

    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"

    def readCSV(self, fileName):
        """
        :type fileName: String
        :rtype: pd.DataFrame
        """
        file = "assets/"+str(fileName)
        return pd.read_csv(file, ",")