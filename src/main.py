
import asyncio
from scraper import Scraper
from data_processor import DataProcessor
from model_utils import ModelUtils

async def main():
    # Specify the website URLs to scrape
    urls = [
        "https://www.example.com/tax-resources",
        "https://www.example.org/tax-faqs",
        # Add more URLs as needed
    ]

    # Initialize the scraper and data processor
    scraper = Scraper()
    data_processor = DataProcessor("models/mpt_7b_quantized")

    # Scrape and process the data
    all_qa_pairs = []
    for url in urls:
        content = await scraper.scrape_website(url)
        qa_pairs = data_processor.generate_qa_pairs(content)
        all_qa_pairs.extend(qa_pairs)

    # Save the Q&A pairs to a JSONL file
    ModelUtils.save_to_jsonl(all_qa_pairs, "data/scraped_data.jsonl")

    print("Data scraping and processing completed.")

if __name__ == "__main__":
    asyncio.run(main())
