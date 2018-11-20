# slackbot_real_time_messaging_api
This is a basic example of how to build a slack bot using the real time messaging API.

## Main Features
1. Reply to the message 'BOT TEST' when it is posted to a slack channel  

## Explanation of Files
1. slackbot_real_time_messaging_api.py: Source code for the slack bot.
2. configs.json: Configuration file.  

## How to Configure the slackbot_events_api_example
In order for this slack bot to work it will need a few keys to authenticate to slack, the contents of the config file as well as what they are can be found below. 
```json
{
  "slack_bot_token":""
}
```

1. slack_bot_token: This is the token of the bot user configured in slack

## How to Run
At a high level, the steps you will need to take to get this set up are listed below. If you want a more comprehensive walk through, please check out the youtube link below. 

1. Create an application in slack
2. Add a bot user to the slack application
3. Enable OAuth for the bot user
4. Grant the bot user chat:write:bot scope
7. Copy the slack bot token to the configs.json file 
8. In a terminal session launch the slack bot
    ```bash
    pip3 install -r requirements.txt
    python3 slackbot_events_api_example.py
    ```
10. Now you should be able to go to the slack app, invite the bot and then send a message
    ```bash
    /invite @slackbot_events_real_time_messaging_api
    @slackbot_events_api_example BOT TEST
    ```
11. If everything went to play the bot should respond with the following
    ```bash
    Responding to `BOT TEST` message sent by user @yourUserName
    ```
## How To Video
[Coming Soon](https://www.youtube.com/watch?v=KiBsVeT-Kqg&t=1s)
