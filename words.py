"""
Sentiment vocabulary module.
Contains lists of positive and negative words for sentiment analysis.
"""

# List of positive sentiment words
POSITIVE_WORDS = [
    "happy", "amazing", "great", "excellent", "wonderful",
    "fantastic", "awesome", "brilliant", "love", "enjoy"
]

# List of negative sentiment words
NEGATIVE_WORDS = [
    "bad", "terrible", "sad", "awful", "horrible",
    "hate", "disappointing", "poor", "annoying", "frustrating"
]

# Words that negate the sentiment of following words
NEGATION_WORDS = ["dont", "not", "never"]
