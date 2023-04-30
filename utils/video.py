from utils.config import api_key
from googleapiclient.discovery import build
import os


class Video:
    api_key = ""

    @classmethod
    def set_api_key(cls):
        cls.api_key = api_key
        return cls.api_key

    @classmethod
    def get_service(cls):
        with build('youtube', 'v3', developerKey=cls.api_key) as youtube_api:
            return youtube_api

    def __init__(self, video_id):
        self.set_api_key()
        self.video_id = video_id
        self.youtube_api = self.get_service()
        self.get_video_statistic()

    def get_video_statistic(self):
        video_response = self.youtube_api.videos().list(part='snippet,statistics', \
                                                    id=self.video_id).execute()
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.video_likes: int = video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']

    def __repr__(self):
        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return text[:-2]

    def __str__(self):
        return self.video_title


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        Video.__init__(self, video_id)
        self.playlist_id = playlist_id
        self.get_playlist_statistic()

    def get_playlist_statistic(self):
        playlist = self.youtube_api.playlists().list(id=self.playlist_id, part='snippet').execute()
        self.playlist_name = playlist['items'][0]['snippet']['title']

        # playlist_videos = self.youtube.playlistItems().list(playlistId=\
        #     self.playlist_id, part='contentDetails', maxResults=50,).execute()

        # получить все id видеороликов из плейлиста
        # video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items'] if video['contentDetails']['videoId'] == self.video_id]

    def __repr__(self):
        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return text[:-2]

    def __str__(self):
        return f"{self.video_title} ({self.playlist_name})"
