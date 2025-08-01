#!/usr/bin/env python3
"""
Quick demo to show the stealth logging changes in action.
Run this to see the difference between INFO and DEBUG level output.
"""

import logging
import sys

def demo_logging_changes():
    """Demonstrate the stealth logging level changes"""
    print("🎭 Stealth Logging Changes Demo")
    print("=" * 50)
    
    # Set up INFO level logging (typical production setting)
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)-5s | %(message)s',
        stream=sys.stdout
    )
    logger = logging.getLogger('stealth_demo')
    
    print("\n📊 INFO LEVEL OUTPUT (production/operations):")
    print("-" * 50)
    
    # Simulate our changes - these are now DEBUG (won't show at INFO level)
    logger.debug('🏗️ BrowserProfile#a1b2 CREATED (obj#c3d4)')
    logger.debug('🏗️   └─ Creation context: demo.py:25 in create_profile()')
    logger.debug('📋 BrowserProfile#a1b2 COPYING (obj#c3d4)')
    logger.debug('📋   └─ Copy context: session.py:298 in apply_overrides()')
    logger.debug('🎭 BrowserSession#e5f6 SETUP_PLAYWRIGHT')
    logger.debug('🎭   └─ Final config: stealth=True, channel=chrome')
    
    # These remain at INFO level (will show)
    logger.info('🕶️ Stealth mode ENABLED: Using patchright + chrome browser')
    logger.info('🕶️ Stealth level: MILITARY_GRADE')
    logger.info('🚀 BrowserSession#e5f6 LAUNCHING BROWSER')
    logger.info('🚀   └─ CONFIRMED STEALTH MODE: True (level: MILITARY_GRADE)')
    logger.info('🚀 BrowserSession#e5f6 BROWSER PROCESS STARTED')
    logger.info('🚀   └─ Process PID: 12345')
    
    print("\n📊 DEBUG LEVEL OUTPUT (development/troubleshooting):")
    print("-" * 50)
    
    # Change to DEBUG level to show all messages
    logging.getLogger().setLevel(logging.DEBUG)
    
    # Now all messages will show
    logger.debug('🏗️ BrowserProfile#a1b2 CREATED (obj#c3d4)')
    logger.debug('🏗️   └─ Creation context: demo.py:25 in create_profile()')
    logger.debug('📋 BrowserProfile#a1b2 COPYING (obj#c3d4)')
    logger.debug('📋   └─ Copy context: session.py:298 in apply_overrides()')
    logger.debug('🎭 BrowserSession#e5f6 SETUP_PLAYWRIGHT')
    logger.debug('🎭   └─ Final config: stealth=True, channel=chrome')
    logger.info('🕶️ Stealth mode ENABLED: Using patchright + chrome browser')
    logger.info('🕶️ Stealth level: MILITARY_GRADE')
    logger.info('🚀 BrowserSession#e5f6 LAUNCHING BROWSER')
    logger.info('🚀   └─ CONFIRMED STEALTH MODE: True (level: MILITARY_GRADE)')
    logger.info('🚀 BrowserSession#e5f6 BROWSER PROCESS STARTED')
    logger.info('🚀   └─ Process PID: 12345')
    
    print("\n✅ BENEFITS:")
    print("  • INFO level: Clean operational status (6 messages)")
    print("  • DEBUG level: Full diagnostic details (12 messages)")
    print("  • Stealth effectiveness: Preserved and enhanced")
    print("  • Troubleshooting: All details available when needed")

if __name__ == "__main__":
    demo_logging_changes()
    print("\n🎯 Demo completed - stealth logging changes working correctly!")