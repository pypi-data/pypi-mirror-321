# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BI.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08\x42I.proto\x12\x02\x42I\"f\n\x1bValidateSessionTokenRequest\x12\x1d\n\x15\x65ncryptedSessionToken\x18\x01 \x01(\x0c\x12\x1c\n\x14returnMcEnterpiseIds\x18\x02 \x01(\x08\x12\n\n\x02ip\x18\x03 \x01(\t\"\xda\x02\n\x1cValidateSessionTokenResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0e\n\x06userId\x18\x02 \x01(\x05\x12\x18\n\x10\x65nterpriseUserId\x18\x03 \x01(\x03\x12\x37\n\x06status\x18\x04 \x01(\x0e\x32\'.BI.ValidateSessionTokenResponse.Status\x12\x15\n\rstatusMessage\x18\x05 \x01(\t\x12\x17\n\x0fmcEnterpriseIds\x18\x06 \x03(\x05\x12\x18\n\x10hasMSPPermission\x18\x07 \x01(\x08\x12\x1e\n\x16\x64\x65letedMcEnterpriseIds\x18\x08 \x03(\x05\"[\n\x06Status\x12\t\n\x05VALID\x10\x00\x12\r\n\tNOT_VALID\x10\x01\x12\x0b\n\x07\x45XPIRED\x10\x02\x12\x0e\n\nIP_BLOCKED\x10\x03\x12\x1a\n\x16INVALID_CLIENT_VERSION\x10\x04\"\x1b\n\x19SubscriptionStatusRequest\"\xa6\x03\n\x1aSubscriptionStatusResponse\x12$\n\x0b\x61utoRenewal\x18\x01 \x01(\x0b\x32\x0f.BI.AutoRenewal\x12/\n\x14\x63urrentPaymentMethod\x18\x02 \x01(\x0b\x32\x11.BI.PaymentMethod\x12\x14\n\x0c\x63heckoutLink\x18\x03 \x01(\t\x12\x19\n\x11licenseCreateDate\x18\x04 \x01(\x03\x12\x15\n\risDistributor\x18\x05 \x01(\x08\x12\x13\n\x0bisLegacyMsp\x18\x06 \x01(\x08\x12&\n\x0clicenseStats\x18\x08 \x03(\x0b\x32\x10.BI.LicenseStats\x12\x35\n\x0egradientStatus\x18\t \x01(\x0e\x32\x1d.BI.GradientIntegrationStatus\x12\x17\n\x0fhideTrialBanner\x18\n \x01(\x08\x12\x1c\n\x14gradientLastSyncDate\x18\x0b \x01(\t\x12\x1c\n\x14gradientNextSyncDate\x18\x0c \x01(\t\x12 \n\x18isGradientMappingPending\x18\r \x01(\x08\"\xd7\x01\n\x0cLicenseStats\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.BI.LicenseStats.Type\x12\x11\n\tavailable\x18\x02 \x01(\x05\x12\x0c\n\x04used\x18\x03 \x01(\x05\"\x80\x01\n\x04Type\x12\x18\n\x14LICENSE_STAT_UNKNOWN\x10\x00\x12\x0c\n\x08MSP_BASE\x10\x01\x12\x0f\n\x0bMC_BUSINESS\x10\x02\x12\x14\n\x10MC_BUSINESS_PLUS\x10\x03\x12\x11\n\rMC_ENTERPRISE\x10\x04\x12\x16\n\x12MC_ENTERPRISE_PLUS\x10\x05\"@\n\x0b\x41utoRenewal\x12\x0e\n\x06nextOn\x18\x01 \x01(\x03\x12\x10\n\x08\x64\x61ysLeft\x18\x02 \x01(\x05\x12\x0f\n\x07isTrial\x18\x03 \x01(\x08\"\x84\x04\n\rPaymentMethod\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.BI.PaymentMethod.Type\x12$\n\x04\x63\x61rd\x18\x02 \x01(\x0b\x32\x16.BI.PaymentMethod.Card\x12$\n\x04sepa\x18\x03 \x01(\x0b\x32\x16.BI.PaymentMethod.Sepa\x12(\n\x06paypal\x18\x04 \x01(\x0b\x32\x18.BI.PaymentMethod.Paypal\x12\x15\n\rfailedBilling\x18\x05 \x01(\x08\x12(\n\x06vendor\x18\x06 \x01(\x0b\x32\x18.BI.PaymentMethod.Vendor\x12\x36\n\rpurchaseOrder\x18\x07 \x01(\x0b\x32\x1f.BI.PaymentMethod.PurchaseOrder\x1a$\n\x04\x43\x61rd\x12\r\n\x05last4\x18\x01 \x01(\t\x12\r\n\x05\x62rand\x18\x02 \x01(\t\x1a&\n\x04Sepa\x12\r\n\x05last4\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\x1a\x08\n\x06Paypal\x1a\x16\n\x06Vendor\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x1d\n\rPurchaseOrder\x12\x0c\n\x04name\x18\x01 \x01(\t\"O\n\x04Type\x12\x08\n\x04\x43\x41RD\x10\x00\x12\x08\n\x04SEPA\x10\x01\x12\n\n\x06PAYPAL\x10\x02\x12\x08\n\x04NONE\x10\x03\x12\n\n\x06VENDOR\x10\x04\x12\x11\n\rPURCHASEORDER\x10\x05\"\x1f\n\x1dSubscriptionMspPricingRequest\"\\\n\x1eSubscriptionMspPricingResponse\x12\x19\n\x06\x61\x64\x64ons\x18\x02 \x03(\x0b\x32\t.BI.Addon\x12\x1f\n\tfilePlans\x18\x03 \x03(\x0b\x32\x0c.BI.FilePlan\"\x1e\n\x1cSubscriptionMcPricingRequest\"|\n\x1dSubscriptionMcPricingResponse\x12\x1f\n\tbasePlans\x18\x01 \x03(\x0b\x32\x0c.BI.BasePlan\x12\x19\n\x06\x61\x64\x64ons\x18\x02 \x03(\x0b\x32\t.BI.Addon\x12\x1f\n\tfilePlans\x18\x03 \x03(\x0b\x32\x0c.BI.FilePlan\".\n\x08\x42\x61sePlan\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x04\x63ost\x18\x02 \x01(\x0b\x32\x08.BI.Cost\"C\n\x05\x41\x64\x64on\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x04\x63ost\x18\x02 \x01(\x0b\x32\x08.BI.Cost\x12\x16\n\x0e\x61mountConsumed\x18\x03 \x01(\x03\".\n\x08\x46ilePlan\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x04\x63ost\x18\x02 \x01(\x0b\x32\x08.BI.Cost\"\xab\x01\n\x04\x43ost\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x01\x12%\n\tamountPer\x18\x04 \x01(\x0e\x32\x12.BI.Cost.AmountPer\x12\x1e\n\x08\x63urrency\x18\x05 \x01(\x0e\x32\x0c.BI.Currency\"L\n\tAmountPer\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05MONTH\x10\x01\x12\x0e\n\nUSER_MONTH\x10\x02\x12\x17\n\x13USER_CONSUMED_MONTH\x10\x03\"\\\n\x14InvoiceSearchRequest\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12\x17\n\x0fstartingAfterId\x18\x02 \x01(\x05\x12\x1d\n\x15\x61llInvoicesUnfiltered\x18\x03 \x01(\x08\"6\n\x15InvoiceSearchResponse\x12\x1d\n\x08invoices\x18\x01 \x03(\x0b\x32\x0b.BI.Invoice\"\xbe\x02\n\x07Invoice\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x15\n\rinvoiceNumber\x18\x02 \x01(\t\x12\x13\n\x0binvoiceDate\x18\x03 \x01(\x03\x12\x14\n\x0clicenseCount\x18\x04 \x01(\x05\x12#\n\ttotalCost\x18\x05 \x01(\x0b\x32\x10.BI.Invoice.Cost\x12%\n\x0binvoiceType\x18\x06 \x01(\x0e\x32\x10.BI.Invoice.Type\x1a\x36\n\x04\x43ost\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x01\x12\x1e\n\x08\x63urrency\x18\x02 \x01(\x0e\x32\x0c.BI.Currency\"a\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\x0b\n\x07RENEWAL\x10\x02\x12\x0b\n\x07UPGRADE\x10\x03\x12\x0b\n\x07RESTORE\x10\x04\x12\x0f\n\x0b\x41SSOCIATION\x10\x05\x12\x0b\n\x07OVERAGE\x10\x06\"/\n\x16InvoiceDownloadRequest\x12\x15\n\rinvoiceNumber\x18\x01 \x01(\t\"9\n\x17InvoiceDownloadResponse\x12\x0c\n\x04link\x18\x01 \x01(\t\x12\x10\n\x08\x66ileName\x18\x02 \x01(\t\"<\n\x1dReportingDailySnapshotRequest\x12\r\n\x05month\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x05\"v\n\x1eReportingDailySnapshotResponse\x12#\n\x07records\x18\x01 \x03(\x0b\x32\x12.BI.SnapshotRecord\x12/\n\rmcEnterprises\x18\x02 \x03(\x0b\x32\x18.BI.SnapshotMcEnterprise\"\xd7\x01\n\x0eSnapshotRecord\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\x03\x12\x16\n\x0emcEnterpriseId\x18\x02 \x01(\x05\x12\x17\n\x0fmaxLicenseCount\x18\x04 \x01(\x05\x12\x19\n\x11maxFilePlanTypeId\x18\x05 \x01(\x05\x12\x15\n\rmaxBasePlanId\x18\x06 \x01(\x05\x12(\n\x06\x61\x64\x64ons\x18\x07 \x03(\x0b\x32\x18.BI.SnapshotRecord.Addon\x1a*\n\x05\x41\x64\x64on\x12\x12\n\nmaxAddonId\x18\x01 \x01(\x05\x12\r\n\x05units\x18\x02 \x01(\x03\"0\n\x14SnapshotMcEnterprise\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x16\n\x14MappingAddonsRequest\"\\\n\x15MappingAddonsResponse\x12\x1f\n\x06\x61\x64\x64ons\x18\x01 \x03(\x0b\x32\x0f.BI.MappingItem\x12\"\n\tfilePlans\x18\x02 \x03(\x0b\x32\x0f.BI.MappingItem\"\'\n\x0bMappingItem\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"1\n\x1aGradientValidateKeyRequest\x12\x13\n\x0bgradientKey\x18\x01 \x01(\t\"?\n\x1bGradientValidateKeyResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"D\n\x13GradientSaveRequest\x12\x13\n\x0bgradientKey\x18\x01 \x01(\t\x12\x18\n\x10\x65nterpriseUserId\x18\x02 \x01(\x03\"g\n\x14GradientSaveResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12-\n\x06status\x18\x02 \x01(\x0e\x32\x1d.BI.GradientIntegrationStatus\x12\x0f\n\x07message\x18\x03 \x01(\t\"1\n\x15GradientRemoveRequest\x12\x18\n\x10\x65nterpriseUserId\x18\x01 \x01(\x03\":\n\x16GradientRemoveResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"/\n\x13GradientSyncRequest\x12\x18\n\x10\x65nterpriseUserId\x18\x01 \x01(\x03\"g\n\x14GradientSyncResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12-\n\x06status\x18\x02 \x01(\x0e\x32\x1d.BI.GradientIntegrationStatus\x12\x0f\n\x07message\x18\x03 \x01(\t\"N\n\'NetPromoterScoreSurveySubmissionRequest\x12\x14\n\x0csurvey_score\x18\x01 \x01(\x05\x12\r\n\x05notes\x18\x02 \x01(\t\"*\n(NetPromoterScoreSurveySubmissionResponse\"&\n$NetPromoterScorePopupScheduleRequest\";\n%NetPromoterScorePopupScheduleResponse\x12\x12\n\nshow_popup\x18\x01 \x01(\x08\"\'\n%NetPromoterScorePopupDismissalRequest\"(\n&NetPromoterScorePopupDismissalResponse\"-\n\x11KCMLicenseRequest\x12\x18\n\x10\x65nterpriseUserId\x18\x01 \x01(\x03\"%\n\x12KCMLicenseResponse\x12\x0f\n\x07message\x18\x01 \x01(\t*D\n\x08\x43urrency\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03USD\x10\x01\x12\x07\n\x03GBP\x10\x02\x12\x07\n\x03JPY\x10\x03\x12\x07\n\x03\x45UR\x10\x04\x12\x07\n\x03\x41UD\x10\x05*S\n\x19GradientIntegrationStatus\x12\x10\n\x0cNOTCONNECTED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\r\n\tCONNECTED\x10\x02\x12\x08\n\x04NONE\x10\x03\x42\x1e\n\x18\x63om.keepersecurity.protoB\x02\x42Ib\x06proto3')

