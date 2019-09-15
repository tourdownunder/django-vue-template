from django.views.generic.list import View


class LoginMusicBrainzView(View):
    template_name = "login_musicbrainz.html"


class LoginSpotifyView(View):
    template_name = "login_spotify.html"


class IndexView(View):
    template_name = "index.html"
