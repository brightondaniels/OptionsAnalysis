from datetime import datetime

stock = 'SPY'
expiration = '12-18-2022'
strike_price = 370
dataSource = 'yahoo'

desired_sigma = 0.015

tradingDays = 252
today = datetime.now()
one_yr_ago = today.replace(year=today.year-1)
