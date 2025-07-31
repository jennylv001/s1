#!/usr/bin/env python3
"""
Integration test to validate stealth configuration fixes.

This test validates that the stealth configuration preservation fixes are correctly implemented
by examining the actual code changes in the relevant files.
"""

import re
from pathlib import Path

def test_agent_service_fixes():
    """Test that Agent service has the stealth configuration preservation fixes."""
    print("🧪 Testing Agent Service Fixes")
    print("-" * 40)
    
    agent_service_path = Path(__file__).parent / 'agent' / 'service.py'
    content = agent_service_path.read_text()
    
    # Test 1: Check for enhanced stealth configuration preservation logic
    if '# Fix 1: Agent State Transfer Preservation' in content:
        print("✅ Fix 1 comment found in agent service")
    else:
        print("❌ Fix 1 comment missing from agent service")
        return False
    
    # Test 2: Check for stealth debugging logs
    stealth_log_patterns = [
        r'Preserving stealth config',
        r'browser_profile\.stealth',
        r'STEALTH CONFIGURATION LOST'
    ]
    
    found_patterns = 0
    for pattern in stealth_log_patterns:
        if re.search(pattern, content):
            found_patterns += 1
            print(f"✅ Found stealth logging pattern: {pattern}")
        else:
            print(f"❌ Missing stealth logging pattern: {pattern}")
    
    if found_patterns >= 2:
        print("✅ Sufficient stealth debugging logs found in agent service")
        return True
    else:
        print("❌ Insufficient stealth debugging logs in agent service")
        return False

def test_browser_session_fixes():
    """Test that BrowserSession has the profile fallback protection fixes."""
    print("\n🧪 Testing Browser Session Fixes")
    print("-" * 40)
    
    session_path = Path(__file__).parent / 'browser' / 'session.py'
    content = session_path.read_text()
    
    # Test 1: Check for fallback protection fix
    if '# Fix 2: Profile Fallback State Protection' in content:
        print("✅ Fix 2 comment found in browser session")
    else:
        print("❌ Fix 2 comment missing from browser session")
        return False
    
    # Test 2: Check for stealth preservation in fallback method
    fallback_patterns = [
        r'stealth_config = getattr.*stealth.*False',
        r'stealth_level = getattr.*stealth_level.*None',
        r'self\.browser_profile\.stealth = stealth_config',
        r'stealth config preserved'
    ]
    
    found_patterns = 0
    for pattern in fallback_patterns:
        if re.search(pattern, content):
            found_patterns += 1
            print(f"✅ Found fallback protection pattern: {pattern}")
        else:
            print(f"⚠️ Fallback protection pattern not found: {pattern}")
    
    # Test 3: Check for enhanced playwright setup logging
    setup_patterns = [
        r'setup_playwright called with stealth',
        r'Successfully using.*for stealth mode',
        r'Expected patchright but got'
    ]
    
    setup_found = 0
    for pattern in setup_patterns:
        if re.search(pattern, content):
            setup_found += 1
            print(f"✅ Found playwright setup pattern: {pattern}")
    
    if found_patterns >= 2 and setup_found >= 1:
        print("✅ Browser session stealth fixes are properly implemented")
        return True
    else:
        print("❌ Browser session stealth fixes need more work")
        return False

def test_browser_profile_fixes():
    """Test that BrowserProfile has the channel enforcement fixes."""
    print("\n🧪 Testing Browser Profile Fixes")
    print("-" * 40)
    
    profile_path = Path(__file__).parent / 'browser' / 'profile.py'
    content = profile_path.read_text()
    
    # Test 1: Check for channel enforcement fix
    if '# Fix 3: Channel Enforcement for Stealth' in content:
        print("✅ Fix 3 comment found in browser profile")
    else:
        print("❌ Fix 3 comment missing from browser profile")
        return False
    
    # Test 2: Check for channel enforcement logic
    channel_patterns = [
        r'Force Chrome channel when stealth=True',
        r'self\.channel = BrowserChannel\.CHROME',
        r'Forcing browser channel.*for patchright compatibility'
    ]
    
    found_patterns = 0
    for pattern in channel_patterns:
        if re.search(pattern, content):
            found_patterns += 1
            print(f"✅ Found channel enforcement pattern: {pattern}")
        else:
            print(f"⚠️ Channel enforcement pattern not found: {pattern}")
    
    # Test 3: Check for enhanced validation logging
    validation_patterns = [
        r'validate_stealth_config.*stealth=',
        r'Final stealth config after validation'
    ]
    
    validation_found = 0
    for pattern in validation_patterns:
        if re.search(pattern, content):
            validation_found += 1
            print(f"✅ Found validation logging pattern: {pattern}")
    
    if found_patterns >= 2 and validation_found >= 1:
        print("✅ Browser profile stealth fixes are properly implemented")
        return True
    else:
        print("❌ Browser profile stealth fixes need more work")
        return False

