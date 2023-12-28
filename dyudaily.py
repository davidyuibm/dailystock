import smtplib
import twstock
import yfinance as yf
from bmdOilPriceFetch import bmdPriceFetch
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
smtp_port = 587
EMAIL_ADDRESS = 'xxxxxx@gmail.com'    # dyu input your gmail id
EMAIL_PASSWORD = 'yyy yyyy yyy yyyy'  #need to apply a Google API password

### get stock price
stock = twstock.Stock("2884")
Esunprice = str(stock.price[-1])

#IBM price
tickerSymbol = 'IBM'

tickerData = yf.Ticker(tickerSymbol)
todayData = tickerData.history(period='1d')
print('%.2f'%(todayData['Close'].iloc[-1]))
IBMprice =  str('%.2f'%(todayData['Close'].iloc[-1]))
#dyusend("IBM stock price", str(todayData['Close'].iloc[-1]))


#Crude oil price

data = bmdPriceFetch()
if data is not None:
    Oilprice = str(f" ${data['regularMarketPrice']:.2f}")
    print(Oilprice)
### /get stock price


body = '''
	<!DOCTYPE html>
	<html>
	<head>
		<link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<style type="text/css">
		h1{font-size:56px}
		h2{font-size:28px;font-weight:900}
		p{font-weight:100}
		td{vertical-align:top}
		#email{margin:auto;width:600px;background-color:#fff}
		</style>
	</head>
	<body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
	<div id="email">
		<table role="presentation" width="100%">
			<tr>
				<td bgcolor="#00A4BD" align="center" style="color: white;">
					<h1> Good Morning ! Formosa </h1>
				</td>
		</table>
		<table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
			<tr>
				<td bgcolor="#FFFFFF" align="center" style="color: white;">
					<p style="color:tomato;">
					ESun price yesterday. <font color="green">  ''' + Esunprice + ''' </font>
					</p>
					<p style="color:tomato;">	
						IBM price yesterday. <font color="green">''' + IBMprice + ''' </font>
					</p>
					<p style="color:tomato;">
						Real time crude Oil price. <font color="green">''' + Oilprice + ''' </font>
					</p>
				</td>
			</tr>
		</table>
	</div>
	</body>
	</html>
'''

msg = MIMEText(body, 'html')
msg['Subject'] = 'Formosa daily report'
from_email = EMAIL_ADDRESS
to_email = EMAIL_ADDRESS

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.sendmail(from_email, to_email, msg.as_string())