_CURRENCY = DESCRIPTOR.enum_types_by_name['Currency']
Currency = enum_type_wrapper.EnumTypeWrapper(_CURRENCY)
_GRADIENTINTEGRATIONSTATUS = DESCRIPTOR.enum_types_by_name['GradientIntegrationStatus']
GradientIntegrationStatus = enum_type_wrapper.EnumTypeWrapper(_GRADIENTINTEGRATIONSTATUS)
UNKNOWN = 0
USD = 1
GBP = 2
JPY = 3
EUR = 4
AUD = 5
NOTCONNECTED = 0
PENDING = 1
CONNECTED = 2
NONE = 3


_VALIDATESESSIONTOKENREQUEST = DESCRIPTOR.message_types_by_name['ValidateSessionTokenRequest']
_VALIDATESESSIONTOKENRESPONSE = DESCRIPTOR.message_types_by_name['ValidateSessionTokenResponse']
_SUBSCRIPTIONSTATUSREQUEST = DESCRIPTOR.message_types_by_name['SubscriptionStatusRequest']
_SUBSCRIPTIONSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['SubscriptionStatusResponse']
_LICENSESTATS = DESCRIPTOR.message_types_by_name['LicenseStats']
_AUTORENEWAL = DESCRIPTOR.message_types_by_name['AutoRenewal']
_PAYMENTMETHOD = DESCRIPTOR.message_types_by_name['PaymentMethod']
_PAYMENTMETHOD_CARD = _PAYMENTMETHOD.nested_types_by_name['Card']
_PAYMENTMETHOD_SEPA = _PAYMENTMETHOD.nested_types_by_name['Sepa']
_PAYMENTMETHOD_PAYPAL = _PAYMENTMETHOD.nested_types_by_name['Paypal']
_PAYMENTMETHOD_VENDOR = _PAYMENTMETHOD.nested_types_by_name['Vendor']
_PAYMENTMETHOD_PURCHASEORDER = _PAYMENTMETHOD.nested_types_by_name['PurchaseOrder']
_SUBSCRIPTIONMSPPRICINGREQUEST = DESCRIPTOR.message_types_by_name['SubscriptionMspPricingRequest']
_SUBSCRIPTIONMSPPRICINGRESPONSE = DESCRIPTOR.message_types_by_name['SubscriptionMspPricingResponse']
_SUBSCRIPTIONMCPRICINGREQUEST = DESCRIPTOR.message_types_by_name['SubscriptionMcPricingRequest']
_SUBSCRIPTIONMCPRICINGRESPONSE = DESCRIPTOR.message_types_by_name['SubscriptionMcPricingResponse']
_BASEPLAN = DESCRIPTOR.message_types_by_name['BasePlan']
_ADDON = DESCRIPTOR.message_types_by_name['Addon']
_FILEPLAN = DESCRIPTOR.message_types_by_name['FilePlan']
_COST = DESCRIPTOR.message_types_by_name['Cost']
_INVOICESEARCHREQUEST = DESCRIPTOR.message_types_by_name['InvoiceSearchRequest']
_INVOICESEARCHRESPONSE = DESCRIPTOR.message_types_by_name['InvoiceSearchResponse']
_INVOICE = DESCRIPTOR.message_types_by_name['Invoice']
_INVOICE_COST = _INVOICE.nested_types_by_name['Cost']
_INVOICEDOWNLOADREQUEST = DESCRIPTOR.message_types_by_name['InvoiceDownloadRequest']
_INVOICEDOWNLOADRESPONSE = DESCRIPTOR.message_types_by_name['InvoiceDownloadResponse']
_REPORTINGDAILYSNAPSHOTREQUEST = DESCRIPTOR.message_types_by_name['ReportingDailySnapshotRequest']
_REPORTINGDAILYSNAPSHOTRESPONSE = DESCRIPTOR.message_types_by_name['ReportingDailySnapshotResponse']
_SNAPSHOTRECORD = DESCRIPTOR.message_types_by_name['SnapshotRecord']
_SNAPSHOTRECORD_ADDON = _SNAPSHOTRECORD.nested_types_by_name['Addon']
_SNAPSHOTMCENTERPRISE = DESCRIPTOR.message_types_by_name['SnapshotMcEnterprise']
_MAPPINGADDONSREQUEST = DESCRIPTOR.message_types_by_name['MappingAddonsRequest']
_MAPPINGADDONSRESPONSE = DESCRIPTOR.message_types_by_name['MappingAddonsResponse']
_MAPPINGITEM = DESCRIPTOR.message_types_by_name['MappingItem']
_GRADIENTVALIDATEKEYREQUEST = DESCRIPTOR.message_types_by_name['GradientValidateKeyRequest']
_GRADIENTVALIDATEKEYRESPONSE = DESCRIPTOR.message_types_by_name['GradientValidateKeyResponse']
_GRADIENTSAVEREQUEST = DESCRIPTOR.message_types_by_name['GradientSaveRequest']
_GRADIENTSAVERESPONSE = DESCRIPTOR.message_types_by_name['GradientSaveResponse']
_GRADIENTREMOVEREQUEST = DESCRIPTOR.message_types_by_name['GradientRemoveRequest']
_GRADIENTREMOVERESPONSE = DESCRIPTOR.message_types_by_name['GradientRemoveResponse']
_GRADIENTSYNCREQUEST = DESCRIPTOR.message_types_by_name['GradientSyncRequest']
_GRADIENTSYNCRESPONSE = DESCRIPTOR.message_types_by_name['GradientSyncResponse']
_NETPROMOTERSCORESURVEYSUBMISSIONREQUEST = DESCRIPTOR.message_types_by_name['NetPromoterScoreSurveySubmissionRequest']
_NETPROMOTERSCORESURVEYSUBMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['NetPromoterScoreSurveySubmissionResponse']
_NETPROMOTERSCOREPOPUPSCHEDULEREQUEST = DESCRIPTOR.message_types_by_name['NetPromoterScorePopupScheduleRequest']
_NETPROMOTERSCOREPOPUPSCHEDULERESPONSE = DESCRIPTOR.message_types_by_name['NetPromoterScorePopupScheduleResponse']
_NETPROMOTERSCOREPOPUPDISMISSALREQUEST = DESCRIPTOR.message_types_by_name['NetPromoterScorePopupDismissalRequest']
_NETPROMOTERSCOREPOPUPDISMISSALRESPONSE = DESCRIPTOR.message_types_by_name['NetPromoterScorePopupDismissalResponse']
_KCMLICENSEREQUEST = DESCRIPTOR.message_types_by_name['KCMLicenseRequest']
_KCMLICENSERESPONSE = DESCRIPTOR.message_types_by_name['KCMLicenseResponse']
_VALIDATESESSIONTOKENRESPONSE_STATUS = _VALIDATESESSIONTOKENRESPONSE.enum_types_by_name['Status']
_LICENSESTATS_TYPE = _LICENSESTATS.enum_types_by_name['Type']
_PAYMENTMETHOD_TYPE = _PAYMENTMETHOD.enum_types_by_name['Type']
_COST_AMOUNTPER = _COST.enum_types_by_name['AmountPer']
_INVOICE_TYPE = _INVOICE.enum_types_by_name['Type']
ValidateSessionTokenRequest = _reflection.GeneratedProtocolMessageType('ValidateSessionTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATESESSIONTOKENREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.ValidateSessionTokenRequest)
  })
