# PyDish
Python Recipe Finder using TheMealDB API-  Search and display recipes in a Tkinter window.


PyDish Recipe Scraper
Welcome to PyDish! This app helps you find delicious recipes based on your cravings. Simply enter what you’re in the mood for, and PyDish will fetch recipes from TheMealDB API and display them in a user-friendly interface.

Features
Search Recipes: Enter a dish name and get a list of recipes.
Detailed Recipe Information: View ingredients, instructions, and source links for each recipe.
Beautiful Background: Enjoy a visually appealing background image from Unsplash.

Installation
Clone the repository:
git clone https://github.com/desireeboudreaux/pydish.git
cd pydish

Install the required packages:
pip install requests pillow tkinter

Run the application:
python pydish.py

How It Works
Download Background Image: The app downloads a beautiful background image from Unsplash.
Set Background: The image is set as the background for the Tkinter window.
User Input: Users can enter the name of a dish they are craving.
Fetch Recipes: The app fetches recipes from TheMealDB API based on the user’s input.
Display Results: The app displays the recipes, including title, category, area, ingredients, instructions, and source link.

Code Overview
download_image(url, filename): Downloads an image from a given URL and saves it locally.
set_background(root, image_path): Sets the downloaded image as the background for the Tkinter window.
get_recipes(query): Fetches recipes from TheMealDB API based on the user’s query.
parse_recipes(data): Parses the JSON response from the API and extracts relevant recipe information.
display_results(recipes): Displays the fetched recipes in the Tkinter window.
user_input(): Handles user input, fetches recipes, and displays the results.

Dependencies
requests: For making HTTP requests to download the background image and fetch recipes.
Pillow: For handling and displaying images.
Tkinter: For creating the graphical user interface.

Contributing
Feel free to fork this repository and contribute by submitting pull requests. Any improvements or bug fixes are welcome and appreciated!



