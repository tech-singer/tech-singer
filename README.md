# TechSinger: Technique Controllable Singing Voice Synthesis via Flow Matching

We introduce TechSinger, an advanced  via flow matching for controllable singing voice synthesis that supports five languages and seven vocal techniques.

We provide the processing codes now in this repository.

Also, you can visit our [Demo Page](https://tech-singer.github.io/) for the results of the generated singing audios.

## Code for preprocessing

The code for processing data is provided in the `./Data_Process`.

### Despendencies

A suitable [conda](https://docs.conda.io/en/latest/) environment named `tech_data` can be created and activated with:

```bash
git clone https://github.com/tech-singer/tech-singer.git
conda create -n tech_data python=3.8 -y
conda activate tech_data
pip install -r requirements.txt
```

#### Data Check

The code for checking the data is provided in `./Data_Process/check/`, including the following files:

- `count_time.py`: Count the time of audios in the directory.

- `plot_f0.py`: Plot the pitch(f0) of the singing voice audio.

- `plot_mel.py`: Plot the mel-spectrogram of audio.

#### Data Preprocessing

The code for preprocessing data is provided in `./Data-Process/process/`, including the following files:

- `gen_final_json.py`: Generate the final JSON file for each singing voice based on the TextGrid file that have been annotated.

- `seg_audio.py`: For the segmentation of singing voice audio.