_sym_db.RegisterMessage(ValidateSessionTokenRequest)

ValidateSessionTokenResponse = _reflection.GeneratedProtocolMessageType('ValidateSessionTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATESESSIONTOKENRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.ValidateSessionTokenResponse)
  })
_sym_db.RegisterMessage(ValidateSessionTokenResponse)

SubscriptionStatusRequest = _reflection.GeneratedProtocolMessageType('SubscriptionStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONSTATUSREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionStatusRequest)
  })
_sym_db.RegisterMessage(SubscriptionStatusRequest)

SubscriptionStatusResponse = _reflection.GeneratedProtocolMessageType('SubscriptionStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONSTATUSRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionStatusResponse)
  })
_sym_db.RegisterMessage(SubscriptionStatusResponse)

LicenseStats = _reflection.GeneratedProtocolMessageType('LicenseStats', (_message.Message,), {
  'DESCRIPTOR' : _LICENSESTATS,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.LicenseStats)
  })
_sym_db.RegisterMessage(LicenseStats)

AutoRenewal = _reflection.GeneratedProtocolMessageType('AutoRenewal', (_message.Message,), {
  'DESCRIPTOR' : _AUTORENEWAL,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.AutoRenewal)
  })
_sym_db.RegisterMessage(AutoRenewal)

