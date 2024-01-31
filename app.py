import re
import json

assembly_code = """
  401000:	ff 20                	jmpq   *(%rax)
  401002:	47 6f                	rex.RXB outsl %ds:(%rsi),(%dx)
  401004:	20 62 75             	and    %ah,0x75(%rdx)
  401007:	69 6c 64 20 49 44 3a 	imul   $0x203a4449,0x20(%rsp,%riz,2),%ebp
  40100e:	20
  40100f:	22 51 67             	and    0x67(%rcx),%dl
"""

def parse_assembly_to_json(assembly_code):
    lines = assembly_code.strip().split('\n')

    json_output = []
    for line in lines:
        # 使用正则表达式匹配地址、指令码、助记符和操作数
        match = re.match(r'\s*([0-9a-fA-F]+):\s+([0-9a-fA-F\s]+)\s+(\S+)\s+(.*)$', line)
        if match:
            address, opcodes, mnemonic, operands = match.groups()
            json_output.append({
                'address': address,
                'opcode': opcodes,
                'mnemonic': mnemonic,
                'operands': operands,
            })

    return json.dumps(json_output, indent=2)

if __name__ == '__main__':
  json_output = parse_assembly_to_json(assembly_code)
  print(json_output)
