import sys
import counter_module
import counter_module
print("in sys.modules:", "counter_module" in sys.modules)
print("same object:", counter_module is sys.modules["counter_module"])
