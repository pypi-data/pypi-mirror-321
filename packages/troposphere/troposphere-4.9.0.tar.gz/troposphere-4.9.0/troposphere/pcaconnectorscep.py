# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType


class Challenge(AWSObject):
    """
    `Challenge <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-challenge.html>`__
    """

    resource_type = "AWS::PCAConnectorSCEP::Challenge"

    props: PropsDictType = {
        "ConnectorArn": (str, True),
        "Tags": (dict, False),
    }


class IntuneConfiguration(AWSProperty):
    """
    `IntuneConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-intuneconfiguration.html>`__
    """

    props: PropsDictType = {
        "AzureApplicationId": (str, True),
        "Domain": (str, True),
    }


class MobileDeviceManagement(AWSProperty):
    """
    `MobileDeviceManagement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-mobiledevicemanagement.html>`__
    """

    props: PropsDictType = {
        "Intune": (IntuneConfiguration, True),
    }


class Connector(AWSObject):
    """
    `Connector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-connector.html>`__
    """

    resource_type = "AWS::PCAConnectorSCEP::Connector"

    props: PropsDictType = {
        "CertificateAuthorityArn": (str, True),
        "MobileDeviceManagement": (MobileDeviceManagement, False),
        "Tags": (dict, False),
    }


class OpenIdConfiguration(AWSProperty):
    """
    `OpenIdConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-openidconfiguration.html>`__
    """

    props: PropsDictType = {
        "Audience": (str, False),
        "Issuer": (str, False),
        "Subject": (str, False),
    }
