# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssocloud.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import APIRequest_pb2 as APIRequest__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0essocloud.proto\x12\x08SsoCloud\x1a\x10\x41PIRequest.proto\"\xd5\x01\n\x14SsoCloudSettingValue\x12\x11\n\tsettingId\x18\x01 \x01(\x04\x12\x13\n\x0bsettingName\x18\x02 \x01(\t\x12\r\n\x05label\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\t\x12%\n\tvalueType\x18\x05 \x01(\x0e\x32\x12.SsoCloud.DataType\x12\x14\n\x0clastModified\x18\x07 \x01(\t\x12\x12\n\nisFromFile\x18\x08 \x01(\x08\x12\x12\n\nisEditable\x18\t \x01(\x08\x12\x12\n\nisRequired\x18\n \x01(\x08\"\x89\x01\n\x15SsoCloudSettingAction\x12\x11\n\tsettingId\x18\x01 \x01(\x04\x12\x13\n\x0bsettingName\x18\x02 \x01(\t\x12\x39\n\toperation\x18\x03 \x01(\x0e\x32&.SsoCloud.SsoCloudSettingOperationType\x12\r\n\x05value\x18\x04 \x01(\t\"\xe1\x01\n\x1cSsoCloudConfigurationRequest\x12\x1c\n\x14ssoServiceProviderId\x18\x01 \x01(\x04\x12\x1c\n\x14ssoSpConfigurationId\x18\x02 \x01(\x04\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x37\n\x13ssoAuthProtocolType\x18\x04 \x01(\x0e\x32\x1a.SsoCloud.AuthProtocolType\x12>\n\x15ssoCloudSettingAction\x18\x05 \x03(\x0b\x32\x1f.SsoCloud.SsoCloudSettingAction\"d\n\x13SsoSharedConfigItem\x12\x1c\n\x14ssoSpConfigurationId\x18\x01 \x01(\x04\x12\x1c\n\x14ssoServiceProviderId\x18\x02 \x01(\x04\x12\x11\n\tssoNodeId\x18\x03 \x01(\x04\"\xad\x02\n\x1dSsoCloudConfigurationResponse\x12\x1c\n\x14ssoServiceProviderId\x18\x01 \x01(\x04\x12\x1c\n\x14ssoSpConfigurationId\x18\x02 \x01(\x04\x12\x14\n\x0c\x65nterpriseId\x18\x03 \x01(\x04\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x10\n\x08protocol\x18\x05 \x01(\t\x12\x14\n\x0clastModified\x18\x06 \x01(\t\x12<\n\x14ssoCloudSettingValue\x18\x07 \x03(\x0b\x32\x1e.SsoCloud.SsoCloudSettingValue\x12\x10\n\x08isShared\x18\x08 \x01(\x08\x12\x34\n\rsharedConfigs\x18\t \x03(\x0b\x32\x1d.SsoCloud.SsoSharedConfigItem\"E\n\x11SsoIdpTypeRequest\x12\x14\n\x0cssoIdpTypeId\x18\x01 \x01(\r\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\r\n\x05label\x18\x03 \x01(\t\"F\n\x12SsoIdpTypeResponse\x12\x14\n\x0cssoIdpTypeId\x18\x01 \x01(\x05\x12\x0b\n\x03tag\x18\x02 \x01(\x05\x12\r\n\x05label\x18\x03 \x01(\x05\"6\n\x16SsoCloudSAMLLogRequest\x12\x1c\n\x14ssoServiceProviderId\x18\x01 \x01(\x04\"\xdc\x01\n\x14SsoCloudSAMLLogEntry\x12\x12\n\nserverTime\x18\x01 \x01(\t\x12\x11\n\tdirection\x18\x02 \x01(\t\x12\x13\n\x0bmessageType\x18\x03 \x01(\t\x12\x15\n\rmessageIssued\x18\x04 \x01(\t\x12\x14\n\x0c\x66romEntityId\x18\x05 \x01(\t\x12\x12\n\nsamlStatus\x18\x06 \x01(\t\x12\x12\n\nrelayState\x18\x07 \x01(\t\x12\x13\n\x0bsamlContent\x18\x08 \x01(\t\x12\x10\n\x08isSigned\x18\t \x01(\x08\x12\x0c\n\x04isOK\x18\n \x01(\x08\"f\n\x17SsoCloudSAMLLogResponse\x12\x1c\n\x14ssoServiceProviderId\x18\x01 \x01(\x04\x12-\n\x05\x65ntry\x18\x02 \x03(\x0b\x32\x1e.SsoCloud.SsoCloudSAMLLogEntry\"b\n$SsoCloudServiceProviderUpdateRequest\x12\x1c\n\x14ssoServiceProviderId\x18\x01 \x01(\x04\x12\x1c\n\x14ssoSpConfigurationId\x18\x02 \x01(\x04\"]\n\x1aSsoCloudIdpMetadataRequest\x12\x1c\n\x14ssoSpConfigurationId\x18\x01 \x01(\x04\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\"\x9b\x01\n!SsoCloudIdpMetadataSupportRequest\x12\x1c\n\x14ssoServiceProviderId\x18\x01 \x01(\x04\x12\x1c\n\x14ssoSpConfigurationId\x18\x02 \x01(\x04\x12\x17\n\x0fssoEnterpriseId\x18\x03 \x01(\x04\x12\x10\n\x08\x66ilename\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\x0c\"F\n&SsoCloudConfigurationValidationRequest\x12\x1c\n\x14ssoSpConfigurationId\x18\x01 \x03(\x04\"]\n\x11ValidationContent\x12\x1c\n\x14ssoSpConfigurationId\x18\x01 \x01(\x04\x12\x14\n\x0cisSuccessful\x18\x02 \x01(\x08\x12\x14\n\x0c\x65rrorMessage\x18\x03 \x03(\t\"a\n\'SsoCloudConfigurationValidationResponse\x12\x36\n\x11validationContent\x18\x01 \x03(\x0b\x32\x1b.SsoCloud.ValidationContent\"O\n/SsoCloudServiceProviderConfigurationListRequest\x12\x1c\n\x14ssoServiceProviderId\x18\x01 \x01(\x04\"u\n\x15\x43onfigurationListItem\x12\x1c\n\x14ssoSpConfigurationId\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nisSelected\x18\x03 \x01(\x08\x12\x1c\n\x14ssoServiceProviderId\x18\x04 \x03(\x04\"n\n0SsoCloudServiceProviderConfigurationListResponse\x12:\n\x11\x63onfigurationItem\x18\x01 \x03(\x0b\x32\x1f.SsoCloud.ConfigurationListItem\"\xbf\x01\n\x0fSsoCloudRequest\x12\x19\n\x11messageSessionUid\x18\x01 \x01(\x0c\x12\x15\n\rclientVersion\x18\x02 \x01(\t\x12\x10\n\x08\x65mbedded\x18\x03 \x01(\x08\x12\x0c\n\x04json\x18\x04 \x01(\x08\x12\x0c\n\x04\x64\x65st\x18\x05 \x01(\t\x12\x14\n\x0cidpSessionId\x18\x06 \x01(\t\x12\x12\n\nforceLogin\x18\x07 \x01(\x08\x12\x10\n\x08username\x18\x08 \x01(\t\x12\x10\n\x08\x64\x65tached\x18\t \x01(\x08\"\xc9\x01\n\x10SsoCloudResponse\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\x12\x19\n\x11messageSessionUid\x18\x02 \x01(\x0c\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x1b\n\x13\x65ncryptedLoginToken\x18\x04 \x01(\x0c\x12\x14\n\x0cproviderName\x18\x05 \x01(\t\x12\x14\n\x0cidpSessionId\x18\x06 \x01(\t\x12\x1d\n\x15\x65ncryptedSessionToken\x18\x07 \x01(\x0c\x12\x12\n\nerrorToken\x18\x08 \x01(\t\"Z\n\x12SsoCloudLogRequest\x12\x1c\n\x14ssoServiceProviderId\x18\x01 \x01(\x04\x12\x13\n\x0bserviceName\x18\x02 \x01(\t\x12\x11\n\tserviceId\x18\x03 \x01(\r\"\x88\x02\n\x0eSamlRelayState\x12\x19\n\x11messageSessionUid\x18\x01 \x01(\x0c\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08\x65mbedded\x18\x03 \x01(\x08\x12\x0c\n\x04json\x18\x04 \x01(\x08\x12\x0e\n\x06\x64\x65stId\x18\x05 \x01(\r\x12\r\n\x05keyId\x18\x06 \x01(\x05\x12<\n\x11supportedLanguage\x18\x07 \x01(\x0e\x32!.Authentication.SupportedLanguage\x12\x10\n\x08\x63hecksum\x18\x08 \x01(\x04\x12\x16\n\x0eisGeneratedUid\x18\t \x01(\x08\x12\x10\n\x08\x64\x65viceId\x18\n \x01(\x03\x12\x10\n\x08\x64\x65tached\x18\x0b \x01(\x08\"q\n\x1eSsoCloudMigrationStatusRequest\x12\x0e\n\x06nodeId\x18\x01 \x01(\x04\x12\x12\n\nfullStatus\x18\x02 \x01(\x08\x12\x1c\n\x14includeMigratedUsers\x18\x03 \x01(\x08\x12\r\n\x05limit\x18\x04 \x01(\x05\"\xe8\x02\n\x1fSsoCloudMigrationStatusResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06nodeId\x18\x03 \x01(\x04\x12\x14\n\x0cssoConnectId\x18\x04 \x01(\x04\x12\x16\n\x0essoConnectName\x18\x05 \x01(\t\x12\x19\n\x11ssoConnectCloudId\x18\x06 \x01(\x04\x12\x1b\n\x13ssoConnectCloudName\x18\x07 \x01(\t\x12\x17\n\x0ftotalUsersCount\x18\x08 \x01(\r\x12\x1a\n\x12usersMigratedCount\x18\t \x01(\r\x12:\n\rmigratedUsers\x18\n \x03(\x0b\x32#.SsoCloud.SsoCloudMigrationUserInfo\x12<\n\x0funmigratedUsers\x18\x0b \x03(\x0b\x32#.SsoCloud.SsoCloudMigrationUserInfo\"`\n\x19SsoCloudMigrationUserInfo\x12\x0e\n\x06userId\x18\x01 \x01(\r\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08\x66ullName\x18\x03 \x01(\t\x12\x12\n\nisMigrated\x18\x04 \x01(\x08*\x1d\n\x10\x41uthProtocolType\x12\t\n\x05SAML2\x10\x00*\x80\x02\n\x08\x44\x61taType\x12\x07\n\x03\x41NY\x10\x00\x12\x0b\n\x07\x42OOLEAN\x10\x01\x12\x0b\n\x07INTEGER\x10\x02\x12\n\n\x06STRING\x10\x03\x12\t\n\x05\x42YTES\x10\x04\x12\x07\n\x03URL\x10\x05\x12.\n*com_keepersecurity_proto_SsoCloud_DataType\x10\x06\x12\x36\n2com_keepersecurity_proto_SsoCloud_AuthProtocolType\x10\x07\x12\x30\n,com_keepersecurity_proto_SsoCloud_SsoIdpType\x10\x08\x12\x08\n\x04LONG\x10\t\x12\r\n\tTIMESTAMP\x10\n*R\n\x1cSsoCloudSettingOperationType\x12\x07\n\x03SET\x10\x00\x12\x07\n\x03GET\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x12\x14\n\x10RESET_TO_DEFAULT\x10\x03*\xd0\x02\n\nSsoIdpType\x12\r\n\tXX_UNUSED\x10\x00\x12\x0b\n\x07GENERIC\x10\x01\x12\x06\n\x02\x46\x35\x10\x02\x12\n\n\x06GOOGLE\x10\x03\x12\x08\n\x04OKTA\x10\x04\x12\x08\n\x04\x41\x44\x46S\x10\x05\x12\t\n\x05\x41ZURE\x10\x06\x12\x0c\n\x08ONELOGIN\x10\x07\x12\x07\n\x03\x41WS\x10\x08\x12\x0c\n\x08\x43\x45NTRIFY\x10\t\x12\x07\n\x03\x44UO\x10\n\x12\x07\n\x03IBM\x10\x0b\x12\r\n\tJUMPCLOUD\x10\x0c\x12\x08\n\x04PING\x10\r\x12\x0b\n\x07PINGONE\x10\x0e\x12\x07\n\x03RSA\x10\x0f\x12\x0e\n\nSECUREAUTH\x10\x10\x12\n\n\x06THALES\x10\x11\x12\t\n\x05\x41UTH0\x10\x12\x12\n\n\x06\x42\x45YOND\x10\x13\x12\x08\n\x04HYPR\x10\x14\x12\n\n\x06PUREID\x10\x15\x12\x07\n\x03SDO\x10\x16\x12\t\n\x05TRAIT\x10\x17\x12\x0c\n\x08TRANSMIT\x10\x18\x12\x0b\n\x07TRUSONA\x10\x19\x12\x0c\n\x08VERIDIUM\x10\x1a\x12\x07\n\x03\x43\x41S\x10\x1b\x42$\n\x18\x63om.keepersecurity.protoB\x08SsoCloudb\x06proto3')

