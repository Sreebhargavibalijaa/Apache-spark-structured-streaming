# Apache-spark-structured-streaming

Spark sql framework component is used for structured and semi structured data processing.![Screen Shot 2023-01-13 at 11 11 19 PM](https://user-images.githubusercontent.com/115974245/212460634-aba1d3e9-118a-41e2-a00e-e571651d26b3.png)


We use Twitter data since Twitter provides an API for developers that is easy to access and presented an end-to-end architecture on how to stream data from Twitter, clean it, and apply a simple sentiment analysis model to detect the polarity and subjectivity of each tweet.

Code detailed explanation:-

• Initially authentication operations and keys were obtained from twitter api and Python module "Tweepy"
• A later stream listener named "Twitter data" was created to generate data for the kafka topic "Global warming". This new method was included in Twitter data object using Affinn module for calculating the sentimental value of tweet
• Further the streaming data is converted into the structured data and placed in sql table named "SQldata" which has two columns "text" and "senti_val"
• Pyspart.sql functions are used to calculate the average of sentimental values of the senti_val column, function fun is added to categorize the tweet to positive, negative or neutral based on the score.
