from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.acmt.acmt_027_001_05.enums import (
    OrganisationLegalStatus1Code,
    PersonIdentificationType5Code,
)
from python_iso20022.acmt.enums import (
    BalanceTransferWindow1Code,
    Gender1Code,
    SwitchStatus1Code,
    SwitchType1Code,
    TaxRateMarker1Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    BusinessDayConvention1Code,
    ChargeBearerType1Code,
    ChequeDelivery1Code,
    ChequeType2Code,
    CreditDebitCode,
    Frequency10Code,
    NamePrefix2Code,
    PreferredContactMethod2Code,
    Priority2Code,
    RegulatoryReportingType1Code,
    RemittanceLocationMethod2Code,
    ResidentialStatus1Code,
    TaxRecordPeriod1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05"


@dataclass
class AccountSchemeName1ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountAcmt02700105(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountAcmt02700105(ISO20022MessageElement):
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
class BalanceTransferReference1Acmt02700105(ISO20022MessageElement):
    bal_trf_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BalTrfRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashAccountType2ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CategoryPurpose1ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CitizenshipInformation1Acmt02700105(ISO20022MessageElement):
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    mnr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MnrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CommunicationAddress3Acmt02700105(ISO20022MessageElement):
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mob",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    tlx_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TlxAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class CreditorReferenceType2ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPlaceOfBirth1Acmt02700105(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DatePeriod2Acmt02700105(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )


@dataclass
class DateType2ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentAmountType1ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineType1ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentType2ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class EndPoint1ChoiceAcmt02700105(ISO20022MessageElement):
    nb_of_pmts: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfPmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LastPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GarnishmentType1ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Acmt02700105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Acmt02700105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class InstructionForCreditorAgent3Acmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    instr_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class LocalInstrument2ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Acmt02700105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherContact1Acmt02700105(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PaymentIdentification6Acmt02700105(ISO20022MessageElement):
    instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountType1ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Purpose2ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RegulatoryAuthority2Acmt02700105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ResponseDetails1Acmt02700105(ISO20022MessageElement):
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class ServiceLevel8ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Acmt02700105(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TaxAuthorisation1Acmt02700105(ISO20022MessageElement):
    titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Titl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TaxParty1Acmt02700105(ISO20022MessageElement):
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransferInstruction1Acmt02700105(ISO20022MessageElement):
    trf_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrfInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 256,
        },
    )
    start_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AccountSwitchDetails1Acmt02700105(ISO20022MessageElement):
    unq_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rtg_unq_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtgUnqRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    swtch_rcvd_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SwtchRcvdDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    swtch_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SwtchDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    swtch_tp: Optional[SwitchType1Code] = field(
        default=None,
        metadata={
            "name": "SwtchTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    swtch_sts: Optional[SwitchStatus1Code] = field(
        default=None,
        metadata={
            "name": "SwtchSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    bal_trf_wndw: Optional[BalanceTransferWindow1Code] = field(
        default=None,
        metadata={
            "name": "BalTrfWndw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    rspn: list[ResponseDetails1Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "Rspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class AddressType3ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class BalanceTransferFundingLimit1Acmt02700105(ISO20022MessageElement):
    ccy_amt: Optional[ActiveCurrencyAndAmountAcmt02700105] = field(
        default=None,
        metadata={
            "name": "CcyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )


@dataclass
class ChequeDeliveryMethod1ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[ChequeDelivery1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Acmt02700105(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact13Acmt02700105(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class CountryAndResidentialStatusType1Acmt02700105(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    resdtl_sts: Optional[ResidentialStatus1Code] = field(
        default=None,
        metadata={
            "name": "ResdtlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )


@dataclass
class CreditorReferenceType3Acmt02700105(ISO20022MessageElement):
    cd_or_prtry: Optional[CreditorReferenceType2ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndType1Acmt02700105(ISO20022MessageElement):
    tp: Optional[DateType2ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )


@dataclass
class DocumentAdjustment1Acmt02700105(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DocumentAmount1Acmt02700105(ISO20022MessageElement):
    tp: Optional[DocumentAmountType1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )


@dataclass
class DocumentLineType1Acmt02700105(ISO20022MessageElement):
    cd_or_prtry: Optional[DocumentLineType1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentType1Acmt02700105(ISO20022MessageElement):
    cd_or_prtry: Optional[DocumentType2ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Frequency37ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[Frequency10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GarnishmentType1Acmt02700105(ISO20022MessageElement):
    cd_or_prtry: Optional[GarnishmentType1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericAccountIdentification1Acmt02700105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Acmt02700105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Acmt02700105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Acmt02700105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IndividualPersonNameLong2Acmt02700105(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    srnm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Srnm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    initls: Optional[str] = field(
        default=None,
        metadata={
            "name": "Initls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 6,
        },
    )
    nm_sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmSfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class OtherIdentification1ChoiceAcmt02700105(ISO20022MessageElement):
    cd: Optional[PersonIdentificationType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    prtry: Optional[GenericIdentification47Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class PaymentTypeInformation26Acmt02700105(ISO20022MessageElement):
    instr_prty: Optional[Priority2Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    svc_lvl: list[ServiceLevel8ChoiceAcmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    lcl_instrm: Optional[LocalInstrument2ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ctgy_purp: Optional[CategoryPurpose1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class ProxyAccountIdentification1Acmt02700105(ISO20022MessageElement):
    tp: Optional[ProxyAccountType1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class StructuredRegulatoryReporting3Acmt02700105(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Inf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Acmt02700105(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )


@dataclass
class TaxParty2Acmt02700105(ISO20022MessageElement):
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    authstn: Optional[TaxAuthorisation1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Authstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class TaxPeriod3Acmt02700105(ISO20022MessageElement):
    yr: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Yr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    tp: Optional[TaxRecordPeriod1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    fr_to_dt: Optional[DatePeriod2Acmt02700105] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class AccountIdentification4ChoiceAcmt02700105(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class CreditorReferenceInformation3Acmt02700105(ISO20022MessageElement):
    tp: Optional[CreditorReferenceType3Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineIdentification1Acmt02700105(ISO20022MessageElement):
    tp: Optional[DocumentLineType1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class Frequency1Acmt02700105(ISO20022MessageElement):
    seq: Optional[str] = field(
        default=None,
        metadata={
            "name": "Seq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[0-9]{1,3}",
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    end_pt_chc: Optional[EndPoint1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "EndPtChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    reqd_frqcy_pttrn: Optional[Frequency37ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "ReqdFrqcyPttrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    non_workg_day_adjstmnt: Optional[BusinessDayConvention1Code] = field(
        default=None,
        metadata={
            "name": "NonWorkgDayAdjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class GenericIdentification44Acmt02700105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[OtherIdentification1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class OrganisationIdentification39Acmt02700105(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class PersonIdentification18Acmt02700105(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    othr: list[GenericPersonIdentification2Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class PostalAddress27Acmt02700105(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class RegulatoryReporting3Acmt02700105(ISO20022MessageElement):
    dbt_cdt_rptg_ind: Optional[RegulatoryReportingType1Code] = field(
        default=None,
        metadata={
            "name": "DbtCdtRptgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    authrty: Optional[RegulatoryAuthority2Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Authrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    dtls: list[StructuredRegulatoryReporting3Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class RemittanceAmount4Acmt02700105(ISO20022MessageElement):
    rmt_amt_and_tp: list[DocumentAmount1Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "RmtAmtAndTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    adjstmnt_amt_and_rsn: list[DocumentAdjustment1Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class TaxRecordDetails3Acmt02700105(ISO20022MessageElement):
    prd: Optional[TaxPeriod3Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )


@dataclass
class BranchData5Acmt02700105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Acmt02700105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class CashAccount40Acmt02700105(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    tp: Optional[CashAccountType2ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class DocumentLineInformation2Acmt02700105(ISO20022MessageElement):
    id: list[DocumentLineIdentification1Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_occurs": 1,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    amt: Optional[RemittanceAmount4Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Acmt02700105(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Acmt02700105] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Acmt02700105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    othr: Optional[GenericFinancialIdentification1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class IndividualPerson44Acmt02700105(ISO20022MessageElement):
    cur_nm: Optional[IndividualPersonNameLong2Acmt02700105] = field(
        default=None,
        metadata={
            "name": "CurNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    prvs_nm: list[IndividualPersonNameLong2Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "PrvsNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    gndr: Optional[Gender1Code] = field(
        default=None,
        metadata={
            "name": "Gndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    taxtn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxtnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_and_resdtl_sts: Optional[CountryAndResidentialStatusType1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "CtryAndResdtlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    scl_scty_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SclSctyNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_adr: list[PostalAddress27Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ctznsh_inf: list[CitizenshipInformation1Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "CtznshInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    pmry_com_adr: Optional[CommunicationAddress3Acmt02700105] = field(
        default=None,
        metadata={
            "name": "PmryComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    scndry_com_adr: Optional[CommunicationAddress3Acmt02700105] = field(
        default=None,
        metadata={
            "name": "ScndryComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    othr_id: list[GenericIdentification44Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    othr_dtls: list[TransferInstruction1Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "OthrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class NameAndAddress18Acmt02700105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    adr: Optional[PostalAddress27Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )


@dataclass
class Party52ChoiceAcmt02700105(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification39Acmt02700105] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    prvt_id: Optional[PersonIdentification18Acmt02700105] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class TaxAmount3Acmt02700105(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmountAcmt02700105] = field(
        default=None,
        metadata={
            "name": "TaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ttl_amt: Optional[ActiveOrHistoricCurrencyAndAmountAcmt02700105] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    dtls: list[TaxRecordDetails3Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Acmt02700105(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Acmt02700105] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Acmt02700105] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class Cheque19Acmt02700105(ISO20022MessageElement):
    chq_tp: Optional[ChequeType2Code] = field(
        default=None,
        metadata={
            "name": "ChqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    chq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chq_fr: Optional[NameAndAddress18Acmt02700105] = field(
        default=None,
        metadata={
            "name": "ChqFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    dlvry_mtd: Optional[ChequeDeliveryMethod1ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "DlvryMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    dlvr_to: Optional[NameAndAddress18Acmt02700105] = field(
        default=None,
        metadata={
            "name": "DlvrTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    instr_prty: Optional[Priority2Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    chq_mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ChqMtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    frms_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    memo_fld: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MemoFld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rgnl_clr_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "RgnlClrZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prt_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sgntr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class PartyIdentification272Acmt02700105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Acmt02700105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    id: Optional[Party52ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Acmt02700105] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class ReferredDocumentInformation8Acmt02700105(ISO20022MessageElement):
    tp: Optional[DocumentType1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: Optional[DateAndType1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    line_dtls: list[DocumentLineInformation2Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "LineDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class RemittanceLocation9Acmt02700105(ISO20022MessageElement):
    rmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rmt_lctn_mtd: Optional[RemittanceLocationMethod2Code] = field(
        default=None,
        metadata={
            "name": "RmtLctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    rmt_lctn_elctrnc_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "RmtLctnElctrncAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    rmt_lctn_pstl_adr: Optional[NameAndAddress18Acmt02700105] = field(
        default=None,
        metadata={
            "name": "RmtLctnPstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class TaxRecord3Acmt02700105(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtgyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frms_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prd: Optional[TaxPeriod3Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    tax_amt: Optional[TaxAmount3Acmt02700105] = field(
        default=None,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class CashAccount43Acmt02700105(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    tp: Optional[CashAccountType2ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ownr: Optional[PartyIdentification272Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Ownr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    svcr: Optional[BranchAndFinancialInstitutionIdentification8Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class Garnishment4Acmt02700105(ISO20022MessageElement):
    tp: Optional[GarnishmentType1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    grnshee: Optional[PartyIdentification272Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Grnshee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    grnshmt_admstr: Optional[PartyIdentification272Acmt02700105] = field(
        default=None,
        metadata={
            "name": "GrnshmtAdmstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmountAcmt02700105] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    fmly_mdcl_insrnc_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FmlyMdclInsrncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    mplyee_termntn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MplyeeTermntnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class Organisation43Acmt02700105(ISO20022MessageElement):
    full_lgl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullLglNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    tradg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    org_lgl_sts: Optional[OrganisationLegalStatus1Code] = field(
        default=None,
        metadata={
            "name": "OrgLglSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    estblishd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EstblishdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    regn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RegnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    taxtn_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxtnIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    taxtn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxtnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_of_opr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfOpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    brd_rsltn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BrdRsltnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    biz_adr: Optional[PostalAddress27Acmt02700105] = field(
        default=None,
        metadata={
            "name": "BizAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    oprl_adr: Optional[PostalAddress27Acmt02700105] = field(
        default=None,
        metadata={
            "name": "OprlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    lgl_adr: Optional[PostalAddress27Acmt02700105] = field(
        default=None,
        metadata={
            "name": "LglAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    rprtv_offcr: list[PartyIdentification272Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "RprtvOffcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    trsr_mgr: Optional[PartyIdentification272Acmt02700105] = field(
        default=None,
        metadata={
            "name": "TrsrMgr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    main_mndt_hldr: list[PartyIdentification272Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "MainMndtHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    sndr: list[PartyIdentification272Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class TaxData1Acmt02700105(ISO20022MessageElement):
    cdtr: Optional[TaxParty1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    dbtr: Optional[TaxParty2Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ultmt_dbtr: Optional[TaxParty2Acmt02700105] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    admstn_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdmstnZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmountAcmt02700105] = field(
        default=None,
        metadata={
            "name": "TtlTaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ttl_tax_amt: Optional[ActiveOrHistoricCurrencyAndAmountAcmt02700105] = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcrd: list[TaxRecord3Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class NewAccount4Acmt02700105(ISO20022MessageElement):
    acct: Optional[CashAccount43Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    acct_pty: list[IndividualPerson44Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "AcctPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_occurs": 1,
        },
    )
    org: Optional[Organisation43Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Org",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class StructuredRemittanceInformation18Acmt02700105(ISO20022MessageElement):
    rfrd_doc_inf: list[ReferredDocumentInformation8Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "RfrdDocInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    rfrd_doc_amt: Optional[RemittanceAmount4Acmt02700105] = field(
        default=None,
        metadata={
            "name": "RfrdDocAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    cdtr_ref_inf: Optional[CreditorReferenceInformation3Acmt02700105] = field(
        default=None,
        metadata={
            "name": "CdtrRefInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    invcr: Optional[PartyIdentification272Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Invcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    invcee: Optional[PartyIdentification272Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Invcee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    tax_rmt: Optional[TaxData1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "TaxRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    grnshmt_rmt: Optional[Garnishment4Acmt02700105] = field(
        default=None,
        metadata={
            "name": "GrnshmtRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    addtl_rmt_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlRmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class RemittanceInformation22Acmt02700105(ISO20022MessageElement):
    ustrd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: list[StructuredRemittanceInformation18Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class CreditTransferTransaction59Acmt02700105(ISO20022MessageElement):
    pmt_id: Optional[PaymentIdentification6Acmt02700105] = field(
        default=None,
        metadata={
            "name": "PmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    pmt_tp_inf: Optional[PaymentTypeInformation26Acmt02700105] = field(
        default=None,
        metadata={
            "name": "PmtTpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    tax_rate_mrkr: Optional[TaxRateMarker1Code] = field(
        default=None,
        metadata={
            "name": "TaxRateMrkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    chrg_br: Optional[ChargeBearerType1Code] = field(
        default=None,
        metadata={
            "name": "ChrgBr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    chq_instr: Optional[Cheque19Acmt02700105] = field(
        default=None,
        metadata={
            "name": "ChqInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    frqcy: Optional[Frequency1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    trf_instr: Optional[TransferInstruction1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "TrfInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ultmt_dbtr: Optional[PartyIdentification272Acmt02700105] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    intrmy_agt1: Optional[BranchAndFinancialInstitutionIdentification8Acmt02700105] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt1",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            },
        )
    )
    intrmy_agt2: Optional[BranchAndFinancialInstitutionIdentification8Acmt02700105] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt2",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            },
        )
    )
    intrmy_agt3: Optional[BranchAndFinancialInstitutionIdentification8Acmt02700105] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt3",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            },
        )
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Acmt02700105] = (
        field(
            default=None,
            metadata={
                "name": "CdtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
                "required": True,
            },
        )
    )
    cdtr: Optional[PartyIdentification272Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    cdtr_acct: Optional[CashAccount40Acmt02700105] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    ultmt_cdtr: Optional[PartyIdentification272Acmt02700105] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    instr_for_cdtr_agt: list[InstructionForCreditorAgent3Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "InstrForCdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    purp: Optional[Purpose2ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    rgltry_rptg: list[RegulatoryReporting3Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "RgltryRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "max_occurs": 10,
        },
    )
    tax: Optional[TaxData1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    rltd_rmt_inf: list[RemittanceLocation9Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "RltdRmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "max_occurs": 10,
        },
    )
    rmt_inf: Optional[RemittanceInformation22Acmt02700105] = field(
        default=None,
        metadata={
            "name": "RmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class SettlementMethod5ChoiceAcmt02700105(ISO20022MessageElement):
    cdt: Optional[CreditTransferTransaction59Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Cdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    dbt: Optional[CreditTransferTransaction59Acmt02700105] = field(
        default=None,
        metadata={
            "name": "Dbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class BalanceTransfer5Acmt02700105(ISO20022MessageElement):
    bal_trf_ref: Optional[BalanceTransferReference1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "BalTrfRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    bal_trf_mtd: Optional[SettlementMethod5ChoiceAcmt02700105] = field(
        default=None,
        metadata={
            "name": "BalTrfMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    bal_trf_fndg_lmt: Optional[BalanceTransferFundingLimit1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "BalTrfFndgLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class AccountSwitchInformationRequestV05Acmt02700105(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    acct_swtch_dtls: Optional[AccountSwitchDetails1Acmt02700105] = field(
        default=None,
        metadata={
            "name": "AcctSwtchDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    new_acct: Optional[NewAccount4Acmt02700105] = field(
        default=None,
        metadata={
            "name": "NewAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    od_acct: Optional[CashAccount43Acmt02700105] = field(
        default=None,
        metadata={
            "name": "OdAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
            "required": True,
        },
    )
    bal_trf: list[BalanceTransfer5Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "BalTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )
    splmtry_data: list[SupplementaryData1Acmt02700105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05",
        },
    )


@dataclass
class Acmt02700105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05"

    acct_swtch_inf_req: Optional[AccountSwitchInformationRequestV05Acmt02700105] = (
        field(
            default=None,
            metadata={
                "name": "AcctSwtchInfReq",
                "type": "Element",
                "required": True,
            },
        )
    )
