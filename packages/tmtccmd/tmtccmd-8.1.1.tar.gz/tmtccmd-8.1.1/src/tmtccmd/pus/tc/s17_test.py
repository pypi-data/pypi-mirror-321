from deprecated.sphinx import deprecated
from spacepackets.ecss import PusService, PusTelecommand
from spacepackets.ecss.pus_17_test import Subservice


@deprecated(
    version="4.0.0a2",
    reason="use create... API instead",
)
def pack_service_17_ping_command(apid: int = 0, seq_count: int = 0) -> PusTelecommand:
    return create_service_17_ping_command(apid, seq_count)


def create_service_17_ping_command(apid: int = 0, seq_count: int = 0) -> PusTelecommand:
    """Generate a simple ping PUS telecommand packet"""
    return PusTelecommand(
        service=PusService.S17_TEST,
        subservice=Subservice.TC_PING,
        apid=apid,
        seq_count=seq_count,
    )