_AUTHPROTOCOLTYPE = DESCRIPTOR.enum_types_by_name['AuthProtocolType']
AuthProtocolType = enum_type_wrapper.EnumTypeWrapper(_AUTHPROTOCOLTYPE)
_DATATYPE = DESCRIPTOR.enum_types_by_name['DataType']
DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
_SSOCLOUDSETTINGOPERATIONTYPE = DESCRIPTOR.enum_types_by_name['SsoCloudSettingOperationType']
SsoCloudSettingOperationType = enum_type_wrapper.EnumTypeWrapper(_SSOCLOUDSETTINGOPERATIONTYPE)
_SSOIDPTYPE = DESCRIPTOR.enum_types_by_name['SsoIdpType']
SsoIdpType = enum_type_wrapper.EnumTypeWrapper(_SSOIDPTYPE)
SAML2 = 0
ANY = 0
BOOLEAN = 1
INTEGER = 2
STRING = 3
BYTES = 4
URL = 5
com_keepersecurity_proto_SsoCloud_DataType = 6
com_keepersecurity_proto_SsoCloud_AuthProtocolType = 7
com_keepersecurity_proto_SsoCloud_SsoIdpType = 8
LONG = 9
TIMESTAMP = 10
SET = 0
GET = 1
DELETE = 2
RESET_TO_DEFAULT = 3
XX_UNUSED = 0
GENERIC = 1
F5 = 2
GOOGLE = 3
OKTA = 4
ADFS = 5
AZURE = 6
ONELOGIN = 7
AWS = 8
CENTRIFY = 9
DUO = 10
IBM = 11
JUMPCLOUD = 12
PING = 13
PINGONE = 14
RSA = 15
SECUREAUTH = 16
THALES = 17
AUTH0 = 18
BEYOND = 19
HYPR = 20
PUREID = 21
SDO = 22
TRAIT = 23
TRANSMIT = 24
TRUSONA = 25
VERIDIUM = 26
CAS = 27


