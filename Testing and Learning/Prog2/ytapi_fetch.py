import googleapiclient.discovery
from googleapiclient.errors import HttpError

API_KEY = 'AIzaSyCunLMSXkrHuWy1bV-kfYJBcZlB_pZ5OOY'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
quota_cost = 0

def get_all_video_details(video_ids):
    global quota_cost
    youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

    try:
        video_data = []
        # Iterate over the video_ids in chunks of 50
        for i in range(0, len(video_ids), 50):
            current_ids = video_ids[i:i + 50]
            print(f"Fetching video details for IDs: {current_ids}")
            print(f"Number of requests sent so far: {i//50+1}")     
            print("-----")

            request = youtube.videos().list(
                part="statistics",
                id=",".join(current_ids),  # Pass the current chunk of video IDs
                maxResults=min(50, len(video_ids) - i)  # Request only the remaining items
            )
            quota_cost += 1
            response = request.execute()
            video_data.extend(response.get('items', []))

        print(f"Video data (first):" + str(video_data[0]))
        print(f"Total videos fetched: {len(video_data)}")
        return video_data

    except HttpError as e:
        print(f"An error occurred while fetching video details: {e}")
        return None

def get_playlist_items(playlist_id):
    global quota_cost
    youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

    try:
        playlist_items = []
        next_page_token = ""

        while next_page_token is not None:
            request = youtube.playlistItems().list(
                part="snippet,contentDetails",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            quota_cost += 1
            response = request.execute()
            playlist_items.extend(response['items'])
            next_page_token = response.get('nextPageToken')

        video_ids = [item['contentDetails']['videoId'] for item in playlist_items]
        print(f"Playlist item (first):" + str(playlist_items[0]))
        # Add debugging output
        print("Fetching video details...")
        print(f"Video IDs: {video_ids}")  # This is a list of video IDs
        print(f"Total videos: {len(video_ids)}")  # This is the number of videos in the playlist

        # Fetching video details using pagination
        video_data = get_all_video_details(video_ids)

        paired_data = []
        for item in playlist_items:
            video_id = item['contentDetails']['videoId']
            video_info = next((video for video in video_data if video['id'] == video_id), None)
            if video_info:
                paired_data.append({'playlist_item': item, 'video_info': video_info})

        return paired_data

    except HttpError as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    playlist_id = 'PLCDmOwXsjuPYMXOGKCgH9yEUSZqebXo5U'  # Replace with the ID of your YouTube playlist
    paired_data = get_playlist_items(playlist_id)

    if paired_data:
        print(f"Total videos paired: {len(paired_data)}")
        for pair in paired_data:
            playlist_item = pair['playlist_item']
            video_info = pair['video_info']
            print(f"Title: {playlist_item['snippet']['title']}")
            print(f"Video ID: {playlist_item['contentDetails']['videoId']}")
            print(f"Views: {video_info['statistics']['viewCount']}")
            print(f"Creator: {playlist_item['snippet']['videoOwnerChannelTitle']}")
            print("-----")
    print(f"Total quota cost: {quota_cost}")