# Project 2 – Citizen Feedback Sentiment Analyser

**Portfolio Part b – Semi-Complex AI Project**  
**Author:** [Your Name]  
**Date:** April 2026  
**University:** University of Bradford  

---

## What this project does

This project uses a Python NLP (Natural Language Processing) library called **TextBlob** to automatically analyse the tone of citizen feedback and questions. It reads each sentence and labels it as:

- **POSITIVE** — the citizen is happy or satisfied
- **NEGATIVE** — the citizen is unhappy or frustrated
- **NEUTRAL** — the citizen is asking a question with no strong feeling

This is called **sentiment analysis** and is a real technique used in AI and data analysis jobs to understand large amounts of text automatically.

---

## Example output

```
============================================================
  Analysing: Sample citizen feedback
============================================================
Sentence                                      Result     Score
------------------------------------------------------------
I am very happy with how quickly the counc... POSITIVE   0.69
The bin collection service is absolutely t... NEGATIVE  -0.44
How do I register to vote?                    NEUTRAL    0.0
I have been waiting 3 months for a respon...  NEGATIVE  -0.33
The new recycling centre is excellent and ... POSITIVE   0.85
------------------------------------------------------------
  Total sentences analysed : 12
  Positive                 : 5  (42%)
  Negative                 : 4  (33%)
  Neutral                  : 3  (25%)
```

---

## How to run it

**Step 1 — Install TextBlob** (only needed once)

Open your terminal or command prompt and type:
```
pip install textblob
```

**Step 2 — Run the script**
```
python sentiment_analyser.py
```

**Optional:** Place the `citizen_qa_dataset.csv` file from my portfolio repo in the same folder to also analyse those questions automatically.

---

## How it works

TextBlob gives each sentence a **polarity score** between -1.0 and 1.0:

| Score range | Meaning | Label |
|---|---|---|
| Above 0.1 | Positive feeling | POSITIVE |
| Between -0.1 and 0.1 | No strong feeling | NEUTRAL |
| Below -0.1 | Negative feeling | NEGATIVE |

The library has been trained on large amounts of English text and has learnt which words carry positive or negative meaning. For example "excellent" scores highly positive, "terrible" scores highly negative, and "how do I" scores neutral.

---

## What I learnt from this project

This project introduced me to **NLP — Natural Language Processing**, which is the branch of AI that deals with understanding human language.

Key things I learnt:

- **What sentiment analysis is** and why businesses and councils use it (e.g. to automatically scan thousands of complaint emails and spot patterns)
- **How to use a Python library** — I did not build the AI myself, but I learnt how to import a library, call its functions, and interpret its output. This is exactly what data analysts do in real jobs.
- **What polarity scores mean** — a number between -1 and 1 representing how positive or negative a piece of text is
- **The limitation of this approach** — TextBlob works well for clear positive/negative language but struggles with sarcasm, slang or very short sentences. More advanced models like BERT handle this better, which I explore in Project 3.

---

## Connection to group project

My group is building a conversational AI agent for citizen support. Sentiment analysis is a useful tool for understanding how citizens feel about council services. In a real deployment, this kind of analysis could be run on all incoming messages to automatically flag angry or urgent requests for priority handling.

---

## Progression across the three projects

| Project | Type | What it uses |
|---|---|---|
| Project 1 – Keyword chatbot | Simple | Plain Python logic, no AI library |
| **Project 2 – Sentiment analyser** | **Semi-complex** | **TextBlob NLP library** |
| Project 3 – AI API chatbot | Complex | Real AI model via API |

---

## Files in this repository

| File | Description |
|---|---|
| `sentiment_analyser.py` | Main Python script |
| `README.md` | This file |
