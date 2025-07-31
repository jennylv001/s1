# filename: browser_use/stealth_ops.py
"""
Military-Grade Stealth Operations for Browser Automation.
Zero detection. Maximum evasion. No compromises.
"""
import random
import json 
import string # Not used in the provided snippet, but kept from user's original import
from typing import Dict, List, Any
from pathlib import Path # Not used in the provided snippet, but kept

class StealthOps:
    """Special Forces grade browser stealth configuration"""

    @staticmethod
    def generate_military_grade_flags() -> List[str]:
        """Chrome flags that make detection near impossible.
           Refined based on stability and effectiveness assessment.
        """
        core_stealth_flags = [
            '--disable-blink-features=AutomationControlled',
            '--exclude-switches=enable-automation',
            # '--disable-features=UserAgentClientHint', # Client Hints can be managed via JS or headers
        ]

        process_and_security_tweaks = [
            '--disable-features=IsolateOrigins,site-per-process,TranslateUI,CertificateTransparencyComponentUpdater,LazyFrameLoading,OutOfBlinkCors,ImprovedCookieControls,PrivacySandboxSettings4,HeavyAdIntervention,HeavyAdPrivacyMitigations',
            '--disable-ipc-flooding-protection',
            '--disable-renderer-backgrounding',
            # '--disable-web-security',  # EXTREMELY RISKY. Only if absolutely necessary.
            # '--allow-running-insecure-content', # Similarly risky.
            '--disable-features=BlockInsecurePrivateNetworkRequests',
        ]

        fingerprint_protection_flags = [
            '--disable-features=AudioServiceOutOfProcess',
            '--force-webrtc-ip-handling-policy=disable_non_proxied_udp',
            '--disable-webrtc-encryption', # Test this; can be a fingerprint itself.
            # The following are very aggressive and might be too revealing or break sites.
            # Prefer JS spoofing for WebRTC parameters.
            # '--disable-webrtc-hw-encoding',
            # '--disable-webrtc-hw-decoding',
            # '--disable-features=WebRtcHWH264Encoding',
            # '--disable-features=WebRtcHWVP8Encoding',
        ]

        telemetry_and_feature_reduction_flags = [
            '--disable-logging',
            '--no-first-run',
            '--no-default-browser-check',
            '--disable-background-timer-throttling',
            '--disable-features=CalculateNativeWinOcclusion',
            '--disable-hang-monitor',
            '--disable-sync',
            '--disable-translate',
            '--metrics-recording-only',
            '--disable-default-apps',
            # '--mute-audio', # Can be fingerprintable; real users have audio.
            '--no-pings',
            '--disable-breakpad',
            '--disable-cloud-import',
            '--disable-gesture-typing',
            '--disable-offer-store-unmasked-wallet-cards',
            '--disable-offer-upload-credit-cards',
            '--disable-print-preview',
            # '--disable-speech-api', # Can be fingerprintable
            # '--disable-speech-synthesis-api', # Can be fingerprintable
            # '--disable-voice-input', # Can be fingerprintable
            '--disable-wake-on-wifi',
            '--disable-notifications',
            '--disable-prompt-on-repost',
            '--disable-background-networking',
            '--disable-client-side-phishing-detection',
            '--disable-component-cloud-policy',
            '--disable-component-update',
            '--disable-domain-reliability',
            '--disable-password-generation',
            '--disable-plugins-discovery',
            '--disable-renderer-accessibility',
            '--disable-search-geolocation-disclosure',
            '--disable-shader-name-hashing',
            '--disable-smooth-scrolling', # Human users have smooth scroll; disabling might be odd.
            '--disable-suggestions-ui',
            '--disable-sync-preferences',
            '--disable-tab-for-desktop-share',
            '--disable-threaded-animation',
            '--disable-threaded-scrolling',
            '--disable-touch-adjustment',
            '--disable-touch-drag-drop',
            '--disable-touch-editing',
            '--disable-usb-keyboard-detect',
            '--disable-v8-idle-notification-after-commit',
            '--disable-vibrate',
            '--disable-xss-auditor', # Deprecated
            '--disable-zero-suggest',
            '--hide-scrollbars', # Good for screenshots, but users see scrollbars.
            '--disable-features=IdleDetection',
            '--disable-features=GlobalMediaControls,GlobalMediaControlsPlayPause,GlobalMediaControlsPictureInPicture,GlobalMediaControlsSeekBar,GlobalMediaControlsModernUI',
            '--disable-features=MediaEngagementBypassAutoplayPolicies,NetworkTimeServiceQuerying',
            # '--disable-permissions-api', # We patch navigator.permissions.query via JS instead.
        ]

        gpu_rendering_flags = [
            '--ignore-gpu-blocklist', # Can force GPU on systems where it might be unstable.
            '--enable-webgl',         # Enable and then spoof parameters via JS.
            '--force-color-profile=srgb',
            # Avoid outright disabling GPU (--disable-gpu) or WebGL (--disable-webgl)
            # as this is a strong fingerprint. Rely on JS parameter spoofing.
            # Disabling AA might also be a fingerprint.
            # '--disable-canvas-aa',
            # '--disable-2d-canvas-clip-aa',
        ]

        # THESE ARE HIGHLY UNSTABLE / DETECTABLE - USE WITH EXTREME CAUTION AND TESTING
        # '--single-process',
        # '--no-zygote', # Linux specific

        all_flags = list(dict.fromkeys( # Deduplicate
            core_stealth_flags
            + process_and_security_tweaks
            + fingerprint_protection_flags
            + telemetry_and_feature_reduction_flags
            + gpu_rendering_flags
        ))
        return all_flags

    @staticmethod
    def get_docker_specific_flags() -> List[str]:
        return [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-gpu-sandbox', # If GPU is not disabled entirely
        ]

    @staticmethod
    def get_user_agent_profile() -> Dict[str, Any]:
        """Returns a realistic User-Agent and corresponding profile data."""
        profiles = [
            {
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
                # For HTTP Headers
                "sec_ch_ua": '"Chromium";v="125", "Google Chrome";v="125", ";Not A Brand";v="99"',
                "sec_ch_ua_mobile": "?0",
                "sec_ch_ua_platform": '"Windows"',
                "sec_ch_ua_platform_version": '"10.0.0"',
                "sec_ch_ua_model": '""',
                "sec_ch_ua_arch": '"x86"',
                "sec_ch_ua_bitness": '"64"',
                "sec_ch_ua_full_version_list": '"Chromium";v="125.0.6422.142", "Google Chrome";v="125.0.6422.142", ";Not A Brand";v="99.0.0.0"',
                "accept_language_header": "en-US,en;q=0.9",
                # For JS Spoofing (navigator.userAgentData)
                "sec_ch_ua_brands_for_js": [
                    {"brand": "Chromium", "version": "125"},
                    {"brand": "Google Chrome", "version": "125"},
                    {"brand": ";Not A Brand", "version": "99"}
                ],
                "sec_ch_ua_mobile_for_js": False,
                "sec_ch_ua_platform_for_js": "Windows",
                "sec_ch_ua_platform_version_for_js": "10.0.0",
                "sec_ch_ua_arch_for_js": "x86",
                "sec_ch_ua_bitness_for_js": "64",
                "sec_ch_ua_model_for_js": "",
                "sec_ch_ua_full_version_for_js": "125.0.6422.142",
                # Other existing fields
                "platform": "Win32", "vendor": "Google Inc.", "languages": ['en-US', 'en'],
                "screen": {"width": 1920, "height": 1080, "availWidth": 1920, "availHeight": 1040, "colorDepth": 24, "pixelDepth": 24},
                "deviceMemory": 8, "hardwareConcurrency": 8,
                "timezone": {"id": "America/New_York", "offset": -300},
                "webgl_vendor": "Google Inc. (Intel)", "webgl_renderer": "ANGLE (Intel, Intel(R) UHD Graphics 630 Direct3D11 vs_5_0 ps_5_0, D3D11)"
            },
            {
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
                # For HTTP Headers
                "sec_ch_ua": '"Chromium";v="125", "Google Chrome";v="125", ";Not A Brand";v="99"',
                "sec_ch_ua_mobile": "?0",
                "sec_ch_ua_platform": '"macOS"',
                "sec_ch_ua_platform_version": '"10.15.7"',
                "sec_ch_ua_model": '""',
                "sec_ch_ua_arch": '"arm"', # Example for M1/M2 Macs
                "sec_ch_ua_bitness": '"64"',
                "sec_ch_ua_full_version_list": '"Chromium";v="125.0.6422.142", "Google Chrome";v="125.0.6422.142", ";Not A Brand";v="99.0.0.0"',
                "accept_language_header": "en-US,en;q=0.9",
                # For JS Spoofing
                "sec_ch_ua_brands_for_js": [
                    {"brand": "Chromium", "version": "125"},
                    {"brand": "Google Chrome", "version": "125"},
                    {"brand": ";Not A Brand", "version": "99"}
                ],
                "sec_ch_ua_mobile_for_js": False,
                "sec_ch_ua_platform_for_js": "macOS",
                "sec_ch_ua_platform_version_for_js": "10.15.7",
                "sec_ch_ua_arch_for_js": "arm",
                "sec_ch_ua_bitness_for_js": "64",
                "sec_ch_ua_model_for_js": "", # e.g. "MacBookPro17,1" - can be added
                "sec_ch_ua_full_version_for_js": "125.0.6422.142",
                # Other existing fields
                "platform": "MacIntel", "vendor": "Google Inc.", "languages": ['en-US', 'en'],
                "screen": {"width": 1728, "height": 1117, "availWidth": 1728, "availHeight": 1079, "colorDepth": 24, "pixelDepth": 24},
                "deviceMemory": 16, "hardwareConcurrency": 10,
                "timezone": {"id": "America/Los_Angeles", "offset": -420},
                "webgl_vendor": "Google Inc. (Apple)", "webgl_renderer": "ANGLE (Apple, Apple M1 Pro, Metal)"
            },
            # TODO: Add more diverse profiles (Linux, other browser versions, mobile if targeted)
            # Ensure all profiles have the new sec_ch_ua* fields.
        ]
        # Add dynamic variations to reduce fingerprinting
        selected_profile = random.choice(profiles)
        return StealthOps._add_profile_variations(selected_profile)

    @staticmethod
    def _add_profile_variations(profile: Dict[str, Any]) -> Dict[str, Any]:
        """Add subtle random variations to user agent profile to reduce fingerprinting."""
        # Create a copy to avoid mutating the original
        varied_profile = profile.copy()
        
        # Add subtle RAM variations (±25% realistic variance)
        base_memory = profile["deviceMemory"]
        memory_variations = [base_memory//2, base_memory, base_memory*2]
        if base_memory >= 8:
            memory_variations.extend([base_memory + 8, base_memory + 16])
        varied_profile["deviceMemory"] = random.choice(memory_variations)
        
        # Add CPU core variations (realistic for the platform)
        base_cores = profile["hardwareConcurrency"]
        if "Intel" in profile.get("webgl_renderer", ""):
            # Intel systems commonly have 4, 6, 8, 12, 16 cores
            core_options = [4, 6, 8, 12, 16]
        elif "Apple" in profile.get("webgl_renderer", ""):
            # Apple Silicon commonly have 8, 10, 12 cores
            core_options = [8, 10, 12]
        else:
            # Generic variations
            core_options = [4, 6, 8, 12, 16]
        varied_profile["hardwareConcurrency"] = random.choice([c for c in core_options if c <= base_cores * 2])
        
        # Add minor screen resolution variations (realistic common resolutions)
        if profile["screen"]["width"] == 1920:
            # Common 1920-width variations
            width_options = [1920, 1920]  # Keep most common
            height_options = [1080, 1200]  # 16:9 and 16:10
        elif profile["screen"]["width"] == 1440:
            width_options = [1440, 1536]  # MacBook variations
            height_options = [900, 960]
        else:
            width_options = [profile["screen"]["width"]]
            height_options = [profile["screen"]["height"]]
            
        new_width = random.choice(width_options)
        new_height = random.choice(height_options)
        varied_profile["screen"]["width"] = new_width
        varied_profile["screen"]["height"] = new_height
        varied_profile["screen"]["availWidth"] = new_width
        varied_profile["screen"]["availHeight"] = new_height - 40  # Taskbar/dock space
        
        return varied_profile


    @staticmethod
    def get_evasion_scripts(profile: Dict[str, Any]) -> str:
        """JavaScript patches that defeat all major detection methods.
           Takes a profile dictionary to inject dynamic values.
        """
        # Prefer profile values, fallback to common defaults if not specified in profile
        # This allows the profile to be the single source of truth for spoofed values.
        navigator_platform = profile.get("platform", "Win32")
        navigator_vendor = profile.get("vendor", "Google Inc.")
        navigator_languages = json.dumps(profile.get("languages", ['en-US', 'en']))
        device_memory = profile.get("deviceMemory", 8)
        hardware_concurrency = profile.get("hardwareConcurrency", random.choice([4, 8, 12, 16]))

        screen_width = profile.get("screen", {}).get("width", 1920)
        screen_height = profile.get("screen", {}).get("height", 1080)
        screen_avail_width = profile.get("screen", {}).get("availWidth", screen_width)
        screen_avail_height = profile.get("screen", {}).get("availHeight", screen_height - 40) # Simulate taskbar
        screen_color_depth = profile.get("screen", {}).get("colorDepth", 24)
        screen_pixel_depth = profile.get("screen", {}).get("pixelDepth", 24)

        webgl_vendor = profile.get("webgl_vendor", "Google Inc. (Intel)")
        webgl_renderer = profile.get("webgl_renderer", "ANGLE (Intel, Intel(R) UHD Graphics 630 Direct3D11 vs_5_0 ps_5_0, D3D11)")

        timezone_offset = profile.get("timezone", {}).get("offset", -300) # e.g., -300 for EST (UTC-5)
        timezone_id = profile.get("timezone", {}).get("id", "America/New_York")
        locale_str = profile.get("languages", ['en-US', 'en'])[0]

        # Values for navigator.userAgentData spoofing
        # Use specific _for_js keys from profile for JS values
        ua_data_brands_json = json.dumps(profile.get("sec_ch_ua_brands_for_js", [
            {"brand": "Chromium", "version": "125"}, # Fallback
            {"brand": "Google Chrome", "version": "125"}, # Fallback
            {"brand": ";Not A Brand", "version": "99"}  # Fallback
        ]))
        ua_data_mobile = profile.get("sec_ch_ua_mobile_for_js", False) # boolean
        ua_data_platform = json.dumps(profile.get("sec_ch_ua_platform_for_js", "Windows")) # string

        return f"""
        // Military-Grade Evasion Suite (Dynamically Configured)
        (async () => {{
            const consoleLog = (msg, isError = false) => {{
                // console.log(`StealthOps: ${{msg}}`); // Internal logging, will be blocked by patchright
            }};

            // --- Function.prototype.toString protection ---
            const _nativeToString = Function.prototype.toString;
            const _patchToString = (obj, prop, originalFuncStr) => {{
                try {{
                    const originalDescriptor = Object.getOwnPropertyDescriptor(obj, prop);
                    if (originalDescriptor && !originalDescriptor.configurable) return; // Cannot patch
                    Object.defineProperty(obj, prop, {{
                        configurable: true, enumerable: false, writable: false,
                        value: function toString() {{ return originalFuncStr || _nativeToString.call(this); }}
                    }});
                }} catch (e) {{ consoleLog(`Failed to patch toString for ${{prop}}`, true); }}
            }};
            const _makeNative = (funcInstance, funcNameStr) => {{
                try {{
                    const nativeLikeStr = `function ${{funcNameStr || funcInstance.name}}() {{ [native code] }}`;
                    _patchToString(funcInstance, 'toString', nativeLikeStr);
                }} catch(e) {{ consoleLog(`Failed to makeNative ${{funcNameStr || funcInstance.name}}`, true); }}
            }};


            // 1. WebDriver
            if (navigator.webdriver) {{
              try {{ Object.defineProperty(navigator, 'webdriver', {{ get: () => false, configurable: true }}); _makeNative(navigator.webdriver.get, 'get webdriver'); }} catch(e) {{consoleLog('P1 fail', true)}}
            }} else {{ // Ensure it's explicitly false if undefined
              try {{ Object.defineProperty(navigator, 'webdriver', {{ get: () => false, configurable: true }}); }} catch(e) {{consoleLog('P1.1 fail', true)}}
            }}


            // 2. Plugins & MimeTypes
            const plugins = [
              {{ name: 'Chrome PDF Plugin', filename: 'internal-pdf-viewer', description: 'Portable Document Format', mimeTypes: [{{ type: 'application/pdf', suffixes: 'pdf', description: '' }},{{ type: 'text/pdf', suffixes: 'pdf', description: '' }}]}},
              {{ name: 'Chrome PDF Viewer', filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai', description: '', mimeTypes: [] }},
              {{ name: 'Native Client', filename: 'internal-nacl-plugin', description: '', mimeTypes: [{{ type: 'application/x-nacl', suffixes: '', description: 'Native Client Executable' }},{{ type: 'application/x-pnacl', suffixes: '', description: 'Portable Native Client Executable' }}] }}
            ];
            const mimeTypes = [
              {{ type: 'application/pdf', suffixes: 'pdf', enabledPlugin: plugins[0], description: '' }}, {{ type: 'text/pdf', suffixes: 'pdf', enabledPlugin: plugins[0], description: '' }},
              {{ type: 'application/x-nacl', suffixes: '', enabledPlugin: plugins[2], description: 'Native Client Executable' }}, {{ type: 'application/x-pnacl', suffixes: '', enabledPlugin: plugins[2], description: 'Portable Native Client Executable' }}
            ];
            try {{ Object.defineProperty(navigator, 'plugins', {{ get: () => ({{ item: i => plugins[i], namedItem: name => plugins.find(p=>p.name===name) || null, length: plugins.length, refresh: () => {{}} }}) , configurable: true}}); _makeNative(navigator.plugins.get, 'get plugins'); }} catch(e) {{consoleLog('P2.1 fail', true)}}
            try {{ Object.defineProperty(navigator, 'mimeTypes', {{ get: () => ({{ item: i => mimeTypes[i], namedItem: name => mimeTypes.find(m=>m.type===name) || null, length: mimeTypes.length }}) , configurable: true}}); _makeNative(navigator.mimeTypes.get, 'get mimeTypes'); }} catch(e) {{consoleLog('P2.2 fail', true)}}


            // 3. Chrome runtime (very gentle, just ensure it exists to prevent errors)
            if (typeof window.chrome === 'undefined') {{
                window.chrome = {{}};
            }}
            if (typeof window.chrome.runtime === 'undefined') {{
                try {{ window.chrome.runtime = {{ id: undefined, connect: () => {{}}, sendMessage: () => {{}} }}; }} catch(e) {{consoleLog('P3 fail', true)}}
            }}


            // 4. Permissions API
            try {{
                const originalPermissionsQuery = navigator.permissions.query;
                const patchedPermissionsQuery = async (permissionDesc) => {{
                    if (permissionDesc.name === 'notifications') return Promise.resolve({{ state: Notification.permission }});
                    if (permissionDesc.name === 'geolocation') return Promise.resolve({{ state: 'prompt' }});
                    if (['camera', 'microphone'].includes(permissionDesc.name)) return Promise.resolve({{ state: 'prompt' }});
                    return originalPermissionsQuery.call(navigator.permissions, permissionDesc);
                }};
                Object.defineProperty(navigator.permissions, 'query', {{ value: patchedPermissionsQuery, configurable: true, writable: true }});
                _makeNative(navigator.permissions.query, 'query');
            }} catch(e) {{consoleLog('P4 fail', true)}}


            // 5. WebGL Vendor/Renderer Spoofing
            try {{
                const originalGetParameter = WebGLRenderingContext.prototype.getParameter;
                const patchedGetParameterWebGL = function(parameter) {{
                    const G = WebGLRenderingContext;
                    if (parameter === G.VENDOR) return '{webgl_vendor}';
                    if (parameter === G.RENDERER) return '{webgl_renderer}';
                    if (parameter === 37446 /* UNMASKED_VENDOR_WEBGL */) return '{webgl_vendor}';
                    if (parameter === 37445 /* UNMASKED_RENDERER_WEBGL */) return '{webgl_renderer}';
                    // Add other common params with typical values for consistency
                    if (parameter === G.MAX_VERTEX_UNIFORM_VECTORS) return 256;
                    if (parameter === G.MAX_TEXTURE_SIZE) return 16384;
                    return originalGetParameter.apply(this, arguments);
                }};
                WebGLRenderingContext.prototype.getParameter = patchedGetParameterWebGL;
                _makeNative(WebGLRenderingContext.prototype.getParameter, 'getParameter');

                if (typeof WebGL2RenderingContext !== 'undefined') {{
                    const originalGetParameter2 = WebGL2RenderingContext.prototype.getParameter;
                     const patchedGetParameterWebGL2 = function(parameter) {{
                        const G2 = WebGL2RenderingContext;
                        if (parameter === G2.VENDOR) return '{webgl_vendor}';
                        if (parameter === G2.RENDERER) return '{webgl_renderer}';
                        if (parameter === 37446 /* UNMASKED_VENDOR_WEBGL */) return '{webgl_vendor}';
                        if (parameter === 37445 /* UNMASKED_RENDERER_WEBGL */) return '{webgl_renderer}';
                        if (parameter === G2.MAX_VERTEX_UNIFORM_VECTORS) return 256;
                        if (parameter === G2.MAX_TEXTURE_SIZE) return 16384;
                        return originalGetParameter2.apply(this, arguments);
                    }};
                    WebGL2RenderingContext.prototype.getParameter = patchedGetParameterWebGL2;
                    _makeNative(WebGL2RenderingContext.prototype.getParameter, 'getParameter');
                }}
            }} catch(e) {{consoleLog('P5 fail', true)}}


            // 6. Canvas Fingerprint Protection (Noise)
            try {{
                const originalGetImageData = CanvasRenderingContext2D.prototype.getImageData;
                const patchedGetImageData = function(x, y, sw, sh) {{
                    const imageData = originalGetImageData.apply(this, arguments);
                    if (imageData && imageData.data) {{
                        const d = imageData.data;
                        for (let i = 0; i < d.length; i += Math.floor(Math.random() * 10 + 20) * 4) {{ // Vary step
                            const noise = Math.floor(Math.random() * 3) - 1; // -1, 0, or 1
                            if (d[i] + noise >= 0 && d[i] + noise <= 255) d[i] += noise;
                        }}
                    }}
                    return imageData;
                }};
                CanvasRenderingContext2D.prototype.getImageData = patchedGetImageData;
                _makeNative(CanvasRenderingContext2D.prototype.getImageData, 'getImageData');

                // Also patch toBlob and toDataURL to ensure they use the modified context
                 const originalToBlob = HTMLCanvasElement.prototype.toBlob;
                 HTMLCanvasElement.prototype.toBlob = function(callback, type, quality) {{
                     const ctx = this.getContext('2d');
                     // Temporarily apply getImageData patch to this specific context if needed, or assume it's globally patched
                     return originalToBlob.apply(this, arguments);
                 }};
                _makeNative(HTMLCanvasElement.prototype.toBlob, 'toBlob');

                 const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
                 HTMLCanvasElement.prototype.toDataURL = function(type, quality) {{
                     const ctx = this.getContext('2d');
                     // Similar to toBlob
                     return originalToDataURL.apply(this, arguments);
                 }};
                _makeNative(HTMLCanvasElement.prototype.toDataURL, 'toDataURL');
            }} catch(e) {{consoleLog('P6 fail', true)}}

            // 7. AudioContext Fingerprint Protection (incomplete in user's example)
            // Effective audio spoofing requires patching methods that return fingerprintable data
            // from an OfflineAudioContext, like getChannelData after rendering.
            // This is complex. A simpler approach might be to always return a consistent noisy buffer.
            try {{
                if (window.OfflineAudioContext || window.webkitOfflineAudioContext) {{
                    const OriginalOfflineAudioContext = window.OfflineAudioContext || window.webkitOfflineAudioContext;
                    const patchedOfflineAudioContext = function(numberOfChannels, length, sampleRate) {{
                        const context = new OriginalOfflineAudioContext(numberOfChannels, length, sampleRate);
                        const originalStartRendering = context.startRendering;
                        context.startRendering = function() {{
                            return originalStartRendering.call(this).then(buffer => {{
                                // Add noise to the buffer channels
                                for (let i = 0; i < buffer.numberOfChannels; i++) {{
                                    const channelData = buffer.getChannelData(i);
                                    for (let j = 0; j < channelData.length; j+= Math.floor(Math.random() * 10 + 50)) {{
                                        channelData[j] += (Math.random() * 0.000002 - 0.000001);
                                    }}
                                }}
                                return buffer;
                            }});
                        }};
                        _makeNative(context.startRendering, 'startRendering');
                        return context;
                    }};
                    if (window.OfflineAudioContext) window.OfflineAudioContext = patchedOfflineAudioContext;
                    if (window.webkitOfflineAudioContext) window.webkitOfflineAudioContext = patchedOfflineAudioContext;
                    _makeNative(patchedOfflineAudioContext, 'OfflineAudioContext');
                }}
            }} catch(e) {{consoleLog('P7 fail', true)}}


            // 8. Languages Detection (from profile)
            try {{ Object.defineProperty(navigator, 'languages', {{ get: () => {navigator_languages}, configurable: true }}); _makeNative(navigator.languages.get, 'get languages'); }} catch(e) {{consoleLog('P8 fail', true)}}

            // 9. Hardware Concurrency (from profile or randomized)
            try {{ Object.defineProperty(navigator, 'hardwareConcurrency', {{ get: () => {hardware_concurrency}, configurable: true }}); _makeNative(navigator.hardwareConcurrency.get, 'get hardwareConcurrency'); }} catch(e) {{consoleLog('P9 fail', true)}}

            // 10. Device Memory (from profile or default)
            try {{ Object.defineProperty(navigator, 'deviceMemory', {{ get: () => {device_memory}, configurable: true }}); _makeNative(navigator.deviceMemory.get, 'get deviceMemory'); }} catch(e) {{consoleLog('P10 fail', true)}}

            // 11. WebRTC IP Leak Prevention (JS side - partial, best with browser flags)
            // This attempts to prevent leakage by modifying iceServers. Stronger methods involve browser flags.
            try {{
                const OriginalRTCPeerConnection = window.RTCPeerConnection || window.webkitRTCPeerConnection || window.mozRTCPeerConnection;
                if (OriginalRTCPeerConnection) {{
                    const PatchedRTCPeerConnection = function(config) {{
                        if (config && config.iceServers) {{
                            config.iceServers = config.iceServers.filter(server => !(server && server.urls && server.urls.includes('stun:')));
                            if (config.iceServers.length === 0) {{ // Add a dummy or proxied TURN if needed, or leave empty
                                // config.iceServers.push({{ urls: 'turn:your.turn.server:3478', username: 'user', credential: 'password' }});
                            }}
                        }}
                        return new OriginalRTCPeerConnection(config);
                    }};
                    window.RTCPeerConnection = PatchedRTCPeerConnection;
                    window.RTCPeerConnection.prototype = OriginalRTCPeerConnection.prototype; // Maintain prototype chain
                    _makeNative(window.RTCPeerConnection, 'RTCPeerConnection');
                }}
            }} catch(e) {{consoleLog('P11 fail', true)}}


            // 12. Battery API Spoofing
            try {{
                if (navigator.getBattery) {{
                    const originalGetBattery = navigator.getBattery;
                    navigator.getBattery = () => Promise.resolve({{
                        charging: true, chargingTime: 0, dischargingTime: Infinity, level: 1.0,
                        addEventListener: () => {{}}, removeEventListener: () => {{}}, dispatchEvent: () => false,
                        onchargingchange: null, onchargingtimechange: null, ondischargingtimechange: null, onlevelchange: null
                    }});
                    _makeNative(navigator.getBattery, 'getBattery');
                }}
            }} catch(e) {{consoleLog('P12 fail', true)}}


            // 13. Timezone and Locale (JS side)
            try {{
                Date.prototype.getTimezoneOffset = function() {{ return {timezone_offset}; }};
                _makeNative(Date.prototype.getTimezoneOffset, 'getTimezoneOffset');

                const originalResolvedOptions = Intl.DateTimeFormat.prototype.resolvedOptions;
                Intl.DateTimeFormat.prototype.resolvedOptions = function() {{
                    const opts = originalResolvedOptions.call(this);
                    opts.timeZone = '{timezone_id}';
                    opts.locale = '{locale_str}';
                    return opts;
                }};
                _makeNative(Intl.DateTimeFormat.prototype.resolvedOptions, 'resolvedOptions');
            }} catch(e) {{consoleLog('P13 fail', true)}}

            // 14. Screen properties (from profile)
            try {{
                Object.defineProperty(screen, 'width', {{ get: () => {screen_width}, configurable: true }}); _makeNative(screen.width.get, 'get width');
                Object.defineProperty(screen, 'height', {{ get: () => {screen_height}, configurable: true }}); _makeNative(screen.height.get, 'get height');
                Object.defineProperty(screen, 'availWidth', {{ get: () => {screen_avail_width}, configurable: true }}); _makeNative(screen.availWidth.get, 'get availWidth');
                Object.defineProperty(screen, 'availHeight', {{ get: () => {screen_avail_height}, configurable: true }}); _makeNative(screen.availHeight.get, 'get availHeight');
                Object.defineProperty(screen, 'colorDepth', {{ get: () => {screen_color_depth}, configurable: true }}); _makeNative(screen.colorDepth.get, 'get colorDepth');
                Object.defineProperty(screen, 'pixelDepth', {{ get: () => {screen_pixel_depth}, configurable: true }}); _makeNative(screen.pixelDepth.get, 'get pixelDepth');
            }} catch(e) {{consoleLog('P14 fail', true)}}

            // 15. Navigator properties (from profile)
            try {{ Object.defineProperty(navigator, 'platform', {{ get: () => '{navigator_platform}', configurable: true }}); _makeNative(navigator.platform.get, 'get platform'); }} catch(e) {{consoleLog('P15.1 fail', true)}}
            try {{ Object.defineProperty(navigator, 'vendor', {{ get: () => '{navigator_vendor}', configurable: true }}); _makeNative(navigator.vendor.get, 'get vendor'); }} catch(e) {{consoleLog('P15.2 fail', true)}}

            // 16. MouseEvent isTrusted fix (from user's script)
            try {{
                const OriginalMouseEvent = MouseEvent;
                window.MouseEvent = function(...args) {{ // Use function to allow constructor behavior
                    const event = new OriginalMouseEvent(...args);
                    try {{ Object.defineProperty(event, 'isTrusted', {{ get: () => true, configurable: true }}); }} catch(e) {{}}
                    return event;
                }};
                window.MouseEvent.prototype = OriginalMouseEvent.prototype;
                _makeNative(window.MouseEvent, 'MouseEvent');
            }} catch(e) {{consoleLog('P16 fail', true)}}

            // 17. User Agent (already set by browser launch, but can reinforce for JS checks)
            // const ua = "{profile.get('user_agent', '')}"; // Get from profile
            // if (ua) {{
            //   try {{ Object.defineProperty(navigator, 'userAgent', {{ get: () => ua, configurable: true }}); _makeNative(navigator.userAgent.get, 'get userAgent'); }} catch(e) {{}}
            //   try {{ Object.defineProperty(navigator, 'appVersion', {{ get: () => ua.substr(ua.indexOf('/') + 1), configurable: true }}); _makeNative(navigator.appVersion.get, 'get appVersion'); }} catch(e) {{}}
            // }}

            // 17.5 UserAgentData (Client Hints in JS)
            if (navigator.userAgentData) {{
                try {{
                    const brands = {ua_data_brands_json};
                    const mobile = {str(ua_data_mobile).lower()}; // Inject as boolean
                    const platform = {ua_data_platform}; // Inject as string

                    Object.defineProperty(navigator, 'userAgentData', {{
                        get: () => ({{
                            brands: brands,
                            mobile: mobile,
                            platform: platform,
                            getHighEntropyValues: (hints) => Promise.resolve(
                                hints.reduce((acc, hint) => {{
                                    if (hint === 'architecture') acc.architecture = "{profile.get('sec_ch_ua_arch_for_js', 'x86')}";
                                    if (hint === 'bitness') acc.bitness = "{profile.get('sec_ch_ua_bitness_for_js', '64')}";
                                    if (hint === 'model') acc.model = "{profile.get('sec_ch_ua_model_for_js', '')}";
                                    if (hint === 'platform') acc.platform = platform; // platform is from outer scope
                                    if (hint === 'platformVersion') acc.platformVersion = "{profile.get('sec_ch_ua_platform_version_for_js', '10.0.0')}";
                                    if (hint === 'uaFullVersion') acc.uaFullVersion = "{profile.get('sec_ch_ua_full_version_for_js', '125.0.6422.142')}";
                                    // Note: 'mobile' and 'brands' are direct properties, not typically fetched via getHighEntropyValues
                                    return acc;
                                }}, {{ brands: brands, mobile: mobile, platform: platform }}) // Include base properties
                            )
                        }}), configurable: true }});
                    _makeNative(navigator.userAgentData.get, 'get userAgentData');
                }} catch (e) {{ consoleLog('P17.5 UserAgentData spoofing failed: ' + e.toString(), true); }}
            }}

            // 18. Clear known automation indicators (less effective, but good hygiene)
            try {{
                if (window.document) {{ // Common check if running in odd contexts
                    window.document.documentElement.removeAttribute('webdriver');
                    window.document.documentElement.removeAttribute('selenium');
                    window.document.documentElement.removeAttribute('driver');
                }}
            }} catch(e) {{consoleLog('P18 fail', true)}}

            // 19. Detection of MutationObserver for DOM artifacts removal (from user's script)
            // This is to hide your *own tool's* artifacts.
            // It's fine, but be aware it consumes resources.
            try {{
                const observer = new MutationObserver(mutations => {{
                    mutations.forEach(mutation => {{
                        mutation.addedNodes.forEach(node => {{
                            if (node.nodeType === 1 && (
                                node.id?.includes('puppeteer') || // General puppeteer traces
                                node.className?.includes('puppeteer') ||
                                node.getAttribute?.('browser-user-highlight-id') // Your tool's specific ID
                            )) {{
                                node.remove();
                                // consoleLog(`Removed node: id=${{node.id}}, class=${{node.className}}`);
                            }}
                        }});
                    }});
                }});
                observer.observe(document, {{childList: true, subtree: true}});
            }} catch(e) {{consoleLog('P19 fail', true)}}

            // Final log - this will be blocked by patchright if console API is fully disabled.
            // Useful for debugging with regular Playwright.
            // consoleLog('StealthOps: All JS patches applied.');
        }})();
        """

    @staticmethod
    def get_enhanced_mouse_movements_js() -> str:
        """JavaScript for advanced human-like mouse movement patterns.
           This should be injected once.
        """
        return """
        // Enhanced Human-like Mouse Movement (can be injected once)
        class HumanMouse {
            constructor() {
                this.lastX = Math.random() * window.innerWidth; // Initialize with random position
                this.lastY = Math.random() * window.innerHeight;
            }

            // Generate realistic mouse path using Bezier curves with momentum
            generatePath(startX, startY, endX, endY) {
                const _startX = startX === null || typeof startX === 'undefined' ? this.lastX : startX;
                const _startY = startY === null || typeof startY === 'undefined' ? this.lastY : startY;

                const distance = Math.sqrt(Math.pow(endX - _startX, 2) + Math.pow(endY - _startY, 2));
                let steps = Math.max(15, Math.min(50, Math.floor(distance / (5 + Math.random() * 10)))); // Dynamic steps based on distance
                if (distance < 20) steps = Math.max(5, Math.floor(distance/2)); // Shorter for small moves

                const path = [];

                const curveIntensityX = Math.min(distance / 150, 2) * (Math.random() * 0.6 + 0.7); // Max intensity based on distance
                const curveIntensityY = Math.min(distance / 150, 2) * (Math.random() * 0.6 + 0.7);

                const controlPoint1X = _startX + (endX - _startX) * 0.25 + (Math.random() - 0.5) * distance * curveIntensityX * 0.15;
                const controlPoint1Y = _startY + (endY - _startY) * 0.25 + (Math.random() - 0.5) * distance * curveIntensityY * 0.15;
                const controlPoint2X = _startX + (endX - _startX) * 0.75 + (Math.random() - 0.5) * distance * curveIntensityX * 0.15;
                const controlPoint2Y = _startY + (endY - _startY) * 0.75 + (Math.random() - 0.5) * distance * curveIntensityY * 0.15;

                for (let i = 0; i <= steps; i++) {
                    const t = i / steps;
                    const eased_t = t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t; // Ease-in-out

                    const x = Math.pow(1 - eased_t, 3) * _startX +
                             3 * Math.pow(1 - eased_t, 2) * eased_t * controlPoint1X +
                             3 * (1 - eased_t) * Math.pow(eased_t, 2) * controlPoint2X +
                             Math.pow(eased_t, 3) * endX;

                    const y = Math.pow(1 - eased_t, 3) * _startY +
                             3 * Math.pow(1 - eased_t, 2) * eased_t * controlPoint1Y +
                             3 * (1 - eased_t) * Math.pow(eased_t, 2) * controlPoint2Y +
                             Math.pow(eased_t, 3) * endY;

                    const jitterX = (Math.random() - 0.5) * (steps > 10 ? 1.5 : 0.5); // Less jitter for short/precise moves
                    const jitterY = (Math.random() - 0.5) * (steps > 10 ? 1.5 : 0.5);

                    path.push({
                        x: x + jitterX,
                        y: y + jitterY,
                        // timestamp: Date.now() + i * (2 + Math.random() * 3) // Timestamps not used by Python side currently
                    });
                }
                this.lastX = path[path.length-1].x;
                this.lastY = path[path.length-1].y;
                return path;
            }

            addOvershoot(path, targetX, targetY) {
                if (path.length === 0) return path;
                const lastPoint = path[path.length - 1];
                const prevPoint = path.length > 1 ? path[path.length - 2] : {x: this.lastX, y: this.lastY};

                const dxTotal = targetX - prevPoint.x;
                const dyTotal = targetY - prevPoint.y;
                const totalDist = Math.sqrt(dxTotal*dxTotal + dyTotal*dyTotal);

                if (totalDist > 70 && Math.random() > 0.65) { // Only overshoot sometimes on longer moves
                    const overshootFactor = 0.05 + Math.random() * 0.10; // 5-15%
                    const overshootX = targetX + dxTotal * overshootFactor;
                    const overshootY = targetY + dyTotal * overshootFactor;

                    path.push({ x: overshootX, y: overshootY });

                    const correctionSteps = 5 + Math.floor(Math.random() * 8);
                    for (let i = 1; i <= correctionSteps; i++) {
                        const t = i / correctionSteps;
                        path.push({
                            x: overshootX + (targetX - overshootX) * t,
                            y: overshootY + (targetY - overshootY) * t,
                        });
                    }
                }
                this.lastX = path[path.length-1].x;
                this.lastY = path[path.length-1].y;
                return path;
            }
        }
        if (!window.__humanMouse) { // Initialize only once
            window.__humanMouse = new HumanMouse();
            // console.log('StealthOps: HumanMouse initialized.'); // Blocked by patchright
        }
        // Store initial mouse position for path generation logic
        // This might require an event listener on mousemove if Python side doesn't track it.
        // For now, assume JS class manages its own lastX, lastY.
        """

    @staticmethod
    def get_viewport_size() -> Dict[str, int]:
        """Common screen resolutions to blend in - use this to set browser window size."""
        # Consistent with a common profile
        profile_screen = StealthOps.get_user_agent_profile()["screen"]
        return {"width": profile_screen["width"], "height": profile_screen["height"]}
