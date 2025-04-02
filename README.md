[Versión en Español](README.es.md)

# YouTube to MP3 Converter

This project is a web application developed with Django that allows converting YouTube videos to MP3 format. It uses FFmpeg for audio processing and provides an intuitive interface for users.

## Features

- **YouTube to MP3 Conversion**: Efficiently converts YouTube videos to MP3 audio format.
- **Video Preview**: Displays the video's thumbnail and title before conversion.

## Prerequisites

Before installing and running this project, ensure you have the following components installed:

- [Python 3.x](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html): Make sure FFmpeg is installed and accessible from the command line. You can verify this by running `ffmpeg -version` in your terminal.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/leonel2077/yt-converter-project.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd yt-converter-project
    ```

3. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
    ```

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up environment variables**:

    Create a `.env` file in the project's root directory and define the necessary variables, such as API keys or specific configurations.

6. **Apply database migrations**:

    ```bash
    python manage.py migrate
    ```

7. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

## Usage

1. **Enter the YouTube video URL**: On the main page, input the link of the video you wish to convert.

2. **Preview**: The application will display the video's thumbnail and title for confirmation.

3. **Start the conversion**: Click the "Convert" button to begin the process.

4. **Download the MP3**: Once the conversion is complete, you can download the resulting MP3 file.

## License

This project is under the MIT License. See the `LICENSE` file for more details.
