#!/usr/bin/env python3
"""
Test stealth logging enhancements.
This test validates the new stealth logging and configuration features.
"""

import logging
import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Set up logging to see all stealth messages
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s [%(name)s] %(message)s',
    stream=sys.stdout
)

def test_stealth_profile_logging():
    """Test stealth logging enhancements in BrowserProfile."""
    print("🧪 Testing stealth profile logging enhancements...")
    
    # Import the modules we need
    try:
        # Load StealthOps first since it's a dependency
        exec(open('browser/stealth_ops.py').read(), globals())
        
        # Mock the browser_use imports needed by profile.py
        import types
        
        # Create mock modules to satisfy imports
        browser_use_config = types.ModuleType('browser_use.config')
        browser_use_config.CONFIG = types.SimpleNamespace()
        browser_use_config.CONFIG.BROWSER_USE_DEFAULT_USER_DATA_DIR = Path.home() / '.cache' / 'browseruse' / 'profiles' / 'default'
        browser_use_config.CONFIG.IN_DOCKER = False
        sys.modules['browser_use.config'] = browser_use_config
        
        browser_use_observability = types.ModuleType('browser_use.observability')
        browser_use_observability.observe_debug = lambda **kwargs: lambda func: func
        sys.modules['browser_use.observability'] = browser_use_observability
        
        browser_use_utils = types.ModuleType('browser_use.utils')
        browser_use_utils._log_pretty_path = lambda x: str(x) if x else None
        browser_use_utils.logger = logging.getLogger('browser_use.utils')
        sys.modules['browser_use.utils'] = browser_use_utils
        
        # Create mock browser_use.browser.types module
        browser_use_types = types.ModuleType('browser_use.browser.types')
        browser_use_types.ViewportSize = dict
        browser_use_types.ClientCertificate = dict
        browser_use_types.Geolocation = dict 
        browser_use_types.HttpCredentials = dict
        browser_use_types.ProxySettings = dict
        sys.modules['browser_use.browser.types'] = browser_use_types
        
        # Create mock stealth_ops module
        browser_use_stealth_ops = types.ModuleType('browser_use.browser.stealth_ops')
        browser_use_stealth_ops.StealthOps = StealthOps
        sys.modules['browser_use.browser.stealth_ops'] = browser_use_stealth_ops
        
        # Now import the profile module
        profile_spec = __import__('importlib.util').util.spec_from_file_location(
            "browser_use.browser.profile", 
            Path(__file__).parent / "browser" / "profile.py"
        )
        profile_module = __import__('importlib.util').util.module_from_spec(profile_spec)
        sys.modules["browser_use.browser.profile"] = profile_module
        profile_spec.loader.exec_module(profile_module)
        
        BrowserProfile = profile_module.BrowserProfile
        StealthLevel = profile_module.StealthLevel
        
        print("✅ Successfully imported BrowserProfile and StealthLevel")
        
    except Exception as e:
        print(f"❌ Failed to import modules: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test basic stealth configuration
    print("\n🔬 Testing BASIC stealth level...")
    basic_profile = BrowserProfile(
        stealth=True,
        stealth_level=StealthLevel.BASIC,
        headless=False
    )
    basic_profile.log_stealth_summary()
    print(f"✅ Basic effectiveness: {basic_profile.calculate_stealth_effectiveness()}%")
    
    print("\n🔬 Testing ADVANCED stealth level...")
    advanced_profile = BrowserProfile(
        stealth=True,
        stealth_level=StealthLevel.ADVANCED,
        headless=False
    )
    advanced_profile.log_stealth_summary()
    print(f"✅ Advanced effectiveness: {advanced_profile.calculate_stealth_effectiveness()}%")
    
    print("\n🔬 Testing MILITARY_GRADE stealth level...")
    military_profile = BrowserProfile(
        stealth=True,
        stealth_level=StealthLevel.MILITARY_GRADE,
        headless=False
    )
    military_profile.log_stealth_summary()
    print(f"✅ Military-grade effectiveness: {military_profile.calculate_stealth_effectiveness()}%")
    
    print("\n🔬 Testing stealth DISABLED...")
    disabled_profile = BrowserProfile(
        stealth=False,
        headless=False
    )
    disabled_profile.log_stealth_summary()
    print(f"✅ Disabled effectiveness: {disabled_profile.calculate_stealth_effectiveness()}%")
    
    print("\n🔬 Testing config validation...")
    # Test invalid stealth level
    invalid_profile = BrowserProfile(
        stealth=True,
        stealth_level="invalid_level",  # This should trigger fallback
        headless=False
    )
    print(f"✅ Invalid config handled, effectiveness: {invalid_profile.calculate_stealth_effectiveness()}%")
    
    return True

if __name__ == "__main__":
    print("🚀 Starting stealth logging test suite")
    success = test_stealth_profile_logging()
    if success:
        print("\n🎉 All stealth logging tests PASSED!")
    else:
        print("\n❌ Some stealth logging tests FAILED!")
        sys.exit(1)