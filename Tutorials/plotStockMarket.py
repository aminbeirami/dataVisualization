# in this tutorial we load data from some online resources, split them up and visualize them using matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import quandl
import pickle

def get_data_and_pickle():
	quandle_api_key = open('quandleAPIKey.txt','r').read()
	data = quandl.get('SCF/SHFE_ZN2_OR',authtoken = quandle_api_key)
	data.to_pickle('stock_data.pickle')

def read_pickled_data():
	read_pickle = open('stock_data_pickle.pickle','rb')
	stock_data_unpickled = pickle.load(read_pickle)
	return stock_data_unpickled

# get_data_and_pickle()

stock_data = pd.read_pickle('stock_data.pickle')
# plt.plot(stock_data['High'],label = 'High Daily', color='g')
# plt.plot(stock_data['Low'], label = 'Low Daily', color='b')

resampled = stock_data.resample('M').median()
plt.plot(resampled['Low'],label='High Monthly', color='r')
plt.plot(resampled['High'],label='Low Monthly', color='k' )

plt.legend()
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('practice of Stock Market Plotting')
plt.show()