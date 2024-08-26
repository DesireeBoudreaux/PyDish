# 🍽️ PyDish Recipe Scraper

Welcome to **PyDish**! This app is your culinary companion, helping you discover delicious recipes based on your cravings. Just tell us what you’re in the mood for, and PyDish will fetch mouth-watering recipes from TheMealDB API and display them in a user-friendly interface. Bon appétit! 🍴

## ✨ Features
- **🔍 Search Recipes**: Enter a dish name and get a list of scrumptious recipes.
- **📋 Detailed Recipe Information**: View ingredients, instructions, and source links for each recipe.
- **🌄 Beautiful Background**: Enjoy a visually appealing background image from Unsplash.

## 🚀 Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/desireeboudreaux/pydish.git
    cd pydish
    ```
2. **Install the required packages**:
    ```bash
    pip install requests pillow tkinter
    ```
3. **Run the application**:
    ```bash
    python pydish.py
    ```

## 🛠️ How It Works
1. **Download Background Image**: The app downloads a stunning background image from Unsplash.
2. **Set Background**: The image is set as the backdrop for the Tkinter window.
3. **User Input**: Enter the name of a dish you’re craving.
4. **Fetch Recipes**: The app fetches recipes from TheMealDB API based on your input.
5. **Display Results**: The app showcases the recipes, including title, category, area, ingredients, instructions, and source link.

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

## 🤝 Contributing
Feel free to fork this repository and contribute by submitting pull requests. Any improvements or bug fixes are welcome and appreciated!

---

Happy cooking with PyDish! 🍲
