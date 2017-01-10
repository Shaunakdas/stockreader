from infrastructure import log

logger = log.get_logger("domain")

class Domain:

    def __init__(self, persistence, download):
        self.persistence = persistence
        self.download = download

    def download_and_save_stock_current_data(self, stock):
        try:
            quote = stock["symbol"]
            logger.info("stock current data %s", quote)
            stock_current_data = self.download.get_stock_current_data(quote)
            self.persistence.upsert_stock_current_data(quote, stock_current_data)
        except Exception as e:
            logger.exception(e)

    def download_and_save_stock_historical_data(self, initialDate, finalDate, stock):
        quote = stock["symbol"]
        logger.info('stock historical data %s, %s, %s', initialDate, finalDate, quote)
        stock_historical_data_array = self.download.get_stock_historical_data(initialDate, finalDate, quote)
        self.persistence.add_stock_historical_data(quote, stock_historical_data_array)

    def stock_exists(self, quote):
        # return self.mongo.stock_exists(quote)
        return self.persistence.stock_exists(quote)

    def get_stock_list(self):
        # return self.mongo.read_stocks_from_stock_list()
        return self.persistence.get_stock_list()

    def add_stock_to_stock_list(self, stock):
        # self.mongo.save_stock_list([stock])
        logger.info('add stock %s', stock)
        self.persistence.add_to_stocks(stock)
