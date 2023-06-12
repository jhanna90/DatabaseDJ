
# """Models for Playlist app."""

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# def connect_db(app):

#     db.app = app
#     db.init_app(app)
#     db.create_all()

# class Playlist(db.Model):
#     """Playlist."""

#     # ADD THE NECESSARY CODE HERE
#     __tablename__ = "playlists"

#     id = db.Column(db.Integer,
#     primary_key=True, autoincrement=True)
#     name = db.Column(db.String(50),nullable=False)
#     description = db.Column(db.String(100))

#     def __repr__(self):
#         return f"<Playlist name={self.name} description={self.description}>"


# class Song(db.Model):
#     """Song."""

#     # ADD THE NECESSARY CODE HERE
#     __tablename__ = "songs"

#     id = db.Column(db.Integer,
#     primary_key=True, autoincrement=True)
#     title = db.Column(db.String(50),nullable=False)
#     artist = db.Column(db.String(50),nullable=False)

#     album = db.relationship("Playlist", secondary="playlists_songs",backref='songs')

#     def __repr__(self):
#         return f"<Song title={self.title} artist={self.artist} >"


# class PlaylistSong(db.Model):
#     """Mapping of a playlist to a song."""

#     # ADD THE NECESSARY CODE HERE
#     __tablename__ = "playlists_songs"

#     id = db.Column(db.Integer,
#     primary_key=True, autoincrement=True)
#     song_id = db.Column(db.Integer,db.ForeignKey("songs.id"))
#     playlist_id = db.Column(db.Integer, 
#     db.ForeignKey("playlists.id"))


# # DO NOT MODIFY THIS FUNCTION
# def connect_db(app):
#     """Connect to database."""

#     db.app = app
#     db.init_app(app)


"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):

    db.app = app
    db.init_app(app)
    db.create_all()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)

    songs = db.relationship('Song',
                            secondary='playlist_songs',
                            backref='playlists')

    def __repr__(self):
        return f"<Playlist {self.name}>"


class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Song {self.title} - {self.artist}>"


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlist_songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"))
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"))
    


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)