from django.shortcuts import render
import yfinance as yahooFinance
from .models import Position

# Create your views here.
def home (request):
    ticker=request.POST['ticker'] 
    stock_data = yahooFinance.Ticker(ticker)
    try:
        stock_info = stock_data.info
    except:
        apiCall = "Error..."
    print("rendering now")
    return render(request, 'home.html', {'apiCall' : apiCall})



def portfolio(request):
    portfolio = Position.objects.all()
    for stock in portfolio:
       stock_data = yahooFinance.Ticker(stock.asset)
       stock_price = stock_data.info['currentPrice']
       stock.price = stock_price
       stock.value = stock_price * stock.quantity
       
       
    return render(request, 'portfolio.html', {'portfolio' : portfolio})