PaymentMethod = _reflection.GeneratedProtocolMessageType('PaymentMethod', (_message.Message,), {

  'Card' : _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), {
    'DESCRIPTOR' : _PAYMENTMETHOD_CARD,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.PaymentMethod.Card)
    })
  ,

  'Sepa' : _reflection.GeneratedProtocolMessageType('Sepa', (_message.Message,), {
    'DESCRIPTOR' : _PAYMENTMETHOD_SEPA,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.PaymentMethod.Sepa)
    })
  ,

  'Paypal' : _reflection.GeneratedProtocolMessageType('Paypal', (_message.Message,), {
    'DESCRIPTOR' : _PAYMENTMETHOD_PAYPAL,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.PaymentMethod.Paypal)
    })
  ,

  'Vendor' : _reflection.GeneratedProtocolMessageType('Vendor', (_message.Message,), {
    'DESCRIPTOR' : _PAYMENTMETHOD_VENDOR,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.PaymentMethod.Vendor)
    })
  ,

  'PurchaseOrder' : _reflection.GeneratedProtocolMessageType('PurchaseOrder', (_message.Message,), {
    'DESCRIPTOR' : _PAYMENTMETHOD_PURCHASEORDER,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.PaymentMethod.PurchaseOrder)
    })
  ,
  'DESCRIPTOR' : _PAYMENTMETHOD,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.PaymentMethod)
  })
