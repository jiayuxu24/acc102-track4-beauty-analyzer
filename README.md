# Beauty Ingredients & User Preference Analyzer
ACC102 Track 4 - FMCG Beauty Analysis

## 🔗 1. Product Link
[View the Streamlit App](https://acc102-track4-beauty-analyzer-nmhksnct4zvu9gmchqc9hw.streamlit.app/)

## 1. Problem & User
This project analyzes popular beauty ingredients, user ratings, and price preferences in the Sephora product catalog.
It aims to identify ingredient trends, price-rating correlations, and category-specific preferences to help users understand market patterns in beauty products.

## 2. Data
- **Source**: Sephora Website Dataset (Kaggle, accessed Apr 2026)
- **Format**: Simulated data based on real Sephora dataset distribution
- **Key Fields**: category, price, rating, ingredients

## 3. Methods (main Python steps)
1. **Data Generation**: Created realistic simulated data based on Sephora's typical ingredient frequencies, price ranges, and rating distributions.
2. **Filtering**: Implemented category, price range, and minimum rating filters to narrow down the dataset.
3. **Analysis**:
    - Ingredient popularity count and bar chart visualization
    - Price vs rating correlation scatter plot
    - Ingredients word cloud
4. **Insights**: Summarized trends in ingredient popularity, price-rating relationships, and category preferences.

## 4. Key Findings
- **Ingredient Trends**: Hyaluronic Acid and Niacinamide are the most common and popular ingredients across skincare products.
- **Price vs Rating**: Mid-range products ($10–$60) tend to have more consistent high ratings, while premium-priced products show greater rating variability.
- **Category Differences**: Skincare products feature the widest variety of ingredients, while fragrances have the most simplified ingredient lists.

## 5. How to Run
1. Install dependencies:
pip install -r requirements.txt
2. Run the Streamlit application:
```bash
streamlit run app.py
## 6. **Limitations & Next Steps**
This version uses simulated data for stable deployment; future versions can integrate the full real dataset.
Additional features could include ingredient recommendation, sentiment analysis, and product matching.
