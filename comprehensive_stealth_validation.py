#!/usr/bin/env python3
"""
Comprehensive Stealth Configuration Validation Test

This test validates that the stealth configuration fixes work correctly by:
1. Creating an Agent with BrowserConfig(stealth=True)
2. Tracking stealth configuration through the initialization chain
3. Actually running a simple task to validate end-to-end functionality
4. Providing detailed logging of configuration state at each step
"""

import asyncio
import logging
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import from the local modules
from agent.service import Agent
from browser import BrowserConfig


def setup_detailed_logging():
    """Setup detailed logging to track stealth configuration throughout the process"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    
    # Enable specific loggers for stealth tracking
    logging.getLogger('browser_use').setLevel(logging.DEBUG)
    logging.getLogger('agent.service').setLevel(logging.DEBUG)
    logging.getLogger('browser.profile').setLevel(logging.DEBUG)
    logging.getLogger('browser.session').setLevel(logging.DEBUG)


async def validate_stealth_initialization_chain():
    """
    Test the complete Agent → BrowserSession → BrowserProfile initialization chain
    with detailed validation at each step
    """
    print("=" * 80)
    print("🔍 COMPREHENSIVE STEALTH CONFIGURATION VALIDATION TEST")
    print("=" * 80)
    
    # Step 1: Create BrowserConfig with stealth=True
    print("\n📋 Step 1: Creating BrowserConfig with stealth=True")
    browser_config = BrowserConfig(stealth=True)
    print(f"✅ BrowserConfig created: stealth={browser_config.stealth}, stealth_level={browser_config.stealth_level}")
    assert browser_config.stealth is True, f"BrowserConfig stealth should be True, got {browser_config.stealth}"
    
    # Step 2: Create Agent with the stealth-enabled BrowserConfig
    print("\n📋 Step 2: Creating Agent with stealth-enabled BrowserConfig")
    print("🔍 Monitoring Agent initialization for stealth configuration preservation...")
    
    try:
        agent = Agent(
            task="Navigate to example.com and capture a screenshot",
            browser_config=browser_config
        )
        print(f"✅ Agent created successfully")
        
        # Step 3: Validate stealth configuration in Agent's browser_profile
        print("\n📋 Step 3: Validating stealth configuration in Agent's browser_profile")
        agent_profile_stealth = getattr(agent.browser_profile, 'stealth', False)
        agent_profile_level = getattr(agent.browser_profile, 'stealth_level', None)
        print(f"🔍 Agent.browser_profile: stealth={agent_profile_stealth}, stealth_level={agent_profile_level}")
        
        if not agent_profile_stealth:
            print(f"❌ CRITICAL: Agent.browser_profile.stealth={agent_profile_stealth} - stealth lost in Agent initialization!")
            return False
        else:
            print(f"✅ Agent.browser_profile stealth configuration preserved: stealth=True")
            
        # Step 4: Validate stealth configuration in BrowserSession
        print("\n📋 Step 4: Validating stealth configuration in Agent.browser_session")
        if not hasattr(agent, 'browser_session') or agent.browser_session is None:
            print("⚠️ BrowserSession not yet initialized, will be created on first use")
        else:
            session_profile_stealth = getattr(agent.browser_session.browser_profile, 'stealth', False)
            session_profile_level = getattr(agent.browser_session.browser_profile, 'stealth_level', None)
            print(f"🔍 Agent.browser_session.browser_profile: stealth={session_profile_stealth}, stealth_level={session_profile_level}")
            
            if not session_profile_stealth:
                print(f"❌ CRITICAL: Agent.browser_session.browser_profile.stealth={session_profile_stealth} - stealth lost in BrowserSession!")
                return False
            else:
                print(f"✅ BrowserSession stealth configuration preserved: stealth=True")
        
        # Step 5: Initialize the browser session and run a simple task
        print("\n📋 Step 5: Running simple task to validate end-to-end stealth functionality")
        print("🔍 This will trigger BrowserSession initialization if not already done...")
        
        # Run a simple task that will initialize the browser session
        result = await agent.run("Navigate to https://example.com")
        
        # Step 6: Final validation after browser session is fully initialized
        print("\n📋 Step 6: Final validation after browser session initialization")
        final_session_stealth = getattr(agent.browser_session.browser_profile, 'stealth', False)
        final_session_level = getattr(agent.browser_session.browser_profile, 'stealth_level', None)
        print(f"🔍 Final Agent.browser_session.browser_profile: stealth={final_session_stealth}, stealth_level={final_session_level}")
        
        if not final_session_stealth:
            print(f"❌ CRITICAL: Final stealth configuration lost! stealth={final_session_stealth}")
            return False
        else:
            print(f"✅ Final stealth configuration preserved: stealth=True")
            
        print(f"\n🎯 Task result: {result}")
        
        # Close the browser session cleanly
        if hasattr(agent, 'browser_session') and agent.browser_session:
            await agent.browser_session.close()
            print("🔒 Browser session closed cleanly")
            
        return True
        
    except Exception as e:
        print(f"❌ ERROR during agent creation or execution: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False


async def run_comprehensive_validation():
    """Run the comprehensive stealth validation test"""
    print("🚀 Starting Comprehensive Stealth Configuration Validation")
    
    # Setup detailed logging
    setup_detailed_logging()
    
    # Run the validation
    success = await validate_stealth_initialization_chain()
    
    print("\n" + "=" * 80)
    if success:
        print("✅ COMPREHENSIVE STEALTH VALIDATION: PASSED")
        print("🔒 Stealth configuration successfully preserved throughout the entire initialization chain")
        print("🎯 End-to-end Agent functionality validated with stealth=True")
    else:
        print("❌ COMPREHENSIVE STEALTH VALIDATION: FAILED")
        print("🚫 Stealth configuration was lost during initialization")
        print("⚠️  The stealth fixes require additional work")
    print("=" * 80)
    
    return success


if __name__ == "__main__":
    # Run the validation
    result = asyncio.run(run_comprehensive_validation())
    sys.exit(0 if result else 1)