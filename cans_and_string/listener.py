from cans_and_string.lib import kinesis_
import os

def string_speaker(string_to_speak):
    return os.system(f"say {string_to_speak}")

def main_function():
    streamer = kinesis_.KinesisClient()
    for record in streamer.listener():
        string_speaker(record)

if __name__ == "__main__":
    main_function()