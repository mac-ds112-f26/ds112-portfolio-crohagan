import csv
import xml.etree.ElementTree as ET

TYPE = "HKCategoryTypeIdentifierSleepAnalysis"

with open("sleep.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["source", "value", "startDate", "endDate"])
    for event, elem in ET.iterparse("pvj/apple_health_export/export.xml", events=("end",)):
        if elem.tag == "Record" and elem.get("type") == TYPE:
            w.writerow([
                elem.get("sourceName"),
                elem.get("value").replace("HKCategoryValueSleepAnalysis", ""),
                elem.get("startDate"),
                elem.get("endDate"),
            ])
        elem.clear()
