# Import modules
import requests
import tkinter as tk
from PIL import Image, ImageTk

print("Modules imported")

# Function to download Unsplash background image
def download_image(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        with open(filename, 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")

# Function to set the Unsplash background image onto Tkinter
def set_background(root, image_path):
    try:
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        background_label = tk.Label(root, image=photo)
        background_label.image = photo  # Keep reference to avoid garbage collection
        background_label.place(relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error setting background: {e}")

# Function to fetch recipes from TheMealDB API
def fetch_recipes(query):
    api_key = '1'  # Test API key
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    print(f"Fetching URL: {url}")  # Debugging statement
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        data = response.json()
        return data['meals']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipes: {e}")
        return None

# Function to parse JSON response and extract recipes
def parse_recipes(data):
    if data is None:
        return []
    recipes = []
    for item in data:
        title = item['strMeal']
        link = item['strSource'] if item['strSource'] else f"https://www.themealdb.com/meal/{item['idMeal']}"
        recipes.append({'title': title, 'link': link})
    print(f"Parsed Recipes: {recipes}")  # Debugging statement
    return recipes

# Function to display the results in the Tkinter window
def display_results(recipes):
    # Clear previous results
    for widget in results_frame.winfo_children():
        widget.destroy()
    # Display new results
    if not recipes:
        result_label = tk.Label(results_frame, text="Sorry, I couldn't find that recipe.", font=('Helvetica', 12), bg='black', fg='white')
        result_label.pack()
    else:
        for recipe in recipes:
            result_label = tk.Label(results_frame, text=f"{recipe['title']}: {recipe['link']}", font=('Helvetica', 12), bg='black', fg='white')
            result_label.pack()

# Function for user input
def user_input():
    user_input = entry.get()
    data = fetch_recipes(user_input)
    recipes = parse_recipes(data)
    display_results(recipes)

# Download background image from Unsplash
image_url = "https://plus.unsplash.com/premium_photo-1673108852141-e8c3c22a4a22?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
download_image(image_url, "background.jpg")

# Create the Tkinter window
root = tk.Tk()
root.title("PyDish")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the size of the Tkinter window to the screen size
root.geometry(f"{screen_width}x{screen_height}")

# Set the background image
set_background(root, "background.jpg")

# Create user interface
frame = tk.Frame(root, bg='black')
frame.pack(pady=20)

label = tk.Label(frame, text="What are you craving?", font=('Helvetica', 16), fg='black', bg='#479254')
label.pack(pady=10)

# Create an opaque entry widget with a border
entry = tk.Entry(frame, font=('Helvetica', 14), highlightbackground='#479254', highlightthickness=2)
entry.pack(pady=10)

button = tk.Button(frame, text="Search", font=('Helvetica', 14), bg='#479254', fg='white', command=user_input)
button.pack(pady=10)

# Create results display
results_frame = tk.Frame(root, bg='black')
results_frame.pack(pady=20)

# Run Tkinter loop
root.mainloop()
