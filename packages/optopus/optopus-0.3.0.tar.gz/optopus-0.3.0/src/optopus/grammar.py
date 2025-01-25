
'''

Status:

    - Able to lex/parse the README examples to an AST.
    - Looks good so far after some moderately thorough verification.

TODO:

    - Convert grammar-syntax AST into a Grammar.

'''

####
# Imports.
####

import attr
import re
from short_con import cons, constants
import inspect
from functools import cache
from collections import OrderedDict

from .errors import OptopusError

def attrcls(*names):
    # Takes attribute names as list or space-delimited string.
    # Returns a class decorator that will add attributes
    # to the given class. Invoke this decorator so that it
    # executes before @attr.s().
    names = tuple(nm for name in names for nm in name.split())

    def decorator(cls):
        for nm in names:
            setattr(cls, nm, attr.ib())
        return cls

    return decorator

####
# Data classes.
####

@attr.s(frozen = True)
@attrcls('kind regex modes emit')
class TokDef:
    pass

@attr.s(frozen = True)
@attrcls('kind text m width pos line col nlines isfirst indent newlines')
class Token:

    def isa(self, *tds):
        return any(self.kind == td.kind for td in tds)

@attr.s(frozen = True)
@attrcls('name')
class Prog:
    pass

@attr.s(frozen = True)
@attrcls('name is_partial elems')
class Variant:
    pass

@attr.s(frozen = True)
@attrcls('elems text')
class OptHelp:
    pass

@attr.s(frozen = True)
@attrcls('title')
class SectionTitle:
    pass

@attr.s(frozen = True)
@attrcls('text')
class QuotedBlock:
    pass

@attr.s(frozen = True)
@attrcls('text')
class QuotedLiteral:
    pass

@attr.s(frozen = True)
@attrcls('name')
class PartialUsage:
    pass

@attr.s(frozen = True)
@attrcls('elems quantifier')
class Parenthesized:
    pass

@attr.s(frozen = True)
@attrcls('elems quantifier')
class Bracketed:
    pass

@attr.s(frozen = True)
@attrcls('sym dest symlit val vals')
class SymDest:
    pass

@attr.s(frozen = True)
@attrcls('sym dest symlit choices quantifier')
class Positional:
    pass

@attr.s(frozen = True)
@attrcls('dest params quantifier')
class Option:
    pass

@attr.s(frozen = True)
@attrcls('')
class ChoiceSep:
    pass

@attr.s(frozen = True)
@attrcls('m n greedy')
class Quantifier:
    pass

@attr.s(frozen = True)
@attrcls('sym dest symlit choice')
class PositionalVariant:
    pass

@attr.s(frozen = True)
@attrcls('sym dest symlit choices')
class Parameter:
    pass

@attr.s(frozen = True)
@attrcls('sym dest symlit choice')
class ParameterVariant:
    pass

@attr.s(frozen = True)
@attrcls('elems')
class Grammar:
    pass

    @staticmethod
    def pp(elem, level = 0):
        lines = []
        indent = '    '
        add = lambda lev, s: lines.append(indent * lev + s)
        add(level, elem.__class__.__name__ + '(')
        special = ('elems', 'params')
        for k, v in elem.__dict__.items():
            if k not in special:
                add(level + 1, '{} = {!r}'.format(k, v))
        for k in special:
            for e in getattr(elem, k, []):
                lines.extend(Grammar.pp(e, level + 1))
        return lines

####
# Functions to return constants collections.
####

@cache
def define_regex_snippets():
    hws0 = r'[ \t]*'
    hws1 = r'[ \t]+'
    name = r'\w+(?:[_-]\w+)*'
    num = r'\d+'
    q = hws0 + ',' + hws0
    return cons(
        hws0   = hws0,
        hws1   = hws1,
        name   = name,
        num    = num,
        q      = q,
        prog   = name + r'(?:\.\w+)?',
        eol    = hws0 + r'(?=\n)',
        bq     = r'(?<!\\)`',
        bq3    = r'(?<!\\)```',
        pre    = '-',
        quant  = hws0 + '|'.join((num + q + num, num + q, q + num, num, q)) + hws0,
        quoted = r'[\s\S]*?',
        head   = '(?m)^',
    )

