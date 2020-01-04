"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random


@route('/', method='GET')
def index():
    return template("chatbot.html")


def jokes(user_message_list):
    jokes_list = ('I ate a clock yesterday, it was very time-consuming.', 'A perfectionist walked into a bar…apparently, the bar wasn’t set high enough.',
             'I was gonna tell a time-traveling joke, but you guys didn’t like it.', 'What do you get when you cross a snowman with a vampire? ... Frostbite')
    return json.dumps(
        {"animation": "laughing", "msg": random.choice(jokes_list)})


def answer(user_message):
    user_message_list = user_message.split()

    name = ['name']
    greetings = ['hi', 'hello', 'hey']
    greeting_responses = ('Nice seeing you today', 'Top of the mornin')
    goodbye_words = ["bye", 'goodbye']
    goodbye_responses = ('Have a great day', 'Enjoy')
    swear_words = ['asshole', 'bitch', 'shit', 'bastard', 'fuck', 'fuck you', 'cunt', 'crap', 'slut', 'twat']
    swear_responses = ('That is not a nice thing to say', 'Watch your language child')
    feelings = ["feeling", 'feeling?', 'you', 'you?']
    feelings_responses = ['afraid', 'content', 'bored', 'confused', 'heartbroke', 'in love', "excited", 'sad', 'happy']
    animal = ['animal', 'animal?']
    animal_response = ['I love dogs']
    activity = ['activity', 'free time', 'activity?', 'free time?']
    activity_response = ('making money', 'dancing')
    joke = ['joke']

    # for word in greetings:
    #     any(item == word for item in greetings):

    if any([word if word in greetings else None for word in user_message_list]):
        return json.dumps({"animation": "excited", "msg": random.choice(greeting_responses)})

    elif any([word if word in goodbye_words else None for word in user_message_list]):
        return json.dumps({"animation": "takeoff", "msg": random.choice(goodbye_responses)})

    elif any([word if word in swear_words else None for word in user_message_list]):
        return json.dumps({"animation": "no", "msg": random.choice(swear_responses)})

    elif any([word if word in feelings else None for word in user_message_list]):
        emotion_to_retrieve = random.choice(feelings_responses)
        return json.dumps({"animation": emotion_to_retrieve, "msg": emotion_to_retrieve})

    elif any([word if word in animal else None for word in user_message_list]):
        return json.dumps({"animation": "dog", "msg": animal_response})

    elif any([word if word in activity else None for word in user_message_list]):
        activity_to_retrieve = random.choice(activity_response)
        return json.dumps({"animation": activity_to_retrieve, "msg": activity_to_retrieve})

    elif any([word if word in name else None for word in user_message_list]):
        return user_name(user_message_list)

    elif any([word if word in joke else None for word in user_message_list]):
        return jokes(user_message_list)

    else:
        return json.dumps({"animation": "no", "msg": "Please say something I can reply to..."})


def user_name(user_message_list):
    return json.dumps(
            {"animation": "takeoff", "msg": f'Hello {user_message_list[user_message_list.index("name") + 2]}'})


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return answer(user_message)


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()