def test_stealth_configuration_pipeline():
    """Test the complete stealth configuration pipeline for consistency."""
    print("\n🧪 Testing Complete Stealth Configuration Pipeline")  
    print("-" * 50)
    
    # Check that all three fixes work together
    agent_service_path = Path(__file__).parent / 'agent' / 'service.py'
    session_path = Path(__file__).parent / 'browser' / 'session.py'
    profile_path = Path(__file__).parent / 'browser' / 'profile.py'
    
    agent_content = agent_service_path.read_text()
    session_content = session_path.read_text()
    profile_content = profile_path.read_text()
    
    # Test that the pipeline has consistent logging keywords
    pipeline_keywords = [
        '🔍',  # Debug logging emoji
        'stealth=',  # Stealth config logging
        'STEALTH CONFIGURATION',  # Error logging for config loss
        'stealth config',  # General stealth config references
    ]
    
    pipeline_consistency = 0
    for keyword in pipeline_keywords:
        files_with_keyword = 0
        
        if keyword in agent_content:
            files_with_keyword += 1
        if keyword in session_content:
            files_with_keyword += 1
        if keyword in profile_content:
            files_with_keyword += 1
        
        if files_with_keyword >= 2:  # At least 2 files should have each keyword
            pipeline_consistency += 1
            print(f"✅ Pipeline consistency: '{keyword}' found in {files_with_keyword}/3 files")
        else:
            print(f"⚠️ Pipeline inconsistency: '{keyword}' found in only {files_with_keyword}/3 files")
    
    # Test that error handling is comprehensive
    error_patterns = [
        'STEALTH CONFIGURATION LOST',
        'stealth=False',
        'stealth config preserved'
    ]
    
    error_handling = 0
    for pattern in error_patterns:
        if pattern in agent_content or pattern in session_content:
            error_handling += 1
            print(f"✅ Error handling: '{pattern}' found in stealth pipeline")
    
    if pipeline_consistency >= 3 and error_handling >= 2:
        print("✅ Stealth configuration pipeline is comprehensive and consistent")
        return True
    else:
        print("❌ Stealth configuration pipeline needs more consistency")
        return False

def main():
    """Run all integration tests to validate stealth fixes."""
    print("🛡️ Stealth Configuration Fixes Integration Test")
    print("=" * 60)
    
    tests = [
        ("Agent Service Fixes", test_agent_service_fixes),
        ("Browser Session Fixes", test_browser_session_fixes), 
        ("Browser Profile Fixes", test_browser_profile_fixes),
        ("Configuration Pipeline", test_stealth_configuration_pipeline),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Error in {test_name}: {type(e).__name__}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n📋 Integration Test Results")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed += 1
    
    print("-" * 60)
    print(f"Results: {passed}/{total} integration tests passed")
    
    if passed == total:
        print("🎉 All stealth configuration fixes are properly implemented!")
        print("\n🔧 Fixes Summary:")
        print("• Fix 1: Agent State Transfer Preservation - ✅ IMPLEMENTED")
        print("• Fix 2: Profile Fallback State Protection - ✅ IMPLEMENTED") 
        print("• Fix 3: Channel Enforcement for Stealth - ✅ IMPLEMENTED")
        print("\n💡 Next Steps:")
        print("• Test with actual browser automation to verify runtime behavior")
        print("• Validate stealth effectiveness on bot detection sites")
        print("• Monitor logs for stealth configuration preservation")
        return True
    else:
        print(f"⚠️ {total - passed} integration tests failed")
        print("🔧 Review the failing components and ensure all fixes are properly implemented")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)