_SSOCLOUDSETTINGVALUE = DESCRIPTOR.message_types_by_name['SsoCloudSettingValue']
_SSOCLOUDSETTINGACTION = DESCRIPTOR.message_types_by_name['SsoCloudSettingAction']
_SSOCLOUDCONFIGURATIONREQUEST = DESCRIPTOR.message_types_by_name['SsoCloudConfigurationRequest']
_SSOSHAREDCONFIGITEM = DESCRIPTOR.message_types_by_name['SsoSharedConfigItem']
_SSOCLOUDCONFIGURATIONRESPONSE = DESCRIPTOR.message_types_by_name['SsoCloudConfigurationResponse']
_SSOIDPTYPEREQUEST = DESCRIPTOR.message_types_by_name['SsoIdpTypeRequest']
_SSOIDPTYPERESPONSE = DESCRIPTOR.message_types_by_name['SsoIdpTypeResponse']
_SSOCLOUDSAMLLOGREQUEST = DESCRIPTOR.message_types_by_name['SsoCloudSAMLLogRequest']
_SSOCLOUDSAMLLOGENTRY = DESCRIPTOR.message_types_by_name['SsoCloudSAMLLogEntry']
_SSOCLOUDSAMLLOGRESPONSE = DESCRIPTOR.message_types_by_name['SsoCloudSAMLLogResponse']
_SSOCLOUDSERVICEPROVIDERUPDATEREQUEST = DESCRIPTOR.message_types_by_name['SsoCloudServiceProviderUpdateRequest']
_SSOCLOUDIDPMETADATAREQUEST = DESCRIPTOR.message_types_by_name['SsoCloudIdpMetadataRequest']
_SSOCLOUDIDPMETADATASUPPORTREQUEST = DESCRIPTOR.message_types_by_name['SsoCloudIdpMetadataSupportRequest']
_SSOCLOUDCONFIGURATIONVALIDATIONREQUEST = DESCRIPTOR.message_types_by_name['SsoCloudConfigurationValidationRequest']
_VALIDATIONCONTENT = DESCRIPTOR.message_types_by_name['ValidationContent']
_SSOCLOUDCONFIGURATIONVALIDATIONRESPONSE = DESCRIPTOR.message_types_by_name['SsoCloudConfigurationValidationResponse']
_SSOCLOUDSERVICEPROVIDERCONFIGURATIONLISTREQUEST = DESCRIPTOR.message_types_by_name['SsoCloudServiceProviderConfigurationListRequest']
_CONFIGURATIONLISTITEM = DESCRIPTOR.message_types_by_name['ConfigurationListItem']
_SSOCLOUDSERVICEPROVIDERCONFIGURATIONLISTRESPONSE = DESCRIPTOR.message_types_by_name['SsoCloudServiceProviderConfigurationListResponse']
_SSOCLOUDREQUEST = DESCRIPTOR.message_types_by_name['SsoCloudRequest']
_SSOCLOUDRESPONSE = DESCRIPTOR.message_types_by_name['SsoCloudResponse']
_SSOCLOUDLOGREQUEST = DESCRIPTOR.message_types_by_name['SsoCloudLogRequest']
_SAMLRELAYSTATE = DESCRIPTOR.message_types_by_name['SamlRelayState']
_SSOCLOUDMIGRATIONSTATUSREQUEST = DESCRIPTOR.message_types_by_name['SsoCloudMigrationStatusRequest']
_SSOCLOUDMIGRATIONSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['SsoCloudMigrationStatusResponse']
_SSOCLOUDMIGRATIONUSERINFO = DESCRIPTOR.message_types_by_name['SsoCloudMigrationUserInfo']
SsoCloudSettingValue = _reflection.GeneratedProtocolMessageType('SsoCloudSettingValue', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDSETTINGVALUE,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudSettingValue)
  })
