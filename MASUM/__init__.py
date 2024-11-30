from MASUM.core.bot import Baby
from MASUM.core.dir import dirr
from MASUM.core.git import git
from MASUM.core.userbot import Userbot
from MASUM.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Baby()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
