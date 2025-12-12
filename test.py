import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_chrome():
    """Initialize Chrome driver with proper session handling"""
    
    # Get absolute path for session
    session_dir = os.path.abspath("whatsapp_session")
    
    # Create directory if it doesn't exist
    if not os.path.exists(session_dir):
        os.makedirs(session_dir)
        print(f"✓ Created session directory: {session_dir}")
    
    print(f"\n🔧 Initializing Chrome driver...")
    print(f"📁 Session directory: {session_dir}")
    
    # Chrome options
    options = webdriver.ChromeOptions()
    
    # Session directory
    options.add_argument(f"--user-data-dir={session_dir}")
    
    # Anti-detection
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-extensions")
    
    # Exclude automation flags
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        print("✓ Chrome driver initialized successfully!")
        return driver
        
    except Exception as e:
        print(f"❌ Error initializing Chrome: {e}")
        return None

# Use the function
driver = initialize_chrome()

if driver:
    print("\n🌐 Opening WhatsApp Web...")
    driver.get("https://web.whatsapp.com")
    
    print("\n📱 Scan QR code if this is first time...")
    print("⏳ Waiting for WhatsApp to load...")
    
    # Wait for WhatsApp to load
    time.sleep(15)
    
    print("✓ Ready!")
else:
    print("Failed to start Chrome driver")