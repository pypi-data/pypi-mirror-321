from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    Algorithm5Code,
    Algorithm7Code,
    Algorithm8Code,
    Algorithm13Code,
    Algorithm20Code,
    Algorithm23Code,
    AttributeType1Code,
    BytePadding1Code,
    ContentType2Code,
    ContentType3Code,
    CreditDebit3Code,
    EncryptedDataFormat1Code,
    EncryptionFormat3Code,
    LifeCycleSupport1Code,
    MessageClass1Code,
    MessageError1Code,
    MessageFunction16Code,
    PartyType9Code,
    PartyType17Code,
    PartyType18Code,
    PartyType26Code,
    PartyType32Code,
    ProtectionMethod1Code,
    PurchaseIdentifierType2Code,
    StorageLocation1Code,
    TypeOfAmount21Code,
    TypeOfAmount22Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03"


@dataclass
class AdditionalData1Cain02600103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class BatchManagementInformation1Cain02600103(ISO20022MessageElement):
    colltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    btch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BtchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,15}",
        },
    )
    msg_chcksm_inpt_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MsgChcksmInptVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class CardData14Cain02600103(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,19}",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{2,3}",
        },
    )
    pmt_acct_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtAcctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtfl_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtflIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateTime2Cain02600103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class EncryptedData2ChoiceCain02600103(ISO20022MessageElement):
    binry: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Binry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )
    hex_binry: Optional[str] = field(
        default=None,
        metadata={
            "name": "HexBinry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,9999}",
        },
    )


