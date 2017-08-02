# feelold
A twitter bot for feeling old.


# Setup

To use, you must provide necessary Twitter API credentials.

To authenticate to the API,
create a Twitter application, and generate
a `twitter_consumer_key` and a `twitter_consumer_secret`.
Save these on separate lines in a file at `keys/consumer`.

To authenticate for a specific twitter account,
include a `twitter_access_token` and a `twitter_access_secret` on separate lines in a file at `keys/feeloldbot`.
The account will need to be authenticated to your Twitter application.

`tweet.py` then accesses these in `main()`:

    twitter_access_token, twitter_access_secret = twitter.read_token_file('keys/feeloldbot')
    twitter_consumer_key, twitter_consumer_secret = twitter.read_token_file('keys/consumer')
