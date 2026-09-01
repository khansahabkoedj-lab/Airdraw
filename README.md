# Sound Booster Tools

This repository contains two Python tools to help boost audio volume on Windows.

## Tools Included

### 1. Audio File Volume Booster (`sound_booster.py`)
A graphical application that allows you to select an audio file (e.g., MP3, WAV) and boost its volume by a specified number of decibels (dB), then save the boosted file.

### 2. System Volume Maximizer (`system_volume_max.py`)
A command-line script specifically for Windows that programmatically un-mutes and maximizes the system's master volume.

## Prerequisites

These scripts are built in Python and require certain libraries to function.

1. Install [Python](https://www.python.org/downloads/) (version 3.7 or higher recommended).
2. For the `sound_booster.py` to process audio files correctly, you may need to install **FFmpeg** and add it to your system PATH.
   - Download FFmpeg from [here](https://ffmpeg.org/download.html).

## Installation

1. Clone or download this repository.
2. Open a Command Prompt or PowerShell in the repository folder.
3. Install the required Python dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Using the Audio File Volume Booster

Run the following command:
```bash
python sound_booster.py
```
A window will open. Click "Select Audio File", choose the amount to boost in dB, and click "Boost and Save" to choose where to save the output file.

### Using the System Volume Maximizer (Windows Only)

Run the following command:
```bash
python system_volume_max.py
```
This will instantly set your Windows system volume to 100%.
