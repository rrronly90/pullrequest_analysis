import datetime

key_path='credentials.json'
keypathlocal='/Users/rawat/Downloads/credentials.json'
project_id="linen-compiler-351008"
datasetid="github_pr"
tableid="pull_request"
repo_owner="rrronly90"
repo_name="casestudy1"

schema_pr = {
"action":str,
"number":int,
"url":str,
"id":int,
"node_id":str,
"html_url":str,
"diff_url":str,
"patch_url":str,
"issue_url":str,
"state":str,
"locked":bool,
"title":str,
"body":str,
"created_at":str,
"updated_at":datetime,
"closed_at":str,
"merged_at":str,
"merge_commit_sha":str,
"assignee":str,
"milestone":str,
"draft":bool,
"commits_url":str,
"review_comments_url":str,
"review_comment_url":str,
"comments_url":str,
"statuses_url":str,
"author_association":str,
"auto_merge":str,
"active_lock_reason":str,
"merged":bool,
"mergeable":str,
"rebaseable":str,
"mergeable_state":str,
"comments":int,
"review_comments":int,
"maintainer_can_modify":bool,
"commits":int,
"additions":int,
"deletions":int,
"changed_files":int
}

