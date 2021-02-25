import unittest
import requests
import logging
from cfg import host, port

logging.basicConfig(level=logging.DEBUG)


class UrlShorteningTests(unittest.TestCase):

    def test_post_get(self):
        url = "http://{}:{}/shorten".format(host, port)
        long_url = "https://www.google.com/maps/place/2360+3rd+St,+San+Francisco,+CA+94107/@37.7597267," \
                   "-122.3909953,17z/data=!3m1!4b1!4m5!3m4!1s0x808f7fb9c99118a7:0xa0ef6a150b3dc463!8m2!3d37." \
                   "7597267!4d-122.3888066?hl=en"
        data = {"url": long_url}
        r = requests.post(url, json=data)
        logging.debug(r.status_code)
        logging.debug(r.text)

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['url'], long_url)

        short_url = r.json()['short_url']

        r = requests.get(short_url)
        logging.debug(r.status_code)
        logging.debug(r.text)

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['url'], long_url)
        self.assertEqual(r.json()['short_url'], short_url)


if __name__ == '__main__':
    unittest.main()
