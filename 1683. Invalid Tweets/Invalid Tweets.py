import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    result = tweets[tweets['content'].str.len()>15][['tweet_id']]
    return result
