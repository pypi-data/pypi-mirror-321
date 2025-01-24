import pandas as pd




class EarningsData:
    def __init__(self, rows):

        self.lastYearRptDt = [i.get('lastYearRptDt') for i in rows]
        self.lastYearEPS = [i.get('lastYearEPS') for i in rows]
        self.time = [i.get('time') for i in rows]
        self.symbol = [i.get('symbol') for i in rows]
        self.name = [i.get('name') for i in rows]
        self.marketCap = [i.get('marketCap') for i in rows]
        self.fiscalQuarterEnding = [i.get('fiscalQuarterEnding') for i in rows]
        self.epsForecast = [i.get('epsForecast') for i in rows]
        self.noOfEsts = [i.get('noOfEsts') for i in rows]

    def as_dataframe(self):
        data = {
            'lastYearRptDt': self.lastYearRptDt,
            'lastYearEPS': self.lastYearEPS,
            'time': self.time,
            'symbol': self.symbol,
            'name': self.name,
            'marketCap': self.marketCap,
            'fiscalQuarterEnding': self.fiscalQuarterEnding,
            'epsForecast': self.epsForecast,
            'noOfEsts': self.noOfEsts,
        }
        return pd.DataFrame(data)



class Dividends:
    def __init__(self, rows):
        self.companyName = [i.get('companyName') for i in rows]
        self.symbol = [i.get('symbol') for i in rows]
        self.dividend_Ex_Date = [i.get('dividend_Ex_Date') for i in rows]
        self.payment_Date = [i.get('payment_Date') for i in rows]
        self.record_Date = [i.get('record_Date') for i in rows]
        self.dividend_Rate = [i.get('dividend_Rate') for i in rows]
        self.indicated_Annual_Dividend = [i.get('indicated_Annual_Dividend') for i in rows]
        self.announcement_Date = [i.get('announcement_Date') for i in rows]

    def as_dataframe(self):
        data = {
            'companyName': self.companyName,
            'symbol': self.symbol,
            'dividend_Ex_Date': self.dividend_Ex_Date,
            'payment_Date': self.payment_Date,
            'record_Date': self.record_Date,
            'dividend_Rate': self.dividend_Rate,
            'indicated_Annual_Dividend': self.indicated_Annual_Dividend,
            'announcement_Date': self.announcement_Date,
        }
        return pd.DataFrame(data)



class EconomicEvents:
    def __init__(self, rows):

        self.gmt = [i.get('gmt') for i in rows]
        self.country = [i.get('country') for i in rows]
        self.eventName = [i.get('eventName') for i in rows]
        self.actual = [i.get('actual') for i in rows]
        self.consensus = [i.get('consensus') for i in rows]
        self.previous = [i.get('previous') for i in rows]
        self.description = [i.get('description') for i in rows]

        self.data_dict = { 
            'gmt': self.gmt,
            'country': self.country,
            'event': self.eventName,
            'actualy': self.actual,
            'consensus': self.consensus,
            'previous': self.previous,
            'description': self.description
        }
        self.as_dataframe = pd.DataFrame(self.data_dict)



class NasdaqScreener:
    def __init__(self, rows):

        self.symbol = [i.get('symbol') for i in rows]
        self.name = [i.get('name') for i in rows]
        self.lastsale = [i.get('lastsale') for i in rows]
        self.netchange = [i.get('netchange') for i in rows]
        self.pctchange = [i.get('pctchange') for i in rows]
        self.marketCap = [i.get('marketCap') for i in rows]
        self.url = [i.get('url') for i in rows]

        self.data_dict = { 
            'ticker': self.symbol,
            'name': self.name,
            'price': self.lastsale,
            'change': self.netchange,
            'change_pct': self.pctchange,
            'market_cap': self.marketCap,
            'url': self.url
        }


        self.as_dataframe = pd.DataFrame(self.data_dict)