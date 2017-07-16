import json
import twitter
import feelold

def main():
    twitter_access_token, twitter_access_secret = twitter.read_token_file('keys/feeloldbot')
    twitter_consumer_key, twitter_consumer_secret = twitter.read_token_file('keys/consumer')

    t = twitter.Twitter(
        auth=twitter.OAuth(
            consumer_key=twitter_consumer_key,
            consumer_secret=twitter_consumer_secret,
            token=twitter_access_token,
            token_secret=twitter_access_secret
        )
    )

    message = feelold.get_random_message()

    assert(len(message) < 140)

    t.statuses.update(status=message)

if __name__ == '__main__':
    main()