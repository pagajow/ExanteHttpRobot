# get instrument groups

"""
    netAssetValue
    string
    total NAV of user in the currency of the report

    positions
    required
    Array of objects (InstrumentPositionResponse)
    open positions

    Array ()
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

    Array ()
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