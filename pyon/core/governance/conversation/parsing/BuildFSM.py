# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 Generate/BuildFSM.g 2014-01-16 19:02:44

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset
        
from pyon.core.governance.conversation.core.fsm import FSM
from pyon.core.governance.conversation.core.fsm import ExceptionFSM
from pyon.core.governance.conversation.core.transition import TransitionFactory
from pyon.core.governance.conversation.core.local_type import LocalType
from pyon.core.governance.conversation.extensions.annotation_processor import *

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
		
	def add_transition(self, transition, assertions = None, transition_context  = None):	        
	       
	        if assertions: 
	        	preprocess_assertion = {}
	        	for assertion in assertions:
	        		preprocess_assertion.update(Assertion.create(assertion))
	        else: preprocess_assertion = assertions
	        
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




class BuildFSM(TreeParser):
    grammarFileName = "Generate/BuildFSM.g"
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
        self.main_fsm = FSMBuilderState()
        self.current_fsm = self.main_fsm




                


        



    # $ANTLR start "description"
    # Generate/BuildFSM.g:110:1: description : ^( PROTOCOL roleName parameterDefs ( activityDef )+ ) ;
    def description(self, ):

        try:
            try:
                # Generate/BuildFSM.g:110:12: ( ^( PROTOCOL roleName parameterDefs ( activityDef )+ ) )
                # Generate/BuildFSM.g:110:14: ^( PROTOCOL roleName parameterDefs ( activityDef )+ )
                pass 
                self.match(self.input, PROTOCOL, self.FOLLOW_PROTOCOL_in_description52)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_roleName_in_description54)
                self.roleName()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_parameterDefs_in_description56)
                self.parameterDefs()

                self._state.following.pop()
                # Generate/BuildFSM.g:110:48: ( activityDef )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((RESV <= LA1_0 <= SEND) or (RECLABEL <= LA1_0 <= PARALLEL) or LA1_0 == GLOBAL_ESCAPE or LA1_0 == 49 or (51 <= LA1_0 <= 52)) :
                        alt1 = 1


                    if alt1 == 1:
                        # Generate/BuildFSM.g:110:48: activityDef
                        pass 
                        self._state.following.append(self.FOLLOW_activityDef_in_description58)
                        self.activityDef()

                        self._state.following.pop()


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1

                self.match(self.input, UP, None)
                #action start
                print "ProtocolDefinition"
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "description"


    # $ANTLR start "parameterDefs"
    # Generate/BuildFSM.g:111:1: parameterDefs : ^( ROLES ( roleName )+ ) ;
    def parameterDefs(self, ):

        try:
            try:
                # Generate/BuildFSM.g:111:14: ( ^( ROLES ( roleName )+ ) )
                # Generate/BuildFSM.g:111:16: ^( ROLES ( roleName )+ )
                pass 
                self.match(self.input, ROLES, self.FOLLOW_ROLES_in_parameterDefs71)

                self.match(self.input, DOWN, None)
                # Generate/BuildFSM.g:111:24: ( roleName )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        alt2 = 1


                    if alt2 == 1:
                        # Generate/BuildFSM.g:111:24: roleName
                        pass 
                        self._state.following.append(self.FOLLOW_roleName_in_parameterDefs73)
                        self.roleName()

                        self._state.following.pop()


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "parameterDefs"


    # $ANTLR start "activityDef"
    # Generate/BuildFSM.g:112:1: activityDef : ( ^( RESV (rlabel= ID )? ( ^( VALUE ( ( (val= ID )? vtype= ( INT | STRING ) ) )* ) ) role= ID ( ^( ASSERT (assertion= ASSERTION )* ) ) ) | ^( SEND (slabel= ID )? ( ^( VALUE ( ( (val= ID )? vtype= ( INT | STRING ) ) )* ) ) role= ID ( ^( ASSERT (assertion= ASSERTION )* ) ) ) | ^( 'choice' ( ^( BRANCH ( activityDef )+ ) )+ ) | ^( PARALLEL ( ^( BRANCH ( activityDef )+ ) )+ ) | ^( 'repeat' ( ^( BRANCH ( activityDef )+ ) ) ) | ^( 'rec' label= ID ( ^( BRANCH ( activityDef )+ ) ) ) | ^( 'RECLABEL' labelID= ID ) | ^( GLOBAL_ESCAPE ( ^( 'do' ( ( activityDef )+ ) ) ) ( ^( 'interrupt' roleName ( ( activityDef )+ ) ) ) ) );
    def activityDef(self, ):

        rlabel = None
        val = None
        vtype = None
        role = None
        assertion = None
        slabel = None
        label = None
        labelID = None

        try:
            try:
                # Generate/BuildFSM.g:112:12: ( ^( RESV (rlabel= ID )? ( ^( VALUE ( ( (val= ID )? vtype= ( INT | STRING ) ) )* ) ) role= ID ( ^( ASSERT (assertion= ASSERTION )* ) ) ) | ^( SEND (slabel= ID )? ( ^( VALUE ( ( (val= ID )? vtype= ( INT | STRING ) ) )* ) ) role= ID ( ^( ASSERT (assertion= ASSERTION )* ) ) ) | ^( 'choice' ( ^( BRANCH ( activityDef )+ ) )+ ) | ^( PARALLEL ( ^( BRANCH ( activityDef )+ ) )+ ) | ^( 'repeat' ( ^( BRANCH ( activityDef )+ ) ) ) | ^( 'rec' label= ID ( ^( BRANCH ( activityDef )+ ) ) ) | ^( 'RECLABEL' labelID= ID ) | ^( GLOBAL_ESCAPE ( ^( 'do' ( ( activityDef )+ ) ) ) ( ^( 'interrupt' roleName ( ( activityDef )+ ) ) ) ) )
                alt19 = 8
                LA19 = self.input.LA(1)
                if LA19 == RESV:
                    alt19 = 1
                elif LA19 == SEND:
                    alt19 = 2
                elif LA19 == 49:
                    alt19 = 3
                elif LA19 == PARALLEL:
                    alt19 = 4
                elif LA19 == 51:
                    alt19 = 5
                elif LA19 == 52:
                    alt19 = 6
                elif LA19 == RECLABEL:
                    alt19 = 7
                elif LA19 == GLOBAL_ESCAPE:
                    alt19 = 8
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # Generate/BuildFSM.g:113:2: ^( RESV (rlabel= ID )? ( ^( VALUE ( ( (val= ID )? vtype= ( INT | STRING ) ) )* ) ) role= ID ( ^( ASSERT (assertion= ASSERTION )* ) ) )
                    pass 
                    self.match(self.input, RESV, self.FOLLOW_RESV_in_activityDef85)

                    #action start
                             
                    assertions = []
                    local_context = []
                    label = ''
                    #action end

                    self.match(self.input, DOWN, None)
                    # Generate/BuildFSM.g:117:5: (rlabel= ID )?
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == ID) :
                        alt3 = 1
                    if alt3 == 1:
                        # Generate/BuildFSM.g:117:6: rlabel= ID
                        pass 
                        rlabel=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef98)
                        #action start
                                          
                        if (rlabel is not None): label = rlabel.text
                        self.memory.append('before setting the label:' +  label)
                        #action end



                    # Generate/BuildFSM.g:120:5: ( ^( VALUE ( ( (val= ID )? vtype= ( INT | STRING ) ) )* ) )
                    # Generate/BuildFSM.g:120:6: ^( VALUE ( ( (val= ID )? vtype= ( INT | STRING ) ) )* )
                    pass 
                    self.match(self.input, VALUE, self.FOLLOW_VALUE_in_activityDef110)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # Generate/BuildFSM.g:120:14: ( ( (val= ID )? vtype= ( INT | STRING ) ) )*
                        while True: #loop5
                            alt5 = 2
                            LA5_0 = self.input.LA(1)

                            if ((INT <= LA5_0 <= STRING) or LA5_0 == ID) :
                                alt5 = 1


                            if alt5 == 1:
                                # Generate/BuildFSM.g:120:15: ( (val= ID )? vtype= ( INT | STRING ) )
                                pass 
                                # Generate/BuildFSM.g:120:15: ( (val= ID )? vtype= ( INT | STRING ) )
                                # Generate/BuildFSM.g:120:16: (val= ID )? vtype= ( INT | STRING )
                                pass 
                                # Generate/BuildFSM.g:120:19: (val= ID )?
                                alt4 = 2
                                LA4_0 = self.input.LA(1)

                                if (LA4_0 == ID) :
                                    alt4 = 1
                                if alt4 == 1:
                                    # Generate/BuildFSM.g:120:19: val= ID
                                    pass 
                                    val=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef116)



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
                                break #loop5

                        self.match(self.input, UP, None)




                    role=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef141)
                    #action start
                    if not(role.text in self.roles): self.roles.append(role.text)
                    #action end
                    # Generate/BuildFSM.g:122:5: ( ^( ASSERT (assertion= ASSERTION )* ) )
                    # Generate/BuildFSM.g:122:6: ^( ASSERT (assertion= ASSERTION )* )
                    pass 
                    self.match(self.input, ASSERT, self.FOLLOW_ASSERT_in_activityDef151)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # Generate/BuildFSM.g:122:15: (assertion= ASSERTION )*
                        while True: #loop6
                            alt6 = 2
                            LA6_0 = self.input.LA(1)

                            if (LA6_0 == ASSERTION) :
                                alt6 = 1


                            if alt6 == 1:
                                # Generate/BuildFSM.g:122:16: assertion= ASSERTION
                                pass 
                                assertion=self.match(self.input, ASSERTION, self.FOLLOW_ASSERTION_in_activityDef156)
                                #action start
                                assertions.append(assertion.text)
                                #action end


                            else:
                                break #loop6

                        self.match(self.input, UP, None)





                    self.match(self.input, UP, None)
                    #action start
                      
                    self.memory.append('label is:' +  label);
                    self.current_fsm.add_transition(TransitionFactory.create(LocalType.RESV, label, role), assertions, local_context)
                    	
                    #action end


                elif alt19 == 2:
                    # Generate/BuildFSM.g:127:3: ^( SEND (slabel= ID )? ( ^( VALUE ( ( (val= ID )? vtype= ( INT | STRING ) ) )* ) ) role= ID ( ^( ASSERT (assertion= ASSERTION )* ) ) )
                    pass 
                    self.match(self.input, SEND, self.FOLLOW_SEND_in_activityDef172)

                    #action start
                              
                    local_context = []
                    assertions = []
                    label = ''
                    #action end

                    self.match(self.input, DOWN, None)
                    # Generate/BuildFSM.g:131:5: (slabel= ID )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == ID) :
                        alt7 = 1
                    if alt7 == 1:
                        # Generate/BuildFSM.g:131:6: slabel= ID
                        pass 
                        slabel=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef185)
                        #action start
                                          
                        self.memory.append('send' + slabel.text)
                        if (slabel is not None): label = slabel.text
                        #action end



                    # Generate/BuildFSM.g:134:12: ( ^( VALUE ( ( (val= ID )? vtype= ( INT | STRING ) ) )* ) )
                    # Generate/BuildFSM.g:134:13: ^( VALUE ( ( (val= ID )? vtype= ( INT | STRING ) ) )* )
                    pass 
                    self.match(self.input, VALUE, self.FOLLOW_VALUE_in_activityDef204)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # Generate/BuildFSM.g:134:21: ( ( (val= ID )? vtype= ( INT | STRING ) ) )*
                        while True: #loop9
                            alt9 = 2
                            LA9_0 = self.input.LA(1)

                            if ((INT <= LA9_0 <= STRING) or LA9_0 == ID) :
                                alt9 = 1


                            if alt9 == 1:
                                # Generate/BuildFSM.g:134:22: ( (val= ID )? vtype= ( INT | STRING ) )
                                pass 
                                # Generate/BuildFSM.g:134:22: ( (val= ID )? vtype= ( INT | STRING ) )
                                # Generate/BuildFSM.g:134:23: (val= ID )? vtype= ( INT | STRING )
                                pass 
                                # Generate/BuildFSM.g:134:26: (val= ID )?
                                alt8 = 2
                                LA8_0 = self.input.LA(1)

                                if (LA8_0 == ID) :
                                    alt8 = 1
                                if alt8 == 1:
                                    # Generate/BuildFSM.g:134:26: val= ID
                                    pass 
                                    val=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef210)



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
                                break #loop9

                        self.match(self.input, UP, None)




                    role=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef239)
                    #action start
                    if not(role.text in self.roles): self.roles.append(role.text)
                    #action end
                    # Generate/BuildFSM.g:136:5: ( ^( ASSERT (assertion= ASSERTION )* ) )
                    # Generate/BuildFSM.g:136:6: ^( ASSERT (assertion= ASSERTION )* )
                    pass 
                    self.match(self.input, ASSERT, self.FOLLOW_ASSERT_in_activityDef249)

                    if self.input.LA(1) == DOWN:
                        self.match(self.input, DOWN, None)
                        # Generate/BuildFSM.g:136:15: (assertion= ASSERTION )*
                        while True: #loop10
                            alt10 = 2
                            LA10_0 = self.input.LA(1)

                            if (LA10_0 == ASSERTION) :
                                alt10 = 1


                            if alt10 == 1:
                                # Generate/BuildFSM.g:136:16: assertion= ASSERTION
                                pass 
                                assertion=self.match(self.input, ASSERTION, self.FOLLOW_ASSERTION_in_activityDef254)
                                #action start
                                assertions.append(assertion.text)
                                #action end


                            else:
                                break #loop10

                        self.match(self.input, UP, None)





                    self.match(self.input, UP, None)
                    #action start
                    self.memory.append('In SEND assertion')
                    #action end
                    #action start
                      
                    self.current_fsm.add_transition(TransitionFactory.create(LocalType.SEND, label, role), assertions,  local_context)
                    	
                    #action end


                elif alt19 == 3:
                    # Generate/BuildFSM.g:141:3: ^( 'choice' ( ^( BRANCH ( activityDef )+ ) )+ )
                    pass 
                    self.match(self.input, 49, self.FOLLOW_49_in_activityDef275)

                    #action start
                    self.memory.append('enter choice state')
                    self.current_fsm.choice_start_state.append(self.current_fsm.get_current_state())
                    self.current_fsm.choice_end_state.append(self.current_fsm.state_gen.next())
                    	
                    #action end

                    self.match(self.input, DOWN, None)
                    # Generate/BuildFSM.g:146:2: ( ^( BRANCH ( activityDef )+ ) )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == BRANCH) :
                            alt12 = 1


                        if alt12 == 1:
                            # Generate/BuildFSM.g:146:3: ^( BRANCH ( activityDef )+ )
                            pass 
                            self.match(self.input, BRANCH, self.FOLLOW_BRANCH_in_activityDef285)

                            #action start
                              
                            self.memory.append('enter choice branch and save the current state')

                            self.current_fsm.move_current_state(self.current_fsm.choice_start_state[-1])
                            	
                            #action end

                            self.match(self.input, DOWN, None)
                            # Generate/BuildFSM.g:151:4: ( activityDef )+
                            cnt11 = 0
                            while True: #loop11
                                alt11 = 2
                                LA11_0 = self.input.LA(1)

                                if ((RESV <= LA11_0 <= SEND) or (RECLABEL <= LA11_0 <= PARALLEL) or LA11_0 == GLOBAL_ESCAPE or LA11_0 == 49 or (51 <= LA11_0 <= 52)) :
                                    alt11 = 1


                                if alt11 == 1:
                                    # Generate/BuildFSM.g:151:4: activityDef
                                    pass 
                                    self._state.following.append(self.FOLLOW_activityDef_in_activityDef291)
                                    self.activityDef()

                                    self._state.following.pop()


                                else:
                                    if cnt11 >= 1:
                                        break #loop11

                                    eee = EarlyExitException(11, self.input)
                                    raise eee

                                cnt11 += 1

                            self.match(self.input, UP, None)
                            #action start
                              
                            self.memory.append('exit choice branch and set the current state to the end state for the choice')
                            self.current_fsm.fsm.add_transition(self.current_fsm.fsm.EMPTY_TRANSITION, self.current_fsm.get_current_state(), self.current_fsm.choice_end_state[-1])
                            	
                            #action end


                        else:
                            if cnt12 >= 1:
                                break #loop12

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1

                    self.match(self.input, UP, None)
                    #action start
                      
                    self.memory.append('set the current state to be equal to the end state for the choice')
                    self.current_fsm.move_current_state(self.current_fsm.choice_end_state[-1])
                    self.current_fsm.choice_end_state.pop()
                    self.current_fsm.choice_start_state.pop()
                    	
                    #action end


                elif alt19 == 4:
                    # Generate/BuildFSM.g:163:4: ^( PARALLEL ( ^( BRANCH ( activityDef )+ ) )+ )
                    pass 
                    self.match(self.input, PARALLEL, self.FOLLOW_PARALLEL_in_activityDef310)

                    #action start
                             
                    self.memory.append('enter parallel state')
                    self.parallel_root = self.current_fsm
                            
                    #action end

                    self.match(self.input, DOWN, None)
                    # Generate/BuildFSM.g:168:2: ( ^( BRANCH ( activityDef )+ ) )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == BRANCH) :
                            alt14 = 1


                        if alt14 == 1:
                            # Generate/BuildFSM.g:168:3: ^( BRANCH ( activityDef )+ )
                            pass 
                            self.match(self.input, BRANCH, self.FOLLOW_BRANCH_in_activityDef327)

                            #action start
                              
                            self.memory.append('enter parallel branch')
                            nested_fsm = FSMBuilderState(self.parallel_root)
                            self.parallel_root.fsm.add_fsm_to_memory(self.parallel_root.get_current_state(), nested_fsm.fsm)
                            self.current_fsm = nested_fsm	
                            	
                            #action end

                            self.match(self.input, DOWN, None)
                            # Generate/BuildFSM.g:175:2: ( activityDef )+
                            cnt13 = 0
                            while True: #loop13
                                alt13 = 2
                                LA13_0 = self.input.LA(1)

                                if ((RESV <= LA13_0 <= SEND) or (RECLABEL <= LA13_0 <= PARALLEL) or LA13_0 == GLOBAL_ESCAPE or LA13_0 == 49 or (51 <= LA13_0 <= 52)) :
                                    alt13 = 1


                                if alt13 == 1:
                                    # Generate/BuildFSM.g:175:3: activityDef
                                    pass 
                                    self._state.following.append(self.FOLLOW_activityDef_in_activityDef336)
                                    self.activityDef()

                                    self._state.following.pop()


                                else:
                                    if cnt13 >= 1:
                                        break #loop13

                                    eee = EarlyExitException(13, self.input)
                                    raise eee

                                cnt13 += 1

                            self.match(self.input, UP, None)
                            #action start
                              
                            self.memory.append('exit parallel branch')
                            self.current_fsm.add_transition(self.current_fsm.fsm.END_PAR_TRANSITION)
                            	
                            #action end


                        else:
                            if cnt14 >= 1:
                                break #loop14

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1

                    self.match(self.input, UP, None)
                    #action start
                    self.memory.append('exit parallel state')
                    self.current_fsm = self.current_fsm.parent
                    self.current_fsm.fsm.add_transition(self.current_fsm.fsm.EMPTY_TRANSITION, self.current_fsm.get_current_state(), self.current_fsm.move_current_state())
                    	
                    #action end


                elif alt19 == 5:
                    # Generate/BuildFSM.g:185:3: ^( 'repeat' ( ^( BRANCH ( activityDef )+ ) ) )
                    pass 
                    self.match(self.input, 51, self.FOLLOW_51_in_activityDef357)

                    #action start
                    self.memory.append('enter repeat state')
                    #action end

                    self.match(self.input, DOWN, None)
                    # Generate/BuildFSM.g:187:2: ( ^( BRANCH ( activityDef )+ ) )
                    # Generate/BuildFSM.g:187:3: ^( BRANCH ( activityDef )+ )
                    pass 
                    self.match(self.input, BRANCH, self.FOLLOW_BRANCH_in_activityDef366)

                    self.match(self.input, DOWN, None)
                    # Generate/BuildFSM.g:187:12: ( activityDef )+
                    cnt15 = 0
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if ((RESV <= LA15_0 <= SEND) or (RECLABEL <= LA15_0 <= PARALLEL) or LA15_0 == GLOBAL_ESCAPE or LA15_0 == 49 or (51 <= LA15_0 <= 52)) :
                            alt15 = 1


                        if alt15 == 1:
                            # Generate/BuildFSM.g:187:13: activityDef
                            pass 
                            self._state.following.append(self.FOLLOW_activityDef_in_activityDef369)
                            self.activityDef()

                            self._state.following.pop()
                            #action start
                            self.memory.append('repeat statement')
                            #action end


                        else:
                            if cnt15 >= 1:
                                break #loop15

                            eee = EarlyExitException(15, self.input)
                            raise eee

                        cnt15 += 1

                    self.match(self.input, UP, None)




                    self.match(self.input, UP, None)
                    #action start
                    self.memory.append('exit repeat state')
                    #action end


                elif alt19 == 6:
                    # Generate/BuildFSM.g:190:10: ^( 'rec' label= ID ( ^( BRANCH ( activityDef )+ ) ) )
                    pass 
                    self.match(self.input, 52, self.FOLLOW_52_in_activityDef393)

                    self.match(self.input, DOWN, None)
                    label=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef399)
                    #action start
                    self.memory.append('enter rec state ' + label.text + str(self.current_fsm.get_current_state()))
                    self.current_fsm.recursions_states.setdefault(label.text, (self.current_fsm.format_state_name(self.current_fsm.get_current_state()), True))
                            
                    #action end
                    # Generate/BuildFSM.g:194:2: ( ^( BRANCH ( activityDef )+ ) )
                    # Generate/BuildFSM.g:194:3: ^( BRANCH ( activityDef )+ )
                    pass 
                    self.match(self.input, BRANCH, self.FOLLOW_BRANCH_in_activityDef415)

                    self.match(self.input, DOWN, None)
                    # Generate/BuildFSM.g:194:12: ( activityDef )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if ((RESV <= LA16_0 <= SEND) or (RECLABEL <= LA16_0 <= PARALLEL) or LA16_0 == GLOBAL_ESCAPE or LA16_0 == 49 or (51 <= LA16_0 <= 52)) :
                            alt16 = 1


                        if alt16 == 1:
                            # Generate/BuildFSM.g:194:13: activityDef
                            pass 
                            self._state.following.append(self.FOLLOW_activityDef_in_activityDef418)
                            self.activityDef()

                            self._state.following.pop()
                            #action start
                            self.memory.append('rec statement')
                            #action end


                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1

                    self.match(self.input, UP, None)




                    self.match(self.input, UP, None)
                    #action start
                      
                    (start_state, isActive) = self.current_fsm.recursions_states.get(label.text)
                    self.memory.append('exit rec state ' + label.text + 'start_state' + str(start_state))
                    self.current_fsm.recursions_states[label.text] = (start_state, False)	 
                    	
                    #action end


                elif alt19 == 7:
                    # Generate/BuildFSM.g:201:3: ^( 'RECLABEL' labelID= ID )
                    pass 
                    self.match(self.input, RECLABEL, self.FOLLOW_RECLABEL_in_activityDef436)

                    self.match(self.input, DOWN, None)
                    labelID=self.match(self.input, ID, self.FOLLOW_ID_in_activityDef443)
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


                elif alt19 == 8:
                    # Generate/BuildFSM.g:218:3: ^( GLOBAL_ESCAPE ( ^( 'do' ( ( activityDef )+ ) ) ) ( ^( 'interrupt' roleName ( ( activityDef )+ ) ) ) )
                    pass 
                    self.match(self.input, GLOBAL_ESCAPE, self.FOLLOW_GLOBAL_ESCAPE_in_activityDef457)

                    self.match(self.input, DOWN, None)
                    # Generate/BuildFSM.g:219:5: ( ^( 'do' ( ( activityDef )+ ) ) )
                    # Generate/BuildFSM.g:219:6: ^( 'do' ( ( activityDef )+ ) )
                    pass 
                    self.match(self.input, 58, self.FOLLOW_58_in_activityDef466)

                    self.match(self.input, DOWN, None)
                    # Generate/BuildFSM.g:219:13: ( ( activityDef )+ )
                    # Generate/BuildFSM.g:219:14: ( activityDef )+
                    pass 
                    # Generate/BuildFSM.g:219:14: ( activityDef )+
                    cnt17 = 0
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if ((RESV <= LA17_0 <= SEND) or (RECLABEL <= LA17_0 <= PARALLEL) or LA17_0 == GLOBAL_ESCAPE or LA17_0 == 49 or (51 <= LA17_0 <= 52)) :
                            alt17 = 1


                        if alt17 == 1:
                            # Generate/BuildFSM.g:219:14: activityDef
                            pass 
                            self._state.following.append(self.FOLLOW_activityDef_in_activityDef469)
                            self.activityDef()

                            self._state.following.pop()


                        else:
                            if cnt17 >= 1:
                                break #loop17

                            eee = EarlyExitException(17, self.input)
                            raise eee

                        cnt17 += 1



                    #action start
                    self.current_fsm.fsm.final_state = self.current_fsm.get_current_state()
                    #action end

                    self.match(self.input, UP, None)



                    # Generate/BuildFSM.g:220:5: ( ^( 'interrupt' roleName ( ( activityDef )+ ) ) )
                    # Generate/BuildFSM.g:220:6: ^( 'interrupt' roleName ( ( activityDef )+ ) )
                    pass 
                    self.match(self.input, 59, self.FOLLOW_59_in_activityDef482)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_roleName_in_activityDef484)
                    self.roleName()

                    self._state.following.pop()
                    #action start
                    self.memory.append('before setting interrupt_transition to True')
                    self.current_fsm.interrupt_start_state = self.current_fsm.move_current_state()
                    self.current_fsm.set_interrupt_transition = True
                    #action end
                    # Generate/BuildFSM.g:223:56: ( ( activityDef )+ )
                    # Generate/BuildFSM.g:223:57: ( activityDef )+
                    pass 
                    # Generate/BuildFSM.g:223:57: ( activityDef )+
                    cnt18 = 0
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if ((RESV <= LA18_0 <= SEND) or (RECLABEL <= LA18_0 <= PARALLEL) or LA18_0 == GLOBAL_ESCAPE or LA18_0 == 49 or (51 <= LA18_0 <= 52)) :
                            alt18 = 1


                        if alt18 == 1:
                            # Generate/BuildFSM.g:223:57: activityDef
                            pass 
                            self._state.following.append(self.FOLLOW_activityDef_in_activityDef493)
                            self.activityDef()

                            self._state.following.pop()


                        else:
                            if cnt18 >= 1:
                                break #loop18

                            eee = EarlyExitException(18, self.input)
                            raise eee

                        cnt18 += 1




                    self.match(self.input, UP, None)




                    self.match(self.input, UP, None)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "activityDef"


    # $ANTLR start "roleName"
    # Generate/BuildFSM.g:225:1: roleName : role= ID ;
    def roleName(self, ):

        role = None

        try:
            try:
                # Generate/BuildFSM.g:225:9: (role= ID )
                # Generate/BuildFSM.g:225:11: role= ID
                pass 
                role=self.match(self.input, ID, self.FOLLOW_ID_in_roleName510)
                #action start
                                      
                if not(role.text in self.roles): 
                	self.roles.append(role.text)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "roleName"


    # $ANTLR start "labelName"
    # Generate/BuildFSM.g:228:1: labelName : ID ;
    def labelName(self, ):

        try:
            try:
                # Generate/BuildFSM.g:228:10: ( ID )
                # Generate/BuildFSM.g:228:12: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_labelName518)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "labelName"


    # $ANTLR start "roleDef"
    # Generate/BuildFSM.g:229:1: roleDef : ID ;
    def roleDef(self, ):

        try:
            try:
                # Generate/BuildFSM.g:229:8: ( ID )
                # Generate/BuildFSM.g:229:10: ID
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_roleDef524)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "roleDef"


    # $ANTLR start "primitivetype"
    # Generate/BuildFSM.g:230:1: primitivetype : INT ;
    def primitivetype(self, ):

        try:
            try:
                # Generate/BuildFSM.g:230:15: ( INT )
                # Generate/BuildFSM.g:230:16: INT
                pass 
                self.match(self.input, INT, self.FOLLOW_INT_in_primitivetype530)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "primitivetype"


    # Delegated rules


 

    FOLLOW_PROTOCOL_in_description52 = frozenset([2])
    FOLLOW_roleName_in_description54 = frozenset([24])
    FOLLOW_parameterDefs_in_description56 = frozenset([12, 13, 18, 19, 22, 49, 51, 52])
    FOLLOW_activityDef_in_description58 = frozenset([3, 12, 13, 18, 19, 22, 49, 51, 52])
    FOLLOW_ROLES_in_parameterDefs71 = frozenset([2])
    FOLLOW_roleName_in_parameterDefs73 = frozenset([3, 26])
    FOLLOW_RESV_in_activityDef85 = frozenset([2])
    FOLLOW_ID_in_activityDef98 = frozenset([15])
    FOLLOW_VALUE_in_activityDef110 = frozenset([2])
    FOLLOW_ID_in_activityDef116 = frozenset([5, 6])
    FOLLOW_set_in_activityDef121 = frozenset([3, 5, 6, 26])
    FOLLOW_ID_in_activityDef141 = frozenset([21])
    FOLLOW_ASSERT_in_activityDef151 = frozenset([2])
    FOLLOW_ASSERTION_in_activityDef156 = frozenset([3, 28])
    FOLLOW_SEND_in_activityDef172 = frozenset([2])
    FOLLOW_ID_in_activityDef185 = frozenset([15])
    FOLLOW_VALUE_in_activityDef204 = frozenset([2])
    FOLLOW_ID_in_activityDef210 = frozenset([5, 6])
    FOLLOW_set_in_activityDef216 = frozenset([3, 5, 6, 26])
    FOLLOW_ID_in_activityDef239 = frozenset([21])
    FOLLOW_ASSERT_in_activityDef249 = frozenset([2])
    FOLLOW_ASSERTION_in_activityDef254 = frozenset([3, 28])
    FOLLOW_49_in_activityDef275 = frozenset([2])
    FOLLOW_BRANCH_in_activityDef285 = frozenset([2])
    FOLLOW_activityDef_in_activityDef291 = frozenset([3, 12, 13, 18, 19, 22, 49, 51, 52])
    FOLLOW_PARALLEL_in_activityDef310 = frozenset([2])
    FOLLOW_BRANCH_in_activityDef327 = frozenset([2])
    FOLLOW_activityDef_in_activityDef336 = frozenset([3, 12, 13, 18, 19, 22, 49, 51, 52])
    FOLLOW_51_in_activityDef357 = frozenset([2])
    FOLLOW_BRANCH_in_activityDef366 = frozenset([2])
    FOLLOW_activityDef_in_activityDef369 = frozenset([3, 12, 13, 18, 19, 22, 49, 51, 52])
    FOLLOW_52_in_activityDef393 = frozenset([2])
    FOLLOW_ID_in_activityDef399 = frozenset([16])
    FOLLOW_BRANCH_in_activityDef415 = frozenset([2])
    FOLLOW_activityDef_in_activityDef418 = frozenset([3, 12, 13, 18, 19, 22, 49, 51, 52])
    FOLLOW_RECLABEL_in_activityDef436 = frozenset([2])
    FOLLOW_ID_in_activityDef443 = frozenset([3])
    FOLLOW_GLOBAL_ESCAPE_in_activityDef457 = frozenset([2])
    FOLLOW_58_in_activityDef466 = frozenset([2])
    FOLLOW_activityDef_in_activityDef469 = frozenset([3, 12, 13, 18, 19, 22, 49, 51, 52])
    FOLLOW_59_in_activityDef482 = frozenset([2])
    FOLLOW_roleName_in_activityDef484 = frozenset([12, 13, 18, 19, 22, 49, 51, 52])
    FOLLOW_activityDef_in_activityDef493 = frozenset([3, 12, 13, 18, 19, 22, 49, 51, 52])
    FOLLOW_ID_in_roleName510 = frozenset([1])
    FOLLOW_ID_in_labelName518 = frozenset([1])
    FOLLOW_ID_in_roleDef524 = frozenset([1])
    FOLLOW_INT_in_primitivetype530 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(BuildFSM)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