_sym_db.RegisterMessage(SsoCloudSettingValue)

SsoCloudSettingAction = _reflection.GeneratedProtocolMessageType('SsoCloudSettingAction', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDSETTINGACTION,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudSettingAction)
  })
_sym_db.RegisterMessage(SsoCloudSettingAction)

SsoCloudConfigurationRequest = _reflection.GeneratedProtocolMessageType('SsoCloudConfigurationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDCONFIGURATIONREQUEST,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudConfigurationRequest)
  })
_sym_db.RegisterMessage(SsoCloudConfigurationRequest)

SsoSharedConfigItem = _reflection.GeneratedProtocolMessageType('SsoSharedConfigItem', (_message.Message,), {
  'DESCRIPTOR' : _SSOSHAREDCONFIGITEM,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoSharedConfigItem)
  })
_sym_db.RegisterMessage(SsoSharedConfigItem)

SsoCloudConfigurationResponse = _reflection.GeneratedProtocolMessageType('SsoCloudConfigurationResponse', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDCONFIGURATIONRESPONSE,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudConfigurationResponse)
  })
_sym_db.RegisterMessage(SsoCloudConfigurationResponse)

SsoIdpTypeRequest = _reflection.GeneratedProtocolMessageType('SsoIdpTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SSOIDPTYPEREQUEST,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoIdpTypeRequest)
  })
