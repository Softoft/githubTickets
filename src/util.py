import os
import time


def new_output_file(_output_file):
    with open(_output_file, 'w') as f:
        f.write("")


def join_files_in_directory(_directory_path, _output_file):
    files = [f for f in os.listdir(_directory_path) if os.path.isfile(os.path.join(_directory_path, f))]

    with open(_output_file, 'a') as outfile:
        for filename in files:
            file_path = os.path.join(_directory_path, filename)
            with open(file_path) as infile:
                outfile.write(f"File {filename}\n")
                outfile.write("content\n")
                outfile.write(infile.read())
                outfile.write("\n\n")


def create_ai_summary():
    directory_path1 = "github_tickets"
    directory_path2 = "../tests"
    output_file = "joined_output.txt"
    new_output_file(output_file)
    join_files_in_directory(directory_path1, output_file)
    join_files_in_directory(directory_path2, output_file)

    print(f"All files have been joined into {output_file}")


if __name__ == "__main__":
    while True:
        create_ai_summary()
        time.sleep(10)
