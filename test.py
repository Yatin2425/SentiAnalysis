import googleapiclient.discovery

def test_youtube_api(developer_id, video_id, results):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = developer_id
    

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    yt_request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=results
    )
    response = yt_request.execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        print({
            'author_name': comment['authorDisplayName'],
            'published_at': comment['publishedAt'],
            'updated_at': comment['updatedAt'],
            'like_count': comment['likeCount'],
            'text': comment['textDisplay']
        })

test_youtube_api("AIzaSyBztcq-7wJa_12T5J28W9i6RuvAAM12yfE", "ckNEdxQ0Tc0", 10)
