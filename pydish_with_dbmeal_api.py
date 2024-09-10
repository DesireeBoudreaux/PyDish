# Import modules
import requests
import tkinter as tk
from PIL import Image, ImageTk


print("Modules imported")

# Download Unsplash background image
"""Downloads an image from Unsplash for Tkinter background"""
def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

# Set the Unsplash background image onto Tkinter
"""Sets the background in the Tkinte window"""
def set_background(root, image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=photo)
    background_label.image = photo
    background_label.place(relwidth=1, relheight=1)

# Get recipes from TheMealDB API
"""Fetches recipes from TheMealDB API"""
def get_recipes(query):
    api_key = '1'  
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    print(f"Getting URL: {url}")  
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")  
    if response.status_code == 200:
        data = response.json()
        return data['meals']
    else:
        print("Failed to retrieve the data.")
        return None

# Parse JSON response & extract recipes
"""Parses the recipe"""
def parse_recipes(data):
    if data is None:
        return []
    recipes = []
    for item in data:
        title = item['strMeal']
        category = item['strCategory']
        area = item['strArea']
        instructions = item['strInstructions']
        ingredients = []
        for i in range(1, 21):
            ingredient = item[f'strIngredient{i}']
            measure = item[f'strMeasure{i}']
            if ingredient:
                ingredients.append(f"{ingredient} - {measure}")
        link = item['strSource'] if item['strSource'] else f"https://www.themealdb.com/meal/{item['idMeal']}"
        recipes.append({
            'title': title,
            'category': category,
            'area': area,
            'instructions': instructions,
            'ingredients': ingredients,
            'link': link
        })
    # Debugging statements
    print(f"Parsed Recipes: {recipes}")  
    return recipes

# Display the results in the Tkinter window
def display_results(recipes):
    """Displays recipes in the Tkinter window"""
    for widget in results_frame.winfo_children():
        widget.destroy()
    # Display results
    if not recipes:
        result_label = tk.Label(results_frame, text="Sorry I couldn't find that recipe.", font=('Helvetica', 12), bg='black', fg='white')
        result_label.pack()
    else:
        for recipe in recipes:
            title_label = tk.Label(results_frame, text=f"Title: {recipe['title']}", font=('Helvetica', 14, 'bold'), bg='black', fg='white')
            title_label.pack()
            category_label = tk.Label(results_frame, text=f"Category: {recipe['category']}", font=('Helvetica', 12), bg='black', fg='white')
            category_label.pack()
            area_label = tk.Label(results_frame, text=f"Area: {recipe['area']}", font=('Helvetica', 12), bg='black', fg='white')
            area_label.pack()
            ingredients_label = tk.Label(results_frame, text="Ingredients:", font=('Helvetica', 12, 'bold'), bg='black', fg='white')
            ingredients_label.pack()
            for ingredient in recipe['ingredients']:
                ingredient_label = tk.Label(results_frame, text=ingredient, font=('Helvetica', 12), bg='black', fg='white')
                ingredient_label.pack()
            instructions_label = tk.Label(results_frame, text="Instructions:", font=('Helvetica', 12, 'bold'), bg='black', fg='white')
            instructions_label.pack()
            instructions_text = tk.Text(results_frame, wrap='word', font=('Helvetica', 12), bg='black', fg='white', height=10, width=50)
            instructions_text.insert('1.0', recipe['instructions'])
            instructions_text.config(state='disabled')
            instructions_text.pack()
            link_label = tk.Label(results_frame, text=f"Source: {recipe['link']}", font=('Helvetica', 12), bg='black', fg='white')
            link_label.pack()
            separator = tk.Label(results_frame, text="-"*50, font=('Helvetica', 12), bg='black', fg='white')
            separator.pack()

# User input
def user_input():
    """Asks the user for Input based on what they are craving & fetches the recipe from TheMealDB API"""
    user_input = entry.get()
    data = get_recipes(user_input)
    recipes = parse_recipes(data)
    display_results(recipes)

# Downloading background from Unsplash
image_url = "https://plus.unsplash.com/premium_photo-1673108852141-e8c3c22a4a22?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
download_image(image_url, "background.jpg")

# Create the Tkinter window
root = tk.Tk()
root.title("PyDish")

# Get screen width & height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set Tkinter window to the screen size
root.geometry(f"{screen_width}x{screen_height}")

# Set background to Unsplash photo
set_background(root, "background.jpg")

# Create the interface
frame = tk.Frame(root, bg='black')
frame.pack(pady=20)

label = tk.Label(frame, text="What are you craving?", font=('Helvetica', 16), fg='black', bg='#479254')
label.pack(pady=10)

# Create the widget
entry = tk.Entry(frame, font=('Helvetica', 14), highlightbackground='black', highlightthickness=2)
entry.pack(pady=10)

button = tk.Button(frame, text="Search", font=('Helvetica', 14), bg='#479254', fg='black', command=user_input)
button.pack(pady=10)

# Create display
results_frame = tk.Frame(root, bg='black')
results_frame.pack(pady=20)

# Run Tkinter
root.mainloop()
