from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    FormOfSecurity1Code,
    NamePrefix1Code,
)
from python_iso20022.seev.enums import (
    BeneficiaryCertificationType1Code,
    CorporateActionEventProcessingType1Code,
    CorporateActionEventType2Code,
    CorporateActionMandatoryVoluntary1Code,
    CorporateActionOptionType1Code,
    PersonIdentificationType3Code,
    SecuritiesBalanceType10Code,
)
from python_iso20022.seev.seev_012_001_01.enums import ElectionType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01"


@dataclass
class AccountIdentification2ChoiceSeev01200101(ISO20022MessageElement):
    csh_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountSeev01200101(ISO20022MessageElement):
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
class AlternateSecurityIdentification3Seev01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    dmst_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTimeChoiceSeev01200101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class DocumentIdentification8Seev01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class GenericIdentification1Seev01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Seev01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformationSeev01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class BeneficiaryCertificationType1FormatChoiceSeev01200101(ISO20022MessageElement):
    cd: Optional[BeneficiaryCertificationType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class CashAccountIdentification1ChoiceSeev01200101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[a-zA-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[0-9]{8,17}",
        },
    )
    dmst_acct: Optional[SimpleIdentificationInformationSeev01200101] = field(
        default=None,
        metadata={
            "name": "DmstAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class ContactIdentification4Seev01200101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class CorporateActionEventProcessingType1FormatChoiceSeev01200101(
    ISO20022MessageElement
):
    cd: Optional[CorporateActionEventProcessingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class CorporateActionEventType2FormatChoiceSeev01200101(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary1FormatChoiceSeev01200101(
    ISO20022MessageElement
):
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class CorporateActionOption1FormatChoiceSeev01200101(ISO20022MessageElement):
    cd: Optional[CorporateActionOptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class ElectionAdviceFunction1Seev01200101(ISO20022MessageElement):
    elctn_tp: Optional[ElectionType1Code] = field(
        default=None,
        metadata={
            "name": "ElctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    prvs_agt_caelctn_advc_id: Optional[DocumentIdentification8Seev01200101] = field(
        default=None,
        metadata={
            "name": "PrvsAgtCAElctnAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    agt_caelctn_sts_advc_id: Optional[DocumentIdentification8Seev01200101] = field(
        default=None,
        metadata={
            "name": "AgtCAElctnStsAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    agt_caelctn_amdmnt_req_id: Optional[DocumentIdentification8Seev01200101] = field(
        default=None,
        metadata={
            "name": "AgtCAElctnAmdmntReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class PersonIdentificationType3ChoiceSeev01200101(ISO20022MessageElement):
    cd: Optional[PersonIdentificationType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class PostalAddress1Seev01200101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SecuritiesBalanceType10FormatChoiceSeev01200101(ISO20022MessageElement):
    cd: Optional[SecuritiesBalanceType10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class SecurityIdentification7Seev01200101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: Optional[AlternateSecurityIdentification3Seev01200101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class UnitOrFaceAmount1ChoiceSeev01200101(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[ActiveCurrencyAndAmountSeev01200101] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class GenericIdentification16Seev01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[PersonIdentificationType3ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NameAndAddress5Seev01200101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev01200101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceSeev01200101(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Seev01200101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev01200101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class BeneficialOwner1Seev01200101(ISO20022MessageElement):
    bnfcl_ownr_id: Optional[PartyIdentification2ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    addtl_id: Optional[GenericIdentification16Seev01200101] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dmcl_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    non_dmcl_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonDmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    certfctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    certfctn_tp: Optional[BeneficiaryCertificationType1FormatChoiceSeev01200101] = (
        field(
            default=None,
            metadata={
                "name": "CertfctnTp",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            },
        )
    )
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    scty_id: Optional[SecurityIdentification7Seev01200101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    elctd_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "ElctdSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )


@dataclass
class CashAccount19Seev01200101(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    acct_id: Optional[AccountIdentification2ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )


@dataclass
class ContactPerson1Seev01200101(ISO20022MessageElement):
    ctct_prsn: Optional[ContactIdentification4Seev01200101] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    instn_id: Optional[PartyIdentification2ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "InstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class FinancialInstrumentDescription3Seev01200101(ISO20022MessageElement):
    scty_id: Optional[SecurityIdentification7Seev01200101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    plc_of_listg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    sfkpg_plc: Optional[PartyIdentification2ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class ProceedsDelivery1Seev01200101(ISO20022MessageElement):
    scties_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    csh_acct_id: Optional[CashAccountIdentification1ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    acct_svcr_id: Optional[PartyIdentification2ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "AcctSvcrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class SecuritiesAccount7Seev01200101(ISO20022MessageElement):
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount9Seev01200101(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    bal_tp: Optional[SecuritiesBalanceType10FormatChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "BalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    optn_tp: Optional[CorporateActionOption1FormatChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[0-9]{3}",
        },
    )
    scty_hldg_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctyHldgForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class CorporateActionAdditionalInformation1Seev01200101(ISO20022MessageElement):
    bnfcl_ownr_dtls: list[BeneficialOwner1Seev01200101] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    rcvr_id: Optional[PartyIdentification2ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "RcvrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    certfctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    certfctn_tp: Optional[BeneficiaryCertificationType1FormatChoiceSeev01200101] = (
        field(
            default=None,
            metadata={
                "name": "CertfctnTp",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            },
        )
    )
    dlvry_dtls: list[ProceedsDelivery1Seev01200101] = field(
        default_factory=list,
        metadata={
            "name": "DlvryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    addtl_instr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionCashMovements2Seev01200101(ISO20022MessageElement):
    pstng_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstngId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstng_dt_tm: Optional[DateAndDateTimeChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "PstngDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    pstng_amt: Optional[ActiveCurrencyAndAmountSeev01200101] = field(
        default=None,
        metadata={
            "name": "PstngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    acct_dtls: list[CashAccount19Seev01200101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class CorporateActionInformation1Seev01200101(ISO20022MessageElement):
    agt_id: Optional[PartyIdentification2ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "AgtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    issr_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnPrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType2FormatChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary1FormatChoiceSeev01200101
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    evt_prcg_tp: Optional[
        CorporateActionEventProcessingType1FormatChoiceSeev01200101
    ] = field(
        default=None,
        metadata={
            "name": "EvtPrcgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentDescription3Seev01200101] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )


@dataclass
class CorporateActionSecuritiesMovement2Seev01200101(ISO20022MessageElement):
    scty_id: Optional[SecurityIdentification7Seev01200101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    pstng_dt_tm: Optional[DateAndDateTimeChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "PstngDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    pstng_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstngId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstng_qty: Optional[UnitOrFaceAmount1ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "PstngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    acct_dtls: list[SecuritiesAccount9Seev01200101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class CorporateActionElection3Seev01200101(ISO20022MessageElement):
    acct_dtls: Optional[SecuritiesAccount7Seev01200101] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    optn_tp: Optional[CorporateActionOption1FormatChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "pattern": r"[0-9]{3}",
        },
    )
    instd_undrlyg_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "InstdUndrlygSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    instd_scties_qty_to_rcv: Optional[UnitOrFaceAmount1ChoiceSeev01200101] = field(
        default=None,
        metadata={
            "name": "InstdSctiesQtyToRcv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    propsd_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PropsdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    csh_mvmnt_dtls: list[CorporateActionCashMovements2Seev01200101] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    scties_mvmnt_dtls: list[CorporateActionSecuritiesMovement2Seev01200101] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class AgentCaelectionAdviceV01Seev01200101(ISO20022MessageElement):
    class Meta:
        name = "AgentCAElectionAdviceV01"

    id: Optional[DocumentIdentification8Seev01200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    elctn_advc_tp_and_lkg: Optional[ElectionAdviceFunction1Seev01200101] = field(
        default=None,
        metadata={
            "name": "ElctnAdvcTpAndLkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionInformation1Seev01200101] = field(
        default=None,
        metadata={
            "name": "CorpActnGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    elctn_dtls: Optional[CorporateActionElection3Seev01200101] = field(
        default=None,
        metadata={
            "name": "ElctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
            "required": True,
        },
    )
    addtl_inf: Optional[CorporateActionAdditionalInformation1Seev01200101] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )
    ctct_dtls: Optional[ContactPerson1Seev01200101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01",
        },
    )


@dataclass
class Seev01200101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01"

    agt_caelctn_advc: Optional[AgentCaelectionAdviceV01Seev01200101] = field(
        default=None,
        metadata={
            "name": "AgtCAElctnAdvc",
            "type": "Element",
            "required": True,
        },
    )
