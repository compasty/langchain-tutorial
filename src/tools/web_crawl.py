import os
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

load_dotenv(override=True)
app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))

