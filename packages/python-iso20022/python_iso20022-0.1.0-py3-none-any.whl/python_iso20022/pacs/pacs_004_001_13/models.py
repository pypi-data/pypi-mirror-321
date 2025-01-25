from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

from python_iso20022.enums import (
    AddressType2Code,
    Authorisation1Code,
    ChargeBearerType1Code,
    ClearingChannel2Code,
    CreditDebitCode,
    Frequency6Code,
    Instruction4Code,
    MandateClassification1Code,
    NamePrefix2Code,
    PaymentMethod4Code,
    PreferredContactMethod2Code,
    Priority2Code,
    Priority3Code,
    SequenceType3Code,
    SettlementMethod1Code,
    TaxRecordPeriod1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13"


@dataclass
class AccountSchemeName1ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountPacs00400113:
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
class ActiveOrHistoricCurrencyAndAmountPacs00400113:
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
class CashAccountType2ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CategoryPurpose1ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification3ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 3,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CreditorReferenceType2ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTime2ChoicePacs00400113:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class DateAndPlaceOfBirth1Pacs00400113:
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DatePeriod2Pacs00400113:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )


@dataclass
class DateType2ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentAmountType1ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineType1ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentType2ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GarnishmentType1ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification3Pacs00400113:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Pacs00400113:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InstructionForCreditorAgent3Pacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    instr_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class LocalInstrument2ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MandateSetupReason1ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalGroupInformation29Pacs00400113:
    orgnl_msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class OtherContact1Pacs00400113:
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountType1ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Purpose2ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ReturnReason5ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ServiceLevel8ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementDateTimeIndication1Pacs00400113:
    dbt_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DbtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    cdt_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CdtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class SettlementTimeRequest2Pacs00400113:
    clstm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "CLSTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    till_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "TillTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    fr_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "FrTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rjct_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "RjctTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Pacs00400113:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TaxAuthorisation1Pacs00400113:
    titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Titl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TaxParty1Pacs00400113:
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AddressType3ChoicePacs00400113:
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prtry: Optional[GenericIdentification30Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class Authorisation1ChoicePacs00400113:
    cd: Optional[Authorisation1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class ChargeType3ChoicePacs00400113:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification3Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Pacs00400113:
    clr_sys_id: Optional[ClearingSystemIdentification2ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact13Pacs00400113:
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class CreditorReferenceType3Pacs00400113:
    cd_or_prtry: Optional[CreditorReferenceType2ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndType1Pacs00400113:
    tp: Optional[DateType2ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )


@dataclass
class DocumentAdjustment1Pacs00400113:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DocumentAmount1Pacs00400113:
    tp: Optional[DocumentAmountType1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )


@dataclass
class DocumentLineType1Pacs00400113:
    cd_or_prtry: Optional[DocumentLineType1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentType1Pacs00400113:
    cd_or_prtry: Optional[DocumentType2ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class EquivalentAmount2Pacs00400113:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    ccy_of_trf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOfTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class FrequencyAndMoment1Pacs00400113:
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    pt_in_tm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "pattern": r"[0-9]{2}",
        },
    )


@dataclass
class FrequencyPeriod1Pacs00400113:
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    cnt_per_prd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CntPerPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class GarnishmentType1Pacs00400113:
    cd_or_prtry: Optional[GarnishmentType1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericAccountIdentification1Pacs00400113:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Pacs00400113:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Pacs00400113:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Pacs00400113:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InstructionForNextAgent1Pacs00400113:
    cd: Optional[Instruction4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    instr_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class MandateClassification1ChoicePacs00400113:
    cd: Optional[MandateClassification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentTypeInformation27Pacs00400113:
    instr_prty: Optional[Priority2Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    clr_chanl: Optional[ClearingChannel2Code] = field(
        default=None,
        metadata={
            "name": "ClrChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    svc_lvl: list[ServiceLevel8ChoicePacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    lcl_instrm: Optional[LocalInstrument2ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    seq_tp: Optional[SequenceType3Code] = field(
        default=None,
        metadata={
            "name": "SeqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ctgy_purp: Optional[CategoryPurpose1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class PaymentTypeInformation28Pacs00400113:
    instr_prty: Optional[Priority2Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    clr_chanl: Optional[ClearingChannel2Code] = field(
        default=None,
        metadata={
            "name": "ClrChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    svc_lvl: list[ServiceLevel8ChoicePacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    lcl_instrm: Optional[LocalInstrument2ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ctgy_purp: Optional[CategoryPurpose1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class ProxyAccountIdentification1Pacs00400113:
    tp: Optional[ProxyAccountType1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class SupplementaryData1Pacs00400113:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )


@dataclass
class TaxParty2Pacs00400113:
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    authstn: Optional[TaxAuthorisation1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Authstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class TaxPeriod3Pacs00400113:
    yr: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Yr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    tp: Optional[TaxRecordPeriod1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    fr_to_dt: Optional[DatePeriod2Pacs00400113] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class AccountIdentification4ChoicePacs00400113:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class AmountType4ChoicePacs00400113:
    instd_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "InstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    eqvt_amt: Optional[EquivalentAmount2Pacs00400113] = field(
        default=None,
        metadata={
            "name": "EqvtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class CreditorReferenceInformation3Pacs00400113:
    tp: Optional[CreditorReferenceType3Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineIdentification1Pacs00400113:
    tp: Optional[DocumentLineType1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class Frequency36ChoicePacs00400113:
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prd: Optional[FrequencyPeriod1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    pt_in_tm: Optional[FrequencyAndMoment1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PtInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class MandateTypeInformation2Pacs00400113:
    svc_lvl: Optional[ServiceLevel8ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    lcl_instrm: Optional[LocalInstrument2ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ctgy_purp: Optional[CategoryPurpose1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    clssfctn: Optional[MandateClassification1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class OrganisationIdentification39Pacs00400113:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class PersonIdentification18Pacs00400113:
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    othr: list[GenericPersonIdentification2Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class PostalAddress27Pacs00400113:
    adr_tp: Optional[AddressType3ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class RemittanceAmount4Pacs00400113:
    rmt_amt_and_tp: list[DocumentAmount1Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "RmtAmtAndTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    adjstmnt_amt_and_rsn: list[DocumentAdjustment1Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class TaxRecordDetails3Pacs00400113:
    prd: Optional[TaxPeriod3Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )


@dataclass
class BranchData5Pacs00400113:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class CashAccount40Pacs00400113:
    id: Optional[AccountIdentification4ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    tp: Optional[CashAccountType2ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class CreditTransferMandateData1Pacs00400113:
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[MandateTypeInformation2Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dt_of_sgntr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dt_of_vrfctn: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtOfVrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    elctrnc_sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ElctrncSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    fnl_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FnlPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    frqcy: Optional[Frequency36ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rsn: Optional[MandateSetupReason1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class DocumentLineInformation2Pacs00400113:
    id: list[DocumentLineIdentification1Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_occurs": 1,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    amt: Optional[RemittanceAmount4Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Pacs00400113:
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Pacs00400113] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    othr: Optional[GenericFinancialIdentification1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class Party52ChoicePacs00400113:
    org_id: Optional[OrganisationIdentification39Pacs00400113] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvt_id: Optional[PersonIdentification18Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class TaxAmount3Pacs00400113:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "TaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ttl_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dtls: list[TaxRecordDetails3Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Pacs00400113:
    fin_instn_id: Optional[FinancialInstitutionIdentification23Pacs00400113] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Pacs00400113] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class PartyIdentification272Pacs00400113:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    id: Optional[Party52ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Pacs00400113] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class ReferredDocumentInformation8Pacs00400113:
    tp: Optional[DocumentType1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: Optional[DateAndType1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    line_dtls: list[DocumentLineInformation2Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "LineDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class TaxRecord3Pacs00400113:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtgyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frms_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prd: Optional[TaxPeriod3Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    tax_amt: Optional[TaxAmount3Pacs00400113] = field(
        default=None,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AmendmentInformationDetails15Pacs00400113:
    orgnl_mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_cdtr_schme_id: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "OrgnlCdtrSchmeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_cdtr_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Pacs00400113
    ] = field(
        default=None,
        metadata={
            "name": "OrgnlCdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_cdtr_agt_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "OrgnlCdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_dbtr: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_dbtr_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_dbtr_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Pacs00400113
    ] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_dbtr_agt_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_fnl_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrgnlFnlColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_frqcy: Optional[Frequency36ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "OrgnlFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_rsn: Optional[MandateSetupReason1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "OrgnlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_trckg_days: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlTrckgDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[0-9]{2}",
        },
    )


@dataclass
class Charges16Pacs00400113:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    tp: Optional[ChargeType3ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class Garnishment4Pacs00400113:
    tp: Optional[GarnishmentType1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    grnshee: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Grnshee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    grnshmt_admstr: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "GrnshmtAdmstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    fmly_mdcl_insrnc_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FmlyMdclInsrncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    mplyee_termntn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MplyeeTermntnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class Party50ChoicePacs00400113:
    pty: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class PaymentReturnReason7Pacs00400113:
    orgtr: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rsn: Optional[ReturnReason5ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class SettlementInstruction15Pacs00400113:
    sttlm_mtd: Optional[SettlementMethod1Code] = field(
        default=None,
        metadata={
            "name": "SttlmMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    sttlm_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "SttlmAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    clr_sys: Optional[ClearingSystemIdentification3ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "ClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    instg_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Pacs00400113
    ] = field(
        default=None,
        metadata={
            "name": "InstgRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    instg_rmbrsmnt_agt_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "InstgRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    instd_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Pacs00400113
    ] = field(
        default=None,
        metadata={
            "name": "InstdRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    instd_rmbrsmnt_agt_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "InstdRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    thrd_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Pacs00400113
    ] = field(
        default=None,
        metadata={
            "name": "ThrdRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    thrd_rmbrsmnt_agt_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "ThrdRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class TaxData1Pacs00400113:
    cdtr: Optional[TaxParty1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dbtr: Optional[TaxParty2Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ultmt_dbtr: Optional[TaxParty2Pacs00400113] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    admstn_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdmstnZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "TtlTaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ttl_tax_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcrd: list[TaxRecord3Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class GroupHeader123Pacs00400113:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    authstn: list[Authorisation1ChoicePacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "Authstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "max_occurs": 2,
        },
    )
    btch_bookg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BtchBookg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    nb_of_txs: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    grp_rtr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GrpRtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ttl_rtrd_intr_bk_sttlm_amt: Optional[ActiveCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "TtlRtrdIntrBkSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    intr_bk_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    sttlm_inf: Optional[SettlementInstruction15Pacs00400113] = field(
        default=None,
        metadata={
            "name": "SttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    pmt_tp_inf: Optional[PaymentTypeInformation28Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PmtTpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    instg_agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "InstgAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    instd_agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "InstdAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )


@dataclass
class MandateRelatedInformation16Pacs00400113:
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_sgntr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    amdmnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmdmntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    amdmnt_inf_dtls: Optional[AmendmentInformationDetails15Pacs00400113] = field(
        default=None,
        metadata={
            "name": "AmdmntInfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    elctrnc_sgntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElctrncSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 1025,
        },
    )
    frst_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    fnl_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FnlColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    frqcy: Optional[Frequency36ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rsn: Optional[MandateSetupReason1ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    trckg_days: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrckgDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[0-9]{2}",
        },
    )


@dataclass
class OriginalGroupHeader19Pacs00400113:
    orgnl_msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rtr_rsn_inf: list[PaymentReturnReason7Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "RtrRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class StructuredRemittanceInformation18Pacs00400113:
    rfrd_doc_inf: list[ReferredDocumentInformation8Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "RfrdDocInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rfrd_doc_amt: Optional[RemittanceAmount4Pacs00400113] = field(
        default=None,
        metadata={
            "name": "RfrdDocAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    cdtr_ref_inf: Optional[CreditorReferenceInformation3Pacs00400113] = field(
        default=None,
        metadata={
            "name": "CdtrRefInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    invcr: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Invcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    invcee: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Invcee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    tax_rmt: Optional[TaxData1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "TaxRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    grnshmt_rmt: Optional[Garnishment4Pacs00400113] = field(
        default=None,
        metadata={
            "name": "GrnshmtRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    addtl_rmt_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlRmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TransactionParties11Pacs00400113:
    ultmt_dbtr: Optional[Party50ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dbtr: Optional[Party50ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    dbtr_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    initg_pty: Optional[Party50ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    dbtr_agt_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt1: Optional[
        BranchAndFinancialInstitutionIdentification8Pacs00400113
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt1_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt2: Optional[
        BranchAndFinancialInstitutionIdentification8Pacs00400113
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt2_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt3: Optional[
        BranchAndFinancialInstitutionIdentification8Pacs00400113
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt3_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt3Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    intrmy_agt1: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt1",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    intrmy_agt1_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    intrmy_agt2: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt2",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    intrmy_agt2_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    intrmy_agt3: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt3",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    intrmy_agt3_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt3Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "CdtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    cdtr_agt_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    cdtr: Optional[Party50ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    cdtr_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ultmt_cdtr: Optional[Party50ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class MandateRelatedData3ChoicePacs00400113:
    drct_dbt_mndt: Optional[MandateRelatedInformation16Pacs00400113] = field(
        default=None,
        metadata={
            "name": "DrctDbtMndt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    cdt_trf_mndt: Optional[CreditTransferMandateData1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "CdtTrfMndt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class RemittanceInformation22Pacs00400113:
    ustrd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: list[StructuredRemittanceInformation18Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class CreditTransferTransaction63Pacs00400113:
    ultmt_dbtr: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    initg_pty: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dbtr: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    dbtr_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
                "required": True,
            },
        )
    )
    dbtr_agt_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt1: Optional[
        BranchAndFinancialInstitutionIdentification8Pacs00400113
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt1_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt2: Optional[
        BranchAndFinancialInstitutionIdentification8Pacs00400113
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt2_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt3: Optional[
        BranchAndFinancialInstitutionIdentification8Pacs00400113
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    prvs_instg_agt3_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt3Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    intrmy_agt1: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt1",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    intrmy_agt1_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    intrmy_agt2: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt2",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    intrmy_agt2_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    intrmy_agt3: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt3",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    intrmy_agt3_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt3Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "CdtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
                "required": True,
            },
        )
    )
    cdtr_agt_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    cdtr: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    cdtr_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ultmt_cdtr: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    instr_for_cdtr_agt: list[InstructionForCreditorAgent3Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "InstrForCdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    instr_for_nxt_agt: list[InstructionForNextAgent1Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "InstrForNxtAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    tax: Optional[TaxData1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rmt_inf: Optional[RemittanceInformation22Pacs00400113] = field(
        default=None,
        metadata={
            "name": "RmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    instd_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "InstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class OriginalTransactionReference41Pacs00400113:
    intr_bk_sttlm_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    amt: Optional[AmountType4ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    intr_bk_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    reqd_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    reqd_exctn_dt: Optional[DateAndDateTime2ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    cdtr_schme_id: Optional[PartyIdentification272Pacs00400113] = field(
        default=None,
        metadata={
            "name": "CdtrSchmeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    sttlm_inf: Optional[SettlementInstruction15Pacs00400113] = field(
        default=None,
        metadata={
            "name": "SttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    pmt_tp_inf: Optional[PaymentTypeInformation27Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PmtTpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    pmt_mtd: Optional[PaymentMethod4Code] = field(
        default=None,
        metadata={
            "name": "PmtMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    mndt_rltd_inf: Optional[MandateRelatedData3ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "MndtRltdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rmt_inf: Optional[RemittanceInformation22Pacs00400113] = field(
        default=None,
        metadata={
            "name": "RmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ultmt_dbtr: Optional[Party50ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dbtr: Optional[Party50ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dbtr_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    dbtr_agt_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "CdtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    cdtr_agt_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    cdtr: Optional[Party50ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    cdtr_acct: Optional[CashAccount40Pacs00400113] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    ultmt_cdtr: Optional[Party50ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    purp: Optional[Purpose2ChoicePacs00400113] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    undrlyg_cstmr_cdt_trf: Optional[CreditTransferTransaction63Pacs00400113] = field(
        default=None,
        metadata={
            "name": "UndrlygCstmrCdtTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class PaymentTransaction159Pacs00400113:
    rtr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_grp_inf: Optional[OriginalGroupInformation29Pacs00400113] = field(
        default=None,
        metadata={
            "name": "OrgnlGrpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlEndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlUETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    orgnl_clr_sys_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlClrSysRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_intr_bk_sttlm_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlIntrBkSttlmAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    orgnl_intr_bk_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrgnlIntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    pmt_tp_inf: Optional[PaymentTypeInformation28Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PmtTpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rtrd_intr_bk_sttlm_amt: Optional[ActiveCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "RtrdIntrBkSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    intr_bk_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    sttlm_prty: Optional[Priority3Code] = field(
        default=None,
        metadata={
            "name": "SttlmPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    sttlm_tm_indctn: Optional[SettlementDateTimeIndication1Pacs00400113] = field(
        default=None,
        metadata={
            "name": "SttlmTmIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    sttlm_tm_req: Optional[SettlementTimeRequest2Pacs00400113] = field(
        default=None,
        metadata={
            "name": "SttlmTmReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rtrd_instd_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "RtrdInstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    compstn_amt: Optional[ActiveOrHistoricCurrencyAndAmountPacs00400113] = field(
        default=None,
        metadata={
            "name": "CompstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    chrg_br: Optional[ChargeBearerType1Code] = field(
        default=None,
        metadata={
            "name": "ChrgBr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    chrgs_inf: list[Charges16Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "ChrgsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    clr_sys_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClrSysRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instg_agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "InstgAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    instd_agt: Optional[BranchAndFinancialInstitutionIdentification8Pacs00400113] = (
        field(
            default=None,
            metadata={
                "name": "InstdAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            },
        )
    )
    rtr_chain: Optional[TransactionParties11Pacs00400113] = field(
        default=None,
        metadata={
            "name": "RtrChain",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    rtr_rsn_inf: list[PaymentReturnReason7Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "RtrRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    orgnl_tx_ref: Optional[OriginalTransactionReference41Pacs00400113] = field(
        default=None,
        metadata={
            "name": "OrgnlTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    splmtry_data: list[SupplementaryData1Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class PaymentReturnV13Pacs00400113:
    grp_hdr: Optional[GroupHeader123Pacs00400113] = field(
        default=None,
        metadata={
            "name": "GrpHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
            "required": True,
        },
    )
    orgnl_grp_inf: Optional[OriginalGroupHeader19Pacs00400113] = field(
        default=None,
        metadata={
            "name": "OrgnlGrpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    tx_inf: list[PaymentTransaction159Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "TxInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )
    splmtry_data: list[SupplementaryData1Pacs00400113] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13",
        },
    )


@dataclass
class Pacs00400113:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.13"

    pmt_rtr: Optional[PaymentReturnV13Pacs00400113] = field(
        default=None,
        metadata={
            "name": "PmtRtr",
            "type": "Element",
            "required": True,
        },
    )
