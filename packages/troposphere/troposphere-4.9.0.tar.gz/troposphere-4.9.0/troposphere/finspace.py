# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags


class AttributeMapItems(AWSProperty):
    """
    `AttributeMapItems <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-attributemapitems.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Value": (str, False),
    }


class FederationParameters(AWSProperty):
    """
    `FederationParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html>`__
    """

    props: PropsDictType = {
        "ApplicationCallBackURL": (str, False),
        "AttributeMap": ([AttributeMapItems], False),
        "FederationProviderName": (str, False),
        "FederationURN": (str, False),
        "SamlMetadataDocument": (str, False),
        "SamlMetadataURL": (str, False),
    }


class SuperuserParameters(AWSProperty):
    """
    `SuperuserParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html>`__
    """

    props: PropsDictType = {
        "EmailAddress": (str, False),
        "FirstName": (str, False),
        "LastName": (str, False),
    }


class Environment(AWSObject):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html>`__
    """

    resource_type = "AWS::FinSpace::Environment"

    props: PropsDictType = {
        "Description": (str, False),
        "FederationMode": (str, False),
        "FederationParameters": (FederationParameters, False),
        "KmsKeyId": (str, False),
        "Name": (str, True),
        "SuperuserParameters": (SuperuserParameters, False),
        "Tags": (Tags, False),
    }
