# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import double, integer


class ConditionBasedCollectionScheme(AWSProperty):
    """
    `ConditionBasedCollectionScheme <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html>`__
    """

    props: PropsDictType = {
        "ConditionLanguageVersion": (integer, False),
        "Expression": (str, True),
        "MinimumTriggerIntervalMs": (double, False),
        "TriggerMode": (str, False),
    }


class TimeBasedCollectionScheme(AWSProperty):
    """
    `TimeBasedCollectionScheme <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timebasedcollectionscheme.html>`__
    """

    props: PropsDictType = {
        "PeriodMs": (double, True),
    }


class CollectionScheme(AWSProperty):
    """
    `CollectionScheme <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html>`__
    """

    props: PropsDictType = {
        "ConditionBasedCollectionScheme": (ConditionBasedCollectionScheme, False),
        "TimeBasedCollectionScheme": (TimeBasedCollectionScheme, False),
    }


class MqttTopicConfig(AWSProperty):
    """
    `MqttTopicConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-mqtttopicconfig.html>`__
    """

    props: PropsDictType = {
        "ExecutionRoleArn": (str, True),
        "MqttTopicArn": (str, True),
    }


class S3Config(AWSProperty):
    """
    `S3Config <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-s3config.html>`__
    """

    props: PropsDictType = {
        "BucketArn": (str, True),
        "DataFormat": (str, False),
        "Prefix": (str, False),
        "StorageCompressionFormat": (str, False),
    }


class TimestreamConfig(AWSProperty):
    """
    `TimestreamConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timestreamconfig.html>`__
    """

    props: PropsDictType = {
        "ExecutionRoleArn": (str, True),
        "TimestreamTableArn": (str, True),
    }


class DataDestinationConfig(AWSProperty):
    """
    `DataDestinationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-datadestinationconfig.html>`__
    """

    props: PropsDictType = {
        "MqttTopicConfig": (MqttTopicConfig, False),
        "S3Config": (S3Config, False),
        "TimestreamConfig": (TimestreamConfig, False),
    }


class StorageMaximumSize(AWSProperty):
    """
    `StorageMaximumSize <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-storagemaximumsize.html>`__
    """

    props: PropsDictType = {
        "Unit": (str, True),
        "Value": (integer, True),
    }


class StorageMinimumTimeToLive(AWSProperty):
    """
    `StorageMinimumTimeToLive <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-storageminimumtimetolive.html>`__
    """

    props: PropsDictType = {
        "Unit": (str, True),
        "Value": (integer, True),
    }


class DataPartitionStorageOptions(AWSProperty):
    """
    `DataPartitionStorageOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-datapartitionstorageoptions.html>`__
    """

    props: PropsDictType = {
        "MaximumSize": (StorageMaximumSize, True),
        "MinimumTimeToLive": (StorageMinimumTimeToLive, True),
        "StorageLocation": (str, True),
    }


class DataPartitionUploadOptions(AWSProperty):
    """
    `DataPartitionUploadOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-datapartitionuploadoptions.html>`__
    """

    props: PropsDictType = {
        "ConditionLanguageVersion": (integer, False),
        "Expression": (str, True),
    }


class DataPartition(AWSProperty):
    """
    `DataPartition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-datapartition.html>`__
    """

    props: PropsDictType = {
        "Id": (str, True),
        "StorageOptions": (DataPartitionStorageOptions, True),
        "UploadOptions": (DataPartitionUploadOptions, False),
    }


class ConditionBasedSignalFetchConfig(AWSProperty):
    """
    `ConditionBasedSignalFetchConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedsignalfetchconfig.html>`__
    """

    props: PropsDictType = {
        "ConditionExpression": (str, True),
        "TriggerMode": (str, True),
    }


class TimeBasedSignalFetchConfig(AWSProperty):
    """
    `TimeBasedSignalFetchConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timebasedsignalfetchconfig.html>`__
    """

    props: PropsDictType = {
        "ExecutionFrequencyMs": (double, True),
    }


class SignalFetchConfig(AWSProperty):
    """
    `SignalFetchConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalfetchconfig.html>`__
    """

    props: PropsDictType = {
        "ConditionBased": (ConditionBasedSignalFetchConfig, False),
        "TimeBased": (TimeBasedSignalFetchConfig, False),
    }


