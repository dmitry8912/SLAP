import tokenize
from io import StringIO


class SlapVM(object):
    __stack = list()
    __vars = dict()

    __code = list()
    __ip = 0

    @classmethod
    def run(cls, code: str):
        cls.__stack = list()
        cls.__vars = dict()
        cls.__code = list()
        cls.__ip = 0

        cls.__code = code.splitlines()
        while cls.__ip < len(cls.__code):
            # print(cls.__ip)
            cls.run_line(cls.__code[cls.__ip])
            cls.__ip = cls.__ip + 1

    @classmethod
    def run_line(cls, code):
        stream = StringIO(code)
        tokens = tokenize.generate_tokens(stream.readline)
        larg = rarg = opcode = None

        for toknum, tokval, _, _, _ in tokens:
            if toknum == tokenize.NAME:
                if cls.is_opcode(tokval):
                    opcode = tokval
                elif larg is None:
                    larg = int(tokval) if tokval.isdigit() else tokval
                else:
                    rarg = int(tokval) if tokval.isdigit() else tokval
            if toknum == tokenize.NUMBER:
                if larg is None:
                    larg = int(tokval) if tokval.isdigit() else tokval
                else:
                    rarg = int(tokval) if tokval.isdigit() else tokval

        if opcode is not None:
            cls.execute_code_object(opcode, larg, rarg)

    @classmethod
    def execute_code_object(cls, opcode: str, larg=None, rarg=None):
        cls.get_opcodes()[opcode.lower()](larg, rarg)

    @classmethod
    def is_opcode(cls, propapbly_opcode: str) -> bool:
        return propapbly_opcode.lower() in cls.get_opcodes().keys()

    @classmethod
    def slapshot(cls, val, *agrs):
        cls.__stack.append(cls.__vars.get(val, val))

    @classmethod
    def backslap(cls, var, *agrs):
        cls.__vars[var] = cls.__stack.pop()

    @classmethod
    def slapscreen(cls, val, *agrs):
        print(cls.__vars.get(val, val))

    @classmethod
    def slapput(cls, var, *agrs):
        print(' SLAP > ')
        input_def = input()
        cls.__vars[var] = int(input_def) if input_def.isdigit() else input_def

    @classmethod
    def plop_in(cls, var, val, *agrs):
        cls.__vars[var] = cls.__vars.get(val, val)

    @classmethod
    def slap(cls, var_l, var_r, *args):
        cls.__vars[var_l] = cls.__vars.get(var_l) + cls.__vars.get(var_r, var_r)

    @classmethod
    def unslap(cls, var_l, var_r, *args):
        cls.__vars[var_l] = cls.__vars.get(var_l) - cls.__vars.get(var_r, var_r)

    @classmethod
    def multislap(cls, var_l, var_r, *args):
        cls.__vars[var_l] = cls.__vars.get(var_l) * cls.__vars.get(var_r, var_r)

    @classmethod
    def multiunslap(cls, var_l, var_r, *args):
        cls.__vars[var_l] = cls.__vars.get(var_l) / cls.__vars.get(var_r, var_r)

    @classmethod
    def punches(cls, var_l, var_r, *args):
        cls.slapshot(int(cls.__vars.get(var_l, var_l) > cls.__vars.get(var_r, var_r)))

    @classmethod
    def nonsmack(cls, var_l, var_r, *args):
        cls.slapshot(int(cls.__vars.get(var_l, var_l) == cls.__vars.get(var_r, var_r)))

    @classmethod
    def knock(cls, mark, *args):
        if cls.__stack.pop():
            cls.__ip = cls.__code.index(mark)

    @classmethod
    def beat(cls, mark, *args):
        cls.__ip = cls.__code.index(mark)

    @classmethod
    def get_opcodes(cls):
        return {
            "slapshot": cls.slapshot,
            "backslap": cls.backslap,
            "slap": cls.slap,
            "unslap": cls.unslap,
            "multislap": cls.multislap,
            "multiunslap": cls.multiunslap,
            "slapscreen": cls.slapscreen,
            "slapput": cls.slapput,
            "knock": cls.knock,
            "beat": cls.beat,
            "plopin": cls.plop_in,
            "punches": cls.punches,
            "nonsmack": cls.nonsmack
        }