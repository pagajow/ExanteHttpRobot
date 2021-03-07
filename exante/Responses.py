class Exchange:
    """
    name
        string
        full exchange name

    id
    required
        string
        exchange internal id

    country
        string
        exchange country
    """

    def __init__(self, id: str = None, name: str = None, country: str = None):
        self.id = id
        self.name = name
        self.country = country


class Instrument:
    """
    exchange
        string
        exchange id where the symbol is traded

    name
        string
        short symbol description

    id
    required
        string
        internal symbol id, required api 2.0 only

    symbolType
    required
        string
        Enum: "FX_SPOT" "CURRENCY" "INDEX" "STOCK" "BOND" "FUND" "FUTURE" "OPTION" "CFD" "CALENDAR_SPREAD"
        symbol type, required api 3.0 only

    symbolId
    required
        string
        internal symbol id, required api 3.0 only

    expiration
        number
        expiration timestamp in ms if applicable

    country
        string
        country of symbol's exchange

    group
        string
        group of symbol, applicable to futures and options

    description
    required
        string
        long symbol description

    currency
    required
        string
        currency of symbol price

    type
    required
        string
        Enum: "FX_SPOT" "CURRENCY" "INDEX" "STOCK" "BOND" "FUND" "FUTURE" "OPTION" "CFD" "CALENDAR_SPREAD"
        symbol type, required api 2.0 only

    minPriceIncrement
    required
        string
        minimum possible increment of symbol price, required api 3.0 only

    ticker
    required
        string
        exchange ticker

    optionData
        object (OptionDataResponse)
        option specific properties

    mpi
    required
        string
        minimum possible increment of symbol price, required api 2.0 only


    """

    def __init__(self, exchange=None, name=None, id=None, symbolType=None, symbolId=None, expiration=None, country=None,
                 group=None, description=None, currency=None, type=None, minPriceIncrement=None, ticker=None,
                 optionData=None, mpi=None):
        self.exchange = exchange
        self.name = name
        self.id = id
        self.symbolType = symbolType
        self.symbolId = symbolId
        self.expiration = expiration
        self.country = country
        self.group = group
        self.description = description
        self.currency = currency
        self.type = type
        self.minPriceIncrement = minPriceIncrement
        self.ticker = ticker
        self.optionData = optionData
        self.mpi = mpi


class InstrumentGroups:
    """
    group
    required
        string
        group id

    name
        string
        group title

    exchange
        string
        exchange id where the group is traded

    types
    required
        string
        Enum: "FX_SPOT" "CURRENCY" "INDEX" "STOCK" "BOND" "FUND" "FUTURE" "OPTION" "CFD" "CALENDAR_SPREAD"
        list of symbol types in the group
    """

    def __init__(self, group=None, name=None, exchange=None, types=None):
        self.group = group
        self.name = name
        self.exchange = exchange
        self.types = types


class InstrumentSchedule:
    """
    intervals
    required
        Array of objects (ScheduleIntervalResponse)
        instrument schedule intervals
    """

    def __init__(self, intervals):
        self.scheduleIntervalResponses = []
        for interval in intervals:
            self.scheduleIntervalResponses.append(ScheduleIntervalResponse(name=interval["name"],
                                                                           period=interval["period"],
                                                                           orderTypes=interval["orderTypes"]))


class ScheduleIntervalResponse:
    """
        name
        required
            string
            Enum: "PreMarket" "MainSession" "AfterMarket" "Offline" "Online" "Expired"
            trading session name

        period
        required
            object (IntervalResponse)
            trading session period

        orderTypes
            object (AvailableOrderDurationTypes)

    """

    def __init__(self, name, period, orderTypes=None):
        self.name = name
        self.period = IntervalResponse(start=period["start"], end=period["end"])
        if orderTypes is not None:
            self.AvailableOrderDurationTypes = \
                AvailableOrderDurationTypes(stop=orderTypes["stop"],
                                            limit=orderTypes["limit"],
                                            pegged=orderTypes["pegged"],
                                            market=orderTypes["market"],
                                            stop_limit=orderTypes["stop_limit"] )
        else:
            self.AvailableOrderDurationTypes = None


class IntervalResponse:
    """
    end
    required
        number
        session end timestamp in ms

    start
    required
        number
        session start timestamp in ms
    """
    def __init__(self, end, start):
        self.enf = end
        self.start = start