_sym_db.RegisterMessage(PaymentMethod)
_sym_db.RegisterMessage(PaymentMethod.Card)
_sym_db.RegisterMessage(PaymentMethod.Sepa)
_sym_db.RegisterMessage(PaymentMethod.Paypal)
_sym_db.RegisterMessage(PaymentMethod.Vendor)
_sym_db.RegisterMessage(PaymentMethod.PurchaseOrder)

SubscriptionMspPricingRequest = _reflection.GeneratedProtocolMessageType('SubscriptionMspPricingRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONMSPPRICINGREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionMspPricingRequest)
  })
_sym_db.RegisterMessage(SubscriptionMspPricingRequest)

SubscriptionMspPricingResponse = _reflection.GeneratedProtocolMessageType('SubscriptionMspPricingResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONMSPPRICINGRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionMspPricingResponse)
  })
_sym_db.RegisterMessage(SubscriptionMspPricingResponse)

SubscriptionMcPricingRequest = _reflection.GeneratedProtocolMessageType('SubscriptionMcPricingRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONMCPRICINGREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionMcPricingRequest)
  })
_sym_db.RegisterMessage(SubscriptionMcPricingRequest)

SubscriptionMcPricingResponse = _reflection.GeneratedProtocolMessageType('SubscriptionMcPricingResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONMCPRICINGRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SubscriptionMcPricingResponse)
  })
_sym_db.RegisterMessage(SubscriptionMcPricingResponse)

BasePlan = _reflection.GeneratedProtocolMessageType('BasePlan', (_message.Message,), {
  'DESCRIPTOR' : _BASEPLAN,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.BasePlan)
  })
_sym_db.RegisterMessage(BasePlan)

Addon = _reflection.GeneratedProtocolMessageType('Addon', (_message.Message,), {
  'DESCRIPTOR' : _ADDON,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.Addon)
  })
_sym_db.RegisterMessage(Addon)

FilePlan = _reflection.GeneratedProtocolMessageType('FilePlan', (_message.Message,), {
  'DESCRIPTOR' : _FILEPLAN,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.FilePlan)
  })
_sym_db.RegisterMessage(FilePlan)

Cost = _reflection.GeneratedProtocolMessageType('Cost', (_message.Message,), {
  'DESCRIPTOR' : _COST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.Cost)
  })
_sym_db.RegisterMessage(Cost)

InvoiceSearchRequest = _reflection.GeneratedProtocolMessageType('InvoiceSearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVOICESEARCHREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.InvoiceSearchRequest)
  })
_sym_db.RegisterMessage(InvoiceSearchRequest)

InvoiceSearchResponse = _reflection.GeneratedProtocolMessageType('InvoiceSearchResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVOICESEARCHRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.InvoiceSearchResponse)
  })
_sym_db.RegisterMessage(InvoiceSearchResponse)

Invoice = _reflection.GeneratedProtocolMessageType('Invoice', (_message.Message,), {

  'Cost' : _reflection.GeneratedProtocolMessageType('Cost', (_message.Message,), {
    'DESCRIPTOR' : _INVOICE_COST,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.Invoice.Cost)
    })
  ,
  'DESCRIPTOR' : _INVOICE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.Invoice)
  })
_sym_db.RegisterMessage(Invoice)
_sym_db.RegisterMessage(Invoice.Cost)

