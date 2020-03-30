import numpy as np

stock_cnt = 200
view_days = 504
stock_day_change = np.random.standard_normal((200, 504))
print(stock_day_change[-2:, -3:])
print(stock_day_change[-2:, -3:].astype(int))
print(np.around(stock_day_change[-2:, -5:], 2))
