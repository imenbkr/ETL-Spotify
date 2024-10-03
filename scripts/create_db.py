# create_db.py
import sqlite3
import logging

def create_database(db_path='spotify_data.db'):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            # Table Definitions
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user (
                    id TEXT PRIMARY KEY,
                    name TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS artist (
                    id TEXT PRIMARY KEY,
                    name TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS album (
                    id TEXT PRIMARY KEY,
                    name TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS playlist (
                    id TEXT PRIMARY KEY,
                    user_id TEXT,
                    name TEXT,
                    FOREIGN KEY(user_id) REFERENCES user(id)
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS track (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    playlist_id TEXT,
                    artist_id TEXT,
                    album_id TEXT,
                    FOREIGN KEY(playlist_id) REFERENCES playlist(id),
                    FOREIGN KEY(artist_id) REFERENCES artist(id),
                    FOREIGN KEY(album_id) REFERENCES album(id)
                )
            ''')

            conn.commit()
            cursor.close()

    except sqlite3.Error as e:
        logging.error(f"Error creating database: {e}", exc_info=True)

if __name__ == '__main__':
    create_database()
