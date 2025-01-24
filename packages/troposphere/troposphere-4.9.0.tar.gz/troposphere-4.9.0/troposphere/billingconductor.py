# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double


class AccountGrouping(AWSProperty):
    """
    `AccountGrouping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-accountgrouping.html>`__
    """

    props: PropsDictType = {
        "AutoAssociate": (boolean, False),
        "LinkedAccountIds": ([str], True),
    }


class ComputationPreference(AWSProperty):
    """
    `ComputationPreference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-computationpreference.html>`__
    """

    props: PropsDictType = {
        "PricingPlanArn": (str, True),
    }


class BillingGroup(AWSObject):
    """
    `BillingGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html>`__
    """

    resource_type = "AWS::BillingConductor::BillingGroup"

    props: PropsDictType = {
        "AccountGrouping": (AccountGrouping, True),
        "ComputationPreference": (ComputationPreference, True),
        "Description": (str, False),
        "Name": (str, True),
        "PrimaryAccountId": (str, True),
        "Tags": (Tags, False),
    }


class BillingPeriodRange(AWSProperty):
    """
    `BillingPeriodRange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-billingperiodrange.html>`__
    """

    props: PropsDictType = {
        "ExclusiveEndBillingPeriod": (str, False),
        "InclusiveStartBillingPeriod": (str, False),
    }


class CustomLineItemFlatChargeDetails(AWSProperty):
    """
    `CustomLineItemFlatChargeDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails.html>`__
    """

    props: PropsDictType = {
        "ChargeValue": (double, True),
    }


class CustomLineItemPercentageChargeDetails(AWSProperty):
    """
    `CustomLineItemPercentageChargeDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitempercentagechargedetails.html>`__
    """

    props: PropsDictType = {
        "ChildAssociatedResources": ([str], False),
        "PercentageValue": (double, True),
    }


class LineItemFilter(AWSProperty):
    """
    `LineItemFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-lineitemfilter.html>`__
    """

    props: PropsDictType = {
        "Attribute": (str, True),
        "MatchOption": (str, True),
        "Values": ([str], True),
    }


class CustomLineItemChargeDetails(AWSProperty):
    """
    `CustomLineItemChargeDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html>`__
    """

    props: PropsDictType = {
        "Flat": (CustomLineItemFlatChargeDetails, False),
        "LineItemFilters": ([LineItemFilter], False),
        "Percentage": (CustomLineItemPercentageChargeDetails, False),
        "Type": (str, True),
    }


class CustomLineItem(AWSObject):
    """
    `CustomLineItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html>`__
    """

    resource_type = "AWS::BillingConductor::CustomLineItem"

    props: PropsDictType = {
        "AccountId": (str, False),
        "BillingGroupArn": (str, True),
        "BillingPeriodRange": (BillingPeriodRange, False),
        "CustomLineItemChargeDetails": (CustomLineItemChargeDetails, False),
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class PricingPlan(AWSObject):
    """
    `PricingPlan <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html>`__
    """

    resource_type = "AWS::BillingConductor::PricingPlan"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "PricingRuleArns": ([str], False),
        "Tags": (Tags, False),
    }


class FreeTier(AWSProperty):
    """
    `FreeTier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-pricingrule-freetier.html>`__
    """

    props: PropsDictType = {
        "Activated": (boolean, True),
    }


class Tiering(AWSProperty):
    """
    `Tiering <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-pricingrule-tiering.html>`__
    """

    props: PropsDictType = {
        "FreeTier": (FreeTier, False),
    }


class PricingRule(AWSObject):
    """
    `PricingRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html>`__
    """

    resource_type = "AWS::BillingConductor::PricingRule"

    props: PropsDictType = {
        "BillingEntity": (str, False),
        "Description": (str, False),
        "ModifierPercentage": (double, False),
        "Name": (str, True),
        "Operation": (str, False),
        "Scope": (str, True),
        "Service": (str, False),
        "Tags": (Tags, False),
        "Tiering": (Tiering, False),
        "Type": (str, True),
        "UsageType": (str, False),
    }
