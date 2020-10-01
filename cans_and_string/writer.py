from cans_and_string.lib import kinesis_

def main_function():
    streamer = kinesis_.KinesisClient()
    streamer.writer()

if __name__ == "__main__":
    main_function()