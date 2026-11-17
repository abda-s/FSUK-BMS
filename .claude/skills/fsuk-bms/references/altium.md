# Altium (AD26) via altium-mcp `run_altium_script`

## The altium-mcp tools (server repo: C:\Users\3adas\.altium-mcp-server\repo)
- Most tools are deferred: load them with ToolSearch (`select:mcp__altium-mcp__run_altium_script,...`) before calling.
- `run_altium_script(script, timeout_seconds)`: main tool. The script body is pasted into `SandboxScript/Sandbox.pas` (procedure Run) and executed in Altium. Set `ResultText` to return text; `SandboxLog('x')` lines show up in `steps`, so the last step tells you where a crash happened. Result fields: `success`, `result`, `steps`, `executor_wedged`, `dialogs_dismissed`. "never started" = compile error or stuck executor; "did not finish" = runtime crash after the last step (an Altium error dialog is probably open).
- `get_screenshot(view_type='sch')`: screenshot of the Altium window (current zoom, low detail). For readable images use the EMF capture below.
- `get_server_status`: check Altium is reachable. Other tools (get_schematic_data, get_component_pins, place_components, get_all_nets, ...) exist, but scripts were more reliable here.
- Don't use: `get_output_job_containers` (crashes). Altium must be open with BMS-Master.PrjPcb focused; ask the user to restart Altium when it hangs.
- Workflow per change: one small read-only script, then the modifying script, then save, compile, check nets (and a capture if the layout changed).

