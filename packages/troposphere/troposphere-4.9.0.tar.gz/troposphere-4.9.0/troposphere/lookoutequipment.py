# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import integer


class InputNameConfiguration(AWSProperty):
    """
    `InputNameConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-inputnameconfiguration.html>`__
    """

    props: PropsDictType = {
        "ComponentTimestampDelimiter": (str, False),
        "TimestampFormat": (str, False),
    }


class S3InputConfiguration(AWSProperty):
    """
    `S3InputConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-s3inputconfiguration.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "Prefix": (str, False),
    }


class DataInputConfiguration(AWSProperty):
    """
    `DataInputConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-datainputconfiguration.html>`__
    """

    props: PropsDictType = {
        "InferenceInputNameConfiguration": (InputNameConfiguration, False),
        "InputTimeZoneOffset": (str, False),
        "S3InputConfiguration": (S3InputConfiguration, True),
    }


class S3OutputConfiguration(AWSProperty):
    """
    `S3OutputConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-s3outputconfiguration.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "Prefix": (str, False),
    }


class DataOutputConfiguration(AWSProperty):
    """
    `DataOutputConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
        "S3OutputConfiguration": (S3OutputConfiguration, True),
    }


class InferenceScheduler(AWSObject):
    """
    `InferenceScheduler <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html>`__
    """

    resource_type = "AWS::LookoutEquipment::InferenceScheduler"

    props: PropsDictType = {
        "DataDelayOffsetInMinutes": (integer, False),
        "DataInputConfiguration": (DataInputConfiguration, True),
        "DataOutputConfiguration": (DataOutputConfiguration, True),
        "DataUploadFrequency": (str, True),
        "InferenceSchedulerName": (str, False),
        "ModelName": (str, True),
        "RoleArn": (str, True),
        "ServerSideKmsKeyId": (str, False),
        "Tags": (Tags, False),
    }
