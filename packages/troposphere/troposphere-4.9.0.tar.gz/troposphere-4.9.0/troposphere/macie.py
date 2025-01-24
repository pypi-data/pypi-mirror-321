# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import integer
from .validators.macie import (
    findingsfilter_action,
    session_findingpublishingfrequency,
    session_status,
)


class S3WordsList(AWSProperty):
    """
    `S3WordsList <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-s3wordslist.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
        "ObjectKey": (str, True),
    }


class Criteria(AWSProperty):
    """
    `Criteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-criteria.html>`__
    """

    props: PropsDictType = {
        "Regex": (str, False),
        "S3WordsList": (S3WordsList, False),
    }


class AllowList(AWSObject):
    """
    `AllowList <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html>`__
    """

    resource_type = "AWS::Macie::AllowList"

    props: PropsDictType = {
        "Criteria": (Criteria, True),
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class CustomDataIdentifier(AWSObject):
    """
    `CustomDataIdentifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html>`__
    """

    resource_type = "AWS::Macie::CustomDataIdentifier"

    props: PropsDictType = {
        "Description": (str, False),
        "IgnoreWords": ([str], False),
        "Keywords": ([str], False),
        "MaximumMatchDistance": (integer, False),
        "Name": (str, True),
        "Regex": (str, True),
        "Tags": (Tags, False),
    }


class CriterionAdditionalProperties(AWSProperty):
    """
    `CriterionAdditionalProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html>`__
    """

    props: PropsDictType = {
        "eq": ([str], False),
        "gt": (integer, False),
        "gte": (integer, False),
        "lt": (integer, False),
        "lte": (integer, False),
        "neq": ([str], False),
    }


class FindingCriteria(AWSProperty):
    """
    `FindingCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html>`__
    """

    props: PropsDictType = {
        "Criterion": (dict, False),
    }


class FindingsFilter(AWSObject):
    """
    `FindingsFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html>`__
    """

    resource_type = "AWS::Macie::FindingsFilter"

    props: PropsDictType = {
        "Action": (findingsfilter_action, False),
        "Description": (str, False),
        "FindingCriteria": (FindingCriteria, True),
        "Name": (str, True),
        "Position": (integer, False),
        "Tags": (Tags, False),
    }


class Session(AWSObject):
    """
    `Session <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html>`__
    """

    resource_type = "AWS::Macie::Session"

    props: PropsDictType = {
        "FindingPublishingFrequency": (session_findingpublishingfrequency, False),
        "Status": (session_status, False),
    }