class SignalFetchInformation(AWSProperty):
    """
    `SignalFetchInformation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalfetchinformation.html>`__
    """

    props: PropsDictType = {
        "Actions": ([str], True),
        "ConditionLanguageVersion": (double, False),
        "FullyQualifiedName": (str, True),
        "SignalFetchConfig": (SignalFetchConfig, True),
    }


class SignalInformation(AWSProperty):
    """
    `SignalInformation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html>`__
    """

    props: PropsDictType = {
        "DataPartitionId": (str, False),
        "MaxSampleCount": (double, False),
        "MinimumSamplingIntervalMs": (double, False),
        "Name": (str, True),
    }


class Campaign(AWSObject):
    """
    `Campaign <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html>`__
    """

    resource_type = "AWS::IoTFleetWise::Campaign"

    props: PropsDictType = {
        "Action": (str, False),
        "CollectionScheme": (CollectionScheme, True),
        "Compression": (str, False),
        "DataDestinationConfigs": ([DataDestinationConfig], False),
        "DataExtraDimensions": ([str], False),
        "DataPartitions": ([DataPartition], False),
        "Description": (str, False),
        "DiagnosticsMode": (str, False),
        "ExpiryTime": (str, False),
        "Name": (str, True),
        "PostTriggerCollectionDuration": (double, False),
        "Priority": (integer, False),
        "SignalCatalogArn": (str, True),
        "SignalsToCollect": ([SignalInformation], False),
        "SignalsToFetch": ([SignalFetchInformation], False),
        "SpoolingMode": (str, False),
        "StartTime": (str, False),
        "Tags": (Tags, False),
        "TargetArn": (str, True),
    }


class CanInterface(AWSProperty):
    """
    `CanInterface <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "ProtocolName": (str, False),
        "ProtocolVersion": (str, False),
    }


class CustomDecodingInterface(AWSProperty):
    """
    `CustomDecodingInterface <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-customdecodinginterface.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
    }


class ObdInterface(AWSProperty):
    """
    `ObdInterface <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html>`__
    """

    props: PropsDictType = {
        "DtcRequestIntervalSeconds": (str, False),
        "HasTransmissionEcu": (str, False),
        "Name": (str, True),
        "ObdStandard": (str, False),
        "PidRequestIntervalSeconds": (str, False),
        "RequestMessageId": (str, True),
        "UseExtendedIds": (str, False),
    }


class NetworkInterfacesItems(AWSProperty):
    """
    `NetworkInterfacesItems <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html>`__
    """

    props: PropsDictType = {
        "CanInterface": (CanInterface, False),
        "CustomDecodingInterface": (CustomDecodingInterface, False),
        "InterfaceId": (str, True),
        "ObdInterface": (ObdInterface, False),
        "Type": (str, True),
    }


class CanSignal(AWSProperty):
    """
    `CanSignal <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html>`__
    """

    props: PropsDictType = {
        "Factor": (str, True),
        "IsBigEndian": (str, True),
        "IsSigned": (str, True),
        "Length": (str, True),
        "MessageId": (str, True),
        "Name": (str, False),
        "Offset": (str, True),
        "StartBit": (str, True),
    }


class CustomDecodingSignal(AWSProperty):
    """
    `CustomDecodingSignal <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-customdecodingsignal.html>`__
    """

    props: PropsDictType = {
        "Id": (str, True),
    }


class ObdSignal(AWSProperty):
    """
    `ObdSignal <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html>`__
    """

    props: PropsDictType = {
        "BitMaskLength": (str, False),
        "BitRightShift": (str, False),
        "ByteLength": (str, True),
        "Offset": (str, True),
        "Pid": (str, True),
        "PidResponseLength": (str, True),
        "Scaling": (str, True),
        "ServiceMode": (str, True),
        "StartByte": (str, True),
    }


class SignalDecodersItems(AWSProperty):
    """
    `SignalDecodersItems <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html>`__
    """

    props: PropsDictType = {
        "CanSignal": (CanSignal, False),
        "CustomDecodingSignal": (CustomDecodingSignal, False),
        "FullyQualifiedName": (str, True),
        "InterfaceId": (str, True),
        "ObdSignal": (ObdSignal, False),
        "Type": (str, True),
    }


class DecoderManifest(AWSObject):
    """
    `DecoderManifest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html>`__
    """

    resource_type = "AWS::IoTFleetWise::DecoderManifest"

    props: PropsDictType = {
        "DefaultForUnmappedSignals": (str, False),
        "Description": (str, False),
        "ModelManifestArn": (str, True),
        "Name": (str, True),
        "NetworkInterfaces": ([NetworkInterfacesItems], False),
        "SignalDecoders": ([SignalDecodersItems], False),
        "Status": (str, False),
        "Tags": (Tags, False),
    }


class Fleet(AWSObject):
    """
    `Fleet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html>`__
    """

    resource_type = "AWS::IoTFleetWise::Fleet"

    props: PropsDictType = {
        "Description": (str, False),
        "Id": (str, True),
        "SignalCatalogArn": (str, True),
        "Tags": (Tags, False),
    }


class ModelManifest(AWSObject):
    """
    `ModelManifest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html>`__
    """

    resource_type = "AWS::IoTFleetWise::ModelManifest"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Nodes": ([str], False),
        "SignalCatalogArn": (str, True),
        "Status": (str, False),
        "Tags": (Tags, False),
    }


class Actuator(AWSProperty):
    """
    `Actuator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html>`__
    """

    props: PropsDictType = {
        "AllowedValues": ([str], False),
        "AssignedValue": (str, False),
        "DataType": (str, True),
        "Description": (str, False),
        "FullyQualifiedName": (str, True),
        "Max": (double, False),
        "Min": (double, False),
        "Unit": (str, False),
    }


class Attribute(AWSProperty):
    """
    `Attribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html>`__
    """

    props: PropsDictType = {
        "AllowedValues": ([str], False),
        "AssignedValue": (str, False),
        "DataType": (str, True),
        "DefaultValue": (str, False),
        "Description": (str, False),
        "FullyQualifiedName": (str, True),
        "Max": (double, False),
        "Min": (double, False),
        "Unit": (str, False),
    }


class Branch(AWSProperty):
    """
    `Branch <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "FullyQualifiedName": (str, True),
    }


