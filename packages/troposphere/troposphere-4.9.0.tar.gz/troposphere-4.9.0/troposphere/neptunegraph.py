# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class VectorSearchConfiguration(AWSProperty):
    """
    `VectorSearchConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-vectorsearchconfiguration.html>`__
    """

    props: PropsDictType = {
        "VectorSearchDimension": (integer, True),
    }


class Graph(AWSObject):
    """
    `Graph <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html>`__
    """

    resource_type = "AWS::NeptuneGraph::Graph"

    props: PropsDictType = {
        "DeletionProtection": (boolean, False),
        "GraphName": (str, False),
        "ProvisionedMemory": (integer, True),
        "PublicConnectivity": (boolean, False),
        "ReplicaCount": (integer, False),
        "Tags": (Tags, False),
        "VectorSearchConfiguration": (VectorSearchConfiguration, False),
    }


class PrivateGraphEndpoint(AWSObject):
    """
    `PrivateGraphEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html>`__
    """

    resource_type = "AWS::NeptuneGraph::PrivateGraphEndpoint"

    props: PropsDictType = {
        "GraphIdentifier": (str, True),
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], False),
        "VpcId": (str, True),
    }
