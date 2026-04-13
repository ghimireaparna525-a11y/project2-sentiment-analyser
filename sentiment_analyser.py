# ============================================================
# Citizen Feedback Sentiment Analyser
# Project 2  – Portfolio Part b
# Author: Aparna Ghimire
# Date: Feb 2026
# Description: Uses the TextBlob NLP library to automatically
#              analyse whether citizen questions and feedback
#              are positive, negative or neutral in tone.
# ============================================================

# --- Step 1: Import the libraries we need ---
# TextBlob is a free NLP (Natural Language Processing) library.
# It does the AI analysis for us.
# csv is a built-in Python library for reading CSV files.

from textblob import TextBlob
import csv

# --- Step 2: Define our sample citizen sentences ---
# These are example pieces of feedback a citizen might write.
# In a real project, this would come from a live database.
# We also load sentences from our dataset CSV file.

sample_feedback = [
    "I am very happy with how quickly the council fixed the pothole.",
    "The bin collection service is absolutely terrible and never on time.",
    "How do I register to vote?",
    "I have been waiting 3 months for a response and nobody has helped me.",
    "The new recycling centre is excellent and very easy to use.",
    "My parking permit application was rejected with no explanation.",
    "The council website is quite useful and easy to navigate.",
    "I am frustrated that my report about fly tipping was ignored.",
    "Can I get information about universal credit please?",
    "The customer service team were very friendly and helpful.",
    "Street lights on my road have been broken for weeks.",
    "I am really satisfied with the housing support I received.",
]

# --- Step 3: Define a function to analyse one sentence ---
# TextBlob gives us a "polarity" score:
#   Polarity > 0  means POSITIVE (e.g. 0.8 = very positive)
#   Polarity = 0  means NEUTRAL  (e.g. 0.0 = no clear feeling)
#   Polarity < 0  means NEGATIVE (e.g. -0.6 = quite negative)

def analyse_sentiment(text):
    # Create a TextBlob object from the text
    blob = TextBlob(text)

    # Get the polarity score (a number between -1.0 and 1.0)
    polarity = blob.sentiment.polarity

    # Decide the label based on the score
    if polarity > 0.1:
        label = "POSITIVE"
    elif polarity < -0.1:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"

    # Return both the label and the score
    return label, round(polarity, 2)


# --- Step 4: Analyse all our sample sentences ---

def analyse_all(sentences, source_label):
    print(f"\n{'='*60}")
    print(f"  Analysing: {source_label}")
    print(f"{'='*60}")
    print(f"{'Sentence':<45} {'Result':<10} {'Score'}")
    print("-" * 60)

    positive_count = 0
    negative_count = 0
    neutral_count  = 0

    for sentence in sentences:
        label, score = analyse_sentiment(sentence)

        # Count each type
        if label == "POSITIVE":
            positive_count += 1
        elif label == "NEGATIVE":
            negative_count += 1
        else:
            neutral_count += 1

        # Print a short version of the sentence (max 44 characters)
        short = sentence[:44] + "..." if len(sentence) > 44 else sentence
        print(f"{short:<45} {label:<10} {score}")

    # Print a summary
    total = len(sentences)
    print("-" * 60)
    print(f"  Total sentences analysed : {total}")
    print(f"  Positive                 : {positive_count} ({round(positive_count/total*100)}%)")
    print(f"  Negative                 : {negative_count} ({round(negative_count/total*100)}%)")
    print(f"  Neutral                  : {neutral_count}  ({round(neutral_count/total*100)}%)")
    print()


# --- Step 5: Try loading sentences from the CSV dataset ---
# This tries to read questions from citizen_qa_dataset.csv
# If the file is not found, it skips this step gracefully.

def load_questions_from_csv(filename):
    questions = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                questions.append(row['question'])
        print(f"\nSuccessfully loaded {len(questions)} questions from {filename}")
    except FileNotFoundError:
        print(f"\nNote: {filename} not found. Skipping CSV analysis.")
    return questions


# --- Step 6: Run everything ---

if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("  Citizen Feedback Sentiment Analyser")
    print("  Using TextBlob NLP Library")
    print("=" * 60)

    # Analyse our hand-written sample feedback
    analyse_all(sample_feedback, "Sample citizen feedback")

    # Try to also analyse questions from the CSV dataset
    csv_questions = load_questions_from_csv("citizen_qa_dataset.csv")
    if csv_questions:
        analyse_all(csv_questions, "Questions from citizen_qa_dataset.csv")

    print("Analysis complete.")
