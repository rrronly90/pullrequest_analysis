/* create tale users for storing real time users feeds please change project id and dataset id as required*/
  
create table `linen-compiler-351008.github_pr.users` 
  (login   STRING,
  id  INTEGER,
  node_id   STRING,
  avatar_url   STRING,
  url   STRING,
  html_url   STRING,
  followers_url   STRING,
  following_url   STRING,
  gists_url   STRING,
  starred_url   STRING,
  subscriptions_url   STRING,
  organizations_url   STRING,
  repos_url   STRING,
  events_url   STRING,
  received_events_url   STRING,
  type   STRING,
  site_admin   STRING , 
  action  string , 
  number  integer , 
  pull_id integer , 
  raised_at datetime
  )

partition by date(raised_at ) cluster by action
;

/* create table statement for pull_request real time  for storing real time pr feeds please change project id and dataset id as required */
create or replace table `linen-compiler-351008.github_pr.pull_request` 
(
 action  STRING    ,       
url   STRING         ,
id INTEGER        ,
node_id  STRING      ,  
html_url STRING     ,      
diff_url STRING     ,      
patch_url   STRING     ,      
issue_url   STRING     ,      
state STRING      ,  
locked   BOOLEAN     ,  
title STRING      ,  
body  INTEGER     ,  
created_at  STRING     ,      
updated_at  TIMESTAMP     ,      
closed_at   STRING      ,  
merged_at   STRING      ,  
merge_commit_sha  STRING      ,  
assignee INTEGER        ,
assignees   INTEGER        ,
requested_reviewers  INTEGER    ,      
requested_teams   INTEGER     ,  
labels   INTEGER        ,
milestone   INTEGER     ,  
draft BOOLEAN        ,
commits_url STRING      ,  
review_comments_url  STRING     ,      
review_comment_url   STRING     ,      
comments_url   STRING      ,  
statuses_url   STRING      ,  
author_association   STRING     ,      
auto_merge  INTEGER        ,
active_lock_reason   INTEGER    ,      
merged   BOOLEAN        ,
mergeable   INTEGER     ,  
rebaseable  INTEGER     ,  
mergeable_state   STRING     ,      
comments INTEGER     ,  
review_comments   INTEGER    ,      
maintainer_can_modify   BOOLEAN    ,      
commits  INTEGER        ,
additions   INTEGER     ,  
deletions   INTEGER     ,  
changed_files  INTEGER     

)
partition by date(updated_at ) cluster by action
;