_sym_db.RegisterMessage(SsoIdpTypeRequest)

SsoIdpTypeResponse = _reflection.GeneratedProtocolMessageType('SsoIdpTypeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SSOIDPTYPERESPONSE,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoIdpTypeResponse)
  })
_sym_db.RegisterMessage(SsoIdpTypeResponse)

SsoCloudSAMLLogRequest = _reflection.GeneratedProtocolMessageType('SsoCloudSAMLLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDSAMLLOGREQUEST,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudSAMLLogRequest)
  })
_sym_db.RegisterMessage(SsoCloudSAMLLogRequest)

SsoCloudSAMLLogEntry = _reflection.GeneratedProtocolMessageType('SsoCloudSAMLLogEntry', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDSAMLLOGENTRY,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudSAMLLogEntry)
  })
_sym_db.RegisterMessage(SsoCloudSAMLLogEntry)

SsoCloudSAMLLogResponse = _reflection.GeneratedProtocolMessageType('SsoCloudSAMLLogResponse', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDSAMLLOGRESPONSE,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudSAMLLogResponse)
  })
_sym_db.RegisterMessage(SsoCloudSAMLLogResponse)

SsoCloudServiceProviderUpdateRequest = _reflection.GeneratedProtocolMessageType('SsoCloudServiceProviderUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDSERVICEPROVIDERUPDATEREQUEST,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudServiceProviderUpdateRequest)
  })
