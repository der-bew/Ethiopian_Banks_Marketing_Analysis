from google_play_scraper import reviews, Sort
import json

# Define the app ID for the Apollo app
app_id = 'com.boa.apollo'  # Replace with the actual app ID if different

# Function to scrape reviews with pagination
def scrape_reviews(app_id, pages=5):
    all_reviews = []
    continuation_token = None
    for page in range(pages):
        result, continuation_token = reviews(
            app_id,
            lang='en',  # Language of reviews
            country='us',  # Country of reviews
            sort=Sort.NEWEST,  # Sort by newest first
            count=100,  # Number of reviews to scrape per page
            continuation_token=continuation_token
        )
        all_reviews.extend(result)
        if not continuation_token:
            break

    return all_reviews

# Scrape the reviews
reviews_data = scrape_reviews(app_id, pages=200)  # Adjust pages if needed

# Extract relevant data
formatted_reviews = []
for review in reviews_data:
    review_data = {
        'reviewId': review['reviewId'],
        'userName': review['userName'],
        'userImage': review['userImage'],
        'reviewCreatedVersion': review.get('reviewCreatedVersion', None),
        'at': review['at'],
        'replyContent': review.get('replyContent', None),
        'repliedAt': review.get('repliedAt', None),
        'appVersion': review.get('appVersion', None),
        'score': review['score'],
        'comments': review['content']
    }
    formatted_reviews.append(review_data)

# Save the JSON data to a file
with open('reviews_app.json', 'w', encoding='utf-8') as f:
    json.dump(formatted_reviews, f, indent=4, ensure_ascii=False, default=str)

