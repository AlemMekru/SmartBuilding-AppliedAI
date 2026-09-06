import asyncio
import logging
from zigpy_znp.zigbee.application import ControllerApplication

#logging.basicConfig(level=logging.DEBUG)

RADIO_PATH = "/dev/cu.usbserial-14330"


async def main():
    app = ControllerApplication(
        {
            "database_path": "zigbee.db",
            "device": {
                "path": RADIO_PATH,
            },
        }
    )

    print("Starting Zigbee coordinator...")

    await app.startup(auto_form=True)

    print("Coordinator started.")
    print("Opening network for pairing for 180 seconds...")

    await app.permit(180)

    print("Put the SONOFF SNZB-02D into pairing mode now.")

    await asyncio.sleep(180)

    print("Pairing window closed.")

    print("\nKnown devices:")
    for ieee, device in app.devices.items():
        print(ieee, device)

    await app.shutdown()


asyncio.run(main())