_sym_db.RegisterMessage(SsoCloudServiceProviderUpdateRequest)

SsoCloudIdpMetadataRequest = _reflection.GeneratedProtocolMessageType('SsoCloudIdpMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDIDPMETADATAREQUEST,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudIdpMetadataRequest)
  })
_sym_db.RegisterMessage(SsoCloudIdpMetadataRequest)

SsoCloudIdpMetadataSupportRequest = _reflection.GeneratedProtocolMessageType('SsoCloudIdpMetadataSupportRequest', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDIDPMETADATASUPPORTREQUEST,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudIdpMetadataSupportRequest)
  })
_sym_db.RegisterMessage(SsoCloudIdpMetadataSupportRequest)

SsoCloudConfigurationValidationRequest = _reflection.GeneratedProtocolMessageType('SsoCloudConfigurationValidationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDCONFIGURATIONVALIDATIONREQUEST,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudConfigurationValidationRequest)
  })
_sym_db.RegisterMessage(SsoCloudConfigurationValidationRequest)

ValidationContent = _reflection.GeneratedProtocolMessageType('ValidationContent', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATIONCONTENT,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.ValidationContent)
  })
_sym_db.RegisterMessage(ValidationContent)

SsoCloudConfigurationValidationResponse = _reflection.GeneratedProtocolMessageType('SsoCloudConfigurationValidationResponse', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDCONFIGURATIONVALIDATIONRESPONSE,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudConfigurationValidationResponse)
  })
_sym_db.RegisterMessage(SsoCloudConfigurationValidationResponse)

