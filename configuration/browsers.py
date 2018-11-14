import enum

@enum.unique
class BrowserSupported(enum.Enum):
    CHROME_MAC = "chrome_mac"
    CHROME_LINUX = "chrome_linux"
    CHROME_WIN = "chrome_win"