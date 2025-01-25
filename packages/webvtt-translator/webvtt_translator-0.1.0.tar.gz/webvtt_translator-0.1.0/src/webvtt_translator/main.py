import openai
import os
import argparse
import sys
import re

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    print("Error: The environment variable 'OPENAI_API_KEY' is not set.")
    sys.exit(1)

def translate_text(text, target_language):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are a dutiful translator. Translate all the following text to {target_language}:\n\n"},
            {"role": "user", "content": f"{text}"}
        ],
        max_tokens=1000
    )
    return response.choices[0].message.content.strip()

def main():
    parser = argparse.ArgumentParser(description='Translate WebVTT files using OpenAI.')
    parser.add_argument('-i', '--input', required=True, help='Path to the input VTT file')
    parser.add_argument('-o', '--output', required=True, help='Path to the output VTT file')
    parser.add_argument('-l', '--language', required=True, help='Target language for translation')

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output
    target_language = args.language

    # client from OpenAI API
    global client
    client = openai.OpenAI()

    # Regular expressions to match special types of line in the vtt
    header_re = re.compile(r'^WEBVTT')
    empty_line_re = re.compile(r'^\s*$')
    id_line_re = re.compile(r'^[0-9a-fA-F]{8}[0-9a-fA-F\-]+')
    timestamp_re = re.compile(r'^\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}')

    with open(input_file, 'r', encoding='utf-8') as infd:
        with open(output_file, 'w', encoding='utf-8') as outfd:
            while line := infd.readline():
                if header_re.match(line) or empty_line_re.match(line) or id_line_re.match(line) or timestamp_re.match(line):
                    outfd.write(line)
                    continue
                else:
                    translated_text = translate_text(line, target_language)
                    outfd.write(f'{translated_text}\n')
    print(f"Translation completed. Translated content written to {output_file}.")

    # Close the client connection to OpenAI
    client.close()

if __name__ == "__main__":
    main()