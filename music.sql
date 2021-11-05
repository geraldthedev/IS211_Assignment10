CREATE TABLE artist (
    id INT PRIMARY KEY,
    artist_name TEXT
);

CREATE TABLE albums (
    album_number INT,
    album_name TEXT
);

CREATE TABLE songs(
    song_name TEXT,
    FOREIGN KEY(album_name) REFERENCES albums(albums_name),
    track_number INT,
    track_length INT
);
