# -*- coding: utf-8 -*-
"""


@author: kafe1012
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

#Pfad return anhand Symbol für CSV-Datei
def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

#Daten auslesen    
def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    
    for symbol in symbols:
        #Auslesen und joinen für jede gewünschte Datei
        df_temp = pd.read_csv("data/{}.csv".format(symbol), sep=';', index_col='Date', usecols=['Date','Open'], parse_dates=True, na_values=['NaN'])
#        df_temp = df_temp.rename(columns={'Open':symbol})
        df = df.join(df_temp)
        
        
#    df['Date'] = df['Date'].apply(pd.to_datetime)
    return df
  
#Maximaler Open Preis anhand Auswahlkriterien(Symbole)
def get_mean_open(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol), sep=';')
    return df['Open'].mean()


def plot_data(df):
    df[['Open']].plot()
    plt.xlabel('Time')
    plt.ylabel('Price in Dollar')
    plt.title('Open prices over time')
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    #plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()  # must be called to show plots
    
#Funktion zum Testen
def test_run():
#    for symbol in ['2016', '2015', '2014', '2013', '2012', '2011']:
#        print "Mean Open Price", symbol
#        print round(get_mean_open(symbol),2)
    
    #Definiere Zeitraum
    dates = pd.date_range('2016-09-13','2016-09-18')
    
    #Definiere Auswahldaten mit Symbol
    symbols = ['BITSTAMP']
    
    #Get Open Daten
    df = get_data(symbols, dates)
    print df
    plot_data(df)

#Ausführung
if __name__ == "__main__":
    test_run()
