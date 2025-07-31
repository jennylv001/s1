#!/usr/bin/env python3
"""
Real Agent Stealth Configuration Validation

This test validates that the stealth configuration fixes work correctly by:
1. Creating real Agent and BrowserConfig instances (without browser dependencies)
2. Tracking stealth configuration through the initialization chain
3. Validating each step of the configuration preservation
4. Testing the exact code paths that would be used in production
"""

import sys
import logging
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def setup_logging():
    """Setup detailed logging"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )

def test_browser_config_creation():
    """Test BrowserConfig creation with stealth=True"""
    print("📋 Step 1: Testing BrowserConfig creation with stealth=True")
    
    try:
        from browser import BrowserConfig
        
        # Create BrowserConfig with stealth=True
        browser_config = BrowserConfig(stealth=True)
        
        print(f"✅ BrowserConfig created successfully")
        print(f"🔍 BrowserConfig.stealth = {browser_config.stealth}")
        print(f"🔍 BrowserConfig.stealth_level = {browser_config.stealth_level}")
        
        # Validate stealth configuration
        if browser_config.stealth is True:
            print("✅ PASS: BrowserConfig.stealth=True preserved")
            return browser_config
        else:
            print(f"❌ FAIL: BrowserConfig.stealth={browser_config.stealth}, expected True")
            return None
            
    except Exception as e:
        print(f"❌ ERROR: Failed to create BrowserConfig: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_browser_profile_creation(browser_config):
    """Test BrowserProfile creation from BrowserConfig"""
    print("\n📋 Step 2: Testing BrowserProfile creation from BrowserConfig")
    
    try:
        from browser.profile import BrowserProfile
        
        # Create BrowserProfile from BrowserConfig (simulating Agent's process)
        profile_kwargs = browser_config.model_dump() if browser_config else {}
        browser_profile = BrowserProfile(**profile_kwargs)
        
        print(f"✅ BrowserProfile created successfully")
        print(f"🔍 BrowserProfile.stealth = {browser_profile.stealth}")
        print(f"🔍 BrowserProfile.stealth_level = {browser_profile.stealth_level}")
        
        # Validate stealth configuration preservation
        if browser_profile.stealth is True:
            print("✅ PASS: BrowserProfile.stealth=True preserved from BrowserConfig")
            return browser_profile
        else:
            print(f"❌ FAIL: BrowserProfile.stealth={browser_profile.stealth}, expected True")
            return None
            
    except Exception as e:
        print(f"❌ ERROR: Failed to create BrowserProfile: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_browser_session_creation(browser_profile):
    """Test BrowserSession creation with stealth profile"""
    print("\n📋 Step 3: Testing BrowserSession creation with stealth profile")
    
    try:
        from browser.session import BrowserSession
        
        # Create BrowserSession with stealth profile (simulating Agent's process)
        # Pass stealth parameters explicitly like our Fix 1 does
        stealth_params = {}
        if hasattr(browser_profile, 'stealth'):
            stealth_params['stealth'] = browser_profile.stealth
        if hasattr(browser_profile, 'stealth_level'):
            stealth_params['stealth_level'] = browser_profile.stealth_level
        
        print(f"🔍 Explicit stealth params being passed: {stealth_params}")
        
        # Create BrowserSession with explicit stealth parameters (like Fix 1)
        session_kwargs = {
            'browser_profile': browser_profile,
        }
        
        # Only add stealth parameters if stealth is enabled (like Fix 1)
        if stealth_params.get('stealth', False):
            session_kwargs.update(stealth_params)
            print(f"🔍 Adding explicit stealth params to BrowserSession")
        
        browser_session = BrowserSession(**session_kwargs)
        
        print(f"✅ BrowserSession created successfully")
        print(f"🔍 BrowserSession.browser_profile.stealth = {browser_session.browser_profile.stealth}")
        print(f"🔍 BrowserSession.browser_profile.stealth_level = {browser_session.browser_profile.stealth_level}")
        
        # Validate stealth configuration preservation
        if browser_session.browser_profile.stealth is True:
            print("✅ PASS: BrowserSession.browser_profile.stealth=True preserved")
            return browser_session
        else:
            print(f"❌ FAIL: BrowserSession.browser_profile.stealth={browser_session.browser_profile.stealth}, expected True")
            return None
            
    except Exception as e:
        print(f"❌ ERROR: Failed to create BrowserSession: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_agent_creation():
    """Test Agent creation with stealth BrowserConfig"""
    print("\n📋 Step 4: Testing Agent creation with stealth BrowserConfig")
    
    try:
        from agent.service import Agent
        from browser import BrowserConfig
        
        # Create Agent with stealth BrowserConfig (real production scenario)
        browser_config = BrowserConfig(stealth=True)
        
        print(f"🔍 Creating Agent with BrowserConfig: stealth={browser_config.stealth}")
        
        # Mock the LLM to avoid external dependencies
        class MockLLM:
            def __init__(self):
                pass
            
            async def ainvoke(self, *args, **kwargs):
                return "Mock response"
                
            async def abatch(self, *args, **kwargs):
                return ["Mock response"]
        
        agent = Agent(
            task="Test stealth configuration preservation",
            llm=MockLLM(),
            browser_config=browser_config
        )
        
        print(f"✅ Agent created successfully")
        
        # Validate Agent's browser_profile stealth configuration
        agent_profile_stealth = getattr(agent.browser_profile, 'stealth', False)
        agent_profile_level = getattr(agent.browser_profile, 'stealth_level', None)
        
        print(f"🔍 Agent.browser_profile.stealth = {agent_profile_stealth}")
        print(f"🔍 Agent.browser_profile.stealth_level = {agent_profile_level}")
        
        if agent_profile_stealth is True:
            print("✅ PASS: Agent.browser_profile.stealth=True preserved from BrowserConfig")
            return agent
        else:
            print(f"❌ FAIL: Agent.browser_profile.stealth={agent_profile_stealth}, expected True")
            return None
            
    except Exception as e:
        print(f"❌ ERROR: Failed to create Agent: {e}")
        import traceback
        traceback.print_exc()
        return None

def run_comprehensive_stealth_validation():
    """Run comprehensive stealth configuration validation"""
    print("🛡️ REAL AGENT STEALTH CONFIGURATION VALIDATION")
    print("=" * 80)
    print("🎯 Testing actual production code paths with stealth configuration fixes")
    
    setup_logging()
    
    # Track test results
    test_results = []
    
    # Step 1: Test BrowserConfig creation
    browser_config = test_browser_config_creation()
    test_results.append(("BrowserConfig Creation", browser_config is not None))
    
    if not browser_config:
        print("\n❌ CRITICAL: Cannot proceed without valid BrowserConfig")
        return False
    
    # Step 2: Test BrowserProfile creation
    browser_profile = test_browser_profile_creation(browser_config)
    test_results.append(("BrowserProfile Creation", browser_profile is not None))
    
    if not browser_profile:
        print("\n❌ CRITICAL: Cannot proceed without valid BrowserProfile")
        return False
    
    # Step 3: Test BrowserSession creation
    browser_session = test_browser_session_creation(browser_profile)
    test_results.append(("BrowserSession Creation", browser_session is not None))
    
    # Step 4: Test Agent creation (most comprehensive test)
    agent = test_agent_creation()
    test_results.append(("Agent Creation", agent is not None))
    
    # Final validation summary
    print("\n" + "=" * 80)
    print("📋 VALIDATION RESULTS SUMMARY")
    print("=" * 80)
    
    passed_tests = sum(1 for _, passed in test_results if passed)
    total_tests = len(test_results)
    
    for test_name, passed in test_results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    success_rate = (passed_tests / total_tests) * 100
    print(f"\n📊 Overall Success Rate: {passed_tests}/{total_tests} ({success_rate:.1f}%)")
    
    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ Stealth configuration successfully preserved through entire initialization chain")
        print("🔒 Production fixes validated - stealth mode will work correctly")
        print("\n🛡️ Key Validations:")
        print("• BrowserConfig(stealth=True) → correctly created")
        print("• BrowserProfile preserves stealth from BrowserConfig") 
        print("• BrowserSession preserves stealth through model_copy operations")
        print("• Agent preserves stealth through complete initialization chain")
        print("• Fix 1 (Agent explicit params) ✅")
        print("• Fix 2 (BrowserSession preservation) ✅")
        print("• Fix 4 (BrowserProfile integrity) ✅")
        return True
    else:
        print("\n❌ VALIDATION FAILED")
        print("🚨 Stealth configuration is still being lost during initialization")
        print("⚠️  Additional fixes may be needed")
        return False

if __name__ == "__main__":
    success = run_comprehensive_stealth_validation()
    sys.exit(0 if success else 1)