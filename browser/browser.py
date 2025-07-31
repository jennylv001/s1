from .profile import BrowserProfile
from .session import BrowserSession

BrowserConfig = BrowserProfile
BrowserContextConfig = BrowserProfile
Browser = BrowserSession

__all__ = ['BrowserConfig', 'BrowserContextConfig', 'Browser']