@cache
def define_tokdefs():
    # Helper to wrap a regex elem in a capture.
    c = lambda s: '(' + s + ')'

    # Convenience vars.
    r = Snippets
    hw = r.hws0
    cnm = c(r.name)

    # Tuples to define TokDef instances.
    tups = (
        # Kind             Emit  Modes    Pattern
        # - Quoted.
        ('quoted_block',   1,    '  s ',  r.bq3 + c(r.quoted) + r.bq3),
        ('quoted_literal', 1,    'vos ',  r.bq + c(r.quoted) + r.bq),
        # - Whitespace.
        ('newline',        0.0,  'vosh',  r'\n'),
        ('indent',         0.0,  'vosh',  r.head + r.hws1 + r'(?=\S)'),
        ('whitespace',     0.0,  'vosh',  r.hws1),
        # - Sections.
        ('section_name',   1,    'v   ',  c(r.prog) + hw + '::' + r.eol),
        ('section_title',  1,    'vos ',  c('.*') + '::' + r.eol),
        # - Parens.
        ('paren_open',     1,    'vos ',  r'\('),
        ('paren_close',    1,    'vos ',  r'\)'),
        ('brack_open',     1,    'vos ',  r'\['),
        ('brack_close',    1,    'vos ',  r'\]'),
        ('angle_open',     1,    'vos ',  '<'),
        ('angle_close',    1,    'vos ',  '>'),
        # - Quants.
        ('quant_range',    1,    'vos ',  r'\{' + c(r.quant) + r'\}'),
        ('triple_dot',     1,    'vos ',  r'\.\.\.'),
        ('question',       1,    'vos ',  r'\?'),
        # - Separators.
        ('choice_sep',     1,    'vos ',  r'\|'),
        ('assign',         1,    'vos ',  '='),
        ('opt_help_sep',   1,    ' os ',  ':'),
        # - Options.
        ('long_option',    1,    'vos ',  r.pre + r.pre + cnm),
        ('short_option',   1,    'vos ',  r.pre + c(r'\w')),
        # - Variants.
        ('partial_def',    1,    'v   ',  cnm + '!' + hw + ':'),
        ('variant_def',    1,    'v   ',  cnm + hw + ':'),
        ('partial_usage',  1,    'v   ',  cnm + '!'),
        # - Sym, dest.
        ('sym_dest',       1,    'vos ',  cnm + hw + c('[!.]') + hw + cnm),
        ('dot_dest',       1,    'vos ',  r'\.' + hw + cnm),
        ('solo_dest',      1,    'vos ',  cnm + hw + r'(?=[>=])'),
        ('name',           1,    'vos ',  r.name),
        # - Special.
        ('rest_of_line',   1,    '   h',  '.+'),
        ('eof',            0.0,  '    ',  ''),
        ('err',            0.0,  '    ',  ''),
    )

    # Parser modes.
    pms = dict(
        v = Pmodes.variant,
        o = Pmodes.opt_help,
        s = Pmodes.section,
        h = Pmodes.help_text,
    )

    # Create a dict mapping kind to each TokDef.
    tds = OrderedDict()
    for kind, emit, ms, patt in tups:
        tds[kind] = TokDef(
            kind = kind,
            regex = re.compile(patt),
            modes = tuple(pms[m] for m in ms if m != Chars.space),
            emit = bool(emit),
        )

    # Return them as a constants collection.
    return constants(tds)

####
# Parsing and grammar constants.
####

Chars = cons(
    space = ' ',
    newline = '\n',
    exclamation = '!',
    comma = ',',
)

Pmodes = cons('variant opt_help section help_text')
Snippets = define_regex_snippets()
TokDefs = define_tokdefs()

