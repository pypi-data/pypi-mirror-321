from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code, NamePrefix1Code
from python_iso20022.tsrv.enums import TerminationReason1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01"


@dataclass
class ActiveCurrencyAndAmountTsrv00600101(ISO20022MessageElement):
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
class AdvisingPartyAdditionalInformation1Tsrv00600101(ISO20022MessageElement):
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    bk_to_bnfcry_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BkToBnfcryInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class AutoExtend1ChoiceTsrv00600101(ISO20022MessageElement):
    days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Days",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    mnths: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Mnths",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    yrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class DateAndDateTimeChoiceTsrv00600101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class DateAndPlaceOfBirthTsrv00600101(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class GenericIdentification1Tsrv00600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceTsrv00600101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceTsrv00600101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProprietaryData3Tsrv00600101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass
class Amount1ChoiceTsrv00600101(ISO20022MessageElement):
    incr_amt: Optional[ActiveCurrencyAndAmountTsrv00600101] = field(
        default=None,
        metadata={
            "name": "IncrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    dcr_amt: Optional[ActiveCurrencyAndAmountTsrv00600101] = field(
        default=None,
        metadata={
            "name": "DcrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class CommunicationMethod1ChoiceTsrv00600101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class ContactDetails2Tsrv00600101(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentFormat1ChoiceTsrv00600101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class GenericOrganisationIdentification1Tsrv00600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification1Tsrv00600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NarrativeType1ChoiceTsrv00600101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class PartyType1ChoiceTsrv00600101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class PostalAddress6Tsrv00600101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class TerminationReason1ChoiceTsrv00600101(ISO20022MessageElement):
    cd: Optional[TerminationReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class UndertakingDocumentType1ChoiceTsrv00600101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class CommunicationChannel1Tsrv00600101(ISO20022MessageElement):
    mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    dlvr_to_pty_tp: Optional[PartyType1ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "DlvrToPtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    dlvr_to_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvrToNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dlvr_to_adr: Optional[PostalAddress6Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "DlvrToAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class Narrative1Tsrv00600101(ISO20022MessageElement):
    tp: Optional[NarrativeType1ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_occurs": 1,
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 20000,
        },
    )


@dataclass
class NonExtension1Tsrv00600101(ISO20022MessageElement):
    ntfctn_prd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NtfctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ntfctn_mtd: Optional[CommunicationMethod1ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "NtfctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    ntfctn_rcpt_tp: Optional[PartyType1ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "NtfctnRcptTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    ntfctn_rcpt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtfctnRcptNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ntfctn_rcpt_adr: Optional[PostalAddress6Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "NtfctnRcptAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class OrganisationIdentification8Tsrv00600101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Tsrv00600101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class PersonIdentification5Tsrv00600101(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirthTsrv00600101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    othr: list[GenericPersonIdentification1Tsrv00600101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class UndertakingAmount2Tsrv00600101(ISO20022MessageElement):
    amt_chc: Optional[Amount1ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "AmtChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class UndertakingTermination3Tsrv00600101(ISO20022MessageElement):
    fctv_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    rsn: Optional[TerminationReason1ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class AutoExtension1Tsrv00600101(ISO20022MessageElement):
    prd: Optional[AutoExtend1ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    fnl_xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FnlXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    non_xtnsn_ntfctn: list[NonExtension1Tsrv00600101] = field(
        default_factory=list,
        metadata={
            "name": "NonXtnsnNtfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class Party11ChoiceTsrv00600101(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification8Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class ExpiryTerms1Tsrv00600101(ISO20022MessageElement):
    dt_tm: Optional[DateAndDateTimeChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    auto_xtnsn: Optional[AutoExtension1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "AutoXtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    cond: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 2000,
        },
    )
    opn_endd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OpnEnddInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class PartyIdentification43Tsrv00600101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    id: Optional[Party11ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[ContactDetails2Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class ExpiryDetails1Tsrv00600101(ISO20022MessageElement):
    xpry_terms: Optional[ExpiryTerms1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "XpryTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    addtl_xpry_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlXpryInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class PartyAndSignature2Tsrv00600101(ISO20022MessageElement):
    pty: Optional[PartyIdentification43Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    sgntr: Optional[ProprietaryData3Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )


@dataclass
class Undertaking7Tsrv00600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[PartyIdentification43Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )


@dataclass
class UndertakingConfirmation1Tsrv00600101(ISO20022MessageElement):
    cnfrmr: Optional[PartyIdentification43Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "Cnfrmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[DateAndDateTimeChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    conf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Conf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class Document9Tsrv00600101(ISO20022MessageElement):
    tp: Optional[UndertakingDocumentType1ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    frmt: Optional[DocumentFormat1ChoiceTsrv00600101] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    nclsr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Nclsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    dgtl_sgntr: Optional[PartyAndSignature2Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class Undertaking11Tsrv00600101(ISO20022MessageElement):
    new_udrtkg_amt: Optional[UndertakingAmount2Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "NewUdrtkgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    new_xpry_dtls: Optional[ExpiryDetails1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "NewXpryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    new_bnfcry: Optional[PartyIdentification43Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "NewBnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    new_udrtkg_terms_and_conds: Optional[Narrative1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "NewUdrtkgTermsAndConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    dlvry_chanl: Optional[CommunicationChannel1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "DlvryChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class Amendment1Tsrv00600101(ISO20022MessageElement):
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    dt_of_issnc: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIssnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    udrtkg_id: Optional[Undertaking7Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "UdrtkgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    advsg_pty: Optional[PartyIdentification43Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "AdvsgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    scnd_advsg_pty: Optional[PartyIdentification43Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "ScndAdvsgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    termntn_dtls: Optional[UndertakingTermination3Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "TermntnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    udrtkg_amt_adjstmnt: Optional[UndertakingAmount2Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "UdrtkgAmtAdjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    new_xpry_dtls: Optional[ExpiryDetails1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "NewXpryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    new_bnfcry: Optional[PartyIdentification43Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "NewBnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    new_udrtkg_terms_and_conds: list[Narrative1Tsrv00600101] = field(
        default_factory=list,
        metadata={
            "name": "NewUdrtkgTermsAndConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    lcl_udrtkg: Optional[Undertaking11Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "LclUdrtkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    bnfcry_cnsnt_req_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BnfcryCnsntReqInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    dlvry_chanl: Optional[CommunicationChannel1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "DlvryChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    nclsd_file: list[Document9Tsrv00600101] = field(
        default_factory=list,
        metadata={
            "name": "NclsdFile",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class UndertakingAmendmentMessage1Tsrv00600101(ISO20022MessageElement):
    udrtkg_amdmnt_dtls: Optional[Amendment1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "UdrtkgAmdmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    dgtl_sgntr: Optional[PartyAndSignature2Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class Amendment2Tsrv00600101(ISO20022MessageElement):
    udrtkg_amdmnt_msg: Optional[UndertakingAmendmentMessage1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "UdrtkgAmdmntMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    frst_advsg_pty_addtl_inf: Optional[
        AdvisingPartyAdditionalInformation1Tsrv00600101
    ] = field(
        default=None,
        metadata={
            "name": "FrstAdvsgPtyAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    scnd_advsg_pty_addtl_inf: Optional[
        AdvisingPartyAdditionalInformation1Tsrv00600101
    ] = field(
        default=None,
        metadata={
            "name": "ScndAdvsgPtyAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    conf_dtls: Optional[UndertakingConfirmation1Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "ConfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    dgtl_sgntr: list[PartyAndSignature2Tsrv00600101] = field(
        default_factory=list,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "max_occurs": 3,
        },
    )


@dataclass
class UndertakingAmendmentAdviceV01Tsrv00600101(ISO20022MessageElement):
    advsg_pty: Optional[PartyIdentification43Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "AdvsgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    scnd_advsg_pty: Optional[PartyIdentification43Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "ScndAdvsgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )
    dt_of_advc: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    udrtkg_amdmnt_advc_dtls: Optional[Amendment2Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "UdrtkgAmdmntAdvcDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "required": True,
        },
    )
    bk_to_bk_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BkToBkInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )
    dgtl_sgntr: Optional[PartyAndSignature2Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
        },
    )


@dataclass
class Tsrv00600101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01"

    udrtkg_amdmnt_advc: Optional[UndertakingAmendmentAdviceV01Tsrv00600101] = field(
        default=None,
        metadata={
            "name": "UdrtkgAmdmntAdvc",
            "type": "Element",
            "required": True,
        },
    )
