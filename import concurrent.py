import concurrent.futures
import sys

def search_keyword(keyword, filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            if keyword in line:
                print(f"Found '{keyword}' in file: {filename}")
                return

if __name__ == "__main__":
    keyword = sys.argv[1]
    filenames = sys.argv[2:]
  
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(filenames)) as executor:
        futures = [executor.submit(search_keyword, keyword, filename) for filename in filenames]
        concurrent.futures.wait(futures)
