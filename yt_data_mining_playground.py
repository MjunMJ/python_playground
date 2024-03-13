
!pip install --upgrade google-api-python-client

!pip install --upgrade google-auth-oauthlib google-auth-httplib2

#to format outputs
from pprint import pprint
# API client library
import googleapiclient.discovery
# API information
api_service_name = "youtube"
api_version = "v3"
# API key
DEVELOPER_KEY = "AIzaSyB3Mi8u40v9jZLawCnabAsNPoAo3P7IITI"
# API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)
request = youtube.search().list(
        part="id,snippet",
        fields="items(id(videoId),snippet(publishedAt,thumbnails(default(url))))",
        maxResults=10,
        type='video', #to get only video results
        q="monkey")
# Query execution
search_response = request.execute()
pprint(search_response)

import pandas as pd

items = search_response['items']

#get additional video level metadata with videos.list



#list to store pd table

videoData= {
    'id':[],
    'publishedAt':[],
    'thumbnail':[],
    'title':[]
}

for l in items:
  vidId = l['id']['videoId']
  videoData['id'].append(vidId)
  videoData['publishedAt'].append(l['snippet']['publishedAt'])
  videoData['thumbnail'].append(l['snippet']['thumbnails']['default']['url'])
  #get video metadata like title
  r = youtube.videos().list(
       part = "snippet",
       id=vidId,
       fields = "items(snippet(title))"
       )
  video_request = r.execute()
  videoData['title']=video_request['items'][0]['snippet']['title']

df_videoData = pd.DataFrame(videoData)

pd.set_option('display.max_colwidth', None)

print(df_videoData.head())

from IPython.display import HTML

df_videoData["iframe"] = '<iframe src="' + df_videoData["thumbnail"] + '" width="100%" height="100px"></iframe>'

display(HTML(df_videoData.to_html(escape=False)))