InvoiceDownloadRequest = _reflection.GeneratedProtocolMessageType('InvoiceDownloadRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVOICEDOWNLOADREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.InvoiceDownloadRequest)
  })
_sym_db.RegisterMessage(InvoiceDownloadRequest)

InvoiceDownloadResponse = _reflection.GeneratedProtocolMessageType('InvoiceDownloadResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVOICEDOWNLOADRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.InvoiceDownloadResponse)
  })
_sym_db.RegisterMessage(InvoiceDownloadResponse)

ReportingDailySnapshotRequest = _reflection.GeneratedProtocolMessageType('ReportingDailySnapshotRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTINGDAILYSNAPSHOTREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.ReportingDailySnapshotRequest)
  })
_sym_db.RegisterMessage(ReportingDailySnapshotRequest)

ReportingDailySnapshotResponse = _reflection.GeneratedProtocolMessageType('ReportingDailySnapshotResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPORTINGDAILYSNAPSHOTRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.ReportingDailySnapshotResponse)
  })
_sym_db.RegisterMessage(ReportingDailySnapshotResponse)

SnapshotRecord = _reflection.GeneratedProtocolMessageType('SnapshotRecord', (_message.Message,), {

  'Addon' : _reflection.GeneratedProtocolMessageType('Addon', (_message.Message,), {
    'DESCRIPTOR' : _SNAPSHOTRECORD_ADDON,
    '__module__' : 'BI_pb2'
    # @@protoc_insertion_point(class_scope:BI.SnapshotRecord.Addon)
    })
  ,
  'DESCRIPTOR' : _SNAPSHOTRECORD,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SnapshotRecord)
  })
_sym_db.RegisterMessage(SnapshotRecord)
_sym_db.RegisterMessage(SnapshotRecord.Addon)

SnapshotMcEnterprise = _reflection.GeneratedProtocolMessageType('SnapshotMcEnterprise', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTMCENTERPRISE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.SnapshotMcEnterprise)
  })
_sym_db.RegisterMessage(SnapshotMcEnterprise)

MappingAddonsRequest = _reflection.GeneratedProtocolMessageType('MappingAddonsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAPPINGADDONSREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.MappingAddonsRequest)
  })
_sym_db.RegisterMessage(MappingAddonsRequest)

MappingAddonsResponse = _reflection.GeneratedProtocolMessageType('MappingAddonsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAPPINGADDONSRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.MappingAddonsResponse)
  })
_sym_db.RegisterMessage(MappingAddonsResponse)

MappingItem = _reflection.GeneratedProtocolMessageType('MappingItem', (_message.Message,), {
  'DESCRIPTOR' : _MAPPINGITEM,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.MappingItem)
  })
_sym_db.RegisterMessage(MappingItem)

GradientValidateKeyRequest = _reflection.GeneratedProtocolMessageType('GradientValidateKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTVALIDATEKEYREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientValidateKeyRequest)
  })
_sym_db.RegisterMessage(GradientValidateKeyRequest)

GradientValidateKeyResponse = _reflection.GeneratedProtocolMessageType('GradientValidateKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTVALIDATEKEYRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientValidateKeyResponse)
  })
_sym_db.RegisterMessage(GradientValidateKeyResponse)

GradientSaveRequest = _reflection.GeneratedProtocolMessageType('GradientSaveRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTSAVEREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientSaveRequest)
  })
_sym_db.RegisterMessage(GradientSaveRequest)

GradientSaveResponse = _reflection.GeneratedProtocolMessageType('GradientSaveResponse', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTSAVERESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientSaveResponse)
  })
_sym_db.RegisterMessage(GradientSaveResponse)

GradientRemoveRequest = _reflection.GeneratedProtocolMessageType('GradientRemoveRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTREMOVEREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientRemoveRequest)
  })
_sym_db.RegisterMessage(GradientRemoveRequest)

GradientRemoveResponse = _reflection.GeneratedProtocolMessageType('GradientRemoveResponse', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTREMOVERESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientRemoveResponse)
  })
_sym_db.RegisterMessage(GradientRemoveResponse)

GradientSyncRequest = _reflection.GeneratedProtocolMessageType('GradientSyncRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTSYNCREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientSyncRequest)
  })
_sym_db.RegisterMessage(GradientSyncRequest)

GradientSyncResponse = _reflection.GeneratedProtocolMessageType('GradientSyncResponse', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTSYNCRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.GradientSyncResponse)
  })
_sym_db.RegisterMessage(GradientSyncResponse)

NetPromoterScoreSurveySubmissionRequest = _reflection.GeneratedProtocolMessageType('NetPromoterScoreSurveySubmissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _NETPROMOTERSCORESURVEYSUBMISSIONREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.NetPromoterScoreSurveySubmissionRequest)
  })
_sym_db.RegisterMessage(NetPromoterScoreSurveySubmissionRequest)

NetPromoterScoreSurveySubmissionResponse = _reflection.GeneratedProtocolMessageType('NetPromoterScoreSurveySubmissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _NETPROMOTERSCORESURVEYSUBMISSIONRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.NetPromoterScoreSurveySubmissionResponse)
  })
_sym_db.RegisterMessage(NetPromoterScoreSurveySubmissionResponse)

