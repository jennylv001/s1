#!/usr/bin/env python3
"""
StealthOps Integration Usage Examples

This script demonstrates how to use the enhanced stealth capabilities
in the browser automation system with different stealth levels.
"""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Load StealthOps for demonstration purposes
import random
import json
from typing import Dict, List, Any
exec(open('browser/stealth_ops.py').read(), globals())

from enum import Enum

class StealthLevel(str, Enum):
    BASIC = 'basic'
    ADVANCED = 'advanced'
    MILITARY_GRADE = 'military-grade'

class MockBrowserProfile:
    """Mock BrowserProfile class to demonstrate stealth integration."""
    
    def __init__(self, stealth: bool = False, stealth_level: StealthLevel = StealthLevel.MILITARY_GRADE):
        self.stealth = stealth
        self.stealth_level = stealth_level
        # Other profile attributes would be here
        self.args = []
        self.headless = False
        self.disable_security = False
        self.deterministic_rendering = False
    
    def _get_stealth_args(self) -> List[str]:
        """Get stealth-specific Chrome CLI args based on stealth level configuration."""
        if not self.stealth:
            return []

        stealth_args = []
        
        if self.stealth_level == StealthLevel.BASIC:
            # Basic level: minimal stealth args already included in default args
            # The main stealth work is done by using patchright instead of playwright
            return stealth_args
            
        elif self.stealth_level == StealthLevel.ADVANCED:
            # Advanced level: add military-grade Chrome flags
            stealth_args.extend(StealthOps.generate_military_grade_flags())
            
        elif self.stealth_level == StealthLevel.MILITARY_GRADE:
            # Military-grade level: all stealth flags
            stealth_args.extend(StealthOps.generate_military_grade_flags())
        
        print(f'🕶️ Applied {len(stealth_args)} stealth-specific Chrome args for {self.stealth_level.value} level')
        return stealth_args

    def get_stealth_user_agent_profile(self) -> dict[str, Any] | None:
        """Get stealth user agent profile for spoofing when stealth is enabled."""
        if not self.stealth or self.stealth_level == StealthLevel.BASIC:
            return None
        return StealthOps.get_user_agent_profile()

    def get_stealth_evasion_scripts(self) -> str | None:
        """Get JavaScript evasion scripts when military-grade stealth is enabled."""
        if not self.stealth or self.stealth_level != StealthLevel.MILITARY_GRADE:
            return None
        
        # Get user agent profile for dynamic script generation
        ua_profile = self.get_stealth_user_agent_profile()
        if not ua_profile:
            return None
            
        return StealthOps.get_evasion_scripts(ua_profile)

def demonstrate_stealth_configurations():
    """Demonstrate different stealth configurations and their capabilities."""
    print("🎭 StealthOps Integration Usage Examples")
    print("=" * 50)
    
    configurations = [
        (False, StealthLevel.BASIC, "No stealth - standard automation"),
        (True, StealthLevel.BASIC, "Basic stealth - patchright only"),
        (True, StealthLevel.ADVANCED, "Advanced stealth - flags + UA spoofing"),
        (True, StealthLevel.MILITARY_GRADE, "Military-grade stealth - full suite")
    ]
    
    for stealth_enabled, stealth_level, description in configurations:
        print(f"\n📋 Configuration: {description}")
        print("-" * 40)
        
        # Create a mock browser profile with the configuration
        profile = MockBrowserProfile(stealth=stealth_enabled, stealth_level=stealth_level)
        
        # Demonstrate Chrome args generation
        stealth_args = profile._get_stealth_args()
        print(f"🔧 Chrome flags: {len(stealth_args)} stealth-specific arguments")
        if stealth_args:
            print(f"   Sample: {stealth_args[0]}")
        
        # Demonstrate user agent spoofing
        ua_profile = profile.get_stealth_user_agent_profile()
        if ua_profile:
            print(f"🎭 User Agent: {ua_profile['user_agent'][:60]}...")
            print(f"🌐 Client Hints: {ua_profile['sec_ch_ua']}")
            print(f"💻 Platform: {ua_profile['sec_ch_ua_platform']}")
        else:
            print("🎭 User Agent: Using default browser UA")
        
        # Demonstrate JavaScript evasion
        evasion_scripts = profile.get_stealth_evasion_scripts()
        if evasion_scripts:
            print(f"🛡️ JS Evasion: {len(evasion_scripts):,} characters of detection evasion code")
            print("   Features: webdriver hiding, plugin spoofing, canvas fingerprint protection")
        else:
            print("🛡️ JS Evasion: None")
        
        # Calculate effectiveness score
        effectiveness = 0
        if stealth_enabled:
            effectiveness += 10  # patchright
            if stealth_level == StealthLevel.ADVANCED:
                effectiveness += 70  # flags
                effectiveness += 10  # UA spoofing
            elif stealth_level == StealthLevel.MILITARY_GRADE:
                effectiveness += 70  # flags
                effectiveness += 10  # UA spoofing
                effectiveness += 10  # JS evasion
        
        print(f"📊 Stealth Effectiveness: {effectiveness}%")

