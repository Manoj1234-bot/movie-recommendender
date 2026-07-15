# 🎬 Movie Recommender System

A **Movie Recommender System** built using **Python, Flask, and Pandas** that suggests movies based on the user's preferred genres. The application supports **genre-based recommendations**, **language filtering**, and **sorting by match score, rating, or release year**. It provides a simple and interactive web interface for discovering movies from both **English** and **Kannada** movie collections.

## 🌟 Features

* 🎭 Recommend movies based on selected genres
* 🌍 Filter recommendations by language
* ⭐ Sort movies by:

  * Best Genre Match
  * Highest Rating
  * Latest Release Year
* 📊 Displays movie details:

  * Movie Title
  * Genres
  * Rating
  * Release Year
  * Language
* ⚡ Fast recommendation using Pandas
* 🖥️ Simple and responsive Flask web interface
* 🎬 Supports both English and Kannada movies

## 🛠️ Technologies Used

* Python 3
* Flask
* Pandas
* HTML5
* CSS3

## 📁 Project Structure

```text
movie-recommender/
│
├── app.py
├── requirements.txt
├── movies_combined.csv
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js (optional)
│


## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Manoj1234-bot/movie-recommender.git
```

### 2. Navigate to the project

```bash
cd movie-recommender
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

### 5. Open in your browser

```
http://127.0.0.1:5000
```

## 📊 Dataset

The application uses a custom movie dataset (`movies_combined.csv`) containing information such as:

* Movie Title
* Genres
* IMDb Rating
* Release Year
* Language

## ⚙️ How It Works

1. Loads the movie dataset using **Pandas**.
2. Splits movie genres into individual genre lists.
3. Allows users to select one or more preferred genres.
4. Filters movies based on the selected language (optional).
5. Calculates a **match score** by comparing user-selected genres with each movie's genres.
6. Recommends only movies with at least one matching genre.
7. Sorts the recommendations by:

   * Best Match
   * Rating
   * Release Year
8. Displays the recommended movies on the web page.

## 📚 What I Learned

* Learned how to build a web application using **Flask**, process datasets with **Pandas**, and implement a simple content-based movie recommendation algorithm.
* Improved my understanding of CSV data handling, filtering, sorting, scoring logic, template rendering, and creating dynamic web applications with Python.

## 🚀 Future Improvements

* 🔍 Movie search by title
* 🎥 Official trailer integration (YouTube)
* ❤️ Favorite movie list
* 👤 User login and profiles
* ⭐ Personalized recommendations
* 🎬 Movie posters using TMDb API
* 📱 Fully responsive UI
* 🤖 AI-based recommendation engine

## 👨‍💻 Author

**Manoj S**

---

⭐ If you like this project, consider giving it a **Star** on GitHub. Feedback and contributions are always welcome!
