# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: mgmt/v1alpha1/user_account.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'mgmt/v1alpha1/user_account.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n mgmt/v1alpha1/user_account.proto\x12\rmgmt.v1alpha1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x10\n\x0eGetUserRequest\"*\n\x0fGetUserResponse\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\x10\n\x0eSetUserRequest\"*\n\x0fSetUserResponse\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\x18\n\x16GetUserAccountsRequest\"Q\n\x17GetUserAccountsResponse\x12\x36\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32\x1a.mgmt.v1alpha1.UserAccountR\x08\x61\x63\x63ounts\"\x9a\x01\n\x0bUserAccount\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x32\n\x04type\x18\x03 \x01(\x0e\x32\x1e.mgmt.v1alpha1.UserAccountTypeR\x04type\x12\x33\n\x16has_stripe_customer_id\x18\x04 \x01(\x08R\x13hasStripeCustomerId\"\x91\x01\n#ConvertPersonalToTeamAccountRequest\x12-\n\x04name\x18\x01 \x01(\tB\x19\xbaH\x16r\x14\x32\x12^[a-z0-9-]{3,100}$R\x04name\x12,\n\naccount_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01H\x00R\taccountId\x88\x01\x01\x42\r\n\x0b_account_id\"\xcc\x01\n$ConvertPersonalToTeamAccountResponse\x12\x1d\n\naccount_id\x18\x01 \x01(\tR\taccountId\x12\x35\n\x14\x63heckout_session_url\x18\x02 \x01(\tH\x00R\x12\x63heckoutSessionUrl\x88\x01\x01\x12\x35\n\x17new_personal_account_id\x18\x03 \x01(\tR\x14newPersonalAccountIdB\x17\n\x15_checkout_session_url\"\x1b\n\x19SetPersonalAccountRequest\";\n\x1aSetPersonalAccountResponse\x12\x1d\n\naccount_id\x18\x01 \x01(\tR\taccountId\"A\n\x16IsUserInAccountRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\")\n\x17IsUserInAccountResponse\x12\x0e\n\x02ok\x18\x01 \x01(\x08R\x02ok\"J\n\x1fGetAccountTemporalConfigRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\"`\n GetAccountTemporalConfigResponse\x12<\n\x06\x63onfig\x18\x01 \x01(\x0b\x32$.mgmt.v1alpha1.AccountTemporalConfigR\x06\x63onfig\"\x88\x01\n\x1fSetAccountTemporalConfigRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12<\n\x06\x63onfig\x18\x02 \x01(\x0b\x32$.mgmt.v1alpha1.AccountTemporalConfigR\x06\x63onfig\"`\n SetAccountTemporalConfigResponse\x12<\n\x06\x63onfig\x18\x01 \x01(\x0b\x32$.mgmt.v1alpha1.AccountTemporalConfigR\x06\x63onfig\"\x91\x01\n\x15\x41\x63\x63ountTemporalConfig\x12\x19\n\x03url\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x03url\x12%\n\tnamespace\x18\x02 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\tnamespace\x12\x36\n\x13sync_job_queue_name\x18\x03 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x10syncJobQueueName\"I\n\x18\x43reateTeamAccountRequest\x12-\n\x04name\x18\x01 \x01(\tB\x19\xbaH\x16r\x14\x32\x12^[a-z0-9-]{3,100}$R\x04name\"\x8a\x01\n\x19\x43reateTeamAccountResponse\x12\x1d\n\naccount_id\x18\x01 \x01(\tR\taccountId\x12\x35\n\x14\x63heckout_session_url\x18\x02 \x01(\tH\x00R\x12\x63heckoutSessionUrl\x88\x01\x01\x42\x17\n\x15_checkout_session_url\"\x8d\x01\n\x0b\x41\x63\x63ountUser\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x14\n\x05image\x18\x03 \x01(\tR\x05image\x12\x14\n\x05\x65mail\x18\x04 \x01(\tR\x05\x65mail\x12.\n\x04role\x18\x05 \x01(\x0e\x32\x1a.mgmt.v1alpha1.AccountRoleR\x04role\"G\n\x1cGetTeamAccountMembersRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\"Q\n\x1dGetTeamAccountMembersResponse\x12\x30\n\x05users\x18\x01 \x03(\x0b\x32\x1a.mgmt.v1alpha1.AccountUserR\x05users\"l\n\x1eRemoveTeamAccountMemberRequest\x12!\n\x07user_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\x06userId\x12\'\n\naccount_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\"!\n\x1fRemoveTeamAccountMemberResponse\"\xa6\x01\n\x1eInviteUserToTeamAccountRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\x1d\n\x05\x65mail\x18\x02 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x05\x65mail\x12\x33\n\x04role\x18\x03 \x01(\x0e\x32\x1a.mgmt.v1alpha1.AccountRoleH\x00R\x04role\x88\x01\x01\x42\x07\n\x05_role\"\x8d\x03\n\rAccountInvite\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\naccount_id\x18\x02 \x01(\tR\taccountId\x12$\n\x0esender_user_id\x18\x03 \x01(\tR\x0csenderUserId\x12\x14\n\x05\x65mail\x18\x04 \x01(\tR\x05\x65mail\x12\x14\n\x05token\x18\x05 \x01(\tR\x05token\x12\x1a\n\x08\x61\x63\x63\x65pted\x18\x06 \x01(\x08R\x08\x61\x63\x63\x65pted\x12\x39\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12\x39\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tupdatedAt\x12\x39\n\nexpires_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt\x12.\n\x04role\x18\n \x01(\x0e\x32\x1a.mgmt.v1alpha1.AccountRoleR\x04role\"W\n\x1fInviteUserToTeamAccountResponse\x12\x34\n\x06invite\x18\x01 \x01(\x0b\x32\x1c.mgmt.v1alpha1.AccountInviteR\x06invite\"G\n\x1cGetTeamAccountInvitesRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\"W\n\x1dGetTeamAccountInvitesResponse\x12\x36\n\x07invites\x18\x01 \x03(\x0b\x32\x1c.mgmt.v1alpha1.AccountInviteR\x07invites\":\n\x1eRemoveTeamAccountInviteRequest\x12\x18\n\x02id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\x02id\"!\n\x1fRemoveTeamAccountInviteResponse\"?\n\x1e\x41\x63\x63\x65ptTeamAccountInviteRequest\x12\x1d\n\x05token\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x05token\"W\n\x1f\x41\x63\x63\x65ptTeamAccountInviteResponse\x12\x34\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x1a.mgmt.v1alpha1.UserAccountR\x07\x61\x63\x63ount\"\x1d\n\x1bGetSystemInformationRequest\"\xfb\x01\n\x1cGetSystemInformationResponse\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12\x16\n\x06\x63ommit\x18\x02 \x01(\tR\x06\x63ommit\x12\x1a\n\x08\x63ompiler\x18\x03 \x01(\tR\x08\x63ompiler\x12\x1a\n\x08platform\x18\x04 \x01(\tR\x08platform\x12\x39\n\nbuild_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tbuildDate\x12\x36\n\x07license\x18\x06 \x01(\x0b\x32\x1c.mgmt.v1alpha1.SystemLicenseR\x07license\"\x8f\x01\n\rSystemLicense\x12\x19\n\x08is_valid\x18\x01 \x01(\x08R\x07isValid\x12\x39\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt\x12(\n\x10is_neosync_cloud\x18\x03 \x01(\x08R\x0eisNeosyncCloud\"L\n!GetAccountOnboardingConfigRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\"d\n\"GetAccountOnboardingConfigResponse\x12>\n\x06\x63onfig\x18\x01 \x01(\x0b\x32&.mgmt.v1alpha1.AccountOnboardingConfigR\x06\x63onfig\"\x8c\x01\n!SetAccountOnboardingConfigRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12>\n\x06\x63onfig\x18\x02 \x01(\x0b\x32&.mgmt.v1alpha1.AccountOnboardingConfigR\x06\x63onfig\"d\n\"SetAccountOnboardingConfigResponse\x12>\n\x06\x63onfig\x18\x01 \x01(\x0b\x32&.mgmt.v1alpha1.AccountOnboardingConfigR\x06\x63onfig\"k\n\x17\x41\x63\x63ountOnboardingConfig\x12\x38\n\x18has_completed_onboarding\x18\x05 \x01(\x08R\x16hasCompletedOnboardingJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05\"B\n\x17GetAccountStatusRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\"\xe5\x01\n\x18GetAccountStatusResponse\x12*\n\x11used_record_count\x18\x01 \x01(\x04R\x0fusedRecordCount\x12\x35\n\x14\x61llowed_record_count\x18\x02 \x01(\x04H\x00R\x12\x61llowedRecordCount\x88\x01\x01\x12M\n\x13subscription_status\x18\x03 \x01(\x0e\x32\x1c.mgmt.v1alpha1.BillingStatusR\x12subscriptionStatusB\x17\n\x15_allowed_record_count\"\x9c\x01\n\x1bIsAccountStatusValidRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12\x39\n\x16requested_record_count\x18\x02 \x01(\x04H\x00R\x14requestedRecordCount\x88\x01\x01\x42\x19\n\x17_requested_record_count\"\xb3\x02\n\x1cIsAccountStatusValidResponse\x12\x19\n\x08is_valid\x18\x01 \x01(\x08R\x07isValid\x12\x1b\n\x06reason\x18\x02 \x01(\tH\x00R\x06reason\x88\x01\x01\x12\x1f\n\x0bshould_poll\x18\x03 \x01(\x08R\nshouldPoll\x12\x43\n\x0e\x61\x63\x63ount_status\x18\x06 \x01(\x0e\x32\x1c.mgmt.v1alpha1.AccountStatusR\raccountStatus\x12I\n\x10trial_expires_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01R\x0etrialExpiresAt\x88\x01\x01\x42\t\n\x07_reasonB\x13\n\x11_trial_expires_atJ\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\"R\n\'GetAccountBillingCheckoutSessionRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\"\\\n(GetAccountBillingCheckoutSessionResponse\x12\x30\n\x14\x63heckout_session_url\x18\x01 \x01(\tR\x12\x63heckoutSessionUrl\"P\n%GetAccountBillingPortalSessionRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\"V\n&GetAccountBillingPortalSessionResponse\x12,\n\x12portal_session_url\x18\x01 \x01(\tR\x10portalSessionUrl\"<\n\x19GetBillingAccountsRequest\x12\x1f\n\x0b\x61\x63\x63ount_ids\x18\x01 \x03(\tR\naccountIds\"T\n\x1aGetBillingAccountsResponse\x12\x36\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32\x1a.mgmt.v1alpha1.UserAccountR\x08\x61\x63\x63ounts\"\xe2\x01\n\x1bSetBillingMeterEventRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12&\n\nevent_name\x18\x02 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\teventName\x12\x1d\n\x05value\x18\x03 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x05value\x12\"\n\x08\x65vent_id\x18\x04 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x07\x65ventId\x12!\n\ttimestamp\x18\x05 \x01(\x04H\x00R\ttimestamp\x88\x01\x01\x42\x0c\n\n_timestamp\"\x1e\n\x1cSetBillingMeterEventResponse\"\x90\x01\n\x12SetUserRoleRequest\x12\'\n\naccount_id\x18\x01 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\taccountId\x12!\n\x07user_id\x18\x02 \x01(\tB\x08\xbaH\x05r\x03\xb0\x01\x01R\x06userId\x12.\n\x04role\x18\x03 \x01(\x0e\x32\x1a.mgmt.v1alpha1.AccountRoleR\x04role\"\x15\n\x13SetUserRoleResponse*\x92\x01\n\x0fUserAccountType\x12!\n\x1dUSER_ACCOUNT_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aUSER_ACCOUNT_TYPE_PERSONAL\x10\x01\x12\x1a\n\x16USER_ACCOUNT_TYPE_TEAM\x10\x02\x12 \n\x1cUSER_ACCOUNT_TYPE_ENTERPRISE\x10\x03*\xa9\x01\n\rBillingStatus\x12\x1e\n\x1a\x42ILLING_STATUS_UNSPECIFIED\x10\x00\x12\x19\n\x15\x42ILLING_STATUS_ACTIVE\x10\x01\x12\x1a\n\x16\x42ILLING_STATUS_EXPIRED\x10\x02\x12\x1f\n\x1b\x42ILLING_STATUS_TRIAL_ACTIVE\x10\x03\x12 \n\x1c\x42ILLING_STATUS_TRIAL_EXPIRED\x10\x04*\x90\x02\n\rAccountStatus\x12%\n!ACCOUNT_STATUS_REASON_UNSPECIFIED\x10\x00\x12+\n\'ACCOUNT_STATUS_ACCOUNT_IN_EXPIRED_STATE\x10\x03\x12\'\n#ACCOUNT_STATUS_ACCOUNT_TRIAL_ACTIVE\x10\x04\x12(\n$ACCOUNT_STATUS_ACCOUNT_TRIAL_EXPIRED\x10\x05\"\x04\x08\x01\x10\x01\"\x04\x08\x02\x10\x02*$ACCOUNT_STATUS_EXCEEDS_ALLOWED_LIMIT*&ACCOUNT_STATUS_REQUESTED_EXCEEDS_LIMIT*\x9f\x01\n\x0b\x41\x63\x63ountRole\x12\x1c\n\x18\x41\x43\x43OUNT_ROLE_UNSPECIFIED\x10\x00\x12\x16\n\x12\x41\x43\x43OUNT_ROLE_ADMIN\x10\x01\x12\x1e\n\x1a\x41\x43\x43OUNT_ROLE_JOB_DEVELOPER\x10\x02\x12\x1b\n\x17\x41\x43\x43OUNT_ROLE_JOB_VIEWER\x10\x03\x12\x1d\n\x19\x41\x43\x43OUNT_ROLE_JOB_EXECUTOR\x10\x04\x32\xf8\x16\n\x12UserAccountService\x12J\n\x07GetUser\x12\x1d.mgmt.v1alpha1.GetUserRequest\x1a\x1e.mgmt.v1alpha1.GetUserResponse\"\x00\x12J\n\x07SetUser\x12\x1d.mgmt.v1alpha1.SetUserRequest\x1a\x1e.mgmt.v1alpha1.SetUserResponse\"\x00\x12\x62\n\x0fGetUserAccounts\x12%.mgmt.v1alpha1.GetUserAccountsRequest\x1a&.mgmt.v1alpha1.GetUserAccountsResponse\"\x00\x12k\n\x12SetPersonalAccount\x12(.mgmt.v1alpha1.SetPersonalAccountRequest\x1a).mgmt.v1alpha1.SetPersonalAccountResponse\"\x00\x12\x89\x01\n\x1c\x43onvertPersonalToTeamAccount\x12\x32.mgmt.v1alpha1.ConvertPersonalToTeamAccountRequest\x1a\x33.mgmt.v1alpha1.ConvertPersonalToTeamAccountResponse\"\x00\x12h\n\x11\x43reateTeamAccount\x12\'.mgmt.v1alpha1.CreateTeamAccountRequest\x1a(.mgmt.v1alpha1.CreateTeamAccountResponse\"\x00\x12\x62\n\x0fIsUserInAccount\x12%.mgmt.v1alpha1.IsUserInAccountRequest\x1a&.mgmt.v1alpha1.IsUserInAccountResponse\"\x00\x12}\n\x18GetAccountTemporalConfig\x12..mgmt.v1alpha1.GetAccountTemporalConfigRequest\x1a/.mgmt.v1alpha1.GetAccountTemporalConfigResponse\"\x00\x12}\n\x18SetAccountTemporalConfig\x12..mgmt.v1alpha1.SetAccountTemporalConfigRequest\x1a/.mgmt.v1alpha1.SetAccountTemporalConfigResponse\"\x00\x12t\n\x15GetTeamAccountMembers\x12+.mgmt.v1alpha1.GetTeamAccountMembersRequest\x1a,.mgmt.v1alpha1.GetTeamAccountMembersResponse\"\x00\x12z\n\x17RemoveTeamAccountMember\x12-.mgmt.v1alpha1.RemoveTeamAccountMemberRequest\x1a..mgmt.v1alpha1.RemoveTeamAccountMemberResponse\"\x00\x12z\n\x17InviteUserToTeamAccount\x12-.mgmt.v1alpha1.InviteUserToTeamAccountRequest\x1a..mgmt.v1alpha1.InviteUserToTeamAccountResponse\"\x00\x12t\n\x15GetTeamAccountInvites\x12+.mgmt.v1alpha1.GetTeamAccountInvitesRequest\x1a,.mgmt.v1alpha1.GetTeamAccountInvitesResponse\"\x00\x12z\n\x17RemoveTeamAccountInvite\x12-.mgmt.v1alpha1.RemoveTeamAccountInviteRequest\x1a..mgmt.v1alpha1.RemoveTeamAccountInviteResponse\"\x00\x12z\n\x17\x41\x63\x63\x65ptTeamAccountInvite\x12-.mgmt.v1alpha1.AcceptTeamAccountInviteRequest\x1a..mgmt.v1alpha1.AcceptTeamAccountInviteResponse\"\x00\x12t\n\x14GetSystemInformation\x12*.mgmt.v1alpha1.GetSystemInformationRequest\x1a+.mgmt.v1alpha1.GetSystemInformationResponse\"\x03\x90\x02\x01\x12\x83\x01\n\x1aGetAccountOnboardingConfig\x12\x30.mgmt.v1alpha1.GetAccountOnboardingConfigRequest\x1a\x31.mgmt.v1alpha1.GetAccountOnboardingConfigResponse\"\x00\x12\x83\x01\n\x1aSetAccountOnboardingConfig\x12\x30.mgmt.v1alpha1.SetAccountOnboardingConfigRequest\x1a\x31.mgmt.v1alpha1.SetAccountOnboardingConfigResponse\"\x00\x12h\n\x10GetAccountStatus\x12&.mgmt.v1alpha1.GetAccountStatusRequest\x1a\'.mgmt.v1alpha1.GetAccountStatusResponse\"\x03\x90\x02\x01\x12t\n\x14IsAccountStatusValid\x12*.mgmt.v1alpha1.IsAccountStatusValidRequest\x1a+.mgmt.v1alpha1.IsAccountStatusValidResponse\"\x03\x90\x02\x01\x12\x95\x01\n GetAccountBillingCheckoutSession\x12\x36.mgmt.v1alpha1.GetAccountBillingCheckoutSessionRequest\x1a\x37.mgmt.v1alpha1.GetAccountBillingCheckoutSessionResponse\"\x00\x12\x8f\x01\n\x1eGetAccountBillingPortalSession\x12\x34.mgmt.v1alpha1.GetAccountBillingPortalSessionRequest\x1a\x35.mgmt.v1alpha1.GetAccountBillingPortalSessionResponse\"\x00\x12n\n\x12GetBillingAccounts\x12(.mgmt.v1alpha1.GetBillingAccountsRequest\x1a).mgmt.v1alpha1.GetBillingAccountsResponse\"\x03\x90\x02\x01\x12q\n\x14SetBillingMeterEvent\x12*.mgmt.v1alpha1.SetBillingMeterEventRequest\x1a+.mgmt.v1alpha1.SetBillingMeterEventResponse\"\x00\x12V\n\x0bSetUserRole\x12!.mgmt.v1alpha1.SetUserRoleRequest\x1a\".mgmt.v1alpha1.SetUserRoleResponse\"\x00\x42\xcc\x01\n\x11\x63om.mgmt.v1alpha1B\x10UserAccountProtoP\x01ZPgithub.com/nucleuscloud/neosync/backend/gen/go/protos/mgmt/v1alpha1;mgmtv1alpha1\xa2\x02\x03MXX\xaa\x02\rMgmt.V1alpha1\xca\x02\rMgmt\\V1alpha1\xe2\x02\x19Mgmt\\V1alpha1\\GPBMetadata\xea\x02\x0eMgmt::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mgmt.v1alpha1.user_account_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.mgmt.v1alpha1B\020UserAccountProtoP\001ZPgithub.com/nucleuscloud/neosync/backend/gen/go/protos/mgmt/v1alpha1;mgmtv1alpha1\242\002\003MXX\252\002\rMgmt.V1alpha1\312\002\rMgmt\\V1alpha1\342\002\031Mgmt\\V1alpha1\\GPBMetadata\352\002\016Mgmt::V1alpha1'
  _globals['_CONVERTPERSONALTOTEAMACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CONVERTPERSONALTOTEAMACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\272H\026r\0242\022^[a-z0-9-]{3,100}$'
  _globals['_CONVERTPERSONALTOTEAMACCOUNTREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_CONVERTPERSONALTOTEAMACCOUNTREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_ISUSERINACCOUNTREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_ISUSERINACCOUNTREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_GETACCOUNTTEMPORALCONFIGREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETACCOUNTTEMPORALCONFIGREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_SETACCOUNTTEMPORALCONFIGREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_SETACCOUNTTEMPORALCONFIGREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_ACCOUNTTEMPORALCONFIG'].fields_by_name['url']._loaded_options = None
  _globals['_ACCOUNTTEMPORALCONFIG'].fields_by_name['url']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_ACCOUNTTEMPORALCONFIG'].fields_by_name['namespace']._loaded_options = None
  _globals['_ACCOUNTTEMPORALCONFIG'].fields_by_name['namespace']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_ACCOUNTTEMPORALCONFIG'].fields_by_name['sync_job_queue_name']._loaded_options = None
  _globals['_ACCOUNTTEMPORALCONFIG'].fields_by_name['sync_job_queue_name']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_CREATETEAMACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATETEAMACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\272H\026r\0242\022^[a-z0-9-]{3,100}$'
  _globals['_GETTEAMACCOUNTMEMBERSREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETTEAMACCOUNTMEMBERSREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_REMOVETEAMACCOUNTMEMBERREQUEST'].fields_by_name['user_id']._loaded_options = None
  _globals['_REMOVETEAMACCOUNTMEMBERREQUEST'].fields_by_name['user_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_REMOVETEAMACCOUNTMEMBERREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_REMOVETEAMACCOUNTMEMBERREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_INVITEUSERTOTEAMACCOUNTREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_INVITEUSERTOTEAMACCOUNTREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_INVITEUSERTOTEAMACCOUNTREQUEST'].fields_by_name['email']._loaded_options = None
  _globals['_INVITEUSERTOTEAMACCOUNTREQUEST'].fields_by_name['email']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_GETTEAMACCOUNTINVITESREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETTEAMACCOUNTINVITESREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_REMOVETEAMACCOUNTINVITEREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_REMOVETEAMACCOUNTINVITEREQUEST'].fields_by_name['id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_ACCEPTTEAMACCOUNTINVITEREQUEST'].fields_by_name['token']._loaded_options = None
  _globals['_ACCEPTTEAMACCOUNTINVITEREQUEST'].fields_by_name['token']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_GETACCOUNTONBOARDINGCONFIGREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETACCOUNTONBOARDINGCONFIGREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_SETACCOUNTONBOARDINGCONFIGREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_SETACCOUNTONBOARDINGCONFIGREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_GETACCOUNTSTATUSREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETACCOUNTSTATUSREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_ISACCOUNTSTATUSVALIDREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_ISACCOUNTSTATUSVALIDREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_GETACCOUNTBILLINGCHECKOUTSESSIONREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETACCOUNTBILLINGCHECKOUTSESSIONREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_GETACCOUNTBILLINGPORTALSESSIONREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETACCOUNTBILLINGPORTALSESSIONREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_SETBILLINGMETEREVENTREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_SETBILLINGMETEREVENTREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_SETBILLINGMETEREVENTREQUEST'].fields_by_name['event_name']._loaded_options = None
  _globals['_SETBILLINGMETEREVENTREQUEST'].fields_by_name['event_name']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_SETBILLINGMETEREVENTREQUEST'].fields_by_name['value']._loaded_options = None
  _globals['_SETBILLINGMETEREVENTREQUEST'].fields_by_name['value']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_SETBILLINGMETEREVENTREQUEST'].fields_by_name['event_id']._loaded_options = None
  _globals['_SETBILLINGMETEREVENTREQUEST'].fields_by_name['event_id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_SETUSERROLEREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_SETUSERROLEREQUEST'].fields_by_name['account_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_SETUSERROLEREQUEST'].fields_by_name['user_id']._loaded_options = None
  _globals['_SETUSERROLEREQUEST'].fields_by_name['user_id']._serialized_options = b'\272H\005r\003\260\001\001'
  _globals['_USERACCOUNTSERVICE'].methods_by_name['GetSystemInformation']._loaded_options = None
  _globals['_USERACCOUNTSERVICE'].methods_by_name['GetSystemInformation']._serialized_options = b'\220\002\001'
  _globals['_USERACCOUNTSERVICE'].methods_by_name['GetAccountStatus']._loaded_options = None
  _globals['_USERACCOUNTSERVICE'].methods_by_name['GetAccountStatus']._serialized_options = b'\220\002\001'
  _globals['_USERACCOUNTSERVICE'].methods_by_name['IsAccountStatusValid']._loaded_options = None
  _globals['_USERACCOUNTSERVICE'].methods_by_name['IsAccountStatusValid']._serialized_options = b'\220\002\001'
  _globals['_USERACCOUNTSERVICE'].methods_by_name['GetBillingAccounts']._loaded_options = None
  _globals['_USERACCOUNTSERVICE'].methods_by_name['GetBillingAccounts']._serialized_options = b'\220\002\001'
  _globals['_USERACCOUNTTYPE']._serialized_start=6009
  _globals['_USERACCOUNTTYPE']._serialized_end=6155
  _globals['_BILLINGSTATUS']._serialized_start=6158
  _globals['_BILLINGSTATUS']._serialized_end=6327
  _globals['_ACCOUNTSTATUS']._serialized_start=6330
  _globals['_ACCOUNTSTATUS']._serialized_end=6602
  _globals['_ACCOUNTROLE']._serialized_start=6605
  _globals['_ACCOUNTROLE']._serialized_end=6764
  _globals['_GETUSERREQUEST']._serialized_start=113
  _globals['_GETUSERREQUEST']._serialized_end=129
  _globals['_GETUSERRESPONSE']._serialized_start=131
  _globals['_GETUSERRESPONSE']._serialized_end=173
  _globals['_SETUSERREQUEST']._serialized_start=175
  _globals['_SETUSERREQUEST']._serialized_end=191
  _globals['_SETUSERRESPONSE']._serialized_start=193
  _globals['_SETUSERRESPONSE']._serialized_end=235
  _globals['_GETUSERACCOUNTSREQUEST']._serialized_start=237
  _globals['_GETUSERACCOUNTSREQUEST']._serialized_end=261
  _globals['_GETUSERACCOUNTSRESPONSE']._serialized_start=263
  _globals['_GETUSERACCOUNTSRESPONSE']._serialized_end=344
  _globals['_USERACCOUNT']._serialized_start=347
  _globals['_USERACCOUNT']._serialized_end=501
  _globals['_CONVERTPERSONALTOTEAMACCOUNTREQUEST']._serialized_start=504
  _globals['_CONVERTPERSONALTOTEAMACCOUNTREQUEST']._serialized_end=649
  _globals['_CONVERTPERSONALTOTEAMACCOUNTRESPONSE']._serialized_start=652
  _globals['_CONVERTPERSONALTOTEAMACCOUNTRESPONSE']._serialized_end=856
  _globals['_SETPERSONALACCOUNTREQUEST']._serialized_start=858
  _globals['_SETPERSONALACCOUNTREQUEST']._serialized_end=885
  _globals['_SETPERSONALACCOUNTRESPONSE']._serialized_start=887
  _globals['_SETPERSONALACCOUNTRESPONSE']._serialized_end=946
  _globals['_ISUSERINACCOUNTREQUEST']._serialized_start=948
  _globals['_ISUSERINACCOUNTREQUEST']._serialized_end=1013
  _globals['_ISUSERINACCOUNTRESPONSE']._serialized_start=1015
  _globals['_ISUSERINACCOUNTRESPONSE']._serialized_end=1056
  _globals['_GETACCOUNTTEMPORALCONFIGREQUEST']._serialized_start=1058
  _globals['_GETACCOUNTTEMPORALCONFIGREQUEST']._serialized_end=1132
  _globals['_GETACCOUNTTEMPORALCONFIGRESPONSE']._serialized_start=1134
  _globals['_GETACCOUNTTEMPORALCONFIGRESPONSE']._serialized_end=1230
  _globals['_SETACCOUNTTEMPORALCONFIGREQUEST']._serialized_start=1233
  _globals['_SETACCOUNTTEMPORALCONFIGREQUEST']._serialized_end=1369
  _globals['_SETACCOUNTTEMPORALCONFIGRESPONSE']._serialized_start=1371
  _globals['_SETACCOUNTTEMPORALCONFIGRESPONSE']._serialized_end=1467
  _globals['_ACCOUNTTEMPORALCONFIG']._serialized_start=1470
  _globals['_ACCOUNTTEMPORALCONFIG']._serialized_end=1615
  _globals['_CREATETEAMACCOUNTREQUEST']._serialized_start=1617
  _globals['_CREATETEAMACCOUNTREQUEST']._serialized_end=1690
  _globals['_CREATETEAMACCOUNTRESPONSE']._serialized_start=1693
  _globals['_CREATETEAMACCOUNTRESPONSE']._serialized_end=1831
  _globals['_ACCOUNTUSER']._serialized_start=1834
  _globals['_ACCOUNTUSER']._serialized_end=1975
  _globals['_GETTEAMACCOUNTMEMBERSREQUEST']._serialized_start=1977
  _globals['_GETTEAMACCOUNTMEMBERSREQUEST']._serialized_end=2048
  _globals['_GETTEAMACCOUNTMEMBERSRESPONSE']._serialized_start=2050
  _globals['_GETTEAMACCOUNTMEMBERSRESPONSE']._serialized_end=2131
  _globals['_REMOVETEAMACCOUNTMEMBERREQUEST']._serialized_start=2133
  _globals['_REMOVETEAMACCOUNTMEMBERREQUEST']._serialized_end=2241
  _globals['_REMOVETEAMACCOUNTMEMBERRESPONSE']._serialized_start=2243
  _globals['_REMOVETEAMACCOUNTMEMBERRESPONSE']._serialized_end=2276
  _globals['_INVITEUSERTOTEAMACCOUNTREQUEST']._serialized_start=2279
  _globals['_INVITEUSERTOTEAMACCOUNTREQUEST']._serialized_end=2445
  _globals['_ACCOUNTINVITE']._serialized_start=2448
  _globals['_ACCOUNTINVITE']._serialized_end=2845
  _globals['_INVITEUSERTOTEAMACCOUNTRESPONSE']._serialized_start=2847
  _globals['_INVITEUSERTOTEAMACCOUNTRESPONSE']._serialized_end=2934
  _globals['_GETTEAMACCOUNTINVITESREQUEST']._serialized_start=2936
  _globals['_GETTEAMACCOUNTINVITESREQUEST']._serialized_end=3007
  _globals['_GETTEAMACCOUNTINVITESRESPONSE']._serialized_start=3009
  _globals['_GETTEAMACCOUNTINVITESRESPONSE']._serialized_end=3096
  _globals['_REMOVETEAMACCOUNTINVITEREQUEST']._serialized_start=3098
  _globals['_REMOVETEAMACCOUNTINVITEREQUEST']._serialized_end=3156
  _globals['_REMOVETEAMACCOUNTINVITERESPONSE']._serialized_start=3158
  _globals['_REMOVETEAMACCOUNTINVITERESPONSE']._serialized_end=3191
  _globals['_ACCEPTTEAMACCOUNTINVITEREQUEST']._serialized_start=3193
  _globals['_ACCEPTTEAMACCOUNTINVITEREQUEST']._serialized_end=3256
  _globals['_ACCEPTTEAMACCOUNTINVITERESPONSE']._serialized_start=3258
  _globals['_ACCEPTTEAMACCOUNTINVITERESPONSE']._serialized_end=3345
  _globals['_GETSYSTEMINFORMATIONREQUEST']._serialized_start=3347
  _globals['_GETSYSTEMINFORMATIONREQUEST']._serialized_end=3376
  _globals['_GETSYSTEMINFORMATIONRESPONSE']._serialized_start=3379
  _globals['_GETSYSTEMINFORMATIONRESPONSE']._serialized_end=3630
  _globals['_SYSTEMLICENSE']._serialized_start=3633
  _globals['_SYSTEMLICENSE']._serialized_end=3776
  _globals['_GETACCOUNTONBOARDINGCONFIGREQUEST']._serialized_start=3778
  _globals['_GETACCOUNTONBOARDINGCONFIGREQUEST']._serialized_end=3854
  _globals['_GETACCOUNTONBOARDINGCONFIGRESPONSE']._serialized_start=3856
  _globals['_GETACCOUNTONBOARDINGCONFIGRESPONSE']._serialized_end=3956
  _globals['_SETACCOUNTONBOARDINGCONFIGREQUEST']._serialized_start=3959
  _globals['_SETACCOUNTONBOARDINGCONFIGREQUEST']._serialized_end=4099
  _globals['_SETACCOUNTONBOARDINGCONFIGRESPONSE']._serialized_start=4101
  _globals['_SETACCOUNTONBOARDINGCONFIGRESPONSE']._serialized_end=4201
  _globals['_ACCOUNTONBOARDINGCONFIG']._serialized_start=4203
  _globals['_ACCOUNTONBOARDINGCONFIG']._serialized_end=4310
  _globals['_GETACCOUNTSTATUSREQUEST']._serialized_start=4312
  _globals['_GETACCOUNTSTATUSREQUEST']._serialized_end=4378
  _globals['_GETACCOUNTSTATUSRESPONSE']._serialized_start=4381
  _globals['_GETACCOUNTSTATUSRESPONSE']._serialized_end=4610
  _globals['_ISACCOUNTSTATUSVALIDREQUEST']._serialized_start=4613
  _globals['_ISACCOUNTSTATUSVALIDREQUEST']._serialized_end=4769
  _globals['_ISACCOUNTSTATUSVALIDRESPONSE']._serialized_start=4772
  _globals['_ISACCOUNTSTATUSVALIDRESPONSE']._serialized_end=5079
  _globals['_GETACCOUNTBILLINGCHECKOUTSESSIONREQUEST']._serialized_start=5081
  _globals['_GETACCOUNTBILLINGCHECKOUTSESSIONREQUEST']._serialized_end=5163
  _globals['_GETACCOUNTBILLINGCHECKOUTSESSIONRESPONSE']._serialized_start=5165
  _globals['_GETACCOUNTBILLINGCHECKOUTSESSIONRESPONSE']._serialized_end=5257
  _globals['_GETACCOUNTBILLINGPORTALSESSIONREQUEST']._serialized_start=5259
  _globals['_GETACCOUNTBILLINGPORTALSESSIONREQUEST']._serialized_end=5339
  _globals['_GETACCOUNTBILLINGPORTALSESSIONRESPONSE']._serialized_start=5341
  _globals['_GETACCOUNTBILLINGPORTALSESSIONRESPONSE']._serialized_end=5427
  _globals['_GETBILLINGACCOUNTSREQUEST']._serialized_start=5429
  _globals['_GETBILLINGACCOUNTSREQUEST']._serialized_end=5489
  _globals['_GETBILLINGACCOUNTSRESPONSE']._serialized_start=5491
  _globals['_GETBILLINGACCOUNTSRESPONSE']._serialized_end=5575
  _globals['_SETBILLINGMETEREVENTREQUEST']._serialized_start=5578
  _globals['_SETBILLINGMETEREVENTREQUEST']._serialized_end=5804
  _globals['_SETBILLINGMETEREVENTRESPONSE']._serialized_start=5806
  _globals['_SETBILLINGMETEREVENTRESPONSE']._serialized_end=5836
  _globals['_SETUSERROLEREQUEST']._serialized_start=5839
  _globals['_SETUSERROLEREQUEST']._serialized_end=5983
  _globals['_SETUSERROLERESPONSE']._serialized_start=5985
  _globals['_SETUSERROLERESPONSE']._serialized_end=6006
  _globals['_USERACCOUNTSERVICE']._serialized_start=6767
  _globals['_USERACCOUNTSERVICE']._serialized_end=9703
# @@protoc_insertion_point(module_scope)
