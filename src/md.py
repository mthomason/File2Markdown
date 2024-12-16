# -*- coding: utf-8 -*-
#
# Copyright © Michael Thomason 2024.  All rights reserved.
#

import argparse
import os
from markitdown import MarkItDown

import argparse
import os
from markitdown import MarkItDown

def convert_file_to_markdown(file_path: str):
	"""
	Converts a file to Markdown using the MarkItDown library.

	Args:
		file_path (str): Path to the file to be converted.

	Returns:
		str: The converted Markdown content.

	Raises:
		FileNotFoundError: If the specified file does not exist.
		ValueError: If the file format is unsupported.
	"""
	if not os.path.exists(file_path):
		raise FileNotFoundError(f"The file '{file_path}' does not exist.")

	# Initialize the MarkItDown converter
	markitdown = MarkItDown()

	# Attempt to convert the file to Markdown
	try:
		result = markitdown.convert_local(path=file_path)
		return result.text_content
	except Exception as e:
		raise ValueError(f"Failed to convert '{file_path}' to Markdown. Error: {str(e)}")

def save_markdown_to_file(markdown_content: str, output_path: str):
	"""
	Saves the Markdown content to a file.

	Args:
		markdown_content (str): The Markdown content to save.
		output_path (str): Path to the output Markdown file.

	Raises:
		IOError: If there is an error writing to the file.
	"""
	try:
		with open(output_path, 'w', encoding='utf-8') as output_file:
			output_file.write(markdown_content)
	except IOError as e:
		raise IOError(f"Failed to save Markdown to '{output_path}'. Error: {str(e)}")

def main():
	"""
	Main function to parse command-line arguments and process the file.
	"""
	# Set up the argument parser
	parser = argparse.ArgumentParser(
		description="File2Markdown: A tool to convert various file formats to Markdown using the MarkItDown library."
	)
	parser.add_argument(
		"--file",
		type=str,
		required=True,
		help="Path to the file to be converted to Markdown."
	)
	parser.add_argument(
		"--output",
		type=str,
		required=False,
		help="Path to save the converted Markdown content. If not specified, the output will be printed to the console."
	)

	# Parse the command-line arguments
	args = parser.parse_args()

	# Extract the file path and output path from the arguments
	file_path = args.file
	output_path = args.output

	# Process the file and handle the Markdown content
	try:
		markdown_content = convert_file_to_markdown(file_path)

		if output_path:
			save_markdown_to_file(markdown_content, output_path)
			print(f"Markdown content successfully saved to '{output_path}'.")
		else:
			print("\nConverted Markdown Content:\n")
			print(markdown_content)
	except FileNotFoundError as fnf_error:
		print(f"Error: {fnf_error}")
	except ValueError as val_error:
		print(f"Error: {val_error}")
	except IOError as io_error:
		print(f"Error: {io_error}")
	except Exception as generic_error:
		print(f"An unexpected error occurred: {generic_error}")

if __name__ == "__main__":
	main()
