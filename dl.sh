nohup yt-dlp --write-sub --write-auto-sub --sub-lang "en.*",live_chat -o "%(upload_date)s - %(title)s/%(title)s [%(id)s].%(ext)s" --restrict-filenames --download-archive list.txt https://www.youtube.com/@JellyHoshiumi/streams &> dl_status.log &

