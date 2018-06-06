#!/usr/bin/env python3

import os
import random
import time
import tweepy
import sys

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FOLDER_PATH = r""


def post_tweet(image, msg=""):
    """Post a tweet with a picture and an optional msg."""
    try:
        api.update_with_media(image, status=msg)
    except tweepy.error.TweepError as tweep_error:
        print("Twitter Error: {} for {}".format(tweep_error, image))


def get_random_image(path):
    """Return a random image from a local folder."""    # TODO: change to return 1+ images
    try:
        images = [os.path.join(path, img) for img in os.listdir(path) if img.endswith((".jpg", ".png"))]
        selected_img = random.choice(images)
    except (FileNotFoundError, IndexError) as exc:
        sys.exit(exc)
    else:
        return selected_img


def main():
    image = get_random_image(FOLDER_PATH)
    time.sleep(random.randint(5, 60))
    post_tweet(image)


if __name__ == "__main__":
    main()
