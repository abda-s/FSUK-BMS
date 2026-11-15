# Altium script failures (symptom -> cause -> fix). Append new ones.

1. Group move doubled child primitives -> unfiltered iterator returns component children -> eIterateFirstLevel or a type filter.
2. `if (a) and (b.Text...)` wedged -> no short-circuit -> nest ifs.
3. TStringList.AddObject with interfaces crashed -> unsupported -> handle objects one at a time.
4. "Undeclared Obj6" -> only Obj1..Obj5.
5. "Undeclared FontManager" -> not global; SchServer.FontManager lacks GetFontID -> copy FontID from an existing label.
6. Stopped at `List1.Clear` -> List1 is nil -> `List1 := TStringList.Create`.
7. Crash building ResultText -> integer concatenated -> IntToStr.
8. "Undeclared SchIterator_Create" -> `.Harness` doc in DM_LogicalDocuments gave nil -> skip non-.SchDoc, check nil.
9. New wires compiled as unconnected -> stale compile -> DoFileSave, WorkspaceManager:Compile; if still stale, restart Altium.
10. "No EMF on clipboard" -> copy ran on another document -> Client.ShowDocument first.
11. Region move missed a port -> port bbox wider than drawn -> move by name or widen region.
12. Part ended off its wire -> user moved it during the script -> re-read coordinates right before modifying; report mismatches.
13. "Never started" after a crash -> paused script/dialog -> REditScript:Stop, ping, user clicks OK.
14. MasterEntryLocation and get_output_job_containers crash: never use.
15. Keyword grep of .SchDoc missed text -> parse OLE FileHeader records.
16. "Connection closed" -> transport drop -> ping, resend.
17. Harness-type warning remained -> Top sheet entries carry HarnessType too -> set connector, port and entry.
18. No-ERC (any symbol, SuppressAll) does not clear "Nets with no driving source" (crystal nets) -> leave the warning.
19. Off-grid bulk snap broke D3/SW1/T1 -> EasyEDA symbols have off-grid pin pitch; wires snapped separately -> diff pin->net before/after; skip or hand-fix such parts.
20. Harness connector resize -> "Invalid connection"/"Unconnected entry" -> toggle each entry's DistanceFromTop, save, compile.
21. Python with regex backrefs written through a shell heredoc turned `\1` into a control char -> use the Write/Edit tool or `chr(92)`.
22. Wedged executor that survives `-REditScript:Stop` (even `ResultText := 'ping'` comes back "never started" / `executor_wedged: true`, and `dialogs_dismissed` may already be 1) -> a **modal dialog is open** in Altium. A runtime error in the last script leaves an error message box, or the script debugger is paused at the crash line. `-REditScript:Stop` (command line) stops a *running* script but does **not** close a modal dialog, so retrying the tool just keeps failing. Fix: ask the user to click OK / press Ctrl+F3 (debugger Stop), or restart Altium. Do not keep re-running scripts in a loop.
23. Reading notes off a sheet crashed and left the #22 dialog -> text frames are `eTextFrame` (text in `.Text`) and standalone labels are `eLabel` (text in `.Text`); iterate each with its own `MkSet(...)`. Keep it to `.Text` only: the note-dump script that died built `MkSet(eTextFrame, eNote, eLabel)` and read `.ObjectId`/`.Location` off the returned objects. After any "did not finish", check the Altium window for a dialog before retrying.
