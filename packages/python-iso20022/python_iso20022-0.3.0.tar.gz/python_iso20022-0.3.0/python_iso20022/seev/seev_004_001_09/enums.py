from enum import Enum


class DeliveryPlace3Code(Enum):
    EMAL = "EMAL"
    EMPL = "EMPL"
    INDI = "INDI"
    ENTR = "ENTR"
    OADR = "OADR"


class PartyRole3Code(Enum):
    GATR = "GATR"


class VoteInstruction7Code(Enum):
    ABST = "ABST"
    CAGS = "CAGS"
    AMGT = "AMGT"
    BLNK = "BLNK"
    CFOR = "CFOR"
    NOAC = "NOAC"
    ONEY = "ONEY"
    THRY = "THRY"
    TWOY = "TWOY"
    WTHH = "WTHH"
    WMGT = "WMGT"


class VotingParticipationMethod2Code(Enum):
    PHNV = "PHNV"
