from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=32Sh5yvm4pg")

video.streams.filter(progressive=True, file_extension='mp4').order_by(
    'resolution').desc().first().download()
