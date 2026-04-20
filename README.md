# Beauty Ingredients Analyzer
ACC102 Track 4 - FMCG Beauty Analysis

## 1. Problem & User
Analyzes Sephora beauty products to identify ingredient trends, price-rating patterns, and category preferences.

## 2. Data
- Source: Sephora Dataset (Kaggle, Apr 2026)
- Format: Simulated based on real distribution
- Key Fields: category, price, rating, ingredients

## 3. Methods
1. Cleaning: Handle missing & invalid price/rating data.
2. Generation: Create realistic Sephora-like product data.
3. Filtering: Filter by category, price, and rating.
4. Analysis: Charts for ingredients, price vs rating, word cloud.

## 4. Key Findings
- Top ingredients: Hyaluronic Acid & Niacinamide.
- Mid-range products ($10–$60) have stable high ratings.
- Skincare uses the most diverse ingredients.

## 5. How to run
```bash
pip install -r requirements.txt
streamlit run app.py```

## 6. Product link / Demo
View the Streamlit App

## 7. Limitations & next steps
Uses simulated data for stable deployment.
Future: Add real API data & recommendations.
