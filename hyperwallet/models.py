#!/usr/bin/env python

import json
from enum import Enum


class HyperwalletModel(object):
    '''
    The base Hyperwallet Model from which all other models will inherit.

    :param data:
        A dictionary containing the attributes for the Model.
    '''

    def __init__(self, data):
        '''
        Create an instance of the base HyperwalletModel.
        '''

        self.defaults = {
            '_raw_json': None
        }

        setattr(self, '_raw_json', data)

    def __str__(self):
        '''
        Return a string representation of the HyperwalletModel. By default this
        is the same as asJsonString().
        '''

        return self.asJsonString()

    def asJsonString(self):
        '''
        Return a JSON string of the HyperwalletModel based on key/value pairs
        returned from the asDict() function.
        '''

        return json.dumps(
            self.asDict(),
            sort_keys=True,
            separators=(',', ':'),
            indent=4
        )

    def asDict(self):
        '''
        Return a dictionary representation of the Model.
        '''

        data = {}

        for (key, value) in self._raw_json.items():
            if isinstance(self._raw_json.get(key, None), (list, tuple, set)):
                data[key] = list()
                for subobj in self._raw_json.get(key, None):
                    data[key].append(subobj)

            elif self._raw_json.get(key, None):
                data[key] = self._raw_json.get(key, None)

        return data


