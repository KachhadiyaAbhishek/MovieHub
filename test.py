from pymongo import MongoClient
import re

client = MongoClient("mongodb://localhost:27017/")
db = client["hdhub4u"]
collection = db["movieList_2025_09_01"]

searchTerm = "Love Untangled (2025) WEB-DL [Hindi (DD5.1) & English] 4K 1080p 720p & 480p Dual Audio [x264/10Bit-HEVC] | Full Movie"
escapedTerm = re.escape(searchTerm)

results = collection.find({
    "movieName": {
        "$regex": escapedTerm,
        "$options": "i"
    }
})

for movie in results:
    movie.pop("_id")
    print(movie)