@dataclass
class Jurisdiction2Cain02600103(ISO20022MessageElement):
    dmst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    dmst_qlfctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier2Cain02600103(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    key_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Kekidentifier6Cain02600103(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier6"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    key_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Macdata1Cain02600103(ISO20022MessageElement):
    class Meta:
        name = "MACData1"

    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    initlstn_vctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )


@dataclass
class Reconciliation4Cain02600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    chckpt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Cain02600103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AdditionalData2Cain02600103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtls: list[AdditionalData1Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class AdditionalFee3Cain02600103(ISO20022MessageElement):
    tp: Optional[TypeOfAmount21Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prgm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prgm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dscrptr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dscrptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
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
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rcncltn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    assgnr: Optional[PartyType32Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    othr_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AlgorithmIdentification26Cain02600103(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    param: Optional[Algorithm5Code] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class ContentInformationType41Cain02600103(ISO20022MessageElement):
    macdata: Optional[Macdata1Cain02600103] = field(
        default=None,
        metadata={
            "name": "MACData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    mac: Optional[str] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1,8}",
        },
    )


@dataclass
class EncryptedDataElement2Cain02600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data: Optional[EncryptedData2ChoiceCain02600103] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    clear_txt_frmt: Optional[EncryptedDataFormat1Code] = field(
        default=None,
        metadata={
            "name": "ClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    othr_clear_txt_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ErrorDetails3Cain02600103(ISO20022MessageElement):
    tp: Optional[MessageError1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 500,
        },
    )
    data_elmt_in_err: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DataElmtInErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 4000,
        },
    )


@dataclass
class GenericIdentification183Cain02600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType17Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LocalData14Cain02600103(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 210,
        },
    )
    addtl_data: list[AdditionalData1Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class OriginalTransactionAmounts3Cain02600103(ISO20022MessageElement):
    amt_qlfr: Optional[TypeOfAmount22Code] = field(
        default=None,
        metadata={
            "name": "AmtQlfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
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
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    crdhldr_bllg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    crdhldr_bllg_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrdhldrBllgFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rcncltn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )


@dataclass
class OriginalTransactionIdentification1Cain02600103(ISO20022MessageElement):
    lcl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LclDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    lcl_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LclTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    tm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    purchs_idr_tp: Optional[PurchaseIdentifierType2Code] = field(
        default=None,
        metadata={
            "name": "PurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    othr_purchs_idr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,12}",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "length": 12,
        },
    )
    life_cycl_spprt: Optional[LifeCycleSupport1Code] = field(
        default=None,
        metadata={
            "name": "LifeCyclSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "length": 15,
        },
    )
    authstn_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    authntcn_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    life_cycl_id_mssng: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclIdMssng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acqrr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acqrr_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,23}",
        },
    )
    issr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class Parameter14Cain02600103(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat3Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )
    bpddg: Optional[BytePadding1Code] = field(
        default=None,
        metadata={
            "name": "BPddg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class Parameter7Cain02600103(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )
    bpddg: Optional[BytePadding1Code] = field(
        default=None,
        metadata={
            "name": "BPddg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class ProgrammeMode5Cain02600103(ISO20022MessageElement):
    apld_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApldId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[AdditionalData1Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class RelativeDistinguishedName1Cain02600103(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementService6Cain02600103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cut_off_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    rptg_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalData1Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class SupplementaryData1Cain02600103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Cain02600103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )


@dataclass
class Token2Cain02600103(ISO20022MessageElement):
    pmt_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,19}",
        },
    )
    tkn_xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "TknXpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    tkn_rqstr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknRqstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,11}",
        },
    )
    tkn_assrnc_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    tkn_assrnc_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TknAssrncMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    tkn_inittd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TknInittdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    storg_lctn: Optional[StorageLocation1Code] = field(
        default=None,
        metadata={
            "name": "StorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    othr_storg_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrStorgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtcn_mtd: Optional[ProtectionMethod1Code] = field(
        default=None,
        metadata={
            "name": "PrtcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    othr_prtcn_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPrtcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_data: list[AdditionalData1Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class Traceability10Cain02600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType17Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class TransactionIdentification53Cain02600103(ISO20022MessageElement):
    purchs_idr_tp: Optional[PurchaseIdentifierType2Code] = field(
        default=None,
        metadata={
            "name": "PurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    othr_purchs_idr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPurchsIdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchsIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "pattern": r"[0-9]{1,12}",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "length": 12,
        },
    )
    life_cycl_spprt: Optional[LifeCycleSupport1Code] = field(
        default=None,
        metadata={
            "name": "LifeCyclSpprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "length": 15,
        },
    )
    authstn_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    presntmnt_seq_cnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "PresntmntSeqCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{2}",
        },
    )
    authntcn_tkn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acqrr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acqrr_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,23}",
        },
    )
    issr_ref_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrRefData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    assoctd_data_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssoctdDataRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AlgorithmIdentification25Cain02600103(ISO20022MessageElement):
    algo: Optional[Algorithm23Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter7Cain02600103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class AlgorithmIdentification28Cain02600103(ISO20022MessageElement):
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter14Cain02600103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class CertificateIssuer1Cain02600103(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class EncryptedData2Cain02600103(ISO20022MessageElement):
    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcrptdFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_elmt: list[EncryptedDataElement2Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class Header71Cain02600103(ISO20022MessageElement):
    msg_fctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )
    xchg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    re_trnsmssn_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReTrnsmssnCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    btch_mgmt_inf: Optional[BatchManagementInformation1Cain02600103] = field(
        default=None,
        metadata={
            "name": "BtchMgmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    initg_pty: Optional[GenericIdentification183Cain02600103] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification183Cain02600103] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    trac_data: list[AdditionalData1Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "TracData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    tracblt: list[Traceability10Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class OriginalDataElements3Cain02600103(ISO20022MessageElement):
    msg_clss: Optional[MessageClass1Code] = field(
        default=None,
        metadata={
            "name": "MsgClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    msg_fctn: Optional[MessageFunction16Code] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    acqrr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,11}",
        },
    )
    sndr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SndrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{1,11}",
        },
    )
    tx_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    tx_id: Optional[OriginalTransactionIdentification1Cain02600103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    convs_dt_tm: Optional[DateTime2Cain02600103] = field(
        default=None,
        metadata={
            "name": "ConvsDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    tx_amts: Optional[OriginalTransactionAmounts3Cain02600103] = field(
        default=None,
        metadata={
            "name": "TxAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    addtl_fee: list[AdditionalFee3Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    apprvl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[a-zA-Z0-9\s]{6}",
        },
    )


@dataclass
class Parameter13Cain02600103(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm20Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification26Cain02600103] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class PartyIdentification285Cain02600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    lcl_data: list[LocalData14Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class PartyIdentification286Cain02600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "pattern": r"[0-9]{1,11}",
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    lcl_data: Optional[LocalData14Cain02600103] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class ProcessingResult23Cain02600103(ISO20022MessageElement):
    rspn_src_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_tp: Optional[PartyType26Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    rspn_src_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_assgnr: Optional[PartyType9Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    rspn_src_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    rspn_src_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    err_dtl: list[ErrorDetails3Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "ErrDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    addtl_inf: list[AdditionalData1Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class AlgorithmIdentification27Cain02600103(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter13Cain02600103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class EncryptedContent8Cain02600103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification25Cain02600103] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    ncrptd_data_elmt: list[EncryptedDataElement2Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdDataElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class IssuerAndSerialNumber1Cain02600103(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Cain02600103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek6Cain02600103(ISO20022MessageElement):
    class Meta:
        name = "KEK6"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier6Cain02600103] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification28Cain02600103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Recipient5ChoiceCain02600103(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Cain02600103] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Cain02600103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class KeyTransport6Cain02600103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCain02600103] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification27Cain02600103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient7ChoiceCain02600103(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport6Cain02600103] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    kek: Optional[Kek6Cain02600103] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    key_idr: Optional[Kekidentifier6Cain02600103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class EnvelopedData12Cain02600103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient7ChoiceCain02600103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent8Cain02600103] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class ProtectedData2Cain02600103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType3Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData12Cain02600103] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    ncrptd_data: Optional[EncryptedData2Cain02600103] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class AddendumResponseV03Cain02600103(ISO20022MessageElement):
    hdr: Optional[Header71Cain02600103] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    tx_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    orgtr: Optional[PartyIdentification286Cain02600103] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    acqrr: Optional[PartyIdentification286Cain02600103] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    sndr: Optional[PartyIdentification286Cain02600103] = field(
        default=None,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    card: Optional[CardData14Cain02600103] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    rcvr: Optional[PartyIdentification286Cain02600103] = field(
        default=None,
        metadata={
            "name": "Rcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    issr: Optional[PartyIdentification286Cain02600103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    dstn: Optional[PartyIdentification286Cain02600103] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    prgrmm: list[ProgrammeMode5Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "Prgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    tx_id: Optional[TransactionIdentification53Cain02600103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    orgnl_data_elmts: Optional[OriginalDataElements3Cain02600103] = field(
        default=None,
        metadata={
            "name": "OrgnlDataElmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    tkn: Optional[Token2Cain02600103] = field(
        default=None,
        metadata={
            "name": "Tkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    accptr: Optional[PartyIdentification285Cain02600103] = field(
        default=None,
        metadata={
            "name": "Accptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    jursdctn: Optional[Jurisdiction2Cain02600103] = field(
        default=None,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    sttlm_svc: Optional[SettlementService6Cain02600103] = field(
        default=None,
        metadata={
            "name": "SttlmSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    addtl_fee: list[AdditionalFee3Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    rcncltn: Optional[Reconciliation4Cain02600103] = field(
        default=None,
        metadata={
            "name": "Rcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    prcg_rslt: Optional[ProcessingResult23Cain02600103] = field(
        default=None,
        metadata={
            "name": "PrcgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
            "required": True,
        },
    )
    addtl_data: list[AdditionalData2Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    prtctd_data: list[ProtectedData2Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "PrtctdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Cain02600103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )
    scty_trlr: Optional[ContentInformationType41Cain02600103] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
        },
    )


@dataclass
class Cain02600103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03"

    adddm_rspn: Optional[AddendumResponseV03Cain02600103] = field(
        default=None,
        metadata={
            "name": "AdddmRspn",
            "type": "Element",
            "required": True,
        },
    )
