from models import Features
import os
import librosa
from librosa import onset
import matplotlib.pyplot as plt
import librosa.display
from pandas import DataFrame as df
from pandas.core.frame import DataFrame

samples_directory = "./samples"
sound_file_format = ("mp3", "ogg", "wav")

def get_samples():
    """
        Loading music samples file paths to dictionary
    """
    samples: dict([str,list]) = dict()
    for genre in os.listdir(samples_directory):
        samples[genre] = []
        for file in os.listdir(f"{samples_directory}/{genre}"):
            if file.endswith(sound_file_format):
                samples[genre].append(f"{samples_directory}/{genre}/{file}") 
    return samples

def get_track_info(filename) -> Features:
    #   Load the audio as a waveform `y`
    #   Store the sampling rate as `sr`
    #   Transform it to mono for simpler analysis
    #   Start after 10 seconds to sample
    y, sr = librosa.load(filename, mono=True, offset=10)
    return y,sr

def extract_features(y, sr, genre):
    #   Remove all "silent" parts, which are unhearable for the human being
    non_silent = librosa.effects.trim(y=y, frame_length=sr, top_db=40)

    # Check which features are the best
    # onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo, beat = librosa.beat.beat_track(y, sr=sr)
    chroma = librosa.feature.chroma_stft(y, sr=sr)


    track_features = dict({
        "tempo": tempo, 
        "beat": beat,
        "chroma": chroma, 
        "genre": genre
    })
    return track_features

if __name__ == "__main__":
    print("Getting samples")
    samples = get_samples()
    track_info = dict()
    print("Getting track info")
    data = []
    for genre in samples:
        for track in samples[genre]:
            y, sr = get_track_info(track)
            tract_features = extract_features(y, sr, genre)
            data.append(tract_features)

    data_df = DataFrame(columns=["tempo", "beat", "chroma", "genre"], data=data)
    print(data_df)


