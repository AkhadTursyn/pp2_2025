import json

with open("/Users/ahadtursyn/VS CODE/pp2/lab4/math/json/sample-data.json") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<5}")
print("-" * 80)

for item in data["imdata"]:
    interface = item["l1PhysIf"]["attributes"]
    dn = interface["dn"]
    description = interface.get("descr", "")
    speed = interface.get("speed", "inherit")
    mtu = interface["mtu"]

    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<5}")