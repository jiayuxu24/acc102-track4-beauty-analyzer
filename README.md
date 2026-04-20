# Beauty Ingredients Analyzer
ACC102 Track 4 - FMCG Beauty Analysis

# 1. Problem & User
Analyzes Sephora beauty products to identify ingredient trends, price-rating patterns, and category preferences.

# 2. Data
- Source: Sephora Dataset (Kaggle, Apr 2026)
- Format: Simulated based on real distribution
- Key Fields: category, price, rating, ingredients

# 3. Methods
1. Cleaning: Handle missing & invalid price/rating data.
2. Generation: Create realistic Sephora-like product data.
3. Filtering: Filter by category, price, and rating.
4. Analysis: Charts for ingredients, price vs rating, word cloud.

# 4. Key Findings
- Top ingredients: Hyaluronic Acid & Niacinamide.
- Mid-range products ($10–$60) have stable high ratings.
- Skincare uses the most diverse ingredients.

# 5. How to Run
1. Install dependencies:
pip install -r requirements.txt

2. Launch the Streamlit app:
streamlit run app.py

# 6. Product Link / Demo

View the Streamlit App:  
[Insert your app link here, e.g., https://your-app.streamlit.app]

# 7. Limitations & Next Steps

- **Limitation:** Uses simulated data for stable deployment (no real-time API data).  
- **Next Steps:**  
- Integrate real API data from skincare/product databases.  
- Add personalized recommendation engine based on user preferences and skin type.
