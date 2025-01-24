# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class ApiDestination(AWSObject):
    """
    `ApiDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.html>`__
    """

    resource_type = "AWS::Events::ApiDestination"

    props: PropsDictType = {
        "ConnectionArn": (str, True),
        "Description": (str, False),
        "HttpMethod": (str, True),
        "InvocationEndpoint": (str, True),
        "InvocationRateLimitPerSecond": (integer, False),
        "Name": (str, False),
    }


class Archive(AWSObject):
    """
    `Archive <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-archive.html>`__
    """

    resource_type = "AWS::Events::Archive"

    props: PropsDictType = {
        "ArchiveName": (str, False),
        "Description": (str, False),
        "EventPattern": (dict, False),
        "RetentionDays": (integer, False),
        "SourceArn": (str, True),
    }


class ApiKeyAuthParameters(AWSProperty):
    """
    `ApiKeyAuthParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-apikeyauthparameters.html>`__
    """

    props: PropsDictType = {
        "ApiKeyName": (str, True),
        "ApiKeyValue": (str, True),
    }


class BasicAuthParameters(AWSProperty):
    """
    `BasicAuthParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-basicauthparameters.html>`__
    """

    props: PropsDictType = {
        "Password": (str, True),
        "Username": (str, True),
    }


class Parameter(AWSProperty):
    """
    `Parameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-parameter.html>`__
    """

    props: PropsDictType = {
        "IsValueSecret": (boolean, False),
        "Key": (str, True),
        "Value": (str, True),
    }


class ConnectionHttpParameters(AWSProperty):
    """
    `ConnectionHttpParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-connectionhttpparameters.html>`__
    """

    props: PropsDictType = {
        "BodyParameters": ([Parameter], False),
        "HeaderParameters": ([Parameter], False),
        "QueryStringParameters": ([Parameter], False),
    }


class ResourceParameters(AWSProperty):
    """
    `ResourceParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-resourceparameters.html>`__
    """

    props: PropsDictType = {
        "ResourceAssociationArn": (str, False),
        "ResourceConfigurationArn": (str, True),
    }


class ConnectivityParameters(AWSProperty):
    """
    `ConnectivityParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-connectivityparameters.html>`__
    """

    props: PropsDictType = {
        "ResourceParameters": (ResourceParameters, True),
    }


class ClientParameters(AWSProperty):
    """
    `ClientParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-clientparameters.html>`__
    """

    props: PropsDictType = {
        "ClientID": (str, True),
        "ClientSecret": (str, True),
    }


class OAuthParameters(AWSProperty):
    """
    `OAuthParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-oauthparameters.html>`__
    """

    props: PropsDictType = {
        "AuthorizationEndpoint": (str, True),
        "ClientParameters": (ClientParameters, True),
        "HttpMethod": (str, True),
        "OAuthHttpParameters": (ConnectionHttpParameters, False),
    }


class AuthParameters(AWSProperty):
    """
    `AuthParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-authparameters.html>`__
    """

    props: PropsDictType = {
        "ApiKeyAuthParameters": (ApiKeyAuthParameters, False),
        "BasicAuthParameters": (BasicAuthParameters, False),
        "ConnectivityParameters": (ConnectivityParameters, False),
        "InvocationHttpParameters": (ConnectionHttpParameters, False),
        "OAuthParameters": (OAuthParameters, False),
    }


class InvocationConnectivityParameters(AWSProperty):
    """
    `InvocationConnectivityParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-invocationconnectivityparameters.html>`__
    """

    props: PropsDictType = {
        "ResourceParameters": (ResourceParameters, True),
    }


class Connection(AWSObject):
    """
    `Connection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.html>`__
    """

    resource_type = "AWS::Events::Connection"

    props: PropsDictType = {
        "AuthParameters": (AuthParameters, False),
        "AuthorizationType": (str, False),
        "Description": (str, False),
        "InvocationConnectivityParameters": (InvocationConnectivityParameters, False),
        "Name": (str, False),
    }


class EndpointEventBus(AWSProperty):
    """
    `EndpointEventBus <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-endpointeventbus.html>`__
    """

    props: PropsDictType = {
        "EventBusArn": (str, True),
    }


class ReplicationConfig(AWSProperty):
    """
    `ReplicationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-replicationconfig.html>`__
    """

    props: PropsDictType = {
        "State": (str, True),
    }


