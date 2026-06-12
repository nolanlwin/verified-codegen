function SlackResponseStyleSpec(has_slack_thread_context: bool): seq<string>
  decreases 0
{
  []
}

method SlackResponseStyle(has_slack_thread_context: bool) returns (result: seq<string>)
  ensures result == SlackResponseStyleSpec(has_slack_thread_context)
{
  if has_slack_thread_context {
    result := ["slack_response_style"];
  } else {
    result := [];
  }
}
