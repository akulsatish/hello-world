%% Script to create a structure of all data for morality and think/no-think

clear
clc

%Assign paths for intrusion data(path1) and subj data(path2) and create
%filenames

%Office paths
%path1 = 'C:\Users\as2307\Dropbox\PhD\Experiment files\Experiment 1 Year 1\Results & Data Analysis\Final Experiment 1 Data\Matlab!!\Final versionsIntrusions Data';
%path2 = 'C:\Users\as2307\Dropbox\PhD\Experiment files\Experiment 1 Year 1\Results & Data Analysis\Final Experiment 1 Data\Matlab!!\Final versions\Subjective Data1\';

%Home paths
path1 = '/Users/akulsatish/Dropbox/PhD/Experiment 1 Year 1/Results & Data Analysis/Final Experiment 1 Data/Matlab!!/Final versions/Intrusions Data';
path2 = '/Users/akulsatish/Dropbox/PhD/Experiment 1 Year 1/Results & Data Analysis/Final Experiment 1 Data/Matlab!!/Final versions/Subjective Data';

filename1 = 'Day1_SubjData.xlsx';
filename2 = 'Day2_SubjData.xlsx';

files = dir(fullfile(path1, '*.xlsx'));

%Create structure 'participant' to store all your data so that it is one
%place and you can analyse it
participant = struct();
participant.ID = [];
participant.age = [];
participant.gender = [];
participant.subjdata_t1 = [];
participant.subjdata_t2 = [];


%% Import psychopy data (.xlsx only) and write this data into structure called 'participants'

for indx=1:numel(files)           %Loop through all files in the folder (see path)
    
    %Create a raw data structure called intr_data_raw and import all data into this structure
    [~,~,intr_data_raw] = xlsread(fullfile(path1, files(indx).name), 'U32:AN271');
    
    %Import only the columns you want from the raw data file and store into
    %structure intr_data
    intr_data = [intr_data_raw(:,1), intr_data_raw(:,2), intr_data_raw(:,8),...
        intr_data_raw(:,9),intr_data_raw(:,10),intr_data_raw(:,11),intr_data_raw(:,14),...
        intr_data_raw(:,20)];
    
    %Clear the raw data file from memory for faster processing
    clear intr_data_raw
    
    participant(indx).ID = intr_data(1,8);
    participant(indx).intrusions_data = intr_data;  
    
    clear intr_data
    
    participant(indx).titles = unique(participant(indx).intrusions_data(:,1));
    
    %Create logical indices to determine the condition each trial belongs to
    NTW_indx = strcmp(participant(indx).intrusions_data(:,2),'red')&strcmp(participant(indx).intrusions_data(:,5),'Wrong');
    NTR_indx = strcmp(participant(indx).intrusions_data(:,2),'red')&strcmp(participant(indx).intrusions_data(:,5),'Right');
    TW_indx = strcmp(participant(indx).intrusions_data(:,2),'green')&strcmp(participant(indx).intrusions_data(:,5),'Wrong');
    TR_indx = strcmp(participant(indx).intrusions_data(:,2),'green')&strcmp(participant(indx).intrusions_data(:,5),'Right');
       
    %Create new cells with all the trials that belong to each condition
    participant(indx).NTW_trials = participant(indx).intrusions_data(NTW_indx,:);
    participant(indx).NTR_trials = participant(indx).intrusions_data(NTR_indx,:);
    participant(indx).TW_trials = participant(indx).intrusions_data(TW_indx,:);
    participant(indx).TR_trials = participant(indx).intrusions_data(TR_indx,:);
    
    
    
end
%clear all variables that take up memory
clear indx
clear NTW_indx
clear TW_indx
clear TR_indx
clear NTR_indx

%% Import Day 1 subjective reports (.xlsx only) to structure participants

[~,~,subjdata_t1_raw] = xlsread(fullfile(path2,filename1),'A1:NX13');
    
