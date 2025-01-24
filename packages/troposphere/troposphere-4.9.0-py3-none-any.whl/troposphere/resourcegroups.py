# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators.resourcegroups import resourcequery_type


class ConfigurationParameter(AWSProperty):
    """
    `ConfigurationParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-configurationparameter.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Values": ([str], False),
    }


class ConfigurationItem(AWSProperty):
    """
    `ConfigurationItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-configurationitem.html>`__
    """

    props: PropsDictType = {
        "Parameters": ([ConfigurationParameter], False),
        "Type": (str, False),
    }


class TagFilter(AWSProperty):
    """
    `TagFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-tagfilter.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Values": ([str], False),
    }


class Query(AWSProperty):
    """
    `Query <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-query.html>`__
    """

    props: PropsDictType = {
        "ResourceTypeFilters": ([str], False),
        "StackIdentifier": (str, False),
        "TagFilters": ([TagFilter], False),
    }


class ResourceQuery(AWSProperty):
    """
    `ResourceQuery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-resourcequery.html>`__
    """

    props: PropsDictType = {
        "Query": (Query, False),
        "Type": (resourcequery_type, False),
    }


class Group(AWSObject):
    """
    `Group <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html>`__
    """

    resource_type = "AWS::ResourceGroups::Group"

    props: PropsDictType = {
        "Configuration": ([ConfigurationItem], False),
        "Description": (str, False),
        "Name": (str, True),
        "ResourceQuery": (ResourceQuery, False),
        "Resources": ([str], False),
        "Tags": (Tags, False),
    }


class TagSyncTask(AWSObject):
    """
    `TagSyncTask <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-tagsynctask.html>`__
    """

    resource_type = "AWS::ResourceGroups::TagSyncTask"

    props: PropsDictType = {
        "Group": (str, True),
        "RoleArn": (str, True),
        "TagKey": (str, True),
        "TagValue": (str, True),
    }
