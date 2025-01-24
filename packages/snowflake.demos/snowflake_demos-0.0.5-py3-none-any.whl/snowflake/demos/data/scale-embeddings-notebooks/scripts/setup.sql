USE ROLE ACCOUNTADMIN;
SET USERNAME = (SELECT CURRENT_USER());
SELECT $USERNAME;

-- Using ACCOUNTADMIN, create a new role for this exercise and grant to applicable users
CREATE OR REPLACE ROLE EMBEDDING_MODEL_HOL_USER;
GRANT ROLE EMBEDDING_MODEL_HOL_USER to USER identifier($USERNAME);

-- Next create a new database and schema,
CREATE DATABASE IF NOT EXISTS EMBEDDING_MODEL_HOL_DB;
CREATE SCHEMA IF NOT EXISTS EMBEDDING_MODEL_HOL_SCHEMA;

-- Create network rule and external access integration for pypi to allow users to pip install python packages within notebooks (on container runtimes)
CREATE NETWORK RULE IF NOT EXISTS pypi_network_rule
  MODE = EGRESS
  TYPE = HOST_PORT
  VALUE_LIST = ('pypi.org', 'pypi.python.org', 'pythonhosted.org',  'files.pythonhosted.org');

CREATE EXTERNAL ACCESS INTEGRATION IF NOT EXISTS pypi_access_integration
  ALLOWED_NETWORK_RULES = (pypi_network_rule)
  ENABLED = true;

-- Create network rule and external access integration for users to access data and models from Hugging Face
CREATE OR REPLACE NETWORK RULE hf_network_rule
  MODE = EGRESS
  TYPE = HOST_PORT
  VALUE_LIST = ('huggingface.co', 'www.huggingface.co', 'cdn-lfs.huggingface.co', 'cdn-lfs-us-1.huggingface.co');

CREATE EXTERNAL ACCESS INTEGRATION IF NOT EXISTS hf_access_integration
  ALLOWED_NETWORK_RULES = (hf_network_rule)
  ENABLED = true;

create or replace network rule allow_all_rule
  TYPE = 'HOST_PORT'
  MODE= 'EGRESS'
  VALUE_LIST = ('0.0.0.0:443','0.0.0.0:80');

CREATE OR REPLACE EXTERNAL ACCESS INTEGRATION allow_all_integration
  ALLOWED_NETWORK_RULES = (allow_all_rule)
  ENABLED = true;
  
GRANT USAGE ON INTEGRATION pypi_access_integration TO ROLE EMBEDDING_MODEL_HOL_USER;
GRANT USAGE ON INTEGRATION hf_access_integration TO ROLE EMBEDDING_MODEL_HOL_USER;
GRANT USAGE ON INTEGRATION allow_all_integration TO ROLE EMBEDDING_MODEL_HOL_USER;

-- Create a snowpark optimized virtual warehouse access of a virtual warehouse for newly created role
CREATE OR REPLACE WAREHOUSE EMBEDDING_MODEL_HOL_WAREHOUSE WITH
  WAREHOUSE_SIZE = 'MEDIUM';
  
GRANT USAGE ON WAREHOUSE EMBEDDING_MODEL_HOL_WAREHOUSE to ROLE EMBEDDING_MODEL_HOL_USER;

-- Create compute pool to leverage GPUs (see docs - https://docs.snowflake.com/en/developer-guide/snowpark-container-services/working-with-compute-pool)

CREATE COMPUTE POOL IF NOT EXISTS GPU_NV_S_COMPUTE_POOL
    MIN_NODES = 4
    MAX_NODES = 4
    INSTANCE_FAMILY = GPU_NV_S;

-- Grant usage of compute pool to newly created role
GRANT OWNERSHIP ON COMPUTE POOL GPU_NV_S_COMPUTE_POOL to ROLE EMBEDDING_MODEL_HOL_USER;

-- Grant ownership of database and schema to newly created role
GRANT OWNERSHIP ON DATABASE EMBEDDING_MODEL_HOL_DB TO ROLE EMBEDDING_MODEL_HOL_USER COPY CURRENT GRANTS;
GRANT OWNERSHIP ON ALL SCHEMAS IN DATABASE EMBEDDING_MODEL_HOL_DB  TO ROLE EMBEDDING_MODEL_HOL_USER COPY CURRENT GRANTS;

-- Grant usage back to ACCOUNTADMIN for visibility/usability
GRANT ALL ON DATABASE EMBEDDING_MODEL_HOL_DB TO ROLE ACCOUNTADMIN;
GRANT ALL ON ALL SCHEMAS IN DATABASE EMBEDDING_MODEL_HOL_DB  TO ROLE ACCOUNTADMIN;

-- Create image repository
CREATE IMAGE REPOSITORY IF NOT EXISTS my_inference_images;
GRANT OWNERSHIP ON IMAGE REPOSITORY my_inference_images TO ROLE EMBEDDING_MODEL_HOL_USER;

GRANT BIND SERVICE ENDPOINT ON ACCOUNT TO ROLE EMBEDDING_MODEL_HOL_USER;
