"""
User interface for the Sentiment Analysis System.
Handles user input and displays analysis results.
"""

from sentiment import analyze_sentiment


def main():
    """Run the sentiment analysis application."""
    print("\n" + "=" * 50)
    print("  SENTIMENT ANALYSIS SYSTEM")
    print("=" * 50 + "\n")

    user_input = input("Enter a sentence to analyze:\n> ")

    print("\n" + "-" * 50)
    print(f"Your input: {user_input}")
    print("-" * 50 + "\n")

    result = analyze_sentiment(user_input)

    # Display results
    print(f"Sentiment: {result['sentiment']}")
    print(f"Positive words found: {result['positive_count']}")
    print(f"Negative words found: {result['negative_count']}")

    if result["positive_matches"]:
        print(f"Positive matches: {', '.join(result['positive_matches'])}")

    if result["negative_matches"]:
        print(f"Negative matches: {', '.join(result['negative_matches'])}")

    print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
