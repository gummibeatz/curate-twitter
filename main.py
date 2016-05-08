from twitter_client import TwitterAPI



consumer_key = "8mmEGIIT9UOqcNq3l4k3ct32R"
consumer_secret = "axEFlGEDzwix7tlwaOkBmSfWAOYEYcdK5eADXncUsHWeb4u00v"

token_key = "701538848250191872-3ZFf4v4KJuWyACQ1cQTrFakKKKjASE3"
token_secret = "NphMo0nU1b3tQwCH80SF88PYZUjIUFlt3uTOBeHH2JdIW"

twitter = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)
followers = twitter.get_followers("bonobos")["users"]