SsoCloudServiceProviderConfigurationListRequest = _reflection.GeneratedProtocolMessageType('SsoCloudServiceProviderConfigurationListRequest', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDSERVICEPROVIDERCONFIGURATIONLISTREQUEST,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudServiceProviderConfigurationListRequest)
  })
_sym_db.RegisterMessage(SsoCloudServiceProviderConfigurationListRequest)

ConfigurationListItem = _reflection.GeneratedProtocolMessageType('ConfigurationListItem', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONLISTITEM,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.ConfigurationListItem)
  })
_sym_db.RegisterMessage(ConfigurationListItem)

SsoCloudServiceProviderConfigurationListResponse = _reflection.GeneratedProtocolMessageType('SsoCloudServiceProviderConfigurationListResponse', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDSERVICEPROVIDERCONFIGURATIONLISTRESPONSE,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudServiceProviderConfigurationListResponse)
  })
_sym_db.RegisterMessage(SsoCloudServiceProviderConfigurationListResponse)

SsoCloudRequest = _reflection.GeneratedProtocolMessageType('SsoCloudRequest', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDREQUEST,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudRequest)
  })
_sym_db.RegisterMessage(SsoCloudRequest)

SsoCloudResponse = _reflection.GeneratedProtocolMessageType('SsoCloudResponse', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDRESPONSE,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudResponse)
  })
_sym_db.RegisterMessage(SsoCloudResponse)

SsoCloudLogRequest = _reflection.GeneratedProtocolMessageType('SsoCloudLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDLOGREQUEST,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudLogRequest)
  })
_sym_db.RegisterMessage(SsoCloudLogRequest)

SamlRelayState = _reflection.GeneratedProtocolMessageType('SamlRelayState', (_message.Message,), {
  'DESCRIPTOR' : _SAMLRELAYSTATE,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SamlRelayState)
  })
_sym_db.RegisterMessage(SamlRelayState)

SsoCloudMigrationStatusRequest = _reflection.GeneratedProtocolMessageType('SsoCloudMigrationStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDMIGRATIONSTATUSREQUEST,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudMigrationStatusRequest)
  })
_sym_db.RegisterMessage(SsoCloudMigrationStatusRequest)

SsoCloudMigrationStatusResponse = _reflection.GeneratedProtocolMessageType('SsoCloudMigrationStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDMIGRATIONSTATUSRESPONSE,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudMigrationStatusResponse)
  })
_sym_db.RegisterMessage(SsoCloudMigrationStatusResponse)

SsoCloudMigrationUserInfo = _reflection.GeneratedProtocolMessageType('SsoCloudMigrationUserInfo', (_message.Message,), {
  'DESCRIPTOR' : _SSOCLOUDMIGRATIONUSERINFO,
  '__module__' : 'ssocloud_pb2'
  # @@protoc_insertion_point(class_scope:SsoCloud.SsoCloudMigrationUserInfo)
  })
