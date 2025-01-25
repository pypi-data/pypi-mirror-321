from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.catp.enums import (
    ActionType6Code,
    Atmdevice1Code,
    AtmserviceType6Code,
    OutputFormat2Code,
    PartyType16Code,
)
from python_iso20022.enums import (
    AccountChoiceMethod1Code,
    AddressType2Code,
    Algorithm7Code,
    Algorithm8Code,
    Algorithm11Code,
    Algorithm12Code,
    Algorithm13Code,
    Algorithm15Code,
    Atmcommand4Code,
    AtmmediaType2Code,
    Atmstatus1Code,
    AttributeType1Code,
    AuthenticationEntity2Code,
    AuthenticationMethod7Code,
    BytePadding1Code,
    CardAccountType3Code,
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

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01"


@dataclass
class AtmcommandIdentification1Catp01300101:
    class Meta:
        name = "ATMCommandIdentification1"

    orgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Orgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AtmcustomerProfile2Catp01300101:
    class Meta:
        name = "ATMCustomerProfile2"

    prfl_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrflRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmtransactionAmounts7Catp01300101:
    class Meta:
        name = "ATMTransactionAmounts7"

    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Labl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Acquirer7Catp01300101:
    acqrg_instn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Acquirer8Catp01300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndCurrency1Catp01300101:
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class CurrencyAndAmountCatp01300101:
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
class DetailedAmount13Catp01300101:
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Labl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class GenericIdentification1Catp01300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicCoordinates1Catp01300101:
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class Kekidentifier2Catp01300101:
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class PlainCardData19Catp01300101:
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[0-9]{8,28}",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 10,
        },
    )
    xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 10,
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 37,
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 104,
        },
    )


