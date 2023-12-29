# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.errors import HttpError

API_KEY = 'AIzaSyCunLMSXkrHuWy1bV-kfYJBcZlB_pZ5OOY'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_playlist_items(playlist_id):
    youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

    try:
        playlist_items = []
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50  # You can adjust this as needed
        )

        while request:
            response = request.execute()
            playlist_items.extend(response['items'])
            request = youtube.playlistItems().list_next(request, response)

        video_ids = [item['contentDetails']['videoId'] for item in playlist_items]
        
        videos_response = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids)
        ).execute()

        video_data = videos_response.get('items', [])

        return playlist_items, video_data

    except HttpError as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    playlist_id = 'PL3_R0-1x5KSMPNoaJRRS1rQ0EwXTiyGCQ'  # Replace with the ID of your YouTube playlist
    playlist_items, video_data = get_playlist_items(playlist_id)

    if playlist_items and video_data:
        for item, video in zip(playlist_items, video_data):
            print(f"Title: {item['snippet']['title']}")
            print(f"Video ID: {item['contentDetails']['videoId']}")
            print(f"Views: {video['statistics']['viewCount']}")
            print("-----")

