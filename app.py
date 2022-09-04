# flask code goes here

from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from elza_bot import ask, append_interaction_to_chat_log

app = Flask(__name__)

app.config['SECRET_KEY'] = "n\xc8.\xbfmS1\x94@\xbd\x898(W\xaf\xd0\xa1\x0c\xf0\x80|\x83\xaf\xcc"

@app.route('/elza_bot', methods=['POST'])
def elza():
  incoming_msg = request.values['Body']
  chat_log = session.get('chat_log')
  answer = ask(incoming_msg, chat_log)
  session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, chat_log)
  msg = MessagingResponse()
  msg.message(answer)
  return str(msg)


if __name__ == "__main__":
  app.run(debug=True)