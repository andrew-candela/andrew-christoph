resource "aws_kinesis_stream" "test_stream" {
  name             = "CansAndString"
  shard_count      = 1
  retention_period = 24

  shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
  ]

  tags = {
    Application = "Andrew-Christoph"
  }
}

resource "aws_iam_policy" "MessangerPolicy" {
  name        = "KinesisMessanger"
  path        = "/KinesisMessanger/"
  description = "Read and Write access for Kinesis Messanger stream"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "kinesis:GetShardIterator",
        "kinesis:GetRecords",
        "kinesis:DescribeStream",
        "kinesis:ListShards",
        "kinesis:PutRecord",
        "kinesis:PutRecords",
        "kinesis:SubscribeToShard"
      ],
      "Effect": "Allow",
      "Resource": "${aws_kinesis_stream.test_stream.arn}"
    }
  ]
}
EOF
}

resource "aws_iam_user" "kinesisMessanger" {
  name = "kinesisMessanger"
  path = "/KinesisMessanger/"

  tags = {
    Application = "Andrew-Christoph"
  }
}

resource "aws_iam_user_policy_attachment" "kinesisMessanger" {
  user       = aws_iam_user.kinesisMessanger.name
  policy_arn = aws_iam_policy.MessangerPolicy.arn
}
