from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.reda.enums import Status6Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01"


@dataclass
class AccountSchemeName1ChoiceReda05100101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashAccountType2ChoiceReda05100101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTime2ChoiceReda05100101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )


@dataclass
class GenericIdentification30Reda05100101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessInstruction1Reda05100101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )


@dataclass
class ProxyAccountType1ChoiceReda05100101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class StatusReason6ChoiceReda05100101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda05100101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class BlockChainAddressWallet3Reda05100101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Reda05100101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class GenericAccountIdentification1Reda05100101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceReda05100101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader12Reda05100101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )
    orgnl_biz_instr: Optional[OriginalBusinessInstruction1Reda05100101] = field(
        default=None,
        metadata={
            "name": "OrgnlBizInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )


@dataclass
class ProxyAccountIdentification1Reda05100101(ISO20022MessageElement):
    tp: Optional[ProxyAccountType1ChoiceReda05100101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class SecuritiesAccount19Reda05100101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Reda05100101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class StatusReasonInformation10Reda05100101(ISO20022MessageElement):
    rsn: Optional[StatusReason6ChoiceReda05100101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SupplementaryData1Reda05100101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda05100101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
        },
    )


@dataclass
class AccountIdentification4ChoiceReda05100101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Reda05100101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )


@dataclass
class AccountLinkStatus1Reda05100101(ISO20022MessageElement):
    sts: Optional[Status6Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
        },
    )
    sts_rsn: list[StatusReasonInformation10Reda05100101] = field(
        default_factory=list,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )


@dataclass
class CashAccount38Reda05100101(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceReda05100101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2ChoiceReda05100101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Reda05100101] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )


@dataclass
class AccountLink8Reda05100101(ISO20022MessageElement):
    scties_acct: Optional[SecuritiesAccount19Reda05100101] = field(
        default=None,
        metadata={
            "name": "SctiesAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Reda05100101] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )
    csh_acct: Optional[CashAccount38Reda05100101] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
        },
    )
    vld_fr: Optional[DateAndDateTime2ChoiceReda05100101] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
        },
    )


@dataclass
class AccountLinkStatusAdviceV01Reda05100101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader12Reda05100101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )
    acct_lk_sts: Optional[AccountLinkStatus1Reda05100101] = field(
        default=None,
        metadata={
            "name": "AcctLkSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
            "required": True,
        },
    )
    acct_lk_id: Optional[AccountLink8Reda05100101] = field(
        default=None,
        metadata={
            "name": "AcctLkId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Reda05100101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01",
        },
    )


@dataclass
class Reda05100101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01"

    acct_lk_sts_advc: Optional[AccountLinkStatusAdviceV01Reda05100101] = field(
        default=None,
        metadata={
            "name": "AcctLkStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
