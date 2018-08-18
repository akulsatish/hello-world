%% Script to analyse participants data and create a .cvs file to continue further analysis
clc
clear


%%%%!!!IF YOU DO NOT HAVE A MATLAB STRUCTURE CALLED PARTICIPANT THEN UNCOMMENT THE CODE BELOW!!!%%%%%%
%run('Create_structure.m')

%IF NOT: Load data created from previous script
load('ParticipantsData.mat')

%Initialise tables to write to and output .cvs files
MotherTable_intr = table();

%Number of blocks in total
no_blocks_total = 20;

%Number of blocks to analyse
block_gap = 1;

%% Intrusions data analysis - blockwise

for indx=1:length(participant)
        
        for b=1:block_gap:no_blocks_total
    
        blocks_id = find(cell2mat(participant(indx).NTW_trials(:,7))== b);
        blocks_id2 = find(cell2mat(participant(indx).NTR_trials(:,7))== b);
        blocks_id3 = find(cell2mat(participant(indx).TW_trials(:,7))== b);
        blocks_id4 = find(cell2mat(participant(indx).TR_trials(:,7))== b);
        temp = participant(indx).intrusions_data(blocks_id,:);
        
        NTW_IntrResp = str2double(string(participant(indx).NTW_trials(blocks_id,3)));
        NTR_IntrResp = str2double(string(participant(indx).NTR_trials(blocks_id2,3)));
        TW_IntrResp = str2double(string(participant(indx).TW_trials(blocks_id3,3)));
        TR_IntrResp = str2double(string(participant(indx).TR_trials(blocks_id4,3)));
      
        Perc_Never_NTW =  sum(NTW_IntrResp==1)/numel(NTW_IntrResp);
        Perc_Never_NTR = sum(NTR_IntrResp==1)/numel(NTR_IntrResp);
        Perc_Never_TW =  sum(TW_IntrResp==1)/numel(TW_IntrResp);
        Perc_Never_TR = sum(TR_IntrResp==1)/numel(TW_IntrResp);
    
        Perc_Briefly_NTW =  sum(NTW_IntrResp==2)/numel(NTW_IntrResp);
        Perc_Briefly_NTR = sum(NTR_IntrResp==2)/numel(NTR_IntrResp);
        Perc_Briefly_TW =  sum(TW_IntrResp==2)/numel(TW_IntrResp);
        Perc_Briefly_TR = sum(TR_IntrResp==2)/numel(TW_IntrResp);
    
        Perc_Often_NTW =  sum(NTW_IntrResp==3)/numel(NTW_IntrResp);
        Perc_Often_NTR = sum(NTR_IntrResp==3)/numel(NTR_IntrResp);
        Perc_Often_TW =  sum(TW_IntrResp==3)/numel(TW_IntrResp);
        Perc_Often_TR = sum(TR_IntrResp==3)/numel(TW_IntrResp);
   
        Perc_Missing_NTW =  sum(isnan(NTW_IntrResp))/numel(NTW_IntrResp);
        Perc_Missing_NTR = sum(isnan(NTR_IntrResp))/numel(NTR_IntrResp);
        Perc_Missing_TW =  sum(isnan(TW_IntrResp))/numel(TW_IntrResp);
        Perc_Missing_TR = sum(isnan(TR_IntrResp))/numel(TW_IntrResp);
    
   
    
        participant_analysis_data = [participant(indx).ID, participant(indx).age, participant(indx).gender, b,...
            Perc_Never_TR, Perc_Briefly_TR, Perc_Often_TR, Perc_Missing_TR,...
            Perc_Never_TW, Perc_Briefly_TW, Perc_Often_TW, Perc_Missing_TW,...
            Perc_Never_NTR, Perc_Briefly_NTR, Perc_Often_NTR, Perc_Missing_NTR,...
            Perc_Never_NTW, Perc_Briefly_NTW, Perc_Often_NTW, Perc_Missing_NTW];
          
    
    participant(indx).intrusions_analysis = participant_analysis_data;
    
    %After all calculations, add the averages for this participant to a row of table "MotherTable_intr"
    MotherTable_intr = [MotherTable_intr; indx, participant_analysis_data];
     
        end
    