%Loop through all participants
for r_indx=1:length(participant)
     
    %Create a variable match_ID1 that will identify the rows in your raw
    %data set that correspond to IDs in participant as determined by
    %the psychopy data file
    match_ID1 = find(strcmp(participant(r_indx).ID,subjdata_t1_raw(:,4)));
    
    %Now import data into participant by using match_ID1 as the participant ID
    participant(r_indx).age = cell2mat(subjdata_t1_raw(match_ID1,1));       %Age
    participant(r_indx).gender = cell2mat(subjdata_t1_raw(match_ID1,2));    %Gender
 
    %Raw qualtrics file is not usable - so make each row one memory
        for c_indx=5:32:length(subjdata_t1_raw(1,:))
        participant(r_indx).subjdata_t1 = [participant(r_indx).subjdata_t1; subjdata_t1_raw(match_ID1,c_indx:31+c_indx)];
        end
    
    %Delete unnecessary columns
    participant(r_indx).subjdata_t1(:,2:5) = [];
   
    %Sort data based on titles descending so you can assign mem_ID to this
    %and match with titles in condition which has automatically sorted for
    %you
    participant(r_indx).subjdata_t1_TEMP = participant(r_indx).subjdata_t1;
    participant(r_indx).subjdata_t1 = sortrows(participant(r_indx).subjdata_t1,2);

    %Find indices for different variables
    NTW_indx2 = ismember(participant(r_indx).titles(:,1),unique(participant(r_indx).NTW_trials(:,1)));
    NTR_indx2 = ismember(participant(r_indx).titles(:,1),(unique(participant(r_indx).NTR_trials(:,1))));
    TW_indx2 = ismember(participant(r_indx).titles(:,1),(unique(participant(r_indx).TW_trials(:,1))));
    TR_indx2 = ismember(participant(r_indx).titles(:,1),(unique(participant(r_indx).TR_trials(:,1))));
    
    %Create new fields with data from your conditiosn
    participant(r_indx).subjdata_t1_NTW = participant(r_indx).subjdata_t1(NTW_indx2,:);
    participant(r_indx).subjdata_t1_NTR = participant(r_indx).subjdata_t1(NTR_indx2,:);
    participant(r_indx).subjdata_t1_TW = participant(r_indx).subjdata_t1(TW_indx2,:);
    participant(r_indx).subjdata_t1_TR = participant(r_indx).subjdata_t1(TR_indx2,:);
    
end
clear subjdata_t1_raw    
clear r_indx
clear c_indx
clear match_ID1
    
%% Import Day 2 subjective data      
    
[~,~,subjdata_t2_raw] = xlsread(fullfile(path2,filename2));
    
    %Index(column) numbers for different variables
    
    for r_indx=1:length(participant)
        
        match_ID2 = strcmp(participant(r_indx).ID,subjdata_t2_raw(:,1));
        %participant(r_indx).subjdata2 = subjdata_t2_raw(match_ID2,:);
    
        %participant(r_indx).subjdata_t2 = subjdata_t2_raw(1,2:32);
        for c_indx=2:31:length(subjdata_t2_raw(1,:))
            participant(r_indx).subjdata_t2 = [participant(r_indx).subjdata_t2; subjdata_t2_raw(match_ID2,c_indx:31+(c_indx-1))];
        end
    
    %Add titles to this dataset 
    participant(r_indx).subjdata_t2(:,2)=participant(r_indx).subjdata_t1_TEMP(:,2);
    
    participant(r_indx).subjdata_t2 = sortrows(participant(r_indx).subjdata_t2, 2);
    
    %Delete unnecessary columns     
    participant(r_indx).subjdata_t2(:,3:5) = []; 
   
    %Do the same division of memories as for subjdata_t1
    NTW_indx2 = ismember(participant(r_indx).titles(:,1),unique(participant(r_indx).NTW_trials(:,1)));
    NTR_indx2 = ismember(participant(r_indx).titles(:,1),(unique(participant(r_indx).NTR_trials(:,1))));
    TW_indx2 = ismember(participant(r_indx).titles(:,1),(unique(participant(r_indx).TW_trials(:,1))));
    TR_indx2 = ismember(participant(r_indx).titles(:,1),(unique(participant(r_indx).TR_trials(:,1))));
    
    participant(r_indx).subjdata_t2_NTW = participant(r_indx).subjdata_t2(NTW_indx2,:);
    participant(r_indx).subjdata_t2_NTR = participant(r_indx).subjdata_t2(NTR_indx2,:);
    participant(r_indx).subjdata_t2_TW = participant(r_indx).subjdata_t2(TW_indx2,:);
    participant(r_indx).subjdata_t2_TR = participant(r_indx).subjdata_t2(TR_indx2,:);
    
    end
    
clear subjdata_t2_raw
clear NTW_indx2
clear NTR_indx2
clear TW_indx2
clear TR_indx2
clear match_ID2
clear r_indx
clear c_indx

save ParticipantsData.mat participant;