NetPromoterScorePopupScheduleRequest = _reflection.GeneratedProtocolMessageType('NetPromoterScorePopupScheduleRequest', (_message.Message,), {
  'DESCRIPTOR' : _NETPROMOTERSCOREPOPUPSCHEDULEREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.NetPromoterScorePopupScheduleRequest)
  })
_sym_db.RegisterMessage(NetPromoterScorePopupScheduleRequest)

NetPromoterScorePopupScheduleResponse = _reflection.GeneratedProtocolMessageType('NetPromoterScorePopupScheduleResponse', (_message.Message,), {
  'DESCRIPTOR' : _NETPROMOTERSCOREPOPUPSCHEDULERESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.NetPromoterScorePopupScheduleResponse)
  })
_sym_db.RegisterMessage(NetPromoterScorePopupScheduleResponse)

NetPromoterScorePopupDismissalRequest = _reflection.GeneratedProtocolMessageType('NetPromoterScorePopupDismissalRequest', (_message.Message,), {
  'DESCRIPTOR' : _NETPROMOTERSCOREPOPUPDISMISSALREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.NetPromoterScorePopupDismissalRequest)
  })
_sym_db.RegisterMessage(NetPromoterScorePopupDismissalRequest)

NetPromoterScorePopupDismissalResponse = _reflection.GeneratedProtocolMessageType('NetPromoterScorePopupDismissalResponse', (_message.Message,), {
  'DESCRIPTOR' : _NETPROMOTERSCOREPOPUPDISMISSALRESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.NetPromoterScorePopupDismissalResponse)
  })
_sym_db.RegisterMessage(NetPromoterScorePopupDismissalResponse)

KCMLicenseRequest = _reflection.GeneratedProtocolMessageType('KCMLicenseRequest', (_message.Message,), {
  'DESCRIPTOR' : _KCMLICENSEREQUEST,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.KCMLicenseRequest)
  })
_sym_db.RegisterMessage(KCMLicenseRequest)

KCMLicenseResponse = _reflection.GeneratedProtocolMessageType('KCMLicenseResponse', (_message.Message,), {
  'DESCRIPTOR' : _KCMLICENSERESPONSE,
  '__module__' : 'BI_pb2'
  # @@protoc_insertion_point(class_scope:BI.KCMLicenseResponse)
  })
