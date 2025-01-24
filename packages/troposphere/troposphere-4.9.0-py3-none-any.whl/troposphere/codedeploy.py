# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.codedeploy import KEY_AND_VALUE  # noqa: F401
from .validators.codedeploy import KEY_ONLY  # noqa: F401
from .validators.codedeploy import VALUE_ONLY  # noqa: F401
from .validators.codedeploy import (
    deployment_option_validator,
    deployment_type_validator,
    validate_deployment_group,
    validate_load_balancer_info,
)


class Application(AWSObject):
    """
    `Application <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html>`__
    """

    resource_type = "AWS::CodeDeploy::Application"

    props: PropsDictType = {
        "ApplicationName": (str, False),
        "ComputePlatform": (str, False),
        "Tags": (Tags, False),
    }


class MinimumHealthyHosts(AWSProperty):
    """
    `MinimumHealthyHosts <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (integer, True),
    }


class TimeBasedCanary(AWSProperty):
    """
    `TimeBasedCanary <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedcanary.html>`__
    """

    props: PropsDictType = {
        "CanaryInterval": (integer, True),
        "CanaryPercentage": (integer, True),
    }


class TimeBasedLinear(AWSProperty):
    """
    `TimeBasedLinear <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedlinear.html>`__
    """

    props: PropsDictType = {
        "LinearInterval": (integer, True),
        "LinearPercentage": (integer, True),
    }


class TrafficRoutingConfig(AWSProperty):
    """
    `TrafficRoutingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-trafficroutingconfig.html>`__
    """

    props: PropsDictType = {
        "TimeBasedCanary": (TimeBasedCanary, False),
        "TimeBasedLinear": (TimeBasedLinear, False),
        "Type": (str, True),
    }


class MinimumHealthyHostsPerZone(AWSProperty):
    """
    `MinimumHealthyHostsPerZone <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhostsperzone.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (integer, True),
    }


class ZonalConfig(AWSProperty):
    """
    `ZonalConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-zonalconfig.html>`__
    """

    props: PropsDictType = {
        "FirstZoneMonitorDurationInSeconds": (integer, False),
        "MinimumHealthyHostsPerZone": (MinimumHealthyHostsPerZone, False),
        "MonitorDurationInSeconds": (integer, False),
    }


class DeploymentConfig(AWSObject):
    """
    `DeploymentConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html>`__
    """

    resource_type = "AWS::CodeDeploy::DeploymentConfig"

    props: PropsDictType = {
        "ComputePlatform": (str, False),
        "DeploymentConfigName": (str, False),
        "MinimumHealthyHosts": (MinimumHealthyHosts, False),
        "TrafficRoutingConfig": (TrafficRoutingConfig, False),
        "ZonalConfig": (ZonalConfig, False),
    }


class Alarm(AWSProperty):
    """
    `Alarm <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarm.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
    }


class AlarmConfiguration(AWSProperty):
    """
    `AlarmConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html>`__
    """

    props: PropsDictType = {
        "Alarms": ([Alarm], False),
        "Enabled": (boolean, False),
        "IgnorePollAlarmFailure": (boolean, False),
    }


class AutoRollbackConfiguration(AWSProperty):
    """
    `AutoRollbackConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "Events": ([str], False),
    }


class BlueInstanceTerminationOption(AWSProperty):
    """
    `BlueInstanceTerminationOption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-blueinstanceterminationoption.html>`__
    """

    props: PropsDictType = {
        "Action": (str, False),
        "TerminationWaitTimeInMinutes": (integer, False),
    }


class DeploymentReadyOption(AWSProperty):
    """
    `DeploymentReadyOption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentreadyoption.html>`__
    """

    props: PropsDictType = {
        "ActionOnTimeout": (str, False),
        "WaitTimeInMinutes": (integer, False),
    }


class GreenFleetProvisioningOption(AWSProperty):
    """
    `GreenFleetProvisioningOption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption.html>`__
    """

    props: PropsDictType = {
        "Action": (str, False),
    }


class BlueGreenDeploymentConfiguration(AWSProperty):
    """
    `BlueGreenDeploymentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-bluegreendeploymentconfiguration.html>`__
    """

    props: PropsDictType = {
        "DeploymentReadyOption": (DeploymentReadyOption, False),
        "GreenFleetProvisioningOption": (GreenFleetProvisioningOption, False),
        "TerminateBlueInstancesOnDeploymentSuccess": (
            BlueInstanceTerminationOption,
            False,
        ),
    }


class GitHubLocation(AWSProperty):
    """
    `GitHubLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html>`__
    """

    props: PropsDictType = {
        "CommitId": (str, True),
        "Repository": (str, True),
    }


class S3Location(AWSProperty):
    """
    `S3Location <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "BundleType": (str, False),
        "ETag": (str, False),
        "Key": (str, True),
        "Version": (str, False),
    }


class Revision(AWSProperty):
    """
    `Revision <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html>`__
    """

    props: PropsDictType = {
        "GitHubLocation": (GitHubLocation, False),
        "RevisionType": (str, False),
        "S3Location": (S3Location, False),
    }


class Deployment(AWSProperty):
    """
    `Deployment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "IgnoreApplicationStopFailures": (boolean, False),
        "Revision": (Revision, True),
    }


