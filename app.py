from flask import Flask,render_template
import requests
app = Flask(__name__)

bot_token = '7125527757:AAFgFpO2wKZ7_5Sdm18FeZnSsj6RPTPl7ac'

@app.route('/')
def home():
   return "<h1>Welcome to EQ Bed</h1>"

@app.route('/a')
def hello():
   send()
   return render_template('index.html')
 
def send():
   chat_ids = ['1738454260','1890659697']
   telegram_message = 'EarthQuake Alert\n Location\n \t\t Lat:11°19\'25.0\"N\n \t\t Lon:77°40\'30.4\"E \nLocation Link:https://maps.app.goo.gl/RUhEhqUDee3btt43A'

   # Send the message to each chat ID in the list
   for chat_id in chat_ids:
      # Send message to Telegram bot API
      requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage',
                  data={'chat_id': chat_id, 'text': telegram_message})
if __name__ == '__main__':
    app.run(debug=True)