end 

clearvars -except participant MotherTable_intr;


%% Intrusions analysis - overall

MotherTable_intr_blocks = table();

for indx=1:length(participant)        
    
        temp = participant(indx).intrusions_data;
        
        %Create variables with the intrusion responses for your different
        %conditions
        NTW_IntrResp = str2double(string(participant(indx).NTW_trials(:,3)));
        NTR_IntrResp = str2double(string(participant(indx).NTR_trials(:,3)));
        TW_IntrResp = str2double(string(participant(indx).TW_trials(:,3)));
        TR_IntrResp = str2double(string(participant(indx).TR_trials(:,3)));
      
        Perc_Never_NTW =  sum(NTW_IntrResp==1)/numel(NTW_IntrResp);
        Perc_Never_NTR = sum(NTR_IntrResp==1)/numel(NTR_IntrResp);
        Perc_Never_TW =  sum(TW_IntrResp==1)/numel(TW_IntrResp);
        Perc_Never_TR = sum(TR_IntrResp==1)/numel(TW_IntrResp);
    
        Perc_Briefly_NTW =  sum(NTW_IntrResp==2)/numel(NTW_IntrResp);
        Perc_Briefly_NTR = sum(NTR_IntrResp==2)/numel(NTR_IntrResp);
        Perc_Briefly_TW =  sum(TW_IntrResp==2)/numel(TW_IntrResp);
        Perc_Briefly_TR = sum(TR_IntrResp==2)/numel(TW_IntrResp);
    
        Perc_Often_NTW =  sum(NTW_IntrResp==3)/numel(NTW_IntrResp);
        Perc_Often_NTR = sum(NTR_IntrResp==3)/numel(NTR_IntrResp);
        Perc_Often_TW =  sum(TW_IntrResp==3)/numel(TW_IntrResp);
        Perc_Often_TR = sum(TR_IntrResp==3)/numel(TW_IntrResp);
   
        Perc_Missing_NTW =  sum(isnan(NTW_IntrResp))/numel(NTW_IntrResp);
        Perc_Missing_NTR = sum(isnan(NTR_IntrResp))/numel(NTR_IntrResp);
        Perc_Missing_TW =  sum(isnan(TW_IntrResp))/numel(TW_IntrResp);
        Perc_Missing_TR = sum(isnan(TR_IntrResp))/numel(TW_IntrResp);
    
    
        participant_analysis_data = [participant(indx).ID, participant(indx).age, participant(indx).gender,...
            Perc_Never_TR, Perc_Briefly_TR, Perc_Often_TR, Perc_Missing_TR,...
            Perc_Never_TW, Perc_Briefly_TW, Perc_Often_TW, Perc_Missing_TW,...
            Perc_Never_NTR, Perc_Briefly_NTR, Perc_Often_NTR, Perc_Missing_NTR,...
            Perc_Never_NTW, Perc_Briefly_NTW, Perc_Often_NTW, Perc_Missing_NTW];
    
        
    participant(indx).intrusions_analysis = participant_analysis_data;
        
    MotherTable_intr_blocks  = [MotherTable_intr_blocks; indx, participant_analysis_data];
      
   
    
end 


%% Subjective Data Analysis

