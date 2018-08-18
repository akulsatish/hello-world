#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on May 24, 2018, at 15:52
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
expName = 'Study_Recall_Phases_final'  # from the Builder filename that created this script
expInfo = {u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\work\\Akul\\Intrusions study PsychoPy program v2\\Study_Recall_Phases_final.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1200), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Initialise_code"
Initialise_codeClock = core.Clock()
import xlrd

#store the excel spreadsheet of the participant data in variable infile

infile = 'Participants_Data/'+expInfo['participant']+'.xlsx'

#number of items in feedback phase

num_fback = 14

#number of reps you want in fback phase
num_fback_reps = 1

#number of total trials in fback phase
num_fback_trials = num_fback*num_fback_reps

# Initialize components for Routine "Study_Instr"
Study_InstrClock = core.Clock()
Instr = visual.TextStim(win=win, name='Instr',
    text='Phase I begins now.\n\nPress any key to continue. ',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Study_Phase"
Study_PhaseClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Title_cue = visual.TextStim(win=win, name='Title_cue',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Feedback_Begins"
Feedback_BeginsClock = core.Clock()
FBack_ = visual.TextStim(win=win, name='FBack_',
    text='Phase 2 begins now.\n\nPress any key to continue.',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "FBack_code"
FBack_codeClock = core.Clock()
#create a list of the order in which to show feedback items
fback_order = range(num_fback)

#current test trial
fback_trial = 0

# Initialize components for Routine "Fback_Phase_Cue"
Fback_Phase_CueClock = core.Clock()
ISI_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
Fixation_ = visual.TextStim(win=win, name='Fixation_',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
Title_cues = visual.TextStim(win=win, name='Title_cues',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Fback_Phase_Response"
Fback_Phase_ResponseClock = core.Clock()
Recall_Instr = visual.TextStim(win=win, name='Recall_Instr',
    text='Remember the event related to the word phrase and talk about it out loud. \n\nTry to answer these three questions:\nWho/what was involved?\nWhat were your actions?\n\nYou have 60 seconds',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Feedback_text = visual.TextStim(win=win, name='Feedback_text',
    text='The experimenter will give you a sheet with the correct answer.\n\nPress the space bar when you have read the sheet and are ready to move on. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Pass_"
Pass_Clock = core.Clock()
Continue_ = visual.TextStim(win=win, name='Continue_',
    text='Please wait for the experimenter.\n\nY/N',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "End"
EndClock = core.Clock()
End_ = visual.TextStim(win=win, name='End_',
    text='You may take a break now if you wish to. \n\nPlease wait for the experimenter. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Initialise_code"-------
t = 0
Initialise_codeClock.reset()  # clock
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
for rowx in range(1,num_fback+1):

    row = insheet.row_values(rowx) #assign all column values for each row to arrayed variable "row"
    
    #print out the value of column A and B for debugging
    #print row[0]+' '+row[1]+" "+row[3]

    title_ar.append(row[0])
    moral_cond.append(row[1])

#create a stimulus order list according to pre-determined pseudo-random list
stim_order = [7, 4, 13, 10, 8, 3, 5, 11, 1, 6, 2, 0, 9, 12] 

#arrays for our final stimuli
title_item = []
moral_cond_item = []

#create in final stimulus list
for i in range(num_fback):
    
    #assign an item from the list of items
    title_item.append(title_ar[stim_order[i]])
    moral_cond_item.append(moral_cond[stim_order[i]])

    
    #user output for debug purposes
    #print "item #" + str(i) + ": " + category_item[i] + " " + title_item[i]+ " "+ moral_cond_item[i]


# keep track of which components have finished
Initialise_codeComponents = []
for thisComponent in Initialise_codeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Initialise_code"-------
while continueRoutine:
    # get current time
    t = Initialise_codeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Initialise_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Initialise_code"-------
for thisComponent in Initialise_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Initialise_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Study_Instr"-------
t = 0
Study_InstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Instr_Resp = event.BuilderKeyResponse()
# keep track of which components have finished
Study_InstrComponents = [Instr, Instr_Resp]
for thisComponent in Study_InstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Study_Instr"-------
while continueRoutine:
    # get current time
    t = Study_InstrClock.getTime()
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
        win.callOnFlip(Instr_Resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if Instr_Resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Instr_Resp.keys = theseKeys[-1]  # just the last key pressed
            Instr_Resp.rt = Instr_Resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Study_InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Study_Instr"-------
for thisComponent in Study_InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Instr_Resp.keys in ['', [], None]:  # No response was made
    Instr_Resp.keys=None
thisExp.addData('Instr_Resp.keys',Instr_Resp.keys)
if Instr_Resp.keys != None:  # we had a response
    thisExp.addData('Instr_Resp.rt', Instr_Resp.rt)
thisExp.nextEntry()
# the Routine "Study_Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
StudyPhase_loops = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(infile),
    seed=None, name='StudyPhase_loops')
thisExp.addLoop(StudyPhase_loops)  # add the loop to the experiment
thisStudyPhase_loop = StudyPhase_loops.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudyPhase_loop.rgb)
if thisStudyPhase_loop != None:
    for paramName in thisStudyPhase_loop.keys():
        exec(paramName + '= thisStudyPhase_loop.' + paramName)

for thisStudyPhase_loop in StudyPhase_loops:
    currentLoop = StudyPhase_loops
    # abbreviate parameter names if possible (e.g. rgb = thisStudyPhase_loop.rgb)
    if thisStudyPhase_loop != None:
        for paramName in thisStudyPhase_loop.keys():
            exec(paramName + '= thisStudyPhase_loop.' + paramName)
    
    # ------Prepare to start Routine "Study_Phase"-------
    t = 0
    Study_PhaseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(60.700000)
    # update component parameters for each repeat
    Title_cue.setText(title)
    Cue_advance = event.BuilderKeyResponse()
    # keep track of which components have finished
    Study_PhaseComponents = [Fixation, ISI, Title_cue, Cue_advance]
    for thisComponent in Study_PhaseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Study_Phase"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Study_PhaseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if t >= 0.5 and Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation.tStart = t
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.setAutoDraw(True)
        frameRemains = 0.5 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation.status == STARTED and t >= frameRemains:
            Fixation.setAutoDraw(False)
        
        # *Title_cue* updates
        if t >= 0.7 and Title_cue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Title_cue.tStart = t
            Title_cue.frameNStart = frameN  # exact frame index
            Title_cue.setAutoDraw(True)
        frameRemains = 0.7 + 60.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Title_cue.status == STARTED and t >= frameRemains:
            Title_cue.setAutoDraw(False)
        
        # *Cue_advance* updates
        if t >= 0.7 and Cue_advance.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cue_advance.tStart = t
            Cue_advance.frameNStart = frameN  # exact frame index
            Cue_advance.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Cue_advance.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.7 + 60.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Cue_advance.status == STARTED and t >= frameRemains:
            Cue_advance.status = STOPPED
        if Cue_advance.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Cue_advance.keys = theseKeys[-1]  # just the last key pressed
                Cue_advance.rt = Cue_advance.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Study_PhaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Study_Phase"-------
    for thisComponent in Study_PhaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Cue_advance.keys in ['', [], None]:  # No response was made
        Cue_advance.keys=None
    StudyPhase_loops.addData('Cue_advance.keys',Cue_advance.keys)
    if Cue_advance.keys != None:  # we had a response
        StudyPhase_loops.addData('Cue_advance.rt', Cue_advance.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'StudyPhase_loops'


# ------Prepare to start Routine "Feedback_Begins"-------
t = 0
Feedback_BeginsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Fback_response = event.BuilderKeyResponse()
# keep track of which components have finished
Feedback_BeginsComponents = [FBack_, Fback_response]
for thisComponent in Feedback_BeginsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Feedback_Begins"-------
while continueRoutine:
    # get current time
    t = Feedback_BeginsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FBack_* updates
    if t >= 0.0 and FBack_.status == NOT_STARTED:
        # keep track of start time/frame for later
        FBack_.tStart = t
        FBack_.frameNStart = frameN  # exact frame index
        FBack_.setAutoDraw(True)
    
    # *Fback_response* updates
    if t >= 0.0 and Fback_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        Fback_response.tStart = t
        Fback_response.frameNStart = frameN  # exact frame index
        Fback_response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Fback_response.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if Fback_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Fback_response.keys = theseKeys[-1]  # just the last key pressed
            Fback_response.rt = Fback_response.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Feedback_BeginsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Feedback_Begins"-------
for thisComponent in Feedback_BeginsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Fback_response.keys in ['', [], None]:  # No response was made
    Fback_response.keys=None
thisExp.addData('Fback_response.keys',Fback_response.keys)
if Fback_response.keys != None:  # we had a response
    thisExp.addData('Fback_response.rt', Fback_response.rt)
thisExp.nextEntry()
# the Routine "Feedback_Begins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Continue_Loop = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Continue_Loop')
thisExp.addLoop(Continue_Loop)  # add the loop to the experiment
thisContinue_Loop = Continue_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisContinue_Loop.rgb)
if thisContinue_Loop != None:
    for paramName in thisContinue_Loop.keys():
        exec(paramName + '= thisContinue_Loop.' + paramName)

for thisContinue_Loop in Continue_Loop:
    currentLoop = Continue_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisContinue_Loop.rgb)
    if thisContinue_Loop != None:
        for paramName in thisContinue_Loop.keys():
            exec(paramName + '= thisContinue_Loop.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    FBack_loop = data.TrialHandler(nReps=num_fback_trials, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='FBack_loop')
    thisExp.addLoop(FBack_loop)  # add the loop to the experiment
    thisFBack_loop = FBack_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFBack_loop.rgb)
    if thisFBack_loop != None:
        for paramName in thisFBack_loop.keys():
            exec(paramName + '= thisFBack_loop.' + paramName)
    
    for thisFBack_loop in FBack_loop:
        currentLoop = FBack_loop
        # abbreviate parameter names if possible (e.g. rgb = thisFBack_loop.rgb)
        if thisFBack_loop != None:
            for paramName in thisFBack_loop.keys():
                exec(paramName + '= thisFBack_loop.' + paramName)
        
        # ------Prepare to start Routine "FBack_code"-------
        t = 0
        FBack_codeClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        #assign the stimuli to variables that are used in the blocks
        title = title_item[fback_order[fback_trial%num_fback]]
        
        #for debug purposes
        #print fback_order
        
        #Add data to data file
        thisExp.addData("title", title)
        
        thisExp.addData('fback_trial', fback_trial)
        thisExp.addData('fback_order', fback_order)
        
        #incrememnt the current test item counter
        fback_trial = fback_trial+1
        # keep track of which components have finished
        FBack_codeComponents = []
        for thisComponent in FBack_codeComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "FBack_code"-------
        while continueRoutine:
            # get current time
            t = FBack_codeClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FBack_codeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FBack_code"-------
        for thisComponent in FBack_codeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "FBack_code" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Fback_Phase_Cue"-------
        t = 0
        Fback_Phase_CueClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.500000)
        # update component parameters for each repeat
        Title_cues.setText(title)
        Cue_response = event.BuilderKeyResponse()
        # keep track of which components have finished
        Fback_Phase_CueComponents = [ISI_2, Fixation_, Title_cues, Cue_response]
        for thisComponent in Fback_Phase_CueComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Fback_Phase_Cue"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Fback_Phase_CueClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation_* updates
            if t >= 0.3 and Fixation_.status == NOT_STARTED:
                # keep track of start time/frame for later
                Fixation_.tStart = t
                Fixation_.frameNStart = frameN  # exact frame index
                Fixation_.setAutoDraw(True)
            frameRemains = 0.3 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Fixation_.status == STARTED and t >= frameRemains:
                Fixation_.setAutoDraw(False)
            
            # *Title_cues* updates
            if t >= 0.5 and Title_cues.status == NOT_STARTED:
                # keep track of start time/frame for later
                Title_cues.tStart = t
                Title_cues.frameNStart = frameN  # exact frame index
                Title_cues.setAutoDraw(True)
            frameRemains = 0.5 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Title_cues.status == STARTED and t >= frameRemains:
                Title_cues.setAutoDraw(False)
            
            # *Cue_response* updates
            if t >= 0.5 and Cue_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                Cue_response.tStart = t
                Cue_response.frameNStart = frameN  # exact frame index
                Cue_response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Cue_response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.5 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Cue_response.status == STARTED and t >= frameRemains:
                Cue_response.status = STOPPED
            if Cue_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Cue_response.keys = theseKeys[-1]  # just the last key pressed
                    Cue_response.rt = Cue_response.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            # *ISI_2* period
            if t >= 0.0 and ISI_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_2.tStart = t
                ISI_2.frameNStart = frameN  # exact frame index
                ISI_2.start(0.3)
            elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
                ISI_2.complete()  # finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fback_Phase_CueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Fback_Phase_Cue"-------
        for thisComponent in Fback_Phase_CueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Cue_response.keys in ['', [], None]:  # No response was made
            Cue_response.keys=None
        FBack_loop.addData('Cue_response.keys',Cue_response.keys)
        if Cue_response.keys != None:  # we had a response
            FBack_loop.addData('Cue_response.rt', Cue_response.rt)
        
        # ------Prepare to start Routine "Fback_Phase_Response"-------
        t = 0
        Fback_Phase_ResponseClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        Recall_Instr_resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        Fback_Phase_ResponseComponents = [Recall_Instr, Recall_Instr_resp]
        for thisComponent in Fback_Phase_ResponseComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Fback_Phase_Response"-------
        while continueRoutine:
            # get current time
            t = Fback_Phase_ResponseClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Recall_Instr* updates
            if t >= 0.0 and Recall_Instr.status == NOT_STARTED:
                # keep track of start time/frame for later
                Recall_Instr.tStart = t
                Recall_Instr.frameNStart = frameN  # exact frame index
                Recall_Instr.setAutoDraw(True)
            frameRemains = 0.0 + 60.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Recall_Instr.status == STARTED and t >= frameRemains:
                Recall_Instr.setAutoDraw(False)
            
            # *Recall_Instr_resp* updates
            if t >= 0.0 and Recall_Instr_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                Recall_Instr_resp.tStart = t
                Recall_Instr_resp.frameNStart = frameN  # exact frame index
                Recall_Instr_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Recall_Instr_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if Recall_Instr_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Recall_Instr_resp.keys = theseKeys[-1]  # just the last key pressed
                    Recall_Instr_resp.rt = Recall_Instr_resp.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fback_Phase_ResponseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Fback_Phase_Response"-------
        for thisComponent in Fback_Phase_ResponseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Recall_Instr_resp.keys in ['', [], None]:  # No response was made
            Recall_Instr_resp.keys=None
        FBack_loop.addData('Recall_Instr_resp.keys',Recall_Instr_resp.keys)
        if Recall_Instr_resp.keys != None:  # we had a response
            FBack_loop.addData('Recall_Instr_resp.rt', Recall_Instr_resp.rt)
        # the Routine "Fback_Phase_Response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback"-------
        t = 0
        FeedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        Feedback_resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        FeedbackComponents = [Feedback_text, Feedback_resp]
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Feedback"-------
        while continueRoutine:
            # get current time
            t = FeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Feedback_text* updates
            if t >= 0.0 and Feedback_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                Feedback_text.tStart = t
                Feedback_text.frameNStart = frameN  # exact frame index
                Feedback_text.setAutoDraw(True)
            
            # *Feedback_resp* updates
            if t >= 0.0 and Feedback_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                Feedback_resp.tStart = t
                Feedback_resp.frameNStart = frameN  # exact frame index
                Feedback_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Feedback_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if Feedback_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Feedback_resp.keys = theseKeys[-1]  # just the last key pressed
                    Feedback_resp.rt = Feedback_resp.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Feedback_resp.keys in ['', [], None]:  # No response was made
            Feedback_resp.keys=None
        FBack_loop.addData('Feedback_resp.keys',Feedback_resp.keys)
        if Feedback_resp.keys != None:  # we had a response
            FBack_loop.addData('Feedback_resp.rt', Feedback_resp.rt)
        # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed num_fback_trials repeats of 'FBack_loop'
    
    
    # ------Prepare to start Routine "Pass_"-------
    t = 0
    Pass_Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Continue_Resp = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    Pass_Components = [Continue_, Continue_Resp]
    for thisComponent in Pass_Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Pass_"-------
    while continueRoutine:
        # get current time
        t = Pass_Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Continue_* updates
        if t >= 0.0 and Continue_.status == NOT_STARTED:
            # keep track of start time/frame for later
            Continue_.tStart = t
            Continue_.frameNStart = frameN  # exact frame index
            Continue_.setAutoDraw(True)
        
        # *Continue_Resp* updates
        if t >= 0.0 and Continue_Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Continue_Resp.tStart = t
            Continue_Resp.frameNStart = frameN  # exact frame index
            Continue_Resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Continue_Resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if Continue_Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Continue_Resp.keys = theseKeys[-1]  # just the last key pressed
                Continue_Resp.rt = Continue_Resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pass_Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pass_"-------
    for thisComponent in Pass_Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Continue_Resp.keys in ['', [], None]:  # No response was made
        Continue_Resp.keys=None
    Continue_Loop.addData('Continue_Resp.keys',Continue_Resp.keys)
    if Continue_Resp.keys != None:  # we had a response
        Continue_Loop.addData('Continue_Resp.rt', Continue_Resp.rt)
    if Continue_Resp.keys == 'y':
        Continue_Loop.finished = True;
    # the Routine "Pass_" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'Continue_Loop'


# ------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
End_resp = event.BuilderKeyResponse()
# keep track of which components have finished
EndComponents = [End_, End_resp]
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *End_* updates
    if t >= 0.0 and End_.status == NOT_STARTED:
        # keep track of start time/frame for later
        End_.tStart = t
        End_.frameNStart = frameN  # exact frame index
        End_.setAutoDraw(True)
    
    # *End_resp* updates
    if t >= 0.0 and End_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        End_resp.tStart = t
        End_resp.frameNStart = frameN  # exact frame index
        End_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(End_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if End_resp.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            End_resp.keys = theseKeys[-1]  # just the last key pressed
            End_resp.rt = End_resp.clock.getTime()
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
# check responses
if End_resp.keys in ['', [], None]:  # No response was made
    End_resp.keys=None
thisExp.addData('End_resp.keys',End_resp.keys)
if End_resp.keys != None:  # we had a response
    thisExp.addData('End_resp.rt', End_resp.rt)
thisExp.nextEntry()
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
