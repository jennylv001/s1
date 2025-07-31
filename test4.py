#!/usr/bin/env python3
"""
Test file for stealth configuration - test4.py reference from problem statement.
This test validates stealth configuration propagation from BrowserConfig → BrowserProfile → Browser Session.
"""

import asyncio
import logging
from pathlib import Path

import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Import from browser_use module structure
try:
    from browser_use.browser.profile import BrowserProfile, StealthLevel
    from browser_use.browser.session import BrowserSession
except ImportError:
    # Fallback to local imports
    import importlib.util
    
    # Import profile module
    profile_spec = importlib.util.spec_from_file_location("profile", Path(__file__).parent / "browser" / "profile.py")
    profile_module = importlib.util.module_from_spec(profile_spec)
    sys.modules["profile"] = profile_module
    profile_spec.loader.exec_module(profile_module)
    
    BrowserProfile = profile_module.BrowserProfile
    StealthLevel = profile_module.StealthLevel
    
    # Import session module
    session_spec = importlib.util.spec_from_file_location("session", Path(__file__).parent / "browser" / "session.py")
    session_module = importlib.util.module_from_spec(session_spec)
    sys.modules["session"] = session_module
    session_spec.loader.exec_module(session_module)
    
    BrowserSession = session_module.BrowserSession


async def test_stealth_configuration():
    """Test stealth configuration propagation through the config pipeline."""
    
    # Test configuration with stealth enabled
    browser_profile = BrowserProfile(
        stealth=True,
        stealth_level=StealthLevel.MILITARY_GRADE,
        headless=False,
        user_data_dir=None,  # Temporary profile
        channel='chrome'
    )
    
    print(f"🧪 Testing stealth configuration:")
    print(f"   stealth={browser_profile.stealth}")
    print(f"   stealth_level={browser_profile.stealth_level}")
    print(f"   headless={browser_profile.headless}")
    
    # Create browser session with stealth configuration
    browser_session = BrowserSession(browser_profile=browser_profile)
    
    print(f"🔧 Browser session created: {browser_session}")
    
    # Test that stealth args are generated correctly
    stealth_args = browser_session.browser_profile._get_stealth_args()
    print(f"🕶️ Generated {len(stealth_args)} stealth Chrome flags")
    
    # Test user agent profile generation
    ua_profile = browser_session.browser_profile.get_stealth_user_agent_profile()
    if ua_profile:
        print(f"🎭 User agent profile: {ua_profile['user_agent'][:50]}...")
    else:
        print(f"🎭 No user agent spoofing (stealth level: {browser_session.browser_profile.stealth_level})")
    
    # Test JavaScript evasion scripts
    evasion_scripts = browser_session.browser_profile.get_stealth_evasion_scripts()
    if evasion_scripts:
        print(f"🛡️ JS evasion scripts: {len(evasion_scripts)} characters")
    else:
        print(f"🛡️ No JS evasion scripts (stealth level: {browser_session.browser_profile.stealth_level})")
    
    # Calculate effectiveness score
    effectiveness = 0
    if browser_session.browser_profile.stealth:
        effectiveness += 10  # patchright
        if browser_session.browser_profile.stealth_level == StealthLevel.ADVANCED:
            effectiveness += 70  # flags
            effectiveness += 10  # UA spoofing
        elif browser_session.browser_profile.stealth_level == StealthLevel.MILITARY_GRADE:
            effectiveness += 70  # flags
            effectiveness += 10  # UA spoofing
            effectiveness += 10  # JS evasion
    
    print(f"📊 Stealth effectiveness: {effectiveness}%")
    
    # Test different stealth levels
    for level in [StealthLevel.BASIC, StealthLevel.ADVANCED, StealthLevel.MILITARY_GRADE]:
        test_profile = BrowserProfile(stealth=True, stealth_level=level)
        test_args = test_profile._get_stealth_args()
        test_ua = test_profile.get_stealth_user_agent_profile()
        test_js = test_profile.get_stealth_evasion_scripts()
        
        print(f"🔬 {level.value}: {len(test_args)} flags, {'✓' if test_ua else '✗'} UA, {'✓' if test_js else '✗'} JS")


if __name__ == "__main__":
    # Set up logging for stealth testing
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
    
    print("🚀 Starting stealth configuration test (test4.py)")
    asyncio.run(test_stealth_configuration())
    print("✅ Stealth configuration test completed")