"""
License: MIT License
Copyright (c) 2023 Miel Donkers

Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

import redis


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        # logging.info(
        #    "GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers)
        # )
        r = redis.Redis(host="redis", port=6379, db=0)
        v = r.lpop("queue")
        # logging.info(v)
        self._set_response()
        if v:
            self.wfile.write(v)

    def do_POST(self):
        content_length = int(
            self.headers["Content-Length"]
        )  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info(
            "POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
            str(self.path),
            str(self.headers),
            post_data.decode("utf-8"),
        )

        r = redis.Redis(host="redis", port=6379, db=0)
        r.rpush("queue", post_data)

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=S, port=80):
    logging.basicConfig(level=logging.INFO)
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    logging.info("Starting httpd...\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info("Stopping httpd...\n")


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
