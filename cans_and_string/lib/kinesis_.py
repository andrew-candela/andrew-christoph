import boto3
import os
import time


class KinesisClient():
    def __init__(self):
        self.kn = boto3.client('kinesis', region_name='us-west-2')
        self.stream_name = 'CansAndString'

    def _put_record(self, message):
        self.kn.put_record(
            StreamName=self.stream_name,
            Data=message.encode(),
            PartitionKey='1',
        )
    
    def _get_shard_iterator(self):
        shards = self.kn.list_shards(
            StreamName=self.stream_name
        )
        # I'm hardcoding the first ShardID here. 
        # If we ever have 2 shards this won't work anymore
        shard_id = shards['Shards'][0]['ShardId']

        shard_iterator_response = self.kn.get_shard_iterator(
            StreamName=self.stream_name,
            ShardId=shard_id,
            ShardIteratorType='LATEST'
        )
        return shard_iterator_response['ShardIterator']

    def writer(self):
        print("Hello! What would you like to say to everyone listening?")
        prompt = ""
        while True:
            try:
                message = input(prompt)
                print("got it! I'll write that to the stream!")
                self._put_record(message)
                prompt = "Anything else you want to say?...   "
            except KeyboardInterrupt:
                print("\nGoodbye!\n")
                break
            except Exception as e:
                raise(e)
    
    def listener(self):
        print("beginning to listen for messages...")
        shard_iterator = self._get_shard_iterator()
        while True:
            try:
                resp = self.kn.get_records(ShardIterator=shard_iterator)
                for record in resp['Records']:
                    print(record['Data'].decode())
                    yield record['Data'].decode()
                shard_iterator = resp['NextShardIterator']
                time.sleep(1)
            except KeyboardInterrupt:
                print("\nGoodbye!\n")
                break
            except Exception as e:
                raise(e)
