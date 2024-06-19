from flask import Flask, request, jsonify ,url_for
import googleapiclient.discovery

app = Flask(__name__)

@app.route("/get-comments/<developer_id>/<video_id>/<int:results>", methods=['GET'])
def get_comments(developer_id , video_id , results):
    try:
        # developer_id = request.args.get('developer_id', default="AIzaSyBztcq-7wJa_12T5J28W9i6RuvAAM12yfE")
        # video_id = request.args.get('video_id', default="ckNEdxQ0Tc0")
        # results = request.args.get('results', default=10, type=int)
        dev_id = developer_id
        vi_id = video_id
        res = results

        if not dev_id or not vi_id:
            return jsonify({"error": "developer_id and video_id are required parameters"}), 400

        # Initialize YouTube Data API client
        api_service_name = "youtube"
        api_version = "v3"
        youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=dev_id)

        # Make request to fetch comments
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=vi_id,
            maxResults=results
        )
        response = request.execute()

        comments = []

        for item in response.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({
                'author_name': comment['authorDisplayName'],
                'published_at': comment['publishedAt'],
                'updated_at': comment['updatedAt'],
                'like_count': comment['likeCount'],
                'text': comment['textDisplay']
            })

        return jsonify(comments), 200

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500
def generate_url_for_get_comments(developer_id, video_id, results):
    with app.test_request_context():
        url = url_for('get_comments', developer_id=developer_id, video_id=video_id, results=results, _external=True)
    return url


if __name__ == '__main__':

    app.run(debug=True)
