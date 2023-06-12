# """Forms for playlist app."""

# # from wsgiref.validate import validator
# from wtforms import SelectField, StringField
# from flask_wtf import FlaskForm
# from wtforms.validators import InputRequired


# class PlaylistForm(FlaskForm):
#     """Form for adding playlists."""

#     # Add the necessary code to use this form
#     name = StringField("Name", validators=[InputRequired()])
#     description = StringField("Description", validators=[InputRequired()])



# class SongForm(FlaskForm):
#     """Form for adding songs."""

#     # Add the necessary code to use this form
#     title = StringField("Title", validators=[InputRequired()])
#     artist = StringField("Artist", validators=[InputRequired()])


# # DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
# class NewSongForPlaylistForm(FlaskForm):
#     """Form for adding a song to playlist."""

#     song = SelectField('Song To Add', coerce=int)

"""Forms for playlist app."""

from wtforms import validators, StringField, SelectField, TextAreaField
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Name', validators=[validators.DataRequired()])
    description = TextAreaField('Description')


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title', validators=[validators.DataRequired()])
    artist = StringField('Artist', validators=[validators.DataRequired()])


class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)