## Setup and recovery
- Altium: `C:\Program Files\Altium\AD26\X2.EXE`. API docs: `C:\Users\3adas\.claude\skills\altium-script\references\` (`SCH_API_Reference.md`, `api\SCH_Interfaces.md`, `api\Constants.md`, `api\Other_Interfaces.md`). Working examples: `C:\Users\3adas\.altium-mcp-server\repo\server\AltiumScript\schematic_utils.pas`.
- Wedged executor ("never started"/"did not finish"): `"C:\Program Files\Altium\AD26\X2.EXE" -REditScript:Stop`, then ping `ResultText := 'ping';`. If a dialog is open ask the user to click OK; else ask for an Altium restart. "Connection closed" = transport drop: ping and resend.
- Never read `MasterEntryLocation`; never call `get_output_job_containers`.

## Sandbox
- Only `S1..S3`, `I1..I3`, `B1` (Integer), `Obj1..Obj5`, `List1` (declared, nil: `List1 := TStringList.Create`), `ResultText` (string). No own vars/functions. `and`/`or` don't short-circuit: nest ifs.
- Numbers into text: `IntToStr`. Records: fixed-width strings + `StrToInt(Trim(Copy(S1, 1, 6)))`. `SandboxLog('step')` before risky lines.
- Coords: `MilsToCoord(mil)`; 1 mil = 10000 units. Ids: Note 2, Rectangle 4, Image 11, TextFrame 13, Wire 19, Label 22, NetLabel 24, Component 26, Parameter 27, ParameterSet 28, NoERC 35, Port 38, PowerObject 39, SheetEntry 40, SheetSymbol 41, HarnessConnector 53, HarnessEntry 54, SignalHarness 56.

## Patterns
- Open: `Obj1 := SchServer.GetSchDocumentByPath(p)`; if nil `Client.OpenDocument('SCH', p)` and get again. Top-level iteration: `SetState_IterationDepth(eIterateFirstLevel)`.
- Modify: `PreProcess(Obj1,'')`, per object `SendMessage(O.I_ObjectAddress, c_BroadCast, SCHM_BeginModify, c_NoEventData)` / `SCHM_EndModify`, `PostProcess`, `GraphicallyInvalidate`.
- Create: `SchObjectFactory(eX, eCreate_GlobalCopy)`, set fields, `Obj1.RegisterSchObjectInContainer(O)`, `SendMessage(Obj1.I_ObjectAddress, c_BroadCast, SCHM_PrimitiveRegistration, O.I_ObjectAddress)`.
  - Wire: `InsertVertex := 1; SetState_Vertex(1, P)` per vertex. GND: `Style 4`, `Orientation 3`, `Text 'GND'`.
  - Dashed box: eRectangle `Location`/`Corner`, `LineStyle eLineStyleDashed`, `IsSolid False`, `Transparent True`, colour `$808080`.
  - Text: eLabel, colour `$800000`; block titles use FontID 5 (copy FontIDs from existing labels; `SchServer.FontManager` has no GetFontID). Print bounding boxes and check overlaps.
  - Diff-pair directive: eParameterSet on the wire + child eParameter `DifferentialPair=True` (`PSet.AddSchObject`). Nets must end `_P`/`_N`.
- Delete: find one, destroy iterator, `Obj1.RemoveSchObject(O)` + registration message; repeat with a max count, never `while <> nil`. In a SchLib symbol RemoveSchObject does nothing: select + `RunProcess('Sch:Clear')` (script-errors #28).
- Move: `MoveByXY` (text follows), `RotateBy90(Location, eRotate90)`. Pin hot end = Location + PinLength along Orientation (0 R, 1 U, 2 L, 3 D).
- Save: `Client.OpenDocument('SCH', p).DoFileSave('')`. Compile: `RunProcess('WorkspaceManager:Compile')` (params Action=Compile, ObjectKind=Project), then `DM_FocusedProject`: `DM_DocumentFlattened.DM_Nets/DM_Pins`, `DM_DifferentialPairCount`, `DM_ViolationCount/DM_Violations(i)` (`DM_ErrorKind`, `DM_LongDescriptorString`, `DM_RelatedObjects`). Skip `.Harness` docs in `DM_LogicalDocuments`.
- Harness type lives on connector, port and the Top sheet entry. After resizing a harness connector, set each entry's `DistanceFromTop` to another value and back.

## Part import (user's EasyEDA Loader plugin, C:\dev\EasyEDALoader)
- `Client.ShowDocument(doc)`, then `ResetParameters; AddStringParameter('Parts','C123,C456'); AddStringParameter('Place','True'); AddStringParameter('X','13000'); AddStringParameter('Y','9500'); RunProcess('EasyEDA-Loader:EasyEDAImport');` Result: `E:\Documents\AltiumEE\batch-import.txt`; library `E:\Documents\AltiumEE\EasyEDA.schlib/.pcblib`.
- Place in a free spot, read pins, capture the symbol to see which pins are joined, then move into place. Verify LCSC stock/specs in the browser (search exact MPN) first. New footprints may need an Altium restart to show.
- The plugin is the user's fork (github abda-s/EasyEDALoader, branch `celestial-passives`): resistors/capacitors drawn like the Celestial library (RKM values 4K7/100n, hidden pin numbers); other symbols converted geometry-faithfully on a 100 mil grid. Build: `dotnet build EasyEDA-Loader\EasyEDA-Loader.csproj -c Release`, then `.\Package.ps1`, then `.\Deploy.ps1` with Altium closed.
- Re-importing a part that is already in EasyEDA.schlib reuses the cached symbol: delete the old part from the library first. All EasyEDA requests go through its cache (`%LOCALAPPDATA%\EasyEDA-Loader\cache`); keep requests few, no proxy/IP rotation.

## Schematic images
- Select first-level objects inside the sheet except Note/TextFrame/Label/Image/Rectangle/type 42; `Client.ShowDocument(doc)`; `Client.SendMessage('Sch:Copy','',255,Client.CurrentView)`; `Sch:Deselect`; `powershell tools\emf2png.ps1 -Out <png> -Width 1800`; crop margins with PIL (`ImageOps.invert(im).getbbox()`, 20 px).

## Reading sheets without Altium
- `.SchDoc` is OLE: `olefile.OleFileIO(f).openstream('FileHeader')`, split on `|RECORD=`, text in `Text=`/`%UTF8%Text=`. No keyword grepping. Unsaved edits exist only in Altium.
