# First cell in the notebook
"""
# Install the required packages
!pip install requests tenacity python-dotenv
"""

# Second cell in the notebook
"""
# load your .env file to colab environment or set the environment variables manually (not recommended)
# import os
# 
# ATTACKIQ_PLATFORM_URL= os.environ["ATTACKIQ_PLATFORM_URL"] = "https://firedrill.attackiq.com"
# ATTACKIQ_API_TOKEN = os.environ["ATTACKIQ_API_TOKEN"] = "your_token_here"
"""
import itertools  # noqa: F401, E402
import os  # noqa: F401, E402
import sys  # noqa: F401, E402
import time  # noqa: F401, E402
from datetime import datetime, timedelta  # noqa: F401, E402
from typing import Optional, Dict, Any, List  # noqa: F401, E402

from dotenv import load_dotenv  # noqa: E402

load_dotenv()

ATTACKIQ_PLATFORM_URL = os.environ.get(
    "ATTACKIQ_PLATFORM_URL", "https://firedrill.attackiq.com"
)
if not ATTACKIQ_PLATFORM_URL:
    print("Error: ATTACKIQ_PLATFORM_URL environment variable is not set.")
    sys.exit(1)

ATTACKIQ_API_TOKEN = os.environ.get("ATTACKIQ_API_TOKEN")
if not ATTACKIQ_API_TOKEN:
    print("Error: ATTACKIQ_API_TOKEN environment variable is not set.")
    sys.exit(1)
