#!/usr/bin/env python3
"""
Browser Stealth Mode Diagnostic Script

This script diagnoses stealth mode configuration and patchright availability.
Used to troubleshoot issues where stealth mode is disabled despite correct configuration.
"""

import sys
import subprocess
import importlib.util
from pathlib import Path
from typing import Dict, Any, Optional

def check_patchright_installation() -> Dict[str, Any]:
    """Check if patchright is installed and get version information."""
    result = {
        'installed': False,
        'version': None,
        'import_error': None,
        'location': None
    }
    
    try:
        # Try to import patchright
        import patchright
        result['installed'] = True
        result['location'] = str(Path(patchright.__file__).parent)
        
        # Try different methods to get version
        version_methods = [
            ('__version__', lambda: getattr(patchright, '__version__', None)),
            ('VERSION', lambda: getattr(patchright, 'VERSION', None)), 
            ('version', lambda: getattr(patchright, 'version', None)),
        ]
        
        for name, method in version_methods:
            try:
                version = method()
                if version:
                    result['version'] = str(version)
                    break
            except (AttributeError, ImportError):
                continue
        
        # If no version found through attributes, try alternative methods
        if not result['version']:
            try:
                # Try to get version from pip show (most reliable method)
                pip_result = subprocess.run(
                    [sys.executable, '-m', 'pip', 'show', 'patchright'],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if pip_result.returncode == 0:
                    for line in pip_result.stdout.split('\n'):
                        if line.startswith('Version:'):
                            result['version'] = line.split(':', 1)[1].strip()
                            break
            except (subprocess.TimeoutExpired, subprocess.SubprocessError):
                pass
        
        # If still no version, try pkg_resources
        if not result['version']:
            try:
                import pkg_resources
                result['version'] = pkg_resources.get_distribution('patchright').version
            except (ImportError, pkg_resources.DistributionNotFound):
                pass
                
    except ImportError as e:
        result['import_error'] = str(e)
    except Exception as e:
        result['import_error'] = f"Unexpected error: {str(e)}"
    
    return result

def check_playwright_installation() -> Dict[str, Any]:
    """Check if playwright is installed and get version information."""
    result = {
        'installed': False,
        'version': None,
        'import_error': None,
        'location': None
    }
    
    try:
        import playwright
        result['installed'] = True
        result['location'] = str(Path(playwright.__file__).parent)
        
        # Try to get version
        if hasattr(playwright, '__version__'):
            result['version'] = playwright.__version__
        else:
            try:
                import pkg_resources
                result['version'] = pkg_resources.get_distribution('playwright').version
            except (ImportError, pkg_resources.DistributionNotFound):
                pass
                
    except ImportError as e:
        result['import_error'] = str(e)
    except Exception as e:
        result['import_error'] = f"Unexpected error: {str(e)}"
    
    return result

def check_stealth_configuration() -> Dict[str, Any]:
    """Check stealth configuration in the browser profile."""
    result = {
        'profile_available': False,
        'stealth_level_enum_available': False,
        'stealth_ops_available': False,
        'configuration_valid': False,
        'errors': []
    }
    
    try:
        # Check if browser profile can be imported
        sys.path.insert(0, str(Path(__file__).parent))
        from browser.profile import BrowserProfile, StealthLevel
        result['profile_available'] = True
        result['stealth_level_enum_available'] = True
        
        # Check if StealthOps can be imported
        from browser.stealth_ops import StealthOps
        result['stealth_ops_available'] = True
        
        # Test basic stealth configuration
        profile = BrowserProfile(stealth=True, stealth_level=StealthLevel.ADVANCED)
        
        # Validate stealth config
        profile.validate_stealth_config()
        
        # Test stealth args generation
        stealth_args = profile._get_stealth_args()
        if len(stealth_args) > 0:
            result['configuration_valid'] = True
        else:
            result['errors'].append("Stealth args generation returned empty list")
            
    except ImportError as e:
        result['errors'].append(f"Import error: {str(e)}")
    except Exception as e:
        result['errors'].append(f"Configuration error: {str(e)}")
    
    return result

def check_browser_session_compatibility() -> Dict[str, Any]:
    """Check if browser session can be created with stealth configuration."""
    result = {
        'session_importable': False,
        'stealth_setup_works': False,
        'errors': []
    }
    
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from browser.session import BrowserSession
        from browser.profile import BrowserProfile, StealthLevel
        result['session_importable'] = True
        
        # Create stealth profile
        profile = BrowserProfile(
            stealth=True,
            stealth_level=StealthLevel.ADVANCED,
            headless=True  # Use headless for diagnostic to avoid opening windows
        )
        
        # Create session (but don't start it - just test creation)
        session = BrowserSession(browser_profile=profile)
        
        # Check if stealth configuration is preserved
        if session.browser_profile.stealth:
            result['stealth_setup_works'] = True
        else:
            result['errors'].append("Stealth configuration lost during session creation")
            
    except ImportError as e:
        result['errors'].append(f"Import error: {str(e)}")
    except Exception as e:
        result['errors'].append(f"Session creation error: {str(e)}")
    
    return result

def diagnose_stealth_pipeline() -> Dict[str, Any]:
    """Run comprehensive stealth pipeline diagnosis."""
    print("🔍 Browser Stealth Mode Diagnostic")
    print("=" * 50)
    
    # Check patchright installation
    print("\n📦 Checking patchright installation...")
    patchright_info = check_patchright_installation()
    if patchright_info['installed']:
        print(f"✅ Patchright installed at: {patchright_info['location']}")
        print(f"✅ Version: {patchright_info['version'] or 'Unknown (detection issue)'}")
    else:
        print(f"❌ Patchright not installed: {patchright_info['import_error']}")
    
    # Check playwright installation
    print("\n📦 Checking playwright installation...")
    playwright_info = check_playwright_installation()
    if playwright_info['installed']:
        print(f"✅ Playwright installed at: {playwright_info['location']}")
        print(f"✅ Version: {playwright_info['version'] or 'Unknown'}")
    else:
        print(f"❌ Playwright not installed: {playwright_info['import_error']}")
    
    # Check stealth configuration
    print("\n⚙️ Checking stealth configuration...")
    stealth_config = check_stealth_configuration()
    if stealth_config['profile_available']:
        print("✅ BrowserProfile available")
    else:
        print("❌ BrowserProfile not available")
        
    if stealth_config['stealth_level_enum_available']:
        print("✅ StealthLevel enum available")
    else:
        print("❌ StealthLevel enum not available")
        
    if stealth_config['stealth_ops_available']:
        print("✅ StealthOps class available")
    else:
        print("❌ StealthOps class not available")
        
    if stealth_config['configuration_valid']:
        print("✅ Stealth configuration validation successful")
    else:
        print("❌ Stealth configuration validation failed")
        for error in stealth_config['errors']:
            print(f"   • {error}")
    
    # Check browser session compatibility
    print("\n🌐 Checking browser session compatibility...")
    session_info = check_browser_session_compatibility()
    if session_info['session_importable']:
        print("✅ BrowserSession importable")
    else:
        print("❌ BrowserSession not importable")
        
    if session_info['stealth_setup_works']:
        print("✅ Stealth configuration preserved in session")
    else:
        print("❌ Stealth configuration lost in session")
        for error in session_info['errors']:
            print(f"   • {error}")
    
    # Overall assessment
    print("\n🎯 Overall Assessment")
    print("-" * 30)
    
    all_checks = [
        patchright_info['installed'],
        playwright_info['installed'],
        stealth_config['configuration_valid'],
        session_info['stealth_setup_works']
    ]
    
    passed_checks = sum(all_checks)
    total_checks = len(all_checks)
    
    if passed_checks == total_checks:
        print("🟢 All stealth components working correctly")
        print("💡 If stealth mode is still disabled, check browser session startup logs")
    elif passed_checks >= total_checks - 1:
        print("🟡 Stealth components mostly working with minor issues")
        print("💡 Review errors above and check runtime behavior")
    else:
        print("🔴 Major stealth component issues detected")
        print("💡 Fix the errors above before enabling stealth mode")
    
    return {
        'patchright': patchright_info,
        'playwright': playwright_info,
        'stealth_config': stealth_config,
        'session_info': session_info,
        'overall_score': f"{passed_checks}/{total_checks}"
    }

def main():
    """Run the stealth diagnostic."""
    try:
        result = diagnose_stealth_pipeline()
        
        print(f"\n📊 Diagnostic Score: {result['overall_score']}")
        
        # Provide specific recommendations
        if not result['patchright']['installed']:
            print("\n🔧 Recommendation: Install patchright for stealth mode")
            print("   pip install patchright")
            
        if result['patchright']['installed'] and not result['patchright']['version']:
            print("\n🔧 Recommendation: Patchright version detection issue")
            print("   This is a known issue but doesn't affect functionality")
            
        print("\n✨ Diagnostic complete!")
        
        return result['overall_score'].split('/')[0] == result['overall_score'].split('/')[1]
        
    except Exception as e:
        print(f"\n💥 Diagnostic failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)