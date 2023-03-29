import json
import os
from googleapiclient.discovery import build
from utils.config import api_key


class Channel:
    # api_key = youtube_api
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('youtube')

    def __init__(self, channel_id):
        self.__channel_id = channel_id
        self.json = ""
        self.get_json()
        self.title = self.json["items"][0]['snippet']['title']
        self.channel_description = self.json["items"][0]['snippet']['description']
        self.url = r"https://www.youtube.com/channel/" + self.__channel_id
        self.video_count = self.json["items"][0]["statistics"]["videoCount"]
        self.channel_number_of_views = self.json["items"][0]["statistics"]["viewCount"]

    def get_json(self):
        #        youtube_api = build('youtube', 'v3', developerKey=os.getenv('youtube'))
        #        with youtube_api as youtube:
        #            channel = youtube.channels().list(id=self.id, part='snippet,statistics').execute()
        #            self.json = json.dumps(channel, indent=2, ensure_ascii=False)
        channel = self.get_service().channels().list(id=self.__channel_id, part="snippet,statistics").execute()
        self.json = channel

    def save_json(self, path):
        text = "["
        for dic in self.__dict__:
            if dic != 'json':
                text += "{'" + str(dic) + "':'" + str(self.__dict__[dic]) + "'}, \n"
        json_text = text[:-3] + "]"
        with open(path, "w", encoding="UTF-8") as file:
            file.write(str(json_text))

    def print_info(self):
        print(self.json)

    @classmethod
    def get_service(cls):
        #        youtube_api = build('youtube', 'v3', developerKey=os.getenv('youtube'))
        with build('youtube', 'v3', developerKey=cls.api_key) as youtube_api:
            return youtube_api

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        if self.channel_id != channel_id:
            raise AttributeError(f"property 'channel_id' of 'Channel' object has no setter")
        self.__channel_id = channel_id
