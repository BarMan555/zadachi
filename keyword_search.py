import multiprocessing
import sys

def search_keyword(keyword, filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            if keyword in line:
                print(f"Found '{keyword}' in file: {filename}")
                return

if __name__ == "__main__":
    # Get the keyword and list of file names from command-line arguments
    keyword = sys.argv[1]
    filenames = sys.argv[2:]
  
    # Create a multiprocessing Pool with the number of processes equal to the number of files
    pool = multiprocessing.Pool(processes=len(filenames))
    
    # Use the pool.starmap function to parallelize the search_keyword function on each (keyword, filename) pair
    pool.starmap(search_keyword, [(keyword, filename) for filename in filenames])
    
    # Close the pool to free resources
    pool.close()
    pool.join()
