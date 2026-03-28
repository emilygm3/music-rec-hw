
import pandas as pd
import matplotlib.pyplot as plt
import random

FILE = "spotify.csv"

df = pd.read_csv(FILE)

# for col in df.columns:
#     print(f"\n--- {col} ---")
#     print(df[col].value_counts())
#
#
# df_small = df[df["track_genre"].isin(["garage", "alt-rock", "alternative", "piano", "rock"])]


# # Filter for Regina Spektor and The Strokes
df_regina = df[df["artists"].isin(["Regina Spektor"])]
df_thisisit = df[df["album_name"].isin(["Is This It"])]


# print(df_small.count())

# col = "track_genre"
# for col in df_regina.columns:
#     print(f"\n--- {col} ---")
#     print(df_regina[col].value_counts())
#
# for col in df_thisisit.columns:
#     print(f"\n--- {col} ---")
#     print(df_thisisit[col].value_counts())

df_genre = df[df["track_genre"].isin([])]


regina_genres = df[df["artists"] == "Regina Spektor"]["track_genre"].unique()
strokes_genres = df[df["album_name"] == "Is This It"]["track_genre"].unique()

# Combine into one set of genres
target_genres = set(regina_genres) | set(strokes_genres)

# Filter full df to only those genres, then sample
df_genre = df[df["track_genre"].isin(target_genres)]

print(df_genre)

df.to_csv("genre_3000.csv", index=False)








# continuous_cols = [
#     "popularity", "duration_ms", "danceability", "energy", "key",
#     "loudness", "mode", "speechiness", "acousticness",
#     "instrumentalness", "liveness", "valence", "tempo"
# ]
#
# fig, axes = plt.subplots(4, 4, figsize=(16, 12))
# axes = axes.flatten()
#
# for i, col in enumerate(continuous_cols):
#     axes[i].hist(df_small[col], bins=15, edgecolor="black", alpha=0.7)
#     axes[i].plot(
#         sorted(df_small[col]),
#         range(len(df_small[col])),
#         color="red", linewidth=1.5
#     )
#     axes[i].set_title(col)
#     axes[i].set_xlabel("Value")
#     axes[i].set_ylabel("Count")
#
# # Hide unused subplots
# for j in range(len(continuous_cols), len(axes)):
#     axes[j].set_visible(False)
#
# plt.suptitle("Regina Spektor & The Strokes — Feature Distributions", fontsize=14, y=1.02)
# plt.tight_layout()
# plt.savefig("distributions.png", bbox_inches="tight")
# plt.show()
