
-- cases
create table cases( ddl_case_id varchar, year int, state_code varchar(2), dist_code varchar(4), court_no varchar(4), judge_position varchar, female_defendant varchar, female_adv_def varchar, female_adv_pet varchar, type_name varchar, purpose_name varchar, date_of_filing varchar, date_of_decision varchar, date_first_list varchar, date_last_list varchar, date_next_list varchar);

-- judges
create table judges(
  ddl_judge_id varchar(5),
  state_code varchar(2),
  dist_code varchar(2),
  court_no varchar(4),
  judge_position varchar,
  female_judge varchar,
  start_date varchar,
  end_date varchar
);

-- judge_case_merge_key
create table judge_case_merge_key(
  ddl_case_id varchar,
  ddl_filing_judge_id varchar,
  ddl_decision_judge_id varchar
);

-- acts sections
create table acts_sections(
  ddl_case_id varchar,
  act varchar,
  section varchar,
  bailable_ipc varchar,
  number_sections_ipc varchar,
  criminal varchar
);

-- act_key
create table act_key(
  act_s varchar,
  count int,
  act varchar
);

-- section
create table section_key(
  section_s varchar,
  count int,
  section varchar
);

-- ====================

-- disposal name key
create table disp_name_key(
  year int,
  disp_name varchar,
  disp_name_s varchar,
  count int
);

-- purpose name key
create table purpose_name_key(
  year int,
  purpose_name varchar,
  purpose_name_s varchar,
  count int
);

-- type name key
create table type_name_key(
  year int,
  type_name varchar,
  type_name_s varchar,
  count int
);

-- cases_court_key
create table cases_court_key(
  year int,
  state_code varchar(2),
  state_name varchar,
  district_name varchar,
  dist_code varchar(2),
  court_no varchar(4),
  court_name varchar
);
