import tweepy

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents)
bot.remove_command('help')

@bot.command()
async def tweets(ctx, username):
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=username, count=5)
    tweet_texts = [tweet.text for tweet in tweets]
    await ctx.send(f"Les derniers tweets de {username} :\n" + "\n".join(tweet_texts))


bot.run('BOT TOKEN')
