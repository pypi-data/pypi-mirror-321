# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType, Tags


class Profile(AWSObject):
    """
    `Profile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profile.html>`__
    """

    resource_type = "AWS::Route53Profiles::Profile"

    props: PropsDictType = {
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class ProfileAssociation(AWSObject):
    """
    `ProfileAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileassociation.html>`__
    """

    resource_type = "AWS::Route53Profiles::ProfileAssociation"

    props: PropsDictType = {
        "Arn": (str, False),
        "Name": (str, True),
        "ProfileId": (str, True),
        "ResourceId": (str, True),
        "Tags": (Tags, False),
    }


class ProfileResourceAssociation(AWSObject):
    """
    `ProfileResourceAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileresourceassociation.html>`__
    """

    resource_type = "AWS::Route53Profiles::ProfileResourceAssociation"

    props: PropsDictType = {
        "Name": (str, True),
        "ProfileId": (str, True),
        "ResourceArn": (str, True),
        "ResourceProperties": (str, False),
    }
