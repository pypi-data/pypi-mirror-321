from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import (
    CreditDebitCode,
    EventFrequency3Code,
    FormOfSecurity1Code,
    InterestComputationMethod2Code,
    OptionStyle2Code,
    OptionType1Code,
    PartialSettlement2Code,
    PriceValueType1Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    SecuritiesPaymentStatus1Code,
)
from python_iso20022.semt.enums import (
    CorporateActionEventType33Code,
    SecuritiesBalanceType11Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09"


@dataclass
class ActiveCurrencyAndAmountSemt01500209:
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
class DateAndDateTime2ChoiceSemt01500209:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class FinancialInstrumentQuantity36ChoiceSemt01500209:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification18Semt01500209:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification39Semt01500209:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([^/]+/)+([^/]+)|([^/]*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 8,
            "pattern": r"([^/]+/)+([^/]+)|([^/]*)",
        },
    )


@dataclass
class GenericIdentification47Semt01500209:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification84Semt01500209:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "min_length": 1,
            "max_length": 34,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification86Semt01500209:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource3ChoiceSemt01500209:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource4ChoiceSemt01500209:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "length": 2,
            "pattern": r"XX|TS",
        },
    )


@dataclass
class MarketIdentification4ChoiceSemt01500209:
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class RestrictedFinactiveOrHistoricCurrencyAnd13DecimalAmountSemt01500209:
    class Meta:
        name = "RestrictedFINActiveOrHistoricCurrencyAnd13DecimalAmount"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 13,
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
class RestrictedFinactiveOrHistoricCurrencyAndAmountSemt01500209:
    class Meta:
        name = "RestrictedFINActiveOrHistoricCurrencyAndAmount"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
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
class SupplementaryDataEnvelope1Semt01500209:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AdditionalParameters34Semt01500209:
    prtl_sttlm: Optional[PartialSettlement2Code] = field(
        default=None,
        metadata={
            "name": "PrtlSttlm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prvs_prtl_conf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvsPrtlConfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class BlockChainAddressWallet7Semt01500209:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    tp: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 70,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,70}",
        },
    )


@dataclass
class ClassificationType33ChoiceSemt01500209:
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification86Semt01500209] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class CorporateActionEventType101ChoiceSemt01500209:
    cd: Optional[CorporateActionEventType33Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prtry: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class ForeignExchangeTerms23Semt01500209:
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSemt01500209] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )


@dataclass
class FormOfSecurity7ChoiceSemt01500209:
    cd: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prtry: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class Frequency27ChoiceSemt01500209:
    cd: Optional[EventFrequency3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prtry: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class GenericIdentification85Semt01500209:
    tp: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class InterestComputationMethodFormat5ChoiceSemt01500209:
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prtry: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class Number23ChoiceSemt01500209:
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[GenericIdentification18Semt01500209] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class OptionStyle9ChoiceSemt01500209:
    cd: Optional[OptionStyle2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prtry: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class OptionType7ChoiceSemt01500209:
    cd: Optional[OptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prtry: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class OtherIdentification2Semt01500209:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "min_length": 1,
            "max_length": 31,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,31}",
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource4ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )


@dataclass
class OtherIdentification3Semt01500209:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "min_length": 1,
            "max_length": 31,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,31}",
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )


@dataclass
class PartyIdentification136ChoiceSemt01500209:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Semt01500209] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class PriceRateOrAmount1ChoiceSemt01500209:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[
        RestrictedFinactiveOrHistoricCurrencyAnd13DecimalAmountSemt01500209
    ] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class QuantityBreakdown64Semt01500209:
    lot_nb: Optional[GenericIdentification39Semt01500209] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    lot_qty: Optional[FinancialInstrumentQuantity36ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "LotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class QuantityBreakdown65Semt01500209:
    lot_nb: Optional[GenericIdentification39Semt01500209] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    lot_qty: Optional[FinancialInstrumentQuantity36ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "LotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    scties_sub_bal_tp: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "SctiesSubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Semt01500209:
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText15Semt01500209:
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class SecuritiesAccount30Semt01500209:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}",
        },
    )
    tp: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesBalanceType8ChoiceSemt01500209:
    cd: Optional[SecuritiesBalanceType11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prtry: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class SecuritiesPaymentStatus6ChoiceSemt01500209:
    cd: Optional[SecuritiesPaymentStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prtry: Optional[GenericIdentification47Semt01500209] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class SupplementaryData1Semt01500209:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt01500209] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )


@dataclass
class YieldedOrValueType1ChoiceSemt01500209:
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    val_tp: Optional[PriceValueType1Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class AmountAndDirection55Semt01500209:
    amt: Optional[RestrictedFinactiveOrHistoricCurrencyAndAmountSemt01500209] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[
        RestrictedFinactiveOrHistoricCurrencyAndAmountSemt01500209
    ] = field(
        default=None,
        metadata={
            "name": "OrgnlCcyAndOrdrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    fxdtls: Optional[ForeignExchangeTerms23Semt01500209] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class Price3Semt01500209:
    tp: Optional[YieldedOrValueType1ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmount1ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )


@dataclass
class SafekeepingPlaceFormat39ChoiceSemt01500209:
    id: Optional[SafekeepingPlaceTypeAndText15Semt01500209] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Semt01500209] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prtry: Optional[GenericIdentification85Semt01500209] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class SecuritiesSubBalanceTypeAndQuantityBreakdown6Semt01500209:
    tp: Optional[SecuritiesBalanceType8ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    qty_brkdwn: list[QuantityBreakdown65Semt01500209] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class SecurityIdentification20Semt01500209:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification2Semt01500209] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class SecurityIdentification32Semt01500209:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification3Semt01500209] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class IntraPositionDetails61Semt01500209:
    sttld_qty: Optional[FinancialInstrumentQuantity36ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "SttldQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    scties_sub_bal_id: Optional[GenericIdentification39Semt01500209] = field(
        default=None,
        metadata={
            "name": "SctiesSubBalId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    coll_mntr_amt: Optional[AmountAndDirection55Semt01500209] = field(
        default=None,
        metadata={
            "name": "CollMntrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prevsly_sttld_qty: Optional[FinancialInstrumentQuantity36ChoiceSemt01500209] = (
        field(
            default=None,
            metadata={
                "name": "PrevslySttldQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            },
        )
    )
    rmng_to_be_sttld_qty: Optional[FinancialInstrumentQuantity36ChoiceSemt01500209] = (
        field(
            default=None,
            metadata={
                "name": "RmngToBeSttldQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            },
        )
    )
    sttlm_dt: Optional[DateAndDateTime2ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    avlbl_dt: Optional[DateAndDateTime2ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "AvlblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    corp_actn_evt_tp: Optional[CorporateActionEventType101ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    bal_fr: Optional[SecuritiesSubBalanceTypeAndQuantityBreakdown6Semt01500209] = field(
        default=None,
        metadata={
            "name": "BalFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    bal_to: Optional[SecuritiesSubBalanceTypeAndQuantityBreakdown6Semt01500209] = field(
        default=None,
        metadata={
            "name": "BalTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    instr_prcg_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrPrcgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class PriceType5ChoiceSemt01500209:
    mkt: Optional[Price3Semt01500209] = field(
        default=None,
        metadata={
            "name": "Mkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    indctv: Optional[Price3Semt01500209] = field(
        default=None,
        metadata={
            "name": "Indctv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class FinancialInstrumentAttributes119Semt01500209:
    plc_of_listg: Optional[MarketIdentification4ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat5ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    regn_form: Optional[FormOfSecurity7ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "RegnForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    pmt_frqcy: Optional[Frequency27ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    pmt_sts: Optional[SecuritiesPaymentStatus6ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "PmtSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    varbl_rate_chng_frqcy: Optional[Frequency27ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "VarblRateChngFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    clssfctn_tp: Optional[ClassificationType33ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    optn_style: Optional[OptionStyle9ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    optn_tp: Optional[OptionType7ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    prvs_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cur_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld_to_mtrty_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "YldToMtrtyRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    indx_rate_bsis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cpn_attchd_nb: Optional[Number23ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "CpnAttchdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    pool_nb: Optional[GenericIdentification39Semt01500209] = field(
        default=None,
        metadata={
            "name": "PoolNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    qty_brkdwn: list[QuantityBreakdown64Semt01500209] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    varbl_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VarblRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    cllbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CllblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    putbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PutblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    mkt_or_indctv_pric: Optional[PriceType5ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "MktOrIndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    exrc_pric: Optional[Price3Semt01500209] = field(
        default=None,
        metadata={
            "name": "ExrcPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    sbcpt_pric: Optional[Price3Semt01500209] = field(
        default=None,
        metadata={
            "name": "SbcptPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    convs_pric: Optional[Price3Semt01500209] = field(
        default=None,
        metadata={
            "name": "ConvsPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    strk_pric: Optional[Price3Semt01500209] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity36ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity36ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    undrlyg_fin_instrm_id: list[SecurityIdentification32Semt01500209] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygFinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    fin_instrm_attr_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class IntraPositionMovementConfirmation002V09Semt01500209:
    addtl_params: Optional[AdditionalParameters34Semt01500209] = field(
        default=None,
        metadata={
            "name": "AddtlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    acct_ownr: Optional[PartyIdentification136ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount30Semt01500209] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet7Semt01500209] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat39ChoiceSemt01500209] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification20Semt01500209] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    fin_instrm_attrbts: Optional[FinancialInstrumentAttributes119Semt01500209] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )
    intra_pos_dtls: Optional[IntraPositionDetails61Semt01500209] = field(
        default=None,
        metadata={
            "name": "IntraPosDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Semt01500209] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09",
        },
    )


@dataclass
class Semt01500209:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09"

    intra_pos_mvmnt_conf: Optional[
        IntraPositionMovementConfirmation002V09Semt01500209
    ] = field(
        default=None,
        metadata={
            "name": "IntraPosMvmntConf",
            "type": "Element",
            "required": True,
        },
    )
