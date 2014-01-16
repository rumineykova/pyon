# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 Generate/Monitor.g 2014-01-16 18:57:08

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
RESV=12
ANNOTATION=25
ASSERTION=28
PARALLEL=19
ID=26
T__61=61
EOF=-1
T__60=60
PROTOCOL=20
TYPE=14
T__55=55
ML_COMMENT=32
T__56=56
INTERACTION=4
T__57=57
ROLES=24
T__58=58
T__51=51
T__52=52
T__53=53
T__54=54
T__59=59
FULLSTOP=11
PLUS=7
SEND=13
DIGIT=30
T__50=50
T__42=42
T__43=43
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
T__45=45
LINE_COMMENT=33
T__48=48
T__49=49
RECLABEL=18
NUMBER=29
WHITESPACE=31
INT=5
MINUS=8
MULT=9
VALUE=15
ASSERT=21
UNORDERED=17
EMPTY=23
StringLiteral=27
GLOBAL_ESCAPE=22
T__34=34
T__35=35
T__36=36
T__37=37
T__38=38
T__39=39
BRANCH=16
DIV=10
STRING=6

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "INTERACTION", "INT", "STRING", "PLUS", "MINUS", "MULT", "DIV", "FULLSTOP", 
    "RESV", "SEND", "TYPE", "VALUE", "BRANCH", "UNORDERED", "RECLABEL", 
    "PARALLEL", "PROTOCOL", "ASSERT", "GLOBAL_ESCAPE", "EMPTY", "ROLES", 
    "ANNOTATION", "ID", "StringLiteral", "ASSERTION", "NUMBER", "DIGIT", 
    "WHITESPACE", "ML_COMMENT", "LINE_COMMENT", "'import'", "'protocol'", 
    "','", "';'", "'from'", "'as'", "'at'", "'{'", "'}'", "'('", "')'", 
    "'role'", "'introduces'", "':'", "'to'", "'choice'", "'or'", "'repeat'", 
    "'rec'", "'end'", "'run'", "'inline'", "'parallel'", "'and'", "'do'", 
    "'interrupt'", "'by'", "'unordered'"
]




