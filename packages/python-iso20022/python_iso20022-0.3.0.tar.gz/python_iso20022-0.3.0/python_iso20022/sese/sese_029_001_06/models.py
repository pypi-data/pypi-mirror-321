from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    DateType3Code,
    DeliveryReceiptType2Code,
    ReceiveDelivery1Code,
    SettlementDate4Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06"


@dataclass
class ActiveCurrencyAndAmountSese02900106(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSese02900106(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceSese02900106(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSese02900106(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Sese02900106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese02900106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSese02900106(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Sese02900106(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Sese02900106(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection51Sese02900106(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSese02900106] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSese02900106] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            },
        )
    )


@dataclass
class BlockChainAddressWallet3Sese02900106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Sese02900106] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class OtherIdentification1Sese02900106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSese02900106(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese02900106] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class PostalAddress1Sese02900106(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Quantity51ChoiceSese02900106(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Sese02900106] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class SecuritiesAccount19Sese02900106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese02900106] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SettlementDateCode7ChoiceSese02900106(ISO20022MessageElement):
    cd: Optional[SettlementDate4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    prtry: Optional[GenericIdentification30Sese02900106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class SettlementTypeAndIdentification18Sese02900106(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_mvmnt_tp: Optional[ReceiveDelivery1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Sese02900106(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Sese02900106] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )


@dataclass
class TradeDateCode3ChoiceSese02900106(ISO20022MessageElement):
    cd: Optional[DateType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    prtry: Optional[GenericIdentification30Sese02900106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class NameAndAddress5Sese02900106(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese02900106] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class PartyIdentification144Sese02900106(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SecurityIdentification19Sese02900106(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Sese02900106] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementDate17ChoiceSese02900106(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    dt_cd: Optional[SettlementDateCode7ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class TradeDate8ChoiceSese02900106(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    dt_cd: Optional[TradeDateCode3ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class PartyIdentification120ChoiceSese02900106(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese02900106] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese02900106] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class PartyIdentification122ChoiceSese02900106(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese02900106] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification134ChoiceSese02900106(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese02900106] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese02900106] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification148Sese02900106(ISO20022MessageElement):
    id: Optional[PartyIdentification122ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification149Sese02900106(ISO20022MessageElement):
    id: Optional[PartyIdentification134ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentificationAndAccount195Sese02900106(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese02900106] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese02900106] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementParties97Sese02900106(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification148Sese02900106] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount195Sese02900106] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount195Sese02900106] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount195Sese02900106] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount195Sese02900106] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount195Sese02900106] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class TransactionDetails153Sese02900106(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Sese02900106] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )
    trad_dt: Optional[TradeDate8ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    sttlm_dt: Optional[SettlementDate17ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )
    sttlm_qty: Optional[Quantity51ChoiceSese02900106] = field(
        default=None,
        metadata={
            "name": "SttlmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )
    sttlm_amt: Optional[AmountAndDirection51Sese02900106] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties97Sese02900106] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties97Sese02900106] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    invstr: Optional[PartyIdentification149Sese02900106] = field(
        default=None,
        metadata={
            "name": "Invstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class SecuritiesSettlementAllegementRemovalAdviceV06Sese02900106(
    ISO20022MessageElement
):
    acct_svcr_tx_id: Optional[SettlementTypeAndIdentification18Sese02900106] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "required": True,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr: Optional[PartyIdentification144Sese02900106] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese02900106] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese02900106] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    tx_dtls: Optional[TransactionDetails153Sese02900106] = field(
        default=None,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )
    splmtry_data: list[SupplementaryData1Sese02900106] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06",
        },
    )


@dataclass
class Sese02900106(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.029.001.06"

    scties_sttlm_allgmt_rmvl_advc: Optional[
        SecuritiesSettlementAllegementRemovalAdviceV06Sese02900106
    ] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmAllgmtRmvlAdvc",
            "type": "Element",
            "required": True,
        },
    )
