from slackclient import SlackClient
import json
import time

#simple comment used to open a pull request.

tokens = {}
with open('configs.json') as json_data:
    tokens = json.load(json_data)

slack_client = SlackClient(tokens.get("slack_bot_token"))

if slack_client.rtm_connect():
    while slack_client.server.connected is True:
        messages = slack_client.rtm_read()
        print(messages)
        if messages:
            for message in messages:
                if message.get("subtype") is None and message.get('user') is not None and message.get('text') is not None and  "BOT TEST" in message.get('text'):
                    channel = message["channel"]
                    send_message = "Responding to `BOT TEST` message sent by user <@%s>" % message["user"]
                    slack_client.api_call("chat.postMessage", channel=channel, text=send_message)

        time.sleep(1)
else:
    print("Connection Failed")