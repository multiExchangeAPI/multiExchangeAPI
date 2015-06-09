# multiExchangeAPI

Python tool to request data from any bitcoin exchange using standardized queries and receive responses in a standardized format.


###Standardized format
Trade pair order matters, so btc_usd is bitcoin/usd pair, while btc_usd is the usd/bitcoin pair. If any exchanges  reverse this logic for any reason, multAPI will reverse it *back*, and always give you the data in the correct order according to standardized format. The data returned will always match the pre-defined standardized format, independent of which exchange is queried, and the standardized format will always be the one that matches international brokerage standards and conventions.


###Exchanges Supported
APIs tentatively planned for integration:
- anxbtc
- bitfinex
- bitstamp
- bittrex
- btc-e
- btccny
- circle
- coinbase
- cryptsy
- itbit
- kraken
- lakebtc
- okcoin
- poloniex
- shapeshift
- kraken

### install notes
if /usr/bin/python points to python2.7, you will need to either update your system so that
/usr/bin/python points to python3, or you can also just hardcode the top line of each python file 
to point to /usr/bin/python3