ParenPairs = {
    TokDefs.paren_open: TokDefs.paren_close,
    TokDefs.brack_open: TokDefs.brack_close,
    TokDefs.angle_open: TokDefs.angle_close,
}

Debug = cons(
    emit = False,
)

####
# Lexer.
####

class RegexLexer(object):

    def __init__(self, text, validator, tokdefs = None):
        # Inputs:
        # - Text to be lexxed.
        # - Validator function from parser to validate tokens.
        # - TokDefs currently of interest.
        self.text = text
        self.validator = validator
        self.tokdefs = tokdefs

        # Current token and final token, that latter to be set
        # with Token(eof)/Token(err) when lexing finishes.
        self.curr = None
        self.end = None

        # Location and token information:
        # - pos: character index
        # - line: line number
        # - col: column number
        # - indent: width of most recently read Token(indent).
        # - isfirst: True if next Token is first on line, after any indent.
        self.maxpos = len(self.text) - 1
        self.pos = 0
        self.line = 1
        self.col = 1
        self.indent = 0
        self.isfirst = True

    @property
    def tokdefs(self):
        return self._tokdefs

    @tokdefs.setter
    def tokdefs(self, tokdefs):
        # If TokDefs are changed, clear any cached Token.
        self._tokdefs = tokdefs
        self.curr = None

    def get_next_token(self):
        # Return if we are already done lexing.
        if self.end:
            return self.end

        # Get the next token, either from self.curr or the matcher.
        if self.curr:
            tok = self.curr
            self.curr = None
        else:
            tok = self.match_token()

        # If we got a Token, return either the token or None --
        # the latter if the parser is not happy with it.
        if tok:
            debug(2, lexed = tok.kind)
            if self.validator(tok):
                self.update_location(tok)
                self.curr = None
                debug(2, returned = tok.kind)
                return tok
            else:
                self.curr = tok
                return None

        # And if we didn't get a token, we have lexed as far as
        # we can. Set the end token and return it.
        td = (TokDefs.err, TokDefs.eof)[self.pos > self.maxpos]
        m = re.search('^$', '')
        tok = self.create_token(td, m)
        self.curr = None
        self.end = tok
        self.update_location(tok)
        return tok

    def match_token(self):
        # Starting at self.pos, reutn the next Token.
        #
        # For non-emitted tokens, we break out of the for-loop,
        # but enter the while-loop again. This allows the lexer
        # to be able to ignore any number of non-emitted tokens
        # on each call of the function.
        tok = True
        while tok:
            tok = None
            for td in self.tokdefs:
                m = td.regex.match(self.text, pos = self.pos)
                if m:
                    tok = self.create_token(td, m)
                    if td.emit:
                        return tok
                    else:
                        self.update_location(tok)
                        break
        return None

    def create_token(self, tokdef, m):
        # Helper to create Token from a TokDef and a regex Match.
        text = m.group(0)
        newlines = tuple(
            i for i, c in enumerate(text)
            if c == Chars.newline
        )
        return Token(
            kind = tokdef.kind,
            text = text,
            m = m,
            width = len(text),
            pos = self.pos,
            line = self.line,
            col = self.col,
            nlines = len(newlines) + 1,
            isfirst = self.isfirst,
            indent = self.indent,
            newlines = newlines,
        )

    def update_location(self, tok):
        # Update the lexer's position-related info, given that
        # the parser has accepted the Token.
        #
        # New column location when newlines present:
        #
        #     tok.text      | tok.width | tok.newlines | self.col
        #     ---------------------------------------------------
        #     \n            | 1         | (0,)         | 1
        #     fubb\n        | 5         | (4,)         | 1
        #     fubb\nbar     | 8         | (4,)         | 4
        #     fubb\nbar\n   | 9         | (4,8)        | 1
        #     fubb\nbar\nxy | 11        | (4,8)        | 3
        #
        self.pos += tok.width
        self.line += tok.nlines - 1
        self.col = (
            tok.width - tok.newlines[-1] if tok.newlines
            else self.col + tok.width
        )

        # Update indent-related info.
        if tok.isa(TokDefs.newline):
            self.indent = 0
            self.isfirst = True
        elif tok.isa(TokDefs.indent):
            self.indent = tok.width
            self.isfirst = True
        else:
            self.isfirst = False

