# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class X12Details(AWSProperty):
    """
    `X12Details <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-x12details.html>`__
    """

    props: PropsDictType = {
        "TransactionSet": (str, False),
        "Version": (str, False),
    }


class EdiType(AWSProperty):
    """
    `EdiType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-editype.html>`__
    """

    props: PropsDictType = {
        "X12Details": (X12Details, True),
    }


class S3Location(AWSProperty):
    """
    `S3Location <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-s3location.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, False),
        "Key": (str, False),
    }


class EdiConfiguration(AWSProperty):
    """
    `EdiConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html>`__
    """

    props: PropsDictType = {
        "CapabilityDirection": (str, False),
        "InputLocation": (S3Location, True),
        "OutputLocation": (S3Location, True),
        "TransformerId": (str, True),
        "Type": (EdiType, True),
    }


class CapabilityConfiguration(AWSProperty):
    """
    `CapabilityConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-capabilityconfiguration.html>`__
    """

    props: PropsDictType = {
        "Edi": (EdiConfiguration, True),
    }


class Capability(AWSObject):
    """
    `Capability <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html>`__
    """

    resource_type = "AWS::B2BI::Capability"

    props: PropsDictType = {
        "Configuration": (CapabilityConfiguration, True),
        "InstructionsDocuments": ([S3Location], False),
        "Name": (str, True),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class X12Delimiters(AWSProperty):
    """
    `X12Delimiters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12delimiters.html>`__
    """

    props: PropsDictType = {
        "ComponentSeparator": (str, False),
        "DataElementSeparator": (str, False),
        "SegmentTerminator": (str, False),
    }


class X12FunctionalGroupHeaders(AWSProperty):
    """
    `X12FunctionalGroupHeaders <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12functionalgroupheaders.html>`__
    """

    props: PropsDictType = {
        "ApplicationReceiverCode": (str, False),
        "ApplicationSenderCode": (str, False),
        "ResponsibleAgencyCode": (str, False),
    }


class X12InterchangeControlHeaders(AWSProperty):
    """
    `X12InterchangeControlHeaders <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12interchangecontrolheaders.html>`__
    """

    props: PropsDictType = {
        "AcknowledgmentRequestedCode": (str, False),
        "ReceiverId": (str, False),
        "ReceiverIdQualifier": (str, False),
        "RepetitionSeparator": (str, False),
        "SenderId": (str, False),
        "SenderIdQualifier": (str, False),
        "UsageIndicatorCode": (str, False),
    }


class X12OutboundEdiHeaders(AWSProperty):
    """
    `X12OutboundEdiHeaders <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12outboundediheaders.html>`__
    """

    props: PropsDictType = {
        "Delimiters": (X12Delimiters, False),
        "FunctionalGroupHeaders": (X12FunctionalGroupHeaders, False),
        "InterchangeControlHeaders": (X12InterchangeControlHeaders, False),
        "ValidateEdi": (boolean, False),
    }


class X12Envelope(AWSProperty):
    """
    `X12Envelope <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12envelope.html>`__
    """

    props: PropsDictType = {
        "Common": (X12OutboundEdiHeaders, False),
    }


class OutboundEdiOptions(AWSProperty):
    """
    `OutboundEdiOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-outboundedioptions.html>`__
    """

    props: PropsDictType = {
        "X12": (X12Envelope, True),
    }


class CapabilityOptions(AWSProperty):
    """
    `CapabilityOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-capabilityoptions.html>`__
    """

    props: PropsDictType = {
        "OutboundEdi": (OutboundEdiOptions, False),
    }


class Partnership(AWSObject):
    """
    `Partnership <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html>`__
    """

    resource_type = "AWS::B2BI::Partnership"

    props: PropsDictType = {
        "Capabilities": ([str], True),
        "CapabilityOptions": (CapabilityOptions, False),
        "Email": (str, True),
        "Name": (str, True),
        "Phone": (str, False),
        "ProfileId": (str, True),
        "Tags": (Tags, False),
    }


class Profile(AWSObject):
    """
    `Profile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html>`__
    """

    resource_type = "AWS::B2BI::Profile"

    props: PropsDictType = {
        "BusinessName": (str, True),
        "Email": (str, False),
        "Logging": (str, True),
        "Name": (str, True),
        "Phone": (str, True),
        "Tags": (Tags, False),
    }


class FormatOptions(AWSProperty):
    """
    `FormatOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-formatoptions.html>`__
    """

    props: PropsDictType = {
        "X12": (X12Details, True),
    }


class InputConversion(AWSProperty):
    """
    `InputConversion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-inputconversion.html>`__
    """

    props: PropsDictType = {
        "FormatOptions": (FormatOptions, False),
        "FromFormat": (str, True),
    }


class Mapping(AWSProperty):
    """
    `Mapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-mapping.html>`__
    """

    props: PropsDictType = {
        "Template": (str, False),
        "TemplateLanguage": (str, True),
    }


class OutputConversion(AWSProperty):
    """
    `OutputConversion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-outputconversion.html>`__
    """

    props: PropsDictType = {
        "FormatOptions": (FormatOptions, False),
        "ToFormat": (str, True),
    }


class SampleDocumentKeys(AWSProperty):
    """
    `SampleDocumentKeys <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-sampledocumentkeys.html>`__
    """

    props: PropsDictType = {
        "Input": (str, False),
        "Output": (str, False),
    }


class SampleDocuments(AWSProperty):
    """
    `SampleDocuments <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-sampledocuments.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
        "Keys": ([SampleDocumentKeys], True),
    }


class Transformer(AWSObject):
    """
    `Transformer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html>`__
    """

    resource_type = "AWS::B2BI::Transformer"

    props: PropsDictType = {
        "InputConversion": (InputConversion, False),
        "Mapping": (Mapping, False),
        "Name": (str, True),
        "OutputConversion": (OutputConversion, False),
        "SampleDocuments": (SampleDocuments, False),
        "Status": (str, True),
        "Tags": (Tags, False),
    }
