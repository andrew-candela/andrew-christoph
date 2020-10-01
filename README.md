# andrew-christoph
Let's build a python project! 
We want to build an app that allows one of us to type something
and that will play on the other person's computer.

There will be a few things we'll have to set up to make this work.

- a message stream ([AWS Kinesis](https://aws.amazon.com/kinesis/)).
- a listener (Python script)
- a writer (Python script)

The idea will be that you can run the writer script to send messages 
to the stream. 
If you are running the listener script then whatever was just 
written will be played on your computer with the `say` command.

# Message Stream
We will use terraform to manage all of our Amazon Web Services infra.
Don't worry about this stuff too much right now.
If you're interested, AWS offers a ton of internet grade products
that many large companies (like Netflix for example) use extensively.
AWS is great.

# Authentication
You'll need to authenticate to AWS in order to listen to messages sent to the stream.
We will be using a `.env` file to store our credentials. 
Keep these credentials secret! 
If someone gets them then they could use my AWS account and I'd have to pay for it.

# Cans And String
The package we'll be working out of is called `cans_and_string`.
It has files for listening and for writing.
If we want to listen to messages from the stream, we can invoke the listener like this:
```
python cans_and_string/listener.py
```
The writer can be run similarly.