_sym_db.RegisterMessage(KCMLicenseResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.keepersecurity.protoB\002BI'
  _CURRENCY._serialized_start=4488
  _CURRENCY._serialized_end=4556
  _GRADIENTINTEGRATIONSTATUS._serialized_start=4558
  _GRADIENTINTEGRATIONSTATUS._serialized_end=4641
  _VALIDATESESSIONTOKENREQUEST._serialized_start=16
  _VALIDATESESSIONTOKENREQUEST._serialized_end=118
  _VALIDATESESSIONTOKENRESPONSE._serialized_start=121
  _VALIDATESESSIONTOKENRESPONSE._serialized_end=467
  _VALIDATESESSIONTOKENRESPONSE_STATUS._serialized_start=376
  _VALIDATESESSIONTOKENRESPONSE_STATUS._serialized_end=467
  _SUBSCRIPTIONSTATUSREQUEST._serialized_start=469
  _SUBSCRIPTIONSTATUSREQUEST._serialized_end=496
  _SUBSCRIPTIONSTATUSRESPONSE._serialized_start=499
  _SUBSCRIPTIONSTATUSRESPONSE._serialized_end=921
  _LICENSESTATS._serialized_start=924
  _LICENSESTATS._serialized_end=1139
  _LICENSESTATS_TYPE._serialized_start=1011
  _LICENSESTATS_TYPE._serialized_end=1139
  _AUTORENEWAL._serialized_start=1141
  _AUTORENEWAL._serialized_end=1205
  _PAYMENTMETHOD._serialized_start=1208
  _PAYMENTMETHOD._serialized_end=1724
  _PAYMENTMETHOD_CARD._serialized_start=1502
  _PAYMENTMETHOD_CARD._serialized_end=1538
  _PAYMENTMETHOD_SEPA._serialized_start=1540
  _PAYMENTMETHOD_SEPA._serialized_end=1578
  _PAYMENTMETHOD_PAYPAL._serialized_start=1580
  _PAYMENTMETHOD_PAYPAL._serialized_end=1588
  _PAYMENTMETHOD_VENDOR._serialized_start=1590
  _PAYMENTMETHOD_VENDOR._serialized_end=1612
  _PAYMENTMETHOD_PURCHASEORDER._serialized_start=1614
  _PAYMENTMETHOD_PURCHASEORDER._serialized_end=1643
  _PAYMENTMETHOD_TYPE._serialized_start=1645
  _PAYMENTMETHOD_TYPE._serialized_end=1724
  _SUBSCRIPTIONMSPPRICINGREQUEST._serialized_start=1726
  _SUBSCRIPTIONMSPPRICINGREQUEST._serialized_end=1757
  _SUBSCRIPTIONMSPPRICINGRESPONSE._serialized_start=1759
  _SUBSCRIPTIONMSPPRICINGRESPONSE._serialized_end=1851
  _SUBSCRIPTIONMCPRICINGREQUEST._serialized_start=1853
  _SUBSCRIPTIONMCPRICINGREQUEST._serialized_end=1883
  _SUBSCRIPTIONMCPRICINGRESPONSE._serialized_start=1885
  _SUBSCRIPTIONMCPRICINGRESPONSE._serialized_end=2009
  _BASEPLAN._serialized_start=2011
  _BASEPLAN._serialized_end=2057
  _ADDON._serialized_start=2059
  _ADDON._serialized_end=2126
  _FILEPLAN._serialized_start=2128
  _FILEPLAN._serialized_end=2174
  _COST._serialized_start=2177
  _COST._serialized_end=2348
  _COST_AMOUNTPER._serialized_start=2272
  _COST_AMOUNTPER._serialized_end=2348
  _INVOICESEARCHREQUEST._serialized_start=2350
  _INVOICESEARCHREQUEST._serialized_end=2442
  _INVOICESEARCHRESPONSE._serialized_start=2444
  _INVOICESEARCHRESPONSE._serialized_end=2498
  _INVOICE._serialized_start=2501
  _INVOICE._serialized_end=2819
  _INVOICE_COST._serialized_start=2666
  _INVOICE_COST._serialized_end=2720
  _INVOICE_TYPE._serialized_start=2722
  _INVOICE_TYPE._serialized_end=2819
  _INVOICEDOWNLOADREQUEST._serialized_start=2821
  _INVOICEDOWNLOADREQUEST._serialized_end=2868
  _INVOICEDOWNLOADRESPONSE._serialized_start=2870
  _INVOICEDOWNLOADRESPONSE._serialized_end=2927
  _REPORTINGDAILYSNAPSHOTREQUEST._serialized_start=2929
  _REPORTINGDAILYSNAPSHOTREQUEST._serialized_end=2989
  _REPORTINGDAILYSNAPSHOTRESPONSE._serialized_start=2991
  _REPORTINGDAILYSNAPSHOTRESPONSE._serialized_end=3109
  _SNAPSHOTRECORD._serialized_start=3112
  _SNAPSHOTRECORD._serialized_end=3327
  _SNAPSHOTRECORD_ADDON._serialized_start=3285
  _SNAPSHOTRECORD_ADDON._serialized_end=3327
  _SNAPSHOTMCENTERPRISE._serialized_start=3329
  _SNAPSHOTMCENTERPRISE._serialized_end=3377
  _MAPPINGADDONSREQUEST._serialized_start=3379
  _MAPPINGADDONSREQUEST._serialized_end=3401
  _MAPPINGADDONSRESPONSE._serialized_start=3403
  _MAPPINGADDONSRESPONSE._serialized_end=3495
  _MAPPINGITEM._serialized_start=3497
  _MAPPINGITEM._serialized_end=3536
  _GRADIENTVALIDATEKEYREQUEST._serialized_start=3538
  _GRADIENTVALIDATEKEYREQUEST._serialized_end=3587
  _GRADIENTVALIDATEKEYRESPONSE._serialized_start=3589
  _GRADIENTVALIDATEKEYRESPONSE._serialized_end=3652
  _GRADIENTSAVEREQUEST._serialized_start=3654
  _GRADIENTSAVEREQUEST._serialized_end=3722
  _GRADIENTSAVERESPONSE._serialized_start=3724
  _GRADIENTSAVERESPONSE._serialized_end=3827
  _GRADIENTREMOVEREQUEST._serialized_start=3829
  _GRADIENTREMOVEREQUEST._serialized_end=3878
  _GRADIENTREMOVERESPONSE._serialized_start=3880
  _GRADIENTREMOVERESPONSE._serialized_end=3938
  _GRADIENTSYNCREQUEST._serialized_start=3940
  _GRADIENTSYNCREQUEST._serialized_end=3987
  _GRADIENTSYNCRESPONSE._serialized_start=3989
  _GRADIENTSYNCRESPONSE._serialized_end=4092
  _NETPROMOTERSCORESURVEYSUBMISSIONREQUEST._serialized_start=4094
  _NETPROMOTERSCORESURVEYSUBMISSIONREQUEST._serialized_end=4172
  _NETPROMOTERSCORESURVEYSUBMISSIONRESPONSE._serialized_start=4174
  _NETPROMOTERSCORESURVEYSUBMISSIONRESPONSE._serialized_end=4216
  _NETPROMOTERSCOREPOPUPSCHEDULEREQUEST._serialized_start=4218
  _NETPROMOTERSCOREPOPUPSCHEDULEREQUEST._serialized_end=4256
  _NETPROMOTERSCOREPOPUPSCHEDULERESPONSE._serialized_start=4258
  _NETPROMOTERSCOREPOPUPSCHEDULERESPONSE._serialized_end=4317
  _NETPROMOTERSCOREPOPUPDISMISSALREQUEST._serialized_start=4319
  _NETPROMOTERSCOREPOPUPDISMISSALREQUEST._serialized_end=4358
  _NETPROMOTERSCOREPOPUPDISMISSALRESPONSE._serialized_start=4360
  _NETPROMOTERSCOREPOPUPDISMISSALRESPONSE._serialized_end=4400
  _KCMLICENSEREQUEST._serialized_start=4402
  _KCMLICENSEREQUEST._serialized_end=4447
  _KCMLICENSERESPONSE._serialized_start=4449
  _KCMLICENSERESPONSE._serialized_end=4486
# @@protoc_insertion_point(module_scope)