class User(HyperwalletModel):
    '''
    The User Model.

    :param data:
        A dictionary containing the attributes for the User.
    '''

    filters_array = {'clientUserId', 'email', 'programToken', 'status', 'verificationStatus', 'taxVerificationStatus', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new User with the provided attributes.
        '''

        super(User, self).__init__(data)

        self.defaults = {
            'addressLine1': None,
            'addressLine2': None,
            'businessContactRole': None,
            'businessName': None,
            'businessOperatingName': None,
            'businessRegistrationCountry': None,
            'businessRegistrationId': None,
            'businessRegistrationStateProvince': None,
            'businessType': None,
            'city': None,
            'clientUserId': None,
            'country': None,
            'countryOfBirth': None,
            'countryOfNationality': None,
            'createdOn': None,
            'dateOfBirth': None,
            'driversLicenseId': None,
            'email': None,
            'employerId': None,
            'firstName': None,
            'gender': None,
            'governmentId': None,
            'governmentIdType': None,
            'language': None,
            'lastName': None,
            'middleName': None,
            'mobileNumber': None,
            'passportId': None,
            'phoneNumber': None,
            'postalCode': None,
            'profileType': None,
            'programToken': None,
            'stateProvince': None,
            'status': None,
            'token': None,
            'verificationStatus': None,
            'taxVerificationStatus': None,
            'timeZone': None,
            'documents': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "User({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class HyperwalletVerificationDocument(HyperwalletModel):
    '''
    The HyperwalletVerificationDocument Model.

    :param data:
        A dictionary containing the attributes for the HyperwalletVerificationDocument.
    '''

    def __init__(self, data):
        '''
        Create a new HyperwalletVerificationDocument with the provided attributes.
        '''

        super(HyperwalletVerificationDocument, self).__init__(data)

        self.defaults = {
            'category': None,
            'type': None,
            'status': None,
            'country': None,
            'reasons': None,
            'createdOn': None,
            'uploadFiles': None,
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "HyperwalletVerificationDocument({category}, {createdOn})".format(
            createdOn=self.createdOn, category=self.category
        )


class HyperwalletVerificationDocumentReason(HyperwalletModel):
    '''
    The HyperwalletVerificationDocumentReason Model.

    :param data:
        A dictionary containing the attributes for the HyperwalletVerificationDocumentReason.
    '''

    def __init__(self, data):
        '''
        Create a new HyperwalletVerificationDocumentReason with the provided attributes.
        '''

        super(HyperwalletVerificationDocumentReason, self).__init__(data)

        self.defaults = {
            'name': None,
            'description': None,
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "HyperwalletVerificationDocumentReason({name}, {description})".format(
            name=self.name, description=self.description
        )


class RejectReason(Enum):
    DOCUMENT_EXPIRED = 0
    DOCUMENT_NOT_RELATED_TO_PROFILE = 1
    DOCUMENT_NOT_READABLE = 2
    DOCUMENT_NOT_DECISIVE = 3
    DOCUMENT_NOT_COMPLETE = 4
    DOCUMENT_CORRECTION_REQUIRED = 5
    DOCUMENT_NOT_VALID_WITH_NOTES = 6
    DOCUMENT_TYPE_NOT_VALID = 7


class AuthenticationToken(HyperwalletModel):
    '''
    The AuthenticationToken Model.

    :param data:
        A dictionary containing the attributes for the Authentication Token.
    '''

    def __init__(self, data):
        '''
        Create a new Authentication Token with the provided attributes.
        '''

        super(AuthenticationToken, self).__init__(data)

        self.defaults = {
            'value': None,
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "AuthenticationToken({value})".format(
            value=self.value
        )


class TransferMethod(HyperwalletModel):
    '''
    The TransferMethod Model.

    :param data:
        A dictionary containing the attributes for the Transfer Method.
    '''

    filters_array = {'status', 'type', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new Transfer Method with the provided attributes.
        '''

        super(TransferMethod, self).__init__(data)

        self.defaults = {
            'createdOn': None,
            'isDefaultTransferMethod': None,
            'status': None,
            'token': None,
            'transferMethodCountry': None,
            'transferMethodCurrency': None,
            'type': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "TransferMethod({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class BankAccount(TransferMethod):
    '''
    The BankAccount Model.

    :param data:
        A dictionary containing the attributes for the Bank Account.
    '''

    filters_array = {'type', 'status', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new Bank Account with the provided attributes.
        '''

        super(BankAccount, self).__init__(data)

        self.defaults = {
            'addressLine1': None,
            'addressLine2': None,
            'bankAccountId': None,
            'bankAccountPurpose': None,
            'bankId': None,
            'bankName': None,
            'branchAddressLine1': None,
            'branchAddressLine2': None,
            'branchCity': None,
            'branchCountry': None,
            'branchId': None,
            'branchName': None,
            'branchPostalCode': None,
            'branchStateProvince': None,
            'buildingSocietyAccount': None,
            'businessContactRole': None,
            'businessName': None,
            'businessOperatingName': None,
            'businessRegistrationCountry': None,
            'businessRegistrationId': None,
            'businessRegistrationStateProvince': None,
            'businessType': None,
            'city': None,
            'country': None,
            'countryOfBirth': None,
            'countryOfNationality': None,
            'dateOfBirth': None,
            'driversLicenseId': None,
            'employerId': None,
            'firstName': None,
            'gender': None,
            'governmentId': None,
            'governmentIdType': None,
            'intermediaryBankAccountId': None,
            'intermediaryBankAddressLine1': None,
            'intermediaryBankAddressLine2': None,
            'intermediaryBankCity': None,
            'intermediaryBankCountry': None,
            'intermediaryBankId': None,
            'intermediaryBankName': None,
            'intermediaryBankPostalCode': None,
            'intermediaryBankStateProvince': None,
            'kpp': None,
            'lastName': None,
            'middleName': None,
            'mobileNumber': None,
            'passportId': None,
            'phoneNumber': None,
            'postalCode': None,
            'profileType': None,
            'stateProvince': None,
            'taxId': None,
            'wireInstructions': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "BankAccount({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class BankCard(TransferMethod):
    '''
    The BankCard Model.

    :param data:
        A dictionary containing the attributes for the Bank Card.
    '''

    filters_array = {'status', 'type', 'createdOn', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new Bank Card with the provided attributes.
        '''

        super(BankCard, self).__init__(data)

        self.defaults = {
            'cardBrand': None,
            'cardNumber': None,
            'cardType': None,
            'cvv': None,
            'processingTime': None,
            'dateOfExpiry': None,
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "BankCard({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class PrepaidCard(TransferMethod):
    '''
    The PrepaidCard Model.

    :param data:
        A dictionary containing the attributes for the Prepaid Card.
    '''

    filters_array = {'status', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new Prepaid Card with the provided attributes.
        '''

        super(PrepaidCard, self).__init__(data)

        self.defaults = {
            'cardBrand': None,
            'cardNumber': None,
            'cardPackage': None,
            'cardType': None,
            'dateOfExpiry': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "PrepaidCard({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class PaperCheck(TransferMethod):
    '''
    The PaperCheck Model.

    :param data:
        A dictionary containing the attributes for the Paper Check.
    '''

    filters_array = {'status', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new Paper Check with the provided attributes.
        '''

        super(PaperCheck, self).__init__(data)

        self.defaults = {
            'addressLine1': None,
            'addressLine2': None,
            'businessContactRole': None,
            'businessName': None,
            'businessOperatingName': None,
            'businessRegistrationCountry': None,
            'businessRegistrationId': None,
            'businessRegistrationStateProvince': None,
            'businessType': None,
            'city': None,
            'country': None,
            'countryOfBirth': None,
            'countryOfNationality': None,
            'dateOfBirth': None,
            'driversLicenseId': None,
            'employerId': None,
            'firstName': None,
            'gender': None,
            'governmentId': None,
            'governmentIdType': None,
            'lastName': None,
            'middleName': None,
            'mobileNumber': None,
            'passportId': None,
            'phoneNumber': None,
            'postalCode': None,
            'profileType': None,
            'shippingMethod': None,
            'stateProvince': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "PaperCheck({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class Transfer(HyperwalletModel):
    '''
    The Transfer Model.

    :param data:
        A dictionary containing the attributes for the Transfer.
    '''

    filters_array = {'clientTransferId', 'sourceToken', 'destinationToken', 'createdBefore', 'createdAfter', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new Transfer with the provided attributes.
        '''

        super(Transfer, self).__init__(data)

        self.defaults = {
            'token': None,
            'status': None,
            'createdOn': None,
            'clientTransferId': None,
            'sourceToken': None,
            'sourceAmount': None,
            'sourceFeeAmount': None,
            'sourceCurrency': None,
            'destinationToken': None,
            'destinationAmount': None,
            'destinationFeeAmount': None,
            'destinationCurrency': None,
            'foreignExchanges': None,
            'notes': None,
            'memo': None,
            'expiresOn': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "Transfer({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class PayPalAccount(TransferMethod):
    '''
    The PayPalAccount Model.

    :param data:
        A dictionary containing the attributes for the PayPal Account.
    '''

    filters_array = {'status', 'type', 'createdOn', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new PayPal Account with the provided attributes.
        '''

        super(PayPalAccount, self).__init__(data)

        self.defaults = {
            'email': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "PayPalAccount({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class VenmoAccount(TransferMethod):
    '''
    The VenmoAccount Model.

    :param data:
        A dictionary containing the attributes for the Venmo Account.
    '''

    filters_array = {'status', 'type', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new Venmo Account with the provided attributes.
        '''

        super(VenmoAccount, self).__init__(data)

        self.defaults = {
            'accountId': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "VenmoAccount({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class Payment(HyperwalletModel):
    '''
    The Payment Model.

    :param data:
        A dictionary containing the attributes for the Payment.
    '''

    filters_array = {'clientPaymentId', 'currency', 'memo', 'releaseDate', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new Payment with the provided attributes.
        '''

        super(Payment, self).__init__(data)

        self.defaults = {
            'amount': None,
            'clientPaymentId': None,
            'createdOn': None,
            'currency': None,
            'destinationToken': None,
            'expiresOn': None,
            'memo': None,
            'notes': None,
            'programToken': None,
            'purpose': None,
            'releaseOn': None,
            'expiresOn': None,
            'status': None,
            'token': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "Payment({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class Balance(HyperwalletModel):
    '''
    The Balance Model.

    :param data:
        A dictionary containing the attributes for the Balance.
    '''

    filters_array_user = {'currency', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}
    filters_array_account = {'currency', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}
    filters_array_prepaid_card = {'createdBefore', 'createdAfter'}

    def __init__(self, data):
        '''
        Create a new Balance with the provided attributes.
        '''

        super(Balance, self).__init__(data)

        self.defaults = {
            'amount': None,
            'currency': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "Balance({currency}, {amount})".format(
            currency=self.currency,
            amount=self.amount
        )


class Receipt(HyperwalletModel):
    '''
    The Receipt Model.

    :param data:
        A dictionary containing the attributes for the Receipt.
    '''

    filters_array_user = {'currency', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}
    filters_array_account = {'currency', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}
    filters_array_prepaid_card = {'createdBefore', 'createdAfter'}

    def __init__(self, data):
        '''
        Create a new Receipt with the provided attributes.
        '''

        super(Receipt, self).__init__(data)

        self.defaults = {
            'amount': None,
            'createdOn': None,
            'currency': None,
            'destinationToken': None,
            'details': None,
            'entry': None,
            'fee': None,
            'foreignExchangeCurrency': None,
            'foreignExchangeRate': None,
            'journalId': None,
            'sourceToken': None,
            'type': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "Receipt({entry}, {amount})".format(
            entry=self.entry,
            amount=self.amount
        )


class Program(HyperwalletModel):
    '''
    The Program Model.

    :param data:
        A dictionary containing the attributes for the Program.
    '''

    def __init__(self, data):
        '''
        Create a new Program with the provided attributes.
        '''

        super(Program, self).__init__(data)

        self.defaults = {
            'createdOn': None,
            'name': None,
            'parentToken': None,
            'token': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "Program({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class Account(HyperwalletModel):
    '''
    The Account Model.

    :param data:
        A dictionary containing the attributes for the Account.
    '''

    def __init__(self, data):
        '''
        Create a new Account with the provided attributes.
        '''

        super(Account, self).__init__(data)

        self.defaults = {
            'createdOn': None,
            'email': None,
            'token': None,
            'type': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "Account({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class StatusTransition(HyperwalletModel):
    '''
    The StatusTransition Model.

    :param data:
        A dictionary containing the attributes for the Status Transition.
    '''

    filters_array = {'transition', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new Status Transition with the provided attributes.
        '''

        super(StatusTransition, self).__init__(data)

        self.defaults = {
            'createdOn': None,
            'fromStatus': None,
            'notes': None,
            'statusCode': None,
            'token': None,
            'toStatus': None,
            'transition': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "StatusTransition({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


class TransferMethodConfiguration(HyperwalletModel):
    '''
    The TransferMethodConfiguration Model.

    :param data:
        A dictionary containing the attributes for the Transfer Method Configuration.
    '''

    filters_array = {'userToken', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new Transfer Method Configuration with the provided attributes.
        '''

        super(TransferMethodConfiguration, self).__init__(data)

        self.defaults = {
            'country': None,
            'currency': None,
            'fields': None,
            'profileType': None,
            'type': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

        # Rename the countries array to a single country
        countries = data.get('countries', ['NONE'])
        setattr(self, 'country', countries[0])

        # Rename the currencies array to a single currency
        currencies = data.get('currencies', ['NONE'])
        setattr(self, 'currency', currencies[0])

    def __repr__(self):
        return "TransferMethodConfiguration({country}, {type})".format(
            country=self.country,
            type=self.type
        )


class Webhook(HyperwalletModel):
    '''
    The Webhook Model.

    :param data:
        A dictionary containing the attributes for the Webhook.
    '''

    filters_array = {'programToken', 'type', 'createdBefore', 'createdAfter', 'sortBy', 'offset', 'limit'}

    def __init__(self, data):
        '''
        Create a new Webhook with the provided attributes.
        '''

        super(Webhook, self).__init__(data)

        self.defaults = {
            'createdOn': None,
            'object': None,
            'token': None,
            'type': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

        if self.type is None:
            return

        if type(self.object) is not dict:
            return

        types = {
            'PAYMENTS': Payment,
            'BANK_ACCOUNTS': BankAccount,
            'PREPAID_CARDS': PrepaidCard,
            'USERS': User,
            "BANK_CARDS": BankCard,
            "PAYPAL_ACCOUNTS": PayPalAccount,
            "PAPER_CHECKS": PaperCheck,
            "VENMO_ACCOUNTS": VenmoAccount,
            "TRANSFERS": Transfer,
            "REFUND": TransferRefunds
        }

        base, sub = self.type.split('.')[:2]

        if sub in types:
            self.object = types[sub](self.object)
        elif base in types:
            self.object = types[base](self.object)

    def __repr__(self):
        return "Webhook({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )


'''

   Transfer Refunds

'''


class TransferRefunds(HyperwalletModel):
    '''
    The TransferRefunds Model.

    :param data:
        A dictionary containing the attributes for the Transfer Refunds.
    '''

    def __init__(self, data):
        '''
        Create a new Transfer Refunds with the provided attributes.
        '''

        super(TransferRefunds, self).__init__(data)

        self.defaults = {
            'token': None,
            'status': None,
            'createdOn': None,
            'clientRefundId': None,
            'sourceToken': None,
            'sourceAmount': None,
            'sourceFeeAmount': None,
            'sourceCurrency': None,
            'destinationToken': None,
            'destinationAmount': None,
            'destinationFeeAmount': None,
            'destinationCurrency': None,
            'foreignExchanges': None,
            'notes': None,
            'memo': None,
            'expiresOn': None
        }

        for (param, default) in self.defaults.items():
            setattr(self, param, data.get(param, default))

    def __repr__(self):
        return "TransferRefunds({date}, {token})".format(
            date=self.createdOn,
            token=self.token
        )
