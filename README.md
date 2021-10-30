# tweetdelete

Delete tweets, retweets and likes of your Twitter's account


## Features

- Delete tweets and retweets
- Delete favs



## Requeriments

Install tweetpy library.

```bash
  pip install tweetpy
```

To access to your twitter data throught the API you need to register a twitter application with the account we'll use. When created, you will recive the consumer keys and access keys.
You can register your application here:
 https://developer.twitter.com/en/portal/projects-and-apps
## Usage

Just run the main.py giving your twitter's username (without @) as a parameter.

```bash
  python main.py potus
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`TWITTER_CONSUMER_KEY`

`TWITTER_CONSUMER_SECRET`

`TWITTER_ACCESS_TOKEN`

`TWITTER_ACCESS_SECRET_TOKEN`

