from wox import Wox
import os
import subprocess

class HammerConverter(Wox):
    def get_icon_path(self):
        """Get the icon path dynamically without changing anything else"""
        return os.path.join(os.path.dirname(__file__), "Images", "app.png")

    def query(self, query):
        icon_path = self.get_icon_path()
        q = query.strip().lower()

        # 🔹 If user just types "hammer", show all available conversions
        if not q:
            return self.show_available_conversions()

        parts = q.split()
        if len(parts) < 3:
            return [{
                "Title": "Usage examples:",
                "SubTitle": "hammer 128 units to meters   •   hammer 3 meters to units",
                "IcoPath": icon_path,

            }] + self.show_available_conversions()

        try:
            value = float(parts[0])
            from_unit = parts[1]
            to_unit = parts[-1]
        except Exception:
            return [{"Title": "Invalid format", "SubTitle": "Use: hammer 128 units to meters", "IcoPath": icon_path}]

        result = self.convert(value, from_unit, to_unit)
        if result is None:
            return [{
                "Title": "Invalid units",
                "SubTitle": "Supported: yards, feet, inches, meters, decimeters, centimeters, units, skybox",
                "IcoPath": icon_path
            }] + self.show_available_conversions()

        return [{
            "Title": f"{value} {from_unit} = {result} {to_unit}",
            "SubTitle": "Press Enter to copy result to clipboard",
            "IcoPath": icon_path,
            "ContextData": "ctxData",
            "JsonRPCAction": {
                "method": "copy",
                "parameters": [str(result)],
                "dontHideAfterAction": False
            }
        }]

    def copy(self, text):
        subprocess.run(["clip"], input=text.encode("utf-8"))
        return {"Result": "Copied!"}

    def show_available_conversions(self):
        icon_path = self.get_icon_path()
        examples = [
            ("Feet → Units", "hammer 1 feet to units"),
            ("Meters → Units", "hammer 3 meters to units"),
            ("Units → Meters", "hammer 128 units to meters"),
            ("Inches → Units", "hammer 12 inches to units"),
            ("Skybox → Meters", "hammer 1 skybox to meters"),
            ("Meters → Skybox", "hammer 64 meters to skybox"),
        ]
        results = []
        for title, example in examples:
            results.append({
                "Title": title,
                "SubTitle": f"Example: {example}",
                "IcoPath": icon_path,
                "ContextData": "ctxData",
                "JsonRPCAction": {
                    "method": "copy",
                    "parameters": [example],
                    "dontHideAfterAction": False
                }
            })
        return results

    def convert(self, value, from_unit, to_unit):
        real = {
            "yards": 0.9144,
            "feet": 0.3048,
            "inches": 0.0254,
            "meters": 1.0,
            "decimeters": 0.1,
            "centimeters": 0.01
        }
        hammer = {
            "units": 0.01905,
            "skybox": 0.3048
        }

        def round_05(x):
            return round(x * 20.0) / 20.0

        # Determine direction
        if from_unit in real and to_unit in hammer:
            from_val = real[from_unit]
            to_val = hammer[to_unit]
        elif from_unit in hammer and to_unit in real:
            from_val = hammer[from_unit]
            to_val = real[to_unit]
        else:
            return None

        converted = value * (from_val / to_val)
        return round_05(converted)

if __name__ == "__main__":
    HammerConverter()
