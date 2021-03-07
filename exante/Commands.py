import threading
import requests


class Commands:
    data = "md"
    trade = "trade"

    def __init__(self, auth, account: str, version: str):
        self.account = account
        self.version = version
        self.auth = auth

    """ URLs:"""
    def url(self, apiPoint: str) -> str:
        return "https://api-{}.exante.eu/{}/{}/".format(self.account, apiPoint, self.version)
    def urlMd(self) -> str:
        return "https://api-{}.exante.eu/md/{}/".format(self.account, self.version)
    def urlTrade(self) -> str:
        return "https://api-{}.exante.eu/trade/{}/".format(self.account, self.version)


    def streamThread(self, func, *args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.setDaemon(True)
        t.start()


    """ API COMMANDS: """
    def getUserAccounts(self):
        """
        Return the list of user accounts and their statuses
        :return:
        """
        url = "".join([self.urlMd(), "accounts"])
        response = requests.get(url=url, auth=self.auth)

        return response

    def getAllDailyChanges(self):
        """
        Return the list of daily changes

        :return:
        """
        url = "".join([self.urlMd(), "change"])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getDailyChanges(self, symbolId: str):
        """
        Return the list of daily changes for requested instruments

        :param symbolId:    string
                            Example: MSFT.NASDAQ,AAPL.NASDAQ,GAZP.MICEX
                            symbol or comma-delimited symbols to request daily change
        :return:
        """
        url = "".join([self.urlMd(), "change/{}".format(symbolId)])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getListOfAvailableCurrencies(self):
        """
        Return the list of available currencies
        :return:
        """
        url = "".join([self.urlMd(), "crossrates"])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getCrossrate(self, fromCurrency: str, toCurrency: str):
        """
        Return the crossrate from one currency to another

        :param fromCurrency: string, from currency
        :param toCurrency: string, to currency
        :return:
        """
        url = "".join([self.urlMd(), "crossrates", "/", fromCurrency, "/", toCurrency])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getExchanges(self):
        """
        get instruments by exchange
        :return:
        """
        url = "".join([self.urlMd(), "exchanges"])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getInstrumentsByExchange(self, exchangeId: str):
        """
        Return the requested exchange financial instruments

        :param exchangeId:  string
                            Example: NASDAQ
                            exchange id to search instruments
        :return:
        """
        url = "".join([self.urlMd(), "exchanges", "/", exchangeId])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getInstrumentGroups(self):
        """
        Return list of available instrument groups
        :return:
        """
        url = "".join([self.urlMd(), "groups"])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getInstrumentsByGroup(self, groupId: str):
        """
        Return financial instruments which belong to specified group


        :param groupId: string
                        Example: NG
                        group id to search instruments
        :return:
        """
        url = "".join([self.urlMd(), "groups/", groupId])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getNearestExpirationInGroup(self, groupId: str):
        """
        Return financial instrument which has the nearest expiration in the group

        :param groupId: string
                        Example: NG
                        group id to search instruments
        :return:
        """
        url = "".join([self.urlMd(), "groups/", groupId, "/nearest"])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getInstrumentList(self):
        """
        Return list of instruments available for authorized user
        :return:
        """
        url = "".join([self.urlMd(), "symbols"])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getInstrument(self, symbolId: str):
        """
        Return instrument available for authorized user

        :param symbolId:    string
                            Example: AAPL.NASDAQ
                            instrument id to search
        :return:
        """
        url = "".join([self.urlMd(), "symbols/", symbolId])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getInstrumentSchedule(self, symbolId: str, types: bool = False):
        """
        Return financial schedule for requested instrument

        :param symbolId:    string
                            Example: AAPL.NASDAQ
                            instrument id to search

        QUERY PARAMETERS
            types   boolean
                    Example: types=true
                    show available order types
        :return:
        """
        url = "".join([self.urlMd(), "symbols/", symbolId, "/schedule"])
        params = {"types": str(types).lower()}
        response = requests.get(url=url, auth=self.auth, params=params)
        return response

    def getInstrumentSpecification(self, symbolId: str):
        """
        Return additional parameters for requested instrument

        :param symbolId:    string
                            Example: AAPL.NASDAQ
                            instrument id to search
        :return:
        """
        url = "".join([self.urlMd(), "symbols/", symbolId, "/specification"])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getInstrumentTypes(self):
        """
        Return list of known instrument types
        :return:
        """
        url = "".join([self.urlMd(), "types"])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getInstrumentsByType(self, symbolType: str):
        """
        get instruments by type

        :param symbolType:  string
                            Example: FUTURE
                            type name to search instruments
        :return:
        """
        url = "".join([self.urlMd(), "types/", symbolType])
        response = requests.get(url=url, auth=self.auth)
        return response

    # STREAM:
    def getTradesStream(self, onData, symbolIds: str):
        """
        Return the trades stream for the specified financial instrument

        :param symbolIds:   string
                            Example: MSFT.NASDAQ,AAPL.NASDAQ,GAZP.MICEX
                            financial instrument id or comma-delimited list of instruments to request trades

        HEADER PARAMETERS
            Accept
            required
                string
                Enum: "application/x-json-stream" "text/event-stream"
                Example: application/x-json-stream
                Acceptiong stream type data
        :return:
        """
        url = "".join([self.urlMd(), "feed/trades/", symbolIds])
        # Enum: "application/x-json-stream" "text/event-stream"
        header = {"Accept": "text/event-stream"}
        session = requests.Session()
        with session.get(url=url, auth=self.auth, stream=True, headers=header) as response:
            for line in response.iter_lines():
                if line:
                    onData(line)

    # STREAM:
    def getQuoteStream(self, onData, symbolIds: str):
        """
        Return the life quote stream for the specified financial instrument

        :param symbolIds:   string
                            Example: MSFT.NASDAQ,AAPL.NASDAQ,GAZP.MICEX
                            financial instrument id or comma-delimited list of instruments to request quotes


        QUERY PARAMETERS
            level
                string
                Default: "best_price"
                Enum: "best_price" "market_depth"
                Example: level=best_price
                quote level to request

        HEADER PARAMETERS
            Accept
            required
                string
                Enum: "application/x-json-stream" "text/event-stream"
                Example: application/x-json-stream
                Acceptiong stream type data
        :return:
        """
        url = "".join([self.urlMd(), "feed/", symbolIds])
        # Enum: "best_price" "market_depth"
        params = {"level": "market_depth"}  # "level=best_price"
        # Enum: "application/x-json-stream" "text/event-stream"
        header = {"Accept": "text/event-stream"}

        session = requests.Session()
        with session.get(url=url, auth=self.auth, stream=True, params=params, headers=header) as response:
            for line in response.iter_lines():
                if line:
                    onData(line)

    # STREAM:
    def getLastQuote(self, onData, symbolIds: str):
        """
        Return the last quote for the specified financial instrument

        :param symbolIds:   string
                            Example: MSFT.NASDAQ,AAPL.NASDAQ,GAZP.MICEX
                            financial instrument id or comma-delimited list of instruments to request quotes
        QUERY PARAMETERS
            level
                string
                Default: "best_price"
                Enum: "best_price" "market_depth"
                Example: level=best_price
                quote level to request
        :return:
        """
        url = "".join([self.urlMd(), "feed/", symbolIds, "/last"])
        # Enum: "best_price" "market_depth"
        params = {"level": "market_depth"}  # "level=best_price"

        session = requests.Session()
        with session.get(url=url, auth=self.auth, stream=True, params=params) as response:
            for line in response.iter_lines():
                if line:
                    onData(line)

    def getOHLC(self, symbolId: str, duration: str, fromTime: str, toTime: str, size: str, type: str):
        """
        Return the list of OHLC candles for the specified financial instrument and duration

        :param symbolId:    string
                            Example: AAPL.NASDAQ
                            financial instrument id to get candles
        :param duration:    number
                            Enum: 60 300 600 900 1800 3600 14400 21600 86400
                            Example: 3600
                            aggregation interval in seconds

        QUERY PARAMETERS
            from
                string
                Example: from=1481565600000
                starting timestamp in ms

            to
                string
                Example: to=1481572800000
                ending timestamp in ms

            size
                string
                Default: "60"
                Example: size=1
                maximum amount of candles to retrieve

            type
                string
                Default: "quotes"
                Enum: "quotes" "trades"
                tick types - trades or quotes

        :return:
        """
        url = "".join([self.urlMd(), "ohlc/", symbolId, "/", duration])
        params = {"from": fromTime, "to": toTime, "size": size, "type": type}
        response = requests.get(url=url, auth=self.auth, params=params)
        return response

    def getTicks(self, symbolId: str, fromTime: str, toTime: str, size: str, type: str):
        """
        Return the list of ticks for the specified financial instrument

        :param symbolId:    string
                            Example: AAPL.NASDAQ
                            financial instrument id to get candles

        QUERY PARAMETERS
            from
                string
                Example: from=1481565600000
                starting timestamp in ms

            to
                string
                Example: to=1481572800000
                ending timestamp in ms

            size
                string
                Default: "60"
                Example: size=1
                maximum amount of candles to retrieve

            type
                string
                Default: "quotes"
                Enum: "quotes" "trades"
                tick types - trades or quotes

        :return:
        """
        url = "".join([self.urlMd(), "tocks/", symbolId])
        params = {"from": fromTime, "to": toTime, "size": size, "type": type}
        response = requests.get(url=url, auth=self.auth, params=params)
        return response

    def getAccountSummary(self, id: str, currency: str):
        """
        Return the summary for the specified account

        :param id:  string
                    Example: ABC1234.001
                    account id to get summary
        :param currency:    string
                            Example: EUR
                            currency to convert summary
        :return:
        """
        url = "".join([self.urlMd(), "summary/", id, "/", currency])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getAccountSummaryByDate(self, id: str, date: str, currency: str):
        """
        Return the summary for the specified account and session date

        :param id:  string
                    Example: ABC1234.001
                    account id to get summary
        :param date:    string
                        Example: 2013-02-16
                        session date of the account summary
        :param currency:    string
                            Example: EUR
                            currency to convert summary
        :return:
        """
        url = "".join([self.urlMd(), "summary/", id, "/", date, "/", currency])
        response = requests.get(url=url, auth=self.auth)
        return response

    def getTransactions(self,
                            uuid: str,
                            accountId: str,
                            symbolId: str,
                            asset: str,
                            operationType: str,
                            offset: int,
                            limit: int,
                            order: str,
                            fromDate: str,
                            toDate: str,
                            orderId: str,
                            orderPos: int,
                            ):
        """
        Return the list of transactions with the specified filter

        QUERY PARAMETERS
            uuid
                string <uuid>
                Example: uuid=c6e9abcc-e9e8-11e9-81b4-2a2ae2dbcce4
                transaction UUID

            accountId
                string
                Example: accountId=ABC1234.001
                transaction account ID

            symbolId
                string
                Example: symbolId=AAPL.NASDAQ
                filter transactions by the financial instrument

            asset
                string
                Example: asset=USD
                filter transactions by the asset

            operationType
                string
                Example: operationType=TRADE
                transaction type or comma-separated list of transaction types to filter

            offset
                number
                offset to list transactions

            limit
                number
                Example: limit=1
                limit response to this amount of transactions

            order
                string
                Default: "ASC"
                Enum: "ASC" "DESC"
                Example: order=ASC
                order transactions by descending (DESC) or ascending (ASC)

            fromDate
                string
                Example: fromDate=1970-01-01T00:00:00.000Z
                starting timestamp of transactions in ISO format

            toDate
                string
                Example: toDate=2019-01-01T00:00:00.000Z
                ending timestamp of transactions in ISO format

            orderId
                string <uuid>
                Example: orderId=d767f127-481f-466c-99b1-4d3069d68b66
                filter transactions by the order id

            orderPos
                number
                filter transactions by the position in the order
        :return:
        """
        url = "".join([self.urlMd(), "transactions"])
        params = {"uuid": uuid, "accountId": accountId, "symbolId": symbolId, "asset": asset,
                  "operationType": operationType, "offset": offset,
                  "limit": limit, "order": order, "fromDate": fromDate, "toDate": toDate, "orderId": orderId,
                  "orderPos": orderPos}
        response = requests.get(url=url, auth=self.auth, params=params)
        return response

    def getHistoricalOrders(self,
                                limit: str,
                                fromTime: str,
                                toTime: str,
                                account: str,
                                accountId: str,
                                ):
        """
        Return the list of historical orders

        QUERY PARAMETERS
            limit
                string
                Example: limit=10
                the limit for max items of the order list

            from
                string
                Example: from=2017-05-18T10:00:00.000Z
                the start date

            to
                string
                Example: to=2017-05-21T17:59:59.999Z
                the stop date

            account
                string
                Example: account=ABC1234.001
                the user account list, required api 2.0 only

            accountId
                string
                Example: accountId=ABC1234.001
                the user account list, required api 3.0 only
        :return:
        """
        url = "".join([self.urlMd(), "orders"])
        params = {"limit": limit, "from": fromTime, "to": toTime, "account": account, "accountId": accountId}
        response = requests.get(url=url, auth=self.auth, params=params)
        return response

    def placeOrder(self,
                       orderType: str,
                       side: str,
                       quantity: str,
                       duration: str,
                       symbolId: str,
                       # not required:
                       gttExpiration: str=None,
                       ocoGroup: str=None,
                       stopLoss: str=None,
                       accountId: str=None,
                       placeInterval: str=None,
                       ifDoneParentId: str=None,
                       priceDistance: str=None,
                       stopPrice: str=None,
                       partQuantity: str=None,
                       takeProfit: str=None,
                       account: str=None,
                       clientTag: str=None,
                       instrument: str=None,
                       limitPrice: str=None,
                       ):  # POST
        """
        Place new trading order

        REQUEST BODY SCHEMA: application/json
            order parameters

                orderType
                    required
                    string
                    Enum: "market" "limit" "stop" "stop_limit" "twap" "trailing_stop" "iceberg"
                    order type

                gttExpiration
                    string
                    order expiration if applicable

                ocoGroup
                    string
                    One-Cancels-the-Other group ID if set

                stopLoss
                    string
                    optional price of stop loss order

                side
                    required
                    string
                    Enum: "buy" "sell"
                    order side

                accountId
                    string
                    user account to place order

                placeInterval
                    string
                    order place interval, Twap orders only

                ifDoneParentId
                    string
                    ID of an order on which this order depends

                priceDistance
                    string
                    order price distance, TrailingStop orders only

                stopPrice
                    string
                    order stop price if applicable

                partQuantity
                    string
                    order partial quantity, Twap and Iceberg orders only

                quantity
                    required
                    string
                    order quantity

                duration
                    required
                    string
                    Enum: "day" "fill_or_kill" "immediate_or_cancel" "good_till_cancel" "good_till_time" "at_the_opening" "at_the_close"
                    order duration

                takeProfit
                    string
                    optional price of take profit order

                account
                    string
                    Deprecated
                    user account to place order, required for API version 1.0

                clientTag
                    string
                    optional client tag to identify or group orders

                instrument
                    string
                    order instrument, required api 2.0 only

                symbolId
                    string
                    order instrument, required api 3.0 only

                limitPrice
                    string
                    order limit price if applicable
        :return:
        """
        url = "".join([self.urlTrade(), "orders"])
        json = {"orderType": orderType, "side": side, "quantity": quantity, "duration": duration, "symbolId": symbolId}
        if gttExpiration is not None: json["gttExpiration"] = gttExpiration
        if ocoGroup is not None: json["ocoGroup"] = ocoGroup
        if stopLoss is not None: json["stopLoss"] = stopLoss
        if accountId is not None: json["accountId"] = accountId
        if placeInterval is not None: json["placeInterval"] = placeInterval
        if ifDoneParentId is not None: json["ifDoneParentId"] = ifDoneParentId
        if priceDistance is not None: json["priceDistance"] = priceDistance
        if stopPrice is not None: json["stopPrice"] = stopPrice
        if partQuantity is not None: json["partQuantity"] = partQuantity
        if takeProfit is not None: json["takeProfit"] = takeProfit
        if account is not None: json["account"] = account
        if clientTag is not None: json["clientTag"] = clientTag
        if instrument is not None: json["instrument"] = instrument
        if limitPrice is not None: json["limitPrice"] = limitPrice

        response = requests.post(url=url, auth=self.auth, json=json)
        return response

    def getActiveOrders(self,
                            limit: str = None,
                            account: str = None,
                            accountId: str = None,
                            instrument: str = None,
                            symbolId: str = None,
                            ):
        """
        Return the list of active trading orders

        QUERY PARAMETERS
            limit
                string
                Example: limit=10
                the limit for max items of the order list

            account
                string
                Example: account=ABC1234.001
                the user account list, required api 2.0 only

            accountId
                string
                Example: accountId=ABC1234.001
                the user account list, required api 3.0 only

            instrument
                string
                Example: instrument=AAPL.NASDAQ
                the instrument identifier, required api 2.0 only

            symbolId
                string
                Example: symbolId=AAPL.NASDAQ
                the instrument identifier, required api 3.0 only
        :return:
        """
        url = "".join([self.urlMd(), "orders/active"])
        params = {}
        if limit is not None: params["limit"] = limit
        if account is not None: params["account"] = account
        if accountId is not None: params["accountId"] = accountId
        if instrument is not None: params["instrument"] = instrument
        if symbolId is not None: params["symbolId"] = symbolId
        response = requests.get(url=url, auth=self.auth, params=params)
        return response

    def getOrder(self, orderId: str):
        """
        Return the order with specified identifier
        :param orderId: string
                        Example: ffecfac8-ccf9-4015-9a0f-b49a6b9673b8
                        the order identifier
        :return:
        """
        url = "".join([self.urlMd(), "orders/", orderId])
        response = requests.get(url=url, auth=self.auth)
        return response

    def modifyOrder(self,
                        orderId: str,
                        action: str,
                        quantity: str, stopPrice: str = None,
                        priceDistance: str = None,
                        limitPrice: str = None):  # POST
        """
        Replace or cancel trading order
        :param orderId: string
                        Example: ffecfac8-ccf9-4015-9a0f-b49a6b9673b8
                        the order identifier

        REQUEST BODY SCHEMA: application/json
            modification parameters

                action
                    required
                    string
                    Enum: "replace" "cancel"
                    order modification action

                parameters
                    object (ReplaceParameters)
                    modification parameters if applicable

                    quantity
                    required
                        string
                        new order quantity to replace

                    limitPrice
                        string
                        new order limit price if applicable

                    priceDistance
                        string
                        new order price distance if applicable

                    stopPrice
                        string
                        new order stop price if applicable
        :return:
        """
        url = "".join([self.urlTrade(), "orders", "/", orderId])
        parameters = {"quantity":quantity}
        if stopPrice is not None: parameters["stopPrice"] = stopPrice
        if priceDistance is not None: parameters["priceDistance"] = priceDistance
        if limitPrice is not None: parameters["limitPrice"] = limitPrice
        json = {"parameters": parameters, "action": action}
        response = requests.post(url=url, auth=self.auth, json=json)
        return response
    # STREAM:
    def orderUpdatesStream(self, onData):
        """
        Order updates stream via HTTP
        :return:
        """
        url = "".join([self.urlMd(), "stream/orders"])
        session = requests.Session()
        with session.get(url=url, auth=self.auth, stream=True) as response:
            for line in response.iter_lines():
                if line:
                    onData(line)

    # STREAM:
    def orderUpdatesWsStream(self, onData):
        """
        Order updates stream via websocket
        :return:
        """
        url = "".join([self.urlMd(), "ws/orders"])
        session = requests.Session()
        with session.get(url=url, auth=self.auth, stream=True) as response:
            for line in response.iter_lines():
                if line:
                    onData(line)

    # STREAM:
    def tradesStream(self, onData):
        """
        Trades updates stream via HTTP
        :return:
        """
        url = "".join([self.urlMd(), "stream/trades"])
        session = requests.Session()
        with session.get(url=url, auth=self.auth, stream=True) as response:
            for line in response.iter_lines():
                if line:
                    onData(line)

    # STREAM:
    def tradesWsStream(self, onData):
        """
        Trades updates stream via websocket
        :return:
        """
        url = "".join([self.urlMd(), "ws/trades"])
        session = requests.Session()
        with session.get(url=url, auth=self.auth, stream=True) as response:
            for line in response.iter_lines():
                if line:
                    onData(line)
