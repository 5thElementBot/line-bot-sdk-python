import base64
import errno
import json
import os
import sys
import tempfile
import requests
import urllib.request
from argparse import ArgumentParser
from requests import Request, Session
from PIL import Image
from io import BytesIO

from flask import Flask, request, abort
from py_translator import Translator

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.http_client import (
    HttpClient, RequestsHttpClient
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, JoinEvent, LeaveEvent, SourceUser, SourceGroup, SourceRoom,
    ConfirmTemplate, MessageAction, TemplateSendMessage,Action, PostbackEvent, MemberIds, Profile, ImageMessage,
    VideoMessage, AudioMessage, FileMessage, QuickReply, QuickReplyButton, PostbackAction
)
app = Flask(__name__)

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

# function for create tmp dir for download content
def make_static_tmp_dir():
    try:
        os.makedirs(static_tmp_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(static_tmp_path):
            pass
        else:
            raise

@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """ Here's all the messages will be handled and processed by the program """
    msg = (event.message.text).lower()
    if msg == 'hello':
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text="Welcome USER!"),
            ImageSendMessage(original_content_url='https://cdn-images-1.medium.com/max/1000/1*6CyTuYz0D92cl4ynXjW45A.jpeg',
                            preview_image_url='https://cdn-images-1.medium.com/max/1000/1*6CyTuYz0D92cl4ynXjW45A.jpeg')])
    elif msg.startswith('.'):
       line_bot_api.multicast(['U62b2508cbda91348fad7fed215af16ea'], #5th
                              TextSendMessage(text='A PROHIBITED COMMAND WAS TYPED!'))
       line_bot_api.push_message('C2cc611a343203dcce471e4c8d3784d7e',TextSendMessage(text='A PROHIBITED COMMAND WAS TYPED!'))#R4 Room
       line_bot_api.reply_message(
           event.reply_token,
            [TextSendMessage(text="WARNING: PROHIBITED COMMAND!")])
    elif msg.endswith('> fr') or msg.endswith('>fr') or msg.endswith('>fr ') or msg.endswith('> fr '):
       s_fr_parsed = msg[:-4]
       print(s_fr_parsed)
       s_fr_parsed_trans = Translator().translate(text=s_fr_parsed, dest='fr').text
       print(s_fr_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_fr_parsed_trans)])
    elif msg.endswith('> en') or msg.endswith('>en') or msg.endswith('>en ') or msg.endswith('> en '):
       s_en_parsed = msg[:-4]
       print(s_en_parsed)
       s_en_parsed_trans = Translator().translate(text=s_en_parsed, dest='en').text
       print(s_en_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_en_parsed_trans)])
    elif msg.endswith('> sp') or msg.endswith('>sp') or msg.endswith('>sp ') or msg.endswith('> sp '):
       s_sp_parsed = msg[:-4]
       print(s_sp_parsed)
       s_sp_parsed_trans = Translator().translate(text=s_sp_parsed, dest='es').text
       print(s_sp_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_sp_parsed_trans)])
    elif msg.endswith('> vi') or msg.endswith('>vi') or msg.endswith('>vi ') or msg.endswith('> vi '):
       s_vi_parsed = msg[:-4]
       print(s_vi_parsed)
       s_vi_parsed_trans = Translator().translate(text=s_vi_parsed, dest='vi').text
       print(s_vi_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_vi_parsed_trans)])
    elif msg.endswith('> cn') or msg.endswith('>cn') or msg.endswith('>cn ') or msg.endswith('> cn '):
       s_cn_parsed = msg[:-4]
       print(s_cn_parsed)
       s_cn_parsed_trans = Translator().translate(text=s_cn_parsed, dest='zh-cn').text
       print(s_cn_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_cn_parsed_trans)])
    elif msg.endswith('> th') or msg.endswith('>th') or msg.endswith('>th ') or msg.endswith('> th '):
       s_th_parsed = msg[:-4]
       print(s_th_parsed)
       s_th_parsed_trans = Translator().translate(text=s_th_parsed, dest='th').text
       print(s_th_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_th_parsed_trans)])
    elif msg.endswith('> ru') or msg.endswith('>ru') or msg.endswith('>ru ') or msg.endswith('> ru '):
       s_ru_parsed = msg[:-4]
       print(s_ru_parsed)
       s_ru_parsed_trans = Translator().translate(text=s_ru_parsed, dest='ru').text
       print(s_ru_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_ru_parsed_trans)])
    elif msg.endswith('> it') or msg.endswith('>it') or msg.endswith('>it ') or msg.endswith('> it '):
       s_it_parsed = msg[:-4]
       print(s_it_parsed)
       s_it_parsed_trans = Translator().translate(text=s_it_parsed, dest='it').text
       print(s_it_parsed_trans)
       line_bot_api.reply_message(
           event.reply_token,
           [TextSendMessage(text=s_it_parsed_trans)])
    elif msg == 'profile' or msg == 'profile ':
        if isinstance(event.source, SourceGroup):
          profile = line_bot_api.get_group_member_profile(event.source.group_id, event.source.user_id)
          line_bot_api.reply_message(
            event.reply_token,
             [TextSendMessage(text=profile.display_name),
              TextSendMessage(text='User id: ' + profile.user_id),
              TextSendMessage(text='Group id: ' + event.source.group_id),
             ])
        else:
          profile = line_bot_api.get_profile(event.source.user_id)
          line_bot_api.reply_message(
            event.reply_token,
             [TextSendMessage(text=profile.display_name),
              TextSendMessage(text='User id: ' + profile.user_id),
             ])
    elif msg == 'time':
       print('TIME IN CHINA')
       time_api_address = 'http://worldtimeapi.org/api/timezone/Asia/Hong_Kong'
       time_api_address1 = 'http://worldtimeapi.org/api/timezone/Asia/Bangkok'
       time_api_address2 = 'http://worldtimeapi.org/api/timezone/Europe/London'
       time_api_address3 = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'
       time_api_address3a = 'http://worldtimeapi.org/api/timezone/Europe/Paris'
       time_api_address4 = 'http://worldtimeapi.org/api/timezone/Europe/Rome'
       time_api_address5 = 'http://worldtimeapi.org/api/timezone/Australia/Sydney'
       time_api_address6 = 'http://worldtimeapi.org/api/timezone/America/Toronto'
       time_api_address7 = 'http://worldtimeapi.org/api/timezone/America/Vancouver'
       time_api_address8 = 'http://worldtimeapi.org/api/timezone/America/Los_Angeles'
       time_api_address9 = 'http://worldtimeapi.org/api/timezone/America/New_York'
       print(time_api_address)
       json_timedata = requests.get(time_api_address).json()
       json_timedata1 = requests.get(time_api_address1).json()
       json_timedata2 = requests.get(time_api_address2).json()
       json_timedata3 = requests.get(time_api_address3).json()
       json_timedata3a = requests.get(time_api_address3a).json()
       json_timedata4 = requests.get(time_api_address4).json()
       json_timedata5 = requests.get(time_api_address5).json()
       json_timedata6 = requests.get(time_api_address6).json()
       json_timedata7 = requests.get(time_api_address7).json()
       json_timedata8 = requests.get(time_api_address8).json()
       json_timedata9 = requests.get(time_api_address9).json()
       print(json_timedata)
       timezone_json_data = json_timedata['timezone']
       timezone_json_data1 = json_timedata1['timezone']
       timezone_json_data2 = json_timedata2['timezone']
       timezone_json_data3 = json_timedata3['timezone']
       timezone_json_data3a = json_timedata3a['timezone']
       timezone_json_data4 = json_timedata4['timezone']
       timezone_json_data5 = json_timedata5['timezone']
       timezone_json_data6 = json_timedata6['timezone']
       timezone_json_data7 = json_timedata7['timezone']
       timezone_json_data8 = json_timedata8['timezone']
       timezone_json_data9 = json_timedata9['timezone']
       datetime_json_data = json_timedata['datetime']
       datetime_json_data1 = json_timedata1['datetime']
       datetime_json_data2 = json_timedata2['datetime']
       datetime_json_data3 = json_timedata3['datetime']
       datetime_json_data3a = json_timedata3a['datetime']
       datetime_json_data4 = json_timedata4['datetime']
       datetime_json_data5 = json_timedata5['datetime']
       datetime_json_data6 = json_timedata6['datetime']
       datetime_json_data7 = json_timedata7['datetime']
       datetime_json_data8 = json_timedata8['datetime']
       datetime_json_data9 = json_timedata9['datetime']
       datetime_short = datetime_json_data[:19]
       datetime_short1 = datetime_json_data1[:19]
       datetime_short2 = datetime_json_data2[:19]
       datetime_short3 = datetime_json_data3[:19]
       datetime_short3a = datetime_json_data3a[:19]
       datetime_short4 = datetime_json_data4[:19]
       datetime_short5 = datetime_json_data5[:19]
       datetime_short6 = datetime_json_data6[:19]
       datetime_short7 = datetime_json_data7[:19]
       datetime_short8 = datetime_json_data8[:19]
       datetime_short9 = datetime_json_data9[:19]
       print(timezone_json_data)
       print(datetime_json_data)
       print(datetime_short)
       line_bot_api.reply_message(
           event.reply_token,
            TextSendMessage(text=timezone_json_data + '\n' + datetime_short + '\n\n' +
                           timezone_json_data1 + '\n' + datetime_short1 + '\n\n' +
                           timezone_json_data2 + '\n' + datetime_short2 + '\n\n' +
                           timezone_json_data3 + '\n' + datetime_short3 + '\n\n' +
                           timezone_json_data3a + '\n' + datetime_short3a + '\n\n' +
                           timezone_json_data4 + '\n' + datetime_short4 + '\n\n' +
                           timezone_json_data5 + '\n' + datetime_short5 + '\n\n' +
                           timezone_json_data6 + '\n' + datetime_short6 + '\n\n' +
                           timezone_json_data7 + '\n' + datetime_short7 + '\n\n' +
                           timezone_json_data8 + '\n' + datetime_short8 + '\n\n' +
                           timezone_json_data9 + '\n' + datetime_short9))
    elif 'currency convert' in msg:
        print('CURRENCY')
        currency_api_key = 'a8a5425df38082adee49'
        currency_api_address = 'https://free.currconv.com/api/v7/convert?q='
        currency_pair = msg[17:]
        print(currency_pair)
        currency_pair_notrailspace = currency_pair.rstrip()
        print(currency_pair_notrailspace)
        currency_address = currency_api_address + currency_pair_notrailspace
        currency_address_full = currency_address.replace(' ', '_', 1) + '&compact=ultra&apiKey=' + currency_api_key
        print(currency_address_full)
        try:
            json_currency_pair = requests.get(currency_address_full).json()
            print(json_currency_pair)
            json_rate = str(json_currency_pair)
            print(json_rate)
            line_bot_api.reply_message(
                event.reply_token,
                 TextSendMessage(text=json_rate))
        except:
            print('CURRENCY PAIR NOT FOUND')
            line_bot_api.reply_message(
              event.reply_token,
               TextSendMessage(text='currency pair not found'))
    elif 'currency list' in msg:        
        print('CURRENCY LIST')
        currency_api_key = 'a8a5425df38082adee49'
        currency_api_list_address = 'https://free.currconv.com/api/v7/currencies?&compact=ultra&apiKey=' + currency_api_key
        print(currency_api_list_address)
        json_currency_api_list_address = requests.get(currency_api_list_address).json()
        json_list = []
        for key1, key2 in json_currency_api_list_address.items():
          print("\nSymbol:", key1)
          for key in sorted(key2):
            print(key + ':', key2[key])
            json_list.append(key + ':')
            json_list.append(key2[key])
        del json_list[1::2]
        print(*json_list, sep = "\n")
        symbol_list = str(json_list)
        line_bot_api.reply_message(
          event.reply_token,
           TextSendMessage(text='List of all currency symbols: \n\n' + symbol_list))
    elif 'tastedive' in msg:
        print('TASTEDIVE')
        tastedive_api_key = '332528-LINEappc-Y51EWKIR'
        tastedive_api_address = 'https://tastedive.com/api/similar?q='
        query = msg[10:]
        print(query)
        tastedive_address = tastedive_api_address + query
        tastedive_address_full = tastedive_address.replace(' ', '+') + '&k=' + tastedive_api_key + '&limit=5&info=1'
        print (tastedive_address_full)
        try:
           json_tastedive_data = requests.get(tastedive_address_full).json()
           print(json_tastedive_data)
           wTeaser_json_data_source = json_tastedive_data['Similar']['Info'][0]['wTeaser']
           wTeaser_json_data_source_short = wTeaser_json_data_source.partition(".")[0]
           name_json_data = json_tastedive_data['Similar']['Results'][0]['Name']
           type_json_data = json_tastedive_data['Similar']['Results'][0]['Type']
           wTeaser_json_data = json_tastedive_data['Similar']['Results'][0]['wTeaser']
           wTeaser_json_data_short = wTeaser_json_data.partition(".")[0]
           name_json_data1 = json_tastedive_data['Similar']['Results'][1]['Name']
           type_json_data1 = json_tastedive_data['Similar']['Results'][1]['Type']
           wTeaser_json_data1 = json_tastedive_data['Similar']['Results'][1]['wTeaser']
           wTeaser_json_data_short1 = wTeaser_json_data1.partition(".")[0]
           name_json_data2 = json_tastedive_data['Similar']['Results'][2]['Name']
           type_json_data2 = json_tastedive_data['Similar']['Results'][2]['Type']
           wTeaser_json_data2= json_tastedive_data['Similar']['Results'][2]['wTeaser']
           wTeaser_json_data_short2= wTeaser_json_data2.partition(".")[0]
           name_json_data3 = json_tastedive_data['Similar']['Results'][3]['Name']
           type_json_data3 = json_tastedive_data['Similar']['Results'][3]['Type']
           wTeaser_json_data3= json_tastedive_data['Similar']['Results'][3]['wTeaser']
           wTeaser_json_data_short3= wTeaser_json_data3.partition(".")[0]
           name_json_data4 = json_tastedive_data['Similar']['Results'][4]['Name']
           type_json_data4 = json_tastedive_data['Similar']['Results'][4]['Type']
           wTeaser_json_data4= json_tastedive_data['Similar']['Results'][4]['wTeaser']
           wTeaser_json_data_short4= wTeaser_json_data4.partition(".")[0]
           print(wTeaser_json_data_source_short)
           print(name_json_data)
           print(type_json_data)
           print(wTeaser_json_data_short)
           print(name_json_data1)
           print(type_json_data1)
           print(wTeaser_json_data_short1)
           print(name_json_data2)
           print(type_json_data2)
           print(wTeaser_json_data_short2)
           line_bot_api.reply_message(
              event.reply_token,
               TextSendMessage(text=wTeaser_json_data_source_short + '\n\n' + 'Top 5 recommendations if you like ' + query + ':\n\n' +
                          '#1 ' + name_json_data  + ', ' + type_json_data + '\n' + wTeaser_json_data_short + '\n\n' +
                          '#2 ' + name_json_data1  + ', ' + type_json_data1 + '\n' + wTeaser_json_data_short1 + '\n\n' + 
                          '#3 ' + name_json_data2  + ', ' + type_json_data2 + '\n' + wTeaser_json_data_short2 + '\n\n' +
                          '#4 ' + name_json_data3  + ', ' + type_json_data3 + '\n' + wTeaser_json_data_short3 + '\n\n' + 
                          '#5 ' + name_json_data4  + ', ' + type_json_data4 + '\n' + wTeaser_json_data_short4 + '\n'))
        except:
            print('SEARCH STRING NOT FOUND')
            line_bot_api.reply_message(
              event.reply_token,
               TextSendMessage(text='Search not found'))
    if msg == 'rally time!':
       line_bot_api.multicast(['U62b2508cbda91348fad7fed215af16ea', #5th
                              'U9e7737b7c02a8b4a02d9be1f09103b0e', #Reegs
                              'U4724e91e674196b95420b4fe6f4818c6', #Moon
                              'U056ece3bb99fb746579fef25f2c91dab'], #Capt
                              TextSendMessage(text='RALLY TIME GET ON NOW!!'))
       line_bot_api.push_message('C4583fe9927c38c1509cb29147e1afe4f',TextSendMessage(text='RALLY TIME GET ON NOW!!'))#group 1UP Family
       line_bot_api.push_message('Cab87dccba4b27adb89ccbef427ea0422',TextSendMessage(text='RALLY TIME GET ON NOW!!'))#1UpUv Rally Chat
       line_bot_api.push_message('C149f17b661f687e0da27f2369ea11e27',TextSendMessage(text='RALLY TIME GET ON NOW!!'))#1UP Rally NO TALK
       line_bot_api.push_message('C2cc611a343203dcce471e4c8d3784d7e',TextSendMessage(text='RALLY TIME GET ON NOW!!'))#R4 Room
       line_bot_api.reply_message(
           event.reply_token,
            TextSendMessage(text='All groups and users have been notified!!'))
    elif msg == 'kick bot':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
    elif 'weather in' in msg:
        weather_api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=5eaa7d67e46c14a502d0b3179c7d2fb3&units=metric&q='
        city = msg[11:]
        weather_url = weather_api_address + city
        json_data = requests.get(weather_url).json()
        print(json_data)
        description_json_data = json_data['weather'][0]['description']
        temperature_json_data = json_data['main']['temp']
        country = json_data['sys']['country']
        city = json_data['name']
        print(description_json_data)
        print(temperature_json_data)
        print(country)
        print(city)
        line_bot_api.reply_message(
            event.reply_token,
             [TextSendMessage(text=city + ', ' + country),
              TextSendMessage(text=description_json_data + ', ' +  'Temp=' + str(temperature_json_data) + 'c' + ' or ' +
                             str(temperature_json_data*1.8+32) + 'F')])
#    else
#       line_bot_api.reply_message(
#           event.reply_token,
#           TextSendMessage(text=event.message.text))
#@handler.add(PostbackEvent)
#def handle_postback(event):
#    if event.postback.data == 'kick bot':
#            if isinstance(event.source, SourceGroup):
#                line_bot_api.reply_message(
#                    event.reply_token, TextSendMessage(text='Leaving group'))
#                line_bot_api.leave_group(event.source.group_id)
#            elif isinstance(event.source, SourceRoom):
#                line_bot_api.reply_message(
#                    event.reply_token, TextSendMessage(text='Leaving group'))
#                line_bot_api.leave_room(event.source.room_id)
#            else:
#                line_bot_api.reply_message(
#                    event.reply_token,
#                    TextSendMessage(text="Bot can't leave from 1:1 chat"))
#    elif event.postback.data == 'nokick bot':
#        line_bot_api.reply_message(
#            event.reply_token, TextSendMessage(text="Bot still here"))
@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Joined this ' + event.source.type))
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
