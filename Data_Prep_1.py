## this file is responsible for the connection of the csv files. 


import pandas as pd

def load_mapping(file_path, index_col):
    """Load mapping files with given index."""
    return pd.read_csv(file_path).set_index(index_col)

def process_chunk(chunk, partner_mapping, product_mapping):
    """Merge chunk with mappings."""
    # Merge with partner names
    chunk = chunk.merge(partner_mapping, on='Partner', how='left')
    # Merge with product descriptions
    chunk = chunk.merge(product_mapping, on='L3', how='left')
    return chunk

def main():
    # Load the partner and product mapping files
    partner_mapping = load_mapping('/Users/selma/Downloads/tradeconnectivity/other_economy.csv', 'Partner')
    product_mapping = load_mapping('/Users/selma/Downloads/tradeconnectivity/products.csv', 'L3')
    
    # Define the path for the main data file and output file
    input_file = '/Users/selma/Downloads/tradeconnectivity/data.csv'
    output_file = '/Users/selma/Downloads/tradeconnectivity/merged_data.csv'
    
    # Use a chunk size appropriate for your memory constraints
    chunk_size = 50000  # Adjust this number based on your system's memory
    
    # Read the main file in chunks
    reader = pd.read_csv(input_file, chunksize=chunk_size)
    
    for i, chunk in enumerate(reader):
        processed_chunk = process_chunk(chunk, partner_mapping, product_mapping)
        
        # Write processed chunk to output file
        mode = 'w' if i == 0 else 'a'
        header = True if i == 0 else False
        processed_chunk.to_csv(output_file, mode=mode, header=header, index=False)
        
        print(f'Processed chunk {i+1}')
    
    print('All data has been processed and written to the output file.')

if __name__ == "__main__":
    main()