class Primary(AWSProperty):
    """
    `Primary <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-primary.html>`__
    """

    props: PropsDictType = {
        "HealthCheck": (str, True),
    }


class Secondary(AWSProperty):
    """
    `Secondary <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-secondary.html>`__
    """

    props: PropsDictType = {
        "Route": (str, True),
    }


class FailoverConfig(AWSProperty):
    """
    `FailoverConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-failoverconfig.html>`__
    """

    props: PropsDictType = {
        "Primary": (Primary, True),
        "Secondary": (Secondary, True),
    }


class RoutingConfig(AWSProperty):
    """
    `RoutingConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-routingconfig.html>`__
    """

    props: PropsDictType = {
        "FailoverConfig": (FailoverConfig, True),
    }


class Endpoint(AWSObject):
    """
    `Endpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html>`__
    """

    resource_type = "AWS::Events::Endpoint"

    props: PropsDictType = {
        "Description": (str, False),
        "EventBuses": ([EndpointEventBus], True),
        "Name": (str, False),
        "ReplicationConfig": (ReplicationConfig, False),
        "RoleArn": (str, False),
        "RoutingConfig": (RoutingConfig, True),
    }


class DeadLetterConfig(AWSProperty):
    """
    `DeadLetterConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-deadletterconfig.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
    }


class EventBus(AWSObject):
    """
    `EventBus <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html>`__
    """

    resource_type = "AWS::Events::EventBus"

    props: PropsDictType = {
        "DeadLetterConfig": (DeadLetterConfig, False),
        "Description": (str, False),
        "EventSourceName": (str, False),
        "KmsKeyIdentifier": (str, False),
        "Name": (str, True),
        "Policy": (dict, False),
        "Tags": (Tags, False),
    }


class Condition(AWSProperty):
    """
    `Condition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Type": (str, False),
        "Value": (str, False),
    }


class EventBusPolicy(AWSObject):
    """
    `EventBusPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html>`__
    """

    resource_type = "AWS::Events::EventBusPolicy"

    props: PropsDictType = {
        "Action": (str, False),
        "Condition": (Condition, False),
        "EventBusName": (str, False),
        "Principal": (str, False),
        "Statement": (dict, False),
        "StatementId": (str, True),
    }


class AppSyncParameters(AWSProperty):
    """
    `AppSyncParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-appsyncparameters.html>`__
    """

    props: PropsDictType = {
        "GraphQLOperation": (str, True),
    }


class BatchArrayProperties(AWSProperty):
    """
    `BatchArrayProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batcharrayproperties.html>`__
    """

    props: PropsDictType = {
        "Size": (integer, False),
    }


class BatchRetryStrategy(AWSProperty):
    """
    `BatchRetryStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchretrystrategy.html>`__
    """

    props: PropsDictType = {
        "Attempts": (integer, False),
    }


class BatchParameters(AWSProperty):
    """
    `BatchParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchparameters.html>`__
    """

    props: PropsDictType = {
        "ArrayProperties": (BatchArrayProperties, False),
        "JobDefinition": (str, True),
        "JobName": (str, True),
        "RetryStrategy": (BatchRetryStrategy, False),
    }


class CapacityProviderStrategyItem(AWSProperty):
    """
    `CapacityProviderStrategyItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-capacityproviderstrategyitem.html>`__
    """

    props: PropsDictType = {
        "Base": (integer, False),
        "CapacityProvider": (str, True),
        "Weight": (integer, False),
    }


class AwsVpcConfiguration(AWSProperty):
    """
    `AwsVpcConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-awsvpcconfiguration.html>`__
    """

    props: PropsDictType = {
        "AssignPublicIp": (str, False),
        "SecurityGroups": ([str], False),
        "Subnets": ([str], True),
    }


class NetworkConfiguration(AWSProperty):
    """
    `NetworkConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-networkconfiguration.html>`__
    """

    props: PropsDictType = {
        "AwsVpcConfiguration": (AwsVpcConfiguration, False),
    }


class PlacementConstraint(AWSProperty):
    """
    `PlacementConstraint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementconstraint.html>`__
    """

    props: PropsDictType = {
        "Expression": (str, False),
        "Type": (str, False),
    }


class PlacementStrategy(AWSProperty):
    """
    `PlacementStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementstrategy.html>`__
    """

    props: PropsDictType = {
        "Field": (str, False),
        "Type": (str, False),
    }


class EcsParameters(AWSProperty):
    """
    `EcsParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html>`__
    """

    props: PropsDictType = {
        "CapacityProviderStrategy": ([CapacityProviderStrategyItem], False),
        "EnableECSManagedTags": (boolean, False),
        "EnableExecuteCommand": (boolean, False),
        "Group": (str, False),
        "LaunchType": (str, False),
        "NetworkConfiguration": (NetworkConfiguration, False),
        "PlacementConstraints": ([PlacementConstraint], False),
        "PlacementStrategies": ([PlacementStrategy], False),
        "PlatformVersion": (str, False),
        "PropagateTags": (str, False),
        "ReferenceId": (str, False),
        "TagList": (Tags, False),
        "TaskCount": (integer, False),
        "TaskDefinitionArn": (str, True),
    }


class HttpParameters(AWSProperty):
    """
    `HttpParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-httpparameters.html>`__
    """

    props: PropsDictType = {
        "HeaderParameters": (dict, False),
        "PathParameterValues": ([str], False),
        "QueryStringParameters": (dict, False),
    }


class InputTransformer(AWSProperty):
    """
    `InputTransformer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html>`__
    """

    props: PropsDictType = {
        "InputPathsMap": (dict, False),
        "InputTemplate": (str, True),
    }


class KinesisParameters(AWSProperty):
    """
    `KinesisParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-kinesisparameters.html>`__
    """

    props: PropsDictType = {
        "PartitionKeyPath": (str, True),
    }


class RedshiftDataParameters(AWSProperty):
    """
    `RedshiftDataParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-redshiftdataparameters.html>`__
    """

    props: PropsDictType = {
        "Database": (str, True),
        "DbUser": (str, False),
        "SecretManagerArn": (str, False),
        "Sql": (str, False),
        "Sqls": ([str], False),
        "StatementName": (str, False),
        "WithEvent": (boolean, False),
    }


class RetryPolicy(AWSProperty):
    """
    `RetryPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-retrypolicy.html>`__
    """

    props: PropsDictType = {
        "MaximumEventAgeInSeconds": (integer, False),
        "MaximumRetryAttempts": (integer, False),
    }


class RunCommandTarget(AWSProperty):
    """
    `RunCommandTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Values": ([str], True),
    }


