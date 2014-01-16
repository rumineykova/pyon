# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 Generate/Monitor.g 2014-01-16 13:57:56

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
RESV=12
ANNOTATION=25
ASSERTION=28
PARALLEL=19
T__61=61
ID=26
T__60=60
EOF=-1
PROTOCOL=20
TYPE=14
T__55=55
INTERACTION=4
T__56=56
ML_COMMENT=32
T__57=57
T__58=58
ROLES=24
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
VALUE=15
MULT=9
MINUS=8
ASSERT=21
UNORDERED=17
EMPTY=23
StringLiteral=27
T__34=34
GLOBAL_ESCAPE=22
T__35=35
T__36=36
T__37=37
T__38=38
T__39=39
BRANCH=16
DIV=10
STRING=6


class MonitorLexer(Lexer):

    grammarFileName = "Generate/Monitor.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(MonitorLexer, self).__init__(input, state)


        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )






    # $ANTLR start "INTERACTION"
    def mINTERACTION(self, ):

        try:
            _type = INTERACTION
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:7:13: ( 'interaction' )
            # Generate/Monitor.g:7:15: 'interaction'
            pass 
            self.match("interaction")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTERACTION"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:8:5: ( 'int' )
            # Generate/Monitor.g:8:7: 'int'
            pass 
            self.match("int")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:9:8: ( 'string' )
            # Generate/Monitor.g:9:10: 'string'
            pass 
            self.match("string")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:10:6: ( '+' )
            # Generate/Monitor.g:10:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:11:7: ( '-' )
            # Generate/Monitor.g:11:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "MULT"
    def mMULT(self, ):

        try:
            _type = MULT
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:12:6: ( '*' )
            # Generate/Monitor.g:12:8: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MULT"



    # $ANTLR start "DIV"
    def mDIV(self, ):

        try:
            _type = DIV
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:13:5: ( '/' )
            # Generate/Monitor.g:13:7: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIV"



    # $ANTLR start "FULLSTOP"
    def mFULLSTOP(self, ):

        try:
            _type = FULLSTOP
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:14:10: ( '.' )
            # Generate/Monitor.g:14:12: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FULLSTOP"



    # $ANTLR start "RESV"
    def mRESV(self, ):

        try:
            _type = RESV
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:15:6: ( 'RESV' )
            # Generate/Monitor.g:15:8: 'RESV'
            pass 
            self.match("RESV")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RESV"



    # $ANTLR start "SEND"
    def mSEND(self, ):

        try:
            _type = SEND
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:16:6: ( 'SEND' )
            # Generate/Monitor.g:16:8: 'SEND'
            pass 
            self.match("SEND")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEND"



    # $ANTLR start "TYPE"
    def mTYPE(self, ):

        try:
            _type = TYPE
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:17:6: ( 'TYPE' )
            # Generate/Monitor.g:17:8: 'TYPE'
            pass 
            self.match("TYPE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TYPE"



    # $ANTLR start "VALUE"
    def mVALUE(self, ):

        try:
            _type = VALUE
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:18:7: ( 'VALUE' )
            # Generate/Monitor.g:18:9: 'VALUE'
            pass 
            self.match("VALUE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VALUE"



    # $ANTLR start "BRANCH"
    def mBRANCH(self, ):

        try:
            _type = BRANCH
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:19:8: ( 'BRANCH' )
            # Generate/Monitor.g:19:10: 'BRANCH'
            pass 
            self.match("BRANCH")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BRANCH"



    # $ANTLR start "UNORDERED"
    def mUNORDERED(self, ):

        try:
            _type = UNORDERED
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:20:11: ( 'UNORDERED' )
            # Generate/Monitor.g:20:13: 'UNORDERED'
            pass 
            self.match("UNORDERED")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNORDERED"



    # $ANTLR start "RECLABEL"
    def mRECLABEL(self, ):

        try:
            _type = RECLABEL
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:21:10: ( 'RECLABEL' )
            # Generate/Monitor.g:21:12: 'RECLABEL'
            pass 
            self.match("RECLABEL")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RECLABEL"



    # $ANTLR start "PARALLEL"
    def mPARALLEL(self, ):

        try:
            _type = PARALLEL
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:22:10: ( 'PARALLEL' )
            # Generate/Monitor.g:22:12: 'PARALLEL'
            pass 
            self.match("PARALLEL")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PARALLEL"



    # $ANTLR start "PROTOCOL"
    def mPROTOCOL(self, ):

        try:
            _type = PROTOCOL
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:23:10: ( 'PROTOCOL' )
            # Generate/Monitor.g:23:12: 'PROTOCOL'
            pass 
            self.match("PROTOCOL")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PROTOCOL"



    # $ANTLR start "ASSERT"
    def mASSERT(self, ):

        try:
            _type = ASSERT
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:24:8: ( 'ASSERT' )
            # Generate/Monitor.g:24:10: 'ASSERT'
            pass 
            self.match("ASSERT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSERT"



    # $ANTLR start "GLOBAL_ESCAPE"
    def mGLOBAL_ESCAPE(self, ):

        try:
            _type = GLOBAL_ESCAPE
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:25:15: ( 'GLOBAL_ESCAPE' )
            # Generate/Monitor.g:25:17: 'GLOBAL_ESCAPE'
            pass 
            self.match("GLOBAL_ESCAPE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBAL_ESCAPE"



    # $ANTLR start "EMPTY"
    def mEMPTY(self, ):

        try:
            _type = EMPTY
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:26:7: ( 'EMPTY' )
            # Generate/Monitor.g:26:9: 'EMPTY'
            pass 
            self.match("EMPTY")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EMPTY"



    # $ANTLR start "ROLES"
    def mROLES(self, ):

        try:
            _type = ROLES
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:27:7: ( 'ROLES' )
            # Generate/Monitor.g:27:9: 'ROLES'
            pass 
            self.match("ROLES")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROLES"



    # $ANTLR start "T__34"
    def mT__34(self, ):

        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:28:7: ( 'import' )
            # Generate/Monitor.g:28:9: 'import'
            pass 
            self.match("import")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__34"



    # $ANTLR start "T__35"
    def mT__35(self, ):

        try:
            _type = T__35
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:29:7: ( 'protocol' )
            # Generate/Monitor.g:29:9: 'protocol'
            pass 
            self.match("protocol")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__35"



    # $ANTLR start "T__36"
    def mT__36(self, ):

        try:
            _type = T__36
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:30:7: ( ',' )
            # Generate/Monitor.g:30:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__36"



    # $ANTLR start "T__37"
    def mT__37(self, ):

        try:
            _type = T__37
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:31:7: ( ';' )
            # Generate/Monitor.g:31:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__37"



    # $ANTLR start "T__38"
    def mT__38(self, ):

        try:
            _type = T__38
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:32:7: ( 'from' )
            # Generate/Monitor.g:32:9: 'from'
            pass 
            self.match("from")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__38"



    # $ANTLR start "T__39"
    def mT__39(self, ):

        try:
            _type = T__39
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:33:7: ( 'as' )
            # Generate/Monitor.g:33:9: 'as'
            pass 
            self.match("as")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__39"



    # $ANTLR start "T__40"
    def mT__40(self, ):

        try:
            _type = T__40
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:34:7: ( 'at' )
            # Generate/Monitor.g:34:9: 'at'
            pass 
            self.match("at")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__40"



    # $ANTLR start "T__41"
    def mT__41(self, ):

        try:
            _type = T__41
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:35:7: ( '{' )
            # Generate/Monitor.g:35:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__41"



    # $ANTLR start "T__42"
    def mT__42(self, ):

        try:
            _type = T__42
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:36:7: ( '}' )
            # Generate/Monitor.g:36:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__42"



    # $ANTLR start "T__43"
    def mT__43(self, ):

        try:
            _type = T__43
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:37:7: ( '(' )
            # Generate/Monitor.g:37:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__43"



    # $ANTLR start "T__44"
    def mT__44(self, ):

        try:
            _type = T__44
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:38:7: ( ')' )
            # Generate/Monitor.g:38:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__44"



    # $ANTLR start "T__45"
    def mT__45(self, ):

        try:
            _type = T__45
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:39:7: ( 'role' )
            # Generate/Monitor.g:39:9: 'role'
            pass 
            self.match("role")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__45"



    # $ANTLR start "T__46"
    def mT__46(self, ):

        try:
            _type = T__46
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:40:7: ( 'introduces' )
            # Generate/Monitor.g:40:9: 'introduces'
            pass 
            self.match("introduces")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__46"



    # $ANTLR start "T__47"
    def mT__47(self, ):

        try:
            _type = T__47
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:41:7: ( ':' )
            # Generate/Monitor.g:41:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__47"



    # $ANTLR start "T__48"
    def mT__48(self, ):

        try:
            _type = T__48
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:42:7: ( 'to' )
            # Generate/Monitor.g:42:9: 'to'
            pass 
            self.match("to")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__48"



    # $ANTLR start "T__49"
    def mT__49(self, ):

        try:
            _type = T__49
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:43:7: ( 'choice' )
            # Generate/Monitor.g:43:9: 'choice'
            pass 
            self.match("choice")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__49"



    # $ANTLR start "T__50"
    def mT__50(self, ):

        try:
            _type = T__50
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:44:7: ( 'or' )
            # Generate/Monitor.g:44:9: 'or'
            pass 
            self.match("or")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__50"



    # $ANTLR start "T__51"
    def mT__51(self, ):

        try:
            _type = T__51
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:45:7: ( 'repeat' )
            # Generate/Monitor.g:45:9: 'repeat'
            pass 
            self.match("repeat")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__51"



    # $ANTLR start "T__52"
    def mT__52(self, ):

        try:
            _type = T__52
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:46:7: ( 'rec' )
            # Generate/Monitor.g:46:9: 'rec'
            pass 
            self.match("rec")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__52"



    # $ANTLR start "T__53"
    def mT__53(self, ):

        try:
            _type = T__53
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:47:7: ( 'end' )
            # Generate/Monitor.g:47:9: 'end'
            pass 
            self.match("end")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__53"



    # $ANTLR start "T__54"
    def mT__54(self, ):

        try:
            _type = T__54
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:48:7: ( 'run' )
            # Generate/Monitor.g:48:9: 'run'
            pass 
            self.match("run")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__54"



    # $ANTLR start "T__55"
    def mT__55(self, ):

        try:
            _type = T__55
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:49:7: ( 'inline' )
            # Generate/Monitor.g:49:9: 'inline'
            pass 
            self.match("inline")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__55"



    # $ANTLR start "T__56"
    def mT__56(self, ):

        try:
            _type = T__56
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:50:7: ( 'parallel' )
            # Generate/Monitor.g:50:9: 'parallel'
            pass 
            self.match("parallel")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__56"



    # $ANTLR start "T__57"
    def mT__57(self, ):

        try:
            _type = T__57
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:51:7: ( 'and' )
            # Generate/Monitor.g:51:9: 'and'
            pass 
            self.match("and")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__57"



    # $ANTLR start "T__58"
    def mT__58(self, ):

        try:
            _type = T__58
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:52:7: ( 'do' )
            # Generate/Monitor.g:52:9: 'do'
            pass 
            self.match("do")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__58"



    # $ANTLR start "T__59"
    def mT__59(self, ):

        try:
            _type = T__59
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:53:7: ( 'interrupt' )
            # Generate/Monitor.g:53:9: 'interrupt'
            pass 
            self.match("interrupt")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__59"



    # $ANTLR start "T__60"
    def mT__60(self, ):

        try:
            _type = T__60
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:54:7: ( 'by' )
            # Generate/Monitor.g:54:9: 'by'
            pass 
            self.match("by")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__60"



    # $ANTLR start "T__61"
    def mT__61(self, ):

        try:
            _type = T__61
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:55:7: ( 'unordered' )
            # Generate/Monitor.g:55:9: 'unordered'
            pass 
            self.match("unordered")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__61"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:157:4: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # Generate/Monitor.g:157:6: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # Generate/Monitor.g:157:29: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # Generate/Monitor.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):

        try:
            _type = NUMBER
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:159:8: ( ( DIGIT )+ )
            # Generate/Monitor.g:159:10: ( DIGIT )+
            pass 
            # Generate/Monitor.g:159:10: ( DIGIT )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # Generate/Monitor.g:159:11: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUMBER"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:161:12: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # Generate/Monitor.g:161:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # Generate/Monitor.g:161:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((9 <= LA3_0 <= 10) or (12 <= LA3_0 <= 13) or LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # Generate/Monitor.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1
            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # Generate/Monitor.g:163:16: ( '0' .. '9' )
            # Generate/Monitor.g:163:18: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "ASSERTION"
    def mASSERTION(self, ):

        try:
            _type = ASSERTION
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:165:11: ( '@{' ( options {greedy=false; } : . )* '}' )
            # Generate/Monitor.g:165:13: '@{' ( options {greedy=false; } : . )* '}'
            pass 
            self.match("@{")
            # Generate/Monitor.g:165:18: ( options {greedy=false; } : . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 125) :
                    alt4 = 2
                elif ((0 <= LA4_0 <= 124) or (126 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # Generate/Monitor.g:165:45: .
                    pass 
                    self.matchAny()


                else:
                    break #loop4
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSERTION"



    # $ANTLR start "ANNOTATION"
    def mANNOTATION(self, ):

        try:
            _type = ANNOTATION
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:167:12: ( '[[' ( options {greedy=false; } : . )* ']]' )
            # Generate/Monitor.g:167:14: '[[' ( options {greedy=false; } : . )* ']]'
            pass 
            self.match("[[")
            # Generate/Monitor.g:167:19: ( options {greedy=false; } : . )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 93) :
                    LA5_1 = self.input.LA(2)

                    if (LA5_1 == 93) :
                        alt5 = 2
                    elif ((0 <= LA5_1 <= 92) or (94 <= LA5_1 <= 65535)) :
                        alt5 = 1


                elif ((0 <= LA5_0 <= 92) or (94 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # Generate/Monitor.g:167:46: .
                    pass 
                    self.matchAny()


                else:
                    break #loop5
            self.match("]]")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ANNOTATION"



    # $ANTLR start "ML_COMMENT"
    def mML_COMMENT(self, ):

        try:
            _type = ML_COMMENT
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:170:5: ( '/*' ( options {greedy=false; } : . )* '*/' )
            # Generate/Monitor.g:170:9: '/*' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match("/*")
            # Generate/Monitor.g:170:14: ( options {greedy=false; } : . )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 42) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == 47) :
                        alt6 = 2
                    elif ((0 <= LA6_1 <= 46) or (48 <= LA6_1 <= 65535)) :
                        alt6 = 1


                elif ((0 <= LA6_0 <= 41) or (43 <= LA6_0 <= 65535)) :
                    alt6 = 1


                if alt6 == 1:
                    # Generate/Monitor.g:170:41: .
                    pass 
                    self.matchAny()


                else:
                    break #loop6
            self.match("*/")
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ML_COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):

        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:173:14: ( '//' ( options {greedy=false; } : . )* '\\n' )
            # Generate/Monitor.g:173:16: '//' ( options {greedy=false; } : . )* '\\n'
            pass 
            self.match("//")
            # Generate/Monitor.g:173:21: ( options {greedy=false; } : . )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 10) :
                    alt7 = 2
                elif ((0 <= LA7_0 <= 9) or (11 <= LA7_0 <= 65535)) :
                    alt7 = 1


                if alt7 == 1:
                    # Generate/Monitor.g:173:48: .
                    pass 
                    self.matchAny()


                else:
                    break #loop7
            self.match(10)
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "StringLiteral"
    def mStringLiteral(self, ):

        try:
            _type = StringLiteral
            _channel = DEFAULT_CHANNEL

            # Generate/Monitor.g:175:14: ( '\"' (~ ( '\\\\' | '\"' ) )* '\"' )
            # Generate/Monitor.g:175:16: '\"' (~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)
            # Generate/Monitor.g:175:20: (~ ( '\\\\' | '\"' ) )*
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((0 <= LA8_0 <= 33) or (35 <= LA8_0 <= 91) or (93 <= LA8_0 <= 65535)) :
                    alt8 = 1


                if alt8 == 1:
                    # Generate/Monitor.g:175:22: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop8
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "StringLiteral"



    def mTokens(self):
        # Generate/Monitor.g:1:8: ( INTERACTION | INT | STRING | PLUS | MINUS | MULT | DIV | FULLSTOP | RESV | SEND | TYPE | VALUE | BRANCH | UNORDERED | RECLABEL | PARALLEL | PROTOCOL | ASSERT | GLOBAL_ESCAPE | EMPTY | ROLES | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | T__60 | T__61 | ID | NUMBER | WHITESPACE | ASSERTION | ANNOTATION | ML_COMMENT | LINE_COMMENT | StringLiteral )
        alt9 = 57
        alt9 = self.dfa9.predict(self.input)
        if alt9 == 1:
            # Generate/Monitor.g:1:10: INTERACTION
            pass 
            self.mINTERACTION()


        elif alt9 == 2:
            # Generate/Monitor.g:1:22: INT
            pass 
            self.mINT()


        elif alt9 == 3:
            # Generate/Monitor.g:1:26: STRING
            pass 
            self.mSTRING()


        elif alt9 == 4:
            # Generate/Monitor.g:1:33: PLUS
            pass 
            self.mPLUS()


        elif alt9 == 5:
            # Generate/Monitor.g:1:38: MINUS
            pass 
            self.mMINUS()


        elif alt9 == 6:
            # Generate/Monitor.g:1:44: MULT
            pass 
            self.mMULT()


        elif alt9 == 7:
            # Generate/Monitor.g:1:49: DIV
            pass 
            self.mDIV()


        elif alt9 == 8:
            # Generate/Monitor.g:1:53: FULLSTOP
            pass 
            self.mFULLSTOP()


        elif alt9 == 9:
            # Generate/Monitor.g:1:62: RESV
            pass 
            self.mRESV()


        elif alt9 == 10:
            # Generate/Monitor.g:1:67: SEND
            pass 
            self.mSEND()


        elif alt9 == 11:
            # Generate/Monitor.g:1:72: TYPE
            pass 
            self.mTYPE()


        elif alt9 == 12:
            # Generate/Monitor.g:1:77: VALUE
            pass 
            self.mVALUE()


        elif alt9 == 13:
            # Generate/Monitor.g:1:83: BRANCH
            pass 
            self.mBRANCH()


        elif alt9 == 14:
            # Generate/Monitor.g:1:90: UNORDERED
            pass 
            self.mUNORDERED()


        elif alt9 == 15:
            # Generate/Monitor.g:1:100: RECLABEL
            pass 
            self.mRECLABEL()


        elif alt9 == 16:
            # Generate/Monitor.g:1:109: PARALLEL
            pass 
            self.mPARALLEL()


        elif alt9 == 17:
            # Generate/Monitor.g:1:118: PROTOCOL
            pass 
            self.mPROTOCOL()


        elif alt9 == 18:
            # Generate/Monitor.g:1:127: ASSERT
            pass 
            self.mASSERT()


        elif alt9 == 19:
            # Generate/Monitor.g:1:134: GLOBAL_ESCAPE
            pass 
            self.mGLOBAL_ESCAPE()


        elif alt9 == 20:
            # Generate/Monitor.g:1:148: EMPTY
            pass 
            self.mEMPTY()


        elif alt9 == 21:
            # Generate/Monitor.g:1:154: ROLES
            pass 
            self.mROLES()


        elif alt9 == 22:
            # Generate/Monitor.g:1:160: T__34
            pass 
            self.mT__34()


        elif alt9 == 23:
            # Generate/Monitor.g:1:166: T__35
            pass 
            self.mT__35()


        elif alt9 == 24:
            # Generate/Monitor.g:1:172: T__36
            pass 
            self.mT__36()


        elif alt9 == 25:
            # Generate/Monitor.g:1:178: T__37
            pass 
            self.mT__37()


        elif alt9 == 26:
            # Generate/Monitor.g:1:184: T__38
            pass 
            self.mT__38()


        elif alt9 == 27:
            # Generate/Monitor.g:1:190: T__39
            pass 
            self.mT__39()


        elif alt9 == 28:
            # Generate/Monitor.g:1:196: T__40
            pass 
            self.mT__40()


        elif alt9 == 29:
            # Generate/Monitor.g:1:202: T__41
            pass 
            self.mT__41()


        elif alt9 == 30:
            # Generate/Monitor.g:1:208: T__42
            pass 
            self.mT__42()


        elif alt9 == 31:
            # Generate/Monitor.g:1:214: T__43
            pass 
            self.mT__43()


        elif alt9 == 32:
            # Generate/Monitor.g:1:220: T__44
            pass 
            self.mT__44()


        elif alt9 == 33:
            # Generate/Monitor.g:1:226: T__45
            pass 
            self.mT__45()


        elif alt9 == 34:
            # Generate/Monitor.g:1:232: T__46
            pass 
            self.mT__46()


        elif alt9 == 35:
            # Generate/Monitor.g:1:238: T__47
            pass 
            self.mT__47()


        elif alt9 == 36:
            # Generate/Monitor.g:1:244: T__48
            pass 
            self.mT__48()


        elif alt9 == 37:
            # Generate/Monitor.g:1:250: T__49
            pass 
            self.mT__49()


        elif alt9 == 38:
            # Generate/Monitor.g:1:256: T__50
            pass 
            self.mT__50()


        elif alt9 == 39:
            # Generate/Monitor.g:1:262: T__51
            pass 
            self.mT__51()


        elif alt9 == 40:
            # Generate/Monitor.g:1:268: T__52
            pass 
            self.mT__52()


        elif alt9 == 41:
            # Generate/Monitor.g:1:274: T__53
            pass 
            self.mT__53()


        elif alt9 == 42:
            # Generate/Monitor.g:1:280: T__54
            pass 
            self.mT__54()


        elif alt9 == 43:
            # Generate/Monitor.g:1:286: T__55
            pass 
            self.mT__55()


        elif alt9 == 44:
            # Generate/Monitor.g:1:292: T__56
            pass 
            self.mT__56()


        elif alt9 == 45:
            # Generate/Monitor.g:1:298: T__57
            pass 
            self.mT__57()


        elif alt9 == 46:
            # Generate/Monitor.g:1:304: T__58
            pass 
            self.mT__58()


        elif alt9 == 47:
            # Generate/Monitor.g:1:310: T__59
            pass 
            self.mT__59()


        elif alt9 == 48:
            # Generate/Monitor.g:1:316: T__60
            pass 
            self.mT__60()


        elif alt9 == 49:
            # Generate/Monitor.g:1:322: T__61
            pass 
            self.mT__61()


        elif alt9 == 50:
            # Generate/Monitor.g:1:328: ID
            pass 
            self.mID()


        elif alt9 == 51:
            # Generate/Monitor.g:1:331: NUMBER
            pass 
            self.mNUMBER()


        elif alt9 == 52:
            # Generate/Monitor.g:1:338: WHITESPACE
            pass 
            self.mWHITESPACE()


        elif alt9 == 53:
            # Generate/Monitor.g:1:349: ASSERTION
            pass 
            self.mASSERTION()


        elif alt9 == 54:
            # Generate/Monitor.g:1:359: ANNOTATION
            pass 
            self.mANNOTATION()


        elif alt9 == 55:
            # Generate/Monitor.g:1:370: ML_COMMENT
            pass 
            self.mML_COMMENT()


        elif alt9 == 56:
            # Generate/Monitor.g:1:381: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt9 == 57:
            # Generate/Monitor.g:1:394: StringLiteral
            pass 
            self.mStringLiteral()







    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\1\uffff\2\44\3\uffff\1\57\1\uffff\13\44\2\uffff\2\44\4\uffff\1"
        u"\44\1\uffff\7\44\6\uffff\3\44\3\uffff\17\44\1\140\1\141\4\44\1"
        u"\147\1\44\1\151\1\44\1\153\1\154\1\44\1\160\23\44\2\uffff\1\u0084"
        u"\2\44\1\u0087\1\u0088\1\uffff\1\44\1\uffff\1\u008a\2\uffff\3\44"
        u"\1\uffff\3\44\1\u0091\2\44\1\u0094\1\u0095\12\44\1\u00a0\1\uffff"
        u"\1\u00a1\1\44\2\uffff\1\44\1\uffff\6\44\1\uffff\1\44\1\u00ac\2"
        u"\uffff\1\u00ad\6\44\1\u00b4\2\44\2\uffff\6\44\1\u00bd\1\u00be\1"
        u"\u00bf\1\44\2\uffff\1\u00c1\3\44\1\u00c5\1\44\1\uffff\2\44\1\u00c9"
        u"\1\u00ca\4\44\3\uffff\1\44\1\uffff\3\44\1\uffff\3\44\2\uffff\4"
        u"\44\1\u00da\1\44\1\u00dc\1\u00dd\1\44\1\u00df\1\u00e0\2\44\1\u00e3"
        u"\1\44\1\uffff\1\u00e5\2\uffff\1\44\2\uffff\1\u00e7\1\44\1\uffff"
        u"\1\u00e9\1\uffff\1\44\1\uffff\1\u00eb\1\uffff\1\44\1\uffff\1\44"
        u"\1\u00ee\1\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\u00ef\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\11\1\155\1\164\3\uffff\1\52\1\uffff\2\105\1\131\1\101\1\122"
        u"\1\116\1\101\1\123\1\114\1\115\1\141\2\uffff\1\162\1\156\4\uffff"
        u"\1\145\1\uffff\1\157\1\150\1\162\1\156\1\157\1\171\1\156\6\uffff"
        u"\1\154\1\160\1\162\3\uffff\1\103\1\114\1\116\1\120\1\114\1\101"
        u"\1\117\1\122\1\117\1\123\1\117\1\120\1\157\1\162\1\157\2\60\1\144"
        u"\1\154\1\143\1\156\1\60\1\157\1\60\1\144\2\60\1\157\1\60\1\151"
        u"\1\157\1\151\1\126\1\114\1\105\1\104\1\105\1\125\1\116\1\122\1"
        u"\101\1\124\1\105\1\102\1\124\1\164\1\141\1\155\2\uffff\1\60\2\145"
        u"\2\60\1\uffff\1\151\1\uffff\1\60\2\uffff\2\162\1\157\1\uffff\1"
        u"\156\1\162\1\156\1\60\1\101\1\123\2\60\1\105\1\103\1\104\1\114"
        u"\1\117\1\122\1\101\1\131\1\157\1\154\1\60\1\uffff\1\60\1\141\2"
        u"\uffff\1\143\1\uffff\1\144\1\141\1\144\1\145\1\164\1\147\1\uffff"
        u"\1\102\1\60\2\uffff\1\60\1\110\1\105\1\114\1\103\1\124\1\114\1"
        u"\60\1\143\1\154\2\uffff\1\164\2\145\1\143\2\165\3\60\1\105\2\uffff"
        u"\1\60\1\122\1\105\1\117\1\60\1\137\1\uffff\1\157\1\145\2\60\1\162"
        u"\1\164\1\160\1\143\3\uffff\1\114\1\uffff\1\105\2\114\1\uffff\1"
        u"\105\2\154\2\uffff\1\145\1\151\1\164\1\145\1\60\1\104\2\60\1\123"
        u"\2\60\1\144\1\157\1\60\1\163\1\uffff\1\60\2\uffff\1\103\2\uffff"
        u"\1\60\1\156\1\uffff\1\60\1\uffff\1\101\1\uffff\1\60\1\uffff\1\120"
        u"\1\uffff\1\105\1\60\1\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\1\175\1\156\1\164\3\uffff\1\57\1\uffff\1\117\1\105\1\131\1\101"
        u"\1\122\1\116\1\122\1\123\1\114\1\115\1\162\2\uffff\1\162\1\164"
        u"\4\uffff\1\165\1\uffff\1\157\1\150\1\162\1\156\1\157\1\171\1\156"
        u"\6\uffff\1\164\1\160\1\162\3\uffff\1\123\1\114\1\116\1\120\1\114"
        u"\1\101\1\117\1\122\1\117\1\123\1\117\1\120\1\157\1\162\1\157\2"
        u"\172\1\144\1\154\1\160\1\156\1\172\1\157\1\172\1\144\2\172\1\157"
        u"\1\172\1\151\1\157\1\151\1\126\1\114\1\105\1\104\1\105\1\125\1"
        u"\116\1\122\1\101\1\124\1\105\1\102\1\124\1\164\1\141\1\155\2\uffff"
        u"\1\172\2\145\2\172\1\uffff\1\151\1\uffff\1\172\2\uffff\2\162\1"
        u"\157\1\uffff\1\156\1\162\1\156\1\172\1\101\1\123\2\172\1\105\1"
        u"\103\1\104\1\114\1\117\1\122\1\101\1\131\1\157\1\154\1\172\1\uffff"
        u"\1\172\1\141\2\uffff\1\143\1\uffff\1\144\1\162\1\144\1\145\1\164"
        u"\1\147\1\uffff\1\102\1\172\2\uffff\1\172\1\110\1\105\1\114\1\103"
        u"\1\124\1\114\1\172\1\143\1\154\2\uffff\1\164\2\145\1\143\2\165"
        u"\3\172\1\105\2\uffff\1\172\1\122\1\105\1\117\1\172\1\137\1\uffff"
        u"\1\157\1\145\2\172\1\162\1\164\1\160\1\143\3\uffff\1\114\1\uffff"
        u"\1\105\2\114\1\uffff\1\105\2\154\2\uffff\1\145\1\151\1\164\1\145"
        u"\1\172\1\104\2\172\1\123\2\172\1\144\1\157\1\172\1\163\1\uffff"
        u"\1\172\2\uffff\1\103\2\uffff\1\172\1\156\1\uffff\1\172\1\uffff"
        u"\1\101\1\uffff\1\172\1\uffff\1\120\1\uffff\1\105\1\172\1\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\3\uffff\1\4\1\5\1\6\1\uffff\1\10\13\uffff\1\30\1\31\2\uffff\1"
        u"\35\1\36\1\37\1\40\1\uffff\1\43\7\uffff\1\62\1\63\1\64\1\65\1\66"
        u"\1\71\3\uffff\1\67\1\70\1\7\60\uffff\1\33\1\34\5\uffff\1\44\1\uffff"
        u"\1\46\1\uffff\1\56\1\60\3\uffff\1\2\23\uffff\1\55\2\uffff\1\50"
        u"\1\52\1\uffff\1\51\6\uffff\1\11\2\uffff\1\12\1\13\12\uffff\1\32"
        u"\1\41\12\uffff\1\25\1\14\6\uffff\1\24\10\uffff\1\53\1\26\1\3\1"
        u"\uffff\1\15\3\uffff\1\22\3\uffff\1\47\1\45\17\uffff\1\17\1\uffff"
        u"\1\20\1\21\1\uffff\1\27\1\54\2\uffff\1\57\1\uffff\1\16\1\uffff"
        u"\1\61\1\uffff\1\42\1\uffff\1\1\2\uffff\1\23"
        )

    DFA9_special = DFA.unpack(
        u"\u00ef\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\2\46\1\uffff\2\46\22\uffff\1\46\1\uffff\1\51\5\uffff"
        u"\1\31\1\32\1\5\1\3\1\23\1\4\1\7\1\6\12\45\1\34\1\24\4\uffff\1\47"
        u"\1\17\1\14\2\44\1\21\1\44\1\20\10\44\1\16\1\44\1\10\1\11\1\12\1"
        u"\15\1\13\4\44\1\50\3\uffff\1\44\1\uffff\1\26\1\42\1\36\1\41\1\40"
        u"\1\25\2\44\1\1\5\44\1\37\1\22\1\44\1\33\1\2\1\35\1\43\5\44\1\27"
        u"\1\uffff\1\30"),
        DFA.unpack(u"\1\53\1\52"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\55\4\uffff\1\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\60\11\uffff\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67\20\uffff\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\75\20\uffff\1\74"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\101\4\uffff\1\77\1\100"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\103\11\uffff\1\102\5\uffff\1\104"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\113"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\115\7\uffff\1\114"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\121\17\uffff\1\120"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\1\125"),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u"\1\145\14\uffff\1\144"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\4\44\1\156"
        u"\14\44\1\157\10\44"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u"\1\164"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\1\166"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\172"),
        DFA.unpack(u"\1\173"),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\1\177"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u"\1\u008c"),
        DFA.unpack(u"\1\u008d"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\1\u0090"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u0092"),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u0096"),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u"\1\u0099"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u"\1\u009b"),
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u"\1\u009d"),
        DFA.unpack(u"\1\u009e"),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u"\1\u00a5\20\uffff\1\u00a6"),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u"\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ab"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\1\u00b0"),
        DFA.unpack(u"\1\u00b1"),
        DFA.unpack(u"\1\u00b2"),
        DFA.unpack(u"\1\u00b3"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00b7"),
        DFA.unpack(u"\1\u00b8"),
        DFA.unpack(u"\1\u00b9"),
        DFA.unpack(u"\1\u00ba"),
        DFA.unpack(u"\1\u00bb"),
        DFA.unpack(u"\1\u00bc"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00c0"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00c2"),
        DFA.unpack(u"\1\u00c3"),
        DFA.unpack(u"\1\u00c4"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00c6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00c7"),
        DFA.unpack(u"\1\u00c8"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00cb"),
        DFA.unpack(u"\1\u00cc"),
        DFA.unpack(u"\1\u00cd"),
        DFA.unpack(u"\1\u00ce"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00cf"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d0"),
        DFA.unpack(u"\1\u00d1"),
        DFA.unpack(u"\1\u00d2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d3"),
        DFA.unpack(u"\1\u00d4"),
        DFA.unpack(u"\1\u00d5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d6"),
        DFA.unpack(u"\1\u00d7"),
        DFA.unpack(u"\1\u00d8"),
        DFA.unpack(u"\1\u00d9"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00db"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00de"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00e1"),
        DFA.unpack(u"\1\u00e2"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00e4"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00e8"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ea"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ec"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ed"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(MonitorLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
