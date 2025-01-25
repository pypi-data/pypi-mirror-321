import os
from colorama import Fore, Style, init
from mymra import embed_file, extract_file, embed_string, extract_string, deembed_file, analyze_file

#
#    Password and marker arguments are always optional
#    If not passed, used marker is b'MQAZWERPASDZXW'
#    If not passed, used password is 'RAMRANCHREALLYROCKS'
#

init()

errors_occurred = False
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Example of embedding a file
try:
    embed_file(
        input_file_path='123.mp4',
        host_file_path='123.png',
        output_file_path='1488.png',
        password='COCKER',
        marker='ITSTEST'
    )
    print(f"{Fore.GREEN}Embedding a file - Successful{Style.RESET_ALL}")
except Exception as e:
    errors_occurred = True
    print(f"{Fore.RED}Embedding a file - Failed! Error: {e}{Style.RESET_ALL}")

# Example of extracting a file
try:
    file_path = extract_file(
        host_file_path='1488.png',
        password='COCKER',
        marker='ITSTEST'
    )
    print(f"{Fore.GREEN}Extracting a file - Successful: {file_path}{Style.RESET_ALL}")
except Exception as e:
    errors_occurred = True
    print(f"{Fore.RED}Extracting a file - Failed! Error: {e}{Style.RESET_ALL}")

# Example of embedding a string
try:
    embed_string(
        input_string='This is a secret string',
        host_file_path='123.png',
        output_file_path='string_embedded.png',
        password='COCKER',
        marker='ITSTEST'
    )
    print(f"{Fore.GREEN}Embedding a string - Successful{Style.RESET_ALL}")
except Exception as e:
    errors_occurred = True
    print(f"{Fore.RED}Embedding a string - Failed! Error: {e}{Style.RESET_ALL}")

# Example of extracting a string
try:
    result = extract_string(
        host_file_path='string_embedded.png',
        password='COCKER',
        marker='ITSTEST'
    )
    print(f"{Fore.GREEN}Extracting a string - Successful: {result}{Style.RESET_ALL}")
except Exception as e:
    errors_occurred = True
    print(f"{Fore.RED}Extracting a string - Failed! Error: {e}{Style.RESET_ALL}")

# Example of analyzing embedded file
try:
    analysis_result = analyze_file(
        host_file_path='1488.png',
        password='COCKER',
        marker='ITSTEST'
    )
    print(f"{Fore.GREEN}Analyzing embedded data - Successful: {analysis_result}{Style.RESET_ALL}")
except Exception as e:
    errors_occurred = True
    print(f"{Fore.RED}Analyzing embedded data - Failed! Error: {e}{Style.RESET_ALL}")

# Example of analyzing embedded string
try:
    analysis_result = analyze_file(
        host_file_path='string_embedded.png',
        password='COCKER',
        marker='ITSTEST'
    )
    print(f"{Fore.GREEN}Analyzing embedded data - Successful: {analysis_result}{Style.RESET_ALL}")
except Exception as e:
    errors_occurred = True
    print(f"{Fore.RED}Analyzing embedded data - Failed! Error: {e}{Style.RESET_ALL}")

# Example of removing embedded data
try:
    deembed_file(
        host_file_path='1488.png',
        output_file_path='cleaned_123.png',
        marker='ITSTEST'
    )
    print(f"{Fore.GREEN}Removing embedded data - Successful{Style.RESET_ALL}")
except Exception as e:
    errors_occurred = True
    print(f"{Fore.RED}Removing embedded data - Failed! Error: {e}{Style.RESET_ALL}")

try:
    os.remove('cleaned_123.png')
    os.remove('1488.png')
    os.remove('string_embedded.png')
except OSError as e:
    errors_occurred = True
    print(f"{Fore.YELLOW}Warning: {e}{Style.RESET_ALL}")

if errors_occurred:
    print(f"{Fore.RED}Errors occurred during execution{Style.RESET_ALL}")
    exit(1)  
else:
    print(f"{Fore.GREEN}Execution completed successfully{Style.RESET_ALL}")
    exit(0)
