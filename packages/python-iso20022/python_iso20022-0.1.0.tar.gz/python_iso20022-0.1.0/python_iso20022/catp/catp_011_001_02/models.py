from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.catp.enums import (
    ActionType6Code,
    Atmdevice1Code,
    AtmserviceType5Code,
    OutputFormat2Code,
)
from python_iso20022.enums import (
    Algorithm7Code,
    Algorithm8Code,
    Algorithm11Code,
    Algorithm12Code,
    Algorithm13Code,
    Algorithm15Code,
    Atmcommand4Code,
    Atmstatus1Code,
    AttributeType1Code,
    AuthenticationEntity2Code,
    AuthenticationMethod7Code,
    BytePadding1Code,
    ContentType2Code,
    DataSetCategory7Code,
    EncryptionFormat1Code,
    MessageFunction8Code,
    MessageFunction11Code,
    PartyType12Code,
    Response4Code,
    ResultDetail4Code,
    TmscontactLevel2Code,
    TransactionEnvironment3Code,
    Verification1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02"


@dataclass
class AtmcommandIdentification1Catp01100102:
    class Meta:
        name = "ATMCommandIdentification1"

    orgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Orgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AtmcustomerProfile2Catp01100102:
    class Meta:
        name = "ATMCustomerProfile2"

    prfl_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrflRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Acquirer7Catp01100102:
    acqrg_instn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Acquirer8Catp01100102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicCoordinates1Catp01100102:
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    long: Optional[str] = field(
        default=None,
        metadata={
            "name": "Long",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class Kekidentifier2Catp01100102:
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class PlainCardData19Catp01100102:
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "pattern": r"[0-9]{8,28}",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 10,
        },
    )
    xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 10,
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 37,
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 104,
        },
    )