@dataclass
class ResponseType8Catp01300101:
    rspndr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspndrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdfctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cdfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_rspn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRspnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformation4Catp01300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionIdentifier1Catp01300101:
    tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    tx_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Utmcoordinates1Catp01300101:
    class Meta:
        name = "UTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AtmconfigurationParameter1Catp01300101:
    class Meta:
        name = "ATMConfigurationParameter1"

    tp: Optional[DataSetCategory7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmmessageFunction2Catp01300101:
    class Meta:
        name = "ATMMessageFunction2"

    fctn: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Atmservice12Catp01300101:
    class Meta:
        name = "ATMService12"

    svc_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc_tp: Optional[AtmserviceType6Code] = field(
        default=None,
        metadata={
            "name": "SvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    svc_varnt_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SvcVarntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    csh_bck: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CshBck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    multi_acct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MultiAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AtmtransactionAmounts9Catp01300101:
    class Meta:
        name = "ATMTransactionAmounts9"

    mdia_tp: Optional[AtmmediaType2Code] = field(
        default=None,
        metadata={
            "name": "MdiaTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    min_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    disp_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DispFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AccountIdentification31ChoiceCatp01300101:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[a-zA-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[0-9]{8,17}",
        },
    )
    dmst_acct: Optional[SimpleIdentificationInformation4Catp01300101] = field(
        default=None,
        metadata={
            "name": "DmstAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class ActionMessage4Catp01300101:
    frmt: Optional[OutputFormat2Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    msg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Msg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 20000,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dvc: Optional[Atmdevice1Code] = field(
        default=None,
        metadata={
            "name": "Dvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    msg_cntt_sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MsgCnttSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class AmountAndDirection43Catp01300101:
    amt: Optional[CurrencyAndAmountCatp01300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class DetailedAmount16Catp01300101:
    acct_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AcctSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    amt_to_dpst: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtToDpst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    csh_bck_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CshBckAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    fees: list[DetailedAmount13Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "Fees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    dontn: list[DetailedAmount13Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "Dontn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class EncapsulatedContent3Catp01300101:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification77Catp01300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    issr: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicLocation1ChoiceCatp01300101:
    geogc_cordints: Optional[GeographicCoordinates1Catp01300101] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    utmcordints: Optional[Utmcoordinates1Catp01300101] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class Parameter5Catp01300101:
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class Parameter6Catp01300101:
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class Parameter7Catp01300101:
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class PartyIdentification72ChoiceCatp01300101:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Catp01300101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class PostalAddress1Catp01300101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class RelativeDistinguishedName1Catp01300101:
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ResponseType7Catp01300101:
    rspn: Optional[Response4Code] = field(
        default=None,
        metadata={
            "name": "Rspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    rspn_rsn: Optional[ResultDetail4Code] = field(
        default=None,
        metadata={
            "name": "RspnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    addtl_rspn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRspnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TerminalHosting1Catp01300101:
    ctgy: Optional[TransactionEnvironment3Code] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionVerificationResult5Catp01300101:
    mtd: Optional[AuthenticationMethod7Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    vrfctn_ntty: Optional[AuthenticationEntity2Code] = field(
        default=None,
        metadata={
            "name": "VrfctnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    rslt: Optional[Verification1Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    addtl_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 500,
        },
    )
    authntcn_tkn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class AtmcommandParameters1ChoiceCatp01300101:
    class Meta:
        name = "ATMCommandParameters1Choice"

    atmreqrd_gbl_sts: Optional[Atmstatus1Code] = field(
        default=None,
        metadata={
            "name": "ATMReqrdGblSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    xpctd_msg_fctn: Optional[MessageFunction8Code] = field(
        default=None,
        metadata={
            "name": "XpctdMsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    reqrd_cfgtn_param: Optional[AtmconfigurationParameter1Catp01300101] = field(
        default=None,
        metadata={
            "name": "ReqrdCfgtnParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class Atmcontext11Catp01300101:
    class Meta:
        name = "ATMContext11"

    ssn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SsnRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc: Optional[Atmservice12Catp01300101] = field(
        default=None,
        metadata={
            "name": "Svc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class Atmcustomer5Catp01300101:
    class Meta:
        name = "ATMCustomer5"

    prfl: Optional[AtmcustomerProfile2Catp01300101] = field(
        default=None,
        metadata={
            "name": "Prfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    authntcn_rslt: list[TransactionVerificationResult5Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "AuthntcnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AtmtransactionAmounts8Catp01300101:
    class Meta:
        name = "ATMTransactionAmounts8"

    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    max_pssbl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxPssblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    min_pssbl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinPssblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    addtl_amt: list[AtmtransactionAmounts7Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    dpst_lmts: list[AtmtransactionAmounts9Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "DpstLmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class Action7Catp01300101:
    actn_tp: Optional[ActionType6Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    msg_to_pres: Optional[ActionMessage4Catp01300101] = field(
        default=None,
        metadata={
            "name": "MsgToPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    req_to_prfrm: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "ReqToPrfrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AlgorithmIdentification12Catp01300101:
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter5Catp01300101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AlgorithmIdentification13Catp01300101:
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter6Catp01300101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AlgorithmIdentification14Catp01300101:
    algo: Optional[Algorithm15Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter6Catp01300101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AlgorithmIdentification15Catp01300101:
    algo: Optional[Algorithm12Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter7Catp01300101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class CertificateIssuer1Catp01300101:
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class NameAndAddress3Catp01300101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress1Catp01300101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )


@dataclass
class PostalAddress17Catp01300101:
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    glctn: Optional[GeographicLocation1ChoiceCatp01300101] = field(
        default=None,
        metadata={
            "name": "GLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class Traceability4Catp01300101:
    rlay_id: Optional[GenericIdentification77Catp01300101] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )


@dataclass
class Atmcommand7Catp01300101:
    class Meta:
        name = "ATMCommand7"

    tp: Optional[Atmcommand4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    urgcy: Optional[TmscontactLevel2Code] = field(
        default=None,
        metadata={
            "name": "Urgcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    cmd_id: Optional[AtmcommandIdentification1Catp01300101] = field(
        default=None,
        metadata={
            "name": "CmdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    cmd_params: Optional[AtmcommandParameters1ChoiceCatp01300101] = field(
        default=None,
        metadata={
            "name": "CmdParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AuthorisationResult13Catp01300101:
    authstn_ntty: Optional[PartyType16Code] = field(
        default=None,
        metadata={
            "name": "AuthstnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    authstn_rspn: Optional[ResponseType7Catp01300101] = field(
        default=None,
        metadata={
            "name": "AuthstnRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    rspn_trac: list[ResponseType8Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "RspnTrac",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    authstn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthstnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 6,
            "max_length": 8,
        },
    )
    actn: list[Action7Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AutomatedTellerMachine2Catp01300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    lctn: Optional[PostalAddress17Catp01300101] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class CardAccount10Catp01300101:
    acct_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AcctSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    selctn_mtd: Optional[AccountChoiceMethod1Code] = field(
        default=None,
        metadata={
            "name": "SelctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    selctd_acct_tp: Optional[CardAccountType3Code] = field(
        default=None,
        metadata={
            "name": "SelctdAcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    acct_ownr: Optional[NameAndAddress3Catp01300101] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    acct_idr: Optional[AccountIdentification31ChoiceCatp01300101] = field(
        default=None,
        metadata={
            "name": "AcctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    cdt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CdtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svcr: Optional[PartyIdentification72ChoiceCatp01300101] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    bal: Optional[AmountAndDirection43Catp01300101] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    bal_disp_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BalDispFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    dflt_acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DfltAcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    lmts: Optional[AtmtransactionAmounts8Catp01300101] = field(
        default=None,
        metadata={
            "name": "Lmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class EncryptedContent3Catp01300101:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification14Catp01300101] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class Header31Catp01300101:
    msg_fctn: Optional[AtmmessageFunction2Catp01300101] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    initg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prc_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tracblt: list[Traceability4Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class IssuerAndSerialNumber1Catp01300101:
    issr: Optional[CertificateIssuer1Catp01300101] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek4Catp01300101:
    class Meta:
        name = "KEK4"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier2Catp01300101] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification13Catp01300101] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter4Catp01300101:
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Catp01300101] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AlgorithmIdentification11Catp01300101:
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter4Catp01300101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class Recipient5ChoiceCatp01300101:
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Catp01300101] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    key_idr: Optional[Kekidentifier2Catp01300101] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class KeyTransport4Catp01300101:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCatp01300101] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification11Catp01300101] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient4ChoiceCatp01300101:
    key_trnsprt: Optional[KeyTransport4Catp01300101] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    kek: Optional[Kek4Catp01300101] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    key_idr: Optional[Kekidentifier2Catp01300101] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AuthenticatedData4Catp01300101:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCatp01300101] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification15Catp01300101] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catp01300101] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData4Catp01300101:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCatp01300101] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent3Catp01300101] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class ContentInformationType10Catp01300101:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData4Catp01300101] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )


@dataclass
class ContentInformationType15Catp01300101:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData4Catp01300101] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )


@dataclass
class Atmenvironment12Catp01300101:
    class Meta:
        name = "ATMEnvironment12"

    acqrr: Optional[Acquirer7Catp01300101] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    atmmgr: Optional[Acquirer8Catp01300101] = field(
        default=None,
        metadata={
            "name": "ATMMgr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    hstg_ntty: Optional[TerminalHosting1Catp01300101] = field(
        default=None,
        metadata={
            "name": "HstgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    atm: Optional[AutomatedTellerMachine2Catp01300101] = field(
        default=None,
        metadata={
            "name": "ATM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    cstmr: Optional[Atmcustomer5Catp01300101] = field(
        default=None,
        metadata={
            "name": "Cstmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    prtctd_card_data: Optional[ContentInformationType10Catp01300101] = field(
        default=None,
        metadata={
            "name": "PrtctdCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    plain_card_data: Optional[PlainCardData19Catp01300101] = field(
        default=None,
        metadata={
            "name": "PlainCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class Atmtransaction16Catp01300101:
    class Meta:
        name = "ATMTransaction16"

    tx_id: Optional[TransactionIdentifier1Catp01300101] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmpltn_reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CmpltnReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    acct_data: Optional[CardAccount10Catp01300101] = field(
        default=None,
        metadata={
            "name": "AcctData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    prtctd_acct_data: Optional[ContentInformationType10Catp01300101] = field(
        default=None,
        metadata={
            "name": "PrtctdAcctData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    ttl_authrsd_amt: Optional[AmountAndCurrency1Catp01300101] = field(
        default=None,
        metadata={
            "name": "TtlAuthrsdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    ttl_reqd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlReqdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dtld_reqd_amt: list[DetailedAmount16Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "DtldReqdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    addtl_chrg: list[DetailedAmount13Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlChrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    authstn_rslt: Optional[AuthorisationResult13Catp01300101] = field(
        default=None,
        metadata={
            "name": "AuthstnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    iccrltd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )
    cmd: list[Atmcommand7Catp01300101] = field(
        default_factory=list,
        metadata={
            "name": "Cmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class AtmdepositResponse1Catp01300101:
    class Meta:
        name = "ATMDepositResponse1"

    envt: Optional[Atmenvironment12Catp01300101] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    cntxt: Optional[Atmcontext11Catp01300101] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    tx: Optional[Atmtransaction16Catp01300101] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )


@dataclass
class AtmdepositResponseV01Catp01300101:
    class Meta:
        name = "ATMDepositResponseV01"

    hdr: Optional[Header31Catp01300101] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
            "required": True,
        },
    )
    prtctd_atmdpst_rspn: Optional[ContentInformationType10Catp01300101] = field(
        default=None,
        metadata={
            "name": "PrtctdATMDpstRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    atmdpst_rspn: Optional[AtmdepositResponse1Catp01300101] = field(
        default=None,
        metadata={
            "name": "ATMDpstRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )
    scty_trlr: Optional[ContentInformationType15Catp01300101] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01",
        },
    )


@dataclass
class Catp01300101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:catp.013.001.01"

    atmdpst_rspn: Optional[AtmdepositResponseV01Catp01300101] = field(
        default=None,
        metadata={
            "name": "ATMDpstRspn",
            "type": "Element",
            "required": True,
        },
    )
