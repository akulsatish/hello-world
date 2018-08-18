#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on May 24, 2018, at 16:38
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'ATNT_Intrusions_Phase_v4'  # from the Builder filename that created this script
expInfo = {u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], ' ', 'PHASE III')

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'Z:\\Intrusions study PsychoPy program\\Intrusions study PsychoPy program v2\\ATNT_Intrusions_Phase_final_v2.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1600, 1200), fullscr=True, screen=1,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Initialise_Code"
Initialise_CodeClock = core.Clock()
import random, xlrd

#randomise the seed so that each time file is opened, the order of presentation is randomised
random.seed()

#stimulus file for the main experiment loop
infile = 'Participants_Data/'+expInfo['participant']+'.xlsx'

#number of test items
num_test = 12

#number of repetitions you want in test loop
num_test_reps = 20

#calculate total number of trials in main experiment
num_test_trials = num_test*num_test_reps


#number of practice items
num_practice = 2

#number of repititions of practice items
num_practice_reps = 5

#number of total trials in main experiment 
num_practice_trials = num_practice*num_practice_reps

#number of total items in your stimulus file
num_total = 14

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instr = visual.TextStim(win=win, name='Instr',
    text='Instructions will be given by the experimenter.\n\nPress any key to continue. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Practice1"
Practice1Clock = core.Clock()
Practice1_instr = visual.TextStim(win=win, name='Practice1_instr',
    text='Practice 1 begins now.\n\nPlease wait for the experimenter.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "PracCode"
PracCodeClock = core.Clock()
#create a list of the order in which to show test items
prac_order = range(num_practice)

#randomise the order of test list items
random.shuffle(prac_order)

#current test trial
prac_trial = 0

# Initialize components for Routine "Think_No_Think"
Think_No_ThinkClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
title_cue = visual.TextStim(win=win, name='title_cue',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Practice2"
Practice2Clock = core.Clock()
Practice2_instr = visual.TextStim(win=win, name='Practice2_instr',
    text='Please wait for the experimenter to adminster the questionnaire.\n\nPractice 2 begins after the questionnaire.\n\nPress any key to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Intrusions_practice"
Intrusions_practiceClock = core.Clock()
Rating = visual.TextStim(win=win, name='Rating',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
ISI_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
Fixate = visual.TextStim(win=win, name='Fixate',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Intrusions_practice_response"
Intrusions_practice_responseClock = core.Clock()
Intr_scale = visual.TextStim(win=win, name='Intr_scale',
    text='1 2 3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "Practice3"
Practice3Clock = core.Clock()
Prac3_instr = visual.TextStim(win=win, name='Prac3_instr',
    text='Practice 3 begins now\n\nPlease wait for the experimenter.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "PracCode"
PracCodeClock = core.Clock()
#create a list of the order in which to show test items
prac_order = range(num_practice)

#randomise the order of test list items
random.shuffle(prac_order)

#current test trial
prac_trial = 0

# Initialize components for Routine "Think_No_Think"
Think_No_ThinkClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
title_cue = visual.TextStim(win=win, name='title_cue',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Intrusions"
IntrusionsClock = core.Clock()
Intrusion_Rating = visual.TextStim(win=win, name='Intrusion_Rating',
    text='1 2 3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Main_Exp"
Main_ExpClock = core.Clock()
Main_Experiment = visual.TextStim(win=win, name='Main_Experiment',
    text='This is the end of practice.\n\nThe actual experiment begins now.\n\nPlease wait for the experimenter to adminster the questionnaire.\n\nYou may press any key to continue after the questionnaire.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Test_Code"
Test_CodeClock = core.Clock()
#create a list of the order in which to show test items
test_order = range(num_test)

#randomise the order of test list items
random.shuffle(test_order)


#current test trial
test_trial = 0


# Initialize components for Routine "Think_No_Think"
Think_No_ThinkClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
title_cue = visual.TextStim(win=win, name='title_cue',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Intrusions"
IntrusionsClock = core.Clock()
Intrusion_Rating = visual.TextStim(win=win, name='Intrusion_Rating',
    text='1 2 3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Break_questionnaire"
Break_questionnaireClock = core.Clock()
Break_q = visual.TextStim(win=win, name='Break_q',
    text='Please take a break now and call the experimenter.\n\nYou are halfway through this task.\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
mycount1 = 0

# Initialize components for Routine "Break"
BreakClock = core.Clock()
Break_Instr = visual.TextStim(win=win, name='Break_Instr',
    text='Please take a short break.\n\nWhenever you are ready to resume, press any key to continue.  ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
mycount=0

# Initialize components for Routine "End"
EndClock = core.Clock()
END_ = visual.TextStim(win=win, name='END_',
    text='Please take a break now if you wish to and wait for the experimenter.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Initialise_Code"-------
t = 0
Initialise_CodeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
#access the xlsx stimulus file
inbook = xlrd.open_workbook(infile)
insheet = inbook.sheet_by_index(0) #go to xlsx file and get sheet number 1

#arrays for our stimuli

title_ar = []
moral_cond = []

#read the stimuli from our sheet
for rowx in range(1,num_test+1):

    row = insheet.row_values(rowx) #assign all column values for each row to arrayed variable "row"
    
    #print out the value of column A and B for debugging
    #print row[0]+" "+row[1]

    title_ar.append(row[0])
    moral_cond.append(row[1])

#create a stimulus order list
stim_order = range(num_test)

#randomises the order of the stimulus array
random.shuffle(stim_order)

#arrays for our final stimuli
title_item = []
moral_cond_item = []
cue_colour = []

#create in final stimulus list
for i in range(num_test):
    
    #assign a item from the list of items

    title_item.append(title_ar[stim_order[i]])
    moral_cond_item.append(moral_cond[stim_order[i]])
    
    #determine the colour of the items
    if moral_cond_item == "Right":                  #This if statement is to ensure that colour is assigned equally across morality conditions 
        
        if i%2==0:                                  #All even rows will be green and all odd rows will be red for morally right cues
            cue_colour.append("green")
        else:
            cue_colour.append("red")
    else:
        
        if i%2==0:                                  #All even rows will be green and all odd rows will be red for morally wrong cues
            cue_colour.append("green")
        else:
            cue_colour.append("red")

    
    #user output for debug purposes
    #print "item #" + str(i) + ": " + category_item[i] + " " + title_item[i]+ " "+ moral_cond_item[i] + " " + cue_colour[i]

#READ STIMULI for PRACTICE BLOCKS

#arrays for our stimuli

title_ar_prac = []

#read the stimuli from our sheet
for rowx in range(num_test+1,num_total+1):

    row = insheet.row_values(rowx) #assign all column values for each row to arrayed variable "row"
    
    #print out the value of column A and B for debugging
    #print row[0]+' '+row[1]+' '+row[2]

    title_ar_prac.append(row[0])

#create a stimulus order list
stim_order_prac = range(num_practice)

#randomises the order of the stimulus array
random.shuffle(stim_order_prac)

#arrays for our final practice stimuli

title_item_prac = []
cue_colour_prac = []

#create in final stimulus list
for i in range(num_practice):
    
    #assign a item from the list of items
    title_item_prac.append(title_ar_prac[stim_order_prac[i]])
    
    
    #determine the colour of the items 
    if i==0:                                  #All even rows will be green and all odd rows will be red for morally right cues
        cue_colour_prac.append("green")
    else:
        cue_colour_prac.append("red")
    
    #user output for debug purposes
    #print "item #" + str(i) + ": " + category_item_prac[i] + " " + title_item_prac[i]+ " "+ cue_colour_prac[i]


# keep track of which components have finished
Initialise_CodeComponents = []
for thisComponent in Initialise_CodeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Initialise_Code"-------
while continueRoutine:
    # get current time
    t = Initialise_CodeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Initialise_CodeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Initialise_Code"-------
for thisComponent in Initialise_CodeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Initialise_Code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Instr_Resp = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [Instr, Instr_Resp]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr* updates
    if t >= 0.0 and Instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr.tStart = t
        Instr.frameNStart = frameN  # exact frame index
        Instr.setAutoDraw(True)
    
    # *Instr_Resp* updates
    if t >= 0.0 and Instr_Resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr_Resp.tStart = t
        Instr_Resp.frameNStart = frameN  # exact frame index
        Instr_Resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Instr_Resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Practice1"-------
t = 0
Practice1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Practice1_resp = event.BuilderKeyResponse()
# keep track of which components have finished
Practice1Components = [Practice1_instr, Practice1_resp]
for thisComponent in Practice1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Practice1"-------
while continueRoutine:
    # get current time
    t = Practice1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Practice1_instr* updates
    if t >= 0.0 and Practice1_instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        Practice1_instr.tStart = t
        Practice1_instr.frameNStart = frameN  # exact frame index
        Practice1_instr.setAutoDraw(True)
    
    # *Practice1_resp* updates
    if t >= 0.0 and Practice1_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        Practice1_resp.tStart = t
        Practice1_resp.frameNStart = frameN  # exact frame index
        Practice1_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Practice1_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if Practice1_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Practice1_resp.keys = theseKeys[-1]  # just the last key pressed
            Practice1_resp.rt = Practice1_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Practice1"-------
for thisComponent in Practice1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Practice1_resp.keys in ['', [], None]:  # No response was made
    Practice1_resp.keys=None
thisExp.addData('Practice1_resp.keys',Practice1_resp.keys)
if Practice1_resp.keys != None:  # we had a response
    thisExp.addData('Practice1_resp.rt', Practice1_resp.rt)
thisExp.nextEntry()
# the Routine "Practice1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TNT_Loop = data.TrialHandler(nReps=num_practice_trials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='TNT_Loop')
thisExp.addLoop(TNT_Loop)  # add the loop to the experiment
thisTNT_Loop = TNT_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTNT_Loop.rgb)
if thisTNT_Loop != None:
    for paramName in thisTNT_Loop.keys():
        exec(paramName + '= thisTNT_Loop.' + paramName)

for thisTNT_Loop in TNT_Loop:
    currentLoop = TNT_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTNT_Loop.rgb)
    if thisTNT_Loop != None:
        for paramName in thisTNT_Loop.keys():
            exec(paramName + '= thisTNT_Loop.' + paramName)
    
    # ------Prepare to start Routine "PracCode"-------
    t = 0
    PracCodeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    #randomises order of stimulus presentation after one loop of presenting all stimuli
    if prac_trial%num_practice == 0:
        random.shuffle(prac_order)
    
    #assign the stimuli to variables that are used in the blocks
    title = title_item_prac[prac_order[prac_trial%num_practice]]
    colour = cue_colour_prac[prac_order[prac_trial%num_practice]]
    
    #for debug purposes
    #print test_order
    
    #Add data to data file
    thisExp.addData("title", title)
    thisExp.addData("colour", colour)
    
    thisExp.addData('practice_trial', prac_trial)
    thisExp.addData('practice_order', prac_order)
    
    #incrememnt the current test item counter
    prac_trial = prac_trial+1
    # keep track of which components have finished
    PracCodeComponents = []
    for thisComponent in PracCodeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "PracCode"-------
    while continueRoutine:
        # get current time
        t = PracCodeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracCodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracCode"-------
    for thisComponent in PracCodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "PracCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Think_No_Think"-------
    t = 0
    Think_No_ThinkClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.600000)
    # update component parameters for each repeat
    title_cue.setColor(colour, colorSpace='rgb')
    title_cue.setText(title)
    # keep track of which components have finished
    Think_No_ThinkComponents = [Fixation, ISI, title_cue]
    for thisComponent in Think_No_ThinkComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Think_No_Think"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Think_No_ThinkClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if t >= 0.4 and Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation.tStart = t
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.setAutoDraw(True)
        frameRemains = 0.4 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation.status == STARTED and t >= frameRemains:
            Fixation.setAutoDraw(False)
        
        # *title_cue* updates
        if t >= 0.6 and title_cue.status == NOT_STARTED:
            # keep track of start time/frame for later
            title_cue.tStart = t
            title_cue.frameNStart = frameN  # exact frame index
            title_cue.setAutoDraw(True)
        frameRemains = 0.6 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if title_cue.status == STARTED and t >= frameRemains:
            title_cue.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.4)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Think_No_ThinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Think_No_Think"-------
    for thisComponent in Think_No_ThinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed num_practice_trials repeats of 'TNT_Loop'

# get names of stimulus parameters
if TNT_Loop.trialList in ([], [None], None):
    params = []
else:
    params = TNT_Loop.trialList[0].keys()
# save data for this loop
TNT_Loop.saveAsExcel(filename + '.xlsx', sheetName='TNT_Loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Practice2"-------
t = 0
Practice2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Practice2_resp = event.BuilderKeyResponse()
# keep track of which components have finished
Practice2Components = [Practice2_instr, Practice2_resp]
for thisComponent in Practice2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Practice2"-------
while continueRoutine:
    # get current time
    t = Practice2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Practice2_instr* updates
    if t >= 0.0 and Practice2_instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        Practice2_instr.tStart = t
        Practice2_instr.frameNStart = frameN  # exact frame index
        Practice2_instr.setAutoDraw(True)
    
    # *Practice2_resp* updates
    if t >= 0.0 and Practice2_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        Practice2_resp.tStart = t
        Practice2_resp.frameNStart = frameN  # exact frame index
        Practice2_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Practice2_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Practice2"-------
for thisComponent in Practice2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Practice2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Intr_practice_loop = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Intrusions study Practice2 conditions.xlsx'),
    seed=None, name='Intr_practice_loop')
thisExp.addLoop(Intr_practice_loop)  # add the loop to the experiment
thisIntr_practice_loop = Intr_practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIntr_practice_loop.rgb)
if thisIntr_practice_loop != None:
    for paramName in thisIntr_practice_loop.keys():
        exec(paramName + '= thisIntr_practice_loop.' + paramName)

for thisIntr_practice_loop in Intr_practice_loop:
    currentLoop = Intr_practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisIntr_practice_loop.rgb)
    if thisIntr_practice_loop != None:
        for paramName in thisIntr_practice_loop.keys():
            exec(paramName + '= thisIntr_practice_loop.' + paramName)
    
    # ------Prepare to start Routine "Intrusions_practice"-------
    t = 0
    Intrusions_practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.800000)
    # update component parameters for each repeat
    Rating.setText(Intr_Rating
)
    # keep track of which components have finished
    Intrusions_practiceComponents = [Rating, ISI_2, Fixate]
    for thisComponent in Intrusions_practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Intrusions_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Intrusions_practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Rating* updates
        if t >= 0.8 and Rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            Rating.tStart = t
            Rating.frameNStart = frameN  # exact frame index
            Rating.setAutoDraw(True)
        frameRemains = 0.8 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Rating.status == STARTED and t >= frameRemains:
            Rating.setAutoDraw(False)
        
        # *Fixate* updates
        if t >= 0.4 and Fixate.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixate.tStart = t
            Fixate.frameNStart = frameN  # exact frame index
            Fixate.setAutoDraw(True)
        frameRemains = 0.4 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixate.status == STARTED and t >= frameRemains:
            Fixate.setAutoDraw(False)
        # *ISI_2* period
        if t >= 0.0 and ISI_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_2.tStart = t
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.start(0.4)
        elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
            ISI_2.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Intrusions_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Intrusions_practice"-------
    for thisComponent in Intrusions_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Intrusions_practice_response"-------
    t = 0
    Intrusions_practice_responseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating_response = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    Intrusions_practice_responseComponents = [Intr_scale, rating_response]
    for thisComponent in Intrusions_practice_responseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Intrusions_practice_response"-------
    while continueRoutine:
        # get current time
        t = Intrusions_practice_responseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Intr_scale* updates
        if t >= 0.1 and Intr_scale.status == NOT_STARTED:
            # keep track of start time/frame for later
            Intr_scale.tStart = t
            Intr_scale.frameNStart = frameN  # exact frame index
            Intr_scale.setAutoDraw(True)
        
        # *rating_response* updates
        if t >= 0.1 and rating_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_response.tStart = t
            rating_response.frameNStart = frameN  # exact frame index
            rating_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(rating_response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if rating_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                rating_response.keys = theseKeys[-1]  # just the last key pressed
                rating_response.rt = rating_response.clock.getTime()
                # was this 'correct'?
                if (rating_response.keys == str(corrAns)) or (rating_response.keys == corrAns):
                    rating_response.corr = 1
                else:
                    rating_response.corr = 0
        if rating_response.corr == 1:
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Intrusions_practice_responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Intrusions_practice_response"-------
    for thisComponent in Intrusions_practice_responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if rating_response.keys in ['', [], None]:  # No response was made
        rating_response.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           rating_response.corr = 1  # correct non-response
        else:
           rating_response.corr = 0  # failed to respond (incorrectly)
    # store data for Intr_practice_loop (TrialHandler)
    Intr_practice_loop.addData('rating_response.keys',rating_response.keys)
    Intr_practice_loop.addData('rating_response.corr', rating_response.corr)
    if rating_response.keys != None:  # we had a response
        Intr_practice_loop.addData('rating_response.rt', rating_response.rt)
    
    # the Routine "Intrusions_practice_response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'Intr_practice_loop'

# get names of stimulus parameters
if Intr_practice_loop.trialList in ([], [None], None):
    params = []
else:
    params = Intr_practice_loop.trialList[0].keys()
# save data for this loop
Intr_practice_loop.saveAsExcel(filename + '.xlsx', sheetName='Intr_practice_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Practice3"-------
t = 0
Practice3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Prac3_instr_resp = event.BuilderKeyResponse()
# keep track of which components have finished
Practice3Components = [Prac3_instr, Prac3_instr_resp]
for thisComponent in Practice3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Practice3"-------
while continueRoutine:
    # get current time
    t = Practice3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Prac3_instr* updates
    if t >= 0.0 and Prac3_instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        Prac3_instr.tStart = t
        Prac3_instr.frameNStart = frameN  # exact frame index
        Prac3_instr.setAutoDraw(True)
    
    # *Prac3_instr_resp* updates
    if t >= 0.0 and Prac3_instr_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        Prac3_instr_resp.tStart = t
        Prac3_instr_resp.frameNStart = frameN  # exact frame index
        Prac3_instr_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Prac3_instr_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Practice3"-------
for thisComponent in Practice3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Practice3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practice_exp_loop = data.TrialHandler(nReps=num_practice_trials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Practice_exp_loop')
thisExp.addLoop(Practice_exp_loop)  # add the loop to the experiment
thisPractice_exp_loop = Practice_exp_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_exp_loop.rgb)
if thisPractice_exp_loop != None:
    for paramName in thisPractice_exp_loop.keys():
        exec(paramName + '= thisPractice_exp_loop.' + paramName)

for thisPractice_exp_loop in Practice_exp_loop:
    currentLoop = Practice_exp_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_exp_loop.rgb)
    if thisPractice_exp_loop != None:
        for paramName in thisPractice_exp_loop.keys():
            exec(paramName + '= thisPractice_exp_loop.' + paramName)
    
    # ------Prepare to start Routine "PracCode"-------
    t = 0
    PracCodeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    #randomises order of stimulus presentation after one loop of presenting all stimuli
    if prac_trial%num_practice == 0:
        random.shuffle(prac_order)
    
    #assign the stimuli to variables that are used in the blocks
    title = title_item_prac[prac_order[prac_trial%num_practice]]
    colour = cue_colour_prac[prac_order[prac_trial%num_practice]]
    
    #for debug purposes
    #print test_order
    
    #Add data to data file
    thisExp.addData("title", title)
    thisExp.addData("colour", colour)
    
    thisExp.addData('practice_trial', prac_trial)
    thisExp.addData('practice_order', prac_order)
    
    #incrememnt the current test item counter
    prac_trial = prac_trial+1
    # keep track of which components have finished
    PracCodeComponents = []
    for thisComponent in PracCodeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "PracCode"-------
    while continueRoutine:
        # get current time
        t = PracCodeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracCodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracCode"-------
    for thisComponent in PracCodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "PracCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Think_No_Think"-------
    t = 0
    Think_No_ThinkClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.600000)
    # update component parameters for each repeat
    title_cue.setColor(colour, colorSpace='rgb')
    title_cue.setText(title)
    # keep track of which components have finished
    Think_No_ThinkComponents = [Fixation, ISI, title_cue]
    for thisComponent in Think_No_ThinkComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Think_No_Think"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Think_No_ThinkClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if t >= 0.4 and Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation.tStart = t
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.setAutoDraw(True)
        frameRemains = 0.4 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation.status == STARTED and t >= frameRemains:
            Fixation.setAutoDraw(False)
        
        # *title_cue* updates
        if t >= 0.6 and title_cue.status == NOT_STARTED:
            # keep track of start time/frame for later
            title_cue.tStart = t
            title_cue.frameNStart = frameN  # exact frame index
            title_cue.setAutoDraw(True)
        frameRemains = 0.6 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if title_cue.status == STARTED and t >= frameRemains:
            title_cue.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.4)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Think_No_ThinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Think_No_Think"-------
    for thisComponent in Think_No_ThinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Intrusions"-------
    t = 0
    IntrusionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.600000)
    # update component parameters for each repeat
    Intrusion_response = event.BuilderKeyResponse()
    # keep track of which components have finished
    IntrusionsComponents = [Intrusion_Rating, Intrusion_response]
    for thisComponent in IntrusionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Intrusions"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = IntrusionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Intrusion_Rating* updates
        if t >= 0.1 and Intrusion_Rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            Intrusion_Rating.tStart = t
            Intrusion_Rating.frameNStart = frameN  # exact frame index
            Intrusion_Rating.setAutoDraw(True)
        frameRemains = 0.1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Intrusion_Rating.status == STARTED and t >= frameRemains:
            Intrusion_Rating.setAutoDraw(False)
        
        # *Intrusion_response* updates
        if t >= 0.1 and Intrusion_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Intrusion_response.tStart = t
            Intrusion_response.frameNStart = frameN  # exact frame index
            Intrusion_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Intrusion_response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Intrusion_response.status == STARTED and t >= frameRemains:
            Intrusion_response.status = STOPPED
        if Intrusion_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Intrusion_response.keys = theseKeys[-1]  # just the last key pressed
                Intrusion_response.rt = Intrusion_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IntrusionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Intrusions"-------
    for thisComponent in IntrusionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Intrusion_response.keys in ['', [], None]:  # No response was made
        Intrusion_response.keys=None
    Practice_exp_loop.addData('Intrusion_response.keys',Intrusion_response.keys)
    if Intrusion_response.keys != None:  # we had a response
        Practice_exp_loop.addData('Intrusion_response.rt', Intrusion_response.rt)
    thisExp.nextEntry()
    
# completed num_practice_trials repeats of 'Practice_exp_loop'

# get names of stimulus parameters
if Practice_exp_loop.trialList in ([], [None], None):
    params = []
else:
    params = Practice_exp_loop.trialList[0].keys()
# save data for this loop
Practice_exp_loop.saveAsExcel(filename + '.xlsx', sheetName='Practice_exp_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Main_Exp"-------
t = 0
Main_ExpClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Exp_response = event.BuilderKeyResponse()
# keep track of which components have finished
Main_ExpComponents = [Main_Experiment, Exp_response]
for thisComponent in Main_ExpComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Main_Exp"-------
while continueRoutine:
    # get current time
    t = Main_ExpClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Main_Experiment* updates
    if t >= 0.0 and Main_Experiment.status == NOT_STARTED:
        # keep track of start time/frame for later
        Main_Experiment.tStart = t
        Main_Experiment.frameNStart = frameN  # exact frame index
        Main_Experiment.setAutoDraw(True)
    
    # *Exp_response* updates
    if t >= 0.0 and Exp_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        Exp_response.tStart = t
        Exp_response.frameNStart = frameN  # exact frame index
        Exp_response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Exp_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Main_ExpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Main_Exp"-------
for thisComponent in Main_ExpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Main_Exp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TNT_loop = data.TrialHandler(nReps=num_test_trials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='TNT_loop')
thisExp.addLoop(TNT_loop)  # add the loop to the experiment
thisTNT_loop = TNT_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTNT_loop.rgb)
if thisTNT_loop != None:
    for paramName in thisTNT_loop.keys():
        exec(paramName + '= thisTNT_loop.' + paramName)

for thisTNT_loop in TNT_loop:
    currentLoop = TNT_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTNT_loop.rgb)
    if thisTNT_loop != None:
        for paramName in thisTNT_loop.keys():
            exec(paramName + '= thisTNT_loop.' + paramName)
    
    # ------Prepare to start Routine "Test_Code"-------
    t = 0
    Test_CodeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    #randomises order of stimulus presentation after one loop of presenting all stimuli
    if test_trial%num_test == 0:
        random.shuffle(test_order)
    
    #assign the current stimulus number to var stimulus_number
    stimulus_number = test_order[test_trial%num_test]
    
    #assign the stimuli to variables that are used in the blocks
    title = title_item[stimulus_number]
    colour = cue_colour[stimulus_number]
    moral_cond = moral_cond_item[stimulus_number]
    
    
    #for debug purposes
    #print test_order
    
    #Add data to data file
    thisExp.addData("title", title)
    thisExp.addData("colour", colour)
    thisExp.addData("morality", moral_cond)
    
    thisExp.addData('test_trial', test_trial)
    thisExp.addData('test_order', test_order)
    thisExp.addData('stimulus_number', stimulus_number)
    
    #incrememnt the current test item counter
    test_trial = test_trial+1
    # keep track of which components have finished
    Test_CodeComponents = []
    for thisComponent in Test_CodeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Test_Code"-------
    while continueRoutine:
        # get current time
        t = Test_CodeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_CodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_Code"-------
    for thisComponent in Test_CodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "Test_Code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Think_No_Think"-------
    t = 0
    Think_No_ThinkClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.600000)
    # update component parameters for each repeat
    title_cue.setColor(colour, colorSpace='rgb')
    title_cue.setText(title)
    # keep track of which components have finished
    Think_No_ThinkComponents = [Fixation, ISI, title_cue]
    for thisComponent in Think_No_ThinkComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Think_No_Think"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Think_No_ThinkClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if t >= 0.4 and Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation.tStart = t
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.setAutoDraw(True)
        frameRemains = 0.4 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation.status == STARTED and t >= frameRemains:
            Fixation.setAutoDraw(False)
        
        # *title_cue* updates
        if t >= 0.6 and title_cue.status == NOT_STARTED:
            # keep track of start time/frame for later
            title_cue.tStart = t
            title_cue.frameNStart = frameN  # exact frame index
            title_cue.setAutoDraw(True)
        frameRemains = 0.6 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if title_cue.status == STARTED and t >= frameRemains:
            title_cue.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.4)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Think_No_ThinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Think_No_Think"-------
    for thisComponent in Think_No_ThinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Intrusions"-------
    t = 0
    IntrusionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.600000)
    # update component parameters for each repeat
    Intrusion_response = event.BuilderKeyResponse()
    # keep track of which components have finished
    IntrusionsComponents = [Intrusion_Rating, Intrusion_response]
    for thisComponent in IntrusionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Intrusions"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = IntrusionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Intrusion_Rating* updates
        if t >= 0.1 and Intrusion_Rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            Intrusion_Rating.tStart = t
            Intrusion_Rating.frameNStart = frameN  # exact frame index
            Intrusion_Rating.setAutoDraw(True)
        frameRemains = 0.1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Intrusion_Rating.status == STARTED and t >= frameRemains:
            Intrusion_Rating.setAutoDraw(False)
        
        # *Intrusion_response* updates
        if t >= 0.1 and Intrusion_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Intrusion_response.tStart = t
            Intrusion_response.frameNStart = frameN  # exact frame index
            Intrusion_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Intrusion_response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Intrusion_response.status == STARTED and t >= frameRemains:
            Intrusion_response.status = STOPPED
        if Intrusion_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Intrusion_response.keys = theseKeys[-1]  # just the last key pressed
                Intrusion_response.rt = Intrusion_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IntrusionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Intrusions"-------
    for thisComponent in IntrusionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Intrusion_response.keys in ['', [], None]:  # No response was made
        Intrusion_response.keys=None
    TNT_loop.addData('Intrusion_response.keys',Intrusion_response.keys)
    if Intrusion_response.keys != None:  # we had a response
        TNT_loop.addData('Intrusion_response.rt', Intrusion_response.rt)
    
    # ------Prepare to start Routine "Break_questionnaire"-------
    t = 0
    Break_questionnaireClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Break_q_resp = event.BuilderKeyResponse()
    mycount1=mycount1+1
    # keep track of which components have finished
    Break_questionnaireComponents = [Break_q, Break_q_resp]
    for thisComponent in Break_questionnaireComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Break_questionnaire"-------
    while continueRoutine:
        # get current time
        t = Break_questionnaireClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Break_q* updates
        if t >= 0.0 and Break_q.status == NOT_STARTED:
            # keep track of start time/frame for later
            Break_q.tStart = t
            Break_q.frameNStart = frameN  # exact frame index
            Break_q.setAutoDraw(True)
        
        # *Break_q_resp* updates
        if t >= 0.0 and Break_q_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Break_q_resp.tStart = t
            Break_q_resp.frameNStart = frameN  # exact frame index
            Break_q_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Break_q_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if Break_q_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Break_q_resp.keys = theseKeys[-1]  # just the last key pressed
                Break_q_resp.rt = Break_q_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        if mycount1 != 144:
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Break_questionnaireComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Break_questionnaire"-------
    for thisComponent in Break_questionnaireComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Break_q_resp.keys in ['', [], None]:  # No response was made
        Break_q_resp.keys=None
    TNT_loop.addData('Break_q_resp.keys',Break_q_resp.keys)
    if Break_q_resp.keys != None:  # we had a response
        TNT_loop.addData('Break_q_resp.rt', Break_q_resp.rt)
    
    # the Routine "Break_questionnaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Break"-------
    t = 0
    BreakClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Break_resp = event.BuilderKeyResponse()
    mycount=mycount+1
    # keep track of which components have finished
    BreakComponents = [Break_Instr, Break_resp]
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Break"-------
    while continueRoutine:
        # get current time
        t = BreakClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Break_Instr* updates
        if t >= 0.0 and Break_Instr.status == NOT_STARTED:
            # keep track of start time/frame for later
            Break_Instr.tStart = t
            Break_Instr.frameNStart = frameN  # exact frame index
            Break_Instr.setAutoDraw(True)
        
        # *Break_resp* updates
        if t >= 0.0 and Break_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Break_resp.tStart = t
            Break_resp.frameNStart = frameN  # exact frame index
            Break_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if Break_resp.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        if mycount==144:
            continueRoutine = False
        elif mycount==240: 
            continueRoutine = False
        elif mycount%48!=0:
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Break"-------
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed num_test_trials repeats of 'TNT_loop'

# get names of stimulus parameters
if TNT_loop.trialList in ([], [None], None):
    params = []
else:
    params = TNT_loop.trialList[0].keys()
# save data for this loop
TNT_loop.saveAsExcel(filename + '.xlsx', sheetName='TNT_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
End_Response = event.BuilderKeyResponse()
# keep track of which components have finished
EndComponents = [END_, End_Response]
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *END_* updates
    if t >= 0.0 and END_.status == NOT_STARTED:
        # keep track of start time/frame for later
        END_.tStart = t
        END_.frameNStart = frameN  # exact frame index
        END_.setAutoDraw(True)
    
    # *End_Response* updates
    if t >= 0.0 and End_Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        End_Response.tStart = t
        End_Response.frameNStart = frameN  # exact frame index
        End_Response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if End_Response.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()







# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
