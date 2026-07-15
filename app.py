"""
Day 5 - Movie Recommender (Flask Web Version)
Core Skills: Data handling, pandas, Flask (web framework)
Author: Manoj S

This is the same genre-matching recommender logic as the CLI version,
now served as a web page using Flask so it runs entirely in Python
(no separate JavaScript logic needed).
"""

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# ----- Load dataset once when the app starts -----
def load_movies(csv_path="movies_combined.csv"):
    df = pd.read_csv(csv_path)
    df["genre_list"] = df["genres"].apply(lambda g: g.split("|"))
    return df


movies_df = load_movies()


def get_all_genres(df):
    """Collect every unique genre available in the dataset."""
    all_genres = set()
    for genres in df["genre_list"]:
        all_genres.update(genres)
    return sorted(all_genres)


def get_all_languages(df):
    if "language" in df.columns:
        return sorted(df["language"].dropna().unique())
    return []


def score_movie(movie_genres, preferred_genres):
    """Score = number of overlapping genres."""
    return len(set(movie_genres) & set(preferred_genres))


def recommend_movies(df, preferred_genres, language_filter=None, sort_by="match"):
    """
    Filter by language (if given), score every movie by genre overlap,
    keep only movies with at least 1 match, then sort.
    """
    filtered = df.copy()

    if language_filter and language_filter != "all":
        filtered = filtered[filtered["language"] == language_filter]

    filtered["match_score"] = filtered["genre_list"].apply(
        lambda genres: score_movie(genres, preferred_genres)
    )

    matched = filtered[filtered["match_score"] > 0]

    if sort_by == "rating":
        matched = matched.sort_values(by="rating", ascending=False)
    elif sort_by == "year":
        matched = matched.sort_values(by="year", ascending=False)
    else:  # default: best match
        matched = matched.sort_values(
            by=["match_score", "rating"], ascending=[False, False]
        )

    return matched.to_dict(orient="records")


@app.route("/", methods=["GET", "POST"])
def home():
    all_genres = get_all_genres(movies_df)
    all_languages = get_all_languages(movies_df)

    results = []
    selected_genres = []
    selected_language = "all"
    sort_by = "match"

    if request.method == "POST":
        selected_genres = request.form.getlist("genres")
        selected_language = request.form.get("language", "all")
        sort_by = request.form.get("sort_by", "match")

        if selected_genres:
            results = recommend_movies(
                movies_df, selected_genres, selected_language, sort_by
            )

    return render_template(
        "index.html",
        all_genres=all_genres,
        all_languages=all_languages,
        results=results,
        selected_genres=selected_genres,
        selected_language=selected_language,
        sort_by=sort_by,
    )


if __name__ == "__main__":
    app.run(debug=True)