class AvailableOrderDurationTypes:
    """
    stop
        Array of objects (Value)
        Items Enum: "day" "at_the_close" "at_the_opening" "fill_or_kill" "immediate_or_cancel" "good_till_cancel" "good_till_time"
    limit
        Array of objects (Value)
        Items Enum: "day" "at_the_close" "at_the_opening" "fill_or_kill" "immediate_or_cancel" "good_till_cancel" "good_till_time"
    pegged
        Array of objects (Value)
        Items Enum: "day" "at_the_close" "at_the_opening" "fill_or_kill" "immediate_or_cancel" "good_till_cancel" "good_till_time"
    market
        Array of objects (Value)
        Items Enum: "day" "at_the_close" "at_the_opening" "fill_or_kill" "immediate_or_cancel" "good_till_cancel" "good_till_time"
    stop_limit
        Array of objects (Value)
        Items Enum: "day" "at_the_close" "at_the_opening" "fill_or_kill" "immediate_or_cancel" "good_till_cancel" "good_till_time"
    """
    stop_limit: list
    market: list
    pegged: list
    limit: list
    stop: list

    def __init__(self, stop=None, limit=None, pegged=None, market=None, stop_limit=None):
        """

        :param stop: list
        :param limit: list
        :param pegged: list
        :param market: list
        :param stop_limit: list
        """
        self.stop = stop
        self.limit = limit
        self.pegged = pegged
        self.market = market
        self.stop_limit = stop_limit


class InstrumentSpecification:
    """
    priceUnit
    required
        string
        instrument price unit

    units
        string
        instrument units name

    lotSize
    required
        string
        instrument lot size value

    leverage
    required
        string
        instrument leverage rate value

    contractMultiplier
    required
        string
        instrument contract multiplier

    """
    def __init__(self, priceUnit, lotSize, leverage, contractMultiplier, units=None):
        self.priceUnit = priceUnit
        self.units = units
        self.lotSize = lotSize
        self.leverage = leverage
        self.contractMultiplier = contractMultiplier


class InstrumentType:
    """
    id
    required
        string
        type id
    """
    def __init__(self, id):
        self.id = id


# STREAMS: ---------------------------------------------------------------
class TradesStreamResponse:
    """
    price
        string
        trade price

    symbolId
    required
        string
        financial instrument id

    timestamp
    required
        number
        trade timestamp

    size
        string
        trade size
    """
    def __init__(self, symbolId, timestamp, price=None, size=None):
        self.symbolId = symbolId
        self.timestamp = timestamp
        self.price = price
        self.size = size


class QuoteStreamResponse:
    """
    ask
    required
        Array of objects (QuoteSide)
        array of ask levels according to requested feed level

    symbolId
    required
        string
        financial instrument id

    timestamp
    required
        number
        quote timestamp

    bid
    required
        Array of objects (QuoteSide)
        array of bid levels according to requested feed level
    """

    def __init__(self, ask, bid, symbolId, timestamp):
        self.ask = []
        for a in ask:
            self.ask.append(a)
        self.bid = []
        for b in bid:
            self.bid.append(b)
        self.symbolId = symbolId
        self.timestamp = timestamp


class LastQuoteResponse:
    """
    ask
    required
        Array of objects (QuoteSide)
        array of ask levels according to requested feed level

    symbolId
    required
        string
        financial instrument id

    timestamp
    required
        number
        quote timestamp

    bid
    required
        Array of objects (QuoteSide)
        array of bid levels according to requested feed level
    """
    def __init__(self, ask, bid, symbolId, timestamp):
        self.ask = []
        for a in ask:
            self.ask.append(a)
        self.bid = []
        for b in bid:
            self.bid.append(b)
        self.symbolId = symbolId
        self.timestamp = timestamp


class QuoteSide:
    """
    price
    required
        string
        quote value of this level, required api 3.0 only

    size
    required
        string
        quantity value of this level

    value
    required
        string
        quote value of this level, required api 2.0 only
    """
    def __init__(self, price, size, value):
        self.price = price
        self.size = size
        self.value = value
# STREAMS: ---------------------------------------------------------------


class OHLCResponse:
    """
    close
    required
        string
        candle close price

    timestamp
    required
        number
        candle timestamp

    open
    required
        string
        candle open price

    low
    required
        string
        candle low price

    high
    required
        string
        candle high price

    volume
    required
        string
        total volume for specified period. Appears and required only for trade candle request
    """
    def __init__(self, timestamp, open, high, low, close, volume):
        self.timestamp = timestamp
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume


class TickResponse:
    """
    price
        string
        trade price. Appears and required only for trade request, required api 3.0 only

    timestamp
    required
        number
        tick timestamp

    bid
        Array of objects (QuoteSide)
        tick bid. Appears and required only for quote request

    ask
        Array of objects (QuoteSide)
        tick ask. Appears and required only for quote request

    symbolId
    required
        string
        financial instrument id

    size
        string
        trade size. Appears and required only for trade request

    value
        string
        trade price. Appears and required only for trade request, required api 2.0 only
    """
    def __init__(self, timestamp, symbolId, price=None, bid=None, ask=None, size=None, value=None):
        self.timestamp = timestamp
        self.symbolId = symbolId
        self.price = price
        self.size = size
        self.value = value
        self.ask = []
        if ask is not None:
            for a in ask:
                self.ask.append(a)
        self.bid = []
        if bid is not None:
            for b in bid:
                self.bid.append(b)


class AccountSummary:
    """
    netAssetValue
        string
        total NAV of user in the currency of the report

    positions
    required
        Array of objects (InstrumentPositionResponse)
        open positions

    currency
    required
        string
        currency of the report

    marginUtilization
        string
        margin utilization in fraction of NAV

    timestamp
    required
        number
        timestamp of the report

    moneyUsedForMargin
        string
        money used for margin in the currency of the report

    currencies
    required
        Array of objects (CurrencyPositionResponse)
        currencies on position

    account
    required
        string
        user account id, required api 2.0 only

    sessionDate
        string
        session date of the report

    freeMoney
        string
        free money in the currency of the report

    accountId
    required
        string
        user account id, required api 3.0 only
    """
    def __init__(self, netAssetValue=None, positions=None, currency=None, marginUtilization=None, timestamp=None,
                 moneyUsedForMargin=None, currencies=None, account=None, sessionDate=None, freeMoney=None, accountId=None):
        self.netAssetValue = netAssetValue
        self.positions = []
        if positions is not None:
            for position in positions:
                self.positions.append(InstrumentPositionResponse(
                    convertedPnl=position["convertedPnl"],
                    symbolType=position["symbolType"],
                    currency=position["currency"],
                    id=position["id"],
                    pnl=position["pnl"],
                    quantity=position["quantity"],
                    symbolId=position["symbolId"],
                    convertedValue=position["convertedValue"],
                    averagePrice=position["averagePrice"],
                    value=position["value"]
                ))
        self.currency = currency
        self.marginUtilization = marginUtilization
        self.timestamp = timestamp
        self.moneyUsedForMargin = moneyUsedForMargin
        self.currencies = []
        if currencies is not None:
            for currency in currencies:
                self.currencies.append(CurrencyPositionResponse(
                    code=currency["code"],
                    convertedValue=currency["convertedValue"],
                    value=currency["value"]
                ))
        self.account = account
        self.sessionDate = sessionDate
        self.freeMoney = freeMoney
        self.accountId = accountId


class InstrumentPositionResponse:
    """
    convertedPnl
        string
        current position PnL in the currency of the report

    symbolType
    required
        string
        financial instrument type

    currency
    required
        string
        currency code of the financial instrument

    id
    required
        string
        financial instrument identifier, required api 2.0 only

    pnl
        string
        current position PnL

    price
        string
        current financial instrument price

    quantity
    required
        string
        quantity on position

    symbolId
    required
        string
        financial instrument identifier, required api 3.0 only

    convertedValue
        string
        position value in the currency of the report

    averagePrice
        string
        average position opening price

    value
        string
        position value
    """
    def __init__(self, convertedPnl=None, symbolType=None, currency=None, id=None, pnl=None, quantity=None,
                 symbolId=None, convertedValue=None, averagePrice=None, value=None):
        self.convertedPnl = convertedPnl
        self.symbolType = symbolType
        self.currency = currency
        self.id = id
        self.pnl = pnl
        self.quantity = quantity
        self.symbolId = symbolId
        self.convertedValue = convertedValue
        self.averagePrice = averagePrice
        self.value = value


class CurrencyPositionResponse:
    """
    code
    required
        string
        currency code

    convertedValue
        string
        converted value of position if crossrates are available

    value
    required
        string
        value of position
    """
    def __init__(self, code=None, convertedValue=None, value=None):
        self.code = code
        self.convertedValue = convertedValue
        self.value = value


