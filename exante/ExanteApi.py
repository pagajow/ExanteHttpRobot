from requests.auth import HTTPBasicAuth

from exante.ApiWorker import ApiWorker
from exante.Commands import Commands


class ExanteApi:
    APIVersion2 = "2.0"
    APIVersion3 = "3.0"
    demo = "demo"
    live = "live"

    def __init__(self, applicationID: str, accessKey: str, account: str = demo, version: str = APIVersion3):
        self.applicationID = applicationID
        self.accessKey = accessKey

        self.account = account
        self.version = version

        self.auth = HTTPBasicAuth(username=self.applicationID, password=self.accessKey)
        self.cmds = Commands(auth=self.auth, account=self.account, version=self.version)

    def checkAccount(self):
        return self.cmds.getUserAccounts()

    def onData(self, data: bytes):
        print(data)

    def start(self):
        exchanges = self.cmds.getExchanges()
        print("exchanges, {}".format(str(exchanges.reason)))

        #ApiWorker(self.cmds.getQuoteStream, symbolIds="MSFT.NASDAQ", onData=self.onData).start()








