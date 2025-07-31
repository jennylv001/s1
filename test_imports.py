#!/usr/bin/env python3
"""
Simple test to check imports for stealth mode
"""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from browser.profile import BrowserProfile, StealthLevel
    print("✅ BrowserProfile and StealthLevel imported successfully")
except ImportError as e:
    print(f"❌ Failed to import BrowserProfile/StealthLevel: {e}")

try:
    from browser.stealth_ops import StealthOps
    print("✅ StealthOps imported successfully")
except ImportError as e:
    print(f"❌ Failed to import StealthOps: {e}")

try:
    from browser.session import BrowserSession
    print("✅ BrowserSession imported successfully")
except ImportError as e:
    print(f"❌ Failed to import BrowserSession: {e}")

try:
    import patchright
    print(f"✅ Patchright imported successfully")
    # Test version detection methods
    version_methods = [
        ('__version__', lambda: getattr(patchright, '__version__', None)),
        ('VERSION', lambda: getattr(patchright, 'VERSION', None)),
        ('version', lambda: getattr(patchright, 'version', None)),
    ]
    
    for name, method in version_methods:
        try:
            version = method()
            if version:
                print(f"✅ Patchright version via {name}: {version}")
                break
        except AttributeError:
            print(f"⚠️ Patchright {name} attribute not found")
    else:
        print("⚠️ No patchright version found via standard attributes")
        
except ImportError as e:
    print(f"❌ Failed to import patchright: {e}")

try:
    import playwright
    print(f"✅ Playwright imported successfully")
    if hasattr(playwright, '__version__'):
        print(f"✅ Playwright version: {playwright.__version__}")
    else:
        print("⚠️ Playwright version not found")
except ImportError as e:
    print(f"❌ Failed to import playwright: {e}")