function SlackResponseStyleSpec(slack_thread_context: bool): seq<string>
{
  []
}

method SlackResponseStyle(slack_thread_context: bool) returns (result: seq<string>)
  ensures result == SlackResponseStyleSpec(slack_thread_context)
{
  if slack_thread_context {
    result := [SLACK_RESPONSE_STYLE_PROMPT];
  } else {
    result := [];
  }
}
