import enum

@enum.unique
class BrowserSupported(enum.Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"
    EDGE = "edge"