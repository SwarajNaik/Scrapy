import pandas as pd
from datetime import datetime
from yahoofinancials import YahooFinancials



def daily_treasury_prices():
    symbols = ['^TNX', '^IRX', '^TYX', '^FVX']
    
    symbol_ = []
    for_date =[]
    high = []
    low = []
    open = []
    close = []
    vol = []
    adj_close = []
    
    for symbol in symbols:
        yahoo_financials = YahooFinancials(symbol)
    
        current_date = datetime.now().strftime('%Y-%m-%d')
        daily_treasury_prices = yahoo_financials.get_historical_price_data('2023-01-01', str(current_date), 'daily')
        
        for data in daily_treasury_prices[symbol]['prices']:
            symbol_.append(symbol)
            for_date.append(data['formatted_date'])
            high.append(data['high'])
            low.append(data['low'])
            open.append(data['open'])
            close.append(data['close'])
            vol.append(data['volume'])  
            adj_close.append(data['adjclose'])
            
    
    dict_ = {"Symbol":symbol_, "formated_date":for_date, "high":high, "low":low, "open":open, "close":close, "Volume":vol, "adj_close": adj_close}
    df = pd.DataFrame(dict_)    
    
    return df 


if __name__=="__main__":
    df = daily_treasury_prices()
