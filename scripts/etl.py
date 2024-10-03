# etl.py
import os
import logging
import pandas as pd
import sqlite3
from spotify_api import SpotifyAPI
from create_db import create_database
from transform_data import transform_data

def extract_spotify_data(client_id, client_secret, user_id):
    spotify_api = SpotifyAPI(client_id, client_secret, user_id)
    
    user_data = spotify_api.get_user_data()
    playlist_data = spotify_api.get_playlists()
    track_data = spotify_api.get_tracks_from_playlists(playlist_data)
    
    return user_data, playlist_data, track_data

def load_data_to_database(user_df, playlist_df, track_df, album_df, artist_df, db_path):
    try:
        conn = sqlite3.connect(db_path)
        user_df.to_sql('user', conn, if_exists='replace', index=False)
        playlist_df.to_sql('playlist', conn, if_exists='replace', index=False)
        track_df.to_sql('track', conn, if_exists='replace', index=False)
        album_df.to_sql('album', conn, if_exists='replace', index=False)
        artist_df.to_sql('artist', conn, if_exists='replace', index=False)
    except sqlite3.Error as e:
        logging.error(f"An error occurred during data insertion: {e}", exc_info=True)

def etl_pipeline():
    try:
        # Set environment variables
        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        user_id = os.getenv('SPOTIFY_USER_ID')
        db_path = os.getenv('DB_PATH', 'spotify_data.db')
        
        # Step 1: Extract
        user_data, playlist_data, track_data = extract_spotify_data(client_id, client_secret, user_id)
        
        # Step 2: Transform
        user_df, playlist_df, track_df, album_df, artist_df = transform_data(track_data, playlist_data, user_data)
        
        # Step 3: Load
        load_data_to_database(user_df, playlist_df, track_df, album_df, artist_df, db_path)
        logging.info("ETL Pipeline completed successfully.")
        
    except Exception as e:
        logging.error(f"An error occurred during ETL Pipeline: {e}", exc_info=True)

if __name__ == '__main__':
    etl_pipeline()