class MonitorParser(Parser):
    grammarFileName = "Generate/Monitor.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(MonitorParser, self).__init__(input, state, *args, **kwargs)

        self.dfa3 = self.DFA3(
            self, 3,
            eot = self.DFA3_eot,
            eof = self.DFA3_eof,
            min = self.DFA3_min,
            max = self.DFA3_max,
            accept = self.DFA3_accept,
            special = self.DFA3_special,
            transition = self.DFA3_transition
            )

        self.dfa17 = self.DFA17(
            self, 17,
            eot = self.DFA17_eot,
            eof = self.DFA17_eof,
            min = self.DFA17_min,
            max = self.DFA17_max,
            accept = self.DFA17_accept,
            special = self.DFA17_special,
            transition = self.DFA17_transition
            )

        self.dfa20 = self.DFA20(
            self, 20,
            eot = self.DFA20_eot,
            eof = self.DFA20_eof,
            min = self.DFA20_min,
            max = self.DFA20_max,
            accept = self.DFA20_accept,
            special = self.DFA20_special,
            transition = self.DFA20_transition
            )

        self.dfa37 = self.DFA37(
            self, 37,
            eot = self.DFA37_eot,
            eof = self.DFA37_eof,
            min = self.DFA37_min,
            max = self.DFA37_max,
            accept = self.DFA37_accept,
            special = self.DFA37_special,
            transition = self.DFA37_transition
            )






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class description_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.description_return, self).__init__()

            self.tree = None




    # $ANTLR start "description"
    # Generate/Monitor.g:40:1: description : ( ( ANNOTATION )* ( importProtocolStatement | importTypeStatement ) )* ( ANNOTATION )* protocolDef -> protocolDef ;
    def description(self, ):

        retval = self.description_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ANNOTATION1 = None
        ANNOTATION4 = None
        importProtocolStatement2 = None

        importTypeStatement3 = None

        protocolDef5 = None


        ANNOTATION1_tree = None
        ANNOTATION4_tree = None
        stream_ANNOTATION = RewriteRuleTokenStream(self._adaptor, "token ANNOTATION")
        stream_importTypeStatement = RewriteRuleSubtreeStream(self._adaptor, "rule importTypeStatement")
        stream_protocolDef = RewriteRuleSubtreeStream(self._adaptor, "rule protocolDef")
        stream_importProtocolStatement = RewriteRuleSubtreeStream(self._adaptor, "rule importProtocolStatement")
        try:
            try:
                # Generate/Monitor.g:40:12: ( ( ( ANNOTATION )* ( importProtocolStatement | importTypeStatement ) )* ( ANNOTATION )* protocolDef -> protocolDef )
                # Generate/Monitor.g:40:14: ( ( ANNOTATION )* ( importProtocolStatement | importTypeStatement ) )* ( ANNOTATION )* protocolDef
                pass 
                # Generate/Monitor.g:40:14: ( ( ANNOTATION )* ( importProtocolStatement | importTypeStatement ) )*
                while True: #loop3
                    alt3 = 2
                    alt3 = self.dfa3.predict(self.input)
                    if alt3 == 1:
                        # Generate/Monitor.g:40:16: ( ANNOTATION )* ( importProtocolStatement | importTypeStatement )
                        pass 
                        # Generate/Monitor.g:40:16: ( ANNOTATION )*
                        while True: #loop1
                            alt1 = 2
                            LA1_0 = self.input.LA(1)

                            if (LA1_0 == ANNOTATION) :
                                alt1 = 1


                            if alt1 == 1:
                                # Generate/Monitor.g:40:18: ANNOTATION
                                pass 
                                ANNOTATION1=self.match(self.input, ANNOTATION, self.FOLLOW_ANNOTATION_in_description257) 
                                stream_ANNOTATION.add(ANNOTATION1)


                            else:
                                break #loop1
                        # Generate/Monitor.g:40:32: ( importProtocolStatement | importTypeStatement )
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == 34) :
                            LA2_1 = self.input.LA(2)

                            if (LA2_1 == 35) :
                                alt2 = 1
                            elif ((ID <= LA2_1 <= StringLiteral)) :
                                alt2 = 2
                            else:
                                nvae = NoViableAltException("", 2, 1, self.input)

                                raise nvae

                        else:
                            nvae = NoViableAltException("", 2, 0, self.input)

                            raise nvae

                        if alt2 == 1:
                            # Generate/Monitor.g:40:34: importProtocolStatement
                            pass 
                            self._state.following.append(self.FOLLOW_importProtocolStatement_in_description264)
                            importProtocolStatement2 = self.importProtocolStatement()

                            self._state.following.pop()
                            stream_importProtocolStatement.add(importProtocolStatement2.tree)


                        elif alt2 == 2:
                            # Generate/Monitor.g:40:60: importTypeStatement
                            pass 
                            self._state.following.append(self.FOLLOW_importTypeStatement_in_description268)
                            importTypeStatement3 = self.importTypeStatement()

                            self._state.following.pop()
                            stream_importTypeStatement.add(importTypeStatement3.tree)





                    else:
                        break #loop3
                # Generate/Monitor.g:40:85: ( ANNOTATION )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ANNOTATION) :
                        alt4 = 1


                    if alt4 == 1:
                        # Generate/Monitor.g:40:87: ANNOTATION
                        pass 
                        ANNOTATION4=self.match(self.input, ANNOTATION, self.FOLLOW_ANNOTATION_in_description277) 
                        stream_ANNOTATION.add(ANNOTATION4)


                    else:
                        break #loop4
                self._state.following.append(self.FOLLOW_protocolDef_in_description282)
                protocolDef5 = self.protocolDef()

                self._state.following.pop()
                stream_protocolDef.add(protocolDef5.tree)

                # AST Rewrite
                # elements: protocolDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 40:113: -> protocolDef
                self._adaptor.addChild(root_0, stream_protocolDef.nextTree())



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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

    class importProtocolStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.importProtocolStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "importProtocolStatement"
    # Generate/Monitor.g:42:1: importProtocolStatement : 'import' 'protocol' importProtocolDef ( ',' importProtocolDef )* ';' ;
    def importProtocolStatement(self, ):

        retval = self.importProtocolStatement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal6 = None
        string_literal7 = None
        char_literal9 = None
        char_literal11 = None
        importProtocolDef8 = None

        importProtocolDef10 = None


        string_literal6_tree = None
        string_literal7_tree = None
        char_literal9_tree = None
        char_literal11_tree = None

        try:
            try:
                # Generate/Monitor.g:42:24: ( 'import' 'protocol' importProtocolDef ( ',' importProtocolDef )* ';' )
                # Generate/Monitor.g:42:26: 'import' 'protocol' importProtocolDef ( ',' importProtocolDef )* ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal6=self.match(self.input, 34, self.FOLLOW_34_in_importProtocolStatement293)

                string_literal6_tree = self._adaptor.createWithPayload(string_literal6)
                self._adaptor.addChild(root_0, string_literal6_tree)

                string_literal7=self.match(self.input, 35, self.FOLLOW_35_in_importProtocolStatement295)

                string_literal7_tree = self._adaptor.createWithPayload(string_literal7)
                self._adaptor.addChild(root_0, string_literal7_tree)

                self._state.following.append(self.FOLLOW_importProtocolDef_in_importProtocolStatement297)
                importProtocolDef8 = self.importProtocolDef()

                self._state.following.pop()
                self._adaptor.addChild(root_0, importProtocolDef8.tree)
                # Generate/Monitor.g:42:64: ( ',' importProtocolDef )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 36) :
                        alt5 = 1


                    if alt5 == 1:
                        # Generate/Monitor.g:42:66: ',' importProtocolDef
                        pass 
                        char_literal9=self.match(self.input, 36, self.FOLLOW_36_in_importProtocolStatement301)
                        self._state.following.append(self.FOLLOW_importProtocolDef_in_importProtocolStatement304)
                        importProtocolDef10 = self.importProtocolDef()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, importProtocolDef10.tree)


                    else:
                        break #loop5
                char_literal11=self.match(self.input, 37, self.FOLLOW_37_in_importProtocolStatement309)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "importProtocolStatement"

    class importProtocolDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.importProtocolDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "importProtocolDef"
    # Generate/Monitor.g:44:1: importProtocolDef : ID 'from' StringLiteral ;
    def importProtocolDef(self, ):

        retval = self.importProtocolDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID12 = None
        string_literal13 = None
        StringLiteral14 = None

        ID12_tree = None
        string_literal13_tree = None
        StringLiteral14_tree = None

        try:
            try:
                # Generate/Monitor.g:44:18: ( ID 'from' StringLiteral )
                # Generate/Monitor.g:44:20: ID 'from' StringLiteral
                pass 
                root_0 = self._adaptor.nil()

                ID12=self.match(self.input, ID, self.FOLLOW_ID_in_importProtocolDef318)

                ID12_tree = self._adaptor.createWithPayload(ID12)
                self._adaptor.addChild(root_0, ID12_tree)

                string_literal13=self.match(self.input, 38, self.FOLLOW_38_in_importProtocolDef320)
                StringLiteral14=self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_importProtocolDef323)

                StringLiteral14_tree = self._adaptor.createWithPayload(StringLiteral14)
                self._adaptor.addChild(root_0, StringLiteral14_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "importProtocolDef"

    class importTypeStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.importTypeStatement_return, self).__init__()

            self.tree = None




    # $ANTLR start "importTypeStatement"
    # Generate/Monitor.g:46:1: importTypeStatement : 'import' ( simpleName )? importTypeDef ( ',' importTypeDef )* ( 'from' StringLiteral )? ';' ;
    def importTypeStatement(self, ):

        retval = self.importTypeStatement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal15 = None
        char_literal18 = None
        string_literal20 = None
        StringLiteral21 = None
        char_literal22 = None
        simpleName16 = None

        importTypeDef17 = None

        importTypeDef19 = None


        string_literal15_tree = None
        char_literal18_tree = None
        string_literal20_tree = None
        StringLiteral21_tree = None
        char_literal22_tree = None

        try:
            try:
                # Generate/Monitor.g:46:20: ( 'import' ( simpleName )? importTypeDef ( ',' importTypeDef )* ( 'from' StringLiteral )? ';' )
                # Generate/Monitor.g:46:22: 'import' ( simpleName )? importTypeDef ( ',' importTypeDef )* ( 'from' StringLiteral )? ';'
                pass 
                root_0 = self._adaptor.nil()

                string_literal15=self.match(self.input, 34, self.FOLLOW_34_in_importTypeStatement336)

                string_literal15_tree = self._adaptor.createWithPayload(string_literal15)
                self._adaptor.addChild(root_0, string_literal15_tree)

                # Generate/Monitor.g:46:31: ( simpleName )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == ID) :
                    LA6_1 = self.input.LA(2)

                    if ((ID <= LA6_1 <= StringLiteral)) :
                        alt6 = 1
                if alt6 == 1:
                    # Generate/Monitor.g:46:33: simpleName
                    pass 
                    self._state.following.append(self.FOLLOW_simpleName_in_importTypeStatement340)
                    simpleName16 = self.simpleName()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, simpleName16.tree)



                self._state.following.append(self.FOLLOW_importTypeDef_in_importTypeStatement345)
                importTypeDef17 = self.importTypeDef()

                self._state.following.pop()
                self._adaptor.addChild(root_0, importTypeDef17.tree)
                # Generate/Monitor.g:46:61: ( ',' importTypeDef )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 36) :
                        alt7 = 1


                    if alt7 == 1:
                        # Generate/Monitor.g:46:63: ',' importTypeDef
                        pass 
                        char_literal18=self.match(self.input, 36, self.FOLLOW_36_in_importTypeStatement349)
                        self._state.following.append(self.FOLLOW_importTypeDef_in_importTypeStatement352)
                        importTypeDef19 = self.importTypeDef()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, importTypeDef19.tree)


                    else:
                        break #loop7
                # Generate/Monitor.g:46:85: ( 'from' StringLiteral )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 38) :
                    alt8 = 1
                if alt8 == 1:
                    # Generate/Monitor.g:46:87: 'from' StringLiteral
                    pass 
                    string_literal20=self.match(self.input, 38, self.FOLLOW_38_in_importTypeStatement359)
                    StringLiteral21=self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_importTypeStatement362)

                    StringLiteral21_tree = self._adaptor.createWithPayload(StringLiteral21)
                    self._adaptor.addChild(root_0, StringLiteral21_tree)




                char_literal22=self.match(self.input, 37, self.FOLLOW_37_in_importTypeStatement367)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "importTypeStatement"

    class importTypeDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.importTypeDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "importTypeDef"
    # Generate/Monitor.g:48:1: importTypeDef : ( dataTypeDef 'as' )? ID ;
    def importTypeDef(self, ):

        retval = self.importTypeDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal24 = None
        ID25 = None
        dataTypeDef23 = None


        string_literal24_tree = None
        ID25_tree = None

        try:
            try:
                # Generate/Monitor.g:48:14: ( ( dataTypeDef 'as' )? ID )
                # Generate/Monitor.g:48:16: ( dataTypeDef 'as' )? ID
                pass 
                root_0 = self._adaptor.nil()

                # Generate/Monitor.g:48:16: ( dataTypeDef 'as' )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == StringLiteral) :
                    alt9 = 1
                if alt9 == 1:
                    # Generate/Monitor.g:48:18: dataTypeDef 'as'
                    pass 
                    self._state.following.append(self.FOLLOW_dataTypeDef_in_importTypeDef378)
                    dataTypeDef23 = self.dataTypeDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, dataTypeDef23.tree)
                    string_literal24=self.match(self.input, 39, self.FOLLOW_39_in_importTypeDef380)



                ID25=self.match(self.input, ID, self.FOLLOW_ID_in_importTypeDef386)

                ID25_tree = self._adaptor.createWithPayload(ID25)
                self._adaptor.addChild(root_0, ID25_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "importTypeDef"

    class dataTypeDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.dataTypeDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "dataTypeDef"
    # Generate/Monitor.g:50:1: dataTypeDef : StringLiteral ;
    def dataTypeDef(self, ):

        retval = self.dataTypeDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        StringLiteral26 = None

        StringLiteral26_tree = None

        try:
            try:
                # Generate/Monitor.g:50:12: ( StringLiteral )
                # Generate/Monitor.g:50:14: StringLiteral
                pass 
                root_0 = self._adaptor.nil()

                StringLiteral26=self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_dataTypeDef394)

                StringLiteral26_tree = self._adaptor.createWithPayload(StringLiteral26)
                self._adaptor.addChild(root_0, StringLiteral26_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "dataTypeDef"

    class simpleName_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.simpleName_return, self).__init__()

            self.tree = None




    # $ANTLR start "simpleName"
    # Generate/Monitor.g:52:1: simpleName : ID ;
    def simpleName(self, ):

        retval = self.simpleName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID27 = None

        ID27_tree = None

        try:
            try:
                # Generate/Monitor.g:52:11: ( ID )
                # Generate/Monitor.g:52:13: ID
                pass 
                root_0 = self._adaptor.nil()

                ID27=self.match(self.input, ID, self.FOLLOW_ID_in_simpleName402)

                ID27_tree = self._adaptor.createWithPayload(ID27)
                self._adaptor.addChild(root_0, ID27_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "simpleName"

    class protocolDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.protocolDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "protocolDef"
    # Generate/Monitor.g:54:1: protocolDef : 'protocol' protocolName ( 'at' roleName )? ( parameterDefs )? '{' protocolBlockDef ( ( ANNOTATION )* protocolDef )* '}' -> ^( PROTOCOL roleName ( parameterDefs )* ( protocolBlockDef )+ ) ;
    def protocolDef(self, ):

        retval = self.protocolDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal28 = None
        string_literal30 = None
        char_literal33 = None
        ANNOTATION35 = None
        char_literal37 = None
        protocolName29 = None

        roleName31 = None

        parameterDefs32 = None

        protocolBlockDef34 = None

        protocolDef36 = None


        string_literal28_tree = None
        string_literal30_tree = None
        char_literal33_tree = None
        ANNOTATION35_tree = None
        char_literal37_tree = None
        stream_42 = RewriteRuleTokenStream(self._adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_40 = RewriteRuleTokenStream(self._adaptor, "token 40")
        stream_35 = RewriteRuleTokenStream(self._adaptor, "token 35")
        stream_ANNOTATION = RewriteRuleTokenStream(self._adaptor, "token ANNOTATION")
        stream_parameterDefs = RewriteRuleSubtreeStream(self._adaptor, "rule parameterDefs")
        stream_protocolDef = RewriteRuleSubtreeStream(self._adaptor, "rule protocolDef")
        stream_protocolName = RewriteRuleSubtreeStream(self._adaptor, "rule protocolName")
        stream_protocolBlockDef = RewriteRuleSubtreeStream(self._adaptor, "rule protocolBlockDef")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        try:
            try:
                # Generate/Monitor.g:54:12: ( 'protocol' protocolName ( 'at' roleName )? ( parameterDefs )? '{' protocolBlockDef ( ( ANNOTATION )* protocolDef )* '}' -> ^( PROTOCOL roleName ( parameterDefs )* ( protocolBlockDef )+ ) )
                # Generate/Monitor.g:54:14: 'protocol' protocolName ( 'at' roleName )? ( parameterDefs )? '{' protocolBlockDef ( ( ANNOTATION )* protocolDef )* '}'
                pass 
                string_literal28=self.match(self.input, 35, self.FOLLOW_35_in_protocolDef410) 
                stream_35.add(string_literal28)
                self._state.following.append(self.FOLLOW_protocolName_in_protocolDef412)
                protocolName29 = self.protocolName()

                self._state.following.pop()
                stream_protocolName.add(protocolName29.tree)
                # Generate/Monitor.g:54:38: ( 'at' roleName )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 40) :
                    alt10 = 1
                if alt10 == 1:
                    # Generate/Monitor.g:54:40: 'at' roleName
                    pass 
                    string_literal30=self.match(self.input, 40, self.FOLLOW_40_in_protocolDef416) 
                    stream_40.add(string_literal30)
                    self._state.following.append(self.FOLLOW_roleName_in_protocolDef418)
                    roleName31 = self.roleName()

                    self._state.following.pop()
                    stream_roleName.add(roleName31.tree)



                # Generate/Monitor.g:54:57: ( parameterDefs )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 43) :
                    alt11 = 1
                if alt11 == 1:
                    # Generate/Monitor.g:54:59: parameterDefs
                    pass 
                    self._state.following.append(self.FOLLOW_parameterDefs_in_protocolDef425)
                    parameterDefs32 = self.parameterDefs()

                    self._state.following.pop()
                    stream_parameterDefs.add(parameterDefs32.tree)



                char_literal33=self.match(self.input, 41, self.FOLLOW_41_in_protocolDef430) 
                stream_41.add(char_literal33)
                self._state.following.append(self.FOLLOW_protocolBlockDef_in_protocolDef432)
                protocolBlockDef34 = self.protocolBlockDef()

                self._state.following.pop()
                stream_protocolBlockDef.add(protocolBlockDef34.tree)
                # Generate/Monitor.g:54:97: ( ( ANNOTATION )* protocolDef )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == ANNOTATION or LA13_0 == 35) :
                        alt13 = 1


                    if alt13 == 1:
                        # Generate/Monitor.g:54:99: ( ANNOTATION )* protocolDef
                        pass 
                        # Generate/Monitor.g:54:99: ( ANNOTATION )*
                        while True: #loop12
                            alt12 = 2
                            LA12_0 = self.input.LA(1)

                            if (LA12_0 == ANNOTATION) :
                                alt12 = 1


                            if alt12 == 1:
                                # Generate/Monitor.g:54:101: ANNOTATION
                                pass 
                                ANNOTATION35=self.match(self.input, ANNOTATION, self.FOLLOW_ANNOTATION_in_protocolDef438) 
                                stream_ANNOTATION.add(ANNOTATION35)


                            else:
                                break #loop12
                        self._state.following.append(self.FOLLOW_protocolDef_in_protocolDef443)
                        protocolDef36 = self.protocolDef()

                        self._state.following.pop()
                        stream_protocolDef.add(protocolDef36.tree)


                    else:
                        break #loop13
                char_literal37=self.match(self.input, 42, self.FOLLOW_42_in_protocolDef448) 
                stream_42.add(char_literal37)

                # AST Rewrite
                # elements: roleName, parameterDefs, protocolBlockDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 55:7: -> ^( PROTOCOL roleName ( parameterDefs )* ( protocolBlockDef )+ )
                # Generate/Monitor.g:55:10: ^( PROTOCOL roleName ( parameterDefs )* ( protocolBlockDef )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROTOCOL, "PROTOCOL"), root_1)

                self._adaptor.addChild(root_1, stream_roleName.nextTree())
                # Generate/Monitor.g:55:31: ( parameterDefs )*
                while stream_parameterDefs.hasNext():
                    self._adaptor.addChild(root_1, stream_parameterDefs.nextTree())


                stream_parameterDefs.reset();
                # Generate/Monitor.g:55:46: ( protocolBlockDef )+
                if not (stream_protocolBlockDef.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_protocolBlockDef.hasNext():
                    self._adaptor.addChild(root_1, stream_protocolBlockDef.nextTree())


                stream_protocolBlockDef.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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

    class protocolName_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.protocolName_return, self).__init__()

            self.tree = None




    # $ANTLR start "protocolName"
    # Generate/Monitor.g:57:1: protocolName : ID ;
    def protocolName(self, ):

        retval = self.protocolName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID38 = None

        ID38_tree = None

        try:
            try:
                # Generate/Monitor.g:57:13: ( ID )
                # Generate/Monitor.g:57:15: ID
                pass 
                root_0 = self._adaptor.nil()

                ID38=self.match(self.input, ID, self.FOLLOW_ID_in_protocolName476)

                ID38_tree = self._adaptor.createWithPayload(ID38)
                self._adaptor.addChild(root_0, ID38_tree)




                retval.stop = self.input.LT(-1)


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

    class parameterDefs_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.parameterDefs_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameterDefs"
    # Generate/Monitor.g:59:1: parameterDefs : '(' roleparameDef ( ',' roleparameDef )* ')' -> ^( ROLES ( roleparameDef )+ ) ;
    def parameterDefs(self, ):

        retval = self.parameterDefs_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal39 = None
        char_literal41 = None
        char_literal43 = None
        roleparameDef40 = None

        roleparameDef42 = None


        char_literal39_tree = None
        char_literal41_tree = None
        char_literal43_tree = None
        stream_43 = RewriteRuleTokenStream(self._adaptor, "token 43")
        stream_44 = RewriteRuleTokenStream(self._adaptor, "token 44")
        stream_36 = RewriteRuleTokenStream(self._adaptor, "token 36")
        stream_roleparameDef = RewriteRuleSubtreeStream(self._adaptor, "rule roleparameDef")
        try:
            try:
                # Generate/Monitor.g:59:14: ( '(' roleparameDef ( ',' roleparameDef )* ')' -> ^( ROLES ( roleparameDef )+ ) )
                # Generate/Monitor.g:59:16: '(' roleparameDef ( ',' roleparameDef )* ')'
                pass 
                char_literal39=self.match(self.input, 43, self.FOLLOW_43_in_parameterDefs484) 
                stream_43.add(char_literal39)
                self._state.following.append(self.FOLLOW_roleparameDef_in_parameterDefs486)
                roleparameDef40 = self.roleparameDef()

                self._state.following.pop()
                stream_roleparameDef.add(roleparameDef40.tree)
                # Generate/Monitor.g:59:34: ( ',' roleparameDef )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == 36) :
                        alt14 = 1


                    if alt14 == 1:
                        # Generate/Monitor.g:59:36: ',' roleparameDef
                        pass 
                        char_literal41=self.match(self.input, 36, self.FOLLOW_36_in_parameterDefs490) 
                        stream_36.add(char_literal41)
                        self._state.following.append(self.FOLLOW_roleparameDef_in_parameterDefs492)
                        roleparameDef42 = self.roleparameDef()

                        self._state.following.pop()
                        stream_roleparameDef.add(roleparameDef42.tree)


                    else:
                        break #loop14
                char_literal43=self.match(self.input, 44, self.FOLLOW_44_in_parameterDefs497) 
                stream_44.add(char_literal43)

                # AST Rewrite
                # elements: roleparameDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 59:61: -> ^( ROLES ( roleparameDef )+ )
                # Generate/Monitor.g:59:64: ^( ROLES ( roleparameDef )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROLES, "ROLES"), root_1)

                # Generate/Monitor.g:59:72: ( roleparameDef )+
                if not (stream_roleparameDef.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_roleparameDef.hasNext():
                    self._adaptor.addChild(root_1, stream_roleparameDef.nextTree())


                stream_roleparameDef.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parameterDefs"

    class roleparameDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.roleparameDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "roleparameDef"
    # Generate/Monitor.g:61:1: roleparameDef : 'role' simpleName -> simpleName ;
    def roleparameDef(self, ):

        retval = self.roleparameDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal44 = None
        simpleName45 = None


        string_literal44_tree = None
        stream_45 = RewriteRuleTokenStream(self._adaptor, "token 45")
        stream_simpleName = RewriteRuleSubtreeStream(self._adaptor, "rule simpleName")
        try:
            try:
                # Generate/Monitor.g:61:14: ( 'role' simpleName -> simpleName )
                # Generate/Monitor.g:61:16: 'role' simpleName
                pass 
                string_literal44=self.match(self.input, 45, self.FOLLOW_45_in_roleparameDef513) 
                stream_45.add(string_literal44)
                self._state.following.append(self.FOLLOW_simpleName_in_roleparameDef515)
                simpleName45 = self.simpleName()

                self._state.following.pop()
                stream_simpleName.add(simpleName45.tree)

                # AST Rewrite
                # elements: simpleName
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 61:34: -> simpleName
                self._adaptor.addChild(root_0, stream_simpleName.nextTree())



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:63:1: protocolBlockDef : activityListDef -> activityListDef ;
    def protocolBlockDef(self, ):

        retval = self.protocolBlockDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        activityListDef46 = None


        stream_activityListDef = RewriteRuleSubtreeStream(self._adaptor, "rule activityListDef")
        try:
            try:
                # Generate/Monitor.g:63:17: ( activityListDef -> activityListDef )
                # Generate/Monitor.g:63:19: activityListDef
                pass 
                self._state.following.append(self.FOLLOW_activityListDef_in_protocolBlockDef526)
                activityListDef46 = self.activityListDef()

                self._state.following.pop()
                stream_activityListDef.add(activityListDef46.tree)

                # AST Rewrite
                # elements: activityListDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 63:35: -> activityListDef
                self._adaptor.addChild(root_0, stream_activityListDef.nextTree())



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:65:1: blockDef : '{' activityListDef '}' -> ^( BRANCH activityListDef ) ;
    def blockDef(self, ):

        retval = self.blockDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal47 = None
        char_literal49 = None
        activityListDef48 = None


        char_literal47_tree = None
        char_literal49_tree = None
        stream_42 = RewriteRuleTokenStream(self._adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_activityListDef = RewriteRuleSubtreeStream(self._adaptor, "rule activityListDef")
        try:
            try:
                # Generate/Monitor.g:65:9: ( '{' activityListDef '}' -> ^( BRANCH activityListDef ) )
                # Generate/Monitor.g:65:11: '{' activityListDef '}'
                pass 
                char_literal47=self.match(self.input, 41, self.FOLLOW_41_in_blockDef537) 
                stream_41.add(char_literal47)
                self._state.following.append(self.FOLLOW_activityListDef_in_blockDef539)
                activityListDef48 = self.activityListDef()

                self._state.following.pop()
                stream_activityListDef.add(activityListDef48.tree)
                char_literal49=self.match(self.input, 42, self.FOLLOW_42_in_blockDef541) 
                stream_42.add(char_literal49)

                # AST Rewrite
                # elements: activityListDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 65:35: -> ^( BRANCH activityListDef )
                # Generate/Monitor.g:65:38: ^( BRANCH activityListDef )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BRANCH, "BRANCH"), root_1)

                self._adaptor.addChild(root_1, stream_activityListDef.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:67:1: assertDef : ( ASSERTION )* -> ^( ASSERT ( ASSERTION )* ) ;
    def assertDef(self, ):

        retval = self.assertDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ASSERTION50 = None

        ASSERTION50_tree = None
        stream_ASSERTION = RewriteRuleTokenStream(self._adaptor, "token ASSERTION")

        try:
            try:
                # Generate/Monitor.g:67:11: ( ( ASSERTION )* -> ^( ASSERT ( ASSERTION )* ) )
                # Generate/Monitor.g:67:13: ( ASSERTION )*
                pass 
                # Generate/Monitor.g:67:13: ( ASSERTION )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == ASSERTION) :
                        alt15 = 1


                    if alt15 == 1:
                        # Generate/Monitor.g:67:14: ASSERTION
                        pass 
                        ASSERTION50=self.match(self.input, ASSERTION, self.FOLLOW_ASSERTION_in_assertDef563) 
                        stream_ASSERTION.add(ASSERTION50)


                    else:
                        break #loop15

                # AST Rewrite
                # elements: ASSERTION
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 67:26: -> ^( ASSERT ( ASSERTION )* )
                # Generate/Monitor.g:67:29: ^( ASSERT ( ASSERTION )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ASSERT, "ASSERT"), root_1)

                # Generate/Monitor.g:67:38: ( ASSERTION )*
                while stream_ASSERTION.hasNext():
                    self._adaptor.addChild(root_1, stream_ASSERTION.nextNode())


                stream_ASSERTION.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:69:1: activityListDef : ( ( ANNOTATION )* activityDef )* -> ( activityDef )+ ;
    def activityListDef(self, ):

        retval = self.activityListDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ANNOTATION51 = None
        activityDef52 = None


        ANNOTATION51_tree = None
        stream_ANNOTATION = RewriteRuleTokenStream(self._adaptor, "token ANNOTATION")
        stream_activityDef = RewriteRuleSubtreeStream(self._adaptor, "rule activityDef")
        try:
            try:
                # Generate/Monitor.g:69:16: ( ( ( ANNOTATION )* activityDef )* -> ( activityDef )+ )
                # Generate/Monitor.g:69:18: ( ( ANNOTATION )* activityDef )*
                pass 
                # Generate/Monitor.g:69:18: ( ( ANNOTATION )* activityDef )*
                while True: #loop17
                    alt17 = 2
                    alt17 = self.dfa17.predict(self.input)
                    if alt17 == 1:
                        # Generate/Monitor.g:69:20: ( ANNOTATION )* activityDef
                        pass 
                        # Generate/Monitor.g:69:20: ( ANNOTATION )*
                        while True: #loop16
                            alt16 = 2
                            LA16_0 = self.input.LA(1)

                            if (LA16_0 == ANNOTATION) :
                                alt16 = 1


                            if alt16 == 1:
                                # Generate/Monitor.g:69:22: ANNOTATION
                                pass 
                                ANNOTATION51=self.match(self.input, ANNOTATION, self.FOLLOW_ANNOTATION_in_activityListDef585) 
                                stream_ANNOTATION.add(ANNOTATION51)


                            else:
                                break #loop16
                        self._state.following.append(self.FOLLOW_activityDef_in_activityListDef590)
                        activityDef52 = self.activityDef()

                        self._state.following.pop()
                        stream_activityDef.add(activityDef52.tree)


                    else:
                        break #loop17

                # AST Rewrite
                # elements: activityDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 69:51: -> ( activityDef )+
                # Generate/Monitor.g:69:54: ( activityDef )+
                if not (stream_activityDef.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_activityDef.hasNext():
                    self._adaptor.addChild(root_0, stream_activityDef.nextTree())


                stream_activityDef.reset()



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:71:1: primitivetype : ( INT -> INT | STRING -> STRING ) ;
    def primitivetype(self, ):

        retval = self.primitivetype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INT53 = None
        STRING54 = None

        INT53_tree = None
        STRING54_tree = None
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")

        try:
            try:
                # Generate/Monitor.g:71:15: ( ( INT -> INT | STRING -> STRING ) )
                # Generate/Monitor.g:71:16: ( INT -> INT | STRING -> STRING )
                pass 
                # Generate/Monitor.g:71:16: ( INT -> INT | STRING -> STRING )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == INT) :
                    alt18 = 1
                elif (LA18_0 == STRING) :
                    alt18 = 2
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # Generate/Monitor.g:71:17: INT
                    pass 
                    INT53=self.match(self.input, INT, self.FOLLOW_INT_in_primitivetype606) 
                    stream_INT.add(INT53)

                    # AST Rewrite
                    # elements: INT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 71:21: -> INT
                    self._adaptor.addChild(root_0, stream_INT.nextNode())



                    retval.tree = root_0


                elif alt18 == 2:
                    # Generate/Monitor.g:71:28: STRING
                    pass 
                    STRING54=self.match(self.input, STRING, self.FOLLOW_STRING_in_primitivetype612) 
                    stream_STRING.add(STRING54)

                    # AST Rewrite
                    # elements: STRING
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 71:34: -> STRING
                    self._adaptor.addChild(root_0, stream_STRING.nextNode())



                    retval.tree = root_0






                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:73:1: activityDef : ( ( introducesDef | interactionDef | inlineDef | runDef | recursionDef | endDef | RECLABEL ) ';' | choiceDef | directedChoiceDef | parallelDef | repeatDef | unorderedDef | recBlockDef | globalEscapeDef );
    def activityDef(self, ):

        retval = self.activityDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RECLABEL61 = None
        char_literal62 = None
        introducesDef55 = None

        interactionDef56 = None

        inlineDef57 = None

        runDef58 = None

        recursionDef59 = None

        endDef60 = None

        choiceDef63 = None

        directedChoiceDef64 = None

        parallelDef65 = None

        repeatDef66 = None

        unorderedDef67 = None

        recBlockDef68 = None

        globalEscapeDef69 = None


        RECLABEL61_tree = None
        char_literal62_tree = None

        try:
            try:
                # Generate/Monitor.g:73:12: ( ( introducesDef | interactionDef | inlineDef | runDef | recursionDef | endDef | RECLABEL ) ';' | choiceDef | directedChoiceDef | parallelDef | repeatDef | unorderedDef | recBlockDef | globalEscapeDef )
                alt20 = 8
                alt20 = self.dfa20.predict(self.input)
                if alt20 == 1:
                    # Generate/Monitor.g:73:14: ( introducesDef | interactionDef | inlineDef | runDef | recursionDef | endDef | RECLABEL ) ';'
                    pass 
                    root_0 = self._adaptor.nil()

                    # Generate/Monitor.g:73:14: ( introducesDef | interactionDef | inlineDef | runDef | recursionDef | endDef | RECLABEL )
                    alt19 = 7
                    LA19 = self.input.LA(1)
                    if LA19 == ID:
                        LA19 = self.input.LA(2)
                        if LA19 == 38 or LA19 == 43 or LA19 == 48:
                            alt19 = 2
                        elif LA19 == 37:
                            alt19 = 5
                        elif LA19 == 46:
                            alt19 = 1
                        else:
                            nvae = NoViableAltException("", 19, 1, self.input)

                            raise nvae

                    elif LA19 == ASSERTION or LA19 == 43:
                        alt19 = 2
                    elif LA19 == 55:
                        alt19 = 3
                    elif LA19 == 54:
                        alt19 = 4
                    elif LA19 == 53:
                        alt19 = 6
                    elif LA19 == RECLABEL:
                        alt19 = 7
                    else:
                        nvae = NoViableAltException("", 19, 0, self.input)

                        raise nvae

                    if alt19 == 1:
                        # Generate/Monitor.g:73:16: introducesDef
                        pass 
                        self._state.following.append(self.FOLLOW_introducesDef_in_activityDef625)
                        introducesDef55 = self.introducesDef()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, introducesDef55.tree)


                    elif alt19 == 2:
                        # Generate/Monitor.g:73:32: interactionDef
                        pass 
                        self._state.following.append(self.FOLLOW_interactionDef_in_activityDef629)
                        interactionDef56 = self.interactionDef()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, interactionDef56.tree)


                    elif alt19 == 3:
                        # Generate/Monitor.g:73:49: inlineDef
                        pass 
                        self._state.following.append(self.FOLLOW_inlineDef_in_activityDef633)
                        inlineDef57 = self.inlineDef()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, inlineDef57.tree)


                    elif alt19 == 4:
                        # Generate/Monitor.g:73:61: runDef
                        pass 
                        self._state.following.append(self.FOLLOW_runDef_in_activityDef637)
                        runDef58 = self.runDef()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, runDef58.tree)


                    elif alt19 == 5:
                        # Generate/Monitor.g:73:70: recursionDef
                        pass 
                        self._state.following.append(self.FOLLOW_recursionDef_in_activityDef641)
                        recursionDef59 = self.recursionDef()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, recursionDef59.tree)


                    elif alt19 == 6:
                        # Generate/Monitor.g:73:85: endDef
                        pass 
                        self._state.following.append(self.FOLLOW_endDef_in_activityDef645)
                        endDef60 = self.endDef()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, endDef60.tree)


                    elif alt19 == 7:
                        # Generate/Monitor.g:73:94: RECLABEL
                        pass 
                        RECLABEL61=self.match(self.input, RECLABEL, self.FOLLOW_RECLABEL_in_activityDef649)

                        RECLABEL61_tree = self._adaptor.createWithPayload(RECLABEL61)
                        self._adaptor.addChild(root_0, RECLABEL61_tree)




                    char_literal62=self.match(self.input, 37, self.FOLLOW_37_in_activityDef653)


                elif alt20 == 2:
                    # Generate/Monitor.g:74:4: choiceDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_choiceDef_in_activityDef662)
                    choiceDef63 = self.choiceDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, choiceDef63.tree)


                elif alt20 == 3:
                    # Generate/Monitor.g:74:16: directedChoiceDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_directedChoiceDef_in_activityDef666)
                    directedChoiceDef64 = self.directedChoiceDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, directedChoiceDef64.tree)


                elif alt20 == 4:
                    # Generate/Monitor.g:74:36: parallelDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_parallelDef_in_activityDef670)
                    parallelDef65 = self.parallelDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, parallelDef65.tree)


                elif alt20 == 5:
                    # Generate/Monitor.g:74:50: repeatDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_repeatDef_in_activityDef674)
                    repeatDef66 = self.repeatDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, repeatDef66.tree)


                elif alt20 == 6:
                    # Generate/Monitor.g:74:62: unorderedDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_unorderedDef_in_activityDef678)
                    unorderedDef67 = self.unorderedDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, unorderedDef67.tree)


                elif alt20 == 7:
                    # Generate/Monitor.g:75:4: recBlockDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_recBlockDef_in_activityDef685)
                    recBlockDef68 = self.recBlockDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, recBlockDef68.tree)


                elif alt20 == 8:
                    # Generate/Monitor.g:75:18: globalEscapeDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_globalEscapeDef_in_activityDef689)
                    globalEscapeDef69 = self.globalEscapeDef()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, globalEscapeDef69.tree)


                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:77:1: introducesDef : roleDef 'introduces' roleDef ( ',' roleDef )* ;
    def introducesDef(self, ):

        retval = self.introducesDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal71 = None
        char_literal73 = None
        roleDef70 = None

        roleDef72 = None

        roleDef74 = None


        string_literal71_tree = None
        char_literal73_tree = None

        try:
            try:
                # Generate/Monitor.g:77:14: ( roleDef 'introduces' roleDef ( ',' roleDef )* )
                # Generate/Monitor.g:77:16: roleDef 'introduces' roleDef ( ',' roleDef )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_roleDef_in_introducesDef697)
                roleDef70 = self.roleDef()

                self._state.following.pop()
                self._adaptor.addChild(root_0, roleDef70.tree)
                string_literal71=self.match(self.input, 46, self.FOLLOW_46_in_introducesDef699)

                string_literal71_tree = self._adaptor.createWithPayload(string_literal71)
                self._adaptor.addChild(root_0, string_literal71_tree)

                self._state.following.append(self.FOLLOW_roleDef_in_introducesDef701)
                roleDef72 = self.roleDef()

                self._state.following.pop()
                self._adaptor.addChild(root_0, roleDef72.tree)
                # Generate/Monitor.g:77:45: ( ',' roleDef )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == 36) :
                        alt21 = 1


                    if alt21 == 1:
                        # Generate/Monitor.g:77:47: ',' roleDef
                        pass 
                        char_literal73=self.match(self.input, 36, self.FOLLOW_36_in_introducesDef705)

                        char_literal73_tree = self._adaptor.createWithPayload(char_literal73)
                        self._adaptor.addChild(root_0, char_literal73_tree)

                        self._state.following.append(self.FOLLOW_roleDef_in_introducesDef707)
                        roleDef74 = self.roleDef()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, roleDef74.tree)


                    else:
                        break #loop21



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:79:1: roleDef : ID -> ID ;
    def roleDef(self, ):

        retval = self.roleDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID75 = None

        ID75_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # Generate/Monitor.g:79:8: ( ID -> ID )
                # Generate/Monitor.g:79:10: ID
                pass 
                ID75=self.match(self.input, ID, self.FOLLOW_ID_in_roleDef718) 
                stream_ID.add(ID75)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 79:13: -> ID
                self._adaptor.addChild(root_0, stream_ID.nextNode())



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:81:1: roleName : ID -> ID ;
    def roleName(self, ):

        retval = self.roleName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID76 = None

        ID76_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # Generate/Monitor.g:81:9: ( ID -> ID )
                # Generate/Monitor.g:81:11: ID
                pass 
                ID76=self.match(self.input, ID, self.FOLLOW_ID_in_roleName729) 
                stream_ID.add(ID76)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 81:14: -> ID
                self._adaptor.addChild(root_0, stream_ID.nextNode())



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:83:1: typeReferenceDef : ID -> ID ;
    def typeReferenceDef(self, ):

        retval = self.typeReferenceDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID77 = None

        ID77_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # Generate/Monitor.g:83:17: ( ID -> ID )
                # Generate/Monitor.g:83:19: ID
                pass 
                ID77=self.match(self.input, ID, self.FOLLOW_ID_in_typeReferenceDef740) 
                stream_ID.add(ID77)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 83:22: -> ID
                self._adaptor.addChild(root_0, stream_ID.nextNode())



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:84:1: interactionSignatureDef : ( ( typeReferenceDef ( '(' ( valueDecl )? ( ',' valueDecl )* ')' )? -> typeReferenceDef ^( VALUE ( valueDecl )* ) ) | ( ( '(' ( valueDecl )? ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) ) ) ;
    def interactionSignatureDef(self, ):

        retval = self.interactionSignatureDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal79 = None
        char_literal81 = None
        char_literal83 = None
        char_literal84 = None
        char_literal86 = None
        char_literal88 = None
        typeReferenceDef78 = None

        valueDecl80 = None

        valueDecl82 = None

        valueDecl85 = None

        valueDecl87 = None


        char_literal79_tree = None
        char_literal81_tree = None
        char_literal83_tree = None
        char_literal84_tree = None
        char_literal86_tree = None
        char_literal88_tree = None
        stream_43 = RewriteRuleTokenStream(self._adaptor, "token 43")
        stream_44 = RewriteRuleTokenStream(self._adaptor, "token 44")
        stream_36 = RewriteRuleTokenStream(self._adaptor, "token 36")
        stream_typeReferenceDef = RewriteRuleSubtreeStream(self._adaptor, "rule typeReferenceDef")
        stream_valueDecl = RewriteRuleSubtreeStream(self._adaptor, "rule valueDecl")
        try:
            try:
                # Generate/Monitor.g:84:24: ( ( ( typeReferenceDef ( '(' ( valueDecl )? ( ',' valueDecl )* ')' )? -> typeReferenceDef ^( VALUE ( valueDecl )* ) ) | ( ( '(' ( valueDecl )? ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) ) ) )
                # Generate/Monitor.g:84:26: ( ( typeReferenceDef ( '(' ( valueDecl )? ( ',' valueDecl )* ')' )? -> typeReferenceDef ^( VALUE ( valueDecl )* ) ) | ( ( '(' ( valueDecl )? ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) ) )
                pass 
                # Generate/Monitor.g:84:26: ( ( typeReferenceDef ( '(' ( valueDecl )? ( ',' valueDecl )* ')' )? -> typeReferenceDef ^( VALUE ( valueDecl )* ) ) | ( ( '(' ( valueDecl )? ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) ) )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == ID) :
                    alt27 = 1
                elif (LA27_0 == 43) :
                    alt27 = 2
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # Generate/Monitor.g:84:27: ( typeReferenceDef ( '(' ( valueDecl )? ( ',' valueDecl )* ')' )? -> typeReferenceDef ^( VALUE ( valueDecl )* ) )
                    pass 
                    # Generate/Monitor.g:84:27: ( typeReferenceDef ( '(' ( valueDecl )? ( ',' valueDecl )* ')' )? -> typeReferenceDef ^( VALUE ( valueDecl )* ) )
                    # Generate/Monitor.g:84:28: typeReferenceDef ( '(' ( valueDecl )? ( ',' valueDecl )* ')' )?
                    pass 
                    self._state.following.append(self.FOLLOW_typeReferenceDef_in_interactionSignatureDef751)
                    typeReferenceDef78 = self.typeReferenceDef()

                    self._state.following.pop()
                    stream_typeReferenceDef.add(typeReferenceDef78.tree)
                    # Generate/Monitor.g:84:45: ( '(' ( valueDecl )? ( ',' valueDecl )* ')' )?
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == 43) :
                        alt24 = 1
                    if alt24 == 1:
                        # Generate/Monitor.g:84:46: '(' ( valueDecl )? ( ',' valueDecl )* ')'
                        pass 
                        char_literal79=self.match(self.input, 43, self.FOLLOW_43_in_interactionSignatureDef754) 
                        stream_43.add(char_literal79)
                        # Generate/Monitor.g:84:50: ( valueDecl )?
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if ((INT <= LA22_0 <= STRING) or LA22_0 == ID) :
                            alt22 = 1
                        if alt22 == 1:
                            # Generate/Monitor.g:84:52: valueDecl
                            pass 
                            self._state.following.append(self.FOLLOW_valueDecl_in_interactionSignatureDef758)
                            valueDecl80 = self.valueDecl()

                            self._state.following.pop()
                            stream_valueDecl.add(valueDecl80.tree)



                        # Generate/Monitor.g:84:65: ( ',' valueDecl )*
                        while True: #loop23
                            alt23 = 2
                            LA23_0 = self.input.LA(1)

                            if (LA23_0 == 36) :
                                alt23 = 1


                            if alt23 == 1:
                                # Generate/Monitor.g:84:66: ',' valueDecl
                                pass 
                                char_literal81=self.match(self.input, 36, self.FOLLOW_36_in_interactionSignatureDef764) 
                                stream_36.add(char_literal81)
                                self._state.following.append(self.FOLLOW_valueDecl_in_interactionSignatureDef766)
                                valueDecl82 = self.valueDecl()

                                self._state.following.pop()
                                stream_valueDecl.add(valueDecl82.tree)


                            else:
                                break #loop23
                        char_literal83=self.match(self.input, 44, self.FOLLOW_44_in_interactionSignatureDef770) 
                        stream_44.add(char_literal83)




                    # AST Rewrite
                    # elements: typeReferenceDef, valueDecl
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 84:88: -> typeReferenceDef ^( VALUE ( valueDecl )* )
                    self._adaptor.addChild(root_0, stream_typeReferenceDef.nextTree())
                    # Generate/Monitor.g:84:108: ^( VALUE ( valueDecl )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VALUE, "VALUE"), root_1)

                    # Generate/Monitor.g:84:116: ( valueDecl )*
                    while stream_valueDecl.hasNext():
                        self._adaptor.addChild(root_1, stream_valueDecl.nextTree())


                    stream_valueDecl.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0





                elif alt27 == 2:
                    # Generate/Monitor.g:85:7: ( ( '(' ( valueDecl )? ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) )
                    pass 
                    # Generate/Monitor.g:85:7: ( ( '(' ( valueDecl )? ( ',' valueDecl )* ')' ) -> ^( VALUE ( valueDecl )* ) )
                    # Generate/Monitor.g:85:8: ( '(' ( valueDecl )? ( ',' valueDecl )* ')' )
                    pass 
                    # Generate/Monitor.g:85:8: ( '(' ( valueDecl )? ( ',' valueDecl )* ')' )
                    # Generate/Monitor.g:85:9: '(' ( valueDecl )? ( ',' valueDecl )* ')'
                    pass 
                    char_literal84=self.match(self.input, 43, self.FOLLOW_43_in_interactionSignatureDef794) 
                    stream_43.add(char_literal84)
                    # Generate/Monitor.g:85:13: ( valueDecl )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if ((INT <= LA25_0 <= STRING) or LA25_0 == ID) :
                        alt25 = 1
                    if alt25 == 1:
                        # Generate/Monitor.g:85:15: valueDecl
                        pass 
                        self._state.following.append(self.FOLLOW_valueDecl_in_interactionSignatureDef798)
                        valueDecl85 = self.valueDecl()

                        self._state.following.pop()
                        stream_valueDecl.add(valueDecl85.tree)



                    # Generate/Monitor.g:85:28: ( ',' valueDecl )*
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == 36) :
                            alt26 = 1


                        if alt26 == 1:
                            # Generate/Monitor.g:85:29: ',' valueDecl
                            pass 
                            char_literal86=self.match(self.input, 36, self.FOLLOW_36_in_interactionSignatureDef804) 
                            stream_36.add(char_literal86)
                            self._state.following.append(self.FOLLOW_valueDecl_in_interactionSignatureDef806)
                            valueDecl87 = self.valueDecl()

                            self._state.following.pop()
                            stream_valueDecl.add(valueDecl87.tree)


                        else:
                            break #loop26
                    char_literal88=self.match(self.input, 44, self.FOLLOW_44_in_interactionSignatureDef810) 
                    stream_44.add(char_literal88)




                    # AST Rewrite
                    # elements: valueDecl
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 85:50: -> ^( VALUE ( valueDecl )* )
                    # Generate/Monitor.g:85:53: ^( VALUE ( valueDecl )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VALUE, "VALUE"), root_1)

                    # Generate/Monitor.g:85:61: ( valueDecl )*
                    while stream_valueDecl.hasNext():
                        self._adaptor.addChild(root_1, stream_valueDecl.nextTree())


                    stream_valueDecl.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0









                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:87:1: valueDecl : ( ID ':' )? primitivetype ;
    def valueDecl(self, ):

        retval = self.valueDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID89 = None
        char_literal90 = None
        primitivetype91 = None


        ID89_tree = None
        char_literal90_tree = None

        try:
            try:
                # Generate/Monitor.g:87:11: ( ( ID ':' )? primitivetype )
                # Generate/Monitor.g:87:13: ( ID ':' )? primitivetype
                pass 
                root_0 = self._adaptor.nil()

                # Generate/Monitor.g:87:13: ( ID ':' )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == ID) :
                    alt28 = 1
                if alt28 == 1:
                    # Generate/Monitor.g:87:15: ID ':'
                    pass 
                    ID89=self.match(self.input, ID, self.FOLLOW_ID_in_valueDecl832)

                    ID89_tree = self._adaptor.createWithPayload(ID89)
                    self._adaptor.addChild(root_0, ID89_tree)

                    char_literal90=self.match(self.input, 47, self.FOLLOW_47_in_valueDecl834)



                self._state.following.append(self.FOLLOW_primitivetype_in_valueDecl840)
                primitivetype91 = self.primitivetype()

                self._state.following.pop()
                self._adaptor.addChild(root_0, primitivetype91.tree)



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:88:1: firstValueDecl : valueDecl ;
    def firstValueDecl(self, ):

        retval = self.firstValueDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        valueDecl92 = None



        try:
            try:
                # Generate/Monitor.g:88:16: ( valueDecl )
                # Generate/Monitor.g:88:18: valueDecl
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_valueDecl_in_firstValueDecl849)
                valueDecl92 = self.valueDecl()

                self._state.following.pop()
                self._adaptor.addChild(root_0, valueDecl92.tree)



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:91:1: interactionDef : assertDef interactionSignatureDef ( 'from' role= roleName -> ^( RESV interactionSignatureDef $role assertDef ) | 'to' roleName -> ^( SEND interactionSignatureDef roleName assertDef ) ) ;
    def interactionDef(self, ):

        retval = self.interactionDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal95 = None
        string_literal96 = None
        role = None

        assertDef93 = None

        interactionSignatureDef94 = None

        roleName97 = None


        string_literal95_tree = None
        string_literal96_tree = None
        stream_48 = RewriteRuleTokenStream(self._adaptor, "token 48")
        stream_38 = RewriteRuleTokenStream(self._adaptor, "token 38")
        stream_assertDef = RewriteRuleSubtreeStream(self._adaptor, "rule assertDef")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        stream_interactionSignatureDef = RewriteRuleSubtreeStream(self._adaptor, "rule interactionSignatureDef")
        try:
            try:
                # Generate/Monitor.g:91:15: ( assertDef interactionSignatureDef ( 'from' role= roleName -> ^( RESV interactionSignatureDef $role assertDef ) | 'to' roleName -> ^( SEND interactionSignatureDef roleName assertDef ) ) )
                # Generate/Monitor.g:92:9: assertDef interactionSignatureDef ( 'from' role= roleName -> ^( RESV interactionSignatureDef $role assertDef ) | 'to' roleName -> ^( SEND interactionSignatureDef roleName assertDef ) )
                pass 
                self._state.following.append(self.FOLLOW_assertDef_in_interactionDef866)
                assertDef93 = self.assertDef()

                self._state.following.pop()
                stream_assertDef.add(assertDef93.tree)
                self._state.following.append(self.FOLLOW_interactionSignatureDef_in_interactionDef870)
                interactionSignatureDef94 = self.interactionSignatureDef()

                self._state.following.pop()
                stream_interactionSignatureDef.add(interactionSignatureDef94.tree)
                # Generate/Monitor.g:92:47: ( 'from' role= roleName -> ^( RESV interactionSignatureDef $role assertDef ) | 'to' roleName -> ^( SEND interactionSignatureDef roleName assertDef ) )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == 38) :
                    alt29 = 1
                elif (LA29_0 == 48) :
                    alt29 = 2
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # Generate/Monitor.g:93:9: 'from' role= roleName
                    pass 
                    string_literal95=self.match(self.input, 38, self.FOLLOW_38_in_interactionDef884) 
                    stream_38.add(string_literal95)
                    self._state.following.append(self.FOLLOW_roleName_in_interactionDef889)
                    role = self.roleName()

                    self._state.following.pop()
                    stream_roleName.add(role.tree)

                    # AST Rewrite
                    # elements: assertDef, role, interactionSignatureDef
                    # token labels: 
                    # rule labels: retval, role
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

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
                    # 93:32: -> ^( RESV interactionSignatureDef $role assertDef )
                    # Generate/Monitor.g:93:35: ^( RESV interactionSignatureDef $role assertDef )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RESV, "RESV"), root_1)

                    self._adaptor.addChild(root_1, stream_interactionSignatureDef.nextTree())
                    self._adaptor.addChild(root_1, stream_role.nextTree())
                    self._adaptor.addChild(root_1, stream_assertDef.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt29 == 2:
                    # Generate/Monitor.g:94:11: 'to' roleName
                    pass 
                    string_literal96=self.match(self.input, 48, self.FOLLOW_48_in_interactionDef915) 
                    stream_48.add(string_literal96)
                    self._state.following.append(self.FOLLOW_roleName_in_interactionDef917)
                    roleName97 = self.roleName()

                    self._state.following.pop()
                    stream_roleName.add(roleName97.tree)

                    # AST Rewrite
                    # elements: assertDef, roleName, interactionSignatureDef
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 94:27: -> ^( SEND interactionSignatureDef roleName assertDef )
                    # Generate/Monitor.g:94:30: ^( SEND interactionSignatureDef roleName assertDef )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SEND, "SEND"), root_1)

                    self._adaptor.addChild(root_1, stream_interactionSignatureDef.nextTree())
                    self._adaptor.addChild(root_1, stream_roleName.nextTree())
                    self._adaptor.addChild(root_1, stream_assertDef.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0






                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:96:1: choiceDef : 'choice' ( 'at' roleName )? blockDef ( 'or' blockDef )* -> ^( 'choice' ( blockDef )+ ) ;
    def choiceDef(self, ):

        retval = self.choiceDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal98 = None
        string_literal99 = None
        string_literal102 = None
        roleName100 = None

        blockDef101 = None

        blockDef103 = None


        string_literal98_tree = None
        string_literal99_tree = None
        string_literal102_tree = None
        stream_49 = RewriteRuleTokenStream(self._adaptor, "token 49")
        stream_40 = RewriteRuleTokenStream(self._adaptor, "token 40")
        stream_50 = RewriteRuleTokenStream(self._adaptor, "token 50")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        stream_blockDef = RewriteRuleSubtreeStream(self._adaptor, "rule blockDef")
        try:
            try:
                # Generate/Monitor.g:96:10: ( 'choice' ( 'at' roleName )? blockDef ( 'or' blockDef )* -> ^( 'choice' ( blockDef )+ ) )
                # Generate/Monitor.g:96:12: 'choice' ( 'at' roleName )? blockDef ( 'or' blockDef )*
                pass 
                string_literal98=self.match(self.input, 49, self.FOLLOW_49_in_choiceDef939) 
                stream_49.add(string_literal98)
                # Generate/Monitor.g:96:21: ( 'at' roleName )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == 40) :
                    alt30 = 1
                if alt30 == 1:
                    # Generate/Monitor.g:96:23: 'at' roleName
                    pass 
                    string_literal99=self.match(self.input, 40, self.FOLLOW_40_in_choiceDef943) 
                    stream_40.add(string_literal99)
                    self._state.following.append(self.FOLLOW_roleName_in_choiceDef945)
                    roleName100 = self.roleName()

                    self._state.following.pop()
                    stream_roleName.add(roleName100.tree)



                self._state.following.append(self.FOLLOW_blockDef_in_choiceDef950)
                blockDef101 = self.blockDef()

                self._state.following.pop()
                stream_blockDef.add(blockDef101.tree)
                # Generate/Monitor.g:96:49: ( 'or' blockDef )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == 50) :
                        alt31 = 1


                    if alt31 == 1:
                        # Generate/Monitor.g:96:51: 'or' blockDef
                        pass 
                        string_literal102=self.match(self.input, 50, self.FOLLOW_50_in_choiceDef954) 
                        stream_50.add(string_literal102)
                        self._state.following.append(self.FOLLOW_blockDef_in_choiceDef956)
                        blockDef103 = self.blockDef()

                        self._state.following.pop()
                        stream_blockDef.add(blockDef103.tree)


                    else:
                        break #loop31

                # AST Rewrite
                # elements: 49, blockDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 96:68: -> ^( 'choice' ( blockDef )+ )
                # Generate/Monitor.g:96:71: ^( 'choice' ( blockDef )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_49.nextNode(), root_1)

                # Generate/Monitor.g:96:82: ( blockDef )+
                if not (stream_blockDef.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_blockDef.hasNext():
                    self._adaptor.addChild(root_1, stream_blockDef.nextTree())


                stream_blockDef.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:98:1: directedChoiceDef : ( 'from' roleName )? ( 'to' roleName ( ',' roleName )* )? '{' ( onMessageDef )+ '}' ;
    def directedChoiceDef(self, ):

        retval = self.directedChoiceDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal104 = None
        string_literal106 = None
        char_literal108 = None
        char_literal110 = None
        char_literal112 = None
        roleName105 = None

        roleName107 = None

        roleName109 = None

        onMessageDef111 = None


        string_literal104_tree = None
        string_literal106_tree = None
        char_literal108_tree = None
        char_literal110_tree = None
        char_literal112_tree = None

        try:
            try:
                # Generate/Monitor.g:98:18: ( ( 'from' roleName )? ( 'to' roleName ( ',' roleName )* )? '{' ( onMessageDef )+ '}' )
                # Generate/Monitor.g:98:20: ( 'from' roleName )? ( 'to' roleName ( ',' roleName )* )? '{' ( onMessageDef )+ '}'
                pass 
                root_0 = self._adaptor.nil()

                # Generate/Monitor.g:98:20: ( 'from' roleName )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == 38) :
                    alt32 = 1
                if alt32 == 1:
                    # Generate/Monitor.g:98:22: 'from' roleName
                    pass 
                    string_literal104=self.match(self.input, 38, self.FOLLOW_38_in_directedChoiceDef977)

                    string_literal104_tree = self._adaptor.createWithPayload(string_literal104)
                    self._adaptor.addChild(root_0, string_literal104_tree)

                    self._state.following.append(self.FOLLOW_roleName_in_directedChoiceDef979)
                    roleName105 = self.roleName()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, roleName105.tree)



                # Generate/Monitor.g:98:41: ( 'to' roleName ( ',' roleName )* )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == 48) :
                    alt34 = 1
                if alt34 == 1:
                    # Generate/Monitor.g:98:43: 'to' roleName ( ',' roleName )*
                    pass 
                    string_literal106=self.match(self.input, 48, self.FOLLOW_48_in_directedChoiceDef986)

                    string_literal106_tree = self._adaptor.createWithPayload(string_literal106)
                    self._adaptor.addChild(root_0, string_literal106_tree)

                    self._state.following.append(self.FOLLOW_roleName_in_directedChoiceDef988)
                    roleName107 = self.roleName()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, roleName107.tree)
                    # Generate/Monitor.g:98:57: ( ',' roleName )*
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == 36) :
                            alt33 = 1


                        if alt33 == 1:
                            # Generate/Monitor.g:98:59: ',' roleName
                            pass 
                            char_literal108=self.match(self.input, 36, self.FOLLOW_36_in_directedChoiceDef992)
                            self._state.following.append(self.FOLLOW_roleName_in_directedChoiceDef995)
                            roleName109 = self.roleName()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, roleName109.tree)


                        else:
                            break #loop33



                char_literal110=self.match(self.input, 41, self.FOLLOW_41_in_directedChoiceDef1003)

                char_literal110_tree = self._adaptor.createWithPayload(char_literal110)
                self._adaptor.addChild(root_0, char_literal110_tree)

                # Generate/Monitor.g:98:83: ( onMessageDef )+
                cnt35 = 0
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == ID or LA35_0 == 43) :
                        alt35 = 1


                    if alt35 == 1:
                        # Generate/Monitor.g:98:85: onMessageDef
                        pass 
                        self._state.following.append(self.FOLLOW_onMessageDef_in_directedChoiceDef1007)
                        onMessageDef111 = self.onMessageDef()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, onMessageDef111.tree)


                    else:
                        if cnt35 >= 1:
                            break #loop35

                        eee = EarlyExitException(35, self.input)
                        raise eee

                    cnt35 += 1
                char_literal112=self.match(self.input, 42, self.FOLLOW_42_in_directedChoiceDef1012)

                char_literal112_tree = self._adaptor.createWithPayload(char_literal112)
                self._adaptor.addChild(root_0, char_literal112_tree)




                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:100:1: onMessageDef : interactionSignatureDef ':' activityList ;
    def onMessageDef(self, ):

        retval = self.onMessageDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal114 = None
        interactionSignatureDef113 = None

        activityList115 = None


        char_literal114_tree = None

        try:
            try:
                # Generate/Monitor.g:100:13: ( interactionSignatureDef ':' activityList )
                # Generate/Monitor.g:100:15: interactionSignatureDef ':' activityList
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_interactionSignatureDef_in_onMessageDef1019)
                interactionSignatureDef113 = self.interactionSignatureDef()

                self._state.following.pop()
                self._adaptor.addChild(root_0, interactionSignatureDef113.tree)
                char_literal114=self.match(self.input, 47, self.FOLLOW_47_in_onMessageDef1021)

                char_literal114_tree = self._adaptor.createWithPayload(char_literal114)
                self._adaptor.addChild(root_0, char_literal114_tree)

                self._state.following.append(self.FOLLOW_activityList_in_onMessageDef1023)
                activityList115 = self.activityList()

                self._state.following.pop()
                self._adaptor.addChild(root_0, activityList115.tree)



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:102:1: activityList : ( ( ANNOTATION )* activityDef )* ;
    def activityList(self, ):

        retval = self.activityList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ANNOTATION116 = None
        activityDef117 = None


        ANNOTATION116_tree = None

        try:
            try:
                # Generate/Monitor.g:102:13: ( ( ( ANNOTATION )* activityDef )* )
                # Generate/Monitor.g:102:15: ( ( ANNOTATION )* activityDef )*
                pass 
                root_0 = self._adaptor.nil()

                # Generate/Monitor.g:102:15: ( ( ANNOTATION )* activityDef )*
                while True: #loop37
                    alt37 = 2
                    alt37 = self.dfa37.predict(self.input)
                    if alt37 == 1:
                        # Generate/Monitor.g:102:17: ( ANNOTATION )* activityDef
                        pass 
                        # Generate/Monitor.g:102:17: ( ANNOTATION )*
                        while True: #loop36
                            alt36 = 2
                            LA36_0 = self.input.LA(1)

                            if (LA36_0 == ANNOTATION) :
                                alt36 = 1


                            if alt36 == 1:
                                # Generate/Monitor.g:102:19: ANNOTATION
                                pass 
                                ANNOTATION116=self.match(self.input, ANNOTATION, self.FOLLOW_ANNOTATION_in_activityList1036)

                                ANNOTATION116_tree = self._adaptor.createWithPayload(ANNOTATION116)
                                self._adaptor.addChild(root_0, ANNOTATION116_tree)



                            else:
                                break #loop36
                        self._state.following.append(self.FOLLOW_activityDef_in_activityList1041)
                        activityDef117 = self.activityDef()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, activityDef117.tree)


                    else:
                        break #loop37



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:104:1: repeatDef : 'repeat' ( 'at' roleName ( ',' roleName )* )? blockDef -> ^( 'repeat' blockDef ) ;
    def repeatDef(self, ):

        retval = self.repeatDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal118 = None
        string_literal119 = None
        char_literal121 = None
        roleName120 = None

        roleName122 = None

        blockDef123 = None


        string_literal118_tree = None
        string_literal119_tree = None
        char_literal121_tree = None
        stream_40 = RewriteRuleTokenStream(self._adaptor, "token 40")
        stream_51 = RewriteRuleTokenStream(self._adaptor, "token 51")
        stream_36 = RewriteRuleTokenStream(self._adaptor, "token 36")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        stream_blockDef = RewriteRuleSubtreeStream(self._adaptor, "rule blockDef")
        try:
            try:
                # Generate/Monitor.g:104:10: ( 'repeat' ( 'at' roleName ( ',' roleName )* )? blockDef -> ^( 'repeat' blockDef ) )
                # Generate/Monitor.g:104:12: 'repeat' ( 'at' roleName ( ',' roleName )* )? blockDef
                pass 
                string_literal118=self.match(self.input, 51, self.FOLLOW_51_in_repeatDef1051) 
                stream_51.add(string_literal118)
                # Generate/Monitor.g:104:21: ( 'at' roleName ( ',' roleName )* )?
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == 40) :
                    alt39 = 1
                if alt39 == 1:
                    # Generate/Monitor.g:104:23: 'at' roleName ( ',' roleName )*
                    pass 
                    string_literal119=self.match(self.input, 40, self.FOLLOW_40_in_repeatDef1055) 
                    stream_40.add(string_literal119)
                    self._state.following.append(self.FOLLOW_roleName_in_repeatDef1057)
                    roleName120 = self.roleName()

                    self._state.following.pop()
                    stream_roleName.add(roleName120.tree)
                    # Generate/Monitor.g:104:37: ( ',' roleName )*
                    while True: #loop38
                        alt38 = 2
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == 36) :
                            alt38 = 1


                        if alt38 == 1:
                            # Generate/Monitor.g:104:39: ',' roleName
                            pass 
                            char_literal121=self.match(self.input, 36, self.FOLLOW_36_in_repeatDef1061) 
                            stream_36.add(char_literal121)
                            self._state.following.append(self.FOLLOW_roleName_in_repeatDef1063)
                            roleName122 = self.roleName()

                            self._state.following.pop()
                            stream_roleName.add(roleName122.tree)


                        else:
                            break #loop38



                self._state.following.append(self.FOLLOW_blockDef_in_repeatDef1071)
                blockDef123 = self.blockDef()

                self._state.following.pop()
                stream_blockDef.add(blockDef123.tree)

                # AST Rewrite
                # elements: 51, blockDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 104:68: -> ^( 'repeat' blockDef )
                # Generate/Monitor.g:104:71: ^( 'repeat' blockDef )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_51.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_blockDef.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:106:1: recBlockDef : assertDef 'rec' labelName blockDef -> ^( 'rec' labelName blockDef ) ;
    def recBlockDef(self, ):

        retval = self.recBlockDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal125 = None
        assertDef124 = None

        labelName126 = None

        blockDef127 = None


        string_literal125_tree = None
        stream_52 = RewriteRuleTokenStream(self._adaptor, "token 52")
        stream_assertDef = RewriteRuleSubtreeStream(self._adaptor, "rule assertDef")
        stream_labelName = RewriteRuleSubtreeStream(self._adaptor, "rule labelName")
        stream_blockDef = RewriteRuleSubtreeStream(self._adaptor, "rule blockDef")
        try:
            try:
                # Generate/Monitor.g:106:12: ( assertDef 'rec' labelName blockDef -> ^( 'rec' labelName blockDef ) )
                # Generate/Monitor.g:106:14: assertDef 'rec' labelName blockDef
                pass 
                self._state.following.append(self.FOLLOW_assertDef_in_recBlockDef1087)
                assertDef124 = self.assertDef()

                self._state.following.pop()
                stream_assertDef.add(assertDef124.tree)
                string_literal125=self.match(self.input, 52, self.FOLLOW_52_in_recBlockDef1089) 
                stream_52.add(string_literal125)
                self._state.following.append(self.FOLLOW_labelName_in_recBlockDef1091)
                labelName126 = self.labelName()

                self._state.following.pop()
                stream_labelName.add(labelName126.tree)
                self._state.following.append(self.FOLLOW_blockDef_in_recBlockDef1093)
                blockDef127 = self.blockDef()

                self._state.following.pop()
                stream_blockDef.add(blockDef127.tree)

                # AST Rewrite
                # elements: 52, labelName, blockDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 106:49: -> ^( 'rec' labelName blockDef )
                # Generate/Monitor.g:106:52: ^( 'rec' labelName blockDef )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_52.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_labelName.nextTree())
                self._adaptor.addChild(root_1, stream_blockDef.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:108:1: labelName : ID -> ID ;
    def labelName(self, ):

        retval = self.labelName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID128 = None

        ID128_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # Generate/Monitor.g:108:10: ( ID -> ID )
                # Generate/Monitor.g:108:12: ID
                pass 
                ID128=self.match(self.input, ID, self.FOLLOW_ID_in_labelName1110) 
                stream_ID.add(ID128)

                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 108:15: -> ID
                self._adaptor.addChild(root_0, stream_ID.nextNode())



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:110:1: recursionDef : labelName -> ^( RECLABEL labelName ) ;
    def recursionDef(self, ):

        retval = self.recursionDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        labelName129 = None


        stream_labelName = RewriteRuleSubtreeStream(self._adaptor, "rule labelName")
        try:
            try:
                # Generate/Monitor.g:110:13: ( labelName -> ^( RECLABEL labelName ) )
                # Generate/Monitor.g:110:15: labelName
                pass 
                self._state.following.append(self.FOLLOW_labelName_in_recursionDef1122)
                labelName129 = self.labelName()

                self._state.following.pop()
                stream_labelName.add(labelName129.tree)

                # AST Rewrite
                # elements: labelName
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 110:25: -> ^( RECLABEL labelName )
                # Generate/Monitor.g:110:28: ^( RECLABEL labelName )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RECLABEL, "RECLABEL"), root_1)

                self._adaptor.addChild(root_1, stream_labelName.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:113:1: endDef : 'end' ;
    def endDef(self, ):

        retval = self.endDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal130 = None

        string_literal130_tree = None

        try:
            try:
                # Generate/Monitor.g:113:7: ( 'end' )
                # Generate/Monitor.g:113:9: 'end'
                pass 
                root_0 = self._adaptor.nil()

                string_literal130=self.match(self.input, 53, self.FOLLOW_53_in_endDef1138)

                string_literal130_tree = self._adaptor.createWithPayload(string_literal130)
                root_0 = self._adaptor.becomeRoot(string_literal130_tree, root_0)




                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:116:1: runDef : 'run' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )? 'from' roleName ;
    def runDef(self, ):

        retval = self.runDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal131 = None
        char_literal133 = None
        char_literal135 = None
        char_literal137 = None
        string_literal138 = None
        protocolRefDef132 = None

        parameter134 = None

        parameter136 = None

        roleName139 = None


        string_literal131_tree = None
        char_literal133_tree = None
        char_literal135_tree = None
        char_literal137_tree = None
        string_literal138_tree = None

        try:
            try:
                # Generate/Monitor.g:116:7: ( 'run' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )? 'from' roleName )
                # Generate/Monitor.g:116:9: 'run' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )? 'from' roleName
                pass 
                root_0 = self._adaptor.nil()

                string_literal131=self.match(self.input, 54, self.FOLLOW_54_in_runDef1148)

                string_literal131_tree = self._adaptor.createWithPayload(string_literal131)
                root_0 = self._adaptor.becomeRoot(string_literal131_tree, root_0)

                self._state.following.append(self.FOLLOW_protocolRefDef_in_runDef1151)
                protocolRefDef132 = self.protocolRefDef()

                self._state.following.pop()
                self._adaptor.addChild(root_0, protocolRefDef132.tree)
                # Generate/Monitor.g:116:31: ( '(' parameter ( ',' parameter )* ')' )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == 43) :
                    alt41 = 1
                if alt41 == 1:
                    # Generate/Monitor.g:116:33: '(' parameter ( ',' parameter )* ')'
                    pass 
                    char_literal133=self.match(self.input, 43, self.FOLLOW_43_in_runDef1155)
                    self._state.following.append(self.FOLLOW_parameter_in_runDef1158)
                    parameter134 = self.parameter()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, parameter134.tree)
                    # Generate/Monitor.g:116:48: ( ',' parameter )*
                    while True: #loop40
                        alt40 = 2
                        LA40_0 = self.input.LA(1)

                        if (LA40_0 == 36) :
                            alt40 = 1


                        if alt40 == 1:
                            # Generate/Monitor.g:116:50: ',' parameter
                            pass 
                            char_literal135=self.match(self.input, 36, self.FOLLOW_36_in_runDef1162)
                            self._state.following.append(self.FOLLOW_parameter_in_runDef1165)
                            parameter136 = self.parameter()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, parameter136.tree)


                        else:
                            break #loop40
                    char_literal137=self.match(self.input, 44, self.FOLLOW_44_in_runDef1170)



                string_literal138=self.match(self.input, 38, self.FOLLOW_38_in_runDef1176)

                string_literal138_tree = self._adaptor.createWithPayload(string_literal138)
                self._adaptor.addChild(root_0, string_literal138_tree)

                self._state.following.append(self.FOLLOW_roleName_in_runDef1178)
                roleName139 = self.roleName()

                self._state.following.pop()
                self._adaptor.addChild(root_0, roleName139.tree)



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:118:1: protocolRefDef : ID ( 'at' roleName )? ;
    def protocolRefDef(self, ):

        retval = self.protocolRefDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID140 = None
        string_literal141 = None
        roleName142 = None


        ID140_tree = None
        string_literal141_tree = None

        try:
            try:
                # Generate/Monitor.g:118:15: ( ID ( 'at' roleName )? )
                # Generate/Monitor.g:118:17: ID ( 'at' roleName )?
                pass 
                root_0 = self._adaptor.nil()

                ID140=self.match(self.input, ID, self.FOLLOW_ID_in_protocolRefDef1186)

                ID140_tree = self._adaptor.createWithPayload(ID140)
                self._adaptor.addChild(root_0, ID140_tree)

                # Generate/Monitor.g:118:20: ( 'at' roleName )?
                alt42 = 2
                LA42_0 = self.input.LA(1)

                if (LA42_0 == 40) :
                    alt42 = 1
                if alt42 == 1:
                    # Generate/Monitor.g:118:22: 'at' roleName
                    pass 
                    string_literal141=self.match(self.input, 40, self.FOLLOW_40_in_protocolRefDef1190)

                    string_literal141_tree = self._adaptor.createWithPayload(string_literal141)
                    self._adaptor.addChild(root_0, string_literal141_tree)

                    self._state.following.append(self.FOLLOW_roleName_in_protocolRefDef1192)
                    roleName142 = self.roleName()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, roleName142.tree)






                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:120:1: declarationName : ID ;
    def declarationName(self, ):

        retval = self.declarationName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID143 = None

        ID143_tree = None

        try:
            try:
                # Generate/Monitor.g:120:16: ( ID )
                # Generate/Monitor.g:120:18: ID
                pass 
                root_0 = self._adaptor.nil()

                ID143=self.match(self.input, ID, self.FOLLOW_ID_in_declarationName1203)

                ID143_tree = self._adaptor.createWithPayload(ID143)
                self._adaptor.addChild(root_0, ID143_tree)




                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:122:1: parameter : declarationName ;
    def parameter(self, ):

        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        declarationName144 = None



        try:
            try:
                # Generate/Monitor.g:122:10: ( declarationName )
                # Generate/Monitor.g:122:12: declarationName
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_declarationName_in_parameter1211)
                declarationName144 = self.declarationName()

                self._state.following.pop()
                self._adaptor.addChild(root_0, declarationName144.tree)



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:125:1: inlineDef : 'inline' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )? ;
    def inlineDef(self, ):

        retval = self.inlineDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal145 = None
        char_literal147 = None
        char_literal149 = None
        char_literal151 = None
        protocolRefDef146 = None

        parameter148 = None

        parameter150 = None


        string_literal145_tree = None
        char_literal147_tree = None
        char_literal149_tree = None
        char_literal151_tree = None

        try:
            try:
                # Generate/Monitor.g:125:10: ( 'inline' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )? )
                # Generate/Monitor.g:125:12: 'inline' protocolRefDef ( '(' parameter ( ',' parameter )* ')' )?
                pass 
                root_0 = self._adaptor.nil()

                string_literal145=self.match(self.input, 55, self.FOLLOW_55_in_inlineDef1220)

                string_literal145_tree = self._adaptor.createWithPayload(string_literal145)
                root_0 = self._adaptor.becomeRoot(string_literal145_tree, root_0)

                self._state.following.append(self.FOLLOW_protocolRefDef_in_inlineDef1223)
                protocolRefDef146 = self.protocolRefDef()

                self._state.following.pop()
                self._adaptor.addChild(root_0, protocolRefDef146.tree)
                # Generate/Monitor.g:125:37: ( '(' parameter ( ',' parameter )* ')' )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if (LA44_0 == 43) :
                    alt44 = 1
                if alt44 == 1:
                    # Generate/Monitor.g:125:39: '(' parameter ( ',' parameter )* ')'
                    pass 
                    char_literal147=self.match(self.input, 43, self.FOLLOW_43_in_inlineDef1227)
                    self._state.following.append(self.FOLLOW_parameter_in_inlineDef1230)
                    parameter148 = self.parameter()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, parameter148.tree)
                    # Generate/Monitor.g:125:54: ( ',' parameter )*
                    while True: #loop43
                        alt43 = 2
                        LA43_0 = self.input.LA(1)

                        if (LA43_0 == 36) :
                            alt43 = 1


                        if alt43 == 1:
                            # Generate/Monitor.g:125:56: ',' parameter
                            pass 
                            char_literal149=self.match(self.input, 36, self.FOLLOW_36_in_inlineDef1234)
                            self._state.following.append(self.FOLLOW_parameter_in_inlineDef1237)
                            parameter150 = self.parameter()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, parameter150.tree)


                        else:
                            break #loop43
                    char_literal151=self.match(self.input, 44, self.FOLLOW_44_in_inlineDef1242)






                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:127:1: parallelDef : 'parallel' blockDef ( 'and' blockDef )* -> ^( PARALLEL ( blockDef )+ ) ;
    def parallelDef(self, ):

        retval = self.parallelDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal152 = None
        string_literal154 = None
        blockDef153 = None

        blockDef155 = None


        string_literal152_tree = None
        string_literal154_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_blockDef = RewriteRuleSubtreeStream(self._adaptor, "rule blockDef")
        try:
            try:
                # Generate/Monitor.g:127:12: ( 'parallel' blockDef ( 'and' blockDef )* -> ^( PARALLEL ( blockDef )+ ) )
                # Generate/Monitor.g:127:14: 'parallel' blockDef ( 'and' blockDef )*
                pass 
                string_literal152=self.match(self.input, 56, self.FOLLOW_56_in_parallelDef1254) 
                stream_56.add(string_literal152)
                self._state.following.append(self.FOLLOW_blockDef_in_parallelDef1256)
                blockDef153 = self.blockDef()

                self._state.following.pop()
                stream_blockDef.add(blockDef153.tree)
                # Generate/Monitor.g:127:34: ( 'and' blockDef )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == 57) :
                        alt45 = 1


                    if alt45 == 1:
                        # Generate/Monitor.g:127:36: 'and' blockDef
                        pass 
                        string_literal154=self.match(self.input, 57, self.FOLLOW_57_in_parallelDef1260) 
                        stream_57.add(string_literal154)
                        self._state.following.append(self.FOLLOW_blockDef_in_parallelDef1262)
                        blockDef155 = self.blockDef()

                        self._state.following.pop()
                        stream_blockDef.add(blockDef155.tree)


                    else:
                        break #loop45

                # AST Rewrite
                # elements: blockDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 127:54: -> ^( PARALLEL ( blockDef )+ )
                # Generate/Monitor.g:127:57: ^( PARALLEL ( blockDef )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARALLEL, "PARALLEL"), root_1)

                # Generate/Monitor.g:127:68: ( blockDef )+
                if not (stream_blockDef.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_blockDef.hasNext():
                    self._adaptor.addChild(root_1, stream_blockDef.nextTree())


                stream_blockDef.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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

    class doBlockDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.doBlockDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "doBlockDef"
    # Generate/Monitor.g:130:1: doBlockDef : 'do' '{' activityListDef '}' -> ^( 'do' activityListDef ) ;
    def doBlockDef(self, ):

        retval = self.doBlockDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal156 = None
        char_literal157 = None
        char_literal159 = None
        activityListDef158 = None


        string_literal156_tree = None
        char_literal157_tree = None
        char_literal159_tree = None
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_42 = RewriteRuleTokenStream(self._adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_activityListDef = RewriteRuleSubtreeStream(self._adaptor, "rule activityListDef")
        try:
            try:
                # Generate/Monitor.g:130:11: ( 'do' '{' activityListDef '}' -> ^( 'do' activityListDef ) )
                # Generate/Monitor.g:130:13: 'do' '{' activityListDef '}'
                pass 
                string_literal156=self.match(self.input, 58, self.FOLLOW_58_in_doBlockDef1282) 
                stream_58.add(string_literal156)
                char_literal157=self.match(self.input, 41, self.FOLLOW_41_in_doBlockDef1284) 
                stream_41.add(char_literal157)
                self._state.following.append(self.FOLLOW_activityListDef_in_doBlockDef1286)
                activityListDef158 = self.activityListDef()

                self._state.following.pop()
                stream_activityListDef.add(activityListDef158.tree)
                char_literal159=self.match(self.input, 42, self.FOLLOW_42_in_doBlockDef1289) 
                stream_42.add(char_literal159)

                # AST Rewrite
                # elements: activityListDef, 58
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 130:43: -> ^( 'do' activityListDef )
                # Generate/Monitor.g:130:46: ^( 'do' activityListDef )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_58.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_activityListDef.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "doBlockDef"

    class interruptDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.interruptDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "interruptDef"
    # Generate/Monitor.g:132:1: interruptDef : 'interrupt' 'by' roleName '{' activityListDef '}' -> ^( 'interrupt' roleName activityListDef ) ;
    def interruptDef(self, ):

        retval = self.interruptDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal160 = None
        string_literal161 = None
        char_literal163 = None
        char_literal165 = None
        roleName162 = None

        activityListDef164 = None


        string_literal160_tree = None
        string_literal161_tree = None
        char_literal163_tree = None
        char_literal165_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_42 = RewriteRuleTokenStream(self._adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_activityListDef = RewriteRuleSubtreeStream(self._adaptor, "rule activityListDef")
        stream_roleName = RewriteRuleSubtreeStream(self._adaptor, "rule roleName")
        try:
            try:
                # Generate/Monitor.g:132:13: ( 'interrupt' 'by' roleName '{' activityListDef '}' -> ^( 'interrupt' roleName activityListDef ) )
                # Generate/Monitor.g:132:15: 'interrupt' 'by' roleName '{' activityListDef '}'
                pass 
                string_literal160=self.match(self.input, 59, self.FOLLOW_59_in_interruptDef1307) 
                stream_59.add(string_literal160)
                string_literal161=self.match(self.input, 60, self.FOLLOW_60_in_interruptDef1309) 
                stream_60.add(string_literal161)
                self._state.following.append(self.FOLLOW_roleName_in_interruptDef1311)
                roleName162 = self.roleName()

                self._state.following.pop()
                stream_roleName.add(roleName162.tree)
                char_literal163=self.match(self.input, 41, self.FOLLOW_41_in_interruptDef1313) 
                stream_41.add(char_literal163)
                self._state.following.append(self.FOLLOW_activityListDef_in_interruptDef1315)
                activityListDef164 = self.activityListDef()

                self._state.following.pop()
                stream_activityListDef.add(activityListDef164.tree)
                char_literal165=self.match(self.input, 42, self.FOLLOW_42_in_interruptDef1317) 
                stream_42.add(char_literal165)

                # AST Rewrite
                # elements: 59, roleName, activityListDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 132:65: -> ^( 'interrupt' roleName activityListDef )
                # Generate/Monitor.g:132:68: ^( 'interrupt' roleName activityListDef )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_59.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_roleName.nextTree())
                self._adaptor.addChild(root_1, stream_activityListDef.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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

    class globalEscapeDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.globalEscapeDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "globalEscapeDef"
    # Generate/Monitor.g:134:1: globalEscapeDef : doBlockDef interruptDef -> ^( GLOBAL_ESCAPE doBlockDef interruptDef ) ;
    def globalEscapeDef(self, ):

        retval = self.globalEscapeDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        doBlockDef166 = None

        interruptDef167 = None


        stream_interruptDef = RewriteRuleSubtreeStream(self._adaptor, "rule interruptDef")
        stream_doBlockDef = RewriteRuleSubtreeStream(self._adaptor, "rule doBlockDef")
        try:
            try:
                # Generate/Monitor.g:134:16: ( doBlockDef interruptDef -> ^( GLOBAL_ESCAPE doBlockDef interruptDef ) )
                # Generate/Monitor.g:134:19: doBlockDef interruptDef
                pass 
                self._state.following.append(self.FOLLOW_doBlockDef_in_globalEscapeDef1335)
                doBlockDef166 = self.doBlockDef()

                self._state.following.pop()
                stream_doBlockDef.add(doBlockDef166.tree)
                self._state.following.append(self.FOLLOW_interruptDef_in_globalEscapeDef1338)
                interruptDef167 = self.interruptDef()

                self._state.following.pop()
                stream_interruptDef.add(interruptDef167.tree)

                # AST Rewrite
                # elements: interruptDef, doBlockDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 134:44: -> ^( GLOBAL_ESCAPE doBlockDef interruptDef )
                # Generate/Monitor.g:134:47: ^( GLOBAL_ESCAPE doBlockDef interruptDef )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GLOBAL_ESCAPE, "GLOBAL_ESCAPE"), root_1)

                self._adaptor.addChild(root_1, stream_doBlockDef.nextTree())
                self._adaptor.addChild(root_1, stream_interruptDef.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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

    class unorderedDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.unorderedDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "unorderedDef"
    # Generate/Monitor.g:136:1: unorderedDef : 'unordered' '{' ( ( ANNOTATION )* activityDef )* '}' -> ^( PARALLEL ( ^( BRANCH activityDef ) )+ ) ;
    def unorderedDef(self, ):

        retval = self.unorderedDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal168 = None
        char_literal169 = None
        ANNOTATION170 = None
        char_literal172 = None
        activityDef171 = None


        string_literal168_tree = None
        char_literal169_tree = None
        ANNOTATION170_tree = None
        char_literal172_tree = None
        stream_42 = RewriteRuleTokenStream(self._adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self._adaptor, "token 41")
        stream_ANNOTATION = RewriteRuleTokenStream(self._adaptor, "token ANNOTATION")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
        stream_activityDef = RewriteRuleSubtreeStream(self._adaptor, "rule activityDef")
        try:
            try:
                # Generate/Monitor.g:136:13: ( 'unordered' '{' ( ( ANNOTATION )* activityDef )* '}' -> ^( PARALLEL ( ^( BRANCH activityDef ) )+ ) )
                # Generate/Monitor.g:136:15: 'unordered' '{' ( ( ANNOTATION )* activityDef )* '}'
                pass 
                string_literal168=self.match(self.input, 61, self.FOLLOW_61_in_unorderedDef1355) 
                stream_61.add(string_literal168)
                char_literal169=self.match(self.input, 41, self.FOLLOW_41_in_unorderedDef1357) 
                stream_41.add(char_literal169)
                # Generate/Monitor.g:136:31: ( ( ANNOTATION )* activityDef )*
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == RECLABEL or (ANNOTATION <= LA47_0 <= ID) or LA47_0 == ASSERTION or LA47_0 == 38 or LA47_0 == 41 or LA47_0 == 43 or (48 <= LA47_0 <= 49) or (51 <= LA47_0 <= 56) or LA47_0 == 58 or LA47_0 == 61) :
                        alt47 = 1


                    if alt47 == 1:
                        # Generate/Monitor.g:136:33: ( ANNOTATION )* activityDef
                        pass 
                        # Generate/Monitor.g:136:33: ( ANNOTATION )*
                        while True: #loop46
                            alt46 = 2
                            LA46_0 = self.input.LA(1)

                            if (LA46_0 == ANNOTATION) :
                                alt46 = 1


                            if alt46 == 1:
                                # Generate/Monitor.g:136:35: ANNOTATION
                                pass 
                                ANNOTATION170=self.match(self.input, ANNOTATION, self.FOLLOW_ANNOTATION_in_unorderedDef1363) 
                                stream_ANNOTATION.add(ANNOTATION170)


                            else:
                                break #loop46
                        self._state.following.append(self.FOLLOW_activityDef_in_unorderedDef1368)
                        activityDef171 = self.activityDef()

                        self._state.following.pop()
                        stream_activityDef.add(activityDef171.tree)


                    else:
                        break #loop47
                char_literal172=self.match(self.input, 42, self.FOLLOW_42_in_unorderedDef1373) 
                stream_42.add(char_literal172)

                # AST Rewrite
                # elements: activityDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 136:68: -> ^( PARALLEL ( ^( BRANCH activityDef ) )+ )
                # Generate/Monitor.g:136:71: ^( PARALLEL ( ^( BRANCH activityDef ) )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARALLEL, "PARALLEL"), root_1)

                # Generate/Monitor.g:136:82: ( ^( BRANCH activityDef ) )+
                if not (stream_activityDef.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_activityDef.hasNext():
                    # Generate/Monitor.g:136:82: ^( BRANCH activityDef )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(BRANCH, "BRANCH"), root_2)

                    self._adaptor.addChild(root_2, stream_activityDef.nextTree())

                    self._adaptor.addChild(root_1, root_2)


                stream_activityDef.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


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

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(MonitorParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # Generate/Monitor.g:145:1: expr : term ( ( PLUS | MINUS ) term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set174 = None
        term173 = None

        term175 = None


        set174_tree = None

        try:
            try:
                # Generate/Monitor.g:145:6: ( term ( ( PLUS | MINUS ) term )* )
                # Generate/Monitor.g:145:8: term ( ( PLUS | MINUS ) term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1398)
                term173 = self.term()

                self._state.following.pop()
                self._adaptor.addChild(root_0, term173.tree)
                # Generate/Monitor.g:145:13: ( ( PLUS | MINUS ) term )*
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if ((PLUS <= LA48_0 <= MINUS)) :
                        alt48 = 1


                    if alt48 == 1:
                        # Generate/Monitor.g:145:15: ( PLUS | MINUS ) term
                        pass 
                        set174 = self.input.LT(1)
                        if (PLUS <= self.input.LA(1) <= MINUS):
                            self.input.consume()
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set174))
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_term_in_expr1413)
                        term175 = self.term()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, term175.tree)


                    else:
                        break #loop48



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:147:1: term : factor ( ( MULT | DIV ) factor )* ;
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set177 = None
        factor176 = None

        factor178 = None


        set177_tree = None

        try:
            try:
                # Generate/Monitor.g:147:6: ( factor ( ( MULT | DIV ) factor )* )
                # Generate/Monitor.g:147:8: factor ( ( MULT | DIV ) factor )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_factor_in_term1425)
                factor176 = self.factor()

                self._state.following.pop()
                self._adaptor.addChild(root_0, factor176.tree)
                # Generate/Monitor.g:147:15: ( ( MULT | DIV ) factor )*
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if ((MULT <= LA49_0 <= DIV)) :
                        alt49 = 1


                    if alt49 == 1:
                        # Generate/Monitor.g:147:17: ( MULT | DIV ) factor
                        pass 
                        set177 = self.input.LT(1)
                        if (MULT <= self.input.LA(1) <= DIV):
                            self.input.consume()
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set177))
                            self._state.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_factor_in_term1439)
                        factor178 = self.factor()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, factor178.tree)


                    else:
                        break #loop49



                retval.stop = self.input.LT(-1)


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
    # Generate/Monitor.g:149:1: factor : NUMBER ;
    def factor(self, ):

        retval = self.factor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NUMBER179 = None

        NUMBER179_tree = None

        try:
            try:
                # Generate/Monitor.g:149:8: ( NUMBER )
                # Generate/Monitor.g:149:10: NUMBER
                pass 
                root_0 = self._adaptor.nil()

                NUMBER179=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_factor1451)

                NUMBER179_tree = self._adaptor.createWithPayload(NUMBER179)
                self._adaptor.addChild(root_0, NUMBER179_tree)




                retval.stop = self.input.LT(-1)


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


    # Delegated rules


    # lookup tables for DFA #3

    DFA3_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA3_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA3_min = DFA.unpack(
        u"\2\31\2\uffff"
        )

    DFA3_max = DFA.unpack(
        u"\2\43\2\uffff"
        )

    DFA3_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA3_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA3_transition = [
        DFA.unpack(u"\1\1\10\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\10\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #3

    class DFA3(DFA):
        pass


    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA17_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\2\22\2\uffff"
        )

    DFA17_max = DFA.unpack(
        u"\2\75\2\uffff"
        )

    DFA17_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA17_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA17_transition = [
        DFA.unpack(u"\1\3\6\uffff\1\1\1\3\1\uffff\1\3\6\uffff\1\2\2\uffff"
        u"\1\3\2\uffff\1\3\1\2\1\3\4\uffff\2\3\1\uffff\6\3\1\uffff\1\3\2"
        u"\uffff\1\3"),
        DFA.unpack(u"\1\3\6\uffff\1\1\1\3\1\uffff\1\3\6\uffff\1\2\2\uffff"
        u"\1\3\2\uffff\1\3\1\uffff\1\3\4\uffff\2\3\1\uffff\6\3\1\uffff\1"
        u"\3\2\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass


    # lookup tables for DFA #20

    DFA20_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA20_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA20_min = DFA.unpack(
        u"\1\22\1\uffff\1\32\7\uffff"
        )

    DFA20_max = DFA.unpack(
        u"\1\75\1\uffff\1\64\7\uffff"
        )

    DFA20_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2\1\3\1\4\1\5\1\6\1\7\1\10"
        )

    DFA20_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA20_transition = [
        DFA.unpack(u"\1\1\7\uffff\1\1\1\uffff\1\2\11\uffff\1\4\2\uffff\1"
        u"\4\1\uffff\1\1\4\uffff\1\4\1\3\1\uffff\1\6\1\10\3\1\1\5\1\uffff"
        u"\1\11\2\uffff\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\1\1\uffff\1\2\16\uffff\1\1\10\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #20

    class DFA20(DFA):
        pass


    # lookup tables for DFA #37

    DFA37_eot = DFA.unpack(
        u"\32\uffff"
        )

    DFA37_eof = DFA.unpack(
        u"\32\uffff"
        )

    DFA37_min = DFA.unpack(
        u"\1\22\1\uffff\1\45\1\5\1\uffff\1\5\1\57\2\44\1\5\1\46\1\57\2\44"
        u"\1\5\1\46\1\5\1\57\2\44\1\5\1\57\2\44\2\5"
        )

    DFA37_max = DFA.unpack(
        u"\1\75\1\uffff\1\60\1\54\1\uffff\1\54\1\57\2\54\1\32\1\60\1\57\2"
        u"\54\1\32\1\60\1\6\1\57\2\54\1\6\1\57\2\54\2\6"
        )

    DFA37_accept = DFA.unpack(
        u"\1\uffff\1\2\2\uffff\1\1\25\uffff"
        )

    DFA37_special = DFA.unpack(
        u"\32\uffff"
        )

            
    DFA37_transition = [
        DFA.unpack(u"\1\4\6\uffff\1\4\1\2\1\uffff\1\4\11\uffff\1\4\2\uffff"
        u"\1\4\1\1\1\3\4\uffff\2\4\1\uffff\6\4\1\uffff\1\4\2\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\4\4\uffff\1\5\2\uffff\1\4\1\1\1\4"),
        DFA.unpack(u"\1\7\1\10\23\uffff\1\6\11\uffff\1\11\7\uffff\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\14\1\15\23\uffff\1\13\11\uffff\1\16\7\uffff\1\17"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\1\11\7\uffff\1\12"),
        DFA.unpack(u"\1\11\7\uffff\1\12"),
        DFA.unpack(u"\1\22\1\23\23\uffff\1\21"),
        DFA.unpack(u"\1\4\10\uffff\1\1\1\4"),
        DFA.unpack(u"\1\24"),
        DFA.unpack(u"\1\16\7\uffff\1\17"),
        DFA.unpack(u"\1\16\7\uffff\1\17"),
        DFA.unpack(u"\1\26\1\27\23\uffff\1\25"),
        DFA.unpack(u"\1\4\10\uffff\1\1\1\4"),
        DFA.unpack(u"\1\7\1\10"),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u"\1\11\7\uffff\1\12"),
        DFA.unpack(u"\1\11\7\uffff\1\12"),
        DFA.unpack(u"\1\14\1\15"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\16\7\uffff\1\17"),
        DFA.unpack(u"\1\16\7\uffff\1\17"),
        DFA.unpack(u"\1\22\1\23"),
        DFA.unpack(u"\1\26\1\27")
    ]

    # class definition for DFA #37

    class DFA37(DFA):
        pass


 

    FOLLOW_ANNOTATION_in_description257 = frozenset([25, 34])
    FOLLOW_importProtocolStatement_in_description264 = frozenset([25, 34, 35])
    FOLLOW_importTypeStatement_in_description268 = frozenset([25, 34, 35])
    FOLLOW_ANNOTATION_in_description277 = frozenset([25, 35])
    FOLLOW_protocolDef_in_description282 = frozenset([1])
    FOLLOW_34_in_importProtocolStatement293 = frozenset([35])
    FOLLOW_35_in_importProtocolStatement295 = frozenset([26])
    FOLLOW_importProtocolDef_in_importProtocolStatement297 = frozenset([36, 37])
    FOLLOW_36_in_importProtocolStatement301 = frozenset([26])
    FOLLOW_importProtocolDef_in_importProtocolStatement304 = frozenset([36, 37])
    FOLLOW_37_in_importProtocolStatement309 = frozenset([1])
    FOLLOW_ID_in_importProtocolDef318 = frozenset([38])
    FOLLOW_38_in_importProtocolDef320 = frozenset([27])
    FOLLOW_StringLiteral_in_importProtocolDef323 = frozenset([1])
    FOLLOW_34_in_importTypeStatement336 = frozenset([26, 27])
    FOLLOW_simpleName_in_importTypeStatement340 = frozenset([26, 27])
    FOLLOW_importTypeDef_in_importTypeStatement345 = frozenset([36, 37, 38])
    FOLLOW_36_in_importTypeStatement349 = frozenset([26, 27])
    FOLLOW_importTypeDef_in_importTypeStatement352 = frozenset([36, 37, 38])
    FOLLOW_38_in_importTypeStatement359 = frozenset([27])
    FOLLOW_StringLiteral_in_importTypeStatement362 = frozenset([37])
    FOLLOW_37_in_importTypeStatement367 = frozenset([1])
    FOLLOW_dataTypeDef_in_importTypeDef378 = frozenset([39])
    FOLLOW_39_in_importTypeDef380 = frozenset([26])
    FOLLOW_ID_in_importTypeDef386 = frozenset([1])
    FOLLOW_StringLiteral_in_dataTypeDef394 = frozenset([1])
    FOLLOW_ID_in_simpleName402 = frozenset([1])
    FOLLOW_35_in_protocolDef410 = frozenset([26])
    FOLLOW_protocolName_in_protocolDef412 = frozenset([40, 41, 43])
    FOLLOW_40_in_protocolDef416 = frozenset([26])
    FOLLOW_roleName_in_protocolDef418 = frozenset([41, 43])
    FOLLOW_parameterDefs_in_protocolDef425 = frozenset([41])
    FOLLOW_41_in_protocolDef430 = frozenset([18, 25, 26, 28, 38, 41, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_protocolBlockDef_in_protocolDef432 = frozenset([25, 35, 42])
    FOLLOW_ANNOTATION_in_protocolDef438 = frozenset([25, 35])
    FOLLOW_protocolDef_in_protocolDef443 = frozenset([25, 35, 42])
    FOLLOW_42_in_protocolDef448 = frozenset([1])
    FOLLOW_ID_in_protocolName476 = frozenset([1])
    FOLLOW_43_in_parameterDefs484 = frozenset([45])
    FOLLOW_roleparameDef_in_parameterDefs486 = frozenset([36, 44])
    FOLLOW_36_in_parameterDefs490 = frozenset([45])
    FOLLOW_roleparameDef_in_parameterDefs492 = frozenset([36, 44])
    FOLLOW_44_in_parameterDefs497 = frozenset([1])
    FOLLOW_45_in_roleparameDef513 = frozenset([26])
    FOLLOW_simpleName_in_roleparameDef515 = frozenset([1])
    FOLLOW_activityListDef_in_protocolBlockDef526 = frozenset([1])
    FOLLOW_41_in_blockDef537 = frozenset([18, 25, 26, 28, 38, 41, 42, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_activityListDef_in_blockDef539 = frozenset([42])
    FOLLOW_42_in_blockDef541 = frozenset([1])
    FOLLOW_ASSERTION_in_assertDef563 = frozenset([1, 28])
    FOLLOW_ANNOTATION_in_activityListDef585 = frozenset([18, 25, 26, 28, 38, 41, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_activityDef_in_activityListDef590 = frozenset([1, 18, 25, 26, 28, 38, 41, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_INT_in_primitivetype606 = frozenset([1])
    FOLLOW_STRING_in_primitivetype612 = frozenset([1])
    FOLLOW_introducesDef_in_activityDef625 = frozenset([37])
    FOLLOW_interactionDef_in_activityDef629 = frozenset([37])
    FOLLOW_inlineDef_in_activityDef633 = frozenset([37])
    FOLLOW_runDef_in_activityDef637 = frozenset([37])
    FOLLOW_recursionDef_in_activityDef641 = frozenset([37])
    FOLLOW_endDef_in_activityDef645 = frozenset([37])
    FOLLOW_RECLABEL_in_activityDef649 = frozenset([37])
    FOLLOW_37_in_activityDef653 = frozenset([1])
    FOLLOW_choiceDef_in_activityDef662 = frozenset([1])
    FOLLOW_directedChoiceDef_in_activityDef666 = frozenset([1])
    FOLLOW_parallelDef_in_activityDef670 = frozenset([1])
    FOLLOW_repeatDef_in_activityDef674 = frozenset([1])
    FOLLOW_unorderedDef_in_activityDef678 = frozenset([1])
    FOLLOW_recBlockDef_in_activityDef685 = frozenset([1])
    FOLLOW_globalEscapeDef_in_activityDef689 = frozenset([1])
    FOLLOW_roleDef_in_introducesDef697 = frozenset([46])
    FOLLOW_46_in_introducesDef699 = frozenset([26])
    FOLLOW_roleDef_in_introducesDef701 = frozenset([1, 36])
    FOLLOW_36_in_introducesDef705 = frozenset([26])
    FOLLOW_roleDef_in_introducesDef707 = frozenset([1, 36])
    FOLLOW_ID_in_roleDef718 = frozenset([1])
    FOLLOW_ID_in_roleName729 = frozenset([1])
    FOLLOW_ID_in_typeReferenceDef740 = frozenset([1])
    FOLLOW_typeReferenceDef_in_interactionSignatureDef751 = frozenset([1, 43])
    FOLLOW_43_in_interactionSignatureDef754 = frozenset([5, 6, 26, 36, 44])
    FOLLOW_valueDecl_in_interactionSignatureDef758 = frozenset([36, 44])
    FOLLOW_36_in_interactionSignatureDef764 = frozenset([5, 6, 26])
    FOLLOW_valueDecl_in_interactionSignatureDef766 = frozenset([36, 44])
    FOLLOW_44_in_interactionSignatureDef770 = frozenset([1])
    FOLLOW_43_in_interactionSignatureDef794 = frozenset([5, 6, 26, 36, 44])
    FOLLOW_valueDecl_in_interactionSignatureDef798 = frozenset([36, 44])
    FOLLOW_36_in_interactionSignatureDef804 = frozenset([5, 6, 26])
    FOLLOW_valueDecl_in_interactionSignatureDef806 = frozenset([36, 44])
    FOLLOW_44_in_interactionSignatureDef810 = frozenset([1])
    FOLLOW_ID_in_valueDecl832 = frozenset([47])
    FOLLOW_47_in_valueDecl834 = frozenset([5, 6, 26])
    FOLLOW_primitivetype_in_valueDecl840 = frozenset([1])
    FOLLOW_valueDecl_in_firstValueDecl849 = frozenset([1])
    FOLLOW_assertDef_in_interactionDef866 = frozenset([26, 28, 43])
    FOLLOW_interactionSignatureDef_in_interactionDef870 = frozenset([38, 48])
    FOLLOW_38_in_interactionDef884 = frozenset([26])
    FOLLOW_roleName_in_interactionDef889 = frozenset([1])
    FOLLOW_48_in_interactionDef915 = frozenset([26])
    FOLLOW_roleName_in_interactionDef917 = frozenset([1])
    FOLLOW_49_in_choiceDef939 = frozenset([40, 41])
    FOLLOW_40_in_choiceDef943 = frozenset([26])
    FOLLOW_roleName_in_choiceDef945 = frozenset([40, 41])
    FOLLOW_blockDef_in_choiceDef950 = frozenset([1, 50])
    FOLLOW_50_in_choiceDef954 = frozenset([40, 41])
    FOLLOW_blockDef_in_choiceDef956 = frozenset([1, 50])
    FOLLOW_38_in_directedChoiceDef977 = frozenset([26])
    FOLLOW_roleName_in_directedChoiceDef979 = frozenset([41, 48])
    FOLLOW_48_in_directedChoiceDef986 = frozenset([26])
    FOLLOW_roleName_in_directedChoiceDef988 = frozenset([36, 41])
    FOLLOW_36_in_directedChoiceDef992 = frozenset([26])
    FOLLOW_roleName_in_directedChoiceDef995 = frozenset([36, 41])
    FOLLOW_41_in_directedChoiceDef1003 = frozenset([26, 28, 43])
    FOLLOW_onMessageDef_in_directedChoiceDef1007 = frozenset([26, 28, 42, 43])
    FOLLOW_42_in_directedChoiceDef1012 = frozenset([1])
    FOLLOW_interactionSignatureDef_in_onMessageDef1019 = frozenset([47])
    FOLLOW_47_in_onMessageDef1021 = frozenset([18, 25, 26, 28, 38, 41, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_activityList_in_onMessageDef1023 = frozenset([1])
    FOLLOW_ANNOTATION_in_activityList1036 = frozenset([18, 25, 26, 28, 38, 41, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_activityDef_in_activityList1041 = frozenset([1, 18, 25, 26, 28, 38, 41, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_51_in_repeatDef1051 = frozenset([40, 41])
    FOLLOW_40_in_repeatDef1055 = frozenset([26])
    FOLLOW_roleName_in_repeatDef1057 = frozenset([36, 40, 41])
    FOLLOW_36_in_repeatDef1061 = frozenset([26])
    FOLLOW_roleName_in_repeatDef1063 = frozenset([36, 40, 41])
    FOLLOW_blockDef_in_repeatDef1071 = frozenset([1])
    FOLLOW_assertDef_in_recBlockDef1087 = frozenset([52])
    FOLLOW_52_in_recBlockDef1089 = frozenset([26])
    FOLLOW_labelName_in_recBlockDef1091 = frozenset([40, 41])
    FOLLOW_blockDef_in_recBlockDef1093 = frozenset([1])
    FOLLOW_ID_in_labelName1110 = frozenset([1])
    FOLLOW_labelName_in_recursionDef1122 = frozenset([1])
    FOLLOW_53_in_endDef1138 = frozenset([1])
    FOLLOW_54_in_runDef1148 = frozenset([26])
    FOLLOW_protocolRefDef_in_runDef1151 = frozenset([38, 43])
    FOLLOW_43_in_runDef1155 = frozenset([26])
    FOLLOW_parameter_in_runDef1158 = frozenset([36, 44])
    FOLLOW_36_in_runDef1162 = frozenset([26])
    FOLLOW_parameter_in_runDef1165 = frozenset([36, 44])
    FOLLOW_44_in_runDef1170 = frozenset([38])
    FOLLOW_38_in_runDef1176 = frozenset([26])
    FOLLOW_roleName_in_runDef1178 = frozenset([1])
    FOLLOW_ID_in_protocolRefDef1186 = frozenset([1, 40])
    FOLLOW_40_in_protocolRefDef1190 = frozenset([26])
    FOLLOW_roleName_in_protocolRefDef1192 = frozenset([1])
    FOLLOW_ID_in_declarationName1203 = frozenset([1])
    FOLLOW_declarationName_in_parameter1211 = frozenset([1])
    FOLLOW_55_in_inlineDef1220 = frozenset([26])
    FOLLOW_protocolRefDef_in_inlineDef1223 = frozenset([1, 43])
    FOLLOW_43_in_inlineDef1227 = frozenset([26])
    FOLLOW_parameter_in_inlineDef1230 = frozenset([36, 44])
    FOLLOW_36_in_inlineDef1234 = frozenset([26])
    FOLLOW_parameter_in_inlineDef1237 = frozenset([36, 44])
    FOLLOW_44_in_inlineDef1242 = frozenset([1])
    FOLLOW_56_in_parallelDef1254 = frozenset([40, 41])
    FOLLOW_blockDef_in_parallelDef1256 = frozenset([1, 57])
    FOLLOW_57_in_parallelDef1260 = frozenset([40, 41])
    FOLLOW_blockDef_in_parallelDef1262 = frozenset([1, 57])
    FOLLOW_58_in_doBlockDef1282 = frozenset([41])
    FOLLOW_41_in_doBlockDef1284 = frozenset([18, 25, 26, 28, 38, 41, 42, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_activityListDef_in_doBlockDef1286 = frozenset([42])
    FOLLOW_42_in_doBlockDef1289 = frozenset([1])
    FOLLOW_59_in_interruptDef1307 = frozenset([60])
    FOLLOW_60_in_interruptDef1309 = frozenset([26])
    FOLLOW_roleName_in_interruptDef1311 = frozenset([41])
    FOLLOW_41_in_interruptDef1313 = frozenset([18, 25, 26, 28, 38, 41, 42, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_activityListDef_in_interruptDef1315 = frozenset([42])
    FOLLOW_42_in_interruptDef1317 = frozenset([1])
    FOLLOW_doBlockDef_in_globalEscapeDef1335 = frozenset([59])
    FOLLOW_interruptDef_in_globalEscapeDef1338 = frozenset([1])
    FOLLOW_61_in_unorderedDef1355 = frozenset([41])
    FOLLOW_41_in_unorderedDef1357 = frozenset([18, 25, 26, 28, 38, 41, 42, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_ANNOTATION_in_unorderedDef1363 = frozenset([18, 25, 26, 28, 38, 41, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_activityDef_in_unorderedDef1368 = frozenset([18, 25, 26, 28, 38, 41, 42, 43, 48, 49, 51, 52, 53, 54, 55, 56, 58, 61])
    FOLLOW_42_in_unorderedDef1373 = frozenset([1])
    FOLLOW_term_in_expr1398 = frozenset([1, 7, 8])
    FOLLOW_set_in_expr1402 = frozenset([29])
    FOLLOW_term_in_expr1413 = frozenset([1, 7, 8])
    FOLLOW_factor_in_term1425 = frozenset([1, 9, 10])
    FOLLOW_set_in_term1429 = frozenset([29])
    FOLLOW_factor_in_term1439 = frozenset([1, 9, 10])
    FOLLOW_NUMBER_in_factor1451 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("MonitorLexer", MonitorParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
