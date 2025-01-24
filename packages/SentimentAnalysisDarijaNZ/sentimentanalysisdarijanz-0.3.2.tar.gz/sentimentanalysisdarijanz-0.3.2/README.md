
# SentimentAnalysisDarijaNZ

**SentimentAnalysisDarijaNZ** is a modular Python library designed for text processing in Moroccan Darija (Arabic dialect). The library provides tools for similarity calculation, filtering, and sentiment analysis.

## Key Features

### 1. **Similarity Calculation**
This module includes advanced similarity measures tailored for Moroccan Darija. It provides functions to compute similarity scores between words or phrases while handling linguistic nuances such as:
- **Levenshtein Similarity:** Accounts for minor variations in spelling.
- **Phonetic Similarity:** Matches words based on their phonetic resemblance.
- **Sequence Similarity:** Uses sequence matching to evaluate structural similarity.

Example:
```python
from SentimentAnalysisDarijaNZ import similarity
similarity_score = similarity.levenshtein_similarity("makla", "maakla")
print(similarity_score)
```

### 2. **Filtering**
This module identifies and filters text based on specific brands, quality indicators, or prices. It also includes spam detection tailored for Moroccan Darija.

**Spam Filtering Example:**
```python
from SentimentAnalysisDarijaNZ import filtering
positive_spam, neutral_phrases = filtering.spam_analysis(["Check this link www.fake.com", "Free money!"], spam_dict)
print(positive_spam)
```

**Brand Filtering Example:**
```python
filtered, not_filtered = filtering.filterbrand([["laptop of good quality"]], "quality")
print(filtered)
```

### 3. **Sentiment Analysis**
Detects positive and negative sentiments in Darija text, accounting for nuances like negations and intensifiers.

Example:
```python
from SentimentAnalysisDarijaNZ import sentiment
positive, negative, neutral = sentiment.sentiment_analysis_darija(["The product is amazing!", "Terrible quality"])
print(positive)
```

## Installation

Install the library via pip:
```bash
pip install SentimentAnalysisDarijaNZ
```

## Usage

After installation, import the necessary modules:
```python
from SentimentAnalysisDarijaNZ import similarity, filtering, sentiment
```

## License

This project is licensed under the Apache License 2.0.



## Licence

Ce projet est sous licence MIT. Veuillez consulter le fichier `LICENSE` pour plus d'informations.

## Auteur
  **Nawfal BENHAMDANE**  
   - Elève-Ingénieur à l'Ecole Centrale Casablanca
  **Zaynab RAOUNAK**  
   - Elève-Ingénieur à l'Ecole Centrale Casablanca
  **Hamza Laraisse**  
   - Elève-Ingénieur à l'Ecole Centrale Casablanca