class Transaction:
    """
    symbolId
    required
        string
        transaction financial instrument

    operationType
    required
        string
        transaction type

    timestamp
    required
        number
        timestamp of the transaction, required api 3.0 only

    asset
    required
        string
        transaction asset

    id
    required
        number
        transaction id

    accountId
    required
        string
        transaction account id

    sum
    required
        string
        transaction amount

    when
    required
        number
        timestamp of the transaction, required api 2.0 only
    """
    def __init__(self, symbolId, operationType, timestamp, asset, id, accountId, sum, when):
        self.symbolId = symbolId
        self.operationType = operationType
        self.timestamp = timestamp
        self.asset = asset
        self.id = id
        self.accountId = accountId
        self.sum = sum
        self.when = when


class ApiOrder:
    """
    orderState
    required
        object (OrderState)
        order state response

    username
        string
        associated name

    clientTag
        string
        optional client tag to identify or group orders

    orderParameters
    required
        object (OrderParameters)
        order response parameters

    accountId
    required
        string
        associated account ID

    currentModificationId
    required
        string
        current order modification unique ID

    id
    required
        string
        unique order ID, required api 2.0 only

    orderId
    required
        string
        unique order ID, required api 3.0 only

    placeTime
    required
        string <date-time>
        order place time
    """
    def __init__(self, orderState=None, username=None, clientTag=None, orderParameters=None,
                 accountId=None, currentModificationId=None, id=None, orderId=None, placeTime=None):
        self.orderState = None
        if orderState is not None:
            self.orderState = OrderState(
                lastUpdate=orderState["lastUpdate"],
                fills=orderState["fills"],
                status=orderState["status"],
                reason=orderState["reason"]
            )
        self.username = username
        self.clientTag = clientTag
        self.orderParameters = None
        if orderParameters is not None:
            self.orderParameters = OrderParameters(
                symbolId=orderParameters["symbolId"],
                orderType=orderParameters["orderType"],
                gttExpiration=orderParameters["gttExpiration"],
                ocoGroup=orderParameters["ocoGroup"],
                side=orderParameters["side"],
                placeInterval=orderParameters["placeInterval"],
                ifDoneParentId=orderParameters["ifDoneParentId"],
                priceDistance=orderParameters["priceDistance"],
                stopPrice=orderParameters["stopPrice"],
                partQuantity=orderParameters["partQuantity"],
                quantity=orderParameters["quantity"],
                duration=orderParameters["duration"],
                instrument=orderParameters["instrument"],
                limitPrice=orderParameters["limitPrice"]
            )
        self.accountId = accountId
        self.currentModificationId = currentModificationId
        self.id = id
        self.orderId = orderId
        self.placeTime = placeTime


class OrderState:
    """
    lastUpdate
    required
        string <date-time>
        order last update time

    fills
    required
        Array of objects (OrderFill)
        array of order fills

    status
    required
        string
        Enum: "placing" "working" "cancelled" "pending" "filled" "rejected"
        current order status

    reason
        string
        order rejected reason if applicable
    """
    def __init__(self, lastUpdate=None, fills=None, status=None, reason=None):
        self.lastUpdate = lastUpdate
        self.fills = []
        if fills is not None:
            for fill in fills:
                self.fills.append(
                    OrderFill(
                        price=fill["price"],
                        quantity=fill["quantity"],
                        timestamp=fill["timestamp"],
                        time=fill["time"],
                        position=fill["position"]
                    )
                )
        self.status = status
        self.reason = reason


class OrderFill:
    """
    price
    required
        string
        fill price

    quantity
    required
        string
        fill quantity

    timestamp
    required
        string <date-time>
        fill time, required api 3.0 only

    time
    required
        string <date-time>
        fill time, required api 2.0 only

    position
    required
        string
        fill serial number
    """
    def __init__(self, price=None, quantity=None, timestamp=None, time=None, position=None):
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp
        self.time = time
        self.position = position


