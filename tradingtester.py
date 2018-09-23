import keys
import datetime
from time import sleep
from binance.client import Client
from bittrex.bittrex import Bittrex, API_V2_0
# list coins = [bmbm, das,dsf asdf,]
client = Client(keys.APIkey, keys.SecretKey)
symbol = 'BTCUSDT'
quantity = .05

trades = client.get_orderbook_tickers()


my_bittrex = Bittrex(None, None)  # or defaulting to v1.1 as Bittrex(None, None)

#print(my_bittrex.get_markets())
bittrades = my_bittrex.get_orderbook("BTC-OMG",'both')
#print(bittrades)
bit_result = bittrades[u'result']
#print(nigga)

bit_sell = bit_result[u'sell']
bit_order_sell= bit_sell[0]
bit_rate_sell = bit_order_sell[u'Rate']

bit_buy= bit_result[u'buy']
bit_order_buy = bit_buy[0]
bit_rate_buy = bit_order_buy[u'Rate']

for e in trades:
    if e[u'symbol'] == u'OMGBTC':
        cost = e[u'askPrice']
        bid = e[u'bidPrice']
        quant = e[u'askQty']
        bquant = e[u'bidQty']


print('Binance Buy at: ', float(cost)*1.001)
print('Binance Sell at: ', float(bid)*.99900)


print('Bittrex Sell at: ',float(bit_rate_buy) * .9975)
print('Bittrex Buy at: ' ,float(bit_rate_sell) *  1.0025)

#print(trades)

binbuy = float(cost)*1.001
binsell = float(bid)*.99900
bitbuy = float(bit_rate_sell) *  1.0025
bitbuy = float(bit_rate_buy) * .9975
