import xml.etree.ElementTree as ET
import csv
import argparse
import requests

def get_scryfall_id(catid):
    """
    Fetch the Scryfall ID corresponding to a given CatID from the Scryfall API.
    
    Args:
        catid (str): The CatID of the card to look up.
    
    Returns:
        str: The corresponding Scryfall ID, or None if not found.
    """
    response = requests.get(f'https://api.scryfall.com/cards/search?q=mtgoid:{catid}')
    
    if response.status_code == 200:
        data = response.json()
        # Check if cards were found
        if data['total_cards'] > 0:
            print(f"Response for {catid}: {data['data'][0]['name']}")
            return data['data'][0]['id']  # Return the Scryfall ID of the first card found
    print(f"Scryfall does not response to MTGO ID {catid}")
    return None

def parse_xml(xml_file):
    """
    Parse the XML file and extract the name, quantity, and CatID of each card.
    
    Args:
        xml_file (str): The path to the XML file.
    
    Returns:
        list: A list of tuples, where each tuple contains (quantity, name, scryfall_id).
    """
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Get all the Cards elements
    cards = root.findall('.//Cards')
    
    # Initialize an empty list to store the card data
    card_data = []
    
    # Iterate over each card
    for card in cards:
        # Read quantity, name, and CatID
        quantity = int(card.attrib.get('Quantity'))
        name = card.attrib.get('Name')
        catid = card.attrib.get('CatID')
        
        # Fetch the corresponding Scryfall ID
        scryfall_id = get_scryfall_id(catid)
        
        # Add the data to the list
        card_data.append((quantity, name, scryfall_id))
    
    return card_data

def write_to_csv(card_data, csv_file):
    """
    Write the card data to a CSV file using space as the separator.
    
    Args:
        card_data (list): A list of tuples, where each tuple contains (quantity, name, scryfall_id).
        csv_file (str): The path to the CSV file.
    """
    # Open the CSV file for writing
    with open(csv_file, 'w', newline='') as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile, delimiter=' ')  # Set space as the delimiter
        
        # Write the header
        writer.writerow(['Quantity', 'Name', 'Scryfall_ID'])
        
        # Write each card
        for quantity, name, scryfall_id in card_data:
            writer.writerow([quantity, name, scryfall_id])

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert XML file of Magic: The Gathering cards to CSV.')
    parser.add_argument('xml_file', type=str, help='Path to the XML file containing the card data.')
    parser.add_argument('csv_file', type=str, help='Path to the output CSV file.')

    # Parse command line arguments
    args = parser.parse_args()

    # Parse the XML file
    card_data = parse_xml(args.xml_file)
    
    # Write the card data to the CSV file
    write_to_csv(card_data, args.csv_file)

if __name__ == "__main__":
    main()