@dataclass
class TransactionIdentifier1Catp01100102:
    tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    tx_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Utmcoordinates1Catp01100102:
    class Meta:
        name = "UTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    utmestwrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UTMEstwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    utmnrthwrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UTMNrthwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AtmconfigurationParameter1Catp01100102:
    class Meta:
        name = "ATMConfigurationParameter1"

    tp: Optional[DataSetCategory7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmmessageFunction2Catp01100102:
    class Meta:
        name = "ATMMessageFunction2"

    fctn: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Atmservice21Catp01100102:
    class Meta:
        name = "ATMService21"

    svc_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc_tp: Optional[AtmserviceType5Code] = field(
        default=None,
        metadata={
            "name": "SvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    svc_varnt_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SvcVarntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActionMessage4Catp01100102:
    frmt: Optional[OutputFormat2Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    msg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Msg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 20000,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dvc: Optional[Atmdevice1Code] = field(
        default=None,
        metadata={
            "name": "Dvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    msg_cntt_sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MsgCnttSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class EncapsulatedContent3Catp01100102:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification77Catp01100102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    issr: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicLocation1ChoiceCatp01100102:
    geogc_cordints: Optional[GeographicCoordinates1Catp01100102] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    utmcordints: Optional[Utmcoordinates1Catp01100102] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class Parameter5Catp01100102:
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class Parameter6Catp01100102:
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class Parameter7Catp01100102:
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class RelativeDistinguishedName1Catp01100102:
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ResponseType7Catp01100102:
    rspn: Optional[Response4Code] = field(
        default=None,
        metadata={
            "name": "Rspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    rspn_rsn: Optional[ResultDetail4Code] = field(
        default=None,
        metadata={
            "name": "RspnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    addtl_rspn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRspnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TerminalHosting1Catp01100102:
    ctgy: Optional[TransactionEnvironment3Code] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionVerificationResult5Catp01100102:
    mtd: Optional[AuthenticationMethod7Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    vrfctn_ntty: Optional[AuthenticationEntity2Code] = field(
        default=None,
        metadata={
            "name": "VrfctnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    rslt: Optional[Verification1Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    addtl_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )
    authntcn_tkn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class AtmcommandParameters1ChoiceCatp01100102:
    class Meta:
        name = "ATMCommandParameters1Choice"

    atmreqrd_gbl_sts: Optional[Atmstatus1Code] = field(
        default=None,
        metadata={
            "name": "ATMReqrdGblSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    xpctd_msg_fctn: Optional[MessageFunction8Code] = field(
        default=None,
        metadata={
            "name": "XpctdMsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    reqrd_cfgtn_param: Optional[AtmconfigurationParameter1Catp01100102] = field(
        default=None,
        metadata={
            "name": "ReqrdCfgtnParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class Atmcontext17Catp01100102:
    class Meta:
        name = "ATMContext17"

    ssn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SsnRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc: Optional[Atmservice21Catp01100102] = field(
        default=None,
        metadata={
            "name": "Svc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )


@dataclass
class Atmcustomer5Catp01100102:
    class Meta:
        name = "ATMCustomer5"

    prfl: Optional[AtmcustomerProfile2Catp01100102] = field(
        default=None,
        metadata={
            "name": "Prfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    authntcn_rslt: list[TransactionVerificationResult5Catp01100102] = field(
        default_factory=list,
        metadata={
            "name": "AuthntcnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class Action7Catp01100102:
    actn_tp: Optional[ActionType6Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    msg_to_pres: Optional[ActionMessage4Catp01100102] = field(
        default=None,
        metadata={
            "name": "MsgToPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    req_to_prfrm: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "ReqToPrfrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class AlgorithmIdentification12Catp01100102:
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter5Catp01100102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class AlgorithmIdentification13Catp01100102:
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter6Catp01100102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class AlgorithmIdentification14Catp01100102:
    algo: Optional[Algorithm15Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter6Catp01100102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class AlgorithmIdentification15Catp01100102:
    algo: Optional[Algorithm12Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter7Catp01100102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class CertificateIssuer1Catp01100102:
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Catp01100102] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class PostalAddress17Catp01100102:
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    glctn: Optional[GeographicLocation1ChoiceCatp01100102] = field(
        default=None,
        metadata={
            "name": "GLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class Traceability4Catp01100102:
    rlay_id: Optional[GenericIdentification77Catp01100102] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )


@dataclass
class Atmcommand7Catp01100102:
    class Meta:
        name = "ATMCommand7"

    tp: Optional[Atmcommand4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    urgcy: Optional[TmscontactLevel2Code] = field(
        default=None,
        metadata={
            "name": "Urgcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    cmd_id: Optional[AtmcommandIdentification1Catp01100102] = field(
        default=None,
        metadata={
            "name": "CmdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    cmd_params: Optional[AtmcommandParameters1ChoiceCatp01100102] = field(
        default=None,
        metadata={
            "name": "CmdParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class AutomatedTellerMachine2Catp01100102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    lctn: Optional[PostalAddress17Catp01100102] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class EncryptedContent3Catp01100102:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification14Catp01100102] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class Header31Catp01100102:
    msg_fctn: Optional[AtmmessageFunction2Catp01100102] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 6,
        },
    )
    xchg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    initg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prc_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tracblt: list[Traceability4Catp01100102] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class IssuerAndSerialNumber1Catp01100102:
    issr: Optional[CertificateIssuer1Catp01100102] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek4Catp01100102:
    class Meta:
        name = "KEK4"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier2Catp01100102] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification13Catp01100102] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter4Catp01100102:
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Catp01100102] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class Atmtransaction22Catp01100102:
    class Meta:
        name = "ATMTransaction22"

    tx_id: Optional[TransactionIdentifier1Catp01100102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmpltn_reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CmpltnReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    tx_rspn: Optional[ResponseType7Catp01100102] = field(
        default=None,
        metadata={
            "name": "TxRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    actn: list[Action7Catp01100102] = field(
        default_factory=list,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    iccrltd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )
    cmd: list[Atmcommand7Catp01100102] = field(
        default_factory=list,
        metadata={
            "name": "Cmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class AlgorithmIdentification11Catp01100102:
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter4Catp01100102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class Recipient5ChoiceCatp01100102:
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Catp01100102] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    key_idr: Optional[Kekidentifier2Catp01100102] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class KeyTransport4Catp01100102:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCatp01100102] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification11Catp01100102] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient4ChoiceCatp01100102:
    key_trnsprt: Optional[KeyTransport4Catp01100102] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    kek: Optional[Kek4Catp01100102] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    key_idr: Optional[Kekidentifier2Catp01100102] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class AuthenticatedData4Catp01100102:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCatp01100102] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification15Catp01100102] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catp01100102] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData4Catp01100102:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCatp01100102] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent3Catp01100102] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class ContentInformationType10Catp01100102:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData4Catp01100102] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )


@dataclass
class ContentInformationType15Catp01100102:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData4Catp01100102] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )


@dataclass
class Atmenvironment12Catp01100102:
    class Meta:
        name = "ATMEnvironment12"

    acqrr: Optional[Acquirer7Catp01100102] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    atmmgr: Optional[Acquirer8Catp01100102] = field(
        default=None,
        metadata={
            "name": "ATMMgr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    hstg_ntty: Optional[TerminalHosting1Catp01100102] = field(
        default=None,
        metadata={
            "name": "HstgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    atm: Optional[AutomatedTellerMachine2Catp01100102] = field(
        default=None,
        metadata={
            "name": "ATM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    cstmr: Optional[Atmcustomer5Catp01100102] = field(
        default=None,
        metadata={
            "name": "Cstmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    prtctd_card_data: Optional[ContentInformationType10Catp01100102] = field(
        default=None,
        metadata={
            "name": "PrtctdCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    plain_card_data: Optional[PlainCardData19Catp01100102] = field(
        default=None,
        metadata={
            "name": "PlainCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class AtmpinmanagementResponse2Catp01100102:
    class Meta:
        name = "ATMPINManagementResponse2"

    envt: Optional[Atmenvironment12Catp01100102] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    cntxt: Optional[Atmcontext17Catp01100102] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    tx: Optional[Atmtransaction22Catp01100102] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )


@dataclass
class AtmpinmanagementResponseV02Catp01100102:
    class Meta:
        name = "ATMPINManagementResponseV02"

    hdr: Optional[Header31Catp01100102] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
            "required": True,
        },
    )
    prtctd_atmpinmgmt_rspn: Optional[ContentInformationType10Catp01100102] = field(
        default=None,
        metadata={
            "name": "PrtctdATMPINMgmtRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    atmpinmgmt_rspn: Optional[AtmpinmanagementResponse2Catp01100102] = field(
        default=None,
        metadata={
            "name": "ATMPINMgmtRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )
    scty_trlr: Optional[ContentInformationType15Catp01100102] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02",
        },
    )


@dataclass
class Catp01100102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:catp.011.001.02"

    atmpinmgmt_rspn: Optional[AtmpinmanagementResponseV02Catp01100102] = field(
        default=None,
        metadata={
            "name": "ATMPINMgmtRspn",
            "type": "Element",
            "required": True,
        },
    )
