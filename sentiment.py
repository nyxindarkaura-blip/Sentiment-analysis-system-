"""
Sentiment analysis engine.
Provides functions to analyze the emotional tone of text.
"""

import string
from words import POSITIVE_WORDS, NEGATIVE_WORDS, NEGATION_WORDS


def analyze_sentiment(sentence):
    """
    Analyze the sentiment of a given sentence.

    Args:
        sentence (str): The input text to analyze.

    Returns:
        dict: Contains sentiment result with counts and matched words.
    """
    # Clean the sentence: lowercase and remove punctuation
    cleaned = sentence.lower()
    for char in string.punctuation:
        cleaned = cleaned.replace(char, "")

    words = cleaned.split()

    positive_count = 0
    negative_count = 0
    positive_matches = []
    negative_matches = []

    # Scan each word with context for negation
    for i, word in enumerate(words):
        if word in POSITIVE_WORDS:
            # Check if previous word is a negation
            if i > 0 and words[i - 1] in NEGATION_WORDS:
                negative_count += 1
                negative_matches.append(word)
            else:
                positive_count += 1
                positive_matches.append(word)

        elif word in NEGATIVE_WORDS:
            negative_count += 1
            negative_matches.append(word)

    # Determine overall sentiment
    if positive_count > negative_count:
        sentiment = "Positive 😊"
    elif negative_count > positive_count:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😌"

    return {
        "sentiment": sentiment,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "positive_matches": positive_matches,
        "negative_matches": negative_matches
    }
