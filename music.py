from pytube import YouTube

def download_audio(youtube_url):
    try:
        yt = YouTube(youtube_url)
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        stream.download(filename=f'{yt.title}.mp4')

        print("Se descargó el audio correctamente.")
    except Exception as e:
        print("Error: " + str(e))

# URL del video de YouTube a descargar
youtube_url = 'https://www.youtube.com/watch?v=uMx-t0l68EQ&list=RDskKN82KyL_w&index=11'

# Llamada a la función para descargar solo el audio
download_audio(youtube_url)

