import sys

def error_invalid_usage():
    print("Invalid usage!")
    sys.exit(1)

"""
# Old functions - previous REPO - FIXME

def error_unknown(exception):
    print("Caught Exception - {}".format(exception))
    sys.exit(exception)

def error_invalid_path(path):
    error_msg = "Unable to open path - {}".format(path)
    print_usage_message()
    sys.exit(error_msg)

def error_output_file_exists(path):
    error_msg = "Unable to write to path {} - file already exists, and the --force flag was not given".format(path)
    print(error_msg)
    print_usage_message()
    sys.exit(1)

def error_invalid_option(option):
    error_msg = "Invalid option '{}'".format(option)
    print(error_msg)
    print_usage_message()
    sys.exit(1)

def print_usage_message():
    ""
    Print usage message and exit
    ""
    msg = "Usage: {} <input.yaml> [-o <output.json>] [--force]".format(sys.argv[0])
    print(msg)

def main(input_path, output_path=None, force_overwrite=None):
    output = yaml_file_to_json(input_file)
    if not output_path:
        print(output)
    else:
        write_output_file(output, output_path, force_overwrite=force_overwrite)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage_message()

    input_file = sys.argv[1]
    output_file = None
    force_overwrite = False

    if len(sys.argv) >= 4:
        if sys.argv[2] == '-o':
            output_file = sys.argv[3]
        else:
            error_invalid_option(sys.argv[2])

    if len(sys.argv) == 5:
        if sys.argv[4] == '--force' or sys.argv[4] == '-f':
            force_overwrite = True
        else:
            error_invalid_option(sys.argv[2])

    main(input_file, output_path=output_file, force_overwrite=force_overwrite)
    sys.exit()
"""
