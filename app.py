import webbrowser
import os
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
@app.message("Meow")
def message_meow(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")
@app.message()
def handle_message(message,say):
    meow1 =re.findall(r'\d+', message.get('text'))
    if meow1 is None or len(meow1) == 0:
        return
    else:
        meow1=int(meow1[0])
    match meow1:
        case 1:say("Meow")
        case 2:say("Feeling sad today, please send a nice pic of your credit card front and back please")
        case 3:say("Meeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep")
        case 4:say("Side quest: Find a dragonfly eating dragonfruit and DM @Ferboinkles with a pic")
        case 5:say("Eepy")
        case 6:say("Everyone has a past and yours is coming to find you.")
        case 7:say("Once upon a time there was a cat, The End")
        case 8:say("Say Cheeeeeeeeeese like your family picture depends on it (coz it does)")
        case 9:say("Quokka, search it up")
        case 10:say("Why are you typing 10 to a random bot in a random channel in Slack? Time to lock in :3")
        case 67:say("Brainrotted disgrace to society detected, must assassinate immediately.")
        case 69:say("Ewwwwwwwwwwww")
        case 420:say("Please kindly explode")
        case _ :say("Not between 1 and 10 dum dum")

# Start
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()