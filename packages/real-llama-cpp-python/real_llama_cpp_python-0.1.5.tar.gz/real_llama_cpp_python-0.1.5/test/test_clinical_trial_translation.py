import pandas as pd
from pytrials.client import ClinicalTrials
from sklearn.model_selection import train_test_split
import os
import json
import argparse
import random
import time
import re
os.environ["WANDB_DISABLED"] = "true"
from pytrials.utils import json_handler, csv_handler
from pytrials import study_fields
import csv
import numpy as np
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
from llama_cpp import Llama
from langchain_community.llms import LlamaCpp
from langchain.memory import ConversationTokenBufferMemory
# import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from langchain.chains import LLMChain, ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory, 
                                                  ConversationSummaryBufferMemory,
                                                  ConversationSummaryMemory, 
                                                  ConversationBufferWindowMemory,
                                                  ConversationKGMemory)
from langchain_core.pydantic_v1 import BaseModel,Field
from pydantic.v1 import BaseModel
from langchain_core.utils.function_calling import convert_to_openai_tool
from llama_cpp import Llama
from langchain_community.llms import LlamaCpp
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.pydantic_v1 import BaseModel, Field
# from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain.callbacks.tracers import ConsoleCallbackHandler
from langchain.chains import LLMChain, ConversationChain
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
# from langchain_core.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel, Field, model_validator
from langchain_core.output_parsers import PydanticOutputParser
import json
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from dotenv import dotenv_values

config = dotenv_values(".env")

filtered_trial_df = pd.read_csv(f'/home/minhtran/Projects/clinical_trial_llm_translation/All_active_breast_cancer_trials_filtered_breast_cancer.csv', index_col=0)
filtered_trial_df2 = filtered_trial_df[~filtered_trial_df['Phases'].isna()]
tnm_staging = ''
with open('/home/minhtran/Projects/clinical_trial_llm_translation/input/TNM_staging_for_breast_cancer.txt', 'r') as file:
    for line in file:
        # print(line)
        tnm_staging+= line