class OrderParameters:
    """
    symbolId
    required
        string
        associated instrument, required api 3.0 only

    orderType
    required
        string
        Enum: "market" "limit" "stop" "stop_limit" "twap" "trailing_stop" "iceberg"
        order type

    gttExpiration
        string <date-time>
        order expiration if applicable

    ocoGroup
        string
        One-Cancels-the-Other group ID if set

    side
    required
        string
        Enum: "buy" "sell"
        order side

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
        order stop price, Stop orders only

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

    instrument
    required
        string
        associated instrument, required api 2.0 only

    limitPrice
        string
        order limit price, Limit orders only
    """

    def __init__(self, symbolId=None, orderType=None, gttExpiration=None, ocoGroup=None, side=None, placeInterval=None,
                 ifDoneParentId=None, priceDistance=None, stopPrice=None, partQuantity=None, quantity=None,
                 duration=None, instrument=None, limitPrice=None):
        self.symbolId = symbolId
        self.orderType = orderType
        self.gttExpiration = gttExpiration
        self.ocoGroup = ocoGroup
        self.side = side
        self.placeInterval = placeInterval
        self.ifDoneParentId = ifDoneParentId
        self.priceDistance = priceDistance
        self.stopPrice = stopPrice
        self.partQuantity = partQuantity
        self.quantity = quantity
        self.duration = duration
        self.instrument = instrument
        self.limitPrice = limitPrice

# STREAMS: ---------------------------------------------------------------
class ApiOrderStream:
    """
    * OrderUpdate:
        event
        required
            string
            Value: "order"
            event type

        order
        required
            object (ApiOrder)
            order response

    * Heartbeat:
        event
        required
            string
            Value: "heartbeat"
            event type
    """
    def __init__(self, event=None, order=None):
        self.event = event
        if order is None:
            self.order = order
        else:
            self.order = ApiOrder(
                orderState=order["orderState"],
                username=order["username"],
                clientTag=order["clientTag"],
                orderParameters=order["orderParameters"],
                accountId=order["accountId"],
                currentModificationId=order["currentModificationId"],
                id=order["id"],
                orderId=order["orderId"],
                placeTime=order["placeTime"]
            )


class ApiOrderWsStream:
    """
    * WsOrderUpdate:
        event
        required
            string
            Value: "order"
            event type

        sequence_number
        required
            integer <int64>
            sequence number

        order
        required
            object (ApiOrder)
            order response

    * WsHeartbeat:
        event
        required
            string
            Value: "heartbeat"
            event type

        sequence_number
        required
            integer <int64>
            sequence number
    """
    def __init__(self, event=None, sequence_number=None, order=None):
        self.event = event
        self.sequence_number = sequence_number
        if order is None:
            self.order = order
        else:
            self.order = ApiOrder(
                orderState=order["orderState"],
                username=order["username"],
                clientTag=order["clientTag"],
                orderParameters=order["orderParameters"],
                accountId=order["accountId"],
                currentModificationId=order["currentModificationId"],
                id=order["id"],
                orderId=order["orderId"],
                placeTime=order["placeTime"]
            )


class ApiTradesStream:
    """
    * Trade
        event
        required
            string
            Value: "trade"
            event type

        quantity
        required
            string
            trade quantity

        time
        required
            string
            trade timestamp, required api 2.0 only

        price
        required
            string
            trade price

        position
        required
            string
            order fill serial number for the trade

        orderId
        required
            string <uuid>
            respected order ID

        timestamp
        required
            string
            trade timestamp, required api 3.0 only

    * Heartbeat
        event
        required
            string
            Value: "heartbeat"
            event type
    """
    def __init__(self, event=None, quantity=None, time=None, price=None, position=None, orderId=None, timestamp=None):
        self.event = event
        self.quantity = quantity
        self.time = time
        self.price = price
        self.position = position
        self.orderId = orderId
        self.timestamp = timestamp


class ApiTradesWsStream:
    """
    * WsTrade
        event
        required
            string
            Value: "trade"
            event type

        quantity
        required
            string
            trade quantity

        sequence_number
        required
            integer <int64>
            sequence number

        time
        required
            string
            trade timestamp, required api 2.0 only

        price
        required
            string
            trade price

        position
        required
            string
            order fill serial number for the trade

        orderId
        required
            string <uuid>
            respected order ID

        timestamp
        required
            string
            trade timestamp, required api 3.0 only

    * WsHeartbeat
        event
        required
            string
            Value: "heartbeat"
            event type

        sequence_number
        required
            integer <int64>
            sequence number
    """
    def __init__(self, event=None, sequence_number=None, quantity=None, time=None, price=None, position=None, orderId=None, timestamp=None):
        self.event = event
        self.sequence_number = sequence_number
        self.quantity = quantity
        self.time = time
        self.price = price
        self.position = position
        self.orderId = orderId
        self.timestamp = timestamp
# STREAMS: ---------------------------------------------------------------




