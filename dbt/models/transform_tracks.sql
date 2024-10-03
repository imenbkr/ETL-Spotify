-- transform_tracks.sql

WITH cleaned_tracks AS (
    SELECT
        track_id AS id,
        track_name AS name,
        playlist_id,
        artist_id,
        album_id
    FROM {{ ref('raw_tracks') }}
    WHERE track_name IS NOT NULL
),

aggregated_tracks AS (
    SELECT
        artist_id,
        album_id,
        COUNT(*) AS track_count,
        AVG(track_duration_ms) AS avg_duration_ms
    FROM cleaned_tracks
    GROUP BY artist_id, album_id
)

SELECT * FROM aggregated_tracks;
