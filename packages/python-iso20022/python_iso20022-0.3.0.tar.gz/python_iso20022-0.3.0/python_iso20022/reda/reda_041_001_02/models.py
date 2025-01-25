from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    NamePrefix2Code,
    PreferredContactMethod2Code,
)
from python_iso20022.reda.enums import LockStatus1Code, ResidenceType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02"


@dataclass
class GenericIdentification13Reda04100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Reda04100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Reda04100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketSpecificAttribute1Reda04100102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class MessageHeader1Reda04100102(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class OtherContact1Reda04100102(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PartyName4Reda04100102(ISO20022MessageElement):
    vld_fr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda04100102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SystemPartyType1ChoiceReda04100102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TechnicalIdentification2ChoiceReda04100102(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    tech_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class UpdateLogDate1Reda04100102(ISO20022MessageElement):
    od: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    new: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class UpdateLogProprietary1Reda04100102(ISO20022MessageElement):
    fld_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FldNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    od_fld_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "OdFldVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    new_fld_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewFldVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AddressType3ChoiceReda04100102(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Reda04100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class CodeOrProprietary1ChoiceReda04100102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification13Reda04100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class Contact14Reda04100102(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Reda04100102] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    vld_fr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    vld_to: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class PartyLockStatus1Reda04100102(ISO20022MessageElement):
    vld_fr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    sts: Optional[LockStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    lck_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "LckRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress1Reda04100102(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryData1Reda04100102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda04100102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class UpdateLogMarketSpecificAttribute1Reda04100102(ISO20022MessageElement):
    od: Optional[MarketSpecificAttribute1Reda04100102] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    new: Optional[MarketSpecificAttribute1Reda04100102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class UpdateLogPartyName1Reda04100102(ISO20022MessageElement):
    od: Optional[PartyName4Reda04100102] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    new: Optional[PartyName4Reda04100102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class UpdateLogResidenceType1Reda04100102(ISO20022MessageElement):
    od: Optional[ResidenceType1Code] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    new: Optional[ResidenceType1Code] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class UpdateLogSystemPartyType1Reda04100102(ISO20022MessageElement):
    od: Optional[SystemPartyType1ChoiceReda04100102] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    new: Optional[SystemPartyType1ChoiceReda04100102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class UpdateLogTechnicalAddress1Reda04100102(ISO20022MessageElement):
    od: Optional[TechnicalIdentification2ChoiceReda04100102] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    new: Optional[TechnicalIdentification2ChoiceReda04100102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Reda04100102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda04100102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class PostalAddress28Reda04100102(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceReda04100102] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )
    vld_fr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class Restriction1Reda04100102(ISO20022MessageElement):
    rstrctn_tp: Optional[CodeOrProprietary1ChoiceReda04100102] = field(
        default=None,
        metadata={
            "name": "RstrctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    vld_fr: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    vld_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldUntil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class UpdateLogContact2Reda04100102(ISO20022MessageElement):
    od: Optional[Contact14Reda04100102] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    new: Optional[Contact14Reda04100102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class UpdateLogPartyLockStatus1Reda04100102(ISO20022MessageElement):
    od: Optional[PartyLockStatus1Reda04100102] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    new: Optional[PartyLockStatus1Reda04100102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class PartyIdentification120ChoiceReda04100102(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Reda04100102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda04100102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class UpdateLogAddress2Reda04100102(ISO20022MessageElement):
    od: Optional[PostalAddress28Reda04100102] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    new: Optional[PostalAddress28Reda04100102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class UpdateLogRestriction1Reda04100102(ISO20022MessageElement):
    od: Optional[Restriction1Reda04100102] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    new: Optional[Restriction1Reda04100102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class PartyIdentification136Reda04100102(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceReda04100102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class UpdateLogPartyRecord2ChoiceReda04100102(ISO20022MessageElement):
    adr: Optional[UpdateLogAddress2Reda04100102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    ctct_dtls: Optional[UpdateLogContact2Reda04100102] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    opng_dt: Optional[UpdateLogDate1Reda04100102] = field(
        default=None,
        metadata={
            "name": "OpngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    clsg_dt: Optional[UpdateLogDate1Reda04100102] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    tp: Optional[UpdateLogSystemPartyType1Reda04100102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    tech_adr: Optional[UpdateLogTechnicalAddress1Reda04100102] = field(
        default=None,
        metadata={
            "name": "TechAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    mkt_spcfc_attr: Optional[UpdateLogMarketSpecificAttribute1Reda04100102] = field(
        default=None,
        metadata={
            "name": "MktSpcfcAttr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    nm: Optional[UpdateLogPartyName1Reda04100102] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    res_tp: Optional[UpdateLogResidenceType1Reda04100102] = field(
        default=None,
        metadata={
            "name": "ResTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    lck_sts: Optional[UpdateLogPartyLockStatus1Reda04100102] = field(
        default=None,
        metadata={
            "name": "LckSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    rstrctn: Optional[UpdateLogRestriction1Reda04100102] = field(
        default=None,
        metadata={
            "name": "Rstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    othr: list[UpdateLogProprietary1Reda04100102] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class SystemPartyIdentification8Reda04100102(ISO20022MessageElement):
    id: Optional[PartyIdentification136Reda04100102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    rspnsbl_pty_id: Optional[PartyIdentification136Reda04100102] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class PartyReferenceDataChange3Reda04100102(ISO20022MessageElement):
    pty_id: Optional[SystemPartyIdentification8Reda04100102] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    rcrd: list[UpdateLogPartyRecord2ChoiceReda04100102] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "min_occurs": 1,
        },
    )
    opr_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OprTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )


@dataclass
class PartyStatement3Reda04100102(ISO20022MessageElement):
    sys_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SysDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    chng: list[PartyReferenceDataChange3Reda04100102] = field(
        default_factory=list,
        metadata={
            "name": "Chng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class PartyActivityAdviceV02Reda04100102(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader1Reda04100102] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )
    pty_actvty: Optional[PartyStatement3Reda04100102] = field(
        default=None,
        metadata={
            "name": "PtyActvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02",
        },
    )


@dataclass
class Reda04100102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.041.001.02"

    pty_actvty_advc: Optional[PartyActivityAdviceV02Reda04100102] = field(
        default=None,
        metadata={
            "name": "PtyActvtyAdvc",
            "type": "Element",
            "required": True,
        },
    )
