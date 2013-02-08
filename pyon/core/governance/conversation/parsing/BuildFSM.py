# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 BuildFSM.g 2013-01-16 03:06:08

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset
        
from pyon.core.governance.conversation.core.fsm import FSM
from pyon.core.governance.conversation.core.fsm import ExceptionFSM
from pyon.core.governance.conversation.core.transition import TransitionFactory
from pyon.core.governance.conversation.core.local_type import LocalType
from pyon.core.governance.conversation.extensions.simple_logic import *
import pyon
import os

def checkMessages(fsm):
	print "Message is checked: %s" %(fsm.input_symbol)
	

def nothing(fsm):
	print "I am invoked for empty transition"
	
def generate_ints():
	x = 1
    	while True:
        	yield x
        	x += 1

def format_state_name(state, parent_state = None):
	if parent_state is not None:
		return "%s_%s" %(parent_state, state)
	else: return state


class FSMBuilderState(object):
	def __init__(self, parent= None):
	    self.state_gen = generate_ints()
	    self.current_state = self.state_gen.next()
	    if (parent is not None): 
	    	self.parent = parent  
	    	self.fsm = FSM(format_state_name(self.current_state, self.parent.get_current_state()))
	    	self.set_interrupt_transition = self.parent.set_interrupt_transition
	    	self.top_parent = parent.top_parent
	    else: 
	    	self.fsm = FSM(self.current_state)
	    	self.top_parent = self
	    	self.set_interrupt_transition = False
	    self.start_new_par_branch = False
	    # Choice States
	    self.choice_start_state = []
	    self.choice_end_state = []
	    # Recursion states
	    self.recursions_states = {}
	    self.parent = parent  

	def format_state_name(self, state):
		if self.parent is not None:
			return "%s_%s" %(self.parent.get_current_state(), state)
		else: return state
	 
	def move_current_state(self, value = None):
		if value is None:
			self.current_state = self.state_gen.next()
		else: 
			self.current_state = value
		return self.current_state
	def get_current_state(self):
		return self.current_state
		
	def add_transition(self, transition, assertion = None, transition_context  = None):	        
	        print 'Adding transition' 
	        if assertion is not None: preprocess_assertion = Assertion.create(assertion) 
	        else: preprocess_assertion = assertion
	        
		if self.parent is not None: 
			suffix = self.parent.get_current_state()
			self.parent.fsm.add_nested_transition(transition, 
								self.parent.get_current_state(),
								format_state_name(self.get_current_state(), suffix), 
								format_state_name(self.move_current_state(), suffix),
								preprocess_assertion, 
								transition_context)
		else:
			self.fsm.add_transition(transition, 
						self.get_current_state(), 
						self.move_current_state(), 
						preprocess_assertion, 
						transition_context)
		
		# We are in interrup block and want to set the first transition that occur as interrupt_transition
	        # This is a global try catch. We assume that do wraps the whole program 
	        if self.set_interrupt_transition: 
	        	self.set_interrupt_transition = False
	        	self.fsm.add_interrupt_transition(transition, self.interrupt_start_state)
	        



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
PARALLEL=19
CATCHESKW=55
ASSERTION=58
DO=26
ABSTRACT=28
DOKW=51
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
T__83=83
SYMBOL=67
INTERRUPTIBLEKW=48
LINE_COMMENT=63
PARALLELKW=46
RECLABEL=18
NUMBER=59
WHITESPACE=61
UNDERSCORE=66
INT=5
TYPEKW=32
RECKW=44
VALUE=15
MULT=9
MINUS=8
SIGKW=37
T__84=84
ASSERT=21
ORKW=43
BYKW=50
UNORDERED=17
IMPORTKW=31
PARAMETERLIST=27
EMPTY=23
StringLiteral=64
T__71=71
GLOBAL_ESCAPE=22
T__72=72
PROTOCOLKW=33
T__70=70
BRANCH=16
LOCALKW=35
GLOBALKW=34
DIV=10
T__76=76
T__75=75
SPAWNKW=53
T__74=74
T__73=73
T__79=79
STRING=6
T__78=78
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




