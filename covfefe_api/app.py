from flask import Flask, request, jsonify
from google import google
from sentence_transformers import SentenceTransformer
import scipy.spatial
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def validate():
    query = request.get_json()["query"]
    results = google.search(query)
    descriptions = [r.description for r in results]

    model = SentenceTransformer('bert-base-nli-mean-tokens')
    query_embedding = model.encode(query)
    desc_embeddings = model.encode(descriptions)

    closest_n = 5
    distances = scipy.spatial.distance.cdist(query_embedding, desc_embeddings, "cosine")[0]
    closest = zip(range(len(distances)), distances)
    closest = sorted(closest, key=lambda x: x[1])

    links = []
    for idx, distance in closest[0:closest_n]:
        link = {
            "link": results[idx].link,
            "title": results[idx].name,
            "description": results[idx].description,
            "similarity": (2 - distance) / 2
        }
        links.append(link)

    return jsonify(links)

app.run(host='0.0.0.0', port=50000)
