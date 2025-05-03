import json

from channels.generic.websocket import WebsocketConsumer
import google.generativeai as genai

GOOGLE_API_KEY = ""

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Connect to the client
        self.accept()
        self.send(text_data=json.dumps({
            "type":"connection_established",
            "message": "Connection is established successfully!"
        }))

        # Connect to the Gemini API
        genai.configure(api_key = GOOGLE_API_KEY)
        model_name = "gemini-2.0-flash-lite"
        self.model = genai.GenerativeModel(model_name)


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print("Message:", message)
        self.send(text_data=json.dumps({
            "type":"user_chat",
            "message": message,
        }))
        response = self.model.generate_content(message)
        print(response.text)
        self.send(text_data=json.dumps({
            "type":"ai_chat",
            "message": response.text,
        }))


    def disconnect(self, close_code):
        pass