class BuildFSM(TreeParser):
    grammarFileName = "BuildFSM.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(BuildFSM, self).__init__(input, state, *args, **kwargs)



               
        # memory here is used only for logging and debugging purposes. 
        # We append bebugging information to memory so we can print it later. 
        self.memory = []
        self.roles = []
        self.sig_map = {}
        self.main_fsm = FSMBuilderState()
        self.parser = pyon.core.governance.conversation.parsing.base_parser.ANTLRScribbleParser()
        self.current_fsm = self.main_fsm
        self.import_path = '/home/rumi/Repository/pyon/pyon/core/governance/conversation/specs'




                


        



    # $ANTLR start "description"
    # BuildFSM.g:113:1: description : ^( PROTOCOL roleName parameterList roleList ( activityDef )+ ) ;
    def description(self, ):

        try:
            try:
                # BuildFSM.g:113:12: ( ^( PROTOCOL roleName parameterList roleList ( activityDef )+ ) )
                # BuildFSM.g:113:14: ^( PROTOCOL roleName parameterList roleList ( activityDef )+ )
                pass 
                self.match(self.input, PROTOCOL, self.FOLLOW_PROTOCOL_in_description52)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_roleName_in_description54)
                self.roleName()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_parameterList_in_description56)
                self.parameterList()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_roleList_in_description58)
                self.roleList()

                self._state.following.pop()
                # BuildFSM.g:113:57: ( activityDef )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((RESV <= LA1_0 <= SEND) or (RECLABEL <= LA1_0 <= PARALLEL) or LA1_0 == GLOBAL_ESCAPE or LA1_0 == DO or LA1_0 == CHOICEKW or LA1_0 == RECKW or LA1_0 == 78) :
                        alt1 = 1


                    if alt1 == 1:
                        # BuildFSM.g:113:57: activityDef
                        pass 
                        self._state.following.append(self.FOLLOW_activityDef_in_description60)
                        self.activityDef()

                        self._state.following.pop()


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "description"


    # $ANTLR start "parameterList"
    # BuildFSM.g:114:1: parameterList : ^( PARAMETERLIST ( sigName )+ ) ;
    def parameterList(self, ):

        try:
            try:
                # BuildFSM.g:114:14: ( ^( PARAMETERLIST ( sigName )+ ) )
                # BuildFSM.g:114:16: ^( PARAMETERLIST ( sigName )+ )
                pass 
                self.match(self.input, PARAMETERLIST, self.FOLLOW_PARAMETERLIST_in_parameterList71)

                #action start
                self.sig_map_list = []
                #action end

                self.match(self.input, DOWN, None)
                # BuildFSM.g:114:57: ( sigName )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        alt2 = 1


                    if alt2 == 1:
                        # BuildFSM.g:114:57: sigName
                        pass 
                        self._state.following.append(self.FOLLOW_sigName_in_parameterList75)
                        self.sigName()

                        self._state.following.pop()


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1
                #action start
                                                                                  
                for i, s in enumerate(self.sig_map_list):
                	self.sig_map[s] = i
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "parameterList"


    # $ANTLR start "roleList"
    # BuildFSM.g:117:1: roleList : ^( ROLES ( roleName )+ ) ;
    def roleList(self, ):

        try:
            try:
                # BuildFSM.g:117:9: ( ^( ROLES ( roleName )+ ) )
                # BuildFSM.g:117:11: ^( ROLES ( roleName )+ )
                pass 
                self.match(self.input, ROLES, self.FOLLOW_ROLES_in_roleList88)

                self.match(self.input, DOWN, None)
                # BuildFSM.g:117:19: ( roleName )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == ID) :
                        alt3 = 1


                    if alt3 == 1:
                        # BuildFSM.g:117:19: roleName
                        pass 
                        self._state.following.append(self.FOLLOW_roleName_in_roleList90)
                        self.roleName()

                        self._state.following.pop()


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "roleList"


    # $ANTLR start "activityDef"
    # BuildFSM.g:118:1: activityDef : ( ^( RESV ( ABSTRACT siglabel= ID )? (rlabel= ID )? ( ^( VALUE ( (val= ID (vtype= ( INT | STRING ) )? ) )* ) )? role= ID ( ^( ASSERT (assertion= ASSERTION )? ) ) ) | ^( SEND ( ABSTRACT siglabel= ID )? (slabel= ID )? ( ^( VALUE ( (val= ID (vtype= ( INT | STRING ) )? ) )* ) )? role= ID ( ^( ASSERT (assertion= ASSERTION )? ) ) ) | ^( 'choice' ( ^( BRANCH ( activityDef )+ ) )+ ) | ^( PARALLEL ( ^( BRANCH ( activityDef )+ ) )+ ) | ^( 'repeat' ( ^( BRANCH ( activityDef )+ ) ) ) | ^( 'rec' label= ID ( ^( BRANCH ( activityDef )+ ) ) ) | ^( 'RECLABEL' labelID= ID ) | ^( GLOBAL_ESCAPE ( ^( 'interruptible' ( ( activityDef )+ ) ) ) ( ^( 'catch' roleName ( ( activityDef )+ ) ) ) ) | ^( DO (path= ID ) ( ^( PARAMETERLIST ( (label= ID )? ( ^( VALUE ( ID )* ) ) )+ ) ) ( ^( ROLES ( ^( 'as' new_role= ID orig_role= ID ) )+ ) ) ) );
    def activityDef(self, ):

        siglabel = None
        rlabel = None
        val = None
        vtype = None
        role = None
        assertion = None
        slabel = None
        label = None
        labelID = None
        path = None
        new_role = None
        orig_role = None

        try:
            try:
                # BuildFSM.g:118:12: ( ^( RESV ( ABSTRACT siglabel= ID )? (rlabel= ID )? ( ^( VALUE ( (val= ID (vtype= ( INT | STRING ) )? ) )* ) )? role= ID ( ^( ASSERT (assertion= ASSERTION )? ) ) ) | ^( SEND ( ABSTRACT siglabel= ID )? (slabel= ID )? ( ^( VALUE ( (val= ID (vtype= ( INT | STRING ) )? ) )* ) )? role= ID ( ^( ASSERT (assertion= ASSERTION )? ) ) ) | ^( 'choice' ( ^( BRANCH ( activityDef )+ ) )+ ) | ^( PARALLEL ( ^( BRANCH ( activityDef )+ ) )+ ) | ^( 'repeat' ( ^( BRANCH ( activityDef )+ ) ) ) | ^( 'rec' label= ID ( ^( BRANCH ( activityDef )+ ) ) ) | ^( 'RECLABEL' labelID= ID ) | ^( GLOBAL_ESCAPE ( ^( 'interruptible' ( ( activityDef )+ ) ) ) ( ^( 'catch' roleName ( ( activityDef )+ ) ) ) ) | ^( DO (path= ID ) ( ^( PARAMETERLIST ( (label= ID )? ( ^( VALUE ( ID )* ) ) )+ ) ) ( ^( ROLES ( ^( 'as' new_role= ID orig_role= ID ) )+ ) ) ) )
                alt28 = 9
                LA28 = self.input.LA(1)
                if LA28 == RESV:
                    alt28 = 1
                elif LA28 == SEND:
                    alt28 = 2
                elif LA28 == CHOICEKW:
                    alt28 = 3
                elif LA28 == PARALLEL:
                    alt28 = 4
                elif LA28 == 78:
                    alt28 = 5
                elif LA28 == RECKW:
                    alt28 = 6
                elif LA28 == RECLABEL:
                    alt28 = 7
                elif LA28 == GLOBAL_ESCAPE:
                    alt28 = 8
                elif LA28 == DO:
                    alt28 = 9
                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae

                if alt28 == 1:
                    # BuildFSM.g:119:2: ^( RESV ( ABSTRACT siglabel= ID )? (rlabel= ID )? ( ^( VALUE ( (val= ID (vtype= ( INT | STRING ) )? ) )* ) )? role= ID ( ^( ASSERT (assertion= ASSERTION )? ) ) )
                    pass 
                    self.match(self.input, RESV, self.FOLLOW_RESV_in_activityDef102)

                    #action start
                             
                    local_context = []
                    label = ''
                    #action end

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:122:12: ( ABSTRACT siglabel= ID )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ABSTRACT) :
                        alt4 = 1
                    if alt4 == 1:
                        # BuildFSM.g:122:13: ABSTRACT siglabel= ID
                        pass 
                        self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_activityDef118)
                        siglabel=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef124)
                        #action start
                                                            
                        sig = siglabel.text
                        if self.sig_map.has_key(sig): label = self.sig_params[self.sig_map.get(sig)]
                        else: raise ExceptionFSM('Reference to undefined label')
                        #action end



                    # BuildFSM.g:126:5: (rlabel= ID )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == ID) :
                        LA5_1 = self.input.LA(2)

                        if (LA5_1 == VALUE or LA5_1 == ID) :
                            alt5 = 1
                    if alt5 == 1:
                        # BuildFSM.g:126:6: rlabel= ID
                        pass 
                        rlabel=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef141)
                        #action start
                                          
                        if (rlabel is not None): label = rlabel.text
                        self.memory.append('before setting the label:' +  label)
                        #action end



                    # BuildFSM.g:129:5: ( ^( VALUE ( (val= ID (vtype= ( INT | STRING ) )? ) )* ) )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == VALUE) :
                        alt8 = 1
                    if alt8 == 1:
                        # BuildFSM.g:129:6: ^( VALUE ( (val= ID (vtype= ( INT | STRING ) )? ) )* )
                        pass 
                        self.match(self.input, VALUE, self.FOLLOW_VALUE_in_activityDef153)

                        if self.input.LA(1) == DOWN:
                            self.match(self.input, DOWN, None)
                            # BuildFSM.g:129:14: ( (val= ID (vtype= ( INT | STRING ) )? ) )*
                            while True: #loop7
                                alt7 = 2
                                LA7_0 = self.input.LA(1)

                                if (LA7_0 == ID) :
                                    alt7 = 1


                                if alt7 == 1:
                                    # BuildFSM.g:129:15: (val= ID (vtype= ( INT | STRING ) )? )
                                    pass 
                                    # BuildFSM.g:129:15: (val= ID (vtype= ( INT | STRING ) )? )
                                    # BuildFSM.g:129:16: val= ID (vtype= ( INT | STRING ) )?
                                    pass 
                                    val=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef159)
                                    # BuildFSM.g:129:28: (vtype= ( INT | STRING ) )?
                                    alt6 = 2
                                    LA6_0 = self.input.LA(1)

                                    if ((INT <= LA6_0 <= STRING)) :
                                        alt6 = 1
                                    if alt6 == 1:
                                        # BuildFSM.g:129:28: vtype= ( INT | STRING )
                                        pass 
                                        vtype = self.input.LT(1)
                                        if (INT <= self.input.LA(1) <= STRING):
                                            self.input.consume()
                                            self._state.errorRecovery = False

                                        else:
                                            mse = MismatchedSetException(None, self.input)
                                            raise mse








                                    #action start
                                    if ((val is not None) and (vtype is not None)): local_context.append((val.text, vtype.text))
                                    #action end


                                else:
                                    break #loop7

                            self.match(self.input, UP, None)




                    role=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef185)
                    #action start
                    if not(role.text in self.roles): self.roles.append(role.text)
                    #action end
                    # BuildFSM.g:131:5: ( ^( ASSERT (assertion= ASSERTION )? ) )
                    # BuildFSM.g:131:6: ^( ASSERT (assertion= ASSERTION )? )
                    pass 
                    self.match(self.input, ASSERT, self.FOLLOW_ASSERT_in_activityDef195)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # BuildFSM.g:131:15: (assertion= ASSERTION )?
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == ASSERTION) :
                            alt9 = 1
                        if alt9 == 1:
                            # BuildFSM.g:131:16: assertion= ASSERTION
                            pass 
                            assertion=self.match(self.input, ASSERTION, self.FOLLOW_ASSERTION_in_activityDef200)




                        self.match(self.input, UP, None)





                    self.match(self.input, UP, None)
                    #action start
                      
                    self.memory.append('label is:' +  label);
                    print role.text
                    if hasattr(self,'sig_roles'): role = self.sig_roles[role.text]
                    print role
                    self.current_fsm.add_transition(TransitionFactory.create(LocalType.RESV, label, role), assertion, local_context)
                    	
                    #action end


                elif alt28 == 2:
                    # BuildFSM.g:139:3: ^( SEND ( ABSTRACT siglabel= ID )? (slabel= ID )? ( ^( VALUE ( (val= ID (vtype= ( INT | STRING ) )? ) )* ) )? role= ID ( ^( ASSERT (assertion= ASSERTION )? ) ) )
                    pass 
                    self.match(self.input, SEND, self.FOLLOW_SEND_in_activityDef213)

                    #action start
                              
                    local_context = []
                    label = ''
                    #action end

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:142:5: ( ABSTRACT siglabel= ID )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == ABSTRACT) :
                        alt10 = 1
                    if alt10 == 1:
                        # BuildFSM.g:142:6: ABSTRACT siglabel= ID
                        pass 
                        self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_activityDef222)
                        siglabel=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef228)
                        #action start
                                                     
                        sig = siglabel.text
                        if self.sig_map.has_key(sig): label = self.sig_params[self.sig_map.get(sig)]
                        else: raise ExceptionFSM('Reference to undefined label')
                        #action end



                    # BuildFSM.g:146:5: (slabel= ID )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == ID) :
                        LA11_1 = self.input.LA(2)

                        if (LA11_1 == VALUE or LA11_1 == ID) :
                            alt11 = 1
                    if alt11 == 1:
                        # BuildFSM.g:146:6: slabel= ID
                        pass 
                        slabel=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef243)
                        #action start
                                          
                        self.memory.append('send' + slabel.text)
                        if (slabel is not None): label = slabel.text
                        #action end



                    # BuildFSM.g:149:12: ( ^( VALUE ( (val= ID (vtype= ( INT | STRING ) )? ) )* ) )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == VALUE) :
                        alt14 = 1
                    if alt14 == 1:
                        # BuildFSM.g:149:13: ^( VALUE ( (val= ID (vtype= ( INT | STRING ) )? ) )* )
                        pass 
                        self.match(self.input, VALUE, self.FOLLOW_VALUE_in_activityDef262)

                        if self.input.LA(1) == DOWN:
                            self.match(self.input, DOWN, None)
                            # BuildFSM.g:149:21: ( (val= ID (vtype= ( INT | STRING ) )? ) )*
                            while True: #loop13
                                alt13 = 2
                                LA13_0 = self.input.LA(1)

                                if (LA13_0 == ID) :
                                    alt13 = 1


                                if alt13 == 1:
                                    # BuildFSM.g:149:22: (val= ID (vtype= ( INT | STRING ) )? )
                                    pass 
                                    # BuildFSM.g:149:22: (val= ID (vtype= ( INT | STRING ) )? )
                                    # BuildFSM.g:149:23: val= ID (vtype= ( INT | STRING ) )?
                                    pass 
                                    val=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef268)
                                    # BuildFSM.g:149:35: (vtype= ( INT | STRING ) )?
                                    alt12 = 2
                                    LA12_0 = self.input.LA(1)

                                    if ((INT <= LA12_0 <= STRING)) :
                                        alt12 = 1
                                    if alt12 == 1:
                                        # BuildFSM.g:149:35: vtype= ( INT | STRING )
                                        pass 
                                        vtype = self.input.LT(1)
                                        if (INT <= self.input.LA(1) <= STRING):
                                            self.input.consume()
                                            self._state.errorRecovery = False

                                        else:
                                            mse = MismatchedSetException(None, self.input)
                                            raise mse








                                    #action start
                                    if ((val is not None) and (vtype is not None)): local_context.append((val.text, vtype.text))
                                    #action end


                                else:
                                    break #loop13

                            self.match(self.input, UP, None)




                    role=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef298)
                    #action start
                                    
                    print 'Role printing...', role 
                    if not(role.text in self.roles): self.roles.append(role.text)
                    #action end
                    # BuildFSM.g:153:5: ( ^( ASSERT (assertion= ASSERTION )? ) )
                    # BuildFSM.g:153:6: ^( ASSERT (assertion= ASSERTION )? )
                    pass 
                    self.match(self.input, ASSERT, self.FOLLOW_ASSERT_in_activityDef308)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # BuildFSM.g:153:15: (assertion= ASSERTION )?
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == ASSERTION) :
                            alt15 = 1
                        if alt15 == 1:
                            # BuildFSM.g:153:16: assertion= ASSERTION
                            pass 
                            assertion=self.match(self.input, ASSERTION, self.FOLLOW_ASSERTION_in_activityDef313)




                        self.match(self.input, UP, None)





                    self.match(self.input, UP, None)
                    #action start
                    self.memory.append('In SEND assertion')
                    #action end
                    #action start
                      
                    print 'Adding transition', label
                    print role.text
                    if hasattr(self,'sig_roles'): role = self.sig_roles[role.text]
                    print role 
                    self.current_fsm.add_transition(TransitionFactory.create(LocalType.SEND, label, role), assertion, local_context)
                    	
                    #action end


                elif alt28 == 3:
                    # BuildFSM.g:162:3: ^( 'choice' ( ^( BRANCH ( activityDef )+ ) )+ )
                    pass 
                    self.match(self.input, CHOICEKW, self.FOLLOW_CHOICEKW_in_activityDef332)

                    #action start
                    self.memory.append('enter choice state')
                    self.current_fsm.choice_start_state.append(self.current_fsm.get_current_state())
                    self.current_fsm.choice_end_state.append(self.current_fsm.state_gen.next())
                    	
                    #action end

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:167:2: ( ^( BRANCH ( activityDef )+ ) )+
                    cnt17 = 0
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == BRANCH) :
                            alt17 = 1


                        if alt17 == 1:
                            # BuildFSM.g:167:3: ^( BRANCH ( activityDef )+ )
                            pass 
                            self.match(self.input, BRANCH, self.FOLLOW_BRANCH_in_activityDef342)

                            #action start
                              
                            self.memory.append('enter choice branch and save the current state')

                            self.current_fsm.move_current_state(self.current_fsm.choice_start_state[-1])
                            	
                            #action end

                            self.match(self.input, DOWN, None)
                            # BuildFSM.g:172:4: ( activityDef )+
                            cnt16 = 0
                            while True: #loop16
                                alt16 = 2
                                LA16_0 = self.input.LA(1)

                                if ((RESV <= LA16_0 <= SEND) or (RECLABEL <= LA16_0 <= PARALLEL) or LA16_0 == GLOBAL_ESCAPE or LA16_0 == DO or LA16_0 == CHOICEKW or LA16_0 == RECKW or LA16_0 == 78) :
                                    alt16 = 1


                                if alt16 == 1:
                                    # BuildFSM.g:172:4: activityDef
                                    pass 
                                    self._state.following.append(self.FOLLOW_activityDef_in_activityDef348)
                                    self.activityDef()

                                    self._state.following.pop()


                                else:
                                    if cnt16 >= 1:
                                        break #loop16

                                    eee = EarlyExitException(16, self.input)
                                    raise eee

                                cnt16 += 1

                            self.match(self.input, UP, None)
                            #action start
                              
                            self.memory.append('exit choice branch and set the current state to the end state for the choice')
                            self.current_fsm.fsm.add_transition(self.current_fsm.fsm.EMPTY_TRANSITION, self.current_fsm.get_current_state(), self.current_fsm.choice_end_state[-1])
                            	
                            #action end


                        else:
                            if cnt17 >= 1:
                                break #loop17

                            eee = EarlyExitException(17, self.input)
                            raise eee

                        cnt17 += 1

                    self.match(self.input, UP, None)
                    #action start
                      
                    self.memory.append('set the current state to be equal to the end state for the choice')
                    self.current_fsm.move_current_state(self.current_fsm.choice_end_state[-1])
                    self.current_fsm.choice_end_state.pop()
                    self.current_fsm.choice_start_state.pop()
                    	
                    #action end


                elif alt28 == 4:
                    # BuildFSM.g:184:4: ^( PARALLEL ( ^( BRANCH ( activityDef )+ ) )+ )
                    pass 
                    self.match(self.input, PARALLEL, self.FOLLOW_PARALLEL_in_activityDef367)

                    #action start
                             
                    self.memory.append('enter parallel state')
                    self.parallel_root = self.current_fsm
                            
                    #action end

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:189:2: ( ^( BRANCH ( activityDef )+ ) )+
                    cnt19 = 0
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if (LA19_0 == BRANCH) :
                            alt19 = 1


                        if alt19 == 1:
                            # BuildFSM.g:189:3: ^( BRANCH ( activityDef )+ )
                            pass 
                            self.match(self.input, BRANCH, self.FOLLOW_BRANCH_in_activityDef384)

                            #action start
                              
                            self.memory.append('enter parallel branch')
                            nested_fsm = FSMBuilderState(self.parallel_root)
                            self.parallel_root.fsm.add_fsm_to_memory(self.parallel_root.get_current_state(), nested_fsm.fsm)
                            self.current_fsm = nested_fsm	
                            	
                            #action end

                            self.match(self.input, DOWN, None)
                            # BuildFSM.g:196:2: ( activityDef )+
                            cnt18 = 0
                            while True: #loop18
                                alt18 = 2
                                LA18_0 = self.input.LA(1)

                                if ((RESV <= LA18_0 <= SEND) or (RECLABEL <= LA18_0 <= PARALLEL) or LA18_0 == GLOBAL_ESCAPE or LA18_0 == DO or LA18_0 == CHOICEKW or LA18_0 == RECKW or LA18_0 == 78) :
                                    alt18 = 1


                                if alt18 == 1:
                                    # BuildFSM.g:196:3: activityDef
                                    pass 
                                    self._state.following.append(self.FOLLOW_activityDef_in_activityDef393)
                                    self.activityDef()

                                    self._state.following.pop()


                                else:
                                    if cnt18 >= 1:
                                        break #loop18

                                    eee = EarlyExitException(18, self.input)
                                    raise eee

                                cnt18 += 1

                            self.match(self.input, UP, None)
                            #action start
                              
                            self.memory.append('exit parallel branch')
                            self.current_fsm.add_transition(self.current_fsm.fsm.END_PAR_TRANSITION)
                            	
                            #action end


                        else:
                            if cnt19 >= 1:
                                break #loop19

                            eee = EarlyExitException(19, self.input)
                            raise eee

                        cnt19 += 1

                    self.match(self.input, UP, None)
                    #action start
                    self.memory.append('exit parallel state')
                    self.current_fsm = self.current_fsm.parent
                    self.current_fsm.fsm.add_transition(self.current_fsm.fsm.EMPTY_TRANSITION, self.current_fsm.get_current_state(), self.current_fsm.move_current_state())
                    	
                    #action end


                elif alt28 == 5:
                    # BuildFSM.g:206:3: ^( 'repeat' ( ^( BRANCH ( activityDef )+ ) ) )
                    pass 
                    self.match(self.input, 78, self.FOLLOW_78_in_activityDef414)

                    #action start
                    self.memory.append('enter repeat state')
                    #action end

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:208:2: ( ^( BRANCH ( activityDef )+ ) )
                    # BuildFSM.g:208:3: ^( BRANCH ( activityDef )+ )
                    pass 
                    self.match(self.input, BRANCH, self.FOLLOW_BRANCH_in_activityDef423)

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:208:12: ( activityDef )+
                    cnt20 = 0
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if ((RESV <= LA20_0 <= SEND) or (RECLABEL <= LA20_0 <= PARALLEL) or LA20_0 == GLOBAL_ESCAPE or LA20_0 == DO or LA20_0 == CHOICEKW or LA20_0 == RECKW or LA20_0 == 78) :
                            alt20 = 1


                        if alt20 == 1:
                            # BuildFSM.g:208:13: activityDef
                            pass 
                            self._state.following.append(self.FOLLOW_activityDef_in_activityDef426)
                            self.activityDef()

                            self._state.following.pop()
                            #action start
                            self.memory.append('repeat statement')
                            #action end


                        else:
                            if cnt20 >= 1:
                                break #loop20

                            eee = EarlyExitException(20, self.input)
                            raise eee

                        cnt20 += 1

                    self.match(self.input, UP, None)




                    self.match(self.input, UP, None)
                    #action start
                    self.memory.append('exit repeat state')
                    #action end


                elif alt28 == 6:
                    # BuildFSM.g:211:10: ^( 'rec' label= ID ( ^( BRANCH ( activityDef )+ ) ) )
                    pass 
                    self.match(self.input, RECKW, self.FOLLOW_RECKW_in_activityDef450)

                    self.match(self.input, DOWN, None)
                    label=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef456)
                    #action start
                    self.memory.append('enter rec state ' + label.text + str(self.current_fsm.get_current_state()))
                    self.current_fsm.recursions_states.setdefault(label.text, (self.current_fsm.format_state_name(self.current_fsm.get_current_state()), True))
                            
                    #action end
                    # BuildFSM.g:215:2: ( ^( BRANCH ( activityDef )+ ) )
                    # BuildFSM.g:215:3: ^( BRANCH ( activityDef )+ )
                    pass 
                    self.match(self.input, BRANCH, self.FOLLOW_BRANCH_in_activityDef472)

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:215:12: ( activityDef )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if ((RESV <= LA21_0 <= SEND) or (RECLABEL <= LA21_0 <= PARALLEL) or LA21_0 == GLOBAL_ESCAPE or LA21_0 == DO or LA21_0 == CHOICEKW or LA21_0 == RECKW or LA21_0 == 78) :
                            alt21 = 1


                        if alt21 == 1:
                            # BuildFSM.g:215:13: activityDef
                            pass 
                            self._state.following.append(self.FOLLOW_activityDef_in_activityDef475)
                            self.activityDef()

                            self._state.following.pop()
                            #action start
                            self.memory.append('rec statement')
                            #action end


                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1

                    self.match(self.input, UP, None)




                    self.match(self.input, UP, None)
                    #action start
                      
                    (start_state, isActive) = self.current_fsm.recursions_states.get(label.text)
                    self.memory.append('exit rec state ' + label.text + 'start_state' + str(start_state))
                    self.current_fsm.recursions_states[label.text] = (start_state, False)	 
                    	
                    #action end


                elif alt28 == 7:
                    # BuildFSM.g:222:3: ^( 'RECLABEL' labelID= ID )
                    pass 
                    self.match(self.input, RECLABEL, self.FOLLOW_RECLABEL_in_activityDef493)

                    self.match(self.input, DOWN, None)
                    labelID=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef500)
                    #action start
                      
                    	
                    (start_rec_state, isActive) = self.current_fsm.recursions_states.get(labelID.text)
                    self.memory.append('rec label:' + labelID.text + 'starts from state:' + str(start_rec_state))
                    if isActive:
                    	self.current_fsm.fsm.add_transition(self.current_fsm.fsm.EMPTY_TRANSITION, 
                    					    self.current_fsm.format_state_name(self.current_fsm.get_current_state()), 
                    					    start_rec_state)
                    	# Generate unreachable state for the choice construct						    
                    	self.current_fsm.move_current_state()	
                    else: raise ExceptionFSM('Calling a recusrion label from a recursion that is not valid')
                    	
                    #action end

                    self.match(self.input, UP, None)
                    #action start
                      
                    # Do not need it for no
                           #self.current_fsm.fsm.copy_transitions(self.current_fsm.recursions_states[labelID.text], self.current_fsm.get_current_state())
                    	
                    #action end


                elif alt28 == 8:
                    # BuildFSM.g:239:3: ^( GLOBAL_ESCAPE ( ^( 'interruptible' ( ( activityDef )+ ) ) ) ( ^( 'catch' roleName ( ( activityDef )+ ) ) ) )
                    pass 
                    self.match(self.input, GLOBAL_ESCAPE, self.FOLLOW_GLOBAL_ESCAPE_in_activityDef514)

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:240:5: ( ^( 'interruptible' ( ( activityDef )+ ) ) )
                    # BuildFSM.g:240:6: ^( 'interruptible' ( ( activityDef )+ ) )
                    pass 
                    self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_activityDef523)

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:240:24: ( ( activityDef )+ )
                    # BuildFSM.g:240:25: ( activityDef )+
                    pass 
                    # BuildFSM.g:240:25: ( activityDef )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if ((RESV <= LA22_0 <= SEND) or (RECLABEL <= LA22_0 <= PARALLEL) or LA22_0 == GLOBAL_ESCAPE or LA22_0 == DO or LA22_0 == CHOICEKW or LA22_0 == RECKW or LA22_0 == 78) :
                            alt22 = 1


                        if alt22 == 1:
                            # BuildFSM.g:240:25: activityDef
                            pass 
                            self._state.following.append(self.FOLLOW_activityDef_in_activityDef526)
                            self.activityDef()

                            self._state.following.pop()


                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1



                    #action start
                    self.current_fsm.fsm.final_state = self.current_fsm.get_current_state()
                    #action end

                    self.match(self.input, UP, None)



                    # BuildFSM.g:241:5: ( ^( 'catch' roleName ( ( activityDef )+ ) ) )
                    # BuildFSM.g:241:6: ^( 'catch' roleName ( ( activityDef )+ ) )
                    pass 
                    self.match(self.input, 83, self.FOLLOW_83_in_activityDef539)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_roleName_in_activityDef541)
                    self.roleName()

                    self._state.following.pop()
                    #action start
                    self.memory.append('before setting interrupt_transition to True')
                    self.current_fsm.interrupt_start_state = self.current_fsm.move_current_state()
                    self.current_fsm.set_interrupt_transition = True
                    #action end
                    # BuildFSM.g:244:56: ( ( activityDef )+ )
                    # BuildFSM.g:244:57: ( activityDef )+
                    pass 
                    # BuildFSM.g:244:57: ( activityDef )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if ((RESV <= LA23_0 <= SEND) or (RECLABEL <= LA23_0 <= PARALLEL) or LA23_0 == GLOBAL_ESCAPE or LA23_0 == DO or LA23_0 == CHOICEKW or LA23_0 == RECKW or LA23_0 == 78) :
                            alt23 = 1


                        if alt23 == 1:
                            # BuildFSM.g:244:57: activityDef
                            pass 
                            self._state.following.append(self.FOLLOW_activityDef_in_activityDef550)
                            self.activityDef()

                            self._state.following.pop()


                        else:
                            if cnt23 >= 1:
                                break #loop23

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1




                    self.match(self.input, UP, None)




                    self.match(self.input, UP, None)


                elif alt28 == 9:
                    # BuildFSM.g:245:3: ^( DO (path= ID ) ( ^( PARAMETERLIST ( (label= ID )? ( ^( VALUE ( ID )* ) ) )+ ) ) ( ^( ROLES ( ^( 'as' new_role= ID orig_role= ID ) )+ ) ) )
                    pass 
                    self.match(self.input, DO, self.FOLLOW_DO_in_activityDef560)

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:245:9: (path= ID )
                    # BuildFSM.g:245:10: path= ID
                    pass 
                    path=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef566)
                    #action start
                                     
                    path = path.text
                    self.memory.append('START DO')
                    do_sig_params = []
                    do_role_params = {}
                    #action end



                    # BuildFSM.g:250:3: ( ^( PARAMETERLIST ( (label= ID )? ( ^( VALUE ( ID )* ) ) )+ ) )
                    # BuildFSM.g:250:4: ^( PARAMETERLIST ( (label= ID )? ( ^( VALUE ( ID )* ) ) )+ )
                    pass 
                    self.match(self.input, PARAMETERLIST, self.FOLLOW_PARAMETERLIST_in_activityDef574)

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:250:21: ( (label= ID )? ( ^( VALUE ( ID )* ) ) )+
                    cnt26 = 0
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == VALUE or LA26_0 == ID) :
                            alt26 = 1


                        if alt26 == 1:
                            # BuildFSM.g:250:22: (label= ID )? ( ^( VALUE ( ID )* ) )
                            pass 
                            # BuildFSM.g:250:22: (label= ID )?
                            alt24 = 2
                            LA24_0 = self.input.LA(1)

                            if (LA24_0 == ID) :
                                alt24 = 1
                            if alt24 == 1:
                                # BuildFSM.g:250:23: label= ID
                                pass 
                                label=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef581)



                            # BuildFSM.g:250:34: ( ^( VALUE ( ID )* ) )
                            # BuildFSM.g:250:35: ^( VALUE ( ID )* )
                            pass 
                            self.match(self.input, VALUE, self.FOLLOW_VALUE_in_activityDef587)

                            if self.input.LA(1) == DOWN:
                                self.match(self.input, DOWN, None)
                                # BuildFSM.g:250:43: ( ID )*
                                while True: #loop25
                                    alt25 = 2
                                    LA25_0 = self.input.LA(1)

                                    if (LA25_0 == ID) :
                                        alt25 = 1


                                    if alt25 == 1:
                                        # BuildFSM.g:250:43: ID
                                        pass 
                                        self.match(self.input, ID, self.FOLLOW_ID_in_activityDef589)


                                    else:
                                        break #loop25

                                self.match(self.input, UP, None)




                            #action start
                                                                             
                            if label is not None: 
                            	do_sig_params.append(label.text)
                            	label = None
                            else: do_sig_params.append('')
                            			
                            #action end


                        else:
                            if cnt26 >= 1:
                                break #loop26

                            eee = EarlyExitException(26, self.input)
                            raise eee

                        cnt26 += 1

                    self.match(self.input, UP, None)



                    # BuildFSM.g:256:3: ( ^( ROLES ( ^( 'as' new_role= ID orig_role= ID ) )+ ) )
                    # BuildFSM.g:256:4: ^( ROLES ( ^( 'as' new_role= ID orig_role= ID ) )+ )
                    pass 
                    self.match(self.input, ROLES, self.FOLLOW_ROLES_in_activityDef605)

                    self.match(self.input, DOWN, None)
                    # BuildFSM.g:256:13: ( ^( 'as' new_role= ID orig_role= ID ) )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == ASKW) :
                            alt27 = 1


                        if alt27 == 1:
                            # BuildFSM.g:256:14: ^( 'as' new_role= ID orig_role= ID )
                            pass 
                            self.match(self.input, ASKW, self.FOLLOW_ASKW_in_activityDef610)

                            self.match(self.input, DOWN, None)
                            new_role=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef615)
                            orig_role=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef619)

                            self.match(self.input, UP, None)
                            #action start
                                                                           
                            do_role_params[orig_role.text]=new_role.text
                            #action end


                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1

                    self.match(self.input, UP, None)




                    self.match(self.input, UP, None)
                    #action start
                                                                           
                    self.memory.append('do statement is processed')
                    print 'role_params', do_role_params
                    #full_name = path.split('.')
                    #full_name[-2] = full_path[-2] + '.scr'
                    #full_name = os.path.join(self.import_path, *full_name[:-1])
                    full_name = path + '.scr'
                    full_name = os.path.join(self.import_path, full_name) 
                    print 'full name is', full_name
                    parsed = self.parser.parse(full_name)
                    print parsed.tree
                    builder = self.parser.walk(parsed, sig_params =do_sig_params, sig_roles =do_role_params)
                    print 'sig params in init', builder.sig_params
                    print builder.current_fsm.fsm.state_transitions
                    self.memory.append('do statement processing finished')
                    builder.current_fsm.add_transition(self.current_fsm.fsm.END_PAR_TRANSITION)
                    self.current_fsm.fsm.add_fsm_to_memory(self.current_fsm.get_current_state(), builder.current_fsm.fsm)
                    self.current_fsm.fsm.add_transition(self.current_fsm.fsm.EMPTY_TRANSITION, self.current_fsm.get_current_state(), self.current_fsm.move_current_state())	   
                    	   
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "activityDef"


    # $ANTLR start "roleName"
    # BuildFSM.g:277:1: roleName : role= ID ;
    def roleName(self, ):

        role = None

        try:
            try:
                # BuildFSM.g:277:9: (role= ID )
                # BuildFSM.g:277:11: role= ID
                pass 
                role=self.match(self.input, ID, self.FOLLOW_ID_in_roleName639)
                #action start
                                     
                print 'printing...', role
                if not(role.text in self.roles): self.roles.append(role.text)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "roleName"


    # $ANTLR start "sigName"
    # BuildFSM.g:280:1: sigName : sig= ID ;
    def sigName(self, ):

        sig = None

        try:
            try:
                # BuildFSM.g:280:8: (sig= ID )
                # BuildFSM.g:280:10: sig= ID
                pass 
                sig=self.match(self.input, ID, self.FOLLOW_ID_in_sigName651)
                #action start
                self.sig_map_list.append(sig.text)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "sigName"


    # $ANTLR start "labelName"
    # BuildFSM.g:281:1: labelName : ID ;
    def labelName(self, ):

        try:
            try:
                # BuildFSM.g:281:10: ( ID )
                # BuildFSM.g:281:12: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_labelName661)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "labelName"


    # $ANTLR start "roleDef"
    # BuildFSM.g:282:1: roleDef : ID ;
    def roleDef(self, ):

        try:
            try:
                # BuildFSM.g:282:8: ( ID )
                # BuildFSM.g:282:10: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_roleDef667)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "roleDef"


    # $ANTLR start "primitivetype"
    # BuildFSM.g:283:1: primitivetype : INT ;
    def primitivetype(self, ):

        try:
            try:
                # BuildFSM.g:283:14: ( INT )
                # BuildFSM.g:283:15: INT
                pass 
                self.match(self.input, INT, self.FOLLOW_INT_in_primitivetype672)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "primitivetype"


    # Delegated rules


 

    FOLLOW_PROTOCOL_in_description52 = frozenset([2])
    FOLLOW_roleName_in_description54 = frozenset([27])
    FOLLOW_parameterList_in_description56 = frozenset([24])
    FOLLOW_roleList_in_description58 = frozenset([12, 13, 18, 19, 22, 26, 41, 44, 78])
    FOLLOW_activityDef_in_description60 = frozenset([3, 12, 13, 18, 19, 22, 26, 41, 44, 78])
    FOLLOW_PARAMETERLIST_in_parameterList71 = frozenset([2])
    FOLLOW_sigName_in_parameterList75 = frozenset([3, 56])
    FOLLOW_ROLES_in_roleList88 = frozenset([2])
    FOLLOW_roleName_in_roleList90 = frozenset([3, 56])
    FOLLOW_RESV_in_activityDef102 = frozenset([2])
    FOLLOW_ABSTRACT_in_activityDef118 = frozenset([56])
    FOLLOW_ID_in_activityDef124 = frozenset([15, 56])
    FOLLOW_ID_in_activityDef141 = frozenset([15, 56])
    FOLLOW_VALUE_in_activityDef153 = frozenset([2])
    FOLLOW_ID_in_activityDef159 = frozenset([3, 5, 6, 56])
    FOLLOW_set_in_activityDef163 = frozenset([3, 56])
    FOLLOW_ID_in_activityDef185 = frozenset([21])
    FOLLOW_ASSERT_in_activityDef195 = frozenset([2])
    FOLLOW_ASSERTION_in_activityDef200 = frozenset([3])
    FOLLOW_SEND_in_activityDef213 = frozenset([2])
    FOLLOW_ABSTRACT_in_activityDef222 = frozenset([56])
    FOLLOW_ID_in_activityDef228 = frozenset([15, 56])
    FOLLOW_ID_in_activityDef243 = frozenset([15, 56])
    FOLLOW_VALUE_in_activityDef262 = frozenset([2])
    FOLLOW_ID_in_activityDef268 = frozenset([3, 5, 6, 56])
    FOLLOW_set_in_activityDef273 = frozenset([3, 56])
    FOLLOW_ID_in_activityDef298 = frozenset([21])
    FOLLOW_ASSERT_in_activityDef308 = frozenset([2])
    FOLLOW_ASSERTION_in_activityDef313 = frozenset([3])
    FOLLOW_CHOICEKW_in_activityDef332 = frozenset([2])
    FOLLOW_BRANCH_in_activityDef342 = frozenset([2])
    FOLLOW_activityDef_in_activityDef348 = frozenset([3, 12, 13, 18, 19, 22, 26, 41, 44, 78])
    FOLLOW_PARALLEL_in_activityDef367 = frozenset([2])
    FOLLOW_BRANCH_in_activityDef384 = frozenset([2])
    FOLLOW_activityDef_in_activityDef393 = frozenset([3, 12, 13, 18, 19, 22, 26, 41, 44, 78])
    FOLLOW_78_in_activityDef414 = frozenset([2])
    FOLLOW_BRANCH_in_activityDef423 = frozenset([2])
    FOLLOW_activityDef_in_activityDef426 = frozenset([3, 12, 13, 18, 19, 22, 26, 41, 44, 78])
    FOLLOW_RECKW_in_activityDef450 = frozenset([2])
    FOLLOW_ID_in_activityDef456 = frozenset([16])
    FOLLOW_BRANCH_in_activityDef472 = frozenset([2])
    FOLLOW_activityDef_in_activityDef475 = frozenset([3, 12, 13, 18, 19, 22, 26, 41, 44, 78])
    FOLLOW_RECLABEL_in_activityDef493 = frozenset([2])
    FOLLOW_ID_in_activityDef500 = frozenset([3])
    FOLLOW_GLOBAL_ESCAPE_in_activityDef514 = frozenset([2])
    FOLLOW_INTERRUPTIBLEKW_in_activityDef523 = frozenset([2])
    FOLLOW_activityDef_in_activityDef526 = frozenset([3, 12, 13, 18, 19, 22, 26, 41, 44, 78])
    FOLLOW_83_in_activityDef539 = frozenset([2])
    FOLLOW_roleName_in_activityDef541 = frozenset([12, 13, 18, 19, 22, 26, 41, 44, 78])
    FOLLOW_activityDef_in_activityDef550 = frozenset([3, 12, 13, 18, 19, 22, 26, 41, 44, 78])
    FOLLOW_DO_in_activityDef560 = frozenset([2])
    FOLLOW_ID_in_activityDef566 = frozenset([27])
    FOLLOW_PARAMETERLIST_in_activityDef574 = frozenset([2])
    FOLLOW_ID_in_activityDef581 = frozenset([15])
    FOLLOW_VALUE_in_activityDef587 = frozenset([2])
    FOLLOW_ID_in_activityDef589 = frozenset([3, 56])
    FOLLOW_ROLES_in_activityDef605 = frozenset([2])
    FOLLOW_ASKW_in_activityDef610 = frozenset([2])
    FOLLOW_ID_in_activityDef615 = frozenset([56])
    FOLLOW_ID_in_activityDef619 = frozenset([3])
    FOLLOW_ID_in_roleName639 = frozenset([1])
    FOLLOW_ID_in_sigName651 = frozenset([1])
    FOLLOW_ID_in_labelName661 = frozenset([1])
    FOLLOW_ID_in_roleDef667 = frozenset([1])
    FOLLOW_INT_in_primitivetype672 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(BuildFSM)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
