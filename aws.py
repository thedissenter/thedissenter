import re
import os
import boto3
import json

def getEpisodeID(filename):
    filename = os.path.basename(filename)
    return re.sub("\.[^.]*", "", filename)

# Download transcript files from S3
def DownloadTranscript(config):
    client = boto3.client('s3')
    response = client.list_objects_v2(Bucket=config['transcript-bucket'])

    for o in response['Contents']:
        filename = o["Key"]
        episodeID = getEpisodeID(filename)
        if filename.endswith(".json") and episodeID is not None:
            filepath = os.path.join('episode', episodeID)
            if not os.path.isdir(filepath):
                os.makedirs(filepath)
            filepath = os.path.join(filepath, 'transcript.json')
            print('Getting transcript for episode ' + episodeID + ' from ' + filename + ' to ' + filepath)
            client.download_file(config['transcript-bucket'], filename, filepath)

configfile = open('incharge-podcaster.json', mode='r', encoding='utf-8')
config = json.load(configfile)
configfile.close

DownloadTranscript(config)