actrn_trial_pd=pd.read_csv(f'/home/minhtran/Projects/clinical_trial_llm_translation/input/ANZCTR_trials.csv', index_col=0)
concensus_trials = actrn_trial_pd[(actrn_trial_pd['NCT']!='') & (actrn_trial_pd['ACTRN']!=''  ) & ~actrn_trial_pd['NCT'].isna() & ~actrn_trial_pd['ACTRN'].isna()] 
print(concensus_trials)
class TrialInfor:
    """ClinicalTrials.gov API client

    Provides functions to easily access the ClinicalTrials.gov API
    (https://classic.clinicaltrials.gov/api/)
    in Python.

    Attributes:
        study_fields: List of all study fields you can use in your query.
        api_info: Tuple containing the API version number and the last
        time the database was updated.
    """

    _BASE_URL = "https://clinicaltrials.gov/api/v2/"
    _JSON = "format=json"
    _CSV = "format=csv"
    def __init__(self):
        self.api_info = self.__api_info()

    @property
    def study_fields(self):
        """List of all study fields you can use in your query."""

        csv_fields = []
        json_fields = []
        with open(study_fields, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                csv_fields.append(row["Column Name"])
                json_fields.append(row["Included Data Fields"].split("|"))

        return {
            "csv": csv_fields,
            "json": [item for sublist in json_fields for item in sublist],
        }
    def __api_info(self):
        """Returns information about the API"""
        req = json_handler(f"{self._BASE_URL}version")
        last_updated = req["dataTimestamp"]

        api_version = req["apiVersion"]

        return api_version, last_updated
    def get_study_info(self, study_id):
        req = f"{study_id}"
        handler = json_handler
        full_studies = handler(f"{self._BASE_URL}/studies/{req}")

        return full_studies

###
NSW_CITIES = ['Westmead', 'Camperdown', 'Liverpool',
              'North Ryde','North Sydney', 'Sydney','St Leonards',
             'Wollongong', 'Saint Leonards','Subiaco','Darlinghurst','Waratah' ]

def location_parser(input_location, filter_by='Australia'):
    # Regular expression to match the postcodes
    postcode_pattern = r'\b\d{4}\b|\b\d{5}\b|\b\d{6}\b|\b\d{5}-\d{3}\b|\b\d{2}-\d{3}\b'
    # Split the string by the postcodes and keep the postcodes in the resulting list
    split_string = re.split(f'({postcode_pattern})', input_location)
    
    # Combine the split parts with the postcodes
    loc_res = [re.sub(r'^, |^\-\d{3}, ', '', split_string[i] + split_string[i+1]) for i in range(0, len(split_string) - 1, 2)]
    if filter_by:
        output = list()
        for loc in loc_res:
            if filter_by in loc:
                output.append(loc)
        return output
    else:
        return loc_res

def extract_key_clinical_trial_infor(trial_id, repo='NCT'):
    raw_information = dict()
    if repo=='NCT':
        ct = TrialInfor()
        values = ct.get_study_info(trial_id)
        # rev_values = ct.get_full_studies(search_expr=trial_id, max_studies=1)
        # if len(rev_values) > 1:
        #     # raise Exception(f'Multiple trials found with the id: {trial_id}')
        #     # values = values[-1]
        #     item_names = rev_values[0]
        #     trial_info = rev_values[1]
        #     values = dict(zip(item_names, trial_info))
        # return values
        # else:
        # print(values)
        protocol = values['protocolSection']
        official_title = protocol['identificationModule']['officialTitle']
        org_study_id_title = ''
        if protocol['identificationModule'].get('orgStudyIdInfo'):
            org_study_id_title = protocol['identificationModule']['orgStudyIdInfo']['id']
        phase = ' '.join(protocol['designModule']['phases'])
        brief_title = protocol['identificationModule']['briefTitle']
        trial_status = protocol['statusModule']['overallStatus']
        update_date = protocol['statusModule']['lastUpdatePostDateStruct']['date']
        eligibility = protocol['eligibilityModule']['eligibilityCriteria']
        min_age = protocol['eligibilityModule']['minimumAge']
        gender = protocol['eligibilityModule']['sex']
        brief_summary = protocol['descriptionModule']['briefSummary']
        arms = protocol['armsInterventionsModule']['armGroups']
        conditions = protocol['conditionsModule']['conditions']
        masking_info = protocol['designModule']['designInfo']['maskingInfo']
        is_masked = False
        who_masked = list()
        if masking_info.get('masking') and masking_info.get('whoMasked'):
            print('Enter masking', masking_info)
            is_masked = True
            who_masked.extend(masking_info['whoMasked'])
            
        drugs = list()
        intervention_type = list()
        contained_placebo = False
        for arm in protocol['armsInterventionsModule']['armGroups']:
            # print(arm)
            if arm.get('interventionNames'):
                drugs.extend(arm['interventionNames'])
            if arm.get('type'):
                intervention_type.append(arm['type'])
        locations = protocol['contactsLocationsModule']['locations']
        sponsor = protocol['sponsorCollaboratorsModule']['leadSponsor']
        loc_facilities = list()
        au_locations = list()
        postcodes = list()

        if len(locations) >= 1:
            for loc in locations:
#                     print(loc)
                if loc['country'] == 'Australia' : # and loc['LocationState']=='New South Wales':
    #                 print(loc.get('LocationState'))
                    au_locations.append(loc)

                    if loc.get('zip') and loc['zip'].startswith('2'):
                        postcodes.append(loc['zip'])
                    if loc.get('state') == 'New South Wales':
                        loc_facilities.append(loc['facility'])
                    elif loc.get('city') in NSW_CITIES:
                        loc_facilities.append(loc['facility'])
        detail_summary = ''
        if protocol['descriptionModule'].get('detailedDescription'):
            detail_summary = protocol['descriptionModule']['detailedDescription']
        if protocol['identificationModule'].get('acronym'):
            short_name = protocol['identificationModule']['acronym']
        else:
            short_name = protocol['identificationModule']['orgStudyIdInfo']['id']
        if len(drugs):
            for drug in drugs:
                tmp_drug_str = re.sub('Drug:\s', '', drug)
                if 'placebo' in tmp_drug_str.lower():
                    contained_placebo = True
        raw_information = {'ClinicalTrials.gov':trial_id, 
                           'Short Name':short_name,
                           'Official Title':official_title,
                           'Conditions':conditions,
                           'Eligibility Criteria':eligibility,
                           'Eligible Gender':gender, 
                           'Sponsor':sponsor,
                           'Detailed Summary':detail_summary,
                           'Brief Summary':brief_summary,
                           'Trial Status':trial_status,
                           'Arms':arms,
                           'Phase':phase,
                           'Drugs': list(set(drugs)),
                           'Intervention Type':list(set(intervention_type)),
                           'Last Updated':update_date,
                           'Has Placebo':contained_placebo,
                           'Minimum Age':min_age,
                           'Locations':loc_facilities, 
                           'Postcodes (NSW)':postcodes,
                           'Who Masked': who_masked}
    elif repo=='ACTRN':
        pass
    else:
        raise Exception(f'Trial repo:{repo} is not supported')
    return raw_information
### Main information extraction
def extract_prompt_response(response):
    pattern1 = r"Here is my lay-person explanation as an oncologist:(.*)" 
    input_value = response.strip()
    match = re.search(pattern1, input_value, re.DOTALL)
    # print(match.group(0))
    if match:
        clean_res = match.group(1)
        # print(f"Clean response: {clean_res}")
        # print(f"Scientific Title: {scientific_title}")
        return clean_res
    else:
        return input_value

def extract_stat(input_text):
    # Regular expression pattern
    pattern1 = r"Final Answer: (.*)"
    # Extracting titles
    match1 = re.search(pattern1, input_text)
    print(match1.group(0))
    if match1:
        drugs = match1.group(1)
        return drugs
    else:
        return input_text
###
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='The script that performs OCR on pdf files and export json output.')
    
    # Add arguments
    parser.add_argument('-m', '--model', type=str, help='Model name')
    parser.add_argument('-mu', '--model-url', type=str, help='model download url')
    parser.add_argument('-drug_db', '--drug-database-file', type=str, help='Database for cancer intervention')
    parser.add_argument('-std_tm', '--standard-treatment-file', type=str, help='Database for standard Breast cancer for RAG')
    # All_active_breast_cancer_trials_filtered_breast_cancer.csv
    parser.add_argument('-idx', '--trial-index', type=int, help='Index for the requesting clinical trial')
    args = parser.parse_args()
    # Load LLM models
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    mistral_llm = LlamaCpp(
      model_path=f'{args.model_url}/{args.model}',  # Download the model file first
        temperature=0.,
        max_tokens=1500,n_ctx=5000,
        n_gpu_layers=40,
        top_p=1,
        n_batch=512,
        callback_manager=callback_manager,
        verbose=True,  # Verbose is required to pass to the callback manager
    )
    gpt_model = ChatOpenAI(model="gpt-4o",
                           temperature=0,
                           max_tokens=1500, 
                           api_key=config['OPENAI_API_KEY'])
    drug_db = pd.read_csv(f'{args.drug_database_file}', sep='\t', on_bad_lines='warn')
    expand_drug_db = drug_db.assign(**{'drug_class':drug_db['drug_class'].str.split(',')})
    expand_drug_db = expand_drug_db.explode(['drug_class'])
    expand_drug_db.reset_index(inplace=True, drop='index')
    ###
    oncology_template2 =  """ ### [INST]  You act as an expert in oncolgy and answer to the request to the using lay-person language 
        Think rationally before providing the final answer.
        Step 1: You analyze provided context to identify medical jargon from the context. However, you should keep the specific treatment name, drug or test to remain the accurary and fidelity. 
        Step 2: Construct the response to the human request by rephrasing the scientific information and medical jargons into easy-to-understand words. \n
        Step 3: Your should briefly go through each item in the list of eligibilities and explain the medical meaning of its.
        Step 4: Start the final answer with: 'Here is my lay-person explanation as an oncologist:' \n
         [/INST]
        """

    oncology_prompt2 = ChatPromptTemplate.from_messages(
        [
            ("system", oncology_template2),
             ("placeholder", "{chat_history}"),
            ("human", "{input}"),
        ]
    )
    # onco_qa_chain = create_stuff_documents_chain(mistral_llm, oncology_prompt)
    # onco_rag_chain = create_retrieval_chain(tmp_retriever, onco_qa_chain)
    oncologist_chain = oncology_prompt2 | mistral_llm
    oncologist_chain2 = oncology_prompt2 | gpt_model
    chat_history_for_onco_chain = ChatMessageHistory()
    
    oncologist_chain_with_mem = RunnableWithMessageHistory(
        oncologist_chain,
        lambda session_id: chat_history_for_onco_chain,
        input_messages_key="input",
        history_messages_key="chat_history",
    )
    def summarize_messages(chain_input):
        stored_messages = chat_history_for_onco_chain.messages
        if len(stored_messages) == 0:
            return False
        summarization_prompt = ChatPromptTemplate.from_messages(
            [
                MessagesPlaceholder(variable_name="chat_history"),
                (
                    "user",
                    "Distill the above chat messages to a paragraph with less than 200 words. Include as many specific details as you can.",
                ),
            ]
        )
        summarization_chain = summarization_prompt | gpt_model
    
        summary_message = summarization_chain.invoke({"chat_history": stored_messages})
    
        chat_history_for_onco_chain.clear()
    
        chat_history_for_onco_chain.add_message(summary_message)
    
        return True
    
    
    oncologist_chain_with_sum = (
        RunnablePassthrough.assign(messages_summarized=summarize_messages)
        | oncologist_chain_with_mem
    )
    oncologist_chain_with_sum2 = (
        RunnablePassthrough.assign(messages_summarized=summarize_messages)
        | oncologist_chain_with_mem
    )
    general_chain = (PromptTemplate.from_template("""Given the user question below, you perform the task asked by request.
                {input}.
                You think radically before produce the final answer following the step below: 
                Step 1: Identify if the request is about information extraction or classification task. Perform either case 1 or case 2 and omit the remaining.
                    Case 1: If the task is information extraction, you extract the specific information and do not elaborate on the answer. 
                    Case 2: If the task is about classification, you strictly select an option from the list of options in request.
                Step 2: You provide the final answer after considering all the cases and fulfilling all the request from input.
                
            """
        )
        | mistral_llm
        | StrOutputParser()
    )

    general_chain2 = (PromptTemplate.from_template( """Given the user question below, you perform the task asked by request.
                {input}.
                You think radically before produce the final answer following the step below: 
                Step 1: Identify if the request is about information extraction or classification task. Perform either case 1 or case 2 and omit the remaining.
                    Case 1: If the task is information extraction, you extract the specific information and do not elaborate on the answer. 
                    Case 2: If the task is about classification, you strictly select an option from the list of options in request.
                Step 2: You provide the final answer after considering all the cases and fulfilling all the request from input.
                
            """
        )
        | gpt_model
        | StrOutputParser()
    )
    standard_treatments = pd.read_csv(f'{args.standard_treatment_file}')
    standard_treatments.drop(columns=['Source','Added by ', 'Approved by '], inplace=True)

    
    standard_treatments_json = standard_treatments.to_dict(orient='records')
    
    documents = []
    for element in standard_treatments_json:
        tmp_doc = Document(page_content=json.dumps(element, indent=4), metadata={"source": "self-curated"})
        
        documents.append(tmp_doc)
    
    # Chunk text
    text_splitter = CharacterTextSplitter(chunk_size=275, separator="\n",
                                          chunk_overlap=10)
    chunked_documents = text_splitter.split_documents(documents)
    list_of_common_subtype= ''''PARP Inhibitor ',
                            'CDK4/6 (kinease) Inhibitor',
                             'mTOR Inhibitor',
                             'PD-L1 inhibitor',
                             'CTLA-4 inhibitor',
                             'Antibody Drug Conjugate',
                             'Estrogen receptor antagonist',
                             'Selective Estrogen receptor modulator (SERM)',
                             'Aromatase Inhibitor',
                             'gonadotropin-releasing hormone (GnRH) agonist',
                             'monoclonal antibody',
                             'Anthracycline',
                             'Mitotic Inhibitor',
                             'Alkylating Agent',
                             'Taxane',
                             'Anti-metabolite',
                             'Vinca Alkaloid',
                             'Antineoplastic',
                             'Tyrosine Kinease inhibitor',
                             'PIK3K Inhibitor'   '''
    
    db = FAISS.from_documents(chunked_documents, HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"score_threshold": .66,"k": 5})

    treatment_chain = PromptTemplate.from_template("""
            ### [INST] 
            Instruction: Answer the question based on your knowledge about breast cancer treatment. 
            Think rationally before providing the final answer following these steps. 
            Step 1: Check if the question is within the known treatments. 
            Here is a known treatments to help with the response:\n 
            {context} 
            Step 2: If the answer to Step 1 is Yes, construct the response to the question by searching the context. Otherwise, construct your answer based on the provided context in the question. \n
            ### QUESTION:
            {question}            
            [/INST] """
    ) | mistral_llm
    rag_treatment_chain = ( 
     {"context": retriever, "question": RunnablePassthrough()}
        | treatment_chain
        | StrOutputParser()
    )
    editor_prompt = ChatPromptTemplate.from_messages([ ('system', """You are an editor, you take the title from a medical trial and rewrite it in layman language while preserving the main content. \
    Given one scientific title you would reply with a rephrased `public title` with the main goal is to enhance clarity and accessibility to general public. 
    You think radically following the below guidelines:
    1. Start the 'Public title' with the trial's short name and ':' to create the consistency \n \
    2. The 'Public title' should always mention the drug name and specify whether they have other conditions.
    3. You start your answer with: "Here is my public edition:". \n """
    ),
         ("placeholder", "{chat_history}"),
         ("human", "{request_prompt}")])
       
    editor_chain = editor_prompt | gpt_model
    chat_history_for_edit_chain = ChatMessageHistory()
    
    editor_chain_with_mem = RunnableWithMessageHistory(
        editor_chain,
        lambda session_id: chat_history_for_edit_chain,
        input_messages_key="request_prompt",
        history_messages_key="chat_history",
    )

    
    tbn_staging_doc = Document(page_content=tnm_staging, metadata={"source": "TNM_reference"})
    
    # Chunk text
    text_splitter = CharacterTextSplitter(chunk_size=500, separator="\n",
                                          chunk_overlap=75)
    tnm_chunked_doc = text_splitter.split_text(tnm_staging)
    tnm_db = FAISS.from_texts(tnm_chunked_doc, HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
    tnm_retriever = tnm_db.as_retriever(search_type="similarity", search_kwargs={"score_threshold": .66,"k": 5})
    tnm_chain = PromptTemplate.from_template(
    """
        ### [INST] 
        Instruction: Answer the question based on your knowledge about breast cancer TNM staging. 
        Think rationally before providing the final answer following these steps. 
        Step 1: Check if the question is within the knowledge. 
        Here is a known context to help with the response:\n 
        {context} 
        Step 2: Construct the response to the question by searching the context. \n
        ### QUESTION:
        {question} 
        
        [/INST] """
    ) | gpt_model
    rag_tnm_chain = ( 
     {"context": tnm_retriever, "question": RunnablePassthrough()}
        | tnm_chain
        | StrOutputParser()
    )
    common_tests= """ ['ATM','BARDi', 'BRCA-1','BRCA-2','BRIPI'
                    'CHEK2','CHH1','MMR','EPCAM','FANCN','MLH1','MSH1','MSH6','MUTYH'
                    'NBN','PMS2','PD-1','PD-L1','PIK3CA','PIK3CB','STK11','TP53','Other']
                    """

    default_placebo= 'Placebo medication is a substance with no therapeutic effect, often used in clinical trials as a control to test the effectiveness of new treatments.'
    
    #### LLM translation of the requested clinical trial
    key = int(args.trial_index)
    chat_history_for_onco_chain.clear()
    eli_text_splitter = CharacterTextSplitter(chunk_size=150, separator="\n",
                                          chunk_overlap=10)
    
    trial_id = filtered_trial_df2.iloc[key]['NCT Number']
    print(trial_id)
    
    new_row = {'ClinicalTrials.gov': {'id':filtered_trial_df2.iloc[key]['NCT Number'], 'href':f'https://clinicaltrials.gov/study/{trial_id}'}}
    if (len(concensus_trials[concensus_trials['NCT']==trial_id]) ==1) : 
        anzctrn_id = concensus_trials[concensus_trials['NCT']==trial_id]['ACTRN'].values[0]
        new_row['ANZCTR.org.au'] = {'id':anzctrn_id, 'href':f'https://www.anzctr.org.au/TrialSearch.aspx?searchTxt={anzctrn_id}'}
        # print(concensus_trials[concensus_trials['NCT']==trial_id])
        # 1/0
    new_row['Other IDs'] = filtered_trial_df2.iloc[key]['Other IDs']
    trial_detail = extract_key_clinical_trial_infor(trial_id)
    tmp_short_name = str(filtered_trial_df2.iloc[key]['Acronym'])
    tmp_official_title = filtered_trial_df2.iloc[key]['Study Title']
    
    new_row['Sponsor'] = trial_detail['Sponsor']['name']
    new_row['Phase'] = trial_detail['Phase']
    new_row['Short Title'] = filtered_trial_df2.iloc[key]['Acronym']
    new_row['Intervention Arms'] = trial_detail['Intervention Type']
    new_row['Trial Status'] = filtered_trial_df2.iloc[0]['Study Status']
    new_row['Last Updated'] = trial_detail['Last Updated']
    new_row['Has Placebo'] = trial_detail['Has Placebo']
    new_row['Minimum Age'] = trial_detail['Minimum Age']
    new_row['Conditions'] = trial_detail['Conditions']
    new_row['Who Masked'] = trial_detail['Who Masked']
    new_row['Eligible Gender'] = filtered_trial_df2.iloc[key]['Sex']
    new_row['Condition Category'] = 'Cancer'
    new_row['Locations'] = filtered_trial_df2.iloc[key]['Locations']
    new_row['Postcodes (NSW)'] = filtered_trial_df2.iloc[key]['Postcode']
    new_row['Study Type'] = filtered_trial_df2.iloc[key]['Study Type']
    tmp_brief_sum = trial_detail['Brief Summary']
    tmp_detail_summary = trial_detail['Detailed Summary']
    
    
    print(type(tmp_short_name))
    print(tmp_short_name=='nan')
    if tmp_short_name!='nan': 
        title_prompt = f'''The trial has a short name is {tmp_short_name}. Can you rewrite the title using layman language: \n {tmp_official_title}? '''
    else:
        title_prompt= f'''Can you rewrite the title using layman language: \n {tmp_official_title}? '''
    print(title_prompt)
    multihead_result1=editor_chain_with_mem.invoke({'request_prompt':title_prompt},
                                                   {'configurable': {'session_id': f'editor_{trial_id}'}})
    title_output = re.sub(r'(Here is my public edition|Public title):','',multihead_result1.content)
    
    new_row['Public Title'] = title_output
    new_row['Scientific Title'] = tmp_official_title
    new_row['Short Title'] = tmp_short_name
    
    
    interventional_drugs_str = general_chain2.invoke({'input':f'Given this brief summary of a breast cancer clinical trial called {tmp_official_title}:\n {tmp_brief_sum} ### REQUEST: What are the investigational drugs in this trial? Start the answer with `Final Answer:` and the list of tr. Do not explain the reason \n'},
                                                             {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    interventional_drugs_str = extract_stat(interventional_drugs_str)
    print(interventional_drugs_str)
    interventional_drugs = [drug.strip()for drug in interventional_drugs_str.split(',')]
    drug_names = list()
    for drug in trial_detail['Drugs']:
        drug_names.append(re.sub('(Drug|Biological):\s', '', drug))
    list_drugs = list()
    for drug_name in drug_names:
        list_drugs.extend([tmp.strip() for tmp in drug_name.split('and')])
    list_drugs = list(set(list_drugs))
    drug_class = dict()    
    for tmp_drug_str in list_drugs:
        print(tmp_drug_str)
        if 'Placebo' in tmp_drug_str:
            drug_class_values = set(expand_drug_db[expand_drug_db['drug'].str.contains(tmp_drug_str)].drug_class.values)
            drug_class[tmp_drug_str] = {'Drug Class':tmp_drug_str, 'Detail': default_placebo}
        else:
            drug_class_values = set(expand_drug_db[expand_drug_db['drug'].str.contains(tmp_drug_str)].drug_class.values)
            if len(drug_class_values):
                # drug_class_prompt = f'Given the list of common drug class: \n{list_of_common_subtype}. Identify the best match for the {drug_class_values}. Only Response with the list of closest drug classes that matched. Do not explain the reason'
                multihead_result2_1 = rag_treatment_chain.invoke(f'Given the drug called {tmp_drug_str} which is the class of {drug_class_values}, Can you  explain what the drug is used for in breast cancer treatment? If there are multiple drugs, provide as much detail as possible and do not explain step by step')
                print(multihead_result2_1, drug_class_values)
                # drug_class_norm = general_chain.invoke({'input': drug_class_prompt}, {'configurable': {'session_id': f'oncologist_{trial_id}'}})
                # print(drug_class_norm)
                drug_class_norm = ', '.join(drug_class_values)
                drug_class[tmp_drug_str] = {'Drug Class':drug_class_norm, 'Detail': re.sub(r'(###.*\n|Answer:)', '',multihead_result2_1).strip()}
            else:
                multihead_result2_1 = rag_treatment_chain.invoke(f'Given the drug called {tmp_drug_str} which is an Unknown drug class, Can you  explain what the drug is used for in breast cancer treatment? If there are multiple drugs, provide as much detail as possible and do not explain step by step')
                print(multihead_result2_1, drug_class_values)
                # drug_class_norm = general_chain.invoke({'input': drug_class_prompt}, {'configurable': {'session_id': f'oncologist_{trial_id}'}})
                # print(drug_class_norm)
                drug_class[tmp_drug_str] = {'Drug Class':'Unknown', 'Detail': re.sub(r'(###.*\n|Answer:)', '',multihead_result2_1).strip()}
        if tmp_drug_str in interventional_drugs:
            drug_class[tmp_drug_str]['Type'] = 'Interventional Drug'
        else:
            drug_class[tmp_drug_str]['Type'] = 'Comparing Drug'
    new_row['Interventions'] = drug_class
    tmp_eligibility= trial_detail['Eligibility Criteria']
    chunked_eligibility = eli_text_splitter.split_text(tmp_eligibility)
    ###
    menopausal_stat = general_chain2.invoke({'input':f'Given this eligibility criteria list of a breast cancer clinical trial {chunked_eligibility} of a clinical trial called {tmp_official_title}. What is Menopausal status required to participate in this trial? Options include: `Not specific` or `Premenopause` or `Perimenopause` or `Postmenopause` or `NA-male`. Only response with the menopausal status. Start the answer with `Final Answer:`. Do not explain the reason'},
                                                             {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    er_stat = general_chain2.invoke({'input':f'A clinical trial called {tmp_official_title} has the eligibility criteria list as follow {chunked_eligibility}. What is the hormone receptor (HR) called ER status (estrogen receptor), required to participate in this trial? Options include: Positive, Negative or Not specific. Start the answer with `Final Answer:`. Do not explain the reason.'},
                                                             {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    pr_stat = general_chain2.invoke({'input':f'A clinical trial called {tmp_official_title} has the eligibility criteria list as follow {chunked_eligibility}. What is hormone receptor (HR) called PR status (progesterone receptor), required to participate in this trial? Options include: Positive, Negative or Not specific. Start the answer with `Final Answer:`. Do not explain the reason. Remember progesterone is a hormone'},
                                                             {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    her2_stat = general_chain2.invoke({'input':f'A clinical trial called {tmp_official_title} has the eligibility criteria list as follow {chunked_eligibility}. What is HER2 (human epidermal growth factor receptor 2) status required to participate in this trial? Options include: Positive, Negative, Low or Not specific. Only response with the HER2 status.  Start the answer with `Final Answer:`. Do not explain the reason'},
                                                             {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    ecog_stat = general_chain2.invoke({'input':f'A clinical trial called {tmp_official_title} has the eligibility criteria list as follow {chunked_eligibility}. What is ECOG status required to participate in this trial? Options include: 0,1,2,3,4 or 5. Just respond with the only ECOG status.  Start the answer with `Final Answer:`. Do not explain the reason'},
                                                             {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    grade_stat = general_chain2.invoke({'input':f'A clinical trial called {tmp_official_title} has the eligibility criteria list as follow {chunked_eligibility}. What is the current grade eligible to participate in or exclude from this trial? Just respond with the eligible cancer grade in numeric value.  Start the answer with `Final Answer:`.  Do not explain the reason'},
                                                             {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    met_stat = rag_tnm_chain.invoke(f'Given this eligibility criteria list of a breast cancer clinical trial {chunked_eligibility}. Answer whether or not this trial accepts participants with metastasised cancer. If yes, identify all the metastasis sites mentioned in a list. Otherwise return an empty list. Start the answer with `Final Answer:`. Do not Explain the reason'  )
    tumour_size = rag_tnm_chain.invoke(f'Given this eligibility criteria list of a breast cancer clinical trial {chunked_eligibility}. What tumour size is eligible to participate in or exclude from this trial? Just respond with either numeric value of tumour size in millimetre or Not specific. Start the answer with `Final Answer:`. Do not explain the reason' )
    lymph_nodes = rag_tnm_chain.invoke(f'Given this eligibility criteria list of a breast cancer clinical trial {chunked_eligibility}. What number of lymph is eligible to participate in or exclude from this trial? Just respond with either the highest number of lymph nodes or Not specific. Start the answer with `Final Answer:`. Do not explain the reason' )
    
    ###
    
    new_row['Menopausal status'] = extract_stat(menopausal_stat)
    new_row['ER status'] = extract_stat(er_stat)
    new_row['PR status'] = extract_stat(pr_stat)
    new_row['HER2 status'] = extract_stat(her2_stat)
    new_row['ECOG status'] = extract_stat(ecog_stat)
    new_row['Number Lymph nodes'] = extract_stat(lymph_nodes)
    
    new_row['Grade status'] = extract_stat(grade_stat)
    
    new_row['Tumour size'] = extract_stat(tumour_size)
    
    new_row['Metastasised sites'] = extract_stat(met_stat)
    genetic_test = general_chain2.invoke({'input':f'Given this eligibility criteria list of a breast cancer clinical trial {chunked_eligibility} of a clinical trial called {tmp_official_title}. Identify the list of prior test for genetic mutations and biomarkers if any mentioned. If no genetic test is mentioned answer None. Some of the common test that may include {common_tests}.Answer in the form of list with each item is a genetic or boimarker test. Remember Do not explain the reason'},
                                                             {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    # print(genetic_test)
    new_row['Genetic tested'] = genetic_test
    prior_treatment = general_chain2.invoke({'input':f'Given this eligibility criteria list of a breast cancer clinical trial {chunked_eligibility}. Identify the list of prior cancer treatments mentioned. Answer in the form of list with each item is type of treatment. Do not explain the reason'},
                                                             {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    # print(prior_treatment)
    new_row['Prior Treatment'] = prior_treatment
    tmp_gender = new_row['Eligible Gender']
    chat_history_for_onco_chain.clear()
    eligi_translated = oncologist_chain_with_mem.invoke({'input':f'Given the eligbility criteria below: {chunked_eligibility}. Additionally, this trial accept participant from {tmp_gender} gender. Can you go through the list of criteria and explain in simple and formal terms as much details as possible the recruitment criteria in bullet points? Avoid using abbreviations, acronyms and medical jargons. However you may recite the name of genetic mutation, biomarker tests, drug names.'},
                                                         {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    new_row['Translated Eligibility Criteria'] = re.sub('(AI|Expert|Oncologist): ', '', extract_prompt_response(eligi_translated)) 
    
    tmp_arm_string = ', '.join([json.dumps(i) for i in trial_detail['Arms']] )
    chat_history_for_onco_chain.clear()
    brief_summary_result3= oncologist_chain_with_mem.invoke({'input':f'This the a summary of a clinical trial related to breast cancer: {tmp_brief_sum}. Can you explain to me this Brief Summary in lay-person language, formal and simple terms?'},
                                                           {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    new_row['Translated Brief Summary'] = re.sub('(AI|Expert|Oncologist): ', '', extract_prompt_response(brief_summary_result3)) 
    chat_history_for_onco_chain.clear()
    infor2explain = f'Brief description: {tmp_brief_sum} \n Arms: {tmp_arm_string} \n Some more detail: {tmp_detail_summary} \n'
    chunked_infor2explain = eli_text_splitter.split_text(infor2explain)
    multihead_chain4 = oncologist_chain_with_mem.invoke({'input':f'This is some information about the clinical trial: \n {chunked_infor2explain}. Explain to me the trial procedure in lay-person language, formal and easy-to-understand words. Provide as much detail as possible without using abbreviation and acronym'},
                                                      {'configurable': {'session_id': f'oncologist_{trial_id}'}})
    new_row['Translated Detailed Description'] = re.sub('(AI|Expert|Oncologist): ','',extract_prompt_response(multihead_chain4 ))
    new_row['Version'] = datetime.now().strftime('%Y-%m-%d-%H:%M')
    j = json.dumps(new_row, indent=4)
    with open(f'{trial_id}.json', 'w') as fp:
        fp.write(j)


