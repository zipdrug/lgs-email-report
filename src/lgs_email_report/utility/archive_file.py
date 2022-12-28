import boto3
import logging
from botocore.exceptions import ClientError
import os


def upload_to_s3(file_name, bucket, object_name):
    """
    :param file_name:
    :param bucket:
    :param object_name:
    :return:
    """
    s3_client = boto3.client("s3")

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print("S3 Upload Successful")

    except ClientError as e:
        logging.error(e)
        return False

    return True


if __name__ == "__main__":
    upload_to_s3(file_name="aloha_members_req_columns.csv", bucket="testbucketzd2")
