import os
import time
import argparse

def display_banner():
    GREEN_COLOR = "\033[92m"
    RESET_COLOR = "\033[0m"
    banner = f"""
    {GREEN_COLOR}#      ⛏️  Ooli: APK Data Scanning
    #      💎  Extracting treasures from the code!
    #      🛠️  Author: Jina{RESET_COLOR}
    """
    print(banner)

def search_in_smali_files(directory_path, keyword):
    if not os.path.isdir(directory_path):
        print(f"Invalid directory path: {directory_path}")
        return

    print(f"Searching for keyword '{keyword}' in Smali files under '{directory_path}'...")

    found_any = False
    results = []
    smali_files = []
    keyword_count = 0

    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(".smali"):
                smali_files.append(os.path.join(root, file_name))

    total_files = len(smali_files)
    print(f"Total files to process: {total_files}")

    start_time = time.time()

    for index, file_path in enumerate(smali_files, start=1):
        elapsed_time = time.time() - start_time
        estimated_total_time = (elapsed_time / index) * total_files if index > 0 else 0
        remaining_time = estimated_total_time - elapsed_time

        status_message = (f"Processing file {index}/{total_files} | Elapsed: {elapsed_time:.2f}s | "
                          f"Estimated total: {estimated_total_time:.2f}s | Remaining: {remaining_time:.2f}s")
        print(f"\r{status_message}", end="")

        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if keyword in line:
                    found_any = True
                    keyword_count += 1
                    highlighted_line = line.replace(keyword, f"\033[5;91m{keyword}\033[0m")
                    results.append(f"[ {file_path} ] [ (Line {line_number}): {highlighted_line.strip()} ]")

    print("\nProcessing completed.")

    if found_any:
        print("\nResults:")
        for result in results:
            print(result)
        print(f"\nThe keyword '{keyword}' was found {keyword_count} time(s) in total.")
    else:
        print(f"No occurrences of '{keyword}' were found in the specified directory.")

def main():
    try:
        display_banner()
        parser = argparse.ArgumentParser(description="Search for a keyword in Smali files.")
        parser.add_argument("-p", "--path", type=str, required=True, help="Path to the directory containing Smali files.")
        parser.add_argument("-k", "--keyword", type=str, required=True, help="Keyword to search for.")
        args = parser.parse_args()

        search_in_smali_files(args.path, args.keyword)
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user. Exiting...")

if __name__ == "__main__":
    main()
