# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class EntityTypeProperty(AWSProperty):
    """
    `EntityTypeProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
        "CreatedTime": (str, False),
        "Description": (str, False),
        "Inline": (boolean, False),
        "LastUpdatedTime": (str, False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class EventVariable(AWSProperty):
    """
    `EventVariable <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
        "CreatedTime": (str, False),
        "DataSource": (str, False),
        "DataType": (str, False),
        "DefaultValue": (str, False),
        "Description": (str, False),
        "Inline": (boolean, False),
        "LastUpdatedTime": (str, False),
        "Name": (str, False),
        "Tags": (Tags, False),
        "VariableType": (str, False),
    }


class LabelProperty(AWSProperty):
    """
    `LabelProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
        "CreatedTime": (str, False),
        "Description": (str, False),
        "Inline": (boolean, False),
        "LastUpdatedTime": (str, False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class EventTypeProperty(AWSProperty):
    """
    `EventTypeProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
        "CreatedTime": (str, False),
        "Description": (str, False),
        "EntityTypes": ([EntityTypeProperty], False),
        "EventVariables": ([EventVariable], False),
        "Inline": (boolean, False),
        "Labels": ([LabelProperty], False),
        "LastUpdatedTime": (str, False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class Model(AWSProperty):
    """
    `Model <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-model.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
    }


class OutcomeProperty(AWSProperty):
    """
    `OutcomeProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
        "CreatedTime": (str, False),
        "Description": (str, False),
        "Inline": (boolean, False),
        "LastUpdatedTime": (str, False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class Rule(AWSProperty):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
        "CreatedTime": (str, False),
        "Description": (str, False),
        "DetectorId": (str, False),
        "Expression": (str, False),
        "Language": (str, False),
        "LastUpdatedTime": (str, False),
        "Outcomes": ([OutcomeProperty], False),
        "RuleId": (str, False),
        "RuleVersion": (str, False),
        "Tags": (Tags, False),
    }


class Detector(AWSObject):
    """
    `Detector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html>`__
    """

    resource_type = "AWS::FraudDetector::Detector"

    props: PropsDictType = {
        "AssociatedModels": ([Model], False),
        "Description": (str, False),
        "DetectorId": (str, True),
        "DetectorVersionStatus": (str, False),
        "EventType": (EventTypeProperty, True),
        "RuleExecutionMode": (str, False),
        "Rules": ([Rule], True),
        "Tags": (Tags, False),
    }


class EntityType(AWSObject):
    """
    `EntityType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html>`__
    """

    resource_type = "AWS::FraudDetector::EntityType"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class EventType(AWSObject):
    """
    `EventType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html>`__
    """

    resource_type = "AWS::FraudDetector::EventType"

    props: PropsDictType = {
        "Description": (str, False),
        "EntityTypes": ([EntityTypeProperty], True),
        "EventVariables": ([EventVariable], True),
        "Labels": ([LabelProperty], True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class Label(AWSObject):
    """
    `Label <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html>`__
    """

    resource_type = "AWS::FraudDetector::Label"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class List(AWSObject):
    """
    `List <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-list.html>`__
    """

    resource_type = "AWS::FraudDetector::List"

    props: PropsDictType = {
        "Description": (str, False),
        "Elements": ([str], False),
        "Name": (str, True),
        "Tags": (Tags, False),
        "VariableType": (str, False),
    }


class Outcome(AWSObject):
    """
    `Outcome <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html>`__
    """

    resource_type = "AWS::FraudDetector::Outcome"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class Variable(AWSObject):
    """
    `Variable <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html>`__
    """

    resource_type = "AWS::FraudDetector::Variable"

    props: PropsDictType = {
        "DataSource": (str, True),
        "DataType": (str, True),
        "DefaultValue": (str, True),
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
        "VariableType": (str, False),
    }
