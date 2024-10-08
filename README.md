# 🍽️ PyDish Recipe Scraper

Welcome to **PyDish**! This app is your culinary companion, helping you discover delicious recipes based on your cravings. Just tell us what you’re in the mood for, and PyDish will fetch mouth-watering recipes from TheMealDB API and display them in a user-friendly interface.🍴

## ✨ Features
- **🔍 Search Recipes**: Enter a dish name and get a delicious recipe.
- **📋 Detailed Recipe Information**: View ingredients, instructions, and source links for each recipe.
- **🌄 Beautiful Background**: Enjoy a visually appealing background image from Unsplash.
  
## 🎥 PyDish in Action:
- https://github.com/user-attachments/assets/d057b6a8-54d3-4448-8ebd-8b74681dbb82

## 🚀 Installation
1. **Clone the repository**:
    git clone https://github.com/desireeboudreaux/pydish.git
cd pydish

3. **Install the required packages**:
    pip install requests pillow
    
   
   
5. **Run the application**:
    pydish_with_dbmeal_api.py

## 🛠️ How It Works
1. **Download Background Image**: The app downloads a delicious looking background image from Unsplash.
2. **Set Background**: The image is set as the backdrop for the Tkinter window.
3. **User Input**: Enter the name of a dish you’re craving.
4. **Fetch Recipes**: The app fetches recipes from TheMealDB API based on your input.
5. **Display Results**: The app will showcase the recipe, including title, category, area, ingredients, instructions, and source link.
   
🔍 Search Rules and Examples
Search Rules:
Enter the name of a dish or ingredient.
Use specific names for better results (e.g., “Chicken Curry” instead of just “Chicken”).
If multiple recipes are available, scroll down to see all results.
Examples:
Example 1: Searching for “Cheesecake”
!Salted Caramel Cheesecake
Example 2: Searching for “Curry”
!Thai Green Curry
!Katsu Chicken Curry
!Nutty Chicken Curry

## 🧑‍💻 Code Overview
- `download_image(url, filename)`: Downloads an image from a given URL and saves it locally.
- `set_background(root, image_path)`: Sets the downloaded image as the background for the Tkinter window.
- `get_recipes(query)`: Fetches recipes from TheMealDB API based on the user’s query.
- `parse_recipes(data)`: Parses the JSON response from the API and extracts relevant recipe information.
- `display_results(recipes)`: Displays the fetched recipes in the Tkinter window.
- `user_input()`: Handles user input, fetches recipes, and displays the results.

## 📦 Dependencies
- `requests`: For making HTTP requests to download the background image and fetch recipes.
- `Pillow`: For handling and displaying images.
- `Tkinter`: For creating the graphical user interface.
  
📝 Platform Note
- Tested on: Windows

## 🤝 Contributing
Feel free to fork this repository and contribute by submitting pull requests. Any improvements or bug fixes are welcome and appreciated!

 
Happy cooking with PyDish! 🍪
