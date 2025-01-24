import argparse
import subprocess


def aal():
    parser = argparse.ArgumentParser(description='AAL: Auto Assembly Linker - A tool to link assembly files')

    # Positional argument: object_file (always required)
    parser.add_argument("object_file", type=str, help="The object file to link")

    # Required optional argument: -o / --output
    parser.add_argument("-o", "--output", required=True, type=str, help="The output file name")

    # Optional argument: -s / --starter-func
    parser.add_argument("-s", "--starter-func", default="_start", type=str, help="The function to start execution from")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Generate the command
    sdk_path = subprocess.check_output(["xcrun", "-sdk", "macosx", "--show-sdk-path"], text=True).strip()

    command = [
        "ld",
        args.object_file,
        "-o", args.output,
        "-l", "System",
        "-syslibroot", sdk_path,
        "-e", args.starter_func,
        "-arch", "arm64"
    ]

    # Execute the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to link object file. {e}")
        exit(1)
    except FileNotFoundError:
        print("Error: The 'ld' command is not available. Please ensure it is installed and accessible.")
        exit(1)


if __name__ == '__main__':
    aal()
