# YouTube Downloader

A simple YouTube downloader that converts videos to MP3 format using `yt-dlp` and `tkinter` for the GUI.

## Features
- Download audio from YouTube videos
- Convert to MP3 format
- User-friendly GUI

## Requirements
- Python 3
- `yt-dlp` library
- `tkinter` library (comes with Python standard library)

## Installation

### 1. Installing Python

**Windows:**

1. Download and install Python 3 from the [official website](https://www.python.org/downloads/windows/).
2. During installation, make sure to check the box that says "Add Python to PATH".
3. To verify that Python is installed correctly, open a command prompt (`cmd`) and run the command `python --version`. If Python is installed, the Python version will be displayed.

**MacOS:**
1. Open a terminal and install Homebrew (if not already installed):
   
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    
3. Install Python 3:
   
    ```bash
    brew install python@3
    ```
    
4. To verify that Python is installed correctly, run the command `python3 --version` in a terminal. If Python is installed, the Python version will be displayed.

**Linux:**

1. Install Python 3 using your distribution's package manager. For example, on Debian or Ubuntu:
   
    ```bash
    sudo apt-get update
    sudo apt-get install python3
    ```
    
3. To verify that Python is installed correctly, run the command `python3 --version` in a terminal. If Python is installed, the Python version will be displayed.

### 2. Installing `yt-dlp` and `tkinter` Libraries

1. Install the `yt-dlp` and `tkinter` libraries by running the following commands in a terminal or command prompt:

    ```bash
    pip install yt-dlp
    ```
    
    Since the `tkinter` library is part of Python, you do not need to install it separately.

## Usage

1. Clone the repository:
   
    ```bash
    git clone https://github.com/Teknowm3/YoutubeToMp3.git
    cd YoutubeToMp3
    ```

2. Install the required libraries:
   
    ```bash
    pip install yt-dlp
    ```

3. Run the application:
   
    ```bash
    python YoutubeToMp3.py
    ```

4. Enter the YouTube URL in the input field.

5. Click the "Download and Convert" button.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
