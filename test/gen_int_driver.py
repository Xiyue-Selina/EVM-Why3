template = """
printer "ocaml"

module MinimalEVM.UInt_WIDTH_

  syntax type uint_WIDTH_  "int"
  syntax literal uint_WIDTH_ "%1"

  syntax val (+)     "%1 + %2"
  syntax val (-)     "%1 - %2"
  syntax val (-_)    "-%1"
  syntax val ( * )   "%1 * %2"
  syntax val (/)     "%1 / %2"
  syntax val (%)     "%1 % %2"
  syntax val (=)     "%1 == %2"
  syntax val (<=)    "%1 <= %2"
  syntax val (<)     "%1 < %2"
  syntax val (>=)    "%1 >= %2"
  syntax val (>)     "%1 > %2"

  syntax val of_int "%1"
  syntax val to_int "%1"

end
"""
lst = [4, 8, 160, 256]
for x in lst:
  content = template.replace("_WIDTH_", str(x))
  with open("UInt%d.drv" % x, "w") as f:
      f.write(content)