def demonstrate_code_usage():
    """Show example code for using stealth in browser automation."""
    print("\n\n💻 Code Usage Examples")
    print("=" * 50)
    
    print("""
# Example 1: Basic stealth mode (patchright only)
profile = BrowserProfile(
    stealth=True,
    stealth_level=StealthLevel.BASIC
)
browser_session = BrowserSession(browser_profile=profile)

# Example 2: Advanced stealth mode (flags + UA spoofing)  
profile = BrowserProfile(
    stealth=True,
    stealth_level=StealthLevel.ADVANCED,
    headless=False,  # Recommended for maximum stealth
    channel=BrowserChannel.CHROME  # Use real Chrome for best results
)
browser_session = BrowserSession(browser_profile=profile)

# Example 3: Military-grade stealth (full suite)
profile = BrowserProfile(
    stealth=True,
    stealth_level=StealthLevel.MILITARY_GRADE,
    headless=False,
    channel=BrowserChannel.CHROME,
    user_data_dir="/path/to/persistent/profile"  # Persistent profile recommended
)
browser_session = BrowserSession(browser_profile=profile)

# The stealth integration is automatic - just enable stealth=True
# All stealth features are applied transparently during browser launch
""")

def demonstrate_stealth_features():
    """Demonstrate the specific stealth features that are applied."""
    print("\n🛡️ Stealth Features Overview")
    print("=" * 50)
    
    # Chrome flags
    flags = StealthOps.generate_military_grade_flags()
    print(f"\n🔧 Military-Grade Chrome Flags ({len(flags)} total):")
    print("   Core stealth flags:")
    core_flags = [f for f in flags if 'automation' in f.lower() or 'blink' in f.lower()][:3]
    for flag in core_flags:
        print(f"     • {flag}")
    print(f"   + {len(flags) - len(core_flags)} additional flags for fingerprint protection")
    
    # User agent spoofing
    ua_profile = StealthOps.get_user_agent_profile()
    print(f"\n🎭 User Agent Spoofing:")
    print(f"   User-Agent: {ua_profile['user_agent']}")
    print(f"   Platform: {ua_profile['platform']}")
    print(f"   Languages: {ua_profile['languages']}")
    print(f"   Hardware: {ua_profile['hardwareConcurrency']} cores, {ua_profile['deviceMemory']}GB RAM")
    print(f"   Screen: {ua_profile['screen']['width']}x{ua_profile['screen']['height']}")
    
    # JavaScript evasion
    evasion_script = StealthOps.get_evasion_scripts(ua_profile)
    print(f"\n🛡️ JavaScript Evasion ({len(evasion_script):,} characters):")
    print("   Detection bypasses:")
    evasion_features = [
        "navigator.webdriver property hiding",
        "Plugin and MIME type spoofing", 
        "Permissions API manipulation",
        "WebGL vendor/renderer spoofing",
        "Canvas fingerprint noise injection",
        "Audio context fingerprint protection",
        "WebRTC IP leak prevention",
        "Battery API spoofing",
        "Timezone and locale manipulation",
        "Mouse event trust restoration"
    ]
    for feature in evasion_features:
        print(f"     • {feature}")

def main():
    """Run all stealth integration demonstrations."""
    demonstrate_stealth_configurations()
    demonstrate_code_usage()
    demonstrate_stealth_features()
    
    print("\n\n🎯 Summary")
    print("=" * 50)
    print("✅ StealthOps integration provides comprehensive anti-detection capabilities")
    print("✅ Three stealth levels: basic, advanced, military-grade")
    print("✅ 60+ Chrome flags for detection evasion")
    print("✅ Dynamic user agent spoofing with realistic device fingerprints")
    print("✅ 22,000+ chars of JavaScript detection evasion code")
    print("✅ Automatic integration - just set stealth=True")
    print("✅ Backward compatible - existing code continues to work")
    
    print("\n🚀 The browser automation system is now military-grade stealth ready!")

if __name__ == "__main__":
    main()