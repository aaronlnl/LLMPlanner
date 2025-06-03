import json
import os

from channels.generic.websocket import WebsocketConsumer
from google import genai
from google.genai import types

from .models import User, CalendarEvent
from datetime import datetime

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

def get_user_id() -> str:
    """ Returns the user id of the user in the current session.
    Args: None
    """
    return "2"

def get_schedule(user_id: str, **kwargs) -> list[str]:
    """ Returns a list of string representations of events in the schedule of the user filtered by any fields.
    Args: 
        user_id (str): the user id of the user
        kwargs: Additional CalendarEvent field filters. Acceptable keys are:
            - title (str)
            - location (str)
            - description (str)
            - start_date (datetime.date): start date of event
            - start_time (datetime.time): start time of event
            - end_date (datetime.date): end date of event
            - end_time (datetime.time): end time of event
    """
    events = CalendarEvent.objects.filter(user=user_id, **kwargs)
    return [str(event) for event in events]

def get_time_now() -> datetime:
    """Returns the current datetime.
    Args: None
    """
    return datetime.now()

def print_history(chat):
  for content in chat.get_history():
      for part in content.parts:
          if part.text:
              print(part.text)
          if part.function_call:
              print("Function call: {", part.function_call, "}")
          if part.function_response:
              print("Function response: {", part.function_response, "}")
      print("-" * 80)

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Connect to the client
        self.accept()
        self.send(text_data=json.dumps({
            "type":"connection_established",
            "message": "Connection is established successfully!"
        }))

        # Connect to the Gemini API
        self.client = genai.Client(api_key = GOOGLE_API_KEY)

        # MODEL_ID = "gemini-2.0-flash-lite"
        MODEL_ID = "gemini-2.5-flash-preview-05-20"
        system_instruction = """
            You are a helpful AI assistant capable of helping users understand their daily schedule.
            You must look up the user id of the current user using function calling, and must not access events of other users.
            For more complex questions that involve thinking instead of accessing only one event, please filter the events as much as possible,
            then based on the full list of events, answer the user's enquiries using logical thinking.
        """
        tools = [get_time_now, get_schedule, get_user_id]
        self.chat = self.client.chats.create(
            model = MODEL_ID,
            config = {
                "tools": tools,
                "system_instruction": system_instruction,
                "automatic_function_calling": {"disable": False},
            },
        )


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print("Message:", message)
        self.send(text_data=json.dumps({
            "type":"user_chat",
            "message": message,
        }))
        response = self.chat.send_message(message)
        print(response.text)
        self.send(text_data=json.dumps({
            "type":"ai_chat",
            "message": response.text,
        }))


    def disconnect(self, close_code):
        print_history(self.chat)
        pass