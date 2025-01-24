# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType


class LinkFilter(AWSProperty):
    """
    `LinkFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-oam-link-linkfilter.html>`__
    """

    props: PropsDictType = {
        "Filter": (str, True),
    }


class LinkConfiguration(AWSProperty):
    """
    `LinkConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-oam-link-linkconfiguration.html>`__
    """

    props: PropsDictType = {
        "LogGroupConfiguration": (LinkFilter, False),
        "MetricConfiguration": (LinkFilter, False),
    }


class Link(AWSObject):
    """
    `Link <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-link.html>`__
    """

    resource_type = "AWS::Oam::Link"

    props: PropsDictType = {
        "LabelTemplate": (str, False),
        "LinkConfiguration": (LinkConfiguration, False),
        "ResourceTypes": ([str], True),
        "SinkIdentifier": (str, True),
        "Tags": (dict, False),
    }


class Sink(AWSObject):
    """
    `Sink <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-sink.html>`__
    """

    resource_type = "AWS::Oam::Sink"

    props: PropsDictType = {
        "Name": (str, True),
        "Policy": (dict, False),
        "Tags": (dict, False),
    }
