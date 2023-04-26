from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgFPz8oACXd55ruswpL3TBIIGZRgfettB7JvrxY9EK9f3XEuSRY2IbQqnBnOqJ7Q9tiHDLhPqf7f3mv-AOnuX9u-YnSfSjmHnzNHV_4tri2XDmGFegIGHTz2URfL7RxwLvnvrQ8btIKXfy_Ed2E1vNLj9r_Pst85-EjAID0FCEj2iSGPVc1hhPZ5zxOcUI855OGmuBp4Iavx2Y93h1ZGnlQ-ig8j18mgSw6Rpxca-mxcIRi36XoQmZylaZI5Yp34Jf_aqoybci2kDK62EWeDy5hzQc8QodBJFyYU8Hq8ub_iupJkwUydyFhKvGsC17zLJ_8ROUuWgEtNBVTxWgfqRdlQJuNN4QAAAAFc06grAA")
BOT_TOKEN = getenv("BOT_TOKEN", "6195626321:AAGE8qd6TtxzvELWZnqaZ1sVKaD0XdJFzgk")
BOT_NAME = getenv("BOT_NAME", "𝙺𝚁𝙰𝚈𝚉𝙴𝙽 𝙰𝚂i𝚂𝚃𝙰𝙽") 
API_ID = int(getenv("API_ID", 22007754))
API_HASH = getenv("API_HASH", "7f0d6b4d928155eda014acdb5a014620")
BOT_USERNAME = getenv("BOT_USERNAME", "KrayzenMusicbot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
