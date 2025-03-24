from browser_use import BrowserConfig
import inspect

# Print the signature of BrowserConfig.__init__
print("BrowserConfig parameters:")
print(inspect.signature(BrowserConfig.__init__))

# Create an instance to see all attributes
try:
    config = BrowserConfig()
    print("\nDefault attributes:")
    for attr, value in vars(config).items():
        print(f"{attr}: {value}")
except Exception as e:
    print(f"Error creating BrowserConfig: {e}") 