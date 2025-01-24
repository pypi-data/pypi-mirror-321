# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class Cluster(AWSObject):
    """
    `Cluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html>`__
    """

    resource_type = "AWS::Route53RecoveryControl::Cluster"

    props: PropsDictType = {
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class ControlPanel(AWSObject):
    """
    `ControlPanel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html>`__
    """

    resource_type = "AWS::Route53RecoveryControl::ControlPanel"

    props: PropsDictType = {
        "ClusterArn": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class RoutingControl(AWSObject):
    """
    `RoutingControl <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html>`__
    """

    resource_type = "AWS::Route53RecoveryControl::RoutingControl"

    props: PropsDictType = {
        "ClusterArn": (str, False),
        "ControlPanelArn": (str, False),
        "Name": (str, True),
    }


class AssertionRule(AWSProperty):
    """
    `AssertionRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html>`__
    """

    props: PropsDictType = {
        "AssertedControls": ([str], True),
        "WaitPeriodMs": (integer, True),
    }


class GatingRule(AWSProperty):
    """
    `GatingRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html>`__
    """

    props: PropsDictType = {
        "GatingControls": ([str], True),
        "TargetControls": ([str], True),
        "WaitPeriodMs": (integer, True),
    }


class RuleConfig(AWSProperty):
    """
    `RuleConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html>`__
    """

    props: PropsDictType = {
        "Inverted": (boolean, True),
        "Threshold": (integer, True),
        "Type": (str, True),
    }


class SafetyRule(AWSObject):
    """
    `SafetyRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html>`__
    """

    resource_type = "AWS::Route53RecoveryControl::SafetyRule"

    props: PropsDictType = {
        "AssertionRule": (AssertionRule, False),
        "ControlPanelArn": (str, True),
        "GatingRule": (GatingRule, False),
        "Name": (str, True),
        "RuleConfig": (RuleConfig, True),
        "Tags": (Tags, False),
    }


class ClusterEndpoint(AWSProperty):
    """
    `ClusterEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html>`__
    """

    props: PropsDictType = {
        "Endpoint": (str, False),
        "Region": (str, False),
    }
