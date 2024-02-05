import matplotlib.pyplot as plt
import numpy as np

num_simulations = 300
num_days = 252
initial_price = 100
volatility = 0.1
annual_interest_rate = 0.05


def daily_stock():
    dt = 1 / num_days
    returns = (annual_interest_rate - volatility * volatility / 2) * dt + volatility * np.random.normal(0,np.sqrt(1/num_days),(num_simulations,num_days))
    returns[:,0]=initial_price
    for i in range(1, num_days):
        returns[:, i] = initial_price*np.exp(returns[:,i])

    return returns


price_simulations = daily_stock()
print(np.shape(price_simulations))

plt.plot(price_simulations.T)
plt.show()
print(price_simulations[:,-1].mean())


## answer
import numpy as np
s0=100
numofsimulation=300
numofdays=252
mu=0.05
sigma=0.1

Wt=np.random.normal(0,np.sqrt(1/numofdays),(numofsimulation,numofdays))
daily_returns=np.exp((mu-sigma**2/2)*(1/numofdays)+sigma*Wt)
cumulative_returns=np.cumprod(daily_returns,axis=1)*s0
import matplotlib as plt
plt.plot(cumulative_returns.T)
print(cumulative_returns[:,-1].mean())

