library(forecast)
library(tseries)
btc = read.csv("cryptocurrencypricehistory/bitcoin_price.csv")
dates = as.Date(btc$Date, format = "%b %d, %Y")
btc = btc[order(dates),]


btc_ts = ts(btc$Close, start = c(2013,  as.numeric(format(dates[length(dates)], "%j"))), frequency = 365)
plot(btc_ts)

summary(arma(btc_ts, order = c(1,2)))