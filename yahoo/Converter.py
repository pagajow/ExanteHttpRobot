import datetime
import pandas as pd

from yahoo.YahooFile import YahooFile


class Converter:

    def fromQuotesToRateOfReturn(self, quotesDF):
        """quotesDF
        Konwertuje DataFrame z notowaniami danego instrumentu na DataFrame ze stopa zwrotu.

        :type quotesDF: DataFrame
        :returns DataFrame z notowaniami
        :rtype DataFrame
        :return stopa zwrotu w procentach
        """
        data = {"Date": quotesDF["Date"]}
        returns = []
        for i in range(len(quotesDF)):
            r = 100*(quotesDF[YahooFile.CLOSE][i] - quotesDF[YahooFile.OPEN][i])/quotesDF[YahooFile.OPEN][i]
            returns.append(r)
        data["Returns"] = returns
        rorDF = pd.DataFrame(data, columns=["Date", "Returns"])
        return rorDF

    def toDatetime(self, datetimeStr, daily=False):
        """

        :type daily: Bool
        :type datetimeStr: str
        :rtype datetime.datetime
        """
        if daily:
            return datetime.datetime.strptime(datetimeStr, "%Y-%m-%d")
        else:
            return datetime.datetime.strptime(datetimeStr, "%Y-%m-%d").replace(day=1)

    def quotationInCurrency(self, quotesDF, currencyQuotesDF, daily=False):
        """

        :type daily: Bool
        :type currencyQuotesDF: pd.DataFrame
        :type quotesDF: pd.DataFrame
        :rtype pd.DataFrame
        """
        instrument = {}
        currency = {}
        for i in range(len(quotesDF)):
            instrument[self.toDatetime(quotesDF["Date"][i], daily)] = {
                "Open": quotesDF["Open"][i],
                "High": quotesDF["High"][i],
                "Low": quotesDF["Low"][i],
                "Close": quotesDF["Close"][i],
            }

        for i in range(len(currencyQuotesDF)):
            currency[self.toDatetime(currencyQuotesDF["Date"][i], daily)] = {
                "Open": currencyQuotesDF["Open"][i],
                "High": currencyQuotesDF["High"][i],
                "Low": currencyQuotesDF["Low"][i],
                "Close": currencyQuotesDF["Close"][i],
            }

        commonDates = list(set(instrument.keys()).intersection(currency.keys()))
        commonDates = sorted(commonDates)

        date = []
        open = []
        high = []
        low = []
        close = []
        for cd in commonDates:
            date.append(cd.strftime("%Y-%m-%d"))
            open.append(instrument[cd]["Open"] * currency[cd]["Open"])
            high.append(instrument[cd]["High"] * currency[cd]["High"])
            low.append(instrument[cd]["Low"] * currency[cd]["Low"])
            close.append(instrument[cd]["Close"] * currency[cd]["Close"])

        quotesDF = pd.DataFrame(
            {"Date": date, "Open": open, "High": high, "Low": low, "Close": close},
            columns=["Date", "Open", "High", "Low", "Close"]
        )

        return quotesDF
    
    def quotationRelative(self, quotes1DF, quotes2DF, daily=False):
        """

        :type daily: Bool
        :type quotes2DF: pd.DataFrame
        :type quotes1DF: pd.DataFrame
        :rtype pd.DataFrame
        """
        instrument1 = {}
        instrument2 = {}
        for i in range(len(quotes1DF)):
            instrument1[self.toDatetime(quotes1DF["Date"][i], daily)] = {
                "Open": quotes1DF["Open"][i],
                "High": quotes1DF["High"][i],
                "Low": quotes1DF["Low"][i],
                "Close": quotes1DF["Close"][i],
            }

        for i in range(len(quotes2DF)):
            instrument2[self.toDatetime(quotes2DF["Date"][i], daily)] = {
                "Open": quotes2DF["Open"][i],
                "High": quotes2DF["High"][i],
                "Low": quotes2DF["Low"][i],
                "Close": quotes2DF["Close"][i],
            }

        commonDates = list(set(instrument1.keys()).intersection(instrument2.keys()))
        commonDates = sorted(commonDates)

        date = []
        open = []
        high = []
        low = []
        close = []
        for cd in commonDates:
            date.append(cd.strftime("%Y-%m-%d"))
            open.append(instrument1[cd]["Open"] / instrument2[cd]["Open"])
            high.append(instrument1[cd]["High"] / instrument2[cd]["High"])
            low.append(instrument1[cd]["Low"] / instrument2[cd]["Low"])
            close.append(instrument1[cd]["Close"] / instrument2[cd]["Close"])

        quotesDF = pd.DataFrame(
            {"Date": date, "Open": open, "High": high, "Low": low, "Close": close},
            columns=["Date", "Open", "High", "Low", "Close"]
        )

        return quotesDF

    def quotationsCommonDates(self, quotesList, daily=False):
        """

        :type daily: Bool
        :type quotesList: List(pd.DataFrame)
        :rtype list(pd.DataFrame)
        """
        quotations = []
        def getInstrument(quotesDF):
            """

            :type quotesDF: pd.DataFrame
            :rtype dict
            """
            instrument = {}
            for i in range(len(quotesDF)):
                instrument[self.toDatetime(quotesDF["Date"][i], daily)] = {
                    "Open": quotesDF["Open"][i],
                    "High": quotesDF["High"][i],
                    "Low": quotesDF["Low"][i],
                    "Close": quotesDF["Close"][i],
                }
            return instrument

        instruments = []
        if len(quotesList) > 0:
            instruments.append(getInstrument(quotesList[0]))
            commonSet = set(instruments[0].keys())
            for i in range(1, len(quotesList)):
                instruments.append(getInstrument(quotesList[i]))
                commonSet = commonSet.intersection(instruments[i].keys())
            commonDates = list(commonSet)
            commonDates = sorted(commonDates)

        for instrument in instruments:
            date = []
            open = []
            high = []
            low = []
            close = []
            for cd in commonDates:
                date.append(cd.strftime("%Y-%m-%d"))
                open.append(instrument[cd]["Open"])
                high.append(instrument[cd]["High"])
                low.append(instrument[cd]["Low"])
                close.append(instrument[cd]["Close"])

            quotations.append(pd.DataFrame(
                {"Date": date, "Open": open, "High": high, "Low": low, "Close": close},
                columns=["Date", "Open", "High", "Low", "Close"]
            ))

        return quotations



