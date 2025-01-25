from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code, DateType1Code
from python_iso20022.seev.seev_046_001_01.enums import (
    DisclosureRequestCancellationReason1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01"


@dataclass
class DateAndDateTime2ChoiceSeev04600101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )


@dataclass
class GenericIdentification30Seev04600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev04600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev04600101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev04600101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class DateCode20ChoiceSeev04600101(ISO20022MessageElement):
    cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Seev04600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )


@dataclass
class OtherIdentification1Seev04600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev04600101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Seev04600101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryData1Seev04600101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev04600101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "required": True,
        },
    )


@dataclass
class DateFormat46ChoiceSeev04600101(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev04600101] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )
    dt_cd: Optional[DateCode20ChoiceSeev04600101] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )


@dataclass
class NameAndAddress5Seev04600101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev04600101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )


@dataclass
class SecurityIdentification19Seev04600101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev04600101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DisclosureRequestIdentification1Seev04600101(ISO20022MessageElement):
    issr_dsclsr_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrDsclsrReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev04600101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "required": True,
        },
    )
    shrhldrs_dsclsr_rcrd_dt: Optional[DateFormat46ChoiceSeev04600101] = field(
        default=None,
        metadata={
            "name": "ShrhldrsDsclsrRcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "required": True,
        },
    )


@dataclass
class PartyIdentification129ChoiceSeev04600101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev04600101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev04600101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class ShareholdersIdentificationDisclosureRequestCancellationAdviceV01Seev04600101(
    ISO20022MessageElement
):
    issr_dsclsr_req_ref: Optional[DisclosureRequestIdentification1Seev04600101] = field(
        default=None,
        metadata={
            "name": "IssrDsclsrReqRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
            "required": True,
        },
    )
    cxl_rsn: Optional[DisclosureRequestCancellationReason1Code] = field(
        default=None,
        metadata={
            "name": "CxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )
    issr: Optional[PartyIdentification129ChoiceSeev04600101] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Seev04600101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01",
        },
    )


@dataclass
class Seev04600101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.046.001.01"

    shrhldrs_id_dsclsr_req_cxl_advc: Optional[
        ShareholdersIdentificationDisclosureRequestCancellationAdviceV01Seev04600101
    ] = field(
        default=None,
        metadata={
            "name": "ShrhldrsIdDsclsrReqCxlAdvc",
            "type": "Element",
            "required": True,
        },
    )