for indx=1:length(participant)

    %CALCULATE AVERAGE MEMORY AGE ACROSS CONDITIONS FOR TIME 1
    
    Avg_Ratings_TR_t1(:,1)= sum(str2double(string(participant(indx).subjdata_t1_TR(:,3))))/...
        numel(str2double(string(participant(indx).subjdata_t1_TR(:,3))));
    Avg_Ratings_TW_t1(:,1)= sum(str2double(string(participant(indx).subjdata_t1_TW(:,3))))/...
        numel(str2double(string(participant(indx).subjdata_t1_TW(:,3))));
    Avg_Ratings_NTR_t1(:,1)= sum(str2double(string(participant(indx).subjdata_t1_NTR(:,3))))/...
        numel(str2double(string(participant(indx).subjdata_t1_NTR(:,3))));
    Avg_Ratings_NTW_t1(:,1)= sum(str2double(string(participant(indx).subjdata_t1_NTW(:,3))))/...
        numel(str2double(string(participant(indx).subjdata_t1_NTW(:,3))));
    
    %CALCULATE AVERAGES FOR ALL OTHER MEASURES FOR TIME 1
    
        for c=5:28
            Avg_Ratings_TR_t1(:,c-3) = sum(str2double(string(participant(indx).subjdata_t1_TR(:,c))))/...
                numel(str2double(string(participant(indx).subjdata_t1_TR(:,c)))); 
        
            Avg_Ratings_TW_t1(:,c-3)= sum(str2double(string(participant(indx).subjdata_t1_TW(:,c))))/...
                numel(str2double(string(participant(indx).subjdata_t1_TW(:,c))));
       
            Avg_Ratings_NTR_t1(:,c-3)= sum(str2double(string(participant(indx).subjdata_t1_NTR(:,c))))/...
                numel(str2double(string(participant(indx).subjdata_t1_NTR(:,c))));
        
            Avg_Ratings_NTW_t1(:,c-3)= sum(str2double(string(participant(indx).subjdata_t1_NTW(:,c))))/...
                numel(str2double(string(participant(indx).subjdata_t1_NTW(:,c))));
    
        end
    
    %%%%%CALCULATE AVERAGE MEMORY AGE ACROSS CONDITIONS FOR TIME 2%%%%%
    
    Avg_Ratings_TR_t2(:,1)= sum(str2double(string(participant(indx).subjdata_t2_TR(:,3))))/...
        numel(str2double(string(participant(indx).subjdata_t2_TR(:,3))));
    Avg_Ratings_TW_t2(:,1)= sum(str2double(string(participant(indx).subjdata_t2_TW(:,3))))/...
        numel(str2double(string(participant(indx).subjdata_t2_TW(:,3))));
    Avg_Ratings_NTR_t2(:,1)= sum(str2double(string(participant(indx).subjdata_t2_NTR(:,3))))/...
        numel(str2double(string(participant(indx).subjdata_t2_NTR(:,3))));
    Avg_Ratings_NTW_t2(:,1)= sum(str2double(string(participant(indx).subjdata_t2_NTW(:,3))))/...
        numel(str2double(string(participant(indx).subjdata_t2_NTW(:,3))));
    
    %CALCULATE AVERAGES FOR ALL OTHER MEASURES FOR TIME 2
    
        for c=5:28
            Avg_Ratings_TR_t2(:,c-3) = sum(str2double(string(participant(indx).subjdata_t2_TR(:,c))))/...
                numel(str2double(string(participant(indx).subjdata_t2_TR(:,c)))); 
        
            Avg_Ratings_TW_t2(:,c-3)= sum(str2double(string(participant(indx).subjdata_t2_TW(:,c))))/...
                numel(str2double(string(participant(indx).subjdata_t2_TW(:,c))));
       
            Avg_Ratings_NTR_t2(:,c-3)= sum(str2double(string(participant(indx).subjdata_t2_NTR(:,c))))/...
                numel(str2double(string(participant(indx).subjdata_t2_NTR(:,c))));
        
            Avg_Ratings_NTW_t2(:,c-3)= sum(str2double(string(participant(indx).subjdata_t2_NTW(:,c))))/...
                numel(str2double(string(participant(indx).subjdata_t2_NTW(:,c))));
        end
        
    subjective_analysis_t1 = [Avg_Ratings_TR_t1, Avg_Ratings_TW_t1,...
         Avg_Ratings_NTR_t1, Avg_Ratings_NTW_t1];
    subjective_analysis_t2 = [Avg_Ratings_TR_t2, Avg_Ratings_TW_t2,...
         Avg_Ratings_NTR_t2, Avg_Ratings_NTW_t2];
     
    participant(indx).subjective_analysis_t1 = num2cell(subjective_analysis_t1);
    participant(indx).subjective_analysis_t2 = num2cell(subjective_analysis_t2);
        
end   

%% Create new tables to write subjective data
MotherTable_subj_t1 = table();
MotherTable_subj_t2 = table();

for indx=1:length(participant)
   MotherTable_subj_t1 = [MotherTable_subj_t1; participant(indx).ID, participant(indx).subjective_analysis_t1];
   MotherTable_subj_t2 = [MotherTable_subj_t2; participant(indx).ID, participant(indx).subjective_analysis_t2];