class DeploymentStyle(AWSProperty):
    """
    `DeploymentStyle <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html>`__
    """

    props: PropsDictType = {
        "DeploymentOption": (deployment_option_validator, False),
        "DeploymentType": (deployment_type_validator, False),
    }


class ECSService(AWSProperty):
    """
    `ECSService <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ecsservice.html>`__
    """

    props: PropsDictType = {
        "ClusterName": (str, True),
        "ServiceName": (str, True),
    }


class Ec2TagFilters(AWSProperty):
    """
    `Ec2TagFilters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Type": (str, False),
        "Value": (str, False),
    }


class Ec2TagSetListObject(AWSProperty):
    """
    `Ec2TagSetListObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagsetlistobject.html>`__
    """

    props: PropsDictType = {
        "Ec2TagGroup": ([Ec2TagFilters], False),
    }


class Ec2TagSet(AWSProperty):
    """
    `Ec2TagSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagset.html>`__
    """

    props: PropsDictType = {
        "Ec2TagSetList": ([Ec2TagSetListObject], False),
    }


class ElbInfoList(AWSProperty):
    """
    `ElbInfoList <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-elbinfo.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
    }


class TargetGroupInfo(AWSProperty):
    """
    `TargetGroupInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgroupinfo.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
    }


class TrafficRoute(AWSProperty):
    """
    `TrafficRoute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-trafficroute.html>`__
    """

    props: PropsDictType = {
        "ListenerArns": ([str], False),
    }


class TargetGroupPairInfo(AWSProperty):
    """
    `TargetGroupPairInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgrouppairinfo.html>`__
    """

    props: PropsDictType = {
        "ProdTrafficRoute": (TrafficRoute, False),
        "TargetGroups": ([TargetGroupInfo], False),
        "TestTrafficRoute": (TrafficRoute, False),
    }


class LoadBalancerInfo(AWSProperty):
    """
    `LoadBalancerInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html>`__
    """

    props: PropsDictType = {
        "ElbInfoList": ([ElbInfoList], False),
        "TargetGroupInfoList": ([TargetGroupInfo], False),
        "TargetGroupPairInfoList": ([TargetGroupPairInfo], False),
    }

    def validate(self):
        validate_load_balancer_info(self)


class OnPremisesInstanceTagFilters(AWSProperty):
    """
    `OnPremisesInstanceTagFilters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Type": (str, False),
        "Value": (str, False),
    }


class TagFilter(AWSProperty):
    """
    `TagFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Type": (str, False),
        "Value": (str, False),
    }


class OnPremisesTagSetListObject(AWSProperty):
    """
    `OnPremisesTagSetListObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject.html>`__
    """

    props: PropsDictType = {
        "OnPremisesTagGroup": ([TagFilter], False),
    }


class OnPremisesTagSet(AWSProperty):
    """
    `OnPremisesTagSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html>`__
    """

    props: PropsDictType = {
        "OnPremisesTagSetList": ([OnPremisesTagSetListObject], False),
    }


class TriggerConfig(AWSProperty):
    """
    `TriggerConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html>`__
    """

    props: PropsDictType = {
        "TriggerEvents": ([str], False),
        "TriggerName": (str, False),
        "TriggerTargetArn": (str, False),
    }


class DeploymentGroup(AWSObject):
    """
    `DeploymentGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html>`__
    """

    resource_type = "AWS::CodeDeploy::DeploymentGroup"

    props: PropsDictType = {
        "AlarmConfiguration": (AlarmConfiguration, False),
        "ApplicationName": (str, True),
        "AutoRollbackConfiguration": (AutoRollbackConfiguration, False),
        "AutoScalingGroups": ([str], False),
        "BlueGreenDeploymentConfiguration": (BlueGreenDeploymentConfiguration, False),
        "Deployment": (Deployment, False),
        "DeploymentConfigName": (str, False),
        "DeploymentGroupName": (str, False),
        "DeploymentStyle": (DeploymentStyle, False),
        "ECSServices": ([ECSService], False),
        "Ec2TagFilters": ([Ec2TagFilters], False),
        "Ec2TagSet": (Ec2TagSet, False),
        "LoadBalancerInfo": (LoadBalancerInfo, False),
        "OnPremisesInstanceTagFilters": ([OnPremisesInstanceTagFilters], False),
        "OnPremisesTagSet": (OnPremisesTagSet, False),
        "OutdatedInstancesStrategy": (str, False),
        "ServiceRoleArn": (str, True),
        "Tags": (Tags, False),
        "TerminationHookEnabled": (boolean, False),
        "TriggerConfigurations": ([TriggerConfig], False),
    }

    def validate(self):
        validate_deployment_group(self)
