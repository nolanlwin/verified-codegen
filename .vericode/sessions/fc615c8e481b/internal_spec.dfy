function SlackResponseStyleSpec(has_slack_thread_context: bool): seq<string>
  decreases 0
{
  if has_slack_thread_context then
    ["slack_response_style"]
  else
    []
}

method SlackResponseStyle(has_slack_thread_context: bool) returns (result: seq<string>)
  requires true
  ensures result == SlackResponseStyleSpec(has_slack_thread_context)
{
  assume false;
}