class Sensor(AWSProperty):
    """
    `Sensor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html>`__
    """

    props: PropsDictType = {
        "AllowedValues": ([str], False),
        "DataType": (str, True),
        "Description": (str, False),
        "FullyQualifiedName": (str, True),
        "Max": (double, False),
        "Min": (double, False),
        "Unit": (str, False),
    }


class Node(AWSProperty):
    """
    `Node <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html>`__
    """

    props: PropsDictType = {
        "Actuator": (Actuator, False),
        "Attribute": (Attribute, False),
        "Branch": (Branch, False),
        "Sensor": (Sensor, False),
    }


class NodeCounts(AWSProperty):
    """
    `NodeCounts <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html>`__
    """

    props: PropsDictType = {
        "TotalActuators": (double, False),
        "TotalAttributes": (double, False),
        "TotalBranches": (double, False),
        "TotalNodes": (double, False),
        "TotalSensors": (double, False),
    }


class SignalCatalog(AWSObject):
    """
    `SignalCatalog <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html>`__
    """

    resource_type = "AWS::IoTFleetWise::SignalCatalog"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, False),
        "NodeCounts": (NodeCounts, False),
        "Nodes": ([Node], False),
        "Tags": (Tags, False),
    }


class StateTemplate(AWSObject):
    """
    `StateTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-statetemplate.html>`__
    """

    resource_type = "AWS::IoTFleetWise::StateTemplate"

    props: PropsDictType = {
        "DataExtraDimensions": ([str], False),
        "Description": (str, False),
        "MetadataExtraDimensions": ([str], False),
        "Name": (str, True),
        "SignalCatalogArn": (str, True),
        "StateTemplateProperties": ([str], True),
        "Tags": (Tags, False),
    }


class Vehicle(AWSObject):
    """
    `Vehicle <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html>`__
    """

    resource_type = "AWS::IoTFleetWise::Vehicle"

    props: PropsDictType = {
        "AssociationBehavior": (str, False),
        "Attributes": (dict, False),
        "DecoderManifestArn": (str, True),
        "ModelManifestArn": (str, True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }
