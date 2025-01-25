import re
from tkinter import ttk

class CSSParseError(Exception):
    pass

class InvalidCSSPropertyError(Exception):
    def __init__(self, property_name):
        super().__init__(f"Invalid CSS property: {property_name}")

class MissingCSSPropertyError(Exception):
    def __init__(self, selector, property_name):
        super().__init__(f"Missing property '{property_name}' in selector '{selector}'")

class Tkcss:
    def __init__(self, css_file):
        self.css_file = css_file
        self.styles = {}

        self._parse_css()
    
    def _parse_css(self):
        """Parse the CSS file into a dictionary."""
        try:
            with open(self.css_file, 'r') as file:
                content = file.read()

            # Match selectors (e.g., TButton, TLabel) and their properties
            pattern = r'(\w+)\s*{([^}]+)}'
            matches = re.findall(pattern, content)

            if not matches:
                raise CSSParseError("No valid CSS selectors found in the file.")

            for selector, properties in matches:
                props = {}
                for prop in properties.split(';'):
                    if ':' in prop:
                        key, value = prop.split(':', 1)
                        props[key.strip()] = value.strip()
                if not props:
                    raise InvalidCSSPropertyError(selector)
                self.styles[selector] = props

        except FileNotFoundError:
            raise CSSParseError("CSS file not found.")
        except Exception as e:
            raise CSSParseError(f"Error reading CSS file: {e}")
        
    def apply(self):
        """Apply parsed styles to ttk widgets."""
        style = ttk.Style()

        try:
            for selector, properties in self.styles.items():
                if selector == 'Button' or selector == 'button':
                    if 'background-color' not in properties:
                        raise MissingCSSPropertyError(selector, 'background-color')
                    if 'color' not in properties:
                        raise MissingCSSPropertyError(selector, 'color')

                    style.configure(
                        'TButton',
                        background=properties.get('background-color', '#ffffff'),
                        foreground=properties.get('color', '#000000'),
                        font=(
                            properties.get('font-family', 'Arial'),
                            int(properties.get('font-size', '12'))
                        ),
                        padding=properties.get('padding', '5 10').split()
                    )
                    if ':hover' in properties:
                        style.map(
                            'TButton',
                            background=[('active', properties.get('background-color', '#ffffff'))]
                        )

                elif selector == 'Label' or selector == "label":
                    style.configure(
                        'TLabel',
                        font=(
                            properties.get('font-family', 'Arial'),
                            int(properties.get('font-size', '12'))
                        ),
                        foreground=properties.get('color', '#000000')
                    )

                else:
                    raise InvalidCSSPropertyError(selector)

        except MissingCSSPropertyError as e:
            print(f"Error: {e}")
        except InvalidCSSPropertyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error applying styles: {e}")