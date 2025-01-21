import asyncio
from scraper import Scraper
from data_processor import DataProcessor
from model_utils import ModelUtils

async def main():
    # Specify the base URL to start scraping from
    base_url = "https://www.example.com/tax-resources"

    # Download the model
    model_name = "EleutherAI/gpt-neo-1.3B"
    ModelUtils.download_model(model_name)

    # Initialize the scraper and data processor
    scraper = Scraper(base_url)
    data_processor = DataProcessor(model_name)

    # Scrape and process the data
    all_qa_pairs = []
    content = await scraper.scrape_website(base_url)
    qa_pairs = data_processor.generate_qa_pairs(content)
    all_qa_pairs.extend(qa_pairs)

    # Save the Q&A pairs to a JSONL file
    ModelUtils.save_to_jsonl(all_qa_pairs, "data/scraped_data.jsonl")

    print("Data scraping and processing completed.")

if __name__ == "__main__":
    asyncio.run(main())