####
# SpecParser.
####

@attr.s(frozen = True)
class Handler:
    method = attr.ib()
    next_mode = attr.ib()

class SpecParser:

    def __init__(self, text):
        # The text and the lexer.
        self.text = text
        self.lexer = RegexLexer(text, self.taste)

        # Line and indent from the first Token of the top-level
        # ParseElem currently under construction by the parser.
        # And a flag for special indent validation.
        self.line = None
        self.indent = None
        self.allow_second = False

        # Parsing modes. First define the handlers for each mode.
        # Then set the initial mode.
        self.handlers = {
            Pmodes.variant: (
                Handler(self.section_title, Pmodes.section),
                Handler(self.variant, None),
            ),
            Pmodes.opt_help: (
                Handler(self.section_title, Pmodes.section),
                Handler(self.opt_help, None),
            ),
            Pmodes.section: (
                Handler(self.quoted_block, None),
                Handler(self.section_title, None),
                Handler(self.opt_help, None),
            ),
            Pmodes.help_text: tuple(),
        }
        self.mode = Pmodes.variant

        # Tokens the parser has ever eaten and TokDefs
        # it is currently trying to eat.
        self.eaten = []
        self.menu = None

    ####
    # Setting the parser mode.
    ####

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        self._mode = mode
        self.lexer.tokdefs = tuple(
            td for td in TokDefs.values()
            if mode in td.modes
        )

    ####
    # Parse a spec.
    ####

    def parse(self):
        # Determine the parsing mode for the grammar section
        # (opt_help or variant), and get the program name, if any.
        # Because the first variant can reside on the same line as
        # the program name, we set the allow_second flag.
        debug(0)
        debug(0, mode_check = 'started')
        tok = self.eat(TokDefs.section_name)
        if tok:
            self.mode = Pmodes.opt_help
            prog = tok.m.group(1)
            allow_second = False
        else:
            self.mode = Pmodes.variant
            tok = self.eat(TokDefs.name)
            prog = tok.text if tok else None
            allow_second = bool(tok)
        debug(0, mode = self.mode)

        # Parse everything into a list of ParseElem.
        elems = list(self.do_parse(allow_second))

        # Raise if we did not parse the full text.
        tok = self.lexer.end
        if not (tok and tok.isa(TokDefs.eof)):
            self.error('Failed to parse the full spec')

        # Convert elems to a Grammar.
        return self.build_grammar(prog, elems)

    def do_parse(self, allow_second):
        # Yields top-level ParseElem (those declared in self.handlers).

        # The first OptHelp or SectionTitle must start on new line.
        # That differs from the first Variant, which is allowed
        # to immediately follow the program name, if any.

        self.indent = None
        self.line = None
        self.allow_second = allow_second

        # Emit all ParseElem that we find.
        elem = True
        while elem:
            elem = False
            # Try the handlers until one succeeds. When that occurs,
            # we break from the loop and then re-enter it. If no handlers
            # succeed, we will exit the outer loop.
            for h in self.handlers[self.mode]:
                debug(0, handler = h.method.__name__)
                elem = h.method()
                if elem:
                    yield elem
                    # Every subsequent top-level ParseElem must start on a fresh line.
                    self.indent = None
                    self.line = None
                    self.allow_second = False
                    # Advance parser mode, if needed.
                    if h.next_mode:
                        self.mode = h.next_mode
                    break

    def build_grammar(self, prog, elems):
        g = Grammar(elems)

        return g

        '''

        Partition elems on the first SectionTitle:

            gelems : grammar section (all Variant or OptHelp)
            selems : other

        Convert selems into groups, one per section:

            SectionTitle
            0+ QuotedBlock
            0+ OptHelp        # Can be full or mere references.

        At this point, we will have:

            prog : name or None
            variants : 0+
            opthelps : 0+
            sections : 0+

        If no variants:
            If no opthelps:
                - No-config parsing?
                - Or raise?
            Else:
                - Create one Variant from the opthelps.

        Processing a sequence of elems:

            - Applies to Variant, Parenthesized, Bracketed.

            - Organize into groups, partitioning on ChoiceSep.
            - If multiple groups, we will end up with Group(mutext=True)

            ...

        Sections:
            - An ordered list of section-elems.
            - Where each section-elem is: QuotedBlock or Opt-reference.

        '''

        # ParseElem: top-level:
        #     Variant: name is_partial elems
        #     OptHelp: elems text
        #     SectionTitle: title
        #     QuotedBlock: text
        #
        # ParseElem: elems:
        #     ChoiceSep:
        #     QuotedLiteral: text
        #         - Becomes an Opt.
        #         - But has no dest.
        #         - Essentially requires the variant to include a positional constant.
        #         - Does that make it like a PositionalVariant with one choice and no dest or sym?
        #     PartialUsage: name
        #         - Insert the elems from the Variant(partial=True)
        #     Parenthesized: elems quantifier
        #         - Convert to Group or quantified Opt.
        #     Bracketed: elems quantifier
        #         - Convert to Group or quantified Opt.
        #     Option: dest params quantifier
        #     Positional: sym dest symlit choices quantifier
        #     PositionalVariant: sym dest symlit choice
        #     Parameter: sym dest symlit choices
        #     ParameterVariant: sym dest symlit choice
        #
        # ParseElem: subcomponents:
        #     SymDest: sym dest symlit val vals
        #     Quantifier: m n greedy
        #     QuotedLiteral: text

    ####
    # Eat tokens.
    ####

    def eat(self, *tds):
        self.menu = tds
        debug(1, wanted = ','.join(td.kind for td in tds))
        tok = self.lexer.get_next_token()
        if tok is None:
            return None
        elif tok.isa(TokDefs.eof, TokDefs.err):
            return None
        else:
            debug(
                2,
                eaten = tok.kind,
                text = tok.text,
                pos = tok.pos,
                line = tok.line,
                col = tok.col,
            )
            self.eaten.append(tok)
            return tok

    def taste(self, tok):
        # Returns true if the next token from the lexer is the
        # right kind, based on last eat() call, and if it adheres
        # to rules regarding indentation and start-of-line status.
        #
        # - If SpecParser has no indent yet, we are starting a new
        #   top-level ParseElem. So we expect a first-of-line Token.
        #   If so, we remember that token's indent and line.
        #
        # - For subsequent tokens in the expression, we expect tokens
        #   from the same line or a continuation line indented farther
        #   than the first line of the expression.
        #
        if any(tok.isa(td) for td in self.menu):
            if self.indent is None:
                if tok.isfirst or self.allow_second:
                    debug(2, isfirst = True)
                    # HERE_INDENT
                    self.indent = tok.indent
                    self.line = tok.line
                    return True
                else:
                    debug(2, isfirst = False)
                    return False
            else:
                if self.line == tok.line:
                    debug(2, indent_ok = 'line', line = self.line)
                    return True
                elif self.indent < tok.indent:
                    debug(2, indent_ok = 'indent', self_indent = self.indent, tok_indent = tok.indent)
                    # HERE_INDENT
                    # self.line = tok.line
                    return True
                else:
                    debug(2, indent_ok = False, self_indent = self.indent, tok_indent = tok.indent)
                    return False
        else:
            # debug(2, kind = False)
            return False

    ####
    # Top-level ParseElem handlers.
    ####

    def variant(self):
        # Get variant/partial name, if any.
        tds = (TokDefs.variant_def, TokDefs.partial_def)
        tok = self.eat(*tds)
        if tok:
            name = tok.text
            is_partial = tok.isa(TokDefs.partial_def)
        else:
            name = None
            is_partial = False

        # Collect the ParseElem for the variant.
        elems = self.elems()
        if name is None and not elems:
            return None
        elif elems:
            return Variant(name, is_partial, elems)
        else:
            self.error('A Variant cannot be empty')

    def opt_help(self):
        # Try to get elements.
        elems = self.elems()
        if not elems:
            return None

        # Try to get the Opt help text and any continuation lines.
        texts = []
        if self.eat(TokDefs.opt_help_sep):
            self.mode = Pmodes.help_text
            while True:
                tok = self.eat(TokDefs.rest_of_line)
                if tok:
                    texts.append(tok.text.strip())
                else:
                    break
            self.mode = Pmodes.opt_help

        # Join text parts and return.
        text = Chars.space.join(t for t in texts if t)
        return OptHelp(elems, text)

    def section_title(self):
        tok = self.eat(TokDefs.section_title, TokDefs.section_name)
        if tok:
            return SectionTitle(title = tok.m.group(1).strip())
        else:
            return None

    def quoted_block(self):
        tok = self.eat(TokDefs.quoted_block)
        if tok:
            return QuotedBlock(text = tok.m.group(1))
        else:
            return None

    ####
    # ParseElem obtained via the elems() helper.
    ####

    def elems(self):
        elems = []
        takes_quantifier = (Parenthesized, Bracketed, Positional, Option)
        while True:
            e = self.parse_first(
                self.quoted_literal,
                self.choice_sep,
                self.partial_usage,
                self.paren_expression,
                self.brack_expression,
                self.positional,
                self.long_option,
                self.short_option,
            )
            if e and isinstance(e, takes_quantifier):
                q = self.quantifier()
                if q:
                    e = attr.evolve(e, quantifier = q)
                elems.append(e)
            elif e:
                elems.append(e)
            else:
                break
        return elems

    def choice_sep(self):
        tok = self.eat(TokDefs.choice_sep)
        if tok:
            return ChoiceSep()
        else:
            return None

    def quoted_literal(self):
        tok = self.eat(TokDefs.quoted_literal)
        if tok:
            return QuotedLiteral(text = tok.m.group(1))
        else:
            return None

    def partial_usage(self):
        tok = self.eat(TokDefs.partial_usage)
        if tok:
            return PartialUsage(name = tok.m.group(1))
        else:
            return None

    def paren_expression(self):
        elems = self.parenthesized(TokDefs.paren_open, self.elems)
        if elems:
            return Parenthesized(elems, None)
        else:
            return None

    def brack_expression(self):
        elems = self.parenthesized(TokDefs.brack_open, self.elems)
        if elems:
            return Bracketed(elems, None)
        else:
            return None

    def long_option(self):
        return self.option(TokDefs.long_option)

    def short_option(self):
        return self.option(TokDefs.short_option)

    def option(self, tokdef):
        tok = self.eat(tokdef)
        if tok:
            dest = tok.m.group(1)
            params = self.parse_some(self.parameter)
            return Option(dest, params, None)
        else:
            return None

    def positional(self):
        # Try to get a SymDest elem.
        sd = self.parenthesized(TokDefs.angle_open, self.symdest, for_pos = True)
        if not sd:
            return None

        # Return Positional or PositionalVariant.
        xs = (sd.sym, sd.dest, sd.symlit)
        if sd.val is None:
            return Positional(*xs, choices = sd.vals, quantifier = None)
        else:
            return PositionalVariant(*xs, choice = sd.val)

    def parameter(self):
        # Try to get a SymDest elem.
        sd = self.parenthesized(TokDefs.angle_open, self.symdest, empty_ok = True)
        if not sd:
            return None

        # Return Parameter or ParameterVariant.
        xs = (sd.sym, sd.dest, sd.symlit)
        if sd.val is None:
            return Parameter(*xs, choices = sd.vals)
        else:
            return ParameterVariant(*xs, choice = sd.val)

    def symdest(self, for_pos = False):
        # Try to get sym.dest portion.
        sym = None
        dest = None
        symlit = False
        tok = self.eat(TokDefs.sym_dest, TokDefs.dot_dest, TokDefs.solo_dest)
        if tok:
            if tok.isa(TokDefs.sym_dest):
                # Handle <sym.dest> or <sym!dest>.
                sym = tok.m.group(1)
                symlit = tok.m.group(2) == Chars.exclamation
                dest = tok.m.group(3)
            else:
                # Handle <.dest>, <dest>, <dest=> or <sym>.
                txt = tok.m.group(1)
                if for_pos or tok.isa(TokDefs.dot_dest):
                    dest = txt
                else:
                    sym = txt
        elif for_pos:
            self.error('Positionals require at least a dest')

        # Try to get the dest assign equal-sign.
        # For now, treat this as optional.
        assign = self.eat(TokDefs.assign)

        # Try to get choice values.
        vals = []
        tds = (TokDefs.quoted_literal, TokDefs.name, TokDefs.solo_dest)
        while True:
            tok = self.eat(*tds)
            if not tok:
                break

            # If we got one, and if we already had a sym or dest,
            # the assign equal sign becomes required.
            if (sym or dest) and not assign:
                self.error('Found choice values without required equal sign')

            # Consume and store.
            i = 0 if tok.isa(TokDefs.name) else 1
            vals.append(tok.m.group(i))

            # Continue looping if choice_sep is next.
            if not self.eat(TokDefs.choice_sep):
                break

        # Handle single choice value.
        if len(vals) == 1:
            val = vals[0]
            vals = None
        else:
            val = None
            vals = tuple(vals)

        # Return.
        return SymDest(sym, dest, symlit, val, vals)

    def quantifier(self):
        q = self.parse_first(self.triple_dot, self.quantifier_range)
        if q:
            m, n = q
            greedy = not self.eat(TokDefs.question)
            return Quantifier(m, n, greedy)
        elif self.eat(TokDefs.question):
            return Quantifier(None, None, False)
        else:
            return None

    def triple_dot(self):
        tok = self.eat(TokDefs.triple_dot)
        return (1, None) if tok else None

    def quantifier_range(self):
        tok = self.eat(TokDefs.quant_range)
        if tok:
            text = TokDefs.whitespace.regex.sub('', tok.m.group(1))
            xs = [
                None if x == '' else int(x)
                for x in text.split(Chars.comma)
            ]
            if len(xs) == 1:
                return (xs[0], xs[0])
            else:
                return (xs[0], xs[1])
        else:
            return None

    def parenthesized(self, td_open, method, empty_ok = False, **kws):
        td_close = ParenPairs[td_open]
        tok = self.eat(td_open)
        if tok:
            elem = method(**kws)
            if not (elem or empty_ok):
                self.error('Empty parenthesized expression')
            elif self.eat(td_close):
                return elem
            else:
                self.error(
                    msg = 'Failed to find closing paren/bracket',
                    expected = td_close,
                )
        else:
            return None

    ####
    # Other stuff.
    ####

    def error(self, msg, **kws):
        lex = self.lexer
        kws.update(
            msg = msg,
            pos = lex.pos,
            line = lex.line,
            col = lex.col,
            current_token = lex.curr.kind if lex.curr else None,
        )
        raise OptopusError(**kws)

    def parse_first(self, *methods):
        elem = None
        for m in methods:
            elem = m()
            if elem:
                break
        return elem

    def parse_some(self, method):
        elems = []
        while True:
            e = method()
            if e:
                elems.append(e)
            else:
                break
        return elems

def get_caller_name(offset = 2):
    # Get the name of a calling function.
    x = inspect.currentframe()
    for _ in range(offset):
        x = x.f_back
    x = x.f_code.co_name
    return x

def debug(indent, **kws):
    if Debug.emit:
        msg = ''
        if kws:
            func = get_caller_name()
            gen = ('{} = {!r}'.format(k, v) for k, v in kws.items())
            msg = '{}{}({})'.format(
                Chars.space * (indent * 4),
                func,
                ', '.join(gen)
            )
        print(msg)

