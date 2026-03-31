
import pandas as pd

FILE = "spotify.csv"

# This file creates a song with 2000 songs, including all 55 songs by Regina Spektor
# or The Strokes. The rest are randomly sampled from the rest of the Spotify CSV. 

# reading the full 114k line CSV into a DataFrame
df = pd.read_csv(FILE)

# DataFrame of only Regina or The Strokes
df_only_regina_strokes = df[df['artists'].isin(['Regina Spektor', 'The Strokes'])]
# DataFrame with NO Regina or The Strokes
df_no_regina_strokes = df[~df['artists'].isin(['Regina Spektor', 'The Strokes'])]

# We knew there were 55 songs by Regina and the Strokes combined since we filtered
# the original CSV file for those artists when we first downloaded it.
 
# randomly choosing 1945 songs from the DataFrame with no Regina or The Strokes
base_random_2000 = df_no_regina_strokes.sample(n=1945, random_state=42)
# combining the 1945 random songs with the 55 Regina or Strokes songs
random_2000_regina_strokes = pd.concat([df_only_regina_strokes, base_random_2000], ignore_index=True)
# exporting CSV
random_2000_regina_strokes.to_csv("random_2000_regina_strokes.csv", index=False)