from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.enums import (
    AddressType2Code,
    ClearingChannel2Code,
    CreditDebitCode,
    DocumentType3Code,
    DocumentType6Code,
    Frequency6Code,
    MandateClassification1Code,
    NamePrefix2Code,
    PaymentMethod4Code,
    PreferredContactMethod1Code,
    Priority2Code,
    SequenceType3Code,
    SettlementMethod1Code,
    TaxRecordPeriod1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12"


@dataclass
class AccountSchemeName1ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveOrHistoricCurrencyAndAmountPacs00200112:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class CashAccountType2ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CategoryPurpose1ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification3ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 3,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTime2ChoicePacs00200112:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class DateAndPlaceOfBirth1Pacs00200112:
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DatePeriod2Pacs00200112:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )


@dataclass
class DiscountAmountType1ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineType1ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GarnishmentType1ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Pacs00200112:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LocalInstrument2ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MandateSetupReason1ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class NumberOfTransactionsPerStatus5Pacs00200112:
    dtld_nb_of_txs: Optional[str] = field(
        default=None,
        metadata={
            "name": "DtldNbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    dtld_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "DtldSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    dtld_ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DtldCtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessQuery1Pacs00200112:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class OriginalGroupInformation29Pacs00200112:
    orgnl_msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OrgnlCreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class OtherContact1Pacs00200112:
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountType1ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Purpose2ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ServiceLevel8ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class StatusReason6ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Pacs00200112:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TaxAmountType1ChoicePacs00200112:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TaxAuthorisation1Pacs00200112:
    titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Titl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TaxParty1Pacs00200112:
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AddressType3ChoicePacs00200112:
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    prtry: Optional[GenericIdentification30Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Pacs00200112:
    clr_sys_id: Optional[ClearingSystemIdentification2ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact4Pacs00200112:
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod1Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class CreditorReferenceType1ChoicePacs00200112:
    cd: Optional[DocumentType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DiscountAmountAndType1Pacs00200112:
    tp: Optional[DiscountAmountType1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )


@dataclass
class DocumentAdjustment1Pacs00200112:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DocumentLineType1Pacs00200112:
    cd_or_prtry: Optional[DocumentLineType1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class EquivalentAmount2Pacs00200112:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    ccy_of_trf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOfTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class FrequencyAndMoment1Pacs00200112:
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    pt_in_tm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "pattern": r"[0-9]{2}",
        },
    )


@dataclass
class FrequencyPeriod1Pacs00200112:
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    cnt_per_prd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CntPerPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class GarnishmentType1Pacs00200112:
    cd_or_prtry: Optional[GarnishmentType1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericAccountIdentification1Pacs00200112:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Pacs00200112:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification1Pacs00200112:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification1Pacs00200112:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MandateClassification1ChoicePacs00200112:
    cd: Optional[MandateClassification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentTypeInformation27Pacs00200112:
    instr_prty: Optional[Priority2Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    clr_chanl: Optional[ClearingChannel2Code] = field(
        default=None,
        metadata={
            "name": "ClrChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    svc_lvl: list[ServiceLevel8ChoicePacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    lcl_instrm: Optional[LocalInstrument2ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    seq_tp: Optional[SequenceType3Code] = field(
        default=None,
        metadata={
            "name": "SeqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    ctgy_purp: Optional[CategoryPurpose1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class ProxyAccountIdentification1Pacs00200112:
    tp: Optional[ProxyAccountType1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class ReferredDocumentType3ChoicePacs00200112:
    cd: Optional[DocumentType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Pacs00200112:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )


@dataclass
class TaxAmountAndType1Pacs00200112:
    tp: Optional[TaxAmountType1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )


@dataclass
class TaxParty2Pacs00200112:
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    authstn: Optional[TaxAuthorisation1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Authstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class TaxPeriod3Pacs00200112:
    yr: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Yr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    tp: Optional[TaxRecordPeriod1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    fr_to_dt: Optional[DatePeriod2Pacs00200112] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class AccountIdentification4ChoicePacs00200112:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class AmountType4ChoicePacs00200112:
    instd_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "InstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    eqvt_amt: Optional[EquivalentAmount2Pacs00200112] = field(
        default=None,
        metadata={
            "name": "EqvtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class CreditorReferenceType2Pacs00200112:
    cd_or_prtry: Optional[CreditorReferenceType1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineIdentification1Pacs00200112:
    tp: Optional[DocumentLineType1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class Frequency36ChoicePacs00200112:
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    prd: Optional[FrequencyPeriod1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    pt_in_tm: Optional[FrequencyAndMoment1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "PtInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class MandateTypeInformation2Pacs00200112:
    svc_lvl: Optional[ServiceLevel8ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    lcl_instrm: Optional[LocalInstrument2ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    ctgy_purp: Optional[CategoryPurpose1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    clssfctn: Optional[MandateClassification1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class OrganisationIdentification29Pacs00200112:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class PersonIdentification13Pacs00200112:
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    othr: list[GenericPersonIdentification1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class PostalAddress24Pacs00200112:
    adr_tp: Optional[AddressType3ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ReferredDocumentType4Pacs00200112:
    cd_or_prtry: Optional[ReferredDocumentType3ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RemittanceAmount2Pacs00200112:
    due_pybl_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "DuePyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dscnt_apld_amt: list[DiscountAmountAndType1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "DscntApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    cdt_note_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "CdtNoteAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    tax_amt: list[TaxAmountAndType1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    adjstmnt_amt_and_rsn: list[DocumentAdjustment1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class RemittanceAmount3Pacs00200112:
    due_pybl_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "DuePyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dscnt_apld_amt: list[DiscountAmountAndType1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "DscntApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    cdt_note_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "CdtNoteAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    tax_amt: list[TaxAmountAndType1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    adjstmnt_amt_and_rsn: list[DocumentAdjustment1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class TaxRecordDetails3Pacs00200112:
    prd: Optional[TaxPeriod3Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )


@dataclass
class BranchData3Pacs00200112:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress24Pacs00200112] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class CashAccount40Pacs00200112:
    id: Optional[AccountIdentification4ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    tp: Optional[CashAccountType2ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class CreditTransferMandateData1Pacs00200112:
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[MandateTypeInformation2Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dt_of_sgntr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dt_of_vrfctn: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtOfVrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    elctrnc_sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ElctrncSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    fnl_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FnlPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    frqcy: Optional[Frequency36ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    rsn: Optional[MandateSetupReason1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class CreditorReferenceInformation2Pacs00200112:
    tp: Optional[CreditorReferenceType2Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineInformation1Pacs00200112:
    id: list[DocumentLineIdentification1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_occurs": 1,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    amt: Optional[RemittanceAmount3Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class FinancialInstitutionIdentification18Pacs00200112:
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Pacs00200112] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress24Pacs00200112] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    othr: Optional[GenericFinancialIdentification1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class Party38ChoicePacs00200112:
    org_id: Optional[OrganisationIdentification29Pacs00200112] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    prvt_id: Optional[PersonIdentification13Pacs00200112] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class TaxAmount3Pacs00200112:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "TaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    ttl_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dtls: list[TaxRecordDetails3Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification6Pacs00200112:
    fin_instn_id: Optional[FinancialInstitutionIdentification18Pacs00200112] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData3Pacs00200112] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class PartyIdentification135Pacs00200112:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress24Pacs00200112] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    id: Optional[Party38ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact4Pacs00200112] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class ReferredDocumentInformation7Pacs00200112:
    tp: Optional[ReferredDocumentType4Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    line_dtls: list[DocumentLineInformation1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "LineDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class TaxRecord3Pacs00200112:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtgyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frms_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prd: Optional[TaxPeriod3Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    tax_amt: Optional[TaxAmount3Pacs00200112] = field(
        default=None,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AmendmentInformationDetails14Pacs00200112:
    orgnl_mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_cdtr_schme_id: Optional[PartyIdentification135Pacs00200112] = field(
        default=None,
        metadata={
            "name": "OrgnlCdtrSchmeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_cdtr_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Pacs00200112
    ] = field(
        default=None,
        metadata={
            "name": "OrgnlCdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_cdtr_agt_acct: Optional[CashAccount40Pacs00200112] = field(
        default=None,
        metadata={
            "name": "OrgnlCdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_dbtr: Optional[PartyIdentification135Pacs00200112] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_dbtr_acct: Optional[CashAccount40Pacs00200112] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_dbtr_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Pacs00200112
    ] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_dbtr_agt_acct: Optional[CashAccount40Pacs00200112] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_fnl_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrgnlFnlColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_frqcy: Optional[Frequency36ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "OrgnlFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_rsn: Optional[MandateSetupReason1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "OrgnlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_trckg_days: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlTrckgDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[0-9]{2}",
        },
    )


@dataclass
class Charges7Pacs00200112:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    agt: Optional[BranchAndFinancialInstitutionIdentification6Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )


@dataclass
class Garnishment3Pacs00200112:
    tp: Optional[GarnishmentType1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    grnshee: Optional[PartyIdentification135Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Grnshee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    grnshmt_admstr: Optional[PartyIdentification135Pacs00200112] = field(
        default=None,
        metadata={
            "name": "GrnshmtAdmstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    fmly_mdcl_insrnc_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FmlyMdclInsrncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    mplyee_termntn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MplyeeTermntnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class GroupHeader101Pacs00200112:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    instg_agt: Optional[BranchAndFinancialInstitutionIdentification6Pacs00200112] = (
        field(
            default=None,
            metadata={
                "name": "InstgAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            },
        )
    )
    instd_agt: Optional[BranchAndFinancialInstitutionIdentification6Pacs00200112] = (
        field(
            default=None,
            metadata={
                "name": "InstdAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            },
        )
    )
    orgnl_biz_qry: Optional[OriginalBusinessQuery1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "OrgnlBizQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class Party40ChoicePacs00200112:
    pty: Optional[PartyIdentification135Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    agt: Optional[BranchAndFinancialInstitutionIdentification6Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class SettlementInstruction11Pacs00200112:
    sttlm_mtd: Optional[SettlementMethod1Code] = field(
        default=None,
        metadata={
            "name": "SttlmMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    sttlm_acct: Optional[CashAccount40Pacs00200112] = field(
        default=None,
        metadata={
            "name": "SttlmAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    clr_sys: Optional[ClearingSystemIdentification3ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "ClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    instg_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Pacs00200112
    ] = field(
        default=None,
        metadata={
            "name": "InstgRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    instg_rmbrsmnt_agt_acct: Optional[CashAccount40Pacs00200112] = field(
        default=None,
        metadata={
            "name": "InstgRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    instd_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Pacs00200112
    ] = field(
        default=None,
        metadata={
            "name": "InstdRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    instd_rmbrsmnt_agt_acct: Optional[CashAccount40Pacs00200112] = field(
        default=None,
        metadata={
            "name": "InstdRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    thrd_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Pacs00200112
    ] = field(
        default=None,
        metadata={
            "name": "ThrdRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    thrd_rmbrsmnt_agt_acct: Optional[CashAccount40Pacs00200112] = field(
        default=None,
        metadata={
            "name": "ThrdRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class StatusReasonInformation12Pacs00200112:
    orgtr: Optional[PartyIdentification135Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    rsn: Optional[StatusReason6ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class TaxData1Pacs00200112:
    cdtr: Optional[TaxParty1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dbtr: Optional[TaxParty2Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    ultmt_dbtr: Optional[TaxParty2Pacs00200112] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    admstn_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdmstnZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )
    mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "TtlTaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    ttl_tax_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcrd: list[TaxRecord3Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class MandateRelatedInformation15Pacs00200112:
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_sgntr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    amdmnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmdmntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    amdmnt_inf_dtls: Optional[AmendmentInformationDetails14Pacs00200112] = field(
        default=None,
        metadata={
            "name": "AmdmntInfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    elctrnc_sgntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElctrncSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 1025,
        },
    )
    frst_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    fnl_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FnlColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    frqcy: Optional[Frequency36ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    rsn: Optional[MandateSetupReason1ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    trckg_days: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrckgDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[0-9]{2}",
        },
    )


@dataclass
class OriginalGroupHeader17Pacs00200112:
    orgnl_msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OrgnlCreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_nb_of_txs: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlNbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[0-9]{1,15}",
        },
    )
    orgnl_ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OrgnlCtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    grp_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrpSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    sts_rsn_inf: list[StatusReasonInformation12Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "StsRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    nb_of_txs_per_sts: list[NumberOfTransactionsPerStatus5Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "NbOfTxsPerSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class StructuredRemittanceInformation17Pacs00200112:
    rfrd_doc_inf: list[ReferredDocumentInformation7Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "RfrdDocInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    rfrd_doc_amt: Optional[RemittanceAmount2Pacs00200112] = field(
        default=None,
        metadata={
            "name": "RfrdDocAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    cdtr_ref_inf: Optional[CreditorReferenceInformation2Pacs00200112] = field(
        default=None,
        metadata={
            "name": "CdtrRefInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    invcr: Optional[PartyIdentification135Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Invcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    invcee: Optional[PartyIdentification135Pacs00200112] = field(
        default=None,
        metadata={
            "name": "Invcee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    tax_rmt: Optional[TaxData1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "TaxRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    grnshmt_rmt: Optional[Garnishment3Pacs00200112] = field(
        default=None,
        metadata={
            "name": "GrnshmtRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    addtl_rmt_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlRmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class MandateRelatedData2ChoicePacs00200112:
    drct_dbt_mndt: Optional[MandateRelatedInformation15Pacs00200112] = field(
        default=None,
        metadata={
            "name": "DrctDbtMndt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    cdt_trf_mndt: Optional[CreditTransferMandateData1Pacs00200112] = field(
        default=None,
        metadata={
            "name": "CdtTrfMndt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class RemittanceInformation21Pacs00200112:
    ustrd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: list[StructuredRemittanceInformation17Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class OriginalTransactionReference35Pacs00200112:
    intr_bk_sttlm_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00200112] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    amt: Optional[AmountType4ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    intr_bk_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    reqd_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    reqd_exctn_dt: Optional[DateAndDateTime2ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    cdtr_schme_id: Optional[PartyIdentification135Pacs00200112] = field(
        default=None,
        metadata={
            "name": "CdtrSchmeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    sttlm_inf: Optional[SettlementInstruction11Pacs00200112] = field(
        default=None,
        metadata={
            "name": "SttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    pmt_tp_inf: Optional[PaymentTypeInformation27Pacs00200112] = field(
        default=None,
        metadata={
            "name": "PmtTpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    pmt_mtd: Optional[PaymentMethod4Code] = field(
        default=None,
        metadata={
            "name": "PmtMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    mndt_rltd_inf: Optional[MandateRelatedData2ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "MndtRltdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    rmt_inf: Optional[RemittanceInformation21Pacs00200112] = field(
        default=None,
        metadata={
            "name": "RmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    ultmt_dbtr: Optional[Party40ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dbtr: Optional[Party40ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dbtr_acct: Optional[CashAccount40Pacs00200112] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification6Pacs00200112] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            },
        )
    )
    dbtr_agt_acct: Optional[CashAccount40Pacs00200112] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification6Pacs00200112] = (
        field(
            default=None,
            metadata={
                "name": "CdtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            },
        )
    )
    cdtr_agt_acct: Optional[CashAccount40Pacs00200112] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    cdtr: Optional[Party40ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    cdtr_acct: Optional[CashAccount40Pacs00200112] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    ultmt_cdtr: Optional[Party40ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    purp: Optional[Purpose2ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class PaymentTransaction130Pacs00200112:
    sts_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_grp_inf: Optional[OriginalGroupInformation29Pacs00200112] = field(
        default=None,
        metadata={
            "name": "OrgnlGrpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    orgnl_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlEndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlUETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    tx_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 4,
        },
    )
    sts_rsn_inf: list[StatusReasonInformation12Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "StsRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    chrgs_inf: list[Charges7Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "ChrgsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    accptnc_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AccptncDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    fctv_intr_bk_sttlm_dt: Optional[DateAndDateTime2ChoicePacs00200112] = field(
        default=None,
        metadata={
            "name": "FctvIntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    acct_svcr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clr_sys_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClrSysRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instg_agt: Optional[BranchAndFinancialInstitutionIdentification6Pacs00200112] = (
        field(
            default=None,
            metadata={
                "name": "InstgAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            },
        )
    )
    instd_agt: Optional[BranchAndFinancialInstitutionIdentification6Pacs00200112] = (
        field(
            default=None,
            metadata={
                "name": "InstdAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            },
        )
    )
    orgnl_tx_ref: Optional[OriginalTransactionReference35Pacs00200112] = field(
        default=None,
        metadata={
            "name": "OrgnlTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    splmtry_data: list[SupplementaryData1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class FitoFipaymentStatusReportV12Pacs00200112:
    class Meta:
        name = "FIToFIPaymentStatusReportV12"

    grp_hdr: Optional[GroupHeader101Pacs00200112] = field(
        default=None,
        metadata={
            "name": "GrpHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
            "required": True,
        },
    )
    orgnl_grp_inf_and_sts: list[OriginalGroupHeader17Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "OrgnlGrpInfAndSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    tx_inf_and_sts: list[PaymentTransaction130Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "TxInfAndSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )
    splmtry_data: list[SupplementaryData1Pacs00200112] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12",
        },
    )


@dataclass
class Pacs00200112:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12"

    fito_fipmt_sts_rpt: Optional[FitoFipaymentStatusReportV12Pacs00200112] = field(
        default=None,
        metadata={
            "name": "FIToFIPmtStsRpt",
            "type": "Element",
            "required": True,
        },
    )
