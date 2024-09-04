FROM jauderho/yt-dlp

WORKDIR /

RUN apk add --no-cache bash curl jq

COPY ./media-dl-loop /usr/local/bin/
COPY ./instagram-dl /usr/local/bin/
COPY ./soundcloud-download /usr/local/bin/
COPY ./tiktok-dl /usr/local/bin/
COPY ./twitter-dl /usr/local/bin/
COPY ./youtube-download /usr/local/bin/
COPY ./youtube-audio-download /usr/local/bin/
COPY ./vine-dl /usr/local/bin/
COPY ./youtube-offline-playlist /usr/local/bin/
COPY ./send-pushover-message /usr/local/bin/

ENTRYPOINT [ "bash", "/usr/local/bin/media-dl-loop" ]