end

%% OutPut files for SPSS

%Analysis data for intrusions
MotherTable_intr.Properties.VariableNames = {'PNo','Participant_ID','Age','Gender','Block_No',...
        'TR_Never', 'TR_Briefly', 'TR_Often', 'TR_Missing',...
        'TW_Never', 'TW_Briefly', 'TW_Often', 'TW_Missing',...
        'NTR_Never', 'NTR_Briefly', 'NTR_Often', 'NTR_Missing',...
        'NTW_Never', 'NTW_Briefly', 'NTW_Often', 'NTW_Missing'};

MotherTable_intr_blocks.Properties.VariableNames = {'PNo','Participant_ID','Age','Gender',...
        'TR_Never', 'TR_Briefly', 'TR_Often', 'TR_Missing',...
        'TW_Never', 'TW_Briefly', 'TW_Often', 'TW_Missing',...
        'NTR_Never', 'NTR_Briefly', 'NTR_Often', 'NTR_Missing',...
        'NTW_Never', 'NTW_Briefly', 'NTW_Often', 'NTW_Missing'};

%Analysis data for subjective data

MotherTable_subj_t1.Properties.VariableNames = {'Participant_ID',...
    'Age_TR_t1','Viv_TR_t1','Morality_TR_t1','Interested_TR_t1','Distressed_TR_t1','Excited_TR_t1','Upset_TR_t1',...
    'Strong_TR_t1', 'Guilty_TR_t1','Scared_TR_t1','Hostile_TR_t1', 'Enthusiastic_TR_t1', 'Proud_TR_t1', 'Irritable_TR_t1',...
    'Alert_TR_t1', 'Ashamed_TR_t1','Inspired_TR_t1', 'Nervous_TR_t1',	'Determined_TR_t1',	'Attentive_TR_t1',...
    'Jittery_TR_t1', 'Active_TR_t1', 'Afraid_TR_t1', 'Pleasure_TR_t1', 'Arousal_TR_t1',...
    'Age_TW_t1','Viv_TW_t1','Morality_TW_t1','Interested_TW_t1','Distressed_TW_t1','Excited_TW_t1','Upset_TW_t1',...
    'Strong_TW_t1', 'Guilty_TW_t1','Scared_TW_t1','Hostile_TW_t1', 'Enthusiastic_TW_t1', 'Proud_TW_t1', 'Irritable_TW_t1',...
    'Alert_TW_t1', 'Ashamed_TW_t1','Inspired_TW_t1', 'Nervous_TW_t1',	'Determined_TW_t1',	'Attentive_TW_t1',...
    'Jittery_TW_t1', 'Active_TW_t1', 'Afraid_TW_t1', 'Pleasure_TW_t1', 'Arousal_TW_t1',...
    'Age_NTR_t1','Viv_NTR_t1','Morality_NTR_t1','Interested_NTR_t1','Distressed_NTR_t1','Excited_NTR_t1','Upset_NTR_t1',...
    'Strong_NTR_t1', 'Guilty_NTR_t1','Scared_NTR_t1','Hostile_NTR_t1', 'Enthusiastic_NTR_t1', 'Proud_NTR_t1', 'Irritable_NTR_t1',...
    'Alert_NTR_t1', 'Ashamed_NTR_t1','Inspired_NTR_t1', 'Nervous_NTR_t1',	'Determined_NTR_t1',	'Attentive_NTR_t1',...
    'Jittery_NTR_t1', 'Active_NTR_t1', 'Afraid_NTR_t1', 'Pleasure_NTR_t1', 'Arousal_NTR_t1',...
    'Age_NTW_t1','Viv_NTW_t1','Morality_NTW_t1','Interested_NTW_t1','Distressed_NTW_t1','Excited_NTW_t1','Upset_NTW_t1',...
    'Strong_NTW_t1', 'Guilty_NTW_t1','Scared_NTW_t1','Hostile_NTW_t1', 'Enthusiastic_NTW_t1', 'Proud_NTW_t1', 'Irritable_NTW_t1',...
    'Alert_NTW_t1', 'Ashamed_NTW_t1','Inspired_nTW_t1', 'Nervous_NTW_t1',	'Determined_NTW_t1',	'Attentive_NTW_t1',...
    'Jittery_NTW_t1', 'Active_NTW_t1', 'Afraid_NTW_t1', 'Pleasure_NTW_t1', 'Arousal_NTW_t1'};

