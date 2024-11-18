# -*- coding: utf-8 -*-
import sys
import win32print
import win32api
import chardet


def detect_encoding(file_path):
    """Detect file encoding"""
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        detected = chardet.detect(raw_data)
        return detected['encoding'], raw_data


def set_default_printer(printer_name):
    """Set the default printer"""
    try:
        win32print.SetDefaultPrinter(printer_name)
        print(f"Successfully set the default printer to: {printer_name}")
    except Exception as e:
        print(f"Failed to set the default printer: {e}")


def print_file_to_default_printer(file_path):
    """
    Print a file to the current default printer
    :param file_path: File path
    """
    try:
        # Open the file with the default program and print
        win32api.ShellExecute(0, "print", file_path, None, ".", 0)
        print(f"The file has been sent to the current default printer")
    except Exception as e:
        print(f"Failed to print the file: {e}")


def reset_default_printer(original_printer):
    """Restore the default printer"""
    set_default_printer(original_printer)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <file_path> <printer_name>")
        sys.exit(1)

    # Get file path and printer name
    file_path = sys.argv[1]
    printer_name = sys.argv[2]

    # Get the current default printer
    original_printer = win32print.GetDefaultPrinter()
    print(f"Current default printer: {original_printer}")

    # Switch default printer
    print(f"Switching default printer to: {printer_name}")
    set_default_printer(printer_name)

    # Get the new default printer
    new_default_printer = win32print.GetDefaultPrinter()
    print(f"New default printer: {new_default_printer}")

    # Verify if the switch was successful
    if new_default_printer == printer_name:
        print("Default printer switched successfully")
    else:
        print("Failed to switch the default printer. Please check.")

    # Print the file
    print_file_to_default_printer(file_path)