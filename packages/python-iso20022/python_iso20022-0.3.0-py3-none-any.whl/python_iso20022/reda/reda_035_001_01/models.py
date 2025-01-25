from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01"


@dataclass
class GenericIdentification30Reda03500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Reda03500101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
        },
    )


@dataclass
class Pagination1Reda03500101(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda03500101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SecuritiesAccount19Reda03500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Reda03500101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Reda03500101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda03500101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesAccountReferenceDataChange2Reda03500101(ISO20022MessageElement):
    scties_acct_id: Optional[SecuritiesAccount19Reda03500101] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "required": True,
        },
    )
    fld_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FldNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    opr_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OprTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesAccountStatement2Reda03500101(ISO20022MessageElement):
    sys_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SysDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "required": True,
        },
    )
    chng: list[SecuritiesAccountReferenceDataChange2Reda03500101] = field(
        default_factory=list,
        metadata={
            "name": "Chng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
        },
    )


@dataclass
class SecuritiesAccountActivityAdviceV01Reda03500101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader1Reda03500101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
        },
    )
    pgntn: Optional[Pagination1Reda03500101] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "required": True,
        },
    )
    scties_acct_actvty: Optional[SecuritiesAccountStatement2Reda03500101] = field(
        default=None,
        metadata={
            "name": "SctiesAcctActvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda03500101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01",
        },
    )


@dataclass
class Reda03500101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.035.001.01"

    scties_acct_actvty_advc: Optional[
        SecuritiesAccountActivityAdviceV01Reda03500101
    ] = field(
        default=None,
        metadata={
            "name": "SctiesAcctActvtyAdvc",
            "type": "Element",
            "required": True,
        },
    )