_sym_db.RegisterMessage(SsoCloudMigrationUserInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.keepersecurity.protoB\010SsoCloud'
  _AUTHPROTOCOLTYPE._serialized_start=3826
  _AUTHPROTOCOLTYPE._serialized_end=3855
  _DATATYPE._serialized_start=3858
  _DATATYPE._serialized_end=4114
  _SSOCLOUDSETTINGOPERATIONTYPE._serialized_start=4116
  _SSOCLOUDSETTINGOPERATIONTYPE._serialized_end=4198
  _SSOIDPTYPE._serialized_start=4201
  _SSOIDPTYPE._serialized_end=4537
  _SSOCLOUDSETTINGVALUE._serialized_start=47
  _SSOCLOUDSETTINGVALUE._serialized_end=260
  _SSOCLOUDSETTINGACTION._serialized_start=263
  _SSOCLOUDSETTINGACTION._serialized_end=400
  _SSOCLOUDCONFIGURATIONREQUEST._serialized_start=403
  _SSOCLOUDCONFIGURATIONREQUEST._serialized_end=628
  _SSOSHAREDCONFIGITEM._serialized_start=630
  _SSOSHAREDCONFIGITEM._serialized_end=730
  _SSOCLOUDCONFIGURATIONRESPONSE._serialized_start=733
  _SSOCLOUDCONFIGURATIONRESPONSE._serialized_end=1034
  _SSOIDPTYPEREQUEST._serialized_start=1036
  _SSOIDPTYPEREQUEST._serialized_end=1105
  _SSOIDPTYPERESPONSE._serialized_start=1107
  _SSOIDPTYPERESPONSE._serialized_end=1177
  _SSOCLOUDSAMLLOGREQUEST._serialized_start=1179
  _SSOCLOUDSAMLLOGREQUEST._serialized_end=1233
  _SSOCLOUDSAMLLOGENTRY._serialized_start=1236
  _SSOCLOUDSAMLLOGENTRY._serialized_end=1456
  _SSOCLOUDSAMLLOGRESPONSE._serialized_start=1458
  _SSOCLOUDSAMLLOGRESPONSE._serialized_end=1560
  _SSOCLOUDSERVICEPROVIDERUPDATEREQUEST._serialized_start=1562
  _SSOCLOUDSERVICEPROVIDERUPDATEREQUEST._serialized_end=1660
  _SSOCLOUDIDPMETADATAREQUEST._serialized_start=1662
  _SSOCLOUDIDPMETADATAREQUEST._serialized_end=1755
  _SSOCLOUDIDPMETADATASUPPORTREQUEST._serialized_start=1758
  _SSOCLOUDIDPMETADATASUPPORTREQUEST._serialized_end=1913
  _SSOCLOUDCONFIGURATIONVALIDATIONREQUEST._serialized_start=1915
  _SSOCLOUDCONFIGURATIONVALIDATIONREQUEST._serialized_end=1985
  _VALIDATIONCONTENT._serialized_start=1987
  _VALIDATIONCONTENT._serialized_end=2080
  _SSOCLOUDCONFIGURATIONVALIDATIONRESPONSE._serialized_start=2082
  _SSOCLOUDCONFIGURATIONVALIDATIONRESPONSE._serialized_end=2179
  _SSOCLOUDSERVICEPROVIDERCONFIGURATIONLISTREQUEST._serialized_start=2181
  _SSOCLOUDSERVICEPROVIDERCONFIGURATIONLISTREQUEST._serialized_end=2260
  _CONFIGURATIONLISTITEM._serialized_start=2262
  _CONFIGURATIONLISTITEM._serialized_end=2379
  _SSOCLOUDSERVICEPROVIDERCONFIGURATIONLISTRESPONSE._serialized_start=2381
  _SSOCLOUDSERVICEPROVIDERCONFIGURATIONLISTRESPONSE._serialized_end=2491
  _SSOCLOUDREQUEST._serialized_start=2494
  _SSOCLOUDREQUEST._serialized_end=2685
  _SSOCLOUDRESPONSE._serialized_start=2688
  _SSOCLOUDRESPONSE._serialized_end=2889
  _SSOCLOUDLOGREQUEST._serialized_start=2891
  _SSOCLOUDLOGREQUEST._serialized_end=2981
  _SAMLRELAYSTATE._serialized_start=2984
  _SAMLRELAYSTATE._serialized_end=3248
  _SSOCLOUDMIGRATIONSTATUSREQUEST._serialized_start=3250
  _SSOCLOUDMIGRATIONSTATUSREQUEST._serialized_end=3363
  _SSOCLOUDMIGRATIONSTATUSRESPONSE._serialized_start=3366
  _SSOCLOUDMIGRATIONSTATUSRESPONSE._serialized_end=3726
  _SSOCLOUDMIGRATIONUSERINFO._serialized_start=3728
  _SSOCLOUDMIGRATIONUSERINFO._serialized_end=3824
# @@protoc_insertion_point(module_scope)
