# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 final_09_01-13/Monitor.g 2013-01-15 13:09:44

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__68=68
T__69=69
ATKW=42
RESV=12
LETTER=65
PACKAGEKW=30
CHOICEKW=41
ASSERTION=58
CATCHESKW=55
PARALLEL=19
DO=26
DOKW=51
ABSTRACT=28
ID=56
EOF=-1
PROTOCOL=20
ROLEKW=36
TYPE=14
TOKW=40
INSTANTIATESKW=38
ML_COMMENT=62
INTERACTION=4
ROLES=24
ASKW=52
WITHKW=49
EXTID=57
THROWSKW=54
ANDKW=47
FULLSTOP=11
CONTINUEKW=45
PLUS=7
SEND=13
FULLNAME=29
DIGIT=60
INTR=25
T__80=80
FROMKW=39
T__81=81
T__82=82
SYMBOL=67
T__83=83
LINE_COMMENT=63
INTERRUPTIBLEKW=48
PARALLELKW=46
RECLABEL=18
NUMBER=59
WHITESPACE=61
UNDERSCORE=66
TYPEKW=32
INT=5
RECKW=44
SIGKW=37
MINUS=8
MULT=9
VALUE=15
T__84=84
ASSERT=21
BYKW=50
ORKW=43
IMPORTKW=31
UNORDERED=17
PARAMETERLIST=27
EMPTY=23
StringLiteral=64
T__71=71
T__72=72
GLOBAL_ESCAPE=22
PROTOCOLKW=33
T__70=70
BRANCH=16
LOCALKW=35
GLOBALKW=34
DIV=10
T__76=76
SPAWNKW=53
T__75=75
T__74=74
T__73=73
T__79=79
T__78=78
STRING=6
T__77=77

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "INTERACTION", "INT", "STRING", "PLUS", "MINUS", "MULT", "DIV", "FULLSTOP", 
    "RESV", "SEND", "TYPE", "VALUE", "BRANCH", "UNORDERED", "RECLABEL", 
    "PARALLEL", "PROTOCOL", "ASSERT", "GLOBAL_ESCAPE", "EMPTY", "ROLES", 
    "INTR", "DO", "PARAMETERLIST", "ABSTRACT", "FULLNAME", "PACKAGEKW", 
    "IMPORTKW", "TYPEKW", "PROTOCOLKW", "GLOBALKW", "LOCALKW", "ROLEKW", 
    "SIGKW", "INSTANTIATESKW", "FROMKW", "TOKW", "CHOICEKW", "ATKW", "ORKW", 
    "RECKW", "CONTINUEKW", "PARALLELKW", "ANDKW", "INTERRUPTIBLEKW", "WITHKW", 
    "BYKW", "DOKW", "ASKW", "SPAWNKW", "THROWSKW", "CATCHESKW", "ID", "EXTID", 
    "ASSERTION", "NUMBER", "DIGIT", "WHITESPACE", "ML_COMMENT", "LINE_COMMENT", 
    "StringLiteral", "LETTER", "UNDERSCORE", "SYMBOL", "';'", "'<'", "'>'", 
    "','", "'{'", "'}'", "'('", "')'", "'introduces'", "':'", "'repeat'", 
    "'end'", "'run'", "'inline'", "'throw'", "'catch'", "'unordered'"
]