MotherTable_subj_t2.Properties.VariableNames = {'Participant_ID',...
    'Age_TR_t2','Viv_TR_t2','Morality_TR_t2','Interested_TR_t2','Distressed_TR_t2','Excited_TR_t2','Upset_TR_t2',...
    'Strong_TR_t2', 'Guilty_TR_t2','Scared_TR_t2','Hostile_TR_t2', 'Enthusiastic_TR_t2', 'Proud_TR_t2', 'Irritable_TR_t2',...
    'Alert_TR_t2', 'Ashamed_TR_t2','Inspired_TR_t2', 'Nervous_TR_t2',	'Determined_TR_t2',	'Attentive_TR_t2',...
    'Jittery_TR_t2', 'Active_TR_t2', 'Afraid_TR_t2', 'Pleasure_TR_t2', 'Arousal_TR_t2',...
    'Age_TW_t2','Viv_TW_t2','Morality_TW_t2','Interested_TW_t2','Distressed_TW_t2','Excited_TW_t2','Upset_TW_t2',...
    'Strong_TW_t2', 'Guilty_TW_t2','Scared_TW_t2','Hostile_TW_t2', 'Enthusiastic_TW_t2', 'Proud_TW_t2', 'Irritable_TW_t2',...
    'Alert_TW_t2', 'Ashamed_TW_t2','Inspired_TW_t2', 'Nervous_TW_t2',	'Determined_TW_t2',	'Attentive_TW_t2',...
    'Jittery_TW_t2', 'Active_TW_t2', 'Afraid_TW_t2', 'Pleasure_TW_t2', 'Arousal_TW_t2',...
    'Age_NTR_t2','Viv_NTR_t2','Morality_NTR_t2','Interested_NTR_t2','Distressed_NTR_t2','Excited_NTR_t2','Upset_NTR_t2',...
    'Strong_NTR_t2', 'Guilty_NTR_t2','Scared_NTR_t2','Hostile_NTR_t2', 'Enthusiastic_NTR_t2', 'Proud_NTR_t2', 'Irritable_NTR_t2',...
    'Alert_NTR_t2', 'Ashamed_NTR_t2','Inspired_NTR_t2', 'Nervous_NTR_t2',	'Determined_NTR_t2',	'Attentive_NTR_t2',...
    'Jittery_NTR_t2', 'Active_NTR_t2', 'Afraid_NTR_t2', 'Pleasure_NTR_t2', 'Arousal_NTR_t2',...
    'Age_NTW_t2','Viv_NTW_t2','Morality_NTW_t2','Interested_NTW_t2','Distressed_NTW_t2','Excited_NTW_t2','Upset_NTW_t2',...
    'Strong_NTW_t2', 'Guilty_NTW_t2','Scared_NTW_t2','Hostile_NTW_t2', 'Enthusiastic_NTW_t2', 'Proud_NTW_t2', 'Irritable_NTW_t2',...
    'Alert_NTW_t2', 'Ashamed_NTW_t2','Inspired_nTW_t2', 'Nervous_NTW_t2',	'Determined_NTW_t2',	'Attentive_NTW_t2',...
    'Jittery_NTW_t2', 'Active_NTW_t2', 'Afraid_NTW_t2', 'Pleasure_NTW_t2', 'Arousal_NTW_t2'};

%Write all your output tables into a csv file for SPSS analysis
writetable(MotherTable_intr, 'Mother Analysis Intrusions_blockwise.csv');
writetable(MotherTable_intr_blocks, 'Mother Analysis Intrusions_combined.csv');
writetable(MotherTable_subj_t1, 'Mother Analysis Subjective T1.csv');
writetable(MotherTable_subj_t2, 'Mother Analysis Subjective T2.csv');


%clearvars -except participant MotherTable_intr MotherTable_subj_t1 MotherTable_subj_t2 MotherTable_intr_2;
