class Formula:
    def __init__(self, formula, *args):
        self.formula: str = formula
        self.args = args

    def calc(self, *args):
        if len(self.args) != len(args):
            raise ValueError()
        for n in range(len(self.args)):
            exec(f"{self.args[n]} = {args[n]}")
        ans = eval(self.formula)
        return ans

    def getargs(self):
        return self.args


_f = Formula("x**2 + 4 * x + 4", "x")


# print(_f.calc(4))


class Limit:
    def __init__(self, min_limit, value, max_limit, mode_min="e", mode_max="e"):
        self.min = min_limit
        self.mode_min = mode_min
        self.value = value
        self.mode_max = mode_max
        self.max = max_limit
        if self.max < self.min:
            raise ValueError()
        if not (self.mode_min == "n" or self.mode_min == "e"):
            raise ValueError()
        if not (self.mode_max == "n" or self.mode_max == "e"):
            raise ValueError()

    def getvalue(self):
        return self.value

    def check(self, value, num):
        if value != self.value:
            raise ValueError()
        if self.max == "infinity":
            if self.min == "infinity":
                return True
            else:
                if self.mode_min == "e":
                    return self.min <= num
                else:
                    return self.min < num
        else:
            if self.min == "infinity":
                if self.mode_max == "e":
                    return self.max > num
                else:
                    return self.max >= num
            else:
                if self.mode_max == "e":
                    if self.max >= num:
                        if self.mode_min == "e":
                            return self.min <= num
                        else:
                            return self.min < num
                    else:
                        return False
                else:
                    if self.max > num:
                        if self.mode_min == "e":
                            return self.min <= num
                        else:
                            return self.min < num
                    else:
                        return False


_range1 = Limit(2, "x", 10)


# print(_range1.check("x", 1))


class LimitedFormula:
    def __init__(self, formula, *limits):
        self.formula: formula = formula
        self.limits = limits

    def calc(self, *args):
        for i in range(len(self.limits)):
            if not self.limits[i].check(self.formula.args[i], args[i]):
                return None
        ans = self.formula.calc(*args)
        return ans

    def getargs(self):
        return self.formula.getargs()


_g = LimitedFormula(_f, Limit(2, "x", 5))
print(_g.calc(1))


class Formulas:
    def __init__(self, *formulas):
        """*formulasはFormulaでもLimitedFormulaでも可"""
        self.formulas = list(formulas)
        for k in range(len(self.formulas)):
            if type(self.formulas[k]) == Formula:
                self.formulas[k] = LimitedFormula(self.formulas[k],
                                                  Limit("infinity", self.formulas[k].getargs(), "infinity"))
        self.formulas = tuple(self.formulas)

    def calc(self, *args):
        anses = []
        for m in range(len(self.formulas)):
            anses.append = self.formulas[m].calc(*args)


_fs = Formulas(_f, _g)
_fs.calc(4)