class MonitorParser(Parser):
    grammarFileName = "final_09_01-13/Monitor.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(MonitorParser, self).__init__(input, state, *args, **kwargs)

        self.dfa1 = self.DFA1(
            self, 1,
            eot = self.DFA1_eot,
            eof = self.DFA1_eof,
            min = self.DFA1_min,
            max = self.DFA1_max,
            accept = self.DFA1_accept,
            special = self.DFA1_special,
            transition = self.DFA1_transition
            )

        self.dfa6 = self.DFA6(
            self, 6,
            eot = self.DFA6_eot,
            eof = self.DFA6_eof,
            min = self.DFA6_min,
            max = self.DFA6_max,
            accept = self.DFA6_accept,
            special = self.DFA6_special,
            transition = self.DFA6_transition
            )

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )

        self.dfa29 = self.DFA29(
            self, 29,
            eot = self.DFA29_eot,
            eof = self.DFA29_eof,
            min = self.DFA29_min,
            max = self.DFA29_max,
            accept = self.DFA29_accept,
            special = self.DFA29_special,
            transition = self.DFA29_transition
            )






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class module_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.module_return, self).__init__()

            self.tree = None




    # $ANTLR start "module"
    # final_09_01-13/Monitor.g:78:1: module : packagedecl ( importdecl )* ( payloadtypedecl )* ( protocolDef )* ;
    def module(self, ):

        retval = self.module_return()
        retval.start = self.input.LT(1)

        root_0 = None

        packagedecl1 = None

        importdecl2 = None

        payloadtypedecl3 = None

        protocolDef4 = None



        try:
            try:
                # final_09_01-13/Monitor.g:78:7: ( packagedecl ( importdecl )* ( payloadtypedecl )* ( protocolDef )* )
                # final_09_01-13/Monitor.g:78:9: packagedecl ( importdecl )* ( payloadtypedecl )* ( protocolDef )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_packagedecl_in_module506)
                packagedecl1 = self.packagedecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, packagedecl1.tree)
                # final_09_01-13/Monitor.g:78:21: ( importdecl )*
                while True: #loop1
                    alt1 = 2
                    alt1 = self.dfa1.predict(self.input)
                    if alt1 == 1:
                        # final_09_01-13/Monitor.g:78:22: importdecl
                        pass 
                        self._state.following.append(self.FOLLOW_importdecl_in_module509)
                        importdecl2 = self.importdecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, importdecl2.tree)


                    else:
                        break #loop1
                # final_09_01-13/Monitor.g:78:35: ( payloadtypedecl )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == TYPEKW) :
                        alt2 = 1


                    if alt2 == 1:
                        # final_09_01-13/Monitor.g:78:36: payloadtypedecl
                        pass 
                        self._state.following.append(self.FOLLOW_payloadtypedecl_in_module514)
                        payloadtypedecl3 = self.payloadtypedecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, payloadtypedecl3.tree)


                    else:
                        break #loop2
                # final_09_01-13/Monitor.g:78:54: ( protocolDef )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == LOCALKW) :
                        LA3_1 = self.input.LA(2)

                        if (self.synpred3_Monitor()) :
                            alt3 = 1




                    if alt3 == 1:
                        # final_09_01-13/Monitor.g:78:55: protocolDef
                        pass 
                        self._state.following.append(self.FOLLOW_protocolDef_in_module519)
                        protocolDef4 = self.protocolDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, protocolDef4.tree)


                    else:
                        break #loop3



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "module"

    class packagedecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.packagedecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "packagedecl"
    # final_09_01-13/Monitor.g:79:1: packagedecl : PACKAGEKW packagename ';' ;
    def packagedecl(self, ):

        retval = self.packagedecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PACKAGEKW5 = None
        char_literal7 = None
        packagename6 = None


        PACKAGEKW5_tree = None
        char_literal7_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:79:12: ( PACKAGEKW packagename ';' )
                # final_09_01-13/Monitor.g:79:14: PACKAGEKW packagename ';'
                pass 
                root_0 = self._adaptor.nil()

                PACKAGEKW5=self.match(self.input, PACKAGEKW, self.FOLLOW_PACKAGEKW_in_packagedecl527)
                if self._state.backtracking == 0:

                    PACKAGEKW5_tree = self._adaptor.createWithPayload(PACKAGEKW5)
                    self._adaptor.addChild(root_0, PACKAGEKW5_tree)

                self._state.following.append(self.FOLLOW_packagename_in_packagedecl529)
                packagename6 = self.packagename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, packagename6.tree)
                char_literal7=self.match(self.input, 68, self.FOLLOW_68_in_packagedecl531)
                if self._state.backtracking == 0:

                    char_literal7_tree = self._adaptor.createWithPayload(char_literal7)
                    self._adaptor.addChild(root_0, char_literal7_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "packagedecl"

    class packagename_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.packagename_return, self).__init__()

            self.tree = None




    # $ANTLR start "packagename"
    # final_09_01-13/Monitor.g:81:1: packagename : ID ( '.' ID )* ;
    def packagename(self, ):

        retval = self.packagename_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID8 = None
        char_literal9 = None
        ID10 = None

        ID8_tree = None
        char_literal9_tree = None
        ID10_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:81:12: ( ID ( '.' ID )* )
                # final_09_01-13/Monitor.g:81:14: ID ( '.' ID )*
                pass 
                root_0 = self._adaptor.nil()

                ID8=self.match(self.input, ID, self.FOLLOW_ID_in_packagename538)
                if self._state.backtracking == 0:

                    ID8_tree = self._adaptor.createWithPayload(ID8)
                    self._adaptor.addChild(root_0, ID8_tree)

                # final_09_01-13/Monitor.g:81:17: ( '.' ID )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == FULLSTOP) :
                        LA4_2 = self.input.LA(2)

                        if (LA4_2 == ID) :
                            LA4_3 = self.input.LA(3)

                            if (LA4_3 == FULLSTOP or LA4_3 == 68) :
                                alt4 = 1






                    if alt4 == 1:
                        # final_09_01-13/Monitor.g:81:18: '.' ID
                        pass 
                        char_literal9=self.match(self.input, FULLSTOP, self.FOLLOW_FULLSTOP_in_packagename541)
                        if self._state.backtracking == 0:

                            char_literal9_tree = self._adaptor.createWithPayload(char_literal9)
                            self._adaptor.addChild(root_0, char_literal9_tree)

                        ID10=self.match(self.input, ID, self.FOLLOW_ID_in_packagename543)
                        if self._state.backtracking == 0:

                            ID10_tree = self._adaptor.createWithPayload(ID10)
                            self._adaptor.addChild(root_0, ID10_tree)



                    else:
                        break #loop4



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "packagename"

    class importdecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.importdecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "importdecl"
    # final_09_01-13/Monitor.g:83:1: importdecl : ( IMPORTKW ID ( '.' ID )* ';' | FROMKW packagename '.' ID IMPORTKW ID ';' | FROMKW packagename '.' ID IMPORTKW ID ASKW ID ';' );
    def importdecl(self, ):

        retval = self.importdecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTKW11 = None
        ID12 = None
        char_literal13 = None
        ID14 = None
        char_literal15 = None
        FROMKW16 = None
        char_literal18 = None
        ID19 = None
        IMPORTKW20 = None
        ID21 = None
        char_literal22 = None
        FROMKW23 = None
        char_literal25 = None
        ID26 = None
        IMPORTKW27 = None
        ID28 = None
        ASKW29 = None
        ID30 = None
        char_literal31 = None
        packagename17 = None

        packagename24 = None


        IMPORTKW11_tree = None
        ID12_tree = None
        char_literal13_tree = None
        ID14_tree = None
        char_literal15_tree = None
        FROMKW16_tree = None
        char_literal18_tree = None
        ID19_tree = None
        IMPORTKW20_tree = None
        ID21_tree = None
        char_literal22_tree = None
        FROMKW23_tree = None
        char_literal25_tree = None
        ID26_tree = None
        IMPORTKW27_tree = None
        ID28_tree = None
        ASKW29_tree = None
        ID30_tree = None
        char_literal31_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:83:11: ( IMPORTKW ID ( '.' ID )* ';' | FROMKW packagename '.' ID IMPORTKW ID ';' | FROMKW packagename '.' ID IMPORTKW ID ASKW ID ';' )
                alt6 = 3
                alt6 = self.dfa6.predict(self.input)
                if alt6 == 1:
                    # final_09_01-13/Monitor.g:83:13: IMPORTKW ID ( '.' ID )* ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    IMPORTKW11=self.match(self.input, IMPORTKW, self.FOLLOW_IMPORTKW_in_importdecl552)
                    if self._state.backtracking == 0:

                        IMPORTKW11_tree = self._adaptor.createWithPayload(IMPORTKW11)
                        self._adaptor.addChild(root_0, IMPORTKW11_tree)

                    ID12=self.match(self.input, ID, self.FOLLOW_ID_in_importdecl554)
                    if self._state.backtracking == 0:

                        ID12_tree = self._adaptor.createWithPayload(ID12)
                        self._adaptor.addChild(root_0, ID12_tree)

                    # final_09_01-13/Monitor.g:83:25: ( '.' ID )*
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == FULLSTOP) :
                            alt5 = 1


                        if alt5 == 1:
                            # final_09_01-13/Monitor.g:83:26: '.' ID
                            pass 
                            char_literal13=self.match(self.input, FULLSTOP, self.FOLLOW_FULLSTOP_in_importdecl557)
                            if self._state.backtracking == 0:

                                char_literal13_tree = self._adaptor.createWithPayload(char_literal13)
                                self._adaptor.addChild(root_0, char_literal13_tree)

                            ID14=self.match(self.input, ID, self.FOLLOW_ID_in_importdecl559)
                            if self._state.backtracking == 0:

                                ID14_tree = self._adaptor.createWithPayload(ID14)
                                self._adaptor.addChild(root_0, ID14_tree)



                        else:
                            break #loop5
                    char_literal15=self.match(self.input, 68, self.FOLLOW_68_in_importdecl563)
                    if self._state.backtracking == 0:

                        char_literal15_tree = self._adaptor.createWithPayload(char_literal15)
                        self._adaptor.addChild(root_0, char_literal15_tree)



                elif alt6 == 2:
                    # final_09_01-13/Monitor.g:84:7: FROMKW packagename '.' ID IMPORTKW ID ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    FROMKW16=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_importdecl572)
                    if self._state.backtracking == 0:

                        FROMKW16_tree = self._adaptor.createWithPayload(FROMKW16)
                        self._adaptor.addChild(root_0, FROMKW16_tree)

                    self._state.following.append(self.FOLLOW_packagename_in_importdecl574)
                    packagename17 = self.packagename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, packagename17.tree)
                    char_literal18=self.match(self.input, FULLSTOP, self.FOLLOW_FULLSTOP_in_importdecl576)
                    if self._state.backtracking == 0:

                        char_literal18_tree = self._adaptor.createWithPayload(char_literal18)
                        self._adaptor.addChild(root_0, char_literal18_tree)

                    ID19=self.match(self.input, ID, self.FOLLOW_ID_in_importdecl578)
                    if self._state.backtracking == 0:

                        ID19_tree = self._adaptor.createWithPayload(ID19)
                        self._adaptor.addChild(root_0, ID19_tree)

                    IMPORTKW20=self.match(self.input, IMPORTKW, self.FOLLOW_IMPORTKW_in_importdecl580)
                    if self._state.backtracking == 0:

                        IMPORTKW20_tree = self._adaptor.createWithPayload(IMPORTKW20)
                        self._adaptor.addChild(root_0, IMPORTKW20_tree)

                    ID21=self.match(self.input, ID, self.FOLLOW_ID_in_importdecl582)
                    if self._state.backtracking == 0:

                        ID21_tree = self._adaptor.createWithPayload(ID21)
                        self._adaptor.addChild(root_0, ID21_tree)

                    char_literal22=self.match(self.input, 68, self.FOLLOW_68_in_importdecl584)
                    if self._state.backtracking == 0:

                        char_literal22_tree = self._adaptor.createWithPayload(char_literal22)
                        self._adaptor.addChild(root_0, char_literal22_tree)



                elif alt6 == 3:
                    # final_09_01-13/Monitor.g:85:7: FROMKW packagename '.' ID IMPORTKW ID ASKW ID ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    FROMKW23=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_importdecl593)
                    if self._state.backtracking == 0:

                        FROMKW23_tree = self._adaptor.createWithPayload(FROMKW23)
                        self._adaptor.addChild(root_0, FROMKW23_tree)

                    self._state.following.append(self.FOLLOW_packagename_in_importdecl595)
                    packagename24 = self.packagename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, packagename24.tree)
                    char_literal25=self.match(self.input, FULLSTOP, self.FOLLOW_FULLSTOP_in_importdecl597)
                    if self._state.backtracking == 0:

                        char_literal25_tree = self._adaptor.createWithPayload(char_literal25)
                        self._adaptor.addChild(root_0, char_literal25_tree)

                    ID26=self.match(self.input, ID, self.FOLLOW_ID_in_importdecl599)
                    if self._state.backtracking == 0:

                        ID26_tree = self._adaptor.createWithPayload(ID26)
                        self._adaptor.addChild(root_0, ID26_tree)

                    IMPORTKW27=self.match(self.input, IMPORTKW, self.FOLLOW_IMPORTKW_in_importdecl601)
                    if self._state.backtracking == 0:

                        IMPORTKW27_tree = self._adaptor.createWithPayload(IMPORTKW27)
                        self._adaptor.addChild(root_0, IMPORTKW27_tree)

                    ID28=self.match(self.input, ID, self.FOLLOW_ID_in_importdecl603)
                    if self._state.backtracking == 0:

                        ID28_tree = self._adaptor.createWithPayload(ID28)
                        self._adaptor.addChild(root_0, ID28_tree)

                    ASKW29=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_importdecl605)
                    if self._state.backtracking == 0:

                        ASKW29_tree = self._adaptor.createWithPayload(ASKW29)
                        self._adaptor.addChild(root_0, ASKW29_tree)

                    ID30=self.match(self.input, ID, self.FOLLOW_ID_in_importdecl607)
                    if self._state.backtracking == 0:

                        ID30_tree = self._adaptor.createWithPayload(ID30)
                        self._adaptor.addChild(root_0, ID30_tree)

                    char_literal31=self.match(self.input, 68, self.FOLLOW_68_in_importdecl609)
                    if self._state.backtracking == 0:

                        char_literal31_tree = self._adaptor.createWithPayload(char_literal31)
                        self._adaptor.addChild(root_0, char_literal31_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "importdecl"

    class payloadtypedecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.payloadtypedecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "payloadtypedecl"
    # final_09_01-13/Monitor.g:88:1: payloadtypedecl : TYPEKW '<' ID '>' EXTID FROMKW EXTID ASKW ID ';' ;
    def payloadtypedecl(self, ):

        retval = self.payloadtypedecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TYPEKW32 = None
        char_literal33 = None
        ID34 = None
        char_literal35 = None
        EXTID36 = None
        FROMKW37 = None
        EXTID38 = None
        ASKW39 = None
        ID40 = None
        char_literal41 = None

        TYPEKW32_tree = None
        char_literal33_tree = None
        ID34_tree = None
        char_literal35_tree = None
        EXTID36_tree = None
        FROMKW37_tree = None
        EXTID38_tree = None
        ASKW39_tree = None
        ID40_tree = None
        char_literal41_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:88:16: ( TYPEKW '<' ID '>' EXTID FROMKW EXTID ASKW ID ';' )
                # final_09_01-13/Monitor.g:88:19: TYPEKW '<' ID '>' EXTID FROMKW EXTID ASKW ID ';'
                pass 
                root_0 = self._adaptor.nil()

                TYPEKW32=self.match(self.input, TYPEKW, self.FOLLOW_TYPEKW_in_payloadtypedecl618)
                if self._state.backtracking == 0:

                    TYPEKW32_tree = self._adaptor.createWithPayload(TYPEKW32)
                    self._adaptor.addChild(root_0, TYPEKW32_tree)

                char_literal33=self.match(self.input, 69, self.FOLLOW_69_in_payloadtypedecl620)
                if self._state.backtracking == 0:

                    char_literal33_tree = self._adaptor.createWithPayload(char_literal33)
                    self._adaptor.addChild(root_0, char_literal33_tree)

                ID34=self.match(self.input, ID, self.FOLLOW_ID_in_payloadtypedecl622)
                if self._state.backtracking == 0:

                    ID34_tree = self._adaptor.createWithPayload(ID34)
                    self._adaptor.addChild(root_0, ID34_tree)

                char_literal35=self.match(self.input, 70, self.FOLLOW_70_in_payloadtypedecl624)
                if self._state.backtracking == 0:

                    char_literal35_tree = self._adaptor.createWithPayload(char_literal35)
                    self._adaptor.addChild(root_0, char_literal35_tree)

                EXTID36=self.match(self.input, EXTID, self.FOLLOW_EXTID_in_payloadtypedecl626)
                if self._state.backtracking == 0:

                    EXTID36_tree = self._adaptor.createWithPayload(EXTID36)
                    self._adaptor.addChild(root_0, EXTID36_tree)

                FROMKW37=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_payloadtypedecl628)
                if self._state.backtracking == 0:

                    FROMKW37_tree = self._adaptor.createWithPayload(FROMKW37)
                    self._adaptor.addChild(root_0, FROMKW37_tree)

                EXTID38=self.match(self.input, EXTID, self.FOLLOW_EXTID_in_payloadtypedecl630)
                if self._state.backtracking == 0:

                    EXTID38_tree = self._adaptor.createWithPayload(EXTID38)
                    self._adaptor.addChild(root_0, EXTID38_tree)

                ASKW39=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_payloadtypedecl632)
                if self._state.backtracking == 0:

                    ASKW39_tree = self._adaptor.createWithPayload(ASKW39)
                    self._adaptor.addChild(root_0, ASKW39_tree)

                ID40=self.match(self.input, ID, self.FOLLOW_ID_in_payloadtypedecl634)
                if self._state.backtracking == 0:

                    ID40_tree = self._adaptor.createWithPayload(ID40)
                    self._adaptor.addChild(root_0, ID40_tree)

                char_literal41=self.match(self.input, 68, self.FOLLOW_68_in_payloadtypedecl636)
                if self._state.backtracking == 0:

                    char_literal41_tree = self._adaptor.createWithPayload(char_literal41)
                    self._adaptor.addChild(root_0, char_literal41_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "payloadtypedecl"

    class description_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.description_return, self).__init__()

            self.tree = None




    # $ANTLR start "description"
    # final_09_01-13/Monitor.g:90:1: description : ( ( packagedecl | importdecl | module ) )* protocolDef -> protocolDef ;
    def description(self, ):

        retval = self.description_return()
        retval.start = self.input.LT(1)

        root_0 = None

        packagedecl42 = None

        importdecl43 = None

        module44 = None

        protocolDef45 = None


        stream_importdecl = RewriteRuleSubtreeStream(self._adaptor, "rule importdecl")
        stream_module = RewriteRuleSubtreeStream(self._adaptor, "rule module")
        stream_protocolDef = RewriteRuleSubtreeStream(self._adaptor, "rule protocolDef")
        stream_packagedecl = RewriteRuleSubtreeStream(self._adaptor, "rule packagedecl")
        try:
            try:
                # final_09_01-13/Monitor.g:90:12: ( ( ( packagedecl | importdecl | module ) )* protocolDef -> protocolDef )
                # final_09_01-13/Monitor.g:90:14: ( ( packagedecl | importdecl | module ) )* protocolDef
                pass 
                # final_09_01-13/Monitor.g:90:14: ( ( packagedecl | importdecl | module ) )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((PACKAGEKW <= LA8_0 <= IMPORTKW) or LA8_0 == FROMKW) :
                        alt8 = 1


                    if alt8 == 1:
                        # final_09_01-13/Monitor.g:90:16: ( packagedecl | importdecl | module )
                        pass 
                        # final_09_01-13/Monitor.g:90:16: ( packagedecl | importdecl | module )
                        alt7 = 3
                        alt7 = self.dfa7.predict(self.input)
                        if alt7 == 1:
                            # final_09_01-13/Monitor.g:90:18: packagedecl
                            pass 
                            self._state.following.append(self.FOLLOW_packagedecl_in_description647)
                            packagedecl42 = self.packagedecl()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_packagedecl.add(packagedecl42.tree)


                        elif alt7 == 2:
                            # final_09_01-13/Monitor.g:90:32: importdecl
                            pass 
                            self._state.following.append(self.FOLLOW_importdecl_in_description651)
                            importdecl43 = self.importdecl()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_importdecl.add(importdecl43.tree)


                        elif alt7 == 3:
                            # final_09_01-13/Monitor.g:90:45: module
                            pass 
                            self._state.following.append(self.FOLLOW_module_in_description655)
                            module44 = self.module()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_module.add(module44.tree)





                    else:
                        break #loop8
                self._state.following.append(self.FOLLOW_protocolDef_in_description662)
                protocolDef45 = self.protocolDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_protocolDef.add(protocolDef45.tree)

                # AST Rewrite
                # elements: protocolDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 90:69: -> protocolDef
                    self._adaptor.addChild(root_0, stream_protocolDef.nextTree())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "description"

    class parameterList_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.parameterList_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameterList"
    # final_09_01-13/Monitor.g:92:1: parameterList : '<' SIGKW ID ( ',' SIGKW ID )* '>' -> ^( PARAMETERLIST ( ID )+ ) ;
    def parameterList(self, ):

        retval = self.parameterList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal46 = None
        SIGKW47 = None
        ID48 = None
        char_literal49 = None
        SIGKW50 = None
        ID51 = None
        char_literal52 = None

        char_literal46_tree = None
        SIGKW47_tree = None
        ID48_tree = None
        char_literal49_tree = None
        SIGKW50_tree = None
        ID51_tree = None
        char_literal52_tree = None
        stream_69 = RewriteRuleTokenStream(self._adaptor, "token 69")
        stream_SIGKW = RewriteRuleTokenStream(self._adaptor, "token SIGKW")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")

        try:
            try:
                # final_09_01-13/Monitor.g:92:14: ( '<' SIGKW ID ( ',' SIGKW ID )* '>' -> ^( PARAMETERLIST ( ID )+ ) )
                # final_09_01-13/Monitor.g:92:16: '<' SIGKW ID ( ',' SIGKW ID )* '>'
                pass 
                char_literal46=self.match(self.input, 69, self.FOLLOW_69_in_parameterList673) 
                if self._state.backtracking == 0:
                    stream_69.add(char_literal46)
                SIGKW47=self.match(self.input, SIGKW, self.FOLLOW_SIGKW_in_parameterList675) 
                if self._state.backtracking == 0:
                    stream_SIGKW.add(SIGKW47)
                ID48=self.match(self.input, ID, self.FOLLOW_ID_in_parameterList677) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID48)
                # final_09_01-13/Monitor.g:92:29: ( ',' SIGKW ID )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 71) :
                        alt9 = 1


                    if alt9 == 1:
                        # final_09_01-13/Monitor.g:92:30: ',' SIGKW ID
                        pass 
                        char_literal49=self.match(self.input, 71, self.FOLLOW_71_in_parameterList680) 
                        if self._state.backtracking == 0:
                            stream_71.add(char_literal49)
                        SIGKW50=self.match(self.input, SIGKW, self.FOLLOW_SIGKW_in_parameterList682) 
                        if self._state.backtracking == 0:
                            stream_SIGKW.add(SIGKW50)
                        ID51=self.match(self.input, ID, self.FOLLOW_ID_in_parameterList684) 
                        if self._state.backtracking == 0:
                            stream_ID.add(ID51)


                    else:
                        break #loop9
                char_literal52=self.match(self.input, 70, self.FOLLOW_70_in_parameterList688) 
                if self._state.backtracking == 0:
                    stream_70.add(char_literal52)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 92:49: -> ^( PARAMETERLIST ( ID )+ )
                    # final_09_01-13/Monitor.g:92:52: ^( PARAMETERLIST ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMETERLIST, "PARAMETERLIST"), root_1)

                    # final_09_01-13/Monitor.g:92:68: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, stream_ID.nextNode())


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parameterList"

    class protocolDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.protocolDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "protocolDef"
    # final_09_01-13/Monitor.g:94:1: protocolDef : 'local' 'protocol' protocolName ( 'at' roleName ) ( parameterList )? roleList '{' ( protocolBlockDef ) '}' -> ^( PROTOCOL roleName ( parameterList )* ( roleList )+ ( protocolBlockDef )* ) ;
    def protocolDef(self, ):

        retval = self.protocolDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal53 = None
        string_literal54 = None
        string_literal56 = None
        char_literal60 = None
        char_literal62 = None
        protocolName55 = None

        roleName57 = None

        parameterList58 = None

        roleList59 = None

        protocolBlockDef61 = None


        string_literal53_tree = None
        string_literal54_tree = None
        string_literal56_tree = None
        char_literal60_tree = None
        char_literal62_tree = None
        stream_LOCALKW = RewriteRuleTokenStream(self._adaptor, "token LOCALKW")
        stream_ATKW = RewriteRuleTokenStream(self._adaptor, "token ATKW")
        stream_PROTOCOLKW = RewriteRuleTokenStream(self._adaptor, "token PROTOCOLKW")
        stream_72 = RewriteRuleTokenStream(self._adaptor, "token 72")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_roleList = RewriteRuleSubtreeStream(self._adaptor, "rule roleList")
        stream_protocolName = RewriteRuleSubtreeStream(self._adaptor, "rule protocolName")
        stream_parameterList = RewriteRuleSubtreeStream(self._adaptor, "rule parameterList")
        stream_protocolBlockDef = RewriteRuleSubtreeStream(self._adaptor, "rule protocolBlockDef")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        try:
            try:
                # final_09_01-13/Monitor.g:94:12: ( 'local' 'protocol' protocolName ( 'at' roleName ) ( parameterList )? roleList '{' ( protocolBlockDef ) '}' -> ^( PROTOCOL roleName ( parameterList )* ( roleList )+ ( protocolBlockDef )* ) )
                # final_09_01-13/Monitor.g:94:14: 'local' 'protocol' protocolName ( 'at' roleName ) ( parameterList )? roleList '{' ( protocolBlockDef ) '}'
                pass 
                string_literal53=self.match(self.input, LOCALKW, self.FOLLOW_LOCALKW_in_protocolDef706) 
                if self._state.backtracking == 0:
                    stream_LOCALKW.add(string_literal53)
                string_literal54=self.match(self.input, PROTOCOLKW, self.FOLLOW_PROTOCOLKW_in_protocolDef708) 
                if self._state.backtracking == 0:
                    stream_PROTOCOLKW.add(string_literal54)
                self._state.following.append(self.FOLLOW_protocolName_in_protocolDef710)
                protocolName55 = self.protocolName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_protocolName.add(protocolName55.tree)
                # final_09_01-13/Monitor.g:94:46: ( 'at' roleName )
                # final_09_01-13/Monitor.g:94:48: 'at' roleName
                pass 
                string_literal56=self.match(self.input, ATKW, self.FOLLOW_ATKW_in_protocolDef714) 
                if self._state.backtracking == 0:
                    stream_ATKW.add(string_literal56)
                self._state.following.append(self.FOLLOW_roleName_in_protocolDef716)
                roleName57 = self.roleName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleName.add(roleName57.tree)



                # final_09_01-13/Monitor.g:94:65: ( parameterList )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 69) :
                    alt10 = 1
                if alt10 == 1:
                    # final_09_01-13/Monitor.g:94:67: parameterList
                    pass 
                    self._state.following.append(self.FOLLOW_parameterList_in_protocolDef723)
                    parameterList58 = self.parameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameterList.add(parameterList58.tree)



                self._state.following.append(self.FOLLOW_roleList_in_protocolDef728)
                roleList59 = self.roleList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleList.add(roleList59.tree)
                char_literal60=self.match(self.input, 72, self.FOLLOW_72_in_protocolDef730) 
                if self._state.backtracking == 0:
                    stream_72.add(char_literal60)
                # final_09_01-13/Monitor.g:94:97: ( protocolBlockDef )
                # final_09_01-13/Monitor.g:94:99: protocolBlockDef
                pass 
                self._state.following.append(self.FOLLOW_protocolBlockDef_in_protocolDef734)
                protocolBlockDef61 = self.protocolBlockDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_protocolBlockDef.add(protocolBlockDef61.tree)



                char_literal62=self.match(self.input, 73, self.FOLLOW_73_in_protocolDef738) 
                if self._state.backtracking == 0:
                    stream_73.add(char_literal62)

                # AST Rewrite
                # elements: protocolBlockDef, parameterList, roleName, roleList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 95:7: -> ^( PROTOCOL roleName ( parameterList )* ( roleList )+ ( protocolBlockDef )* )
                    # final_09_01-13/Monitor.g:95:10: ^( PROTOCOL roleName ( parameterList )* ( roleList )+ ( protocolBlockDef )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROTOCOL, "PROTOCOL"), root_1)

                    self._adaptor.addChild(root_1, stream_roleName.nextTree())
                    # final_09_01-13/Monitor.g:95:30: ( parameterList )*
                    while stream_parameterList.hasNext():
                        self._adaptor.addChild(root_1, stream_parameterList.nextTree())


                    stream_parameterList.reset();
                    # final_09_01-13/Monitor.g:95:45: ( roleList )+
                    if not (stream_roleList.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_roleList.hasNext():
                        self._adaptor.addChild(root_1, stream_roleList.nextTree())


                    stream_roleList.reset()
                    # final_09_01-13/Monitor.g:95:55: ( protocolBlockDef )*
                    while stream_protocolBlockDef.hasNext():
                        self._adaptor.addChild(root_1, stream_protocolBlockDef.nextTree())


                    stream_protocolBlockDef.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "protocolDef"

    class roleList_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.roleList_return, self).__init__()

            self.tree = None




    # $ANTLR start "roleList"
    # final_09_01-13/Monitor.g:97:1: roleList : '(' roleparameDef ( ',' roleparameDef )* ')' -> ^( ROLES ( roleparameDef )+ ) ;
    def roleList(self, ):

        retval = self.roleList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal63 = None
        char_literal65 = None
        char_literal67 = None
        roleparameDef64 = None

        roleparameDef66 = None


        char_literal63_tree = None
        char_literal65_tree = None
        char_literal67_tree = None
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_75 = RewriteRuleTokenStream(self._adaptor, "token 75")
        stream_roleparameDef = RewriteRuleSubtreeStream(self._adaptor, "rule roleparameDef")
        try:
            try:
                # final_09_01-13/Monitor.g:97:9: ( '(' roleparameDef ( ',' roleparameDef )* ')' -> ^( ROLES ( roleparameDef )+ ) )
                # final_09_01-13/Monitor.g:97:11: '(' roleparameDef ( ',' roleparameDef )* ')'
                pass 
                char_literal63=self.match(self.input, 74, self.FOLLOW_74_in_roleList768) 
                if self._state.backtracking == 0:
                    stream_74.add(char_literal63)
                self._state.following.append(self.FOLLOW_roleparameDef_in_roleList770)
                roleparameDef64 = self.roleparameDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleparameDef.add(roleparameDef64.tree)
                # final_09_01-13/Monitor.g:97:29: ( ',' roleparameDef )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == 71) :
                        alt11 = 1


                    if alt11 == 1:
                        # final_09_01-13/Monitor.g:97:31: ',' roleparameDef
                        pass 
                        char_literal65=self.match(self.input, 71, self.FOLLOW_71_in_roleList774) 
                        if self._state.backtracking == 0:
                            stream_71.add(char_literal65)
                        self._state.following.append(self.FOLLOW_roleparameDef_in_roleList776)
                        roleparameDef66 = self.roleparameDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_roleparameDef.add(roleparameDef66.tree)


                    else:
                        break #loop11
                char_literal67=self.match(self.input, 75, self.FOLLOW_75_in_roleList781) 
                if self._state.backtracking == 0:
                    stream_75.add(char_literal67)

                # AST Rewrite
                # elements: roleparameDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 97:56: -> ^( ROLES ( roleparameDef )+ )
                    # final_09_01-13/Monitor.g:97:59: ^( ROLES ( roleparameDef )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROLES, "ROLES"), root_1)

                    # final_09_01-13/Monitor.g:97:67: ( roleparameDef )+
                    if not (stream_roleparameDef.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_roleparameDef.hasNext():
                        self._adaptor.addChild(root_1, stream_roleparameDef.nextTree())


                    stream_roleparameDef.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "roleList"

    class protocolName_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.protocolName_return, self).__init__()

            self.tree = None




    # $ANTLR start "protocolName"
    # final_09_01-13/Monitor.g:98:1: protocolName : ID ;
    def protocolName(self, ):

        retval = self.protocolName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID68 = None

        ID68_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:98:13: ( ID )
                # final_09_01-13/Monitor.g:98:15: ID
                pass 
                root_0 = self._adaptor.nil()

                ID68=self.match(self.input, ID, self.FOLLOW_ID_in_protocolName796)
                if self._state.backtracking == 0:

                    ID68_tree = self._adaptor.createWithPayload(ID68)
                    self._adaptor.addChild(root_0, ID68_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "protocolName"

    class roleparameDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.roleparameDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "roleparameDef"
    # final_09_01-13/Monitor.g:99:1: roleparameDef : 'role' ID -> ID ;
    def roleparameDef(self, ):

        retval = self.roleparameDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal69 = None
        ID70 = None

        string_literal69_tree = None
        ID70_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_ROLEKW = RewriteRuleTokenStream(self._adaptor, "token ROLEKW")

        try:
            try:
                # final_09_01-13/Monitor.g:99:14: ( 'role' ID -> ID )
                # final_09_01-13/Monitor.g:99:16: 'role' ID
                pass 
                string_literal69=self.match(self.input, ROLEKW, self.FOLLOW_ROLEKW_in_roleparameDef802) 
                if self._state.backtracking == 0:
                    stream_ROLEKW.add(string_literal69)
                ID70=self.match(self.input, ID, self.FOLLOW_ID_in_roleparameDef804) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID70)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 99:26: -> ID
                    self._adaptor.addChild(root_0, stream_ID.nextNode())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "roleparameDef"

    class protocolBlockDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.protocolBlockDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "protocolBlockDef"
    # final_09_01-13/Monitor.g:101:1: protocolBlockDef : activityListDef -> activityListDef ;
    def protocolBlockDef(self, ):

        retval = self.protocolBlockDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        activityListDef71 = None


        stream_activityListDef = RewriteRuleSubtreeStream(self._adaptor, "rule activityListDef")
        try:
            try:
                # final_09_01-13/Monitor.g:101:17: ( activityListDef -> activityListDef )
                # final_09_01-13/Monitor.g:101:19: activityListDef
                pass 
                self._state.following.append(self.FOLLOW_activityListDef_in_protocolBlockDef815)
                activityListDef71 = self.activityListDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_activityListDef.add(activityListDef71.tree)

                # AST Rewrite
                # elements: activityListDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 101:35: -> activityListDef
                    self._adaptor.addChild(root_0, stream_activityListDef.nextTree())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "protocolBlockDef"

    class blockDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.blockDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "blockDef"
    # final_09_01-13/Monitor.g:103:1: blockDef : '{' activityListDef '}' -> ^( BRANCH activityListDef ) ;
    def blockDef(self, ):

        retval = self.blockDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal72 = None
        char_literal74 = None
        activityListDef73 = None


        char_literal72_tree = None
        char_literal74_tree = None
        stream_72 = RewriteRuleTokenStream(self._adaptor, "token 72")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_activityListDef = RewriteRuleSubtreeStream(self._adaptor, "rule activityListDef")
        try:
            try:
                # final_09_01-13/Monitor.g:103:9: ( '{' activityListDef '}' -> ^( BRANCH activityListDef ) )
                # final_09_01-13/Monitor.g:103:11: '{' activityListDef '}'
                pass 
                char_literal72=self.match(self.input, 72, self.FOLLOW_72_in_blockDef827) 
                if self._state.backtracking == 0:
                    stream_72.add(char_literal72)
                self._state.following.append(self.FOLLOW_activityListDef_in_blockDef829)
                activityListDef73 = self.activityListDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_activityListDef.add(activityListDef73.tree)
                char_literal74=self.match(self.input, 73, self.FOLLOW_73_in_blockDef831) 
                if self._state.backtracking == 0:
                    stream_73.add(char_literal74)

                # AST Rewrite
                # elements: activityListDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 103:35: -> ^( BRANCH activityListDef )
                    # final_09_01-13/Monitor.g:103:38: ^( BRANCH activityListDef )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BRANCH, "BRANCH"), root_1)

                    self._adaptor.addChild(root_1, stream_activityListDef.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "blockDef"

    class assertDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.assertDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "assertDef"
    # final_09_01-13/Monitor.g:105:1: assertDef : ( ASSERTION )? -> ^( ASSERT ( ASSERTION )? ) ;
    def assertDef(self, ):

        retval = self.assertDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASSERTION75 = None

        ASSERTION75_tree = None
        stream_ASSERTION = RewriteRuleTokenStream(self._adaptor, "token ASSERTION")

        try:
            try:
                # final_09_01-13/Monitor.g:105:11: ( ( ASSERTION )? -> ^( ASSERT ( ASSERTION )? ) )
                # final_09_01-13/Monitor.g:105:13: ( ASSERTION )?
                pass 
                # final_09_01-13/Monitor.g:105:13: ( ASSERTION )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == ASSERTION) :
                    alt12 = 1
                if alt12 == 1:
                    # final_09_01-13/Monitor.g:105:14: ASSERTION
                    pass 
                    ASSERTION75=self.match(self.input, ASSERTION, self.FOLLOW_ASSERTION_in_assertDef853) 
                    if self._state.backtracking == 0:
                        stream_ASSERTION.add(ASSERTION75)




                # AST Rewrite
                # elements: ASSERTION
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 105:26: -> ^( ASSERT ( ASSERTION )? )
                    # final_09_01-13/Monitor.g:105:29: ^( ASSERT ( ASSERTION )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ASSERT, "ASSERT"), root_1)

                    # final_09_01-13/Monitor.g:105:38: ( ASSERTION )?
                    if stream_ASSERTION.hasNext():
                        self._adaptor.addChild(root_1, stream_ASSERTION.nextNode())


                    stream_ASSERTION.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "assertDef"

    class activityListDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.activityListDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "activityListDef"
    # final_09_01-13/Monitor.g:107:1: activityListDef : ( activityDef )* -> ( activityDef )* ;
    def activityListDef(self, ):

        retval = self.activityListDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        activityDef76 = None


        stream_activityDef = RewriteRuleSubtreeStream(self._adaptor, "rule activityDef")
        try:
            try:
                # final_09_01-13/Monitor.g:107:16: ( ( activityDef )* -> ( activityDef )* )
                # final_09_01-13/Monitor.g:107:18: ( activityDef )*
                pass 
                # final_09_01-13/Monitor.g:107:18: ( activityDef )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((FROMKW <= LA13_0 <= CHOICEKW) or (RECKW <= LA13_0 <= PARALLELKW) or LA13_0 == INTERRUPTIBLEKW or LA13_0 == DOKW or LA13_0 == ID or LA13_0 == 72 or LA13_0 == 74 or (78 <= LA13_0 <= 81) or LA13_0 == 84) :
                        alt13 = 1


                    if alt13 == 1:
                        # final_09_01-13/Monitor.g:107:20: activityDef
                        pass 
                        self._state.following.append(self.FOLLOW_activityDef_in_activityListDef873)
                        activityDef76 = self.activityDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_activityDef.add(activityDef76.tree)


                    else:
                        break #loop13

                # AST Rewrite
                # elements: activityDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 107:35: -> ( activityDef )*
                    # final_09_01-13/Monitor.g:107:38: ( activityDef )*
                    while stream_activityDef.hasNext():
                        self._adaptor.addChild(root_0, stream_activityDef.nextTree())


                    stream_activityDef.reset();



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "activityListDef"

    class primitivetype_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.primitivetype_return, self).__init__()

            self.tree = None




    # $ANTLR start "primitivetype"
    # final_09_01-13/Monitor.g:109:1: primitivetype : ( INT -> INT | STRING -> STRING ) ;
    def primitivetype(self, ):

        retval = self.primitivetype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INT77 = None
        STRING78 = None

        INT77_tree = None
        STRING78_tree = None
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")

        try:
            try:
                # final_09_01-13/Monitor.g:109:15: ( ( INT -> INT | STRING -> STRING ) )
                # final_09_01-13/Monitor.g:109:16: ( INT -> INT | STRING -> STRING )
                pass 
                # final_09_01-13/Monitor.g:109:16: ( INT -> INT | STRING -> STRING )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == INT) :
                    alt14 = 1
                elif (LA14_0 == STRING) :
                    alt14 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # final_09_01-13/Monitor.g:109:17: INT
                    pass 
                    INT77=self.match(self.input, INT, self.FOLLOW_INT_in_primitivetype889) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT77)

                    # AST Rewrite
                    # elements: INT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 109:21: -> INT
                        self._adaptor.addChild(root_0, stream_INT.nextNode())



                        retval.tree = root_0


                elif alt14 == 2:
                    # final_09_01-13/Monitor.g:110:17: STRING
                    pass 
                    STRING78=self.match(self.input, STRING, self.FOLLOW_STRING_in_primitivetype911) 
                    if self._state.backtracking == 0:
                        stream_STRING.add(STRING78)

                    # AST Rewrite
                    # elements: STRING
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 110:23: -> STRING
                        self._adaptor.addChild(root_0, stream_STRING.nextNode())



                        retval.tree = root_0






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "primitivetype"

    class activityDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.activityDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "activityDef"
    # final_09_01-13/Monitor.g:112:1: activityDef : ( ( introducesDef | interactionDef | inlineDef | runDef | recursionDef | endDef | doDef ) ';' | choiceDef | directedChoiceDef | parallelDef | repeatDef | unorderedDef | recBlockDef | globalEscapeDef );
    def activityDef(self, ):

        retval = self.activityDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal86 = None
        introducesDef79 = None

        interactionDef80 = None

        inlineDef81 = None

        runDef82 = None

        recursionDef83 = None

        endDef84 = None

        doDef85 = None

        choiceDef87 = None

        directedChoiceDef88 = None

        parallelDef89 = None

        repeatDef90 = None

        unorderedDef91 = None

        recBlockDef92 = None

        globalEscapeDef93 = None


        char_literal86_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:112:12: ( ( introducesDef | interactionDef | inlineDef | runDef | recursionDef | endDef | doDef ) ';' | choiceDef | directedChoiceDef | parallelDef | repeatDef | unorderedDef | recBlockDef | globalEscapeDef )
                alt16 = 8
                LA16 = self.input.LA(1)
                if LA16 == CONTINUEKW or LA16 == DOKW or LA16 == ID or LA16 == 74 or LA16 == 79 or LA16 == 80 or LA16 == 81:
                    alt16 = 1
                elif LA16 == CHOICEKW:
                    alt16 = 2
                elif LA16 == FROMKW or LA16 == TOKW or LA16 == 72:
                    alt16 = 3
                elif LA16 == PARALLELKW:
                    alt16 = 4
                elif LA16 == 78:
                    alt16 = 5
                elif LA16 == 84:
                    alt16 = 6
                elif LA16 == RECKW:
                    alt16 = 7
                elif LA16 == INTERRUPTIBLEKW:
                    alt16 = 8
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # final_09_01-13/Monitor.g:112:14: ( introducesDef | interactionDef | inlineDef | runDef | recursionDef | endDef | doDef ) ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    # final_09_01-13/Monitor.g:112:14: ( introducesDef | interactionDef | inlineDef | runDef | recursionDef | endDef | doDef )
                    alt15 = 7
                    LA15 = self.input.LA(1)
                    if LA15 == ID:
                        LA15_1 = self.input.LA(2)

                        if ((FROMKW <= LA15_1 <= TOKW) or LA15_1 == 74) :
                            alt15 = 2
                        elif (LA15_1 == 76) :
                            alt15 = 1
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 15, 1, self.input)

                            raise nvae

                    elif LA15 == 74:
                        alt15 = 2
                    elif LA15 == 81:
                        alt15 = 3
                    elif LA15 == 80:
                        alt15 = 4
                    elif LA15 == CONTINUEKW:
                        alt15 = 5
                    elif LA15 == 79:
                        alt15 = 6
                    elif LA15 == DOKW:
                        alt15 = 7
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 15, 0, self.input)

                        raise nvae

                    if alt15 == 1:
                        # final_09_01-13/Monitor.g:112:16: introducesDef
                        pass 
                        self._state.following.append(self.FOLLOW_introducesDef_in_activityDef924)
                        introducesDef79 = self.introducesDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, introducesDef79.tree)


                    elif alt15 == 2:
                        # final_09_01-13/Monitor.g:112:32: interactionDef
                        pass 
                        self._state.following.append(self.FOLLOW_interactionDef_in_activityDef928)
                        interactionDef80 = self.interactionDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, interactionDef80.tree)


                    elif alt15 == 3:
                        # final_09_01-13/Monitor.g:112:49: inlineDef
                        pass 
                        self._state.following.append(self.FOLLOW_inlineDef_in_activityDef932)
                        inlineDef81 = self.inlineDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, inlineDef81.tree)


                    elif alt15 == 4:
                        # final_09_01-13/Monitor.g:112:61: runDef
                        pass 
                        self._state.following.append(self.FOLLOW_runDef_in_activityDef936)
                        runDef82 = self.runDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, runDef82.tree)


                    elif alt15 == 5:
                        # final_09_01-13/Monitor.g:112:70: recursionDef
                        pass 
                        self._state.following.append(self.FOLLOW_recursionDef_in_activityDef940)
                        recursionDef83 = self.recursionDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, recursionDef83.tree)


                    elif alt15 == 6:
                        # final_09_01-13/Monitor.g:112:85: endDef
                        pass 
                        self._state.following.append(self.FOLLOW_endDef_in_activityDef944)
                        endDef84 = self.endDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, endDef84.tree)


                    elif alt15 == 7:
                        # final_09_01-13/Monitor.g:112:94: doDef
                        pass 
                        self._state.following.append(self.FOLLOW_doDef_in_activityDef948)
                        doDef85 = self.doDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, doDef85.tree)



                    char_literal86=self.match(self.input, 68, self.FOLLOW_68_in_activityDef952)


                elif alt16 == 2:
                    # final_09_01-13/Monitor.g:113:4: choiceDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_choiceDef_in_activityDef961)
                    choiceDef87 = self.choiceDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, choiceDef87.tree)


                elif alt16 == 3:
                    # final_09_01-13/Monitor.g:113:16: directedChoiceDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_directedChoiceDef_in_activityDef965)
                    directedChoiceDef88 = self.directedChoiceDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, directedChoiceDef88.tree)


                elif alt16 == 4:
                    # final_09_01-13/Monitor.g:113:36: parallelDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_parallelDef_in_activityDef969)
                    parallelDef89 = self.parallelDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parallelDef89.tree)


                elif alt16 == 5:
                    # final_09_01-13/Monitor.g:113:50: repeatDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_repeatDef_in_activityDef973)
                    repeatDef90 = self.repeatDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, repeatDef90.tree)


                elif alt16 == 6:
                    # final_09_01-13/Monitor.g:113:62: unorderedDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_unorderedDef_in_activityDef977)
                    unorderedDef91 = self.unorderedDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, unorderedDef91.tree)


                elif alt16 == 7:
                    # final_09_01-13/Monitor.g:114:4: recBlockDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_recBlockDef_in_activityDef984)
                    recBlockDef92 = self.recBlockDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, recBlockDef92.tree)


                elif alt16 == 8:
                    # final_09_01-13/Monitor.g:114:18: globalEscapeDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_globalEscapeDef_in_activityDef988)
                    globalEscapeDef93 = self.globalEscapeDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalEscapeDef93.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "activityDef"

    class introducesDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.introducesDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "introducesDef"
    # final_09_01-13/Monitor.g:116:1: introducesDef : roleDef 'introduces' roleDef ( ',' roleDef )* ;
    def introducesDef(self, ):

        retval = self.introducesDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal95 = None
        char_literal97 = None
        roleDef94 = None

        roleDef96 = None

        roleDef98 = None


        string_literal95_tree = None
        char_literal97_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:116:14: ( roleDef 'introduces' roleDef ( ',' roleDef )* )
                # final_09_01-13/Monitor.g:116:16: roleDef 'introduces' roleDef ( ',' roleDef )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_roleDef_in_introducesDef995)
                roleDef94 = self.roleDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, roleDef94.tree)
                string_literal95=self.match(self.input, 76, self.FOLLOW_76_in_introducesDef997)
                if self._state.backtracking == 0:

                    string_literal95_tree = self._adaptor.createWithPayload(string_literal95)
                    self._adaptor.addChild(root_0, string_literal95_tree)

                self._state.following.append(self.FOLLOW_roleDef_in_introducesDef999)
                roleDef96 = self.roleDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, roleDef96.tree)
                # final_09_01-13/Monitor.g:116:45: ( ',' roleDef )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == 71) :
                        alt17 = 1


                    if alt17 == 1:
                        # final_09_01-13/Monitor.g:116:47: ',' roleDef
                        pass 
                        char_literal97=self.match(self.input, 71, self.FOLLOW_71_in_introducesDef1003)
                        if self._state.backtracking == 0:

                            char_literal97_tree = self._adaptor.createWithPayload(char_literal97)
                            self._adaptor.addChild(root_0, char_literal97_tree)

                        self._state.following.append(self.FOLLOW_roleDef_in_introducesDef1005)
                        roleDef98 = self.roleDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, roleDef98.tree)


                    else:
                        break #loop17



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "introducesDef"

    class roleDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.roleDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "roleDef"
    # final_09_01-13/Monitor.g:118:1: roleDef : ID -> ID ;
    def roleDef(self, ):

        retval = self.roleDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID99 = None

        ID99_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # final_09_01-13/Monitor.g:118:8: ( ID -> ID )
                # final_09_01-13/Monitor.g:118:10: ID
                pass 
                ID99=self.match(self.input, ID, self.FOLLOW_ID_in_roleDef1016) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID99)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 118:13: -> ID
                    self._adaptor.addChild(root_0, stream_ID.nextNode())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "roleDef"

    class roleName_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.roleName_return, self).__init__()

            self.tree = None




    # $ANTLR start "roleName"
    # final_09_01-13/Monitor.g:120:1: roleName : ID -> ID ;
    def roleName(self, ):

        retval = self.roleName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID100 = None

        ID100_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # final_09_01-13/Monitor.g:120:9: ( ID -> ID )
                # final_09_01-13/Monitor.g:120:11: ID
                pass 
                ID100=self.match(self.input, ID, self.FOLLOW_ID_in_roleName1027) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID100)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 120:14: -> ID
                    self._adaptor.addChild(root_0, stream_ID.nextNode())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "roleName"

    class typeReferenceDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.typeReferenceDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "typeReferenceDef"
    # final_09_01-13/Monitor.g:122:1: typeReferenceDef : ID -> ID ;
    def typeReferenceDef(self, ):

        retval = self.typeReferenceDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID101 = None

        ID101_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # final_09_01-13/Monitor.g:122:17: ( ID -> ID )
                # final_09_01-13/Monitor.g:122:19: ID
                pass 
                ID101=self.match(self.input, ID, self.FOLLOW_ID_in_typeReferenceDef1038) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID101)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 122:22: -> ID
                    self._adaptor.addChild(root_0, stream_ID.nextNode())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "typeReferenceDef"

    class interactionSignatureDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.interactionSignatureDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "interactionSignatureDef"
    # final_09_01-13/Monitor.g:124:1: interactionSignatureDef : ( ( typeReferenceDef -> ^( ABSTRACT typeReferenceDef ) ) | ( typeReferenceDef '(' ( valueDecl ( ',' valueDecl )* )? ')' -> typeReferenceDef ^( VALUE ( valueDecl )* ) ) | ( ( '(' valueDecl ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) ) ) ;
    def interactionSignatureDef(self, ):

        retval = self.interactionSignatureDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal104 = None
        char_literal106 = None
        char_literal108 = None
        char_literal109 = None
        char_literal111 = None
        char_literal113 = None
        typeReferenceDef102 = None

        typeReferenceDef103 = None

        valueDecl105 = None

        valueDecl107 = None

        valueDecl110 = None

        valueDecl112 = None


        char_literal104_tree = None
        char_literal106_tree = None
        char_literal108_tree = None
        char_literal109_tree = None
        char_literal111_tree = None
        char_literal113_tree = None
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_75 = RewriteRuleTokenStream(self._adaptor, "token 75")
        stream_typeReferenceDef = RewriteRuleSubtreeStream(self._adaptor, "rule typeReferenceDef")
        stream_valueDecl = RewriteRuleSubtreeStream(self._adaptor, "rule valueDecl")
        try:
            try:
                # final_09_01-13/Monitor.g:124:24: ( ( ( typeReferenceDef -> ^( ABSTRACT typeReferenceDef ) ) | ( typeReferenceDef '(' ( valueDecl ( ',' valueDecl )* )? ')' -> typeReferenceDef ^( VALUE ( valueDecl )* ) ) | ( ( '(' valueDecl ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) ) ) )
                # final_09_01-13/Monitor.g:124:26: ( ( typeReferenceDef -> ^( ABSTRACT typeReferenceDef ) ) | ( typeReferenceDef '(' ( valueDecl ( ',' valueDecl )* )? ')' -> typeReferenceDef ^( VALUE ( valueDecl )* ) ) | ( ( '(' valueDecl ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) ) )
                pass 
                # final_09_01-13/Monitor.g:124:26: ( ( typeReferenceDef -> ^( ABSTRACT typeReferenceDef ) ) | ( typeReferenceDef '(' ( valueDecl ( ',' valueDecl )* )? ')' -> typeReferenceDef ^( VALUE ( valueDecl )* ) ) | ( ( '(' valueDecl ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) ) )
                alt21 = 3
                LA21_0 = self.input.LA(1)

                if (LA21_0 == ID) :
                    LA21_1 = self.input.LA(2)

                    if (LA21_1 == 74) :
                        alt21 = 2
                    elif (LA21_1 == EOF or (FROMKW <= LA21_1 <= TOKW) or LA21_1 == BYKW or (70 <= LA21_1 <= 71) or LA21_1 == 77) :
                        alt21 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 21, 1, self.input)

                        raise nvae

                elif (LA21_0 == 74) :
                    alt21 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # final_09_01-13/Monitor.g:124:27: ( typeReferenceDef -> ^( ABSTRACT typeReferenceDef ) )
                    pass 
                    # final_09_01-13/Monitor.g:124:27: ( typeReferenceDef -> ^( ABSTRACT typeReferenceDef ) )
                    # final_09_01-13/Monitor.g:124:28: typeReferenceDef
                    pass 
                    self._state.following.append(self.FOLLOW_typeReferenceDef_in_interactionSignatureDef1051)
                    typeReferenceDef102 = self.typeReferenceDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_typeReferenceDef.add(typeReferenceDef102.tree)

                    # AST Rewrite
                    # elements: typeReferenceDef
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 124:45: -> ^( ABSTRACT typeReferenceDef )
                        # final_09_01-13/Monitor.g:124:48: ^( ABSTRACT typeReferenceDef )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ABSTRACT, "ABSTRACT"), root_1)

                        self._adaptor.addChild(root_1, stream_typeReferenceDef.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0





                elif alt21 == 2:
                    # final_09_01-13/Monitor.g:125:7: ( typeReferenceDef '(' ( valueDecl ( ',' valueDecl )* )? ')' -> typeReferenceDef ^( VALUE ( valueDecl )* ) )
                    pass 
                    # final_09_01-13/Monitor.g:125:7: ( typeReferenceDef '(' ( valueDecl ( ',' valueDecl )* )? ')' -> typeReferenceDef ^( VALUE ( valueDecl )* ) )
                    # final_09_01-13/Monitor.g:125:8: typeReferenceDef '(' ( valueDecl ( ',' valueDecl )* )? ')'
                    pass 
                    self._state.following.append(self.FOLLOW_typeReferenceDef_in_interactionSignatureDef1069)
                    typeReferenceDef103 = self.typeReferenceDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_typeReferenceDef.add(typeReferenceDef103.tree)
                    char_literal104=self.match(self.input, 74, self.FOLLOW_74_in_interactionSignatureDef1071) 
                    if self._state.backtracking == 0:
                        stream_74.add(char_literal104)
                    # final_09_01-13/Monitor.g:125:29: ( valueDecl ( ',' valueDecl )* )?
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == ID) :
                        alt19 = 1
                    if alt19 == 1:
                        # final_09_01-13/Monitor.g:125:30: valueDecl ( ',' valueDecl )*
                        pass 
                        self._state.following.append(self.FOLLOW_valueDecl_in_interactionSignatureDef1074)
                        valueDecl105 = self.valueDecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_valueDecl.add(valueDecl105.tree)
                        # final_09_01-13/Monitor.g:125:40: ( ',' valueDecl )*
                        while True: #loop18
                            alt18 = 2
                            LA18_0 = self.input.LA(1)

                            if (LA18_0 == 71) :
                                alt18 = 1


                            if alt18 == 1:
                                # final_09_01-13/Monitor.g:125:41: ',' valueDecl
                                pass 
                                char_literal106=self.match(self.input, 71, self.FOLLOW_71_in_interactionSignatureDef1077) 
                                if self._state.backtracking == 0:
                                    stream_71.add(char_literal106)
                                self._state.following.append(self.FOLLOW_valueDecl_in_interactionSignatureDef1079)
                                valueDecl107 = self.valueDecl()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_valueDecl.add(valueDecl107.tree)


                            else:
                                break #loop18



                    char_literal108=self.match(self.input, 75, self.FOLLOW_75_in_interactionSignatureDef1086) 
                    if self._state.backtracking == 0:
                        stream_75.add(char_literal108)

                    # AST Rewrite
                    # elements: valueDecl, typeReferenceDef
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 125:64: -> typeReferenceDef ^( VALUE ( valueDecl )* )
                        self._adaptor.addChild(root_0, stream_typeReferenceDef.nextTree())
                        # final_09_01-13/Monitor.g:125:84: ^( VALUE ( valueDecl )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VALUE, "VALUE"), root_1)

                        # final_09_01-13/Monitor.g:125:92: ( valueDecl )*
                        while stream_valueDecl.hasNext():
                            self._adaptor.addChild(root_1, stream_valueDecl.nextTree())


                        stream_valueDecl.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0





                elif alt21 == 3:
                    # final_09_01-13/Monitor.g:126:7: ( ( '(' valueDecl ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) )
                    pass 
                    # final_09_01-13/Monitor.g:126:7: ( ( '(' valueDecl ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) )
                    # final_09_01-13/Monitor.g:126:8: ( '(' valueDecl ( ',' valueDecl )* ')' )
                    pass 
                    # final_09_01-13/Monitor.g:126:8: ( '(' valueDecl ( ',' valueDecl )* ')' )
                    # final_09_01-13/Monitor.g:126:9: '(' valueDecl ( ',' valueDecl )* ')'
                    pass 
                    char_literal109=self.match(self.input, 74, self.FOLLOW_74_in_interactionSignatureDef1108) 
                    if self._state.backtracking == 0:
                        stream_74.add(char_literal109)
                    self._state.following.append(self.FOLLOW_valueDecl_in_interactionSignatureDef1110)
                    valueDecl110 = self.valueDecl()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_valueDecl.add(valueDecl110.tree)
                    # final_09_01-13/Monitor.g:126:23: ( ',' valueDecl )*
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == 71) :
                            alt20 = 1


                        if alt20 == 1:
                            # final_09_01-13/Monitor.g:126:24: ',' valueDecl
                            pass 
                            char_literal111=self.match(self.input, 71, self.FOLLOW_71_in_interactionSignatureDef1113) 
                            if self._state.backtracking == 0:
                                stream_71.add(char_literal111)
                            self._state.following.append(self.FOLLOW_valueDecl_in_interactionSignatureDef1115)
                            valueDecl112 = self.valueDecl()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_valueDecl.add(valueDecl112.tree)


                        else:
                            break #loop20
                    char_literal113=self.match(self.input, 75, self.FOLLOW_75_in_interactionSignatureDef1119) 
                    if self._state.backtracking == 0:
                        stream_75.add(char_literal113)




                    # AST Rewrite
                    # elements: valueDecl
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 126:45: -> ^( VALUE ( valueDecl )* )
                        # final_09_01-13/Monitor.g:126:48: ^( VALUE ( valueDecl )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VALUE, "VALUE"), root_1)

                        # final_09_01-13/Monitor.g:126:56: ( valueDecl )*
                        while stream_valueDecl.hasNext():
                            self._adaptor.addChild(root_1, stream_valueDecl.nextTree())


                        stream_valueDecl.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0









                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "interactionSignatureDef"

    class valueDecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.valueDecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "valueDecl"
    # final_09_01-13/Monitor.g:128:1: valueDecl : ID ( ':' primitivetype )? ;
    def valueDecl(self, ):

        retval = self.valueDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID114 = None
        char_literal115 = None
        primitivetype116 = None


        ID114_tree = None
        char_literal115_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:128:11: ( ID ( ':' primitivetype )? )
                # final_09_01-13/Monitor.g:128:13: ID ( ':' primitivetype )?
                pass 
                root_0 = self._adaptor.nil()

                ID114=self.match(self.input, ID, self.FOLLOW_ID_in_valueDecl1139)
                if self._state.backtracking == 0:

                    ID114_tree = self._adaptor.createWithPayload(ID114)
                    self._adaptor.addChild(root_0, ID114_tree)

                # final_09_01-13/Monitor.g:128:16: ( ':' primitivetype )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == 77) :
                    alt22 = 1
                if alt22 == 1:
                    # final_09_01-13/Monitor.g:128:17: ':' primitivetype
                    pass 
                    char_literal115=self.match(self.input, 77, self.FOLLOW_77_in_valueDecl1142)
                    self._state.following.append(self.FOLLOW_primitivetype_in_valueDecl1145)
                    primitivetype116 = self.primitivetype()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, primitivetype116.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "valueDecl"

    class firstValueDecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.firstValueDecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "firstValueDecl"
    # final_09_01-13/Monitor.g:129:1: firstValueDecl : valueDecl ;
    def firstValueDecl(self, ):

        retval = self.firstValueDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        valueDecl117 = None



        try:
            try:
                # final_09_01-13/Monitor.g:129:16: ( valueDecl )
                # final_09_01-13/Monitor.g:129:18: valueDecl
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_valueDecl_in_firstValueDecl1156)
                valueDecl117 = self.valueDecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, valueDecl117.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "firstValueDecl"

    class interactionDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.interactionDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "interactionDef"
    # final_09_01-13/Monitor.g:132:1: interactionDef : interactionSignatureDef ( 'from' role= roleName ( assertDef ) -> ^( RESV interactionSignatureDef $role assertDef ) | 'to' roleName ( assertDef ) -> ^( SEND interactionSignatureDef roleName assertDef ) ) ;
    def interactionDef(self, ):

        retval = self.interactionDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal119 = None
        string_literal121 = None
        role = None

        interactionSignatureDef118 = None

        assertDef120 = None

        roleName122 = None

        assertDef123 = None


        string_literal119_tree = None
        string_literal121_tree = None
        stream_TOKW = RewriteRuleTokenStream(self._adaptor, "token TOKW")
        stream_FROMKW = RewriteRuleTokenStream(self._adaptor, "token FROMKW")
        stream_assertDef = RewriteRuleSubtreeStream(self._adaptor, "rule assertDef")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        stream_interactionSignatureDef = RewriteRuleSubtreeStream(self._adaptor, "rule interactionSignatureDef")
        try:
            try:
                # final_09_01-13/Monitor.g:132:15: ( interactionSignatureDef ( 'from' role= roleName ( assertDef ) -> ^( RESV interactionSignatureDef $role assertDef ) | 'to' roleName ( assertDef ) -> ^( SEND interactionSignatureDef roleName assertDef ) ) )
                # final_09_01-13/Monitor.g:133:7: interactionSignatureDef ( 'from' role= roleName ( assertDef ) -> ^( RESV interactionSignatureDef $role assertDef ) | 'to' roleName ( assertDef ) -> ^( SEND interactionSignatureDef roleName assertDef ) )
                pass 
                self._state.following.append(self.FOLLOW_interactionSignatureDef_in_interactionDef1171)
                interactionSignatureDef118 = self.interactionSignatureDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_interactionSignatureDef.add(interactionSignatureDef118.tree)
                # final_09_01-13/Monitor.g:133:31: ( 'from' role= roleName ( assertDef ) -> ^( RESV interactionSignatureDef $role assertDef ) | 'to' roleName ( assertDef ) -> ^( SEND interactionSignatureDef roleName assertDef ) )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == FROMKW) :
                    alt23 = 1
                elif (LA23_0 == TOKW) :
                    alt23 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # final_09_01-13/Monitor.g:134:3: 'from' role= roleName ( assertDef )
                    pass 
                    string_literal119=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_interactionDef1177) 
                    if self._state.backtracking == 0:
                        stream_FROMKW.add(string_literal119)
                    self._state.following.append(self.FOLLOW_roleName_in_interactionDef1182)
                    role = self.roleName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleName.add(role.tree)
                    # final_09_01-13/Monitor.g:134:26: ( assertDef )
                    # final_09_01-13/Monitor.g:134:27: assertDef
                    pass 
                    self._state.following.append(self.FOLLOW_assertDef_in_interactionDef1186)
                    assertDef120 = self.assertDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_assertDef.add(assertDef120.tree)




                    # AST Rewrite
                    # elements: role, assertDef, interactionSignatureDef
                    # token labels: 
                    # rule labels: retval, role
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        if role is not None:
                            stream_role = RewriteRuleSubtreeStream(self._adaptor, "rule role", role.tree)
                        else:
                            stream_role = RewriteRuleSubtreeStream(self._adaptor, "token role", None)


                        root_0 = self._adaptor.nil()
                        # 134:37: -> ^( RESV interactionSignatureDef $role assertDef )
                        # final_09_01-13/Monitor.g:134:40: ^( RESV interactionSignatureDef $role assertDef )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RESV, "RESV"), root_1)

                        self._adaptor.addChild(root_1, stream_interactionSignatureDef.nextTree())
                        self._adaptor.addChild(root_1, stream_role.nextTree())
                        self._adaptor.addChild(root_1, stream_assertDef.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt23 == 2:
                    # final_09_01-13/Monitor.g:135:10: 'to' roleName ( assertDef )
                    pass 
                    string_literal121=self.match(self.input, TOKW, self.FOLLOW_TOKW_in_interactionDef1210) 
                    if self._state.backtracking == 0:
                        stream_TOKW.add(string_literal121)
                    self._state.following.append(self.FOLLOW_roleName_in_interactionDef1212)
                    roleName122 = self.roleName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleName.add(roleName122.tree)
                    # final_09_01-13/Monitor.g:135:25: ( assertDef )
                    # final_09_01-13/Monitor.g:135:26: assertDef
                    pass 
                    self._state.following.append(self.FOLLOW_assertDef_in_interactionDef1216)
                    assertDef123 = self.assertDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_assertDef.add(assertDef123.tree)




                    # AST Rewrite
                    # elements: interactionSignatureDef, assertDef, roleName
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 135:37: -> ^( SEND interactionSignatureDef roleName assertDef )
                        # final_09_01-13/Monitor.g:135:40: ^( SEND interactionSignatureDef roleName assertDef )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SEND, "SEND"), root_1)

                        self._adaptor.addChild(root_1, stream_interactionSignatureDef.nextTree())
                        self._adaptor.addChild(root_1, stream_roleName.nextTree())
                        self._adaptor.addChild(root_1, stream_assertDef.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "interactionDef"

    class choiceDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.choiceDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "choiceDef"
    # final_09_01-13/Monitor.g:137:1: choiceDef : 'choice' 'at' roleName blockDef ( 'or' blockDef )* -> ^( 'choice' ( blockDef )+ ) ;
    def choiceDef(self, ):

        retval = self.choiceDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal124 = None
        string_literal125 = None
        string_literal128 = None
        roleName126 = None

        blockDef127 = None

        blockDef129 = None


        string_literal124_tree = None
        string_literal125_tree = None
        string_literal128_tree = None
        stream_ATKW = RewriteRuleTokenStream(self._adaptor, "token ATKW")
        stream_ORKW = RewriteRuleTokenStream(self._adaptor, "token ORKW")
        stream_CHOICEKW = RewriteRuleTokenStream(self._adaptor, "token CHOICEKW")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        stream_blockDef = RewriteRuleSubtreeStream(self._adaptor, "rule blockDef")
        try:
            try:
                # final_09_01-13/Monitor.g:137:10: ( 'choice' 'at' roleName blockDef ( 'or' blockDef )* -> ^( 'choice' ( blockDef )+ ) )
                # final_09_01-13/Monitor.g:137:12: 'choice' 'at' roleName blockDef ( 'or' blockDef )*
                pass 
                string_literal124=self.match(self.input, CHOICEKW, self.FOLLOW_CHOICEKW_in_choiceDef1237) 
                if self._state.backtracking == 0:
                    stream_CHOICEKW.add(string_literal124)
                string_literal125=self.match(self.input, ATKW, self.FOLLOW_ATKW_in_choiceDef1239) 
                if self._state.backtracking == 0:
                    stream_ATKW.add(string_literal125)
                self._state.following.append(self.FOLLOW_roleName_in_choiceDef1241)
                roleName126 = self.roleName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleName.add(roleName126.tree)
                self._state.following.append(self.FOLLOW_blockDef_in_choiceDef1243)
                blockDef127 = self.blockDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_blockDef.add(blockDef127.tree)
                # final_09_01-13/Monitor.g:137:44: ( 'or' blockDef )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == ORKW) :
                        alt24 = 1


                    if alt24 == 1:
                        # final_09_01-13/Monitor.g:137:46: 'or' blockDef
                        pass 
                        string_literal128=self.match(self.input, ORKW, self.FOLLOW_ORKW_in_choiceDef1247) 
                        if self._state.backtracking == 0:
                            stream_ORKW.add(string_literal128)
                        self._state.following.append(self.FOLLOW_blockDef_in_choiceDef1249)
                        blockDef129 = self.blockDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_blockDef.add(blockDef129.tree)


                    else:
                        break #loop24

                # AST Rewrite
                # elements: CHOICEKW, blockDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 137:63: -> ^( 'choice' ( blockDef )+ )
                    # final_09_01-13/Monitor.g:137:66: ^( 'choice' ( blockDef )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_CHOICEKW.nextNode(), root_1)

                    # final_09_01-13/Monitor.g:137:77: ( blockDef )+
                    if not (stream_blockDef.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_blockDef.hasNext():
                        self._adaptor.addChild(root_1, stream_blockDef.nextTree())


                    stream_blockDef.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "choiceDef"

    class directedChoiceDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.directedChoiceDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "directedChoiceDef"
    # final_09_01-13/Monitor.g:139:1: directedChoiceDef : ( 'from' roleName )? ( 'to' roleName ( ',' roleName )* )? '{' ( onMessageDef )+ '}' ;
    def directedChoiceDef(self, ):

        retval = self.directedChoiceDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal130 = None
        string_literal132 = None
        char_literal134 = None
        char_literal136 = None
        char_literal138 = None
        roleName131 = None

        roleName133 = None

        roleName135 = None

        onMessageDef137 = None


        string_literal130_tree = None
        string_literal132_tree = None
        char_literal134_tree = None
        char_literal136_tree = None
        char_literal138_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:139:18: ( ( 'from' roleName )? ( 'to' roleName ( ',' roleName )* )? '{' ( onMessageDef )+ '}' )
                # final_09_01-13/Monitor.g:139:20: ( 'from' roleName )? ( 'to' roleName ( ',' roleName )* )? '{' ( onMessageDef )+ '}'
                pass 
                root_0 = self._adaptor.nil()

                # final_09_01-13/Monitor.g:139:20: ( 'from' roleName )?
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == FROMKW) :
                    alt25 = 1
                if alt25 == 1:
                    # final_09_01-13/Monitor.g:139:22: 'from' roleName
                    pass 
                    string_literal130=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_directedChoiceDef1270)
                    if self._state.backtracking == 0:

                        string_literal130_tree = self._adaptor.createWithPayload(string_literal130)
                        self._adaptor.addChild(root_0, string_literal130_tree)

                    self._state.following.append(self.FOLLOW_roleName_in_directedChoiceDef1272)
                    roleName131 = self.roleName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, roleName131.tree)



                # final_09_01-13/Monitor.g:139:41: ( 'to' roleName ( ',' roleName )* )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == TOKW) :
                    alt27 = 1
                if alt27 == 1:
                    # final_09_01-13/Monitor.g:139:43: 'to' roleName ( ',' roleName )*
                    pass 
                    string_literal132=self.match(self.input, TOKW, self.FOLLOW_TOKW_in_directedChoiceDef1279)
                    if self._state.backtracking == 0:

                        string_literal132_tree = self._adaptor.createWithPayload(string_literal132)
                        self._adaptor.addChild(root_0, string_literal132_tree)

                    self._state.following.append(self.FOLLOW_roleName_in_directedChoiceDef1281)
                    roleName133 = self.roleName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, roleName133.tree)
                    # final_09_01-13/Monitor.g:139:57: ( ',' roleName )*
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == 71) :
                            alt26 = 1


                        if alt26 == 1:
                            # final_09_01-13/Monitor.g:139:59: ',' roleName
                            pass 
                            char_literal134=self.match(self.input, 71, self.FOLLOW_71_in_directedChoiceDef1285)
                            self._state.following.append(self.FOLLOW_roleName_in_directedChoiceDef1288)
                            roleName135 = self.roleName()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, roleName135.tree)


                        else:
                            break #loop26



                char_literal136=self.match(self.input, 72, self.FOLLOW_72_in_directedChoiceDef1296)
                if self._state.backtracking == 0:

                    char_literal136_tree = self._adaptor.createWithPayload(char_literal136)
                    self._adaptor.addChild(root_0, char_literal136_tree)

                # final_09_01-13/Monitor.g:139:83: ( onMessageDef )+
                cnt28 = 0
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == ID or LA28_0 == 74) :
                        alt28 = 1


                    if alt28 == 1:
                        # final_09_01-13/Monitor.g:139:85: onMessageDef
                        pass 
                        self._state.following.append(self.FOLLOW_onMessageDef_in_directedChoiceDef1300)
                        onMessageDef137 = self.onMessageDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, onMessageDef137.tree)


                    else:
                        if cnt28 >= 1:
                            break #loop28

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(28, self.input)
                        raise eee

                    cnt28 += 1
                char_literal138=self.match(self.input, 73, self.FOLLOW_73_in_directedChoiceDef1305)
                if self._state.backtracking == 0:

                    char_literal138_tree = self._adaptor.createWithPayload(char_literal138)
                    self._adaptor.addChild(root_0, char_literal138_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "directedChoiceDef"

    class onMessageDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.onMessageDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "onMessageDef"
    # final_09_01-13/Monitor.g:141:1: onMessageDef : interactionSignatureDef ':' activityList ;
    def onMessageDef(self, ):

        retval = self.onMessageDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal140 = None
        interactionSignatureDef139 = None

        activityList141 = None


        char_literal140_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:141:13: ( interactionSignatureDef ':' activityList )
                # final_09_01-13/Monitor.g:141:15: interactionSignatureDef ':' activityList
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_interactionSignatureDef_in_onMessageDef1312)
                interactionSignatureDef139 = self.interactionSignatureDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, interactionSignatureDef139.tree)
                char_literal140=self.match(self.input, 77, self.FOLLOW_77_in_onMessageDef1314)
                if self._state.backtracking == 0:

                    char_literal140_tree = self._adaptor.createWithPayload(char_literal140)
                    self._adaptor.addChild(root_0, char_literal140_tree)

                self._state.following.append(self.FOLLOW_activityList_in_onMessageDef1316)
                activityList141 = self.activityList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, activityList141.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "onMessageDef"

    class activityList_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.activityList_return, self).__init__()

            self.tree = None




    # $ANTLR start "activityList"
    # final_09_01-13/Monitor.g:143:1: activityList : ( activityDef )* ;
    def activityList(self, ):

        retval = self.activityList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        activityDef142 = None



        try:
            try:
                # final_09_01-13/Monitor.g:143:13: ( ( activityDef )* )
                # final_09_01-13/Monitor.g:143:15: ( activityDef )*
                pass 
                root_0 = self._adaptor.nil()

                # final_09_01-13/Monitor.g:143:15: ( activityDef )*
                while True: #loop29
                    alt29 = 2
                    alt29 = self.dfa29.predict(self.input)
                    if alt29 == 1:
                        # final_09_01-13/Monitor.g:143:17: activityDef
                        pass 
                        self._state.following.append(self.FOLLOW_activityDef_in_activityList1327)
                        activityDef142 = self.activityDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, activityDef142.tree)


                    else:
                        break #loop29



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "activityList"

    class repeatDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.repeatDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "repeatDef"
    # final_09_01-13/Monitor.g:145:1: repeatDef : 'repeat' ( 'at' roleName ( ',' roleName )* )? blockDef -> ^( 'repeat' blockDef ) ;
    def repeatDef(self, ):

        retval = self.repeatDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal143 = None
        string_literal144 = None
        char_literal146 = None
        roleName145 = None

        roleName147 = None

        blockDef148 = None


        string_literal143_tree = None
        string_literal144_tree = None
        char_literal146_tree = None
        stream_ATKW = RewriteRuleTokenStream(self._adaptor, "token ATKW")
        stream_78 = RewriteRuleTokenStream(self._adaptor, "token 78")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        stream_blockDef = RewriteRuleSubtreeStream(self._adaptor, "rule blockDef")
        try:
            try:
                # final_09_01-13/Monitor.g:145:10: ( 'repeat' ( 'at' roleName ( ',' roleName )* )? blockDef -> ^( 'repeat' blockDef ) )
                # final_09_01-13/Monitor.g:145:12: 'repeat' ( 'at' roleName ( ',' roleName )* )? blockDef
                pass 
                string_literal143=self.match(self.input, 78, self.FOLLOW_78_in_repeatDef1337) 
                if self._state.backtracking == 0:
                    stream_78.add(string_literal143)
                # final_09_01-13/Monitor.g:145:21: ( 'at' roleName ( ',' roleName )* )?
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == ATKW) :
                    alt31 = 1
                if alt31 == 1:
                    # final_09_01-13/Monitor.g:145:23: 'at' roleName ( ',' roleName )*
                    pass 
                    string_literal144=self.match(self.input, ATKW, self.FOLLOW_ATKW_in_repeatDef1341) 
                    if self._state.backtracking == 0:
                        stream_ATKW.add(string_literal144)
                    self._state.following.append(self.FOLLOW_roleName_in_repeatDef1343)
                    roleName145 = self.roleName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleName.add(roleName145.tree)
                    # final_09_01-13/Monitor.g:145:37: ( ',' roleName )*
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if (LA30_0 == 71) :
                            alt30 = 1


                        if alt30 == 1:
                            # final_09_01-13/Monitor.g:145:39: ',' roleName
                            pass 
                            char_literal146=self.match(self.input, 71, self.FOLLOW_71_in_repeatDef1347) 
                            if self._state.backtracking == 0:
                                stream_71.add(char_literal146)
                            self._state.following.append(self.FOLLOW_roleName_in_repeatDef1349)
                            roleName147 = self.roleName()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_roleName.add(roleName147.tree)


                        else:
                            break #loop30



                self._state.following.append(self.FOLLOW_blockDef_in_repeatDef1357)
                blockDef148 = self.blockDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_blockDef.add(blockDef148.tree)

                # AST Rewrite
                # elements: 78, blockDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 145:68: -> ^( 'repeat' blockDef )
                    # final_09_01-13/Monitor.g:145:71: ^( 'repeat' blockDef )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_78.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_blockDef.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "repeatDef"

    class recBlockDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.recBlockDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "recBlockDef"
    # final_09_01-13/Monitor.g:147:1: recBlockDef : 'rec' labelName blockDef -> ^( 'rec' labelName blockDef ) ;
    def recBlockDef(self, ):

        retval = self.recBlockDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal149 = None
        labelName150 = None

        blockDef151 = None


        string_literal149_tree = None
        stream_RECKW = RewriteRuleTokenStream(self._adaptor, "token RECKW")
        stream_labelName = RewriteRuleSubtreeStream(self._adaptor, "rule labelName")
        stream_blockDef = RewriteRuleSubtreeStream(self._adaptor, "rule blockDef")
        try:
            try:
                # final_09_01-13/Monitor.g:147:12: ( 'rec' labelName blockDef -> ^( 'rec' labelName blockDef ) )
                # final_09_01-13/Monitor.g:147:14: 'rec' labelName blockDef
                pass 
                string_literal149=self.match(self.input, RECKW, self.FOLLOW_RECKW_in_recBlockDef1373) 
                if self._state.backtracking == 0:
                    stream_RECKW.add(string_literal149)
                self._state.following.append(self.FOLLOW_labelName_in_recBlockDef1375)
                labelName150 = self.labelName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_labelName.add(labelName150.tree)
                self._state.following.append(self.FOLLOW_blockDef_in_recBlockDef1377)
                blockDef151 = self.blockDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_blockDef.add(blockDef151.tree)

                # AST Rewrite
                # elements: labelName, RECKW, blockDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 147:39: -> ^( 'rec' labelName blockDef )
                    # final_09_01-13/Monitor.g:147:42: ^( 'rec' labelName blockDef )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_RECKW.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_labelName.nextTree())
                    self._adaptor.addChild(root_1, stream_blockDef.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "recBlockDef"

    class labelName_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.labelName_return, self).__init__()

            self.tree = None




    # $ANTLR start "labelName"
    # final_09_01-13/Monitor.g:149:1: labelName : ID -> ID ;
    def labelName(self, ):

        retval = self.labelName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID152 = None

        ID152_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # final_09_01-13/Monitor.g:149:10: ( ID -> ID )
                # final_09_01-13/Monitor.g:149:12: ID
                pass 
                ID152=self.match(self.input, ID, self.FOLLOW_ID_in_labelName1394) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID152)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 149:15: -> ID
                    self._adaptor.addChild(root_0, stream_ID.nextNode())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "labelName"

    class recursionDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.recursionDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "recursionDef"
    # final_09_01-13/Monitor.g:151:1: recursionDef : 'continue' labelName -> ^( RECLABEL labelName ) ;
    def recursionDef(self, ):

        retval = self.recursionDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal153 = None
        labelName154 = None


        string_literal153_tree = None
        stream_CONTINUEKW = RewriteRuleTokenStream(self._adaptor, "token CONTINUEKW")
        stream_labelName = RewriteRuleSubtreeStream(self._adaptor, "rule labelName")
        try:
            try:
                # final_09_01-13/Monitor.g:151:13: ( 'continue' labelName -> ^( RECLABEL labelName ) )
                # final_09_01-13/Monitor.g:151:15: 'continue' labelName
                pass 
                string_literal153=self.match(self.input, CONTINUEKW, self.FOLLOW_CONTINUEKW_in_recursionDef1406) 
                if self._state.backtracking == 0:
                    stream_CONTINUEKW.add(string_literal153)
                self._state.following.append(self.FOLLOW_labelName_in_recursionDef1408)
                labelName154 = self.labelName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_labelName.add(labelName154.tree)

                # AST Rewrite
                # elements: labelName
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 151:36: -> ^( RECLABEL labelName )
                    # final_09_01-13/Monitor.g:151:39: ^( RECLABEL labelName )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RECLABEL, "RECLABEL"), root_1)

                    self._adaptor.addChild(root_1, stream_labelName.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "recursionDef"

    class endDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.endDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "endDef"
    # final_09_01-13/Monitor.g:154:1: endDef : 'end' ;
    def endDef(self, ):

        retval = self.endDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal155 = None

        string_literal155_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:154:7: ( 'end' )
                # final_09_01-13/Monitor.g:154:9: 'end'
                pass 
                root_0 = self._adaptor.nil()

                string_literal155=self.match(self.input, 79, self.FOLLOW_79_in_endDef1424)
                if self._state.backtracking == 0:

                    string_literal155_tree = self._adaptor.createWithPayload(string_literal155)
                    root_0 = self._adaptor.becomeRoot(string_literal155_tree, root_0)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "endDef"

    class runDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.runDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "runDef"
    # final_09_01-13/Monitor.g:157:1: runDef : 'run' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )? 'from' roleName ;
    def runDef(self, ):

        retval = self.runDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal156 = None
        char_literal158 = None
        char_literal160 = None
        char_literal162 = None
        string_literal163 = None
        protocolRefDef157 = None

        parameter159 = None

        parameter161 = None

        roleName164 = None


        string_literal156_tree = None
        char_literal158_tree = None
        char_literal160_tree = None
        char_literal162_tree = None
        string_literal163_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:157:7: ( 'run' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )? 'from' roleName )
                # final_09_01-13/Monitor.g:157:9: 'run' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )? 'from' roleName
                pass 
                root_0 = self._adaptor.nil()

                string_literal156=self.match(self.input, 80, self.FOLLOW_80_in_runDef1434)
                if self._state.backtracking == 0:

                    string_literal156_tree = self._adaptor.createWithPayload(string_literal156)
                    root_0 = self._adaptor.becomeRoot(string_literal156_tree, root_0)

                self._state.following.append(self.FOLLOW_protocolRefDef_in_runDef1437)
                protocolRefDef157 = self.protocolRefDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, protocolRefDef157.tree)
                # final_09_01-13/Monitor.g:157:31: ( '(' parameter ( ',' parameter )* ')' )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == 74) :
                    alt33 = 1
                if alt33 == 1:
                    # final_09_01-13/Monitor.g:157:33: '(' parameter ( ',' parameter )* ')'
                    pass 
                    char_literal158=self.match(self.input, 74, self.FOLLOW_74_in_runDef1441)
                    self._state.following.append(self.FOLLOW_parameter_in_runDef1444)
                    parameter159 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parameter159.tree)
                    # final_09_01-13/Monitor.g:157:48: ( ',' parameter )*
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == 71) :
                            alt32 = 1


                        if alt32 == 1:
                            # final_09_01-13/Monitor.g:157:50: ',' parameter
                            pass 
                            char_literal160=self.match(self.input, 71, self.FOLLOW_71_in_runDef1448)
                            self._state.following.append(self.FOLLOW_parameter_in_runDef1451)
                            parameter161 = self.parameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, parameter161.tree)


                        else:
                            break #loop32
                    char_literal162=self.match(self.input, 75, self.FOLLOW_75_in_runDef1456)



                string_literal163=self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_runDef1462)
                if self._state.backtracking == 0:

                    string_literal163_tree = self._adaptor.createWithPayload(string_literal163)
                    self._adaptor.addChild(root_0, string_literal163_tree)

                self._state.following.append(self.FOLLOW_roleName_in_runDef1464)
                roleName164 = self.roleName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, roleName164.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "runDef"

    class protocolRefDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.protocolRefDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "protocolRefDef"
    # final_09_01-13/Monitor.g:159:1: protocolRefDef : ID ( 'at' roleName )? ;
    def protocolRefDef(self, ):

        retval = self.protocolRefDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID165 = None
        string_literal166 = None
        roleName167 = None


        ID165_tree = None
        string_literal166_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:159:15: ( ID ( 'at' roleName )? )
                # final_09_01-13/Monitor.g:159:17: ID ( 'at' roleName )?
                pass 
                root_0 = self._adaptor.nil()

                ID165=self.match(self.input, ID, self.FOLLOW_ID_in_protocolRefDef1472)
                if self._state.backtracking == 0:

                    ID165_tree = self._adaptor.createWithPayload(ID165)
                    self._adaptor.addChild(root_0, ID165_tree)

                # final_09_01-13/Monitor.g:159:20: ( 'at' roleName )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == ATKW) :
                    alt34 = 1
                if alt34 == 1:
                    # final_09_01-13/Monitor.g:159:22: 'at' roleName
                    pass 
                    string_literal166=self.match(self.input, ATKW, self.FOLLOW_ATKW_in_protocolRefDef1476)
                    if self._state.backtracking == 0:

                        string_literal166_tree = self._adaptor.createWithPayload(string_literal166)
                        self._adaptor.addChild(root_0, string_literal166_tree)

                    self._state.following.append(self.FOLLOW_roleName_in_protocolRefDef1478)
                    roleName167 = self.roleName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, roleName167.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "protocolRefDef"

    class declarationName_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.declarationName_return, self).__init__()

            self.tree = None




    # $ANTLR start "declarationName"
    # final_09_01-13/Monitor.g:161:1: declarationName : ID ;
    def declarationName(self, ):

        retval = self.declarationName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID168 = None

        ID168_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:161:16: ( ID )
                # final_09_01-13/Monitor.g:161:18: ID
                pass 
                root_0 = self._adaptor.nil()

                ID168=self.match(self.input, ID, self.FOLLOW_ID_in_declarationName1489)
                if self._state.backtracking == 0:

                    ID168_tree = self._adaptor.createWithPayload(ID168)
                    self._adaptor.addChild(root_0, ID168_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "declarationName"

    class parameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.parameter_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameter"
    # final_09_01-13/Monitor.g:163:1: parameter : declarationName ;
    def parameter(self, ):

        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        declarationName169 = None



        try:
            try:
                # final_09_01-13/Monitor.g:163:10: ( declarationName )
                # final_09_01-13/Monitor.g:163:12: declarationName
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_declarationName_in_parameter1497)
                declarationName169 = self.declarationName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationName169.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parameter"

    class inlineDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.inlineDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "inlineDef"
    # final_09_01-13/Monitor.g:166:1: inlineDef : 'inline' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )? ;
    def inlineDef(self, ):

        retval = self.inlineDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal170 = None
        char_literal172 = None
        char_literal174 = None
        char_literal176 = None
        protocolRefDef171 = None

        parameter173 = None

        parameter175 = None


        string_literal170_tree = None
        char_literal172_tree = None
        char_literal174_tree = None
        char_literal176_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:166:10: ( 'inline' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )? )
                # final_09_01-13/Monitor.g:166:12: 'inline' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal170=self.match(self.input, 81, self.FOLLOW_81_in_inlineDef1506)
                if self._state.backtracking == 0:

                    string_literal170_tree = self._adaptor.createWithPayload(string_literal170)
                    root_0 = self._adaptor.becomeRoot(string_literal170_tree, root_0)

                self._state.following.append(self.FOLLOW_protocolRefDef_in_inlineDef1509)
                protocolRefDef171 = self.protocolRefDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, protocolRefDef171.tree)
                # final_09_01-13/Monitor.g:166:37: ( '(' parameter ( ',' parameter )* ')' )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == 74) :
                    alt36 = 1
                if alt36 == 1:
                    # final_09_01-13/Monitor.g:166:39: '(' parameter ( ',' parameter )* ')'
                    pass 
                    char_literal172=self.match(self.input, 74, self.FOLLOW_74_in_inlineDef1513)
                    self._state.following.append(self.FOLLOW_parameter_in_inlineDef1516)
                    parameter173 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parameter173.tree)
                    # final_09_01-13/Monitor.g:166:54: ( ',' parameter )*
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 == 71) :
                            alt35 = 1


                        if alt35 == 1:
                            # final_09_01-13/Monitor.g:166:56: ',' parameter
                            pass 
                            char_literal174=self.match(self.input, 71, self.FOLLOW_71_in_inlineDef1520)
                            self._state.following.append(self.FOLLOW_parameter_in_inlineDef1523)
                            parameter175 = self.parameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, parameter175.tree)


                        else:
                            break #loop35
                    char_literal176=self.match(self.input, 75, self.FOLLOW_75_in_inlineDef1528)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "inlineDef"

    class parallelDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.parallelDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "parallelDef"
    # final_09_01-13/Monitor.g:168:1: parallelDef : 'par' blockDef ( 'and' blockDef )* -> ^( PARALLEL ( blockDef )+ ) ;
    def parallelDef(self, ):

        retval = self.parallelDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal177 = None
        string_literal179 = None
        blockDef178 = None

        blockDef180 = None


        string_literal177_tree = None
        string_literal179_tree = None
        stream_PARALLELKW = RewriteRuleTokenStream(self._adaptor, "token PARALLELKW")
        stream_ANDKW = RewriteRuleTokenStream(self._adaptor, "token ANDKW")
        stream_blockDef = RewriteRuleSubtreeStream(self._adaptor, "rule blockDef")
        try:
            try:
                # final_09_01-13/Monitor.g:168:12: ( 'par' blockDef ( 'and' blockDef )* -> ^( PARALLEL ( blockDef )+ ) )
                # final_09_01-13/Monitor.g:168:14: 'par' blockDef ( 'and' blockDef )*
                pass 
                string_literal177=self.match(self.input, PARALLELKW, self.FOLLOW_PARALLELKW_in_parallelDef1540) 
                if self._state.backtracking == 0:
                    stream_PARALLELKW.add(string_literal177)
                self._state.following.append(self.FOLLOW_blockDef_in_parallelDef1542)
                blockDef178 = self.blockDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_blockDef.add(blockDef178.tree)
                # final_09_01-13/Monitor.g:168:29: ( 'and' blockDef )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == ANDKW) :
                        alt37 = 1


                    if alt37 == 1:
                        # final_09_01-13/Monitor.g:168:31: 'and' blockDef
                        pass 
                        string_literal179=self.match(self.input, ANDKW, self.FOLLOW_ANDKW_in_parallelDef1546) 
                        if self._state.backtracking == 0:
                            stream_ANDKW.add(string_literal179)
                        self._state.following.append(self.FOLLOW_blockDef_in_parallelDef1548)
                        blockDef180 = self.blockDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_blockDef.add(blockDef180.tree)


                    else:
                        break #loop37

                # AST Rewrite
                # elements: blockDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 168:49: -> ^( PARALLEL ( blockDef )+ )
                    # final_09_01-13/Monitor.g:168:52: ^( PARALLEL ( blockDef )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARALLEL, "PARALLEL"), root_1)

                    # final_09_01-13/Monitor.g:168:63: ( blockDef )+
                    if not (stream_blockDef.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_blockDef.hasNext():
                        self._adaptor.addChild(root_1, stream_blockDef.nextTree())


                    stream_blockDef.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parallelDef"

    class globalEscapeDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.globalEscapeDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalEscapeDef"
    # final_09_01-13/Monitor.g:170:1: globalEscapeDef : 'interruptible' blockDef interruptDef -> ^( INTR blockDef interruptDef ) ;
    def globalEscapeDef(self, ):

        retval = self.globalEscapeDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal181 = None
        blockDef182 = None

        interruptDef183 = None


        string_literal181_tree = None
        stream_INTERRUPTIBLEKW = RewriteRuleTokenStream(self._adaptor, "token INTERRUPTIBLEKW")
        stream_interruptDef = RewriteRuleSubtreeStream(self._adaptor, "rule interruptDef")
        stream_blockDef = RewriteRuleSubtreeStream(self._adaptor, "rule blockDef")
        try:
            try:
                # final_09_01-13/Monitor.g:170:16: ( 'interruptible' blockDef interruptDef -> ^( INTR blockDef interruptDef ) )
                # final_09_01-13/Monitor.g:170:18: 'interruptible' blockDef interruptDef
                pass 
                string_literal181=self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_globalEscapeDef1567) 
                if self._state.backtracking == 0:
                    stream_INTERRUPTIBLEKW.add(string_literal181)
                self._state.following.append(self.FOLLOW_blockDef_in_globalEscapeDef1569)
                blockDef182 = self.blockDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_blockDef.add(blockDef182.tree)
                self._state.following.append(self.FOLLOW_interruptDef_in_globalEscapeDef1571)
                interruptDef183 = self.interruptDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_interruptDef.add(interruptDef183.tree)

                # AST Rewrite
                # elements: blockDef, interruptDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 170:56: -> ^( INTR blockDef interruptDef )
                    # final_09_01-13/Monitor.g:170:59: ^( INTR blockDef interruptDef )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INTR, "INTR"), root_1)

                    self._adaptor.addChild(root_1, stream_blockDef.nextTree())
                    self._adaptor.addChild(root_1, stream_interruptDef.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "globalEscapeDef"

    class interruptDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.interruptDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "interruptDef"
    # final_09_01-13/Monitor.g:173:1: interruptDef : 'with' ( 'throw' interactionSignatureDef ( ',' interactionSignatureDef )* 'by' roleName ( ',' roleName )* ';' -> ^( 'throw' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) ) | 'catch' interactionSignatureDef ( ',' interactionSignatureDef )* 'by' roleName ( ',' roleName )* ';' -> ^( 'catch' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) ) ) ;
    def interruptDef(self, ):

        retval = self.interruptDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal184 = None
        string_literal185 = None
        char_literal187 = None
        string_literal189 = None
        char_literal191 = None
        char_literal193 = None
        string_literal194 = None
        char_literal196 = None
        string_literal198 = None
        char_literal200 = None
        char_literal202 = None
        interactionSignatureDef186 = None

        interactionSignatureDef188 = None

        roleName190 = None

        roleName192 = None

        interactionSignatureDef195 = None

        interactionSignatureDef197 = None

        roleName199 = None

        roleName201 = None


        string_literal184_tree = None
        string_literal185_tree = None
        char_literal187_tree = None
        string_literal189_tree = None
        char_literal191_tree = None
        char_literal193_tree = None
        string_literal194_tree = None
        char_literal196_tree = None
        string_literal198_tree = None
        char_literal200_tree = None
        char_literal202_tree = None
        stream_68 = RewriteRuleTokenStream(self._adaptor, "token 68")
        stream_WITHKW = RewriteRuleTokenStream(self._adaptor, "token WITHKW")
        stream_82 = RewriteRuleTokenStream(self._adaptor, "token 82")
        stream_83 = RewriteRuleTokenStream(self._adaptor, "token 83")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_BYKW = RewriteRuleTokenStream(self._adaptor, "token BYKW")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        stream_interactionSignatureDef = RewriteRuleSubtreeStream(self._adaptor, "rule interactionSignatureDef")
        try:
            try:
                # final_09_01-13/Monitor.g:173:14: ( 'with' ( 'throw' interactionSignatureDef ( ',' interactionSignatureDef )* 'by' roleName ( ',' roleName )* ';' -> ^( 'throw' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) ) | 'catch' interactionSignatureDef ( ',' interactionSignatureDef )* 'by' roleName ( ',' roleName )* ';' -> ^( 'catch' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) ) ) )
                # final_09_01-13/Monitor.g:173:16: 'with' ( 'throw' interactionSignatureDef ( ',' interactionSignatureDef )* 'by' roleName ( ',' roleName )* ';' -> ^( 'throw' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) ) | 'catch' interactionSignatureDef ( ',' interactionSignatureDef )* 'by' roleName ( ',' roleName )* ';' -> ^( 'catch' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) ) )
                pass 
                string_literal184=self.match(self.input, WITHKW, self.FOLLOW_WITHKW_in_interruptDef1590) 
                if self._state.backtracking == 0:
                    stream_WITHKW.add(string_literal184)
                # final_09_01-13/Monitor.g:173:23: ( 'throw' interactionSignatureDef ( ',' interactionSignatureDef )* 'by' roleName ( ',' roleName )* ';' -> ^( 'throw' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) ) | 'catch' interactionSignatureDef ( ',' interactionSignatureDef )* 'by' roleName ( ',' roleName )* ';' -> ^( 'catch' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) ) )
                alt42 = 2
                LA42_0 = self.input.LA(1)

                if (LA42_0 == 82) :
                    alt42 = 1
                elif (LA42_0 == 83) :
                    alt42 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 42, 0, self.input)

                    raise nvae

                if alt42 == 1:
                    # final_09_01-13/Monitor.g:174:8: 'throw' interactionSignatureDef ( ',' interactionSignatureDef )* 'by' roleName ( ',' roleName )* ';'
                    pass 
                    string_literal185=self.match(self.input, 82, self.FOLLOW_82_in_interruptDef1601) 
                    if self._state.backtracking == 0:
                        stream_82.add(string_literal185)
                    self._state.following.append(self.FOLLOW_interactionSignatureDef_in_interruptDef1603)
                    interactionSignatureDef186 = self.interactionSignatureDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_interactionSignatureDef.add(interactionSignatureDef186.tree)
                    # final_09_01-13/Monitor.g:174:40: ( ',' interactionSignatureDef )*
                    while True: #loop38
                        alt38 = 2
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == 71) :
                            alt38 = 1


                        if alt38 == 1:
                            # final_09_01-13/Monitor.g:174:41: ',' interactionSignatureDef
                            pass 
                            char_literal187=self.match(self.input, 71, self.FOLLOW_71_in_interruptDef1606) 
                            if self._state.backtracking == 0:
                                stream_71.add(char_literal187)
                            self._state.following.append(self.FOLLOW_interactionSignatureDef_in_interruptDef1608)
                            interactionSignatureDef188 = self.interactionSignatureDef()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_interactionSignatureDef.add(interactionSignatureDef188.tree)


                        else:
                            break #loop38
                    string_literal189=self.match(self.input, BYKW, self.FOLLOW_BYKW_in_interruptDef1612) 
                    if self._state.backtracking == 0:
                        stream_BYKW.add(string_literal189)
                    self._state.following.append(self.FOLLOW_roleName_in_interruptDef1614)
                    roleName190 = self.roleName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleName.add(roleName190.tree)
                    # final_09_01-13/Monitor.g:174:85: ( ',' roleName )*
                    while True: #loop39
                        alt39 = 2
                        LA39_0 = self.input.LA(1)

                        if (LA39_0 == 71) :
                            alt39 = 1


                        if alt39 == 1:
                            # final_09_01-13/Monitor.g:174:86: ',' roleName
                            pass 
                            char_literal191=self.match(self.input, 71, self.FOLLOW_71_in_interruptDef1617) 
                            if self._state.backtracking == 0:
                                stream_71.add(char_literal191)
                            self._state.following.append(self.FOLLOW_roleName_in_interruptDef1619)
                            roleName192 = self.roleName()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_roleName.add(roleName192.tree)


                        else:
                            break #loop39
                    char_literal193=self.match(self.input, 68, self.FOLLOW_68_in_interruptDef1624) 
                    if self._state.backtracking == 0:
                        stream_68.add(char_literal193)

                    # AST Rewrite
                    # elements: BYKW, 82, roleName, interactionSignatureDef
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 174:105: -> ^( 'throw' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) )
                        # final_09_01-13/Monitor.g:174:108: ^( 'throw' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_82.nextNode(), root_1)

                        # final_09_01-13/Monitor.g:174:118: ( interactionSignatureDef )+
                        if not (stream_interactionSignatureDef.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_interactionSignatureDef.hasNext():
                            self._adaptor.addChild(root_1, stream_interactionSignatureDef.nextTree())


                        stream_interactionSignatureDef.reset()
                        # final_09_01-13/Monitor.g:174:143: ^( 'by' ( roleName )+ )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(stream_BYKW.nextNode(), root_2)

                        # final_09_01-13/Monitor.g:174:150: ( roleName )+
                        if not (stream_roleName.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_roleName.hasNext():
                            self._adaptor.addChild(root_2, stream_roleName.nextTree())


                        stream_roleName.reset()

                        self._adaptor.addChild(root_1, root_2)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt42 == 2:
                    # final_09_01-13/Monitor.g:175:23: 'catch' interactionSignatureDef ( ',' interactionSignatureDef )* 'by' roleName ( ',' roleName )* ';'
                    pass 
                    string_literal194=self.match(self.input, 83, self.FOLLOW_83_in_interruptDef1663) 
                    if self._state.backtracking == 0:
                        stream_83.add(string_literal194)
                    self._state.following.append(self.FOLLOW_interactionSignatureDef_in_interruptDef1665)
                    interactionSignatureDef195 = self.interactionSignatureDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_interactionSignatureDef.add(interactionSignatureDef195.tree)
                    # final_09_01-13/Monitor.g:175:55: ( ',' interactionSignatureDef )*
                    while True: #loop40
                        alt40 = 2
                        LA40_0 = self.input.LA(1)

                        if (LA40_0 == 71) :
                            alt40 = 1


                        if alt40 == 1:
                            # final_09_01-13/Monitor.g:175:56: ',' interactionSignatureDef
                            pass 
                            char_literal196=self.match(self.input, 71, self.FOLLOW_71_in_interruptDef1668) 
                            if self._state.backtracking == 0:
                                stream_71.add(char_literal196)
                            self._state.following.append(self.FOLLOW_interactionSignatureDef_in_interruptDef1670)
                            interactionSignatureDef197 = self.interactionSignatureDef()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_interactionSignatureDef.add(interactionSignatureDef197.tree)


                        else:
                            break #loop40
                    string_literal198=self.match(self.input, BYKW, self.FOLLOW_BYKW_in_interruptDef1674) 
                    if self._state.backtracking == 0:
                        stream_BYKW.add(string_literal198)
                    self._state.following.append(self.FOLLOW_roleName_in_interruptDef1676)
                    roleName199 = self.roleName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleName.add(roleName199.tree)
                    # final_09_01-13/Monitor.g:175:100: ( ',' roleName )*
                    while True: #loop41
                        alt41 = 2
                        LA41_0 = self.input.LA(1)

                        if (LA41_0 == 71) :
                            alt41 = 1


                        if alt41 == 1:
                            # final_09_01-13/Monitor.g:175:101: ',' roleName
                            pass 
                            char_literal200=self.match(self.input, 71, self.FOLLOW_71_in_interruptDef1679) 
                            if self._state.backtracking == 0:
                                stream_71.add(char_literal200)
                            self._state.following.append(self.FOLLOW_roleName_in_interruptDef1681)
                            roleName201 = self.roleName()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_roleName.add(roleName201.tree)


                        else:
                            break #loop41
                    char_literal202=self.match(self.input, 68, self.FOLLOW_68_in_interruptDef1686) 
                    if self._state.backtracking == 0:
                        stream_68.add(char_literal202)

                    # AST Rewrite
                    # elements: BYKW, interactionSignatureDef, 83, roleName
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 175:120: -> ^( 'catch' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) )
                        # final_09_01-13/Monitor.g:175:123: ^( 'catch' ( interactionSignatureDef )+ ^( 'by' ( roleName )+ ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_83.nextNode(), root_1)

                        # final_09_01-13/Monitor.g:175:133: ( interactionSignatureDef )+
                        if not (stream_interactionSignatureDef.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_interactionSignatureDef.hasNext():
                            self._adaptor.addChild(root_1, stream_interactionSignatureDef.nextTree())


                        stream_interactionSignatureDef.reset()
                        # final_09_01-13/Monitor.g:175:158: ^( 'by' ( roleName )+ )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(stream_BYKW.nextNode(), root_2)

                        # final_09_01-13/Monitor.g:175:165: ( roleName )+
                        if not (stream_roleName.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_roleName.hasNext():
                            self._adaptor.addChild(root_2, stream_roleName.nextTree())


                        stream_roleName.reset()

                        self._adaptor.addChild(root_1, root_2)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "interruptDef"

    class unorderedDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.unorderedDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "unorderedDef"
    # final_09_01-13/Monitor.g:177:1: unorderedDef : 'unordered' '{' ( activityDef )* '}' -> ^( PARALLEL ( ^( BRANCH activityDef ) )+ ) ;
    def unorderedDef(self, ):

        retval = self.unorderedDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal203 = None
        char_literal204 = None
        char_literal206 = None
        activityDef205 = None


        string_literal203_tree = None
        char_literal204_tree = None
        char_literal206_tree = None
        stream_72 = RewriteRuleTokenStream(self._adaptor, "token 72")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_84 = RewriteRuleTokenStream(self._adaptor, "token 84")
        stream_activityDef = RewriteRuleSubtreeStream(self._adaptor, "rule activityDef")
        try:
            try:
                # final_09_01-13/Monitor.g:177:13: ( 'unordered' '{' ( activityDef )* '}' -> ^( PARALLEL ( ^( BRANCH activityDef ) )+ ) )
                # final_09_01-13/Monitor.g:177:15: 'unordered' '{' ( activityDef )* '}'
                pass 
                string_literal203=self.match(self.input, 84, self.FOLLOW_84_in_unorderedDef1709) 
                if self._state.backtracking == 0:
                    stream_84.add(string_literal203)
                char_literal204=self.match(self.input, 72, self.FOLLOW_72_in_unorderedDef1711) 
                if self._state.backtracking == 0:
                    stream_72.add(char_literal204)
                # final_09_01-13/Monitor.g:177:31: ( activityDef )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if ((FROMKW <= LA43_0 <= CHOICEKW) or (RECKW <= LA43_0 <= PARALLELKW) or LA43_0 == INTERRUPTIBLEKW or LA43_0 == DOKW or LA43_0 == ID or LA43_0 == 72 or LA43_0 == 74 or (78 <= LA43_0 <= 81) or LA43_0 == 84) :
                        alt43 = 1


                    if alt43 == 1:
                        # final_09_01-13/Monitor.g:177:33: activityDef
                        pass 
                        self._state.following.append(self.FOLLOW_activityDef_in_unorderedDef1715)
                        activityDef205 = self.activityDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_activityDef.add(activityDef205.tree)


                    else:
                        break #loop43
                char_literal206=self.match(self.input, 73, self.FOLLOW_73_in_unorderedDef1720) 
                if self._state.backtracking == 0:
                    stream_73.add(char_literal206)

                # AST Rewrite
                # elements: activityDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 177:52: -> ^( PARALLEL ( ^( BRANCH activityDef ) )+ )
                    # final_09_01-13/Monitor.g:177:55: ^( PARALLEL ( ^( BRANCH activityDef ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARALLEL, "PARALLEL"), root_1)

                    # final_09_01-13/Monitor.g:177:66: ( ^( BRANCH activityDef ) )+
                    if not (stream_activityDef.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_activityDef.hasNext():
                        # final_09_01-13/Monitor.g:177:66: ^( BRANCH activityDef )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(BRANCH, "BRANCH"), root_2)

                        self._adaptor.addChild(root_2, stream_activityDef.nextTree())

                        self._adaptor.addChild(root_1, root_2)


                    stream_activityDef.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "unorderedDef"

    class aliasDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.aliasDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "aliasDef"
    # final_09_01-13/Monitor.g:179:1: aliasDef : roleName 'as' ID -> ^( 'as' roleName ID ) ;
    def aliasDef(self, ):

        retval = self.aliasDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal208 = None
        ID209 = None
        roleName207 = None


        string_literal208_tree = None
        ID209_tree = None
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        try:
            try:
                # final_09_01-13/Monitor.g:179:9: ( roleName 'as' ID -> ^( 'as' roleName ID ) )
                # final_09_01-13/Monitor.g:179:11: roleName 'as' ID
                pass 
                self._state.following.append(self.FOLLOW_roleName_in_aliasDef1740)
                roleName207 = self.roleName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleName.add(roleName207.tree)
                string_literal208=self.match(self.input, ASKW, self.FOLLOW_ASKW_in_aliasDef1742) 
                if self._state.backtracking == 0:
                    stream_ASKW.add(string_literal208)
                ID209=self.match(self.input, ID, self.FOLLOW_ID_in_aliasDef1744) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID209)

                # AST Rewrite
                # elements: ASKW, ID, roleName
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 179:28: -> ^( 'as' roleName ID )
                    # final_09_01-13/Monitor.g:179:31: ^( 'as' roleName ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_ASKW.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_roleName.nextTree())
                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "aliasDef"

    class doDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.doDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "doDef"
    # final_09_01-13/Monitor.g:182:1: doDef : 'do' EXTID ( '<' interactionSignatureDef ( ',' interactionSignatureDef )* '>' )? '(' aliasDef ( ',' aliasDef )* ')' -> ^( DO EXTID ^( PARAMETERLIST ( interactionSignatureDef )* ) ^( ROLES ( aliasDef )+ ) ) ;
    def doDef(self, ):

        retval = self.doDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal210 = None
        EXTID211 = None
        char_literal212 = None
        char_literal214 = None
        char_literal216 = None
        char_literal217 = None
        char_literal219 = None
        char_literal221 = None
        interactionSignatureDef213 = None

        interactionSignatureDef215 = None

        aliasDef218 = None

        aliasDef220 = None


        string_literal210_tree = None
        EXTID211_tree = None
        char_literal212_tree = None
        char_literal214_tree = None
        char_literal216_tree = None
        char_literal217_tree = None
        char_literal219_tree = None
        char_literal221_tree = None
        stream_69 = RewriteRuleTokenStream(self._adaptor, "token 69")
        stream_DOKW = RewriteRuleTokenStream(self._adaptor, "token DOKW")
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_EXTID = RewriteRuleTokenStream(self._adaptor, "token EXTID")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_75 = RewriteRuleTokenStream(self._adaptor, "token 75")
        stream_aliasDef = RewriteRuleSubtreeStream(self._adaptor, "rule aliasDef")
        stream_interactionSignatureDef = RewriteRuleSubtreeStream(self._adaptor, "rule interactionSignatureDef")
        try:
            try:
                # final_09_01-13/Monitor.g:182:6: ( 'do' EXTID ( '<' interactionSignatureDef ( ',' interactionSignatureDef )* '>' )? '(' aliasDef ( ',' aliasDef )* ')' -> ^( DO EXTID ^( PARAMETERLIST ( interactionSignatureDef )* ) ^( ROLES ( aliasDef )+ ) ) )
                # final_09_01-13/Monitor.g:182:8: 'do' EXTID ( '<' interactionSignatureDef ( ',' interactionSignatureDef )* '>' )? '(' aliasDef ( ',' aliasDef )* ')'
                pass 
                string_literal210=self.match(self.input, DOKW, self.FOLLOW_DOKW_in_doDef1765) 
                if self._state.backtracking == 0:
                    stream_DOKW.add(string_literal210)
                EXTID211=self.match(self.input, EXTID, self.FOLLOW_EXTID_in_doDef1767) 
                if self._state.backtracking == 0:
                    stream_EXTID.add(EXTID211)
                # final_09_01-13/Monitor.g:182:19: ( '<' interactionSignatureDef ( ',' interactionSignatureDef )* '>' )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if (LA45_0 == 69) :
                    alt45 = 1
                if alt45 == 1:
                    # final_09_01-13/Monitor.g:182:20: '<' interactionSignatureDef ( ',' interactionSignatureDef )* '>'
                    pass 
                    char_literal212=self.match(self.input, 69, self.FOLLOW_69_in_doDef1770) 
                    if self._state.backtracking == 0:
                        stream_69.add(char_literal212)
                    self._state.following.append(self.FOLLOW_interactionSignatureDef_in_doDef1772)
                    interactionSignatureDef213 = self.interactionSignatureDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_interactionSignatureDef.add(interactionSignatureDef213.tree)
                    # final_09_01-13/Monitor.g:182:48: ( ',' interactionSignatureDef )*
                    while True: #loop44
                        alt44 = 2
                        LA44_0 = self.input.LA(1)

                        if (LA44_0 == 71) :
                            alt44 = 1


                        if alt44 == 1:
                            # final_09_01-13/Monitor.g:182:49: ',' interactionSignatureDef
                            pass 
                            char_literal214=self.match(self.input, 71, self.FOLLOW_71_in_doDef1775) 
                            if self._state.backtracking == 0:
                                stream_71.add(char_literal214)
                            self._state.following.append(self.FOLLOW_interactionSignatureDef_in_doDef1777)
                            interactionSignatureDef215 = self.interactionSignatureDef()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_interactionSignatureDef.add(interactionSignatureDef215.tree)


                        else:
                            break #loop44
                    char_literal216=self.match(self.input, 70, self.FOLLOW_70_in_doDef1781) 
                    if self._state.backtracking == 0:
                        stream_70.add(char_literal216)



                char_literal217=self.match(self.input, 74, self.FOLLOW_74_in_doDef1785) 
                if self._state.backtracking == 0:
                    stream_74.add(char_literal217)
                self._state.following.append(self.FOLLOW_aliasDef_in_doDef1787)
                aliasDef218 = self.aliasDef()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_aliasDef.add(aliasDef218.tree)
                # final_09_01-13/Monitor.g:182:98: ( ',' aliasDef )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == 71) :
                        alt46 = 1


                    if alt46 == 1:
                        # final_09_01-13/Monitor.g:182:99: ',' aliasDef
                        pass 
                        char_literal219=self.match(self.input, 71, self.FOLLOW_71_in_doDef1790) 
                        if self._state.backtracking == 0:
                            stream_71.add(char_literal219)
                        self._state.following.append(self.FOLLOW_aliasDef_in_doDef1792)
                        aliasDef220 = self.aliasDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_aliasDef.add(aliasDef220.tree)


                    else:
                        break #loop46
                char_literal221=self.match(self.input, 75, self.FOLLOW_75_in_doDef1796) 
                if self._state.backtracking == 0:
                    stream_75.add(char_literal221)

                # AST Rewrite
                # elements: aliasDef, EXTID, interactionSignatureDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 182:118: -> ^( DO EXTID ^( PARAMETERLIST ( interactionSignatureDef )* ) ^( ROLES ( aliasDef )+ ) )
                    # final_09_01-13/Monitor.g:182:121: ^( DO EXTID ^( PARAMETERLIST ( interactionSignatureDef )* ) ^( ROLES ( aliasDef )+ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(DO, "DO"), root_1)

                    self._adaptor.addChild(root_1, stream_EXTID.nextNode())
                    # final_09_01-13/Monitor.g:182:132: ^( PARAMETERLIST ( interactionSignatureDef )* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMETERLIST, "PARAMETERLIST"), root_2)

                    # final_09_01-13/Monitor.g:182:148: ( interactionSignatureDef )*
                    while stream_interactionSignatureDef.hasNext():
                        self._adaptor.addChild(root_2, stream_interactionSignatureDef.nextTree())


                    stream_interactionSignatureDef.reset();

                    self._adaptor.addChild(root_1, root_2)
                    # final_09_01-13/Monitor.g:182:174: ^( ROLES ( aliasDef )+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROLES, "ROLES"), root_2)

                    # final_09_01-13/Monitor.g:182:182: ( aliasDef )+
                    if not (stream_aliasDef.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_aliasDef.hasNext():
                        self._adaptor.addChild(root_2, stream_aliasDef.nextTree())


                    stream_aliasDef.reset()

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "doDef"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # final_09_01-13/Monitor.g:192:1: expr : term ( ( PLUS | MINUS ) term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set223 = None
        term222 = None

        term224 = None


        set223_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:192:6: ( term ( ( PLUS | MINUS ) term )* )
                # final_09_01-13/Monitor.g:192:8: term ( ( PLUS | MINUS ) term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1835)
                term222 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term222.tree)
                # final_09_01-13/Monitor.g:192:13: ( ( PLUS | MINUS ) term )*
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if ((PLUS <= LA47_0 <= MINUS)) :
                        alt47 = 1


                    if alt47 == 1:
                        # final_09_01-13/Monitor.g:192:15: ( PLUS | MINUS ) term
                        pass 
                        set223 = self.input.LT(1)
                        if (PLUS <= self.input.LA(1) <= MINUS):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set223))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_term_in_expr1850)
                        term224 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term224.tree)


                    else:
                        break #loop47



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "expr"

    class term_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.term_return, self).__init__()

            self.tree = None




    # $ANTLR start "term"
    # final_09_01-13/Monitor.g:194:1: term : factor ( ( MULT | DIV ) factor )* ;
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set226 = None
        factor225 = None

        factor227 = None


        set226_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:194:6: ( factor ( ( MULT | DIV ) factor )* )
                # final_09_01-13/Monitor.g:194:8: factor ( ( MULT | DIV ) factor )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_factor_in_term1862)
                factor225 = self.factor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, factor225.tree)
                # final_09_01-13/Monitor.g:194:15: ( ( MULT | DIV ) factor )*
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if ((MULT <= LA48_0 <= DIV)) :
                        alt48 = 1


                    if alt48 == 1:
                        # final_09_01-13/Monitor.g:194:17: ( MULT | DIV ) factor
                        pass 
                        set226 = self.input.LT(1)
                        if (MULT <= self.input.LA(1) <= DIV):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set226))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_factor_in_term1876)
                        factor227 = self.factor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, factor227.tree)


                    else:
                        break #loop48



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "term"

    class factor_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.factor_return, self).__init__()

            self.tree = None




    # $ANTLR start "factor"
    # final_09_01-13/Monitor.g:196:1: factor : NUMBER ;
    def factor(self, ):

        retval = self.factor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NUMBER228 = None

        NUMBER228_tree = None

        try:
            try:
                # final_09_01-13/Monitor.g:196:8: ( NUMBER )
                # final_09_01-13/Monitor.g:196:10: NUMBER
                pass 
                root_0 = self._adaptor.nil()

                NUMBER228=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_factor1888)
                if self._state.backtracking == 0:

                    NUMBER228_tree = self._adaptor.createWithPayload(NUMBER228)
                    self._adaptor.addChild(root_0, NUMBER228_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "factor"

    # $ANTLR start "synpred1_Monitor"
    def synpred1_Monitor_fragment(self, ):
        # final_09_01-13/Monitor.g:78:22: ( importdecl )
        # final_09_01-13/Monitor.g:78:22: importdecl
        pass 
        self._state.following.append(self.FOLLOW_importdecl_in_synpred1_Monitor509)
        self.importdecl()

        self._state.following.pop()


    # $ANTLR end "synpred1_Monitor"



    # $ANTLR start "synpred3_Monitor"
    def synpred3_Monitor_fragment(self, ):
        # final_09_01-13/Monitor.g:78:55: ( protocolDef )
        # final_09_01-13/Monitor.g:78:55: protocolDef
        pass 
        self._state.following.append(self.FOLLOW_protocolDef_in_synpred3_Monitor519)
        self.protocolDef()

        self._state.following.pop()


    # $ANTLR end "synpred3_Monitor"



    # $ANTLR start "synpred8_Monitor"
    def synpred8_Monitor_fragment(self, ):
        # final_09_01-13/Monitor.g:90:18: ( packagedecl )
        # final_09_01-13/Monitor.g:90:18: packagedecl
        pass 
        self._state.following.append(self.FOLLOW_packagedecl_in_synpred8_Monitor647)
        self.packagedecl()

        self._state.following.pop()


    # $ANTLR end "synpred8_Monitor"




    # Delegated rules

    def synpred1_Monitor(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_Monitor_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred3_Monitor(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred3_Monitor_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred8_Monitor(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred8_Monitor_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #1

    DFA1_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA1_eof = DFA.unpack(
        u"\1\1\21\uffff"
        )

    DFA1_min = DFA.unpack(
        u"\1\36\1\uffff\2\70\2\13\1\70\1\0\1\70\1\13\1\uffff\1\13\1\70\1"
        u"\64\1\70\1\0\1\104\1\0"
        )

    DFA1_max = DFA.unpack(
        u"\1\47\1\uffff\2\70\1\104\1\13\1\70\1\0\1\70\1\104\1\uffff\1\37"
        u"\1\70\1\104\1\70\1\0\1\104\1\0"
        )

    DFA1_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1\7\uffff"
        )

    DFA1_special = DFA.unpack(
        u"\7\uffff\1\0\7\uffff\1\2\1\uffff\1\1"
        )

            
    DFA1_transition = [
        DFA.unpack(u"\1\1\1\2\1\1\2\uffff\1\1\3\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\6\70\uffff\1\7"),
        DFA.unpack(u"\1\10"),
        DFA.unpack(u"\1\11"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u"\1\6\70\uffff\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\10\23\uffff\1\14"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\16\17\uffff\1\17"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\21"),
        DFA.unpack(u"\1\uffff")
    ]

    # class definition for DFA #1

    class DFA1(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA1_7 = input.LA(1)

                 
                index1_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_Monitor()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index1_7)
                if s >= 0:
                    return s
            elif s == 1: 
                LA1_17 = input.LA(1)

                 
                index1_17 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_Monitor()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index1_17)
                if s >= 0:
                    return s
            elif s == 2: 
                LA1_15 = input.LA(1)

                 
                index1_15 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_Monitor()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index1_15)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 1, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\37\1\uffff\1\70\1\13\1\70\1\13\1\70\1\64\2\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\1\47\1\uffff\1\70\1\13\1\70\1\37\1\70\1\104\2\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\1\uffff\1\1\6\uffff\1\3\1\2"
        )

    DFA6_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA6_transition = [
        DFA.unpack(u"\1\1\7\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\4\23\uffff\1\6"),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u"\1\10\17\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #6

    class DFA6(DFA):
        pass


    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\36\1\70\1\uffff\1\13\1\70\1\0\1\13\2\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\47\1\70\1\uffff\1\104\1\70\1\0\1\104\2\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\2\uffff\1\2\4\uffff\1\1\1\3"
        )

    DFA7_special = DFA.unpack(
        u"\5\uffff\1\0\3\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\1\1\1\2\7\uffff\1\2"),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\70\uffff\1\5"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\4\70\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    class DFA7(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA7_5 = input.LA(1)

                 
                index7_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred8_Monitor()):
                    s = 7

                elif (True):
                    s = 8

                 
                input.seek(index7_5)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 7, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #29

    DFA29_eot = DFA.unpack(
        u"\32\uffff"
        )

    DFA29_eof = DFA.unpack(
        u"\1\1\31\uffff"
        )

    DFA29_min = DFA.unpack(
        u"\1\47\1\uffff\1\47\1\70\1\uffff\1\70\2\107\1\47\1\5\1\70\1\47\1"
        u"\5\1\70\6\107\2\5\4\107"
        )

    DFA29_max = DFA.unpack(
        u"\1\124\1\uffff\1\115\1\70\1\uffff\1\113\3\115\1\6\1\70\1\115\1"
        u"\6\1\70\2\113\1\115\2\113\1\115\2\6\4\113"
        )

    DFA29_accept = DFA.unpack(
        u"\1\uffff\1\2\2\uffff\1\1\25\uffff"
        )

    DFA29_special = DFA.unpack(
        u"\32\uffff"
        )

            
    DFA29_transition = [
        DFA.unpack(u"\3\4\2\uffff\3\4\1\uffff\1\4\2\uffff\1\4\4\uffff\1\2"
        u"\17\uffff\1\4\1\1\1\3\3\uffff\4\4\2\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\4\41\uffff\1\5\1\uffff\1\4\1\1"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\22\uffff\1\10"),
        DFA.unpack(u"\1\12\3\uffff\1\13\1\uffff\1\11"),
        DFA.unpack(u"\1\15\3\uffff\1\10\1\uffff\1\14"),
        DFA.unpack(u"\2\4\44\uffff\1\1"),
        DFA.unpack(u"\1\16\1\17"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\2\4\44\uffff\1\1"),
        DFA.unpack(u"\1\21\1\22"),
        DFA.unpack(u"\1\23"),
        DFA.unpack(u"\1\12\3\uffff\1\13"),
        DFA.unpack(u"\1\12\3\uffff\1\13"),
        DFA.unpack(u"\1\12\3\uffff\1\13\1\uffff\1\24"),
        DFA.unpack(u"\1\15\3\uffff\1\10"),
        DFA.unpack(u"\1\15\3\uffff\1\10"),
        DFA.unpack(u"\1\15\3\uffff\1\10\1\uffff\1\25"),
        DFA.unpack(u"\1\26\1\27"),
        DFA.unpack(u"\1\30\1\31"),
        DFA.unpack(u"\1\12\3\uffff\1\13"),
        DFA.unpack(u"\1\12\3\uffff\1\13"),
        DFA.unpack(u"\1\15\3\uffff\1\10"),
        DFA.unpack(u"\1\15\3\uffff\1\10")
    ]

    # class definition for DFA #29

    class DFA29(DFA):
        pass


 

    FOLLOW_packagedecl_in_module506 = frozenset([1, 31, 32, 35, 39])
    FOLLOW_importdecl_in_module509 = frozenset([1, 31, 32, 35, 39])
    FOLLOW_payloadtypedecl_in_module514 = frozenset([1, 32, 35])
    FOLLOW_protocolDef_in_module519 = frozenset([1, 35])
    FOLLOW_PACKAGEKW_in_packagedecl527 = frozenset([56])
    FOLLOW_packagename_in_packagedecl529 = frozenset([68])
    FOLLOW_68_in_packagedecl531 = frozenset([1])
    FOLLOW_ID_in_packagename538 = frozenset([1, 11])
    FOLLOW_FULLSTOP_in_packagename541 = frozenset([56])
    FOLLOW_ID_in_packagename543 = frozenset([1, 11])
    FOLLOW_IMPORTKW_in_importdecl552 = frozenset([56])
    FOLLOW_ID_in_importdecl554 = frozenset([11, 68])
    FOLLOW_FULLSTOP_in_importdecl557 = frozenset([56])
    FOLLOW_ID_in_importdecl559 = frozenset([11, 68])
    FOLLOW_68_in_importdecl563 = frozenset([1])
    FOLLOW_FROMKW_in_importdecl572 = frozenset([56])
    FOLLOW_packagename_in_importdecl574 = frozenset([11])
    FOLLOW_FULLSTOP_in_importdecl576 = frozenset([56])
    FOLLOW_ID_in_importdecl578 = frozenset([31])
    FOLLOW_IMPORTKW_in_importdecl580 = frozenset([56])
    FOLLOW_ID_in_importdecl582 = frozenset([68])
    FOLLOW_68_in_importdecl584 = frozenset([1])
    FOLLOW_FROMKW_in_importdecl593 = frozenset([56])
    FOLLOW_packagename_in_importdecl595 = frozenset([11])
    FOLLOW_FULLSTOP_in_importdecl597 = frozenset([56])
    FOLLOW_ID_in_importdecl599 = frozenset([31])
    FOLLOW_IMPORTKW_in_importdecl601 = frozenset([56])
    FOLLOW_ID_in_importdecl603 = frozenset([52])
    FOLLOW_ASKW_in_importdecl605 = frozenset([56])
    FOLLOW_ID_in_importdecl607 = frozenset([68])
    FOLLOW_68_in_importdecl609 = frozenset([1])
    FOLLOW_TYPEKW_in_payloadtypedecl618 = frozenset([69])
    FOLLOW_69_in_payloadtypedecl620 = frozenset([56])
    FOLLOW_ID_in_payloadtypedecl622 = frozenset([70])
    FOLLOW_70_in_payloadtypedecl624 = frozenset([57])
    FOLLOW_EXTID_in_payloadtypedecl626 = frozenset([39])
    FOLLOW_FROMKW_in_payloadtypedecl628 = frozenset([57])
    FOLLOW_EXTID_in_payloadtypedecl630 = frozenset([52])
    FOLLOW_ASKW_in_payloadtypedecl632 = frozenset([56])
    FOLLOW_ID_in_payloadtypedecl634 = frozenset([68])
    FOLLOW_68_in_payloadtypedecl636 = frozenset([1])
    FOLLOW_packagedecl_in_description647 = frozenset([30, 31, 35, 39])
    FOLLOW_importdecl_in_description651 = frozenset([30, 31, 35, 39])
    FOLLOW_module_in_description655 = frozenset([30, 31, 35, 39])
    FOLLOW_protocolDef_in_description662 = frozenset([1])
    FOLLOW_69_in_parameterList673 = frozenset([37])
    FOLLOW_SIGKW_in_parameterList675 = frozenset([56])
    FOLLOW_ID_in_parameterList677 = frozenset([70, 71])
    FOLLOW_71_in_parameterList680 = frozenset([37])
    FOLLOW_SIGKW_in_parameterList682 = frozenset([56])
    FOLLOW_ID_in_parameterList684 = frozenset([70, 71])
    FOLLOW_70_in_parameterList688 = frozenset([1])
    FOLLOW_LOCALKW_in_protocolDef706 = frozenset([33])
    FOLLOW_PROTOCOLKW_in_protocolDef708 = frozenset([56])
    FOLLOW_protocolName_in_protocolDef710 = frozenset([42])
    FOLLOW_ATKW_in_protocolDef714 = frozenset([56])
    FOLLOW_roleName_in_protocolDef716 = frozenset([69, 74])
    FOLLOW_parameterList_in_protocolDef723 = frozenset([69, 74])
    FOLLOW_roleList_in_protocolDef728 = frozenset([72])
    FOLLOW_72_in_protocolDef730 = frozenset([39, 40, 41, 44, 45, 46, 48, 51, 56, 72, 74, 78, 79, 80, 81, 84])
    FOLLOW_protocolBlockDef_in_protocolDef734 = frozenset([73])
    FOLLOW_73_in_protocolDef738 = frozenset([1])
    FOLLOW_74_in_roleList768 = frozenset([36])
    FOLLOW_roleparameDef_in_roleList770 = frozenset([71, 75])
    FOLLOW_71_in_roleList774 = frozenset([36])
    FOLLOW_roleparameDef_in_roleList776 = frozenset([71, 75])
    FOLLOW_75_in_roleList781 = frozenset([1])
    FOLLOW_ID_in_protocolName796 = frozenset([1])
    FOLLOW_ROLEKW_in_roleparameDef802 = frozenset([56])
    FOLLOW_ID_in_roleparameDef804 = frozenset([1])
    FOLLOW_activityListDef_in_protocolBlockDef815 = frozenset([1])
    FOLLOW_72_in_blockDef827 = frozenset([39, 40, 41, 44, 45, 46, 48, 51, 56, 72, 73, 74, 78, 79, 80, 81, 84])
    FOLLOW_activityListDef_in_blockDef829 = frozenset([73])
    FOLLOW_73_in_blockDef831 = frozenset([1])
    FOLLOW_ASSERTION_in_assertDef853 = frozenset([1])
    FOLLOW_activityDef_in_activityListDef873 = frozenset([1, 39, 40, 41, 44, 45, 46, 48, 51, 56, 72, 74, 78, 79, 80, 81, 84])
    FOLLOW_INT_in_primitivetype889 = frozenset([1])
    FOLLOW_STRING_in_primitivetype911 = frozenset([1])
    FOLLOW_introducesDef_in_activityDef924 = frozenset([68])
    FOLLOW_interactionDef_in_activityDef928 = frozenset([68])
    FOLLOW_inlineDef_in_activityDef932 = frozenset([68])
    FOLLOW_runDef_in_activityDef936 = frozenset([68])
    FOLLOW_recursionDef_in_activityDef940 = frozenset([68])
    FOLLOW_endDef_in_activityDef944 = frozenset([68])
    FOLLOW_doDef_in_activityDef948 = frozenset([68])
    FOLLOW_68_in_activityDef952 = frozenset([1])
    FOLLOW_choiceDef_in_activityDef961 = frozenset([1])
    FOLLOW_directedChoiceDef_in_activityDef965 = frozenset([1])
    FOLLOW_parallelDef_in_activityDef969 = frozenset([1])
    FOLLOW_repeatDef_in_activityDef973 = frozenset([1])
    FOLLOW_unorderedDef_in_activityDef977 = frozenset([1])
    FOLLOW_recBlockDef_in_activityDef984 = frozenset([1])
    FOLLOW_globalEscapeDef_in_activityDef988 = frozenset([1])
    FOLLOW_roleDef_in_introducesDef995 = frozenset([76])
    FOLLOW_76_in_introducesDef997 = frozenset([56])
    FOLLOW_roleDef_in_introducesDef999 = frozenset([1, 71])
    FOLLOW_71_in_introducesDef1003 = frozenset([56])
    FOLLOW_roleDef_in_introducesDef1005 = frozenset([1, 71])
    FOLLOW_ID_in_roleDef1016 = frozenset([1])
    FOLLOW_ID_in_roleName1027 = frozenset([1])
    FOLLOW_ID_in_typeReferenceDef1038 = frozenset([1])
    FOLLOW_typeReferenceDef_in_interactionSignatureDef1051 = frozenset([1])
    FOLLOW_typeReferenceDef_in_interactionSignatureDef1069 = frozenset([74])
    FOLLOW_74_in_interactionSignatureDef1071 = frozenset([56, 75])
    FOLLOW_valueDecl_in_interactionSignatureDef1074 = frozenset([71, 75])
    FOLLOW_71_in_interactionSignatureDef1077 = frozenset([56])
    FOLLOW_valueDecl_in_interactionSignatureDef1079 = frozenset([71, 75])
    FOLLOW_75_in_interactionSignatureDef1086 = frozenset([1])
    FOLLOW_74_in_interactionSignatureDef1108 = frozenset([56])
    FOLLOW_valueDecl_in_interactionSignatureDef1110 = frozenset([71, 75])
    FOLLOW_71_in_interactionSignatureDef1113 = frozenset([56])
    FOLLOW_valueDecl_in_interactionSignatureDef1115 = frozenset([71, 75])
    FOLLOW_75_in_interactionSignatureDef1119 = frozenset([1])
    FOLLOW_ID_in_valueDecl1139 = frozenset([1, 77])
    FOLLOW_77_in_valueDecl1142 = frozenset([5, 6])
    FOLLOW_primitivetype_in_valueDecl1145 = frozenset([1])
    FOLLOW_valueDecl_in_firstValueDecl1156 = frozenset([1])
    FOLLOW_interactionSignatureDef_in_interactionDef1171 = frozenset([39, 40])
    FOLLOW_FROMKW_in_interactionDef1177 = frozenset([56])
    FOLLOW_roleName_in_interactionDef1182 = frozenset([58])
    FOLLOW_assertDef_in_interactionDef1186 = frozenset([1])
    FOLLOW_TOKW_in_interactionDef1210 = frozenset([56])
    FOLLOW_roleName_in_interactionDef1212 = frozenset([58])
    FOLLOW_assertDef_in_interactionDef1216 = frozenset([1])
    FOLLOW_CHOICEKW_in_choiceDef1237 = frozenset([42])
    FOLLOW_ATKW_in_choiceDef1239 = frozenset([56])
    FOLLOW_roleName_in_choiceDef1241 = frozenset([72])
    FOLLOW_blockDef_in_choiceDef1243 = frozenset([1, 43])
    FOLLOW_ORKW_in_choiceDef1247 = frozenset([72])
    FOLLOW_blockDef_in_choiceDef1249 = frozenset([1, 43])
    FOLLOW_FROMKW_in_directedChoiceDef1270 = frozenset([56])
    FOLLOW_roleName_in_directedChoiceDef1272 = frozenset([40, 72])
    FOLLOW_TOKW_in_directedChoiceDef1279 = frozenset([56])
    FOLLOW_roleName_in_directedChoiceDef1281 = frozenset([71, 72])
    FOLLOW_71_in_directedChoiceDef1285 = frozenset([56])
    FOLLOW_roleName_in_directedChoiceDef1288 = frozenset([71, 72])
    FOLLOW_72_in_directedChoiceDef1296 = frozenset([56, 74])
    FOLLOW_onMessageDef_in_directedChoiceDef1300 = frozenset([56, 73, 74])
    FOLLOW_73_in_directedChoiceDef1305 = frozenset([1])
    FOLLOW_interactionSignatureDef_in_onMessageDef1312 = frozenset([77])
    FOLLOW_77_in_onMessageDef1314 = frozenset([39, 40, 41, 44, 45, 46, 48, 51, 56, 72, 74, 78, 79, 80, 81, 84])
    FOLLOW_activityList_in_onMessageDef1316 = frozenset([1])
    FOLLOW_activityDef_in_activityList1327 = frozenset([1, 39, 40, 41, 44, 45, 46, 48, 51, 56, 72, 74, 78, 79, 80, 81, 84])
    FOLLOW_78_in_repeatDef1337 = frozenset([42, 72])
    FOLLOW_ATKW_in_repeatDef1341 = frozenset([56])
    FOLLOW_roleName_in_repeatDef1343 = frozenset([71, 72])
    FOLLOW_71_in_repeatDef1347 = frozenset([56])
    FOLLOW_roleName_in_repeatDef1349 = frozenset([71, 72])
    FOLLOW_blockDef_in_repeatDef1357 = frozenset([1])
    FOLLOW_RECKW_in_recBlockDef1373 = frozenset([56])
    FOLLOW_labelName_in_recBlockDef1375 = frozenset([72])
    FOLLOW_blockDef_in_recBlockDef1377 = frozenset([1])
    FOLLOW_ID_in_labelName1394 = frozenset([1])
    FOLLOW_CONTINUEKW_in_recursionDef1406 = frozenset([56])
    FOLLOW_labelName_in_recursionDef1408 = frozenset([1])
    FOLLOW_79_in_endDef1424 = frozenset([1])
    FOLLOW_80_in_runDef1434 = frozenset([56])
    FOLLOW_protocolRefDef_in_runDef1437 = frozenset([39, 74])
    FOLLOW_74_in_runDef1441 = frozenset([56])
    FOLLOW_parameter_in_runDef1444 = frozenset([71, 75])
    FOLLOW_71_in_runDef1448 = frozenset([56])
    FOLLOW_parameter_in_runDef1451 = frozenset([71, 75])
    FOLLOW_75_in_runDef1456 = frozenset([39])
    FOLLOW_FROMKW_in_runDef1462 = frozenset([56])
    FOLLOW_roleName_in_runDef1464 = frozenset([1])
    FOLLOW_ID_in_protocolRefDef1472 = frozenset([1, 42])
    FOLLOW_ATKW_in_protocolRefDef1476 = frozenset([56])
    FOLLOW_roleName_in_protocolRefDef1478 = frozenset([1])
    FOLLOW_ID_in_declarationName1489 = frozenset([1])
    FOLLOW_declarationName_in_parameter1497 = frozenset([1])
    FOLLOW_81_in_inlineDef1506 = frozenset([56])
    FOLLOW_protocolRefDef_in_inlineDef1509 = frozenset([1, 74])
    FOLLOW_74_in_inlineDef1513 = frozenset([56])
    FOLLOW_parameter_in_inlineDef1516 = frozenset([71, 75])
    FOLLOW_71_in_inlineDef1520 = frozenset([56])
    FOLLOW_parameter_in_inlineDef1523 = frozenset([71, 75])
    FOLLOW_75_in_inlineDef1528 = frozenset([1])
    FOLLOW_PARALLELKW_in_parallelDef1540 = frozenset([72])
    FOLLOW_blockDef_in_parallelDef1542 = frozenset([1, 47])
    FOLLOW_ANDKW_in_parallelDef1546 = frozenset([72])
    FOLLOW_blockDef_in_parallelDef1548 = frozenset([1, 47])
    FOLLOW_INTERRUPTIBLEKW_in_globalEscapeDef1567 = frozenset([72])
    FOLLOW_blockDef_in_globalEscapeDef1569 = frozenset([49])
    FOLLOW_interruptDef_in_globalEscapeDef1571 = frozenset([1])
    FOLLOW_WITHKW_in_interruptDef1590 = frozenset([82, 83])
    FOLLOW_82_in_interruptDef1601 = frozenset([56, 74])
    FOLLOW_interactionSignatureDef_in_interruptDef1603 = frozenset([50, 71])
    FOLLOW_71_in_interruptDef1606 = frozenset([56, 74])
    FOLLOW_interactionSignatureDef_in_interruptDef1608 = frozenset([50, 71])
    FOLLOW_BYKW_in_interruptDef1612 = frozenset([56])
    FOLLOW_roleName_in_interruptDef1614 = frozenset([68, 71])
    FOLLOW_71_in_interruptDef1617 = frozenset([56])
    FOLLOW_roleName_in_interruptDef1619 = frozenset([68, 71])
    FOLLOW_68_in_interruptDef1624 = frozenset([1])
    FOLLOW_83_in_interruptDef1663 = frozenset([56, 74])
    FOLLOW_interactionSignatureDef_in_interruptDef1665 = frozenset([50, 71])
    FOLLOW_71_in_interruptDef1668 = frozenset([56, 74])
    FOLLOW_interactionSignatureDef_in_interruptDef1670 = frozenset([50, 71])
    FOLLOW_BYKW_in_interruptDef1674 = frozenset([56])
    FOLLOW_roleName_in_interruptDef1676 = frozenset([68, 71])
    FOLLOW_71_in_interruptDef1679 = frozenset([56])
    FOLLOW_roleName_in_interruptDef1681 = frozenset([68, 71])
    FOLLOW_68_in_interruptDef1686 = frozenset([1])
    FOLLOW_84_in_unorderedDef1709 = frozenset([72])
    FOLLOW_72_in_unorderedDef1711 = frozenset([39, 40, 41, 44, 45, 46, 48, 51, 56, 72, 73, 74, 78, 79, 80, 81, 84])
    FOLLOW_activityDef_in_unorderedDef1715 = frozenset([39, 40, 41, 44, 45, 46, 48, 51, 56, 72, 73, 74, 78, 79, 80, 81, 84])
    FOLLOW_73_in_unorderedDef1720 = frozenset([1])
    FOLLOW_roleName_in_aliasDef1740 = frozenset([52])
    FOLLOW_ASKW_in_aliasDef1742 = frozenset([56])
    FOLLOW_ID_in_aliasDef1744 = frozenset([1])
    FOLLOW_DOKW_in_doDef1765 = frozenset([57])
    FOLLOW_EXTID_in_doDef1767 = frozenset([69, 74])
    FOLLOW_69_in_doDef1770 = frozenset([56, 74])
    FOLLOW_interactionSignatureDef_in_doDef1772 = frozenset([70, 71])
    FOLLOW_71_in_doDef1775 = frozenset([56, 74])
    FOLLOW_interactionSignatureDef_in_doDef1777 = frozenset([70, 71])
    FOLLOW_70_in_doDef1781 = frozenset([74])
    FOLLOW_74_in_doDef1785 = frozenset([56])
    FOLLOW_aliasDef_in_doDef1787 = frozenset([71, 75])
    FOLLOW_71_in_doDef1790 = frozenset([56])
    FOLLOW_aliasDef_in_doDef1792 = frozenset([71, 75])
    FOLLOW_75_in_doDef1796 = frozenset([1])
    FOLLOW_term_in_expr1835 = frozenset([1, 7, 8])
    FOLLOW_set_in_expr1839 = frozenset([59])
    FOLLOW_term_in_expr1850 = frozenset([1, 7, 8])
    FOLLOW_factor_in_term1862 = frozenset([1, 9, 10])
    FOLLOW_set_in_term1866 = frozenset([59])
    FOLLOW_factor_in_term1876 = frozenset([1, 9, 10])
    FOLLOW_NUMBER_in_factor1888 = frozenset([1])
    FOLLOW_importdecl_in_synpred1_Monitor509 = frozenset([1])
    FOLLOW_protocolDef_in_synpred3_Monitor519 = frozenset([1])
    FOLLOW_packagedecl_in_synpred8_Monitor647 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("MonitorLexer", MonitorParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
