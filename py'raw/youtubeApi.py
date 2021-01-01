from googleapiclient.discovery import build

api_key = 'AIzaSyAu0II3vr64fZdqYHzQHFIHn1avRFPk-zA'

youtube = build('youtube', 'v3', developerKey=api_key)

link = "https://www.youtube.com/channel/schafer5"
username = link[32:]
print(username)

request = youtube.channels().list(
    part='statistics',
    forUsername='DjWalkzz'
)

response = request.execute()

# print(response['items'][0]['statistics']['subscriberCount'])

print(response)