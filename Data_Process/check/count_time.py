import os
from pathlib import Path
import argparse
from tqdm import tqdm
import librosa

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=str, required=True)
    
    args = parser.parse_args()
    wav_dir = args.data_dir
    read_length_flag = args.read

    # get all wav files
    wav_paths = []
    for root, dirs, files in os.walk(wav_dir):
        if len(files) > 0:
            for f_name in files:
                if Path(f_name).suffix in ['.wav']:
                    wav_paths.append(os.path.join(root, f_name))
    wav_paths = sorted(wav_paths)

    # the statistics of time
    time = 0
    for wav_path in tqdm(wav_paths, total=len(wav_paths)):
        wav_duration = librosa.get_duration(filename=wav_path)
        time += wav_duration

    time=time/3600.0
    print(f'The total time is {time} hours')