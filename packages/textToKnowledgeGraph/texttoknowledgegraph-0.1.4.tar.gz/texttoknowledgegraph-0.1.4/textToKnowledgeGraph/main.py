import sys
import re
import argparse
import logging
from ndex2.client import Ndex2
from .convert_to_cx2 import convert_to_cx2
from .pub import get_pubtator_paragraphs, download_pubtator_xml
from .sentence_level_extraction import llm_bel_processing
from .indra_download_extract import save_to_json, setup_output_directory
from .transform_bel_statements import process_llm_results


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def validate_pmc_id(pmc_id):
    pattern = r'^PMC\d+$'
    if not re.match(pattern, pmc_id):
        raise ValueError("Invalid PMC ID format. It should start with 'PMC' followed by digits.")


def process_paper(pmc_id, api_key, ndex_email=None, ndex_password=None, upload_to_ndex=False):
    """
    Process a single PMC ID to generate BEL statements and CX2 network.

    Args:
        api_key(str): OpenAI API key for processing.
        pmc_id (str): The PubMed Central ID of the article to process.
        ndex_email (str): The NDEx email for authentication.
        ndex_password (str): The NDEx password for authentication.

    Returns:
        bool: True if processing succeeds, False otherwise.
    """
    try:
        validate_pmc_id(pmc_id)
        logging.info(f"Setting up output directory for {pmc_id}")
        output_dir = setup_output_directory(pmc_id)

        file_path = download_pubtator_xml(pmc_id, output_dir)
        if not file_path:
            logging.error("Aborting process due to download failure.")
            return

        logging.info("Processing xml file to get text paragraphs")
        paragraphs = get_pubtator_paragraphs(file_path)
        paragraphs_filename = f"{pmc_id}_pub_paragraphs.json"
        save_to_json(paragraphs, paragraphs_filename, output_dir)

        logging.info("Processing paragraphs with LLM-BEL model")
        llm_results = llm_bel_processing(paragraphs, api_key)
        llm_filename = 'llm_results.json'
        save_to_json(llm_results, llm_filename, output_dir)

        logging.info("Processing LLM results to generate CX2 network")
        extracted_results = process_llm_results(llm_results)
        cx2_network = convert_to_cx2(extracted_results)
        cx2_filename = 'cx2_network.cx'
        save_to_json(cx2_network.to_cx2(), cx2_filename, output_dir)

        if upload_to_ndex:
            if not ndex_email or not ndex_password:
                logging.error("NDEx email and password are required to upload.")
                return False
            logging.info("Saving cx2 network to NDEx")
            client = Ndex2(username=ndex_email, password=ndex_password)
            client.save_new_cx2_network(cx2_network.to_cx2())

        logging.info(f"Processing completed successfully for {pmc_id}.")
        return True

    except ValueError as ve:
        logging.error(ve)
        sys.exit(1)
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)
        return False


def main(pmc_ids, api_key, ndex_email, ndex_password, upload_to_ndex=False):
    """
    Main function to process a list of PMC IDs.

    Args:
        pmc_ids (list of str): A list of PubMed Central IDs to process.
        api_key (str): OpenAI API key for processing.
        ndex_email (str): The NDEx email for authentication.
        ndex_password (str): The NDEx password for authentication.
        upload_to_ndex (bool): Whether to upload the generated network to NDEx.
    """
    success_count = 0
    failure_count = 0

    for pmc_id in pmc_ids:
        logging.info(f"Starting processing for PMC ID: {pmc_id}")
        if process_paper(pmc_id, api_key, ndex_email, ndex_password, upload_to_ndex):
            success_count += 1
        else:
            failure_count += 1

    logging.info(f"Processing completed. Success: {success_count}, Failures: {failure_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a list of PMC articles and extract interaction data.")
    parser.add_argument(
        "--api_key",
        type=str,
        required=True,  # Defaults to None if no key is provided
        help="OpenAI API key for processing"
    )
    parser.add_argument(
        "--pmc_ids",
        type=str,
        required=True,  # Allows multiple arguments to be passed as a list
        help="PubMed Central IDs of the articles to process (space-separated)."
    )
    parser.add_argument(
        "--ndex_email",
        type=str,
        required=False,
        help="NDEx account email for authentication."
    )
    parser.add_argument(
        "--ndex_password",
        type=str,
        required=False,
        help="NDEx account password for authentication."
    )
    parser.add_argument(
        "--upload_to_ndex",
        action="store_true", 
        help="Set this flag to upload the network to NDEx."
    )  
    args = parser.parse_args()

    main(args.pmc_ids, args.ndex_email, args.ndex_password, args.style_path)
