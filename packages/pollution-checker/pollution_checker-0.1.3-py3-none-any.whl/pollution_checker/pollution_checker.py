
""" Check Class Pollution Type with universal payload:
    1. Good Get, Good Set
    2. Good Get, Attribute Set Only
    3. TODO: Good Get, Item Set Only
    4. Attribute Get Only, Good Set
    5. Attribute Set/Get Only
"""
class PollutionChecker:
    def __init__(self, dst_obj, func):
        self.dst_obj = dst_obj
        self.p_function = func
        self.init_payloads()
        
    def init_payloads(self):
        self.payloads = {
            "Good Get, Good Set": [
                # Good Get With Set Item
                (
                    {"__init__": {"__globals__": {"__builtins__": {"__loader__": {"__doc__": "polluted"}}}}},
                    'result=str(self.dst_obj.__init__.__globals__["__builtins__"].__loader__.__doc__)'
                ),
                # Attribute Get With Attr Set (If execution happens here, Good Get is proved)
                (
                    {"__init__": {"__globals__":{"__name__": "polluted"}}},
                    'result=str(self.dst_obj.__init__.__globals__["__name__"])'
                )
            ],
            "Good Get, Attribute Set Only": [
                (
                    {"__init__": {"__globals__": {"__builtins__": {"__loader__": {"__doc__": "polluted"}}}}},
                    'result=str(self.dst_obj.__init__.__globals__["__builtins__"].__loader__.__doc__)'
                )
            ],
            "Attribute Get Only, Good Set": [
                # Set Item
                (
                    {"__init__": {"__globals__":{"__name__": "polluted"}}},
                    'result=str(self.dst_obj.__init__.__globals__["__name__"])'
                ),
                # Set Attribute
                (
                    {"__class__": {"poooolute_test": "polluted"}},
                    'result=str(self.dst_obj.__class__.poooolute_test)'
                )
            ],
            "Attribute Set/Get Only": [
                (
                    {"__class__": {"poooolute_test": "polluted"}},
                    'result=str(self.dst_obj.__class__.poooolute_test)'
                )
            ]
        }
    def func(self, *args):
        for rule_name, rules in self.payloads.items():
            for payload, assertion in rules:
                loaded_args = tuple(payload if arg == "PAYLOADS" else arg for arg in args)
                self.p_function(*loaded_args)
                try:
                    """ https://stackoverflow.com/questions/23917776/how-do-i-get-the-return-value-when-using-python-exec-on-the-code-object-of-a-fun """
                    loc = {}
                    # TODO: dst_obj = kwargs["dst_obj"]
                    exec(assertion, locals(), loc)
                    assert loc["result"].endswith("polluted"), f"[-] {rule_name} Failed!"
                except Exception as e:
                    break
                print(f"[+] {rule_name} Passed!")
                return True
            print(f"[-] {rule_name} Failed!")
        return False
