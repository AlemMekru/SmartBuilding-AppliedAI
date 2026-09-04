from strands import tool

from app.data.building_state import building_state


@tool
def get_zone_status(zone_name: str) -> dict:
    """
    Get the current operational status of a smart-building zone.

    Args:
        zone_name: Zone identifier, for example "meeting_room_204".

    Returns:
        Current HVAC, temperature, occupancy, lighting,
        alarm, and access-control information for the zone.
    """
    zones = building_state["zones"]

    if zone_name not in zones:
        return {
            "error": "Zone not found",
            "zone_name": zone_name,
        }

    return {
        "building": building_state["building"],
        "zone": zone_name,
        "status": zones[zone_name],
    }