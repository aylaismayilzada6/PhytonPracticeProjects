import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "GSIY6VBJJ4N6L1QG"
TWIL_SID = "real_sid"
TWIL_TOKEN = "real_token"
NEWS_API = "real_key"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

api_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
api_response.raise_for_status()
stock_json = api_response.json()

if "Time Series (Daily)" not in stock_json:
    print("Stock API error:")
    print(stock_json)
    raise SystemExit

data = stock_json["Time Series (Daily)"]
data_list = list(data.items())

yesterday_data = data_list[0][1]
day_before_yesterday_data = data_list[1][1]

yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


difference_in_closing = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference_in_closing / float(day_before_yesterday_closing_price))*100

if diff_percent > 5:
    news_parameters = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME,
        "pageSize": 3
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles =[f"HeadLine: {articles['title']}. \n Brief: {articles['description']}" for articles in three_articles ]


    client = Client(TWIL_SID, TWIL_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+18777804236",
            to='whatsapp:+994517671533'
        )