class RunCommandParameters(AWSProperty):
    """
    `RunCommandParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandparameters.html>`__
    """

    props: PropsDictType = {
        "RunCommandTargets": ([RunCommandTarget], True),
    }


class SageMakerPipelineParameter(AWSProperty):
    """
    `SageMakerPipelineParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameter.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Value": (str, True),
    }


class SageMakerPipelineParameters(AWSProperty):
    """
    `SageMakerPipelineParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameters.html>`__
    """

    props: PropsDictType = {
        "PipelineParameterList": ([SageMakerPipelineParameter], False),
    }


class SqsParameters(AWSProperty):
    """
    `SqsParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sqsparameters.html>`__
    """

    props: PropsDictType = {
        "MessageGroupId": (str, True),
    }


class Target(AWSProperty):
    """
    `Target <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html>`__
    """

    props: PropsDictType = {
        "AppSyncParameters": (AppSyncParameters, False),
        "Arn": (str, True),
        "BatchParameters": (BatchParameters, False),
        "DeadLetterConfig": (DeadLetterConfig, False),
        "EcsParameters": (EcsParameters, False),
        "HttpParameters": (HttpParameters, False),
        "Id": (str, True),
        "Input": (str, False),
        "InputPath": (str, False),
        "InputTransformer": (InputTransformer, False),
        "KinesisParameters": (KinesisParameters, False),
        "RedshiftDataParameters": (RedshiftDataParameters, False),
        "RetryPolicy": (RetryPolicy, False),
        "RoleArn": (str, False),
        "RunCommandParameters": (RunCommandParameters, False),
        "SageMakerPipelineParameters": (SageMakerPipelineParameters, False),
        "SqsParameters": (SqsParameters, False),
    }


class Rule(AWSObject):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html>`__
    """

    resource_type = "AWS::Events::Rule"

    props: PropsDictType = {
        "Description": (str, False),
        "EventBusName": (str, False),
        "EventPattern": (dict, False),
        "Name": (str, False),
        "RoleArn": (str, False),
        "ScheduleExpression": (str, False),
        "State": (str, False),
        "Targets": ([Target], False),
    }
