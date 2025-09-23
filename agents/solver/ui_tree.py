ui_tree1="""
Control Identifiers:

Dialog - 'Document1 - Word'    (L-11, T-11, R1931, B1019)
['Dialog', 'Document1 - Word', 'Document1 - WordDialog']
child_window(title="Document1 - Word", control_type="Window")
   | 
   | Pane - 'DropShadowTop'    (L0, T267, R1920, B276)
   | ['DropShadowTopPane', 'DropShadowTop', 'Pane', 'Pane0', 'Pane1']
   | child_window(title="DropShadowTop", control_type="Pane")
   | 
   | Pane - 'MsoDockTop'    (L0, T0, R1920, B267)
   | ['MsoDockTop', 'Pane2', 'MsoDockTopPane']
   | child_window(title="MsoDockTop", control_type="Pane")
   |    | 
   |    | Toolbar - ''    (L0, T0, R1920, B267)
   |    | ['Toolbar', 'Toolbar0', 'Toolbar1']
   |    |    | 
   |    |    | Pane - 'Ribbon'    (L0, T0, R1920, B267)
   |    |    | ['Ribbon', 'Pane3', 'RibbonPane', 'Ribbon0', 'Ribbon1', 'RibbonPane0', 'RibbonPane1']
   |    |    | child_window(title="Ribbon", control_type="Pane")
   |    |    |    | 
   |    |    |    | Pane - ''    (L0, T0, R1920, B267)
   |    |    |    | ['Pane4']
   |    |    |    |    | 
   |    |    |    |    | Pane - ''    (L0, T0, R1920, B267)
   |    |    |    |    | ['Pane5']
   |    |    |    |    |    | 
   |    |    |    |    |    | Pane - 'Ribbon'    (L0, T0, R1920, B267)
   |    |    |    |    |    | ['Ribbon2', 'Pane6', 'RibbonPane2']
   |    |    |    |    |    | child_window(title="Ribbon", control_type="Pane")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Toolbar - 'Quick Access Toolbar'    (L63, T0, R408, B72)
   |    |    |    |    |    |    | ['Quick Access Toolbar', 'Quick Access ToolbarToolbar', 'Toolbar2']
   |    |    |    |    |    |    | child_window(title="Quick Access Toolbar", control_type="ToolBar")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'AutoSave'    (L63, T14, R221, B58)
   |    |    |    |    |    |    |    | ['AutoSaveButton', 'Button', 'AutoSave', 'Button0', 'Button1']
   |    |    |    |    |    |    |    | child_window(title="AutoSave", auto_id="AutoSaveSwitch", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Save'    (L222, T14, R264, B57)
   |    |    |    |    |    |    |    | ['Save', 'Button2', 'SaveButton']
   |    |    |    |    |    |    |    | child_window(title="Save", auto_id="FileSave", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | SplitButton - 'Undo Typing'    (L265, T14, R321, B57)
   |    |    |    |    |    |    |    | ['SplitButton', 'Undo Typing', 'Undo TypingSplitButton', 'Undo Typing0', 'Undo Typing1', 'SplitButton0', 'SplitButton1']
   |    |    |    |    |    |    |    | child_window(title="Undo Typing", auto_id="Undo", control_type="SplitButton")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | Button - 'Undo Typing'    (L265, T14, R302, B57)
   |    |    |    |    |    |    |    |    | ['Undo Typing2', 'Undo TypingButton', 'Button3']
   |    |    |    |    |    |    |    |    | child_window(title="Undo Typing", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L302, T14, R321, B57)
   |    |    |    |    |    |    |    |    | ['More OptionsMenuItem', 'MenuItem', 'More Options', 'MenuItem0', 'MenuItem1', 'More OptionsMenuItem0', 'More OptionsMenuItem1', 'More Options0', 'More Options1']
   |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="Undo_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Repeat Typing'    (L322, T14, R364, B57)
   |    |    |    |    |    |    |    | ['Button4', 'Repeat TypingButton', 'Repeat Typing']
   |    |    |    |    |    |    |    | child_window(title="Repeat Typing", auto_id="RedoOrRepeat", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | MenuItem - 'Customize Quick Access Toolbar'    (L366, T13, R408, B59)
   |    |    |    |    |    |    |    | ['Customize Quick Access Toolbar', 'MenuItem2', 'Customize Quick Access ToolbarMenuItem']
   |    |    |    |    |    |    |    | child_window(title="Customize Quick Access Toolbar", control_type="MenuItem")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | TitleBar - '‪Document1‬  -  Word'    (L409, T0, R713, B72)
   |    |    |    |    |    |    | ['TitleBar', '\u202aDocument1\u202c  -  WordTitleBar', '\u202aDocument1\u202c  -  Word', '\u202aDocument1\u202c  -  Word0', '\u202aDocument1\u202c  -  Word1', 'TitleBar0', 'TitleBar1']
   |    |    |    |    |    |    | child_window(title="‪Document1‬  -  Word", control_type="TitleBar")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - '‪Document1‬  -  Word'    (L409, T0, R612, B72)
   |    |    |    |    |    |    |    | ['\u202aDocument1\u202c  -  WordButton', 'Button5', '\u202aDocument1\u202c  -  Word2']
   |    |    |    |    |    |    |    | child_window(title="‪Document1‬  -  Word", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | MenuItem - 'Type to search and use the up and down arrow keys to navigate'    (L713, T12, R1231, B60)
   |    |    |    |    |    |    | ['Type to search and use the up and down arrow keys to navigateMenuItem', 'MenuItem3', 'Type to search and use the up and down arrow keys to navigate']
   |    |    |    |    |    |    | child_window(title="Type to search and use the up and down arrow keys to navigate", auto_id="TellMeControlAnchor", control_type="MenuItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Edit - ''    (L774, T21, R1212, B53)
   |    |    |    |    |    |    |    | ['Edit', 'Edit0', 'Edit1']
   |    |    |    |    |    |    |    | child_window(auto_id="TellMeTextBoxAutomationId", control_type="Edit")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | MenuItem - 'Kaviya Gopi'    (L1629, T0, R1704, B72)
   |    |    |    |    |    |    | ['Kaviya GopiMenuItem', 'MenuItem4', 'Kaviya Gopi']
   |    |    |    |    |    |    | child_window(title="Kaviya Gopi", auto_id="MeControlWidget", control_type="MenuItem")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Minimize'    (L1704, T0, R1776, B72)
   |    |    |    |    |    |    | ['Minimize', 'MinimizeButton', 'Button6', 'Minimize0', 'Minimize1', 'MinimizeButton0', 'MinimizeButton1']
   |    |    |    |    |    |    | child_window(title="Minimize", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Restore Down'    (L1776, T0, R1848, B72)
   |    |    |    |    |    |    | ['Restore Down', 'Restore DownButton', 'Button7']
   |    |    |    |    |    |    | child_window(title="Restore Down", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Close'    (L1848, T0, R1920, B72)
   |    |    |    |    |    |    | ['Close', 'CloseButton', 'Button8', 'Close0', 'Close1', 'CloseButton0', 'CloseButton1']
   |    |    |    |    |    |    | child_window(title="Close", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'File Tab'    (L6, T72, R87, B117)
   |    |    |    |    |    |    | ['File TabButton', 'Button9', 'File Tab']
   |    |    |    |    |    |    | child_window(title="File Tab", auto_id="FileTabButton", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | TabControl - 'Ribbon Tabs'    (L87, T72, R1920, B117)
   |    |    |    |    |    |    | ['Ribbon Tabs', 'TabControl', 'Ribbon TabsTabControl']
   |    |    |    |    |    |    | child_window(title="Ribbon Tabs", control_type="Tab")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Home'    (L87, T72, R170, B117)
   |    |    |    |    |    |    |    | ['HomeTabItem', 'TabItem', 'Home', 'TabItem0', 'TabItem1', 'Home0', 'Home1']
   |    |    |    |    |    |    |    | child_window(title="Home", auto_id="TabHome", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Insert'    (L171, T72, R251, B117)
   |    |    |    |    |    |    |    | ['TabItem2', 'Insert', 'InsertTabItem']
   |    |    |    |    |    |    |    | child_window(title="Insert", auto_id="TabInsert", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Draw'    (L252, T72, R325, B117)
   |    |    |    |    |    |    |    | ['TabItem3', 'DrawTabItem', 'Draw']
   |    |    |    |    |    |    |    | child_window(title="Draw", auto_id="TabDrawInk", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Design'    (L326, T72, R416, B117)
   |    |    |    |    |    |    |    | ['TabItem4', 'DesignTabItem', 'Design']
   |    |    |    |    |    |    |    | child_window(title="Design", auto_id="TabWordDesign", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Layout'    (L417, T72, R505, B117)
   |    |    |    |    |    |    |    | ['TabItem5', 'Layout', 'LayoutTabItem']
   |    |    |    |    |    |    |    | child_window(title="Layout", auto_id="TabPageLayoutWord", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'References'    (L506, T72, R632, B117)
   |    |    |    |    |    |    |    | ['TabItem6', 'References', 'ReferencesTabItem']
   |    |    |    |    |    |    |    | child_window(title="References", auto_id="TabReferences", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Mailings'    (L633, T72, R736, B117)
   |    |    |    |    |    |    |    | ['TabItem7', 'MailingsTabItem', 'Mailings']
   |    |    |    |    |    |    |    | child_window(title="Mailings", auto_id="TabMailings", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Review'    (L737, T72, R827, B117)
   |    |    |    |    |    |    |    | ['Review', 'TabItem8', 'ReviewTabItem']
   |    |    |    |    |    |    |    | child_window(title="Review", auto_id="TabReviewWord", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'View'    (L828, T72, R899, B117)
   |    |    |    |    |    |    |    | ['View', 'TabItem9', 'ViewTabItem']
   |    |    |    |    |    |    |    | child_window(title="View", auto_id="TabView", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Help'    (L900, T72, R970, B117)
   |    |    |    |    |    |    |    | ['TabItem10', 'HelpTabItem', 'Help']
   |    |    |    |    |    |    |    | child_window(title="Help", auto_id="HelpTab", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Comments'    (L1532, T76, R1667, B112)
   |    |    |    |    |    |    |    | ['CommentsButton', 'Button10', 'Comments']
   |    |    |    |    |    |    |    | child_window(title="Comments", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | ComboBox - 'Editing'    (L1679, T76, R1803, B112)
   |    |    |    |    |    |    |    | ['ComboBox', 'Editing', 'EditingComboBox', 'ComboBox0', 'ComboBox1', 'Editing0', 'Editing1']
   |    |    |    |    |    |    |    | child_window(title="Editing", control_type="ComboBox")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | MenuItem - 'Share'    (L1815, T72, R1920, B117)
   |    |    |    |    |    |    |    | ['ShareMenuItem', 'MenuItem5', 'Share']
   |    |    |    |    |    |    |    | child_window(title="Share", control_type="MenuItem")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Pane - 'Lower Ribbon'    (L12, T117, R1866, B267)
   |    |    |    |    |    |    | ['Pane7', 'Lower RibbonPane', 'Lower Ribbon']
   |    |    |    |    |    |    | child_window(title="Lower Ribbon", control_type="Pane")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | GroupBox - 'Home'    (L18, T117, R1866, B267)
   |    |    |    |    |    |    |    | ['HomeGroupBox', 'Home2', 'GroupBox', 'GroupBox0', 'GroupBox1']
   |    |    |    |    |    |    |    | child_window(title="Home", control_type="Group")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Clipboard'    (L18, T120, R143, B264)
   |    |    |    |    |    |    |    |    | ['GroupBox2', 'ClipboardGroupBox', 'Clipboard']
   |    |    |    |    |    |    |    |    | child_window(title="Clipboard", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Paste'    (L30, T123, R92, B237)
   |    |    |    |    |    |    |    |    |    | ['SplitButton2', 'PasteSplitButton', 'Paste', 'Paste0', 'Paste1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Paste", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Paste'    (L30, T123, R92, B180)
   |    |    |    |    |    |    |    |    |    |    | ['PasteButton', 'Paste2', 'Button11']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Paste", auto_id="Paste", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L30, T180, R92, B237)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem2', 'MenuItem6', 'More Options2']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="PasteMenu_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Cut'    (L95, T123, R131, B159)
   |    |    |    |    |    |    |    |    |    | ['CutButton', 'Button12', 'Cut']
   |    |    |    |    |    |    |    |    |    | child_window(title="Cut", auto_id="Cut", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Copy'    (L95, T162, R131, B198)
   |    |    |    |    |    |    |    |    |    | ['CopyButton', 'Copy', 'Button13']
   |    |    |    |    |    |    |    |    |    | child_window(title="Copy", auto_id="Copy", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Format Painter'    (L95, T201, R131, B237)
   |    |    |    |    |    |    |    |    |    | ['Format PainterButton', 'Format Painter', 'Button14']
   |    |    |    |    |    |    |    |    |    | child_window(title="Format Painter", auto_id="FormatPainter", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Office Clipboard...'    (L119, T240, R143, B264)
   |    |    |    |    |    |    |    |    |    | ['Office Clipboard...', 'Office Clipboard...Button', 'Button15']
   |    |    |    |    |    |    |    |    |    | child_window(title="Office Clipboard...", auto_id="ShowClipboard", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Font'    (L143, T120, R494, B264)
   |    |    |    |    |    |    |    |    | ['FontGroupBox', 'Font', 'GroupBox3', 'Font0', 'Font1']
   |    |    |    |    |    |    |    |    | child_window(title="Font", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | ComboBox - 'Font'    (L155, T123, R414, B159)
   |    |    |    |    |    |    |    |    |    | ['Font2', 'ComboBox2', 'FontComboBox']
   |    |    |    |    |    |    |    |    |    | child_window(title="Font", auto_id="Font", control_type="ComboBox")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Edit - 'Aptos (Body)'    (L156, T125, R395, B156)
   |    |    |    |    |    |    |    |    |    |    | ['Edit2']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Aptos (Body)", control_type="Edit")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Open'    (L395, T124, R413, B158)
   |    |    |    |    |    |    |    |    |    |    | ['Open', 'Button16', 'OpenButton', 'Open0', 'Open1', 'OpenButton0', 'OpenButton1']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Open", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | ComboBox - 'Font Size'    (L417, T123, R482, B159)
   |    |    |    |    |    |    |    |    |    | ['Font Size', 'ComboBox3', 'Font SizeComboBox']
   |    |    |    |    |    |    |    |    |    | child_window(title="Font Size", auto_id="FontSize", control_type="ComboBox")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Edit - '12'    (L418, T125, R463, B156)
   |    |    |    |    |    |    |    |    |    |    | ['Edit3']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="12", control_type="Edit")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Open'    (L463, T124, R481, B158)
   |    |    |    |    |    |    |    |    |    |    | ['Open2', 'Button17', 'OpenButton2']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Open", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Grow Font'    (L407, T201, R443, B237)
   |    |    |    |    |    |    |    |    |    | ['Grow Font', 'Button18', 'Grow FontButton']
   |    |    |    |    |    |    |    |    |    | child_window(title="Grow Font", auto_id="FontSizeIncreaseWord", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Shrink Font'    (L446, T201, R482, B237)
   |    |    |    |    |    |    |    |    |    | ['Shrink Font', 'Button19', 'Shrink FontButton']
   |    |    |    |    |    |    |    |    |    | child_window(title="Shrink Font", auto_id="FontSizeDecreaseWord", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Change Case'    (L340, T201, R400, B237)
   |    |    |    |    |    |    |    |    |    | ['Change CaseMenuItem', 'Change Case', 'MenuItem7']
   |    |    |    |    |    |    |    |    |    | child_window(title="Change Case", auto_id="ChangeCaseGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Clear Formatting'    (L415, T162, R451, B198)
   |    |    |    |    |    |    |    |    |    | ['Clear Formatting', 'Clear FormattingButton', 'Button20']
   |    |    |    |    |    |    |    |    |    | child_window(title="Clear Formatting", auto_id="ClearFormatting", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Bold'    (L155, T162, R191, B198)
   |    |    |    |    |    |    |    |    |    | ['BoldButton', 'Bold', 'Button21']
   |    |    |    |    |    |    |    |    |    | child_window(title="Bold", auto_id="Bold", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Italic'    (L194, T162, R230, B198)
   |    |    |    |    |    |    |    |    |    | ['Italic', 'ItalicButton', 'Button22']
   |    |    |    |    |    |    |    |    |    | child_window(title="Italic", auto_id="Italic", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Underline'    (L233, T162, R291, B198)
   |    |    |    |    |    |    |    |    |    | ['SplitButton3', 'UnderlineSplitButton', 'Underline', 'Underline0', 'Underline1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Underline", auto_id="UnderlineGallery", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Underline'    (L233, T162, R269, B198)
   |    |    |    |    |    |    |    |    |    |    | ['UnderlineButton', 'Button23', 'Underline2']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Underline", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L269, T162, R291, B198)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem3', 'MenuItem8', 'More Options3']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="UnderlineGallery_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Strikethrough'    (L294, T162, R330, B198)
   |    |    |    |    |    |    |    |    |    | ['Strikethrough', 'StrikethroughButton', 'Button24']
   |    |    |    |    |    |    |    |    |    | child_window(title="Strikethrough", auto_id="Strikethrough", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Subscript'    (L333, T162, R369, B198)
   |    |    |    |    |    |    |    |    |    | ['Subscript', 'SubscriptButton', 'Button25']
   |    |    |    |    |    |    |    |    |    | child_window(title="Subscript", auto_id="Subscript", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Superscript'    (L372, T162, R408, B198)
   |    |    |    |    |    |    |    |    |    | ['Superscript', 'Button26', 'SuperscriptButton']
   |    |    |    |    |    |    |    |    |    | child_window(title="Superscript", auto_id="Superscript", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Text Effects and Typography'    (L155, T201, R215, B237)
   |    |    |    |    |    |    |    |    |    | ['Text Effects and Typography', 'MenuItem9', 'Text Effects and TypographyMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Text Effects and Typography", auto_id="TextEffectsGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Text Highlight Color'    (L218, T201, R276, B237)
   |    |    |    |    |    |    |    |    |    | ['SplitButton4', 'Text Highlight Color', 'Text Highlight ColorSplitButton']
   |    |    |    |    |    |    |    |    |    | child_window(title="Text Highlight Color", auto_id="TextHighlightColorPicker", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Text Highlight Color Yellow'    (L218, T201, R254, B237)
   |    |    |    |    |    |    |    |    |    |    | ['Text Highlight Color YellowButton', 'Text Highlight Color Yellow', 'Button27']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Text Highlight Color Yellow", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L254, T201, R276, B237)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem4', 'MenuItem10', 'More Options4']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="TextHighlightColorPicker_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Font Color'    (L279, T201, R337, B237)
   |    |    |    |    |    |    |    |    |    | ['SplitButton5', 'Font Color', 'Font ColorSplitButton']
   |    |    |    |    |    |    |    |    |    | child_window(title="Font Color", auto_id="FontColorPicker", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Font Color Red'    (L279, T201, R315, B237)
   |    |    |    |    |    |    |    |    |    |    | ['Font Color Red', 'Font Color RedButton', 'Button28']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Font Color Red", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L315, T201, R337, B237)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem5', 'MenuItem11', 'More Options5']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="FontColorPicker_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Font...'    (L470, T240, R494, B264)
   |    |    |    |    |    |    |    |    |    | ['Font...', 'Button29', 'Font...Button']
   |    |    |    |    |    |    |    |    |    | child_window(title="Font...", auto_id="FontDialog", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Paragraph'    (L494, T120, R782, B264)
   |    |    |    |    |    |    |    |    | ['ParagraphGroupBox', 'GroupBox4', 'Paragraph']
   |    |    |    |    |    |    |    |    | child_window(title="Paragraph", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Bullets'    (L506, T123, R564, B159)
   |    |    |    |    |    |    |    |    |    | ['SplitButton6', 'Bullets', 'BulletsSplitButton', 'Bullets0', 'Bullets1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Bullets", auto_id="BulletsGalleryWord", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Bullets'    (L506, T123, R542, B159)
   |    |    |    |    |    |    |    |    |    |    | ['BulletsButton', 'Bullets2', 'Button30']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Bullets", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L542, T123, R564, B159)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem6', 'MenuItem12', 'More Options6']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="BulletsGalleryWord_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Numbering'    (L567, T123, R625, B159)
   |    |    |    |    |    |    |    |    |    | ['SplitButton7', 'NumberingSplitButton', 'Numbering', 'Numbering0', 'Numbering1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Numbering", auto_id="NumberingGalleryWord", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Numbering'    (L567, T123, R603, B159)
   |    |    |    |    |    |    |    |    |    |    | ['Numbering2', 'Button31', 'NumberingButton']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Numbering", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L603, T123, R625, B159)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem7', 'MenuItem13', 'More Options7']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="NumberingGalleryWord_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Multilevel List'    (L628, T123, R688, B159)
   |    |    |    |    |    |    |    |    |    | ['Multilevel List', 'MenuItem14', 'Multilevel ListMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Multilevel List", auto_id="MultilevelListGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Decrease Indent'    (L695, T123, R731, B159)
   |    |    |    |    |    |    |    |    |    | ['Decrease IndentButton', 'Decrease Indent', 'Button32']
   |    |    |    |    |    |    |    |    |    | child_window(title="Decrease Indent", auto_id="IndentDecreaseWord", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Increase Indent'    (L734, T123, R770, B159)
   |    |    |    |    |    |    |    |    |    | ['Increase Indent', 'Button33', 'Increase IndentButton']
   |    |    |    |    |    |    |    |    |    | child_window(title="Increase Indent", auto_id="IndentIncreaseWord", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Sort...'    (L632, T201, R668, B237)
   |    |    |    |    |    |    |    |    |    | ['Sort...Button', 'Button34', 'Sort...']
   |    |    |    |    |    |    |    |    |    | child_window(title="Sort...", auto_id="SortDialogClassic", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Show All'    (L675, T201, R711, B237)
   |    |    |    |    |    |    |    |    |    | ['Show AllButton', 'Show All', 'Button35']
   |    |    |    |    |    |    |    |    |    | child_window(title="Show All", auto_id="ParagraphMarks", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Align Left'    (L506, T162, R542, B198)
   |    |    |    |    |    |    |    |    |    | ['Align Left', 'Align LeftButton', 'Button36']
   |    |    |    |    |    |    |    |    |    | child_window(title="Align Left", auto_id="AlignLeft", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Center'    (L545, T162, R581, B198)
   |    |    |    |    |    |    |    |    |    | ['Center', 'Button37', 'CenterButton']
   |    |    |    |    |    |    |    |    |    | child_window(title="Center", auto_id="AlignCenter", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Align Right'    (L584, T162, R620, B198)
   |    |    |    |    |    |    |    |    |    | ['Align Right', 'Button38', 'Align RightButton']
   |    |    |    |    |    |    |    |    |    | child_window(title="Align Right", auto_id="AlignRight", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Justify'    (L623, T162, R659, B198)
   |    |    |    |    |    |    |    |    |    | ['JustifyButton', 'Button39', 'Justify']
   |    |    |    |    |    |    |    |    |    | child_window(title="Justify", auto_id="AlignJustify", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Line and Paragraph Spacing'    (L666, T162, R726, B198)
   |    |    |    |    |    |    |    |    |    | ['Line and Paragraph SpacingMenuItem', 'MenuItem15', 'Line and Paragraph Spacing']
   |    |    |    |    |    |    |    |    |    | child_window(title="Line and Paragraph Spacing", auto_id="LineSpacingGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Shading'    (L506, T201, R564, B237)
   |    |    |    |    |    |    |    |    |    | ['SplitButton8', 'Shading', 'ShadingSplitButton']
   |    |    |    |    |    |    |    |    |    | child_window(title="Shading", auto_id="ShadingColorPicker", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Shading RGB(0, 0, 0)'    (L506, T201, R542, B237)
   |    |    |    |    |    |    |    |    |    |    | ['Shading RGB(0, 0, 0)Button', 'Shading RGB(0, 0, 0)', 'Button40']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Shading RGB(0, 0, 0)", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L542, T201, R564, B237)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem8', 'MenuItem16', 'More Options8']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="ShadingColorPicker_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Borders'    (L567, T201, R625, B237)
   |    |    |    |    |    |    |    |    |    | ['SplitButton9', 'BordersSplitButton', 'Borders', 'Borders0', 'Borders1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Borders", auto_id="BordersSelectionGallery", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Borders'    (L567, T201, R603, B237)
   |    |    |    |    |    |    |    |    |    |    | ['BordersButton', 'Borders2', 'Button41']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Borders", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L603, T201, R625, B237)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem9', 'MenuItem17', 'More Options9']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="BordersSelectionGallery_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Paragraph...'    (L758, T240, R782, B264)
   |    |    |    |    |    |    |    |    |    | ['Paragraph...', 'Paragraph...Button', 'Button42']
   |    |    |    |    |    |    |    |    |    | child_window(title="Paragraph...", auto_id="ParagraphDialog", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Styles'    (L782, T120, R1336, B264)
   |    |    |    |    |    |    |    |    | ['StylesGroupBox', 'GroupBox5', 'Styles', 'StylesGroupBox0', 'StylesGroupBox1', 'Styles0', 'Styles1']
   |    |    |    |    |    |    |    |    | child_window(title="Styles", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | GroupBox - 'Styles'    (L794, T130, R1324, B224)
   |    |    |    |    |    |    |    |    |    | ['StylesGroupBox2', 'GroupBox6', 'Styles2']
   |    |    |    |    |    |    |    |    |    | child_window(title="Styles", control_type="Group")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - ''    (L794, T134, R1324, B224)
   |    |    |    |    |    |    |    |    |    |    | ['MenuItem18']
   |    |    |    |    |    |    |    |    |    |    | child_window(auto_id="QuickStylesGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    | Pane - 'Styles'    (L796, T137, R1284, B221)
   |    |    |    |    |    |    |    |    |    |    |    | ['StylesPane', 'Styles3', 'Pane8']
   |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Styles", control_type="Pane")
   |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    | ListView - 'Styles'    (L797, T137, R1283, B641)
   |    |    |    |    |    |    |    |    |    |    |    |    | ['StylesListView', 'Styles4', 'ListView']
   |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Styles", control_type="DataGrid")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - '¶ Normal'    (L797, T137, R959, B221)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['¶ Normal', 'ListItem', '¶ NormalListItem', 'ListItem0', 'ListItem1']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="¶ Normal", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - '¶ No Spacing'    (L959, T137, R1121, B221)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['¶ No Spacing', 'ListItem2', '¶ No SpacingListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="¶ No Spacing", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Heading 1'    (L1121, T137, R1283, B221)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Heading 1', 'ListItem3', 'Heading 1ListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Heading 1", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Heading 2'    (L797, T221, R959, B305)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Heading 2', 'ListItem4', 'Heading 2ListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Heading 2", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Title'    (L959, T221, R1121, B305)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['ListItem5', 'TitleListItem', 'Title']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Title", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Subtitle'    (L1121, T221, R1283, B305)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Subtitle', 'ListItem6', 'SubtitleListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Subtitle", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Subtle Emphasis'    (L797, T305, R959, B389)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Subtle EmphasisListItem', 'ListItem7', 'Subtle Emphasis']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Subtle Emphasis", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Emphasis'    (L959, T305, R1121, B389)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Emphasis', 'EmphasisListItem', 'ListItem8']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Emphasis", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Intense Emphasis'    (L1121, T305, R1283, B389)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Intense Emphasis', 'ListItem9', 'Intense EmphasisListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Intense Emphasis", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Strong'    (L797, T389, R959, B473)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['StrongListItem', 'ListItem10', 'Strong']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Strong", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Quote'    (L959, T389, R1121, B473)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Quote', 'ListItem11', 'QuoteListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Quote", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Intense Quote'    (L1121, T389, R1283, B473)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Intense Quote', 'ListItem12', 'Intense QuoteListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Intense Quote", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Subtle Reference'    (L797, T473, R959, B557)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['ListItem13', 'Subtle Reference', 'Subtle ReferenceListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Subtle Reference", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Intense Reference'    (L959, T473, R1121, B557)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['ListItem14', 'Intense ReferenceListItem', 'Intense Reference']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Intense Reference", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Book Title'    (L1121, T473, R1283, B557)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Book Title', 'ListItem15', 'Book TitleListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Book Title", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - '¶ List Paragraph'    (L797, T557, R959, B641)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['ListItem16', '¶ List Paragraph', '¶ List ParagraphListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="¶ List Paragraph", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    | Button - 'Styles'    (L1284, T134, R1320, B224)
   |    |    |    |    |    |    |    |    |    |    |    | ['StylesButton', 'Styles5', 'Button43']
   |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Styles", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    | Image - ''    (L1296, T173, R1308, B185)
   |    |    |    |    |    |    |    |    |    |    |    |    | ['Image']
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Styles...'    (L1312, T240, R1336, B264)
   |    |    |    |    |    |    |    |    |    | ['Styles...', 'Button44', 'Styles...Button']
   |    |    |    |    |    |    |    |    |    | child_window(title="Styles...", auto_id="StylesPane", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Editing'    (L1336, T120, R1418, B264)
   |    |    |    |    |    |    |    |    | ['EditingGroupBox', 'GroupBox7', 'Editing2']
   |    |    |    |    |    |    |    |    | child_window(title="Editing", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Editing'    (L1336, T120, R1418, B264)
   |    |    |    |    |    |    |    |    |    | ['MenuItem19', 'Editing3', 'EditingMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Editing", control_type="MenuItem")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Voice'    (L1418, T120, R1505, B264)
   |    |    |    |    |    |    |    |    | ['GroupBox8', 'VoiceGroupBox', 'Voice']
   |    |    |    |    |    |    |    |    | child_window(title="Voice", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Dictate'    (L1430, T123, R1493, B237)
   |    |    |    |    |    |    |    |    |    | ['SplitButton10', 'DictateSplitButton', 'Dictate', 'Dictate0', 'Dictate1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Dictate", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Dictate'    (L1430, T123, R1493, B180)
   |    |    |    |    |    |    |    |    |    |    | ['Dictate2', 'Button45', 'DictateButton']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Dictate", auto_id="Dictate", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L1430, T180, R1493, B237)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem10', 'MenuItem20', 'More Options10']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="DictationMenu_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Sensitivity'    (L1505, T120, R1616, B264)
   |    |    |    |    |    |    |    |    | ['Sensitivity', 'GroupBox9', 'SensitivityGroupBox', 'Sensitivity0', 'Sensitivity1']
   |    |    |    |    |    |    |    |    | child_window(title="Sensitivity", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Sensitivity'    (L1517, T123, R1604, B237)
   |    |    |    |    |    |    |    |    |    | ['Sensitivity2', 'SensitivityMenuItem', 'MenuItem21']
   |    |    |    |    |    |    |    |    |    | child_window(title="Sensitivity", auto_id="ClassifyLabelProtect", control_type="MenuItem")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Editor'    (L1616, T120, R1702, B264)
   |    |    |    |    |    |    |    |    | ['EditorGroupBox', 'GroupBox10', 'Editor', 'Editor0', 'Editor1']
   |    |    |    |    |    |    |    |    | child_window(title="Editor", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Editor'    (L1628, T123, R1690, B237)
   |    |    |    |    |    |    |    |    |    | ['Button46', 'Editor2', 'EditorButton']
   |    |    |    |    |    |    |    |    |    | child_window(title="Editor", auto_id="WritingAssistanceCheckDocument", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Add-ins'    (L1702, T120, R1797, B264)
   |    |    |    |    |    |    |    |    | ['GroupBox11', 'Add-insGroupBox', 'Add-ins']
   |    |    |    |    |    |    |    |    | child_window(title="Add-ins", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Add‑ins'    (L1714, T123, R1785, B237)
   |    |    |    |    |    |    |    |    |    | ['Add‑ins', 'Add‑insButton', 'Button47']
   |    |    |    |    |    |    |    |    |    | child_window(title="Add‑ins", auto_id="OfficeExtensionsShowAddinFlyout", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | MenuItem - 'Ribbon Display Options'    (L1872, T231, R1902, B261)
   |    |    |    |    |    |    | ['Ribbon Display Options', 'Ribbon Display OptionsMenuItem', 'MenuItem22']
   |    |    |    |    |    |    | child_window(title="Ribbon Display Options", control_type="MenuItem")
   | 
   | Pane - 'MsoDockBottom'    (L0, T975, R1920, B1008)
   | ['MsoDockBottom', 'MsoDockBottomPane', 'Pane9']
   | child_window(title="MsoDockBottom", control_type="Pane")
   |    | 
   |    | Toolbar - ''    (L0, T975, R1920, B1008)
   |    | ['Word Count 0 wordsToolbar', 'Toolbar3']
   |    |    | 
   |    |    | Pane - 'Status Bar'    (L0, T975, R1920, B1008)
   |    |    | ['Status Bar', 'Pane10', 'Status BarPane']
   |    |    | child_window(title="Status Bar", control_type="Pane")
   |    |    |    | 
   |    |    |    | Pane - ''    (L0, T975, R1920, B1008)
   |    |    |    | ['Pane11', 'Word Count 0 wordsPane', 'Word Count 0 wordsPane0', 'Word Count 0 wordsPane1']
   |    |    |    |    | 
   |    |    |    |    | Pane - ''    (L0, T975, R1920, B1008)
   |    |    |    |    | ['Pane12', 'Word Count 0 wordsPane2']
   |    |    |    |    |    | 
   |    |    |    |    |    | StatusBar - ''    (L0, T975, R1920, B1008)
   |    |    |    |    |    | ['StatusBar', 'Word Count 0 wordsStatusBar']
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Page Number Page 1 of 1'    (L6, T976, R106, B1008)
   |    |    |    |    |    |    | ['Page Number Page 1 of 1Button', 'Page Number Page 1 of 1', 'Button48']
   |    |    |    |    |    |    | child_window(title="Page Number Page 1 of 1", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Static - 'Word Count 0 words'    (L111, T976, R190, B1008)
   |    |    |    |    |    |    | ['Word Count 0 words', 'Word Count 0 wordsStatic', 'Static', 'Static0', 'Static1']
   |    |    |    |    |    |    | child_window(title="Word Count 0 words", control_type="Text")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Spelling and Grammar Check No Errors'    (L195, T976, R242, B1008)
   |    |    |    |    |    |    | ['Spelling and Grammar Check No Errors', 'Spelling and Grammar Check No ErrorsButton', 'Button49']
   |    |    |    |    |    |    | child_window(title="Spelling and Grammar Check No Errors", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Language English (United States)'    (L242, T976, R420, B1008)
   |    |    |    |    |    |    | ['Language English (United States)', 'Language English (United States)Button', 'Button50']
   |    |    |    |    |    |    | child_window(title="Language English (United States)", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Static - 'Text Predictions Text Predictions: On'    (L425, T976, R583, B1008)
   |    |    |    |    |    |    | ['Text Predictions Text Predictions: OnStatic', 'Text Predictions Text Predictions: On', 'Static2']
   |    |    |    |    |    |    | child_window(title="Text Predictions Text Predictions: On", control_type="Text")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Accessibility Checker Accessibility: Good to go'    (L588, T976, R807, B1008)
   |    |    |    |    |    |    | ['Button51', 'Accessibility Checker Accessibility: Good to goButton', 'Accessibility Checker Accessibility: Good to go']
   |    |    |    |    |    |    | child_window(title="Accessibility Checker Accessibility: Good to go", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Focus '    (L1363, T976, R1453, B1008)
   |    |    |    |    |    |    | ['Focus Button', 'Focus ', 'Button52']
   |    |    |    |    |    |    | child_window(title="Focus ", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Read Mode'    (L1457, T976, R1517, B1008)
   |    |    |    |    |    |    | ['Read ModeButton', 'Button53', 'Read Mode']
   |    |    |    |    |    |    | child_window(title="Read Mode", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Print Layout'    (L1517, T976, R1577, B1008)
   |    |    |    |    |    |    | ['Print Layout', 'Print LayoutButton', 'Button54']
   |    |    |    |    |    |    | child_window(title="Print Layout", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Web Layout'    (L1577, T976, R1637, B1008)
   |    |    |    |    |    |    | ['Web LayoutButton', 'Button55', 'Web Layout']
   |    |    |    |    |    |    | child_window(title="Web Layout", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Zoom Out (Ctrl -)'    (L1638, T976, R1664, B1008)
   |    |    |    |    |    |    | ['Zoom Out (Ctrl -)Button', 'Zoom Out (Ctrl -)', 'Button56']
   |    |    |    |    |    |    | child_window(title="Zoom Out (Ctrl -)", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Slider - 'Zoom'    (L1664, T976, R1814, B1008)
   |    |    |    |    |    |    | ['Slider']
   |    |    |    |    |    |    | child_window(title="Zoom", control_type="Slider")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Zoom Out'    (L1664, T976, R1739, B1008)
   |    |    |    |    |    |    |    | ['Zoom Out', 'Zoom OutButton', 'Button57']
   |    |    |    |    |    |    |    | child_window(title="Zoom Out", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Thumb - 'Position'    (L1739, T983, R1747, B1000)
   |    |    |    |    |    |    |    | ['Thumb', 'PositionThumb', 'Position', 'Thumb0', 'Thumb1']
   |    |    |    |    |    |    |    | child_window(title="Position", control_type="Thumb")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Zoom In'    (L1747, T976, R1814, B1008)
   |    |    |    |    |    |    |    | ['Zoom InButton', 'Button58', 'Zoom In']
   |    |    |    |    |    |    |    | child_window(title="Zoom In", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Zoom In (Ctrl +)'    (L1814, T976, R1840, B1008)
   |    |    |    |    |    |    | ['Zoom In (Ctrl +)', 'Button59', 'Zoom In (Ctrl +)Button']
   |    |    |    |    |    |    | child_window(title="Zoom In (Ctrl +)", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Static - 'Zoom 120%'    (L1840, T976, R1903, B1008)
   |    |    |    |    |    |    | ['Zoom 120%Static', 'Zoom 120%', 'Static3']
   |    |    |    |    |    |    | child_window(title="Zoom 120%", control_type="Text")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Thumb - 'Size box'    (L1903, T976, R1920, B1008)
   |    |    |    |    |    |    | ['Thumb2', 'Size box', 'Size boxThumb']
   |    |    |    |    |    |    | child_window(title="Size box", control_type="Thumb")
   | 
   | Pane - ''    (L0, T267, R1920, B975)
   | ['Pane13']
   |    | 
   |    | Pane - 'Document1'    (L0, T267, R1920, B975)
   |    | ['Document1', 'Document1Pane', 'Pane14']
   |    | child_window(title="Document1", control_type="Pane")
   |    |    | 
   |    |    | Document - ''    (L0, T267, R1894, B975)
   |    |    | ['Document']
   |    |    |    | 
   |    |    |    | Custom - 'Page 1'    (L212, T298, R1682, B975)
   |    |    |    | ['Page 1Custom', 'Page 1', 'Custom']
   |    |    |    | child_window(title="Page 1", auto_id="UIA_AutomationId_Word_Page_1", control_type="Custom")
   |    |    |    |    | 
   |    |    |    |    | Edit - 'Page 1 content'    (L212, T471, R1682, B975)
   |    |    |    |    | ['Edit4']
   |    |    |    |    | child_window(title="Page 1 content", auto_id="Body", control_type="Edit")
   |    |    | 
   |    |    | Pane - 'Vertical'    (L1894, T267, R1920, B975)
   |    |    | ['Vertical', 'Pane15', 'VerticalPane']
   |    |    | child_window(title="Vertical", control_type="Pane")
   |    |    |    | 
   |    |    |    | Pane - ''    (L1894, T267, R1920, B975)
   |    |    |    | ['Pane16']
   |    |    |    |    | 
   |    |    |    |    | ScrollBar - ''    (L1894, T267, R1920, B975)
   |    |    |    |    | ['ScrollBar']
   | 
   | TitleBar - ''    (L0, T-8, R1920, B0)
   | ['TitleBar2']
   |    | 
   |    | Menu - 'System'    (L0, T0, R33, B33)
   |    | ['SystemMenu', 'Menu', 'System', 'System0', 'System1', 'Menu0', 'Menu1']
   |    | child_window(title="System", auto_id="MenuBar", control_type="MenuBar")
   |    |    | 
   |    |    | MenuItem - 'System'    (L0, T0, R33, B33)
   |    |    | ['MenuItem23', 'SystemMenuItem', 'System2']
   |    |    | child_window(title="System", control_type="MenuItem")
   |    | 
   |    | Button - 'Minimize'    (L0, T0, R0, B0)
   |    | ['Minimize2', 'MinimizeButton2', 'Button60']
   |    | child_window(title="Minimize", control_type="Button")
   |    | 
   |    | Button - 'Restore'    (L0, T0, R0, B0)
   |    | ['Restore', 'Button61', 'RestoreButton']
   |    | child_window(title="Restore", control_type="Button")
   |    | 
   |    | Button - 'Close'    (L0, T0, R0, B0)
   |    | ['Close2', 'CloseButton2', 'Button62']
   |    | child_window(title="Close", control_type="Button")
   | 
   | Menu - 'Menu Bar'    (L0, T0, R0, B0)
   | ['Menu2', 'Menu Bar', 'Menu BarMenu']
   | child_window(title="Menu Bar", control_type="MenuBar")
   |    | 
   |    | ComboBox - 'Ask a Question'    (L0, T0, R0, B0)
   |    | ['Ask a QuestionComboBox', 'ComboBox4', 'Ask a Question']
   |    | child_window(title="Ask a Question", control_type="ComboBox")"""

ui_tree2="""
Control Identifiers:

Dialog - 'Document1 - Word'    (L-11, T-11, R1931, B1019)
['Dialog', 'Document1 - Word', 'Document1 - WordDialog']
child_window(title="Document1 - Word", control_type="Window")
   | 
   | Pane - 'DropShadowTop'    (L0, T267, R1920, B276)
   | ['DropShadowTopPane', 'DropShadowTop', 'Pane', 'Pane0', 'Pane1']
   | child_window(title="DropShadowTop", control_type="Pane")
   | 
   | Pane - 'MsoDockTop'    (L0, T0, R1920, B267)
   | ['MsoDockTop', 'Pane2', 'MsoDockTopPane']
   | child_window(title="MsoDockTop", control_type="Pane")
   |    | 
   |    | Toolbar - ''    (L0, T0, R1920, B267)
   |    | ['Toolbar', 'Toolbar0', 'Toolbar1']
   |    |    | 
   |    |    | Pane - 'Ribbon'    (L0, T0, R1920, B267)
   |    |    | ['Ribbon', 'Pane3', 'RibbonPane', 'Ribbon0', 'Ribbon1', 'RibbonPane0', 'RibbonPane1']
   |    |    | child_window(title="Ribbon", control_type="Pane")
   |    |    |    | 
   |    |    |    | Pane - ''    (L0, T0, R1920, B267)
   |    |    |    | ['Pane4']
   |    |    |    |    | 
   |    |    |    |    | Pane - ''    (L0, T0, R1920, B267)
   |    |    |    |    | ['Pane5']
   |    |    |    |    |    | 
   |    |    |    |    |    | Pane - 'Ribbon'    (L0, T0, R1920, B267)
   |    |    |    |    |    | ['Ribbon2', 'Pane6', 'RibbonPane2']
   |    |    |    |    |    | child_window(title="Ribbon", control_type="Pane")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Toolbar - 'Quick Access Toolbar'    (L63, T0, R408, B72)
   |    |    |    |    |    |    | ['Quick Access Toolbar', 'Quick Access ToolbarToolbar', 'Toolbar2']
   |    |    |    |    |    |    | child_window(title="Quick Access Toolbar", control_type="ToolBar")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'AutoSave'    (L63, T14, R221, B58)
   |    |    |    |    |    |    |    | ['AutoSaveButton', 'Button', 'AutoSave', 'Button0', 'Button1']
   |    |    |    |    |    |    |    | child_window(title="AutoSave", auto_id="AutoSaveSwitch", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Save'    (L222, T14, R264, B57)
   |    |    |    |    |    |    |    | ['Save', 'Button2', 'SaveButton']
   |    |    |    |    |    |    |    | child_window(title="Save", auto_id="FileSave", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | SplitButton - 'Undo Typing'    (L265, T14, R321, B57)
   |    |    |    |    |    |    |    | ['SplitButton', 'Undo Typing', 'Undo TypingSplitButton', 'Undo Typing0', 'Undo Typing1', 'SplitButton0', 'SplitButton1']
   |    |    |    |    |    |    |    | child_window(title="Undo Typing", auto_id="Undo", control_type="SplitButton")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | Button - 'Undo Typing'    (L265, T14, R302, B57)
   |    |    |    |    |    |    |    |    | ['Undo Typing2', 'Undo TypingButton', 'Button3']
   |    |    |    |    |    |    |    |    | child_window(title="Undo Typing", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L302, T14, R321, B57)
   |    |    |    |    |    |    |    |    | ['More OptionsMenuItem', 'MenuItem', 'More Options', 'MenuItem0', 'MenuItem1', 'More OptionsMenuItem0', 'More OptionsMenuItem1', 'More Options0', 'More Options1']
   |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="Undo_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Repeat Typing'    (L322, T14, R364, B57)
   |    |    |    |    |    |    |    | ['Button4', 'Repeat TypingButton', 'Repeat Typing']
   |    |    |    |    |    |    |    | child_window(title="Repeat Typing", auto_id="RedoOrRepeat", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | MenuItem - 'Customize Quick Access Toolbar'    (L366, T13, R408, B59)
   |    |    |    |    |    |    |    | ['Customize Quick Access Toolbar', 'MenuItem2', 'Customize Quick Access ToolbarMenuItem']
   |    |    |    |    |    |    |    | child_window(title="Customize Quick Access Toolbar", control_type="MenuItem")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | TitleBar - '‪Document1‬  -  Word'    (L409, T0, R713, B72)
   |    |    |    |    |    |    | ['TitleBar', '\u202aDocument1\u202c  -  WordTitleBar', '\u202aDocument1\u202c  -  Word', '\u202aDocument1\u202c  -  Word0', '\u202aDocument1\u202c  -  Word1', 'TitleBar0', 'TitleBar1']
   |    |    |    |    |    |    | child_window(title="‪Document1‬  -  Word", control_type="TitleBar")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - '‪Document1‬  -  Word'    (L409, T0, R612, B72)
   |    |    |    |    |    |    |    | ['\u202aDocument1\u202c  -  WordButton', 'Button5', '\u202aDocument1\u202c  -  Word2']
   |    |    |    |    |    |    |    | child_window(title="‪Document1‬  -  Word", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | MenuItem - 'Type to search and use the up and down arrow keys to navigate'    (L713, T12, R1231, B60)
   |    |    |    |    |    |    | ['Type to search and use the up and down arrow keys to navigateMenuItem', 'MenuItem3', 'Type to search and use the up and down arrow keys to navigate']
   |    |    |    |    |    |    | child_window(title="Type to search and use the up and down arrow keys to navigate", auto_id="TellMeControlAnchor", control_type="MenuItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Edit - ''    (L774, T21, R1212, B53)
   |    |    |    |    |    |    |    | ['Edit', 'Edit0', 'Edit1']
   |    |    |    |    |    |    |    | child_window(auto_id="TellMeTextBoxAutomationId", control_type="Edit")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | MenuItem - 'Kaviya Gopi'    (L1629, T0, R1704, B72)
   |    |    |    |    |    |    | ['Kaviya GopiMenuItem', 'MenuItem4', 'Kaviya Gopi']
   |    |    |    |    |    |    | child_window(title="Kaviya Gopi", auto_id="MeControlWidget", control_type="MenuItem")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Minimize'    (L1704, T0, R1776, B72)
   |    |    |    |    |    |    | ['Minimize', 'MinimizeButton', 'Button6', 'Minimize0', 'Minimize1', 'MinimizeButton0', 'MinimizeButton1']
   |    |    |    |    |    |    | child_window(title="Minimize", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Restore Down'    (L1776, T0, R1848, B72)
   |    |    |    |    |    |    | ['Restore Down', 'Restore DownButton', 'Button7']
   |    |    |    |    |    |    | child_window(title="Restore Down", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Close'    (L1848, T0, R1920, B72)
   |    |    |    |    |    |    | ['Close', 'CloseButton', 'Button8', 'Close0', 'Close1', 'CloseButton0', 'CloseButton1']
   |    |    |    |    |    |    | child_window(title="Close", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'File Tab'    (L6, T72, R87, B117)
   |    |    |    |    |    |    | ['File TabButton', 'Button9', 'File Tab']
   |    |    |    |    |    |    | child_window(title="File Tab", auto_id="FileTabButton", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | TabControl - 'Ribbon Tabs'    (L87, T72, R1920, B117)
   |    |    |    |    |    |    | ['Ribbon Tabs', 'TabControl', 'Ribbon TabsTabControl']
   |    |    |    |    |    |    | child_window(title="Ribbon Tabs", control_type="Tab")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Home'    (L87, T72, R170, B117)
   |    |    |    |    |    |    |    | ['HomeTabItem', 'TabItem', 'Home', 'TabItem0', 'TabItem1']
   |    |    |    |    |    |    |    | child_window(title="Home", auto_id="TabHome", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Insert'    (L171, T72, R251, B117)
   |    |    |    |    |    |    |    | ['TabItem2', 'Insert', 'InsertTabItem']
   |    |    |    |    |    |    |    | child_window(title="Insert", auto_id="TabInsert", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Draw'    (L252, T72, R325, B117)
   |    |    |    |    |    |    |    | ['TabItem3', 'DrawTabItem', 'Draw']
   |    |    |    |    |    |    |    | child_window(title="Draw", auto_id="TabDrawInk", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Design'    (L326, T72, R416, B117)
   |    |    |    |    |    |    |    | ['TabItem4', 'DesignTabItem', 'Design']
   |    |    |    |    |    |    |    | child_window(title="Design", auto_id="TabWordDesign", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Layout'    (L417, T72, R505, B117)
   |    |    |    |    |    |    |    | ['TabItem5', 'Layout', 'LayoutTabItem', 'Layout0', 'Layout1']
   |    |    |    |    |    |    |    | child_window(title="Layout", auto_id="TabPageLayoutWord", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'References'    (L506, T72, R632, B117)
   |    |    |    |    |    |    |    | ['TabItem6', 'References', 'ReferencesTabItem']
   |    |    |    |    |    |    |    | child_window(title="References", auto_id="TabReferences", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Mailings'    (L633, T72, R736, B117)
   |    |    |    |    |    |    |    | ['TabItem7', 'MailingsTabItem', 'Mailings']
   |    |    |    |    |    |    |    | child_window(title="Mailings", auto_id="TabMailings", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Review'    (L737, T72, R827, B117)
   |    |    |    |    |    |    |    | ['Review', 'TabItem8', 'ReviewTabItem']
   |    |    |    |    |    |    |    | child_window(title="Review", auto_id="TabReviewWord", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'View'    (L828, T72, R899, B117)
   |    |    |    |    |    |    |    | ['View', 'TabItem9', 'ViewTabItem']
   |    |    |    |    |    |    |    | child_window(title="View", auto_id="TabView", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Help'    (L900, T72, R970, B117)
   |    |    |    |    |    |    |    | ['TabItem10', 'HelpTabItem', 'Help']
   |    |    |    |    |    |    |    | child_window(title="Help", auto_id="HelpTab", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Comments'    (L1532, T76, R1667, B112)
   |    |    |    |    |    |    |    | ['CommentsButton', 'Button10', 'Comments']
   |    |    |    |    |    |    |    | child_window(title="Comments", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | ComboBox - 'Editing'    (L1679, T76, R1803, B112)
   |    |    |    |    |    |    |    | ['ComboBox', 'Editing', 'EditingComboBox', 'ComboBox0', 'ComboBox1']
   |    |    |    |    |    |    |    | child_window(title="Editing", control_type="ComboBox")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | MenuItem - 'Share'    (L1815, T72, R1920, B117)
   |    |    |    |    |    |    |    | ['ShareMenuItem', 'MenuItem5', 'Share']
   |    |    |    |    |    |    |    | child_window(title="Share", control_type="MenuItem")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Pane - 'Lower Ribbon'    (L12, T117, R1866, B267)
   |    |    |    |    |    |    | ['Pane7', 'Lower RibbonPane', 'Lower Ribbon']
   |    |    |    |    |    |    | child_window(title="Lower Ribbon", control_type="Pane")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | GroupBox - 'Layout'    (L18, T117, R1866, B267)
   |    |    |    |    |    |    |    | ['GroupBox', 'Layout2', 'LayoutGroupBox', 'GroupBox0', 'GroupBox1']
   |    |    |    |    |    |    |    | child_window(title="Layout", control_type="Group")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Page Setup'    (L18, T120, R539, B264)
   |    |    |    |    |    |    |    |    | ['GroupBox2', 'Page SetupGroupBox', 'Page Setup']
   |    |    |    |    |    |    |    |    | child_window(title="Page Setup", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Margins'    (L30, T123, R102, B237)
   |    |    |    |    |    |    |    |    |    | ['MenuItem6', 'Margins', 'MarginsMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Margins", auto_id="PageMarginsGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Orientation'    (L105, T123, R202, B237)
   |    |    |    |    |    |    |    |    |    | ['Orientation', 'OrientationMenuItem', 'MenuItem7']
   |    |    |    |    |    |    |    |    |    | child_window(title="Orientation", auto_id="PageOrientationGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Size'    (L205, T123, R267, B237)
   |    |    |    |    |    |    |    |    |    | ['SizeMenuItem', 'MenuItem8', 'Size']
   |    |    |    |    |    |    |    |    |    | child_window(title="Size", auto_id="PageSizeGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Columns'    (L270, T123, R348, B237)
   |    |    |    |    |    |    |    |    |    | ['Columns', 'ColumnsMenuItem', 'MenuItem9']
   |    |    |    |    |    |    |    |    |    | child_window(title="Columns", auto_id="TableColumnsGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Breaks'    (L351, T123, R469, B159)
   |    |    |    |    |    |    |    |    |    | ['MenuItem10', 'Breaks', 'BreaksMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Breaks", auto_id="BreaksGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Line Numbers'    (L351, T162, R527, B198)
   |    |    |    |    |    |    |    |    |    | ['MenuItem11', 'Line Numbers', 'Line NumbersMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Line Numbers", auto_id="LineNumbersMenu", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Hyphenation'    (L351, T201, R520, B237)
   |    |    |    |    |    |    |    |    |    | ['HyphenationMenuItem', 'MenuItem12', 'Hyphenation']
   |    |    |    |    |    |    |    |    |    | child_window(title="Hyphenation", auto_id="HyphenationMenu", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Page Setup...'    (L515, T240, R539, B264)
   |    |    |    |    |    |    |    |    |    | ['Page Setup...Button', 'Button11', 'Page Setup...']
   |    |    |    |    |    |    |    |    |    | child_window(title="Page Setup...", auto_id="PageSetupDialog", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Paragraph'    (L539, T120, R971, B264)
   |    |    |    |    |    |    |    |    | ['ParagraphGroupBox', 'GroupBox3', 'Paragraph']
   |    |    |    |    |    |    |    |    | child_window(title="Paragraph", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | UpDown - '0"'    (L637, T164, R722, B195)
   |    |    |    |    |    |    |    |    |    | ['0"', 'UpDown', '0"UpDown', '0"0', '0"1', 'UpDown0', 'UpDown1', '0"UpDown0', '0"UpDown1']
   |    |    |    |    |    |    |    |    |    | child_window(title="0"", auto_id="ParagraphIndentLeft", control_type="Spinner")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'More'    (L722, T163, R748, B180)
   |    |    |    |    |    |    |    |    |    | ['MoreButton', 'More', 'Button12', 'MoreButton0', 'MoreButton1', 'More0', 'More1']
   |    |    |    |    |    |    |    |    |    | child_window(title="More", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Less'    (L722, T180, R748, B197)
   |    |    |    |    |    |    |    |    |    | ['Less', 'LessButton', 'Button13', 'Less0', 'Less1', 'LessButton0', 'LessButton1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Less", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | UpDown - '0"'    (L637, T203, R722, B234)
   |    |    |    |    |    |    |    |    |    | ['0"2', 'UpDown2', '0"UpDown2']
   |    |    |    |    |    |    |    |    |    | child_window(title="0"", auto_id="ParagraphIndentRight", control_type="Spinner")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'More'    (L722, T202, R748, B219)
   |    |    |    |    |    |    |    |    |    | ['MoreButton2', 'More2', 'Button14']
   |    |    |    |    |    |    |    |    |    | child_window(title="More", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Less'    (L722, T219, R748, B236)
   |    |    |    |    |    |    |    |    |    | ['Less2', 'LessButton2', 'Button15']
   |    |    |    |    |    |    |    |    |    | child_window(title="Less", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | UpDown - '0 pt'    (L847, T164, R932, B195)
   |    |    |    |    |    |    |    |    |    | ['0 ptUpDown', 'UpDown3', '0 pt']
   |    |    |    |    |    |    |    |    |    | child_window(title="0 pt", auto_id="ParagraphSpacingBefore", control_type="Spinner")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'More'    (L932, T163, R958, B180)
   |    |    |    |    |    |    |    |    |    | ['MoreButton3', 'More3', 'Button16']
   |    |    |    |    |    |    |    |    |    | child_window(title="More", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Less'    (L932, T180, R958, B197)
   |    |    |    |    |    |    |    |    |    | ['Less3', 'LessButton3', 'Button17']
   |    |    |    |    |    |    |    |    |    | child_window(title="Less", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | UpDown - '8 pt'    (L847, T203, R932, B234)
   |    |    |    |    |    |    |    |    |    | ['8 ptUpDown', 'UpDown4', '8 pt']
   |    |    |    |    |    |    |    |    |    | child_window(title="8 pt", auto_id="ParagraphSpacingAfter", control_type="Spinner")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'More'    (L932, T202, R958, B219)
   |    |    |    |    |    |    |    |    |    | ['MoreButton4', 'More4', 'Button18']
   |    |    |    |    |    |    |    |    |    | child_window(title="More", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Less'    (L932, T219, R958, B236)
   |    |    |    |    |    |    |    |    |    | ['Less4', 'LessButton4', 'Button19']
   |    |    |    |    |    |    |    |    |    | child_window(title="Less", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Paragraph...'    (L947, T240, R971, B264)
   |    |    |    |    |    |    |    |    |    | ['Paragraph...', 'Paragraph...Button', 'Button20']
   |    |    |    |    |    |    |    |    |    | child_window(title="Paragraph...", auto_id="ParagraphDialog", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Arrange'    (L971, T120, R1530, B264)
   |    |    |    |    |    |    |    |    | ['GroupBox4', 'ArrangeGroupBox', 'Arrange']
   |    |    |    |    |    |    |    |    | child_window(title="Arrange", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Position'    (L983, T123, R1054, B237)
   |    |    |    |    |    |    |    |    |    | ['PositionMenuItem', 'MenuItem13', 'Position', 'Position0', 'Position1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Position", auto_id="PicturePositionGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Wrap Text'    (L1057, T123, R1119, B237)
   |    |    |    |    |    |    |    |    |    | ['MenuItem14', 'Wrap Text', 'Wrap TextMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Wrap Text", auto_id="TextWrapGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Bring Forward'    (L1122, T123, R1212, B237)
   |    |    |    |    |    |    |    |    |    | ['SplitButton2', 'Bring ForwardSplitButton', 'Bring Forward', 'Bring Forward0', 'Bring Forward1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Bring Forward", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Bring Forward'    (L1122, T123, R1212, B180)
   |    |    |    |    |    |    |    |    |    |    | ['Bring ForwardButton', 'Button21', 'Bring Forward2']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Bring Forward", auto_id="ObjectBringForward", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L1122, T180, R1212, B237)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem2', 'MenuItem15', 'More Options2']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="ObjectBringForwardMenu_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Send Backward'    (L1215, T123, R1315, B237)
   |    |    |    |    |    |    |    |    |    | ['SplitButton3', 'Send BackwardSplitButton', 'Send Backward', 'Send Backward0', 'Send Backward1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Send Backward", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Send Backward'    (L1215, T123, R1315, B180)
   |    |    |    |    |    |    |    |    |    |    | ['Send Backward2', 'Send BackwardButton', 'Button22']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Send Backward", auto_id="ObjectSendBackward", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L1215, T180, R1315, B237)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem3', 'MenuItem16', 'More Options3']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="ObjectSendBackwardMenu_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Selection Pane...'    (L1318, T123, R1397, B237)
   |    |    |    |    |    |    |    |    |    | ['Button23', 'Selection Pane...', 'Selection Pane...Button']
   |    |    |    |    |    |    |    |    |    | child_window(title="Selection Pane...", auto_id="SelectionPane", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Align'    (L1400, T123, R1508, B159)
   |    |    |    |    |    |    |    |    |    | ['Align', 'MenuItem17', 'AlignMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Align", auto_id="ObjectAlignMenu", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Group'    (L1400, T162, R1517, B198)
   |    |    |    |    |    |    |    |    |    | ['MenuItem18', 'GroupMenuItem', 'Group']
   |    |    |    |    |    |    |    |    |    | child_window(title="Group", auto_id="ObjectsGroupMenu", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Rotate'    (L1400, T201, R1518, B237)
   |    |    |    |    |    |    |    |    |    | ['RotateMenuItem', 'MenuItem19', 'Rotate']
   |    |    |    |    |    |    |    |    |    | child_window(title="Rotate", auto_id="ObjectRotateGallery", control_type="MenuItem")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | MenuItem - 'Ribbon Display Options'    (L1872, T231, R1902, B261)
   |    |    |    |    |    |    | ['Ribbon Display Options', 'Ribbon Display OptionsMenuItem', 'MenuItem20']
   |    |    |    |    |    |    | child_window(title="Ribbon Display Options", control_type="MenuItem")
   | 
   | Pane - 'MsoDockBottom'    (L0, T975, R1920, B1008)
   | ['MsoDockBottom', 'MsoDockBottomPane', 'Pane8']
   | child_window(title="MsoDockBottom", control_type="Pane")
   |    | 
   |    | Toolbar - ''    (L0, T975, R1920, B1008)
   |    | ['Word Count 0 wordsToolbar', 'Toolbar3']
   |    |    | 
   |    |    | Pane - 'Status Bar'    (L0, T975, R1920, B1008)
   |    |    | ['Status Bar', 'Pane9', 'Status BarPane']
   |    |    | child_window(title="Status Bar", control_type="Pane")
   |    |    |    | 
   |    |    |    | Pane - ''    (L0, T975, R1920, B1008)
   |    |    |    | ['Pane10', 'Word Count 0 wordsPane', 'Word Count 0 wordsPane0', 'Word Count 0 wordsPane1']
   |    |    |    |    | 
   |    |    |    |    | Pane - ''    (L0, T975, R1920, B1008)
   |    |    |    |    | ['Pane11', 'Word Count 0 wordsPane2']
   |    |    |    |    |    | 
   |    |    |    |    |    | StatusBar - ''    (L0, T975, R1920, B1008)
   |    |    |    |    |    | ['StatusBar', 'Word Count 0 wordsStatusBar']
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Page Number Page 1 of 1'    (L6, T976, R106, B1008)
   |    |    |    |    |    |    | ['Page Number Page 1 of 1Button', 'Page Number Page 1 of 1', 'Button24']
   |    |    |    |    |    |    | child_window(title="Page Number Page 1 of 1", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Static - 'Word Count 0 words'    (L111, T976, R190, B1008)
   |    |    |    |    |    |    | ['Word Count 0 words', 'Word Count 0 wordsStatic', 'Static', 'Static0', 'Static1']
   |    |    |    |    |    |    | child_window(title="Word Count 0 words", control_type="Text")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Spelling and Grammar Check No Errors'    (L195, T976, R242, B1008)
   |    |    |    |    |    |    | ['Spelling and Grammar Check No Errors', 'Spelling and Grammar Check No ErrorsButton', 'Button25']
   |    |    |    |    |    |    | child_window(title="Spelling and Grammar Check No Errors", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Language English (United States)'    (L242, T976, R420, B1008)
   |    |    |    |    |    |    | ['Language English (United States)', 'Language English (United States)Button', 'Button26']
   |    |    |    |    |    |    | child_window(title="Language English (United States)", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Static - 'Text Predictions Text Predictions: On'    (L425, T976, R583, B1008)
   |    |    |    |    |    |    | ['Text Predictions Text Predictions: OnStatic', 'Text Predictions Text Predictions: On', 'Static2']
   |    |    |    |    |    |    | child_window(title="Text Predictions Text Predictions: On", control_type="Text")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Accessibility Checker Accessibility: Good to go'    (L588, T976, R807, B1008)
   |    |    |    |    |    |    | ['Button27', 'Accessibility Checker Accessibility: Good to goButton', 'Accessibility Checker Accessibility: Good to go']
   |    |    |    |    |    |    | child_window(title="Accessibility Checker Accessibility: Good to go", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Focus '    (L1363, T976, R1453, B1008)
   |    |    |    |    |    |    | ['Focus Button', 'Focus ', 'Button28']
   |    |    |    |    |    |    | child_window(title="Focus ", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Read Mode'    (L1457, T976, R1517, B1008)
   |    |    |    |    |    |    | ['Read ModeButton', 'Button29', 'Read Mode']
   |    |    |    |    |    |    | child_window(title="Read Mode", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Print Layout'    (L1517, T976, R1577, B1008)
   |    |    |    |    |    |    | ['Print Layout', 'Print LayoutButton', 'Button30']
   |    |    |    |    |    |    | child_window(title="Print Layout", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Web Layout'    (L1577, T976, R1637, B1008)
   |    |    |    |    |    |    | ['Web LayoutButton', 'Button31', 'Web Layout']
   |    |    |    |    |    |    | child_window(title="Web Layout", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Zoom Out (Ctrl -)'    (L1638, T976, R1664, B1008)
   |    |    |    |    |    |    | ['Zoom Out (Ctrl -)Button', 'Zoom Out (Ctrl -)', 'Button32']
   |    |    |    |    |    |    | child_window(title="Zoom Out (Ctrl -)", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Slider - 'Zoom'    (L1664, T976, R1814, B1008)
   |    |    |    |    |    |    | ['Slider']
   |    |    |    |    |    |    | child_window(title="Zoom", control_type="Slider")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Zoom Out'    (L1664, T976, R1739, B1008)
   |    |    |    |    |    |    |    | ['Zoom Out', 'Zoom OutButton', 'Button33']
   |    |    |    |    |    |    |    | child_window(title="Zoom Out", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Thumb - 'Position'    (L1739, T983, R1747, B1000)
   |    |    |    |    |    |    |    | ['Thumb', 'PositionThumb', 'Position2', 'Thumb0', 'Thumb1']
   |    |    |    |    |    |    |    | child_window(title="Position", control_type="Thumb")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Zoom In'    (L1747, T976, R1814, B1008)
   |    |    |    |    |    |    |    | ['Zoom InButton', 'Button34', 'Zoom In']
   |    |    |    |    |    |    |    | child_window(title="Zoom In", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Zoom In (Ctrl +)'    (L1814, T976, R1840, B1008)
   |    |    |    |    |    |    | ['Zoom In (Ctrl +)', 'Button35', 'Zoom In (Ctrl +)Button']
   |    |    |    |    |    |    | child_window(title="Zoom In (Ctrl +)", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Static - 'Zoom 120%'    (L1840, T976, R1903, B1008)
   |    |    |    |    |    |    | ['Zoom 120%Static', 'Zoom 120%', 'Static3']
   |    |    |    |    |    |    | child_window(title="Zoom 120%", control_type="Text")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Thumb - 'Size box'    (L1903, T976, R1920, B1008)
   |    |    |    |    |    |    | ['Thumb2', 'Size box', 'Size boxThumb']
   |    |    |    |    |    |    | child_window(title="Size box", control_type="Thumb")
   | 
   | Pane - ''    (L0, T267, R1920, B975)
   | ['Pane12']
   |    | 
   |    | Pane - 'Document1'    (L0, T267, R1920, B975)
   |    | ['Document1', 'Document1Pane', 'Pane13']
   |    | child_window(title="Document1", control_type="Pane")
   |    |    | 
   |    |    | Document - ''    (L0, T267, R1894, B975)
   |    |    | ['Document']
   |    |    |    | 
   |    |    |    | Custom - 'Page 1'    (L212, T298, R1682, B975)
   |    |    |    | ['Page 1Custom', 'Page 1', 'Custom']
   |    |    |    | child_window(title="Page 1", auto_id="UIA_AutomationId_Word_Page_1", control_type="Custom")
   |    |    |    |    | 
   |    |    |    |    | Edit - 'Page 1 content'    (L212, T471, R1682, B975)
   |    |    |    |    | ['Edit2']
   |    |    |    |    | child_window(title="Page 1 content", auto_id="Body", control_type="Edit")
   |    |    | 
   |    |    | Pane - 'Vertical'    (L1894, T267, R1920, B975)
   |    |    | ['Vertical', 'Pane14', 'VerticalPane']
   |    |    | child_window(title="Vertical", control_type="Pane")
   |    |    |    | 
   |    |    |    | Pane - ''    (L1894, T267, R1920, B975)
   |    |    |    | ['Pane15']
   |    |    |    |    | 
   |    |    |    |    | ScrollBar - ''    (L1894, T267, R1920, B975)
   |    |    |    |    | ['ScrollBar']
   | 
   | TitleBar - ''    (L0, T-8, R1920, B0)
   | ['TitleBar2']
   |    | 
   |    | Menu - 'System'    (L0, T0, R33, B33)
   |    | ['SystemMenu', 'Menu', 'System', 'System0', 'System1', 'Menu0', 'Menu1']
   |    | child_window(title="System", auto_id="MenuBar", control_type="MenuBar")
   |    |    | 
   |    |    | MenuItem - 'System'    (L0, T0, R33, B33)
   |    |    | ['MenuItem21', 'SystemMenuItem', 'System2']
   |    |    | child_window(title="System", control_type="MenuItem")
   |    | 
   |    | Button - 'Minimize'    (L0, T0, R0, B0)
   |    | ['Minimize2', 'MinimizeButton2', 'Button36']
   |    | child_window(title="Minimize", control_type="Button")
   |    | 
   |    | Button - 'Restore'    (L0, T0, R0, B0)
   |    | ['Restore', 'Button37', 'RestoreButton']
   |    | child_window(title="Restore", control_type="Button")
   |    | 
   |    | Button - 'Close'    (L0, T0, R0, B0)
   |    | ['Close2', 'CloseButton2', 'Button38']
   |    | child_window(title="Close", control_type="Button")
   | 
   | Menu - 'Menu Bar'    (L0, T0, R0, B0)
   | ['Menu2', 'Menu Bar', 'Menu BarMenu']
   | child_window(title="Menu Bar", control_type="MenuBar")
   |    | 
   |    | ComboBox - 'Ask a Question'    (L0, T0, R0, B0)
   |    | ['Ask a QuestionComboBox', 'ComboBox2', 'Ask a Question']
   |    | child_window(title="Ask a Question", control_type="ComboBox")"""

ui_tree3="""
Control Identifiers:

Dialog - 'Document1 - Word'    (L-11, T-11, R1931, B1019)
['Dialog', 'Document1 - Word', 'Document1 - WordDialog']
child_window(title="Document1 - Word", control_type="Window")
   | 
   | Pane - 'DropShadowTop'    (L0, T267, R1920, B276)
   | ['DropShadowTopPane', 'DropShadowTop', 'Pane', 'Pane0', 'Pane1']
   | child_window(title="DropShadowTop", control_type="Pane")
   | 
   | Pane - 'MsoDockTop'    (L0, T0, R1920, B267)
   | ['MsoDockTop', 'Pane2', 'MsoDockTopPane']
   | child_window(title="MsoDockTop", control_type="Pane")
   |    | 
   |    | Toolbar - ''    (L0, T0, R1920, B267)
   |    | ['Toolbar', 'Toolbar0', 'Toolbar1']
   |    |    | 
   |    |    | Pane - 'Ribbon'    (L0, T0, R1920, B267)
   |    |    | ['Ribbon', 'Pane3', 'RibbonPane', 'Ribbon0', 'Ribbon1', 'RibbonPane0', 'RibbonPane1']
   |    |    | child_window(title="Ribbon", control_type="Pane")
   |    |    |    | 
   |    |    |    | Pane - ''    (L0, T0, R1920, B267)
   |    |    |    | ['Pane4']
   |    |    |    |    | 
   |    |    |    |    | Pane - ''    (L0, T0, R1920, B267)
   |    |    |    |    | ['Pane5']
   |    |    |    |    |    | 
   |    |    |    |    |    | Pane - 'Ribbon'    (L0, T0, R1920, B267)
   |    |    |    |    |    | ['Ribbon2', 'Pane6', 'RibbonPane2']
   |    |    |    |    |    | child_window(title="Ribbon", control_type="Pane")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Toolbar - 'Quick Access Toolbar'    (L63, T0, R408, B72)
   |    |    |    |    |    |    | ['Quick Access Toolbar', 'Quick Access ToolbarToolbar', 'Toolbar2']
   |    |    |    |    |    |    | child_window(title="Quick Access Toolbar", control_type="ToolBar")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'AutoSave'    (L63, T14, R221, B58)
   |    |    |    |    |    |    |    | ['AutoSaveButton', 'Button', 'AutoSave', 'Button0', 'Button1']
   |    |    |    |    |    |    |    | child_window(title="AutoSave", auto_id="AutoSaveSwitch", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Save'    (L222, T14, R264, B57)
   |    |    |    |    |    |    |    | ['Save', 'Button2', 'SaveButton']
   |    |    |    |    |    |    |    | child_window(title="Save", auto_id="FileSave", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | SplitButton - 'Undo Typing'    (L265, T14, R321, B57)
   |    |    |    |    |    |    |    | ['SplitButton', 'Undo Typing', 'Undo TypingSplitButton', 'Undo Typing0', 'Undo Typing1', 'SplitButton0', 'SplitButton1']
   |    |    |    |    |    |    |    | child_window(title="Undo Typing", auto_id="Undo", control_type="SplitButton")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | Button - 'Undo Typing'    (L265, T14, R302, B57)
   |    |    |    |    |    |    |    |    | ['Undo Typing2', 'Undo TypingButton', 'Button3']
   |    |    |    |    |    |    |    |    | child_window(title="Undo Typing", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L302, T14, R321, B57)
   |    |    |    |    |    |    |    |    | ['More OptionsMenuItem', 'MenuItem', 'More Options', 'MenuItem0', 'MenuItem1', 'More OptionsMenuItem0', 'More OptionsMenuItem1', 'More Options0', 'More Options1']
   |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="Undo_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Repeat Typing'    (L322, T14, R364, B57)
   |    |    |    |    |    |    |    | ['Button4', 'Repeat TypingButton', 'Repeat Typing']
   |    |    |    |    |    |    |    | child_window(title="Repeat Typing", auto_id="RedoOrRepeat", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | MenuItem - 'Customize Quick Access Toolbar'    (L366, T13, R408, B59)
   |    |    |    |    |    |    |    | ['Customize Quick Access Toolbar', 'MenuItem2', 'Customize Quick Access ToolbarMenuItem']
   |    |    |    |    |    |    |    | child_window(title="Customize Quick Access Toolbar", control_type="MenuItem")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | TitleBar - '‪Document1‬  -  Word'    (L409, T0, R713, B72)
   |    |    |    |    |    |    | ['TitleBar', '\u202aDocument1\u202c  -  WordTitleBar', '\u202aDocument1\u202c  -  Word', '\u202aDocument1\u202c  -  Word0', '\u202aDocument1\u202c  -  Word1', 'TitleBar0', 'TitleBar1']
   |    |    |    |    |    |    | child_window(title="‪Document1‬  -  Word", control_type="TitleBar")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - '‪Document1‬  -  Word'    (L409, T0, R612, B72)
   |    |    |    |    |    |    |    | ['\u202aDocument1\u202c  -  WordButton', 'Button5', '\u202aDocument1\u202c  -  Word2']
   |    |    |    |    |    |    |    | child_window(title="‪Document1‬  -  Word", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | MenuItem - 'Type to search and use the up and down arrow keys to navigate'    (L713, T12, R1231, B60)
   |    |    |    |    |    |    | ['Type to search and use the up and down arrow keys to navigateMenuItem', 'MenuItem3', 'Type to search and use the up and down arrow keys to navigate']
   |    |    |    |    |    |    | child_window(title="Type to search and use the up and down arrow keys to navigate", auto_id="TellMeControlAnchor", control_type="MenuItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Edit - ''    (L774, T21, R1212, B53)
   |    |    |    |    |    |    |    | ['Edit', 'Edit0', 'Edit1']
   |    |    |    |    |    |    |    | child_window(auto_id="TellMeTextBoxAutomationId", control_type="Edit")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | MenuItem - 'Kaviya Gopi'    (L1629, T0, R1704, B72)
   |    |    |    |    |    |    | ['Kaviya GopiMenuItem', 'MenuItem4', 'Kaviya Gopi']
   |    |    |    |    |    |    | child_window(title="Kaviya Gopi", auto_id="MeControlWidget", control_type="MenuItem")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Minimize'    (L1704, T0, R1776, B72)
   |    |    |    |    |    |    | ['Minimize', 'MinimizeButton', 'Button6', 'Minimize0', 'Minimize1', 'MinimizeButton0', 'MinimizeButton1']
   |    |    |    |    |    |    | child_window(title="Minimize", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Restore Down'    (L1776, T0, R1848, B72)
   |    |    |    |    |    |    | ['Restore Down', 'Restore DownButton', 'Button7']
   |    |    |    |    |    |    | child_window(title="Restore Down", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Close'    (L1848, T0, R1920, B72)
   |    |    |    |    |    |    | ['Close', 'CloseButton', 'Button8', 'Close0', 'Close1', 'CloseButton0', 'CloseButton1']
   |    |    |    |    |    |    | child_window(title="Close", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'File Tab'    (L6, T72, R87, B117)
   |    |    |    |    |    |    | ['File TabButton', 'Button9', 'File Tab']
   |    |    |    |    |    |    | child_window(title="File Tab", auto_id="FileTabButton", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | TabControl - 'Ribbon Tabs'    (L87, T72, R1920, B117)
   |    |    |    |    |    |    | ['Ribbon Tabs', 'TabControl', 'Ribbon TabsTabControl']
   |    |    |    |    |    |    | child_window(title="Ribbon Tabs", control_type="Tab")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Home'    (L87, T72, R170, B117)
   |    |    |    |    |    |    |    | ['HomeTabItem', 'TabItem', 'Home', 'TabItem0', 'TabItem1']
   |    |    |    |    |    |    |    | child_window(title="Home", auto_id="TabHome", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Insert'    (L171, T72, R251, B117)
   |    |    |    |    |    |    |    | ['TabItem2', 'Insert', 'InsertTabItem']
   |    |    |    |    |    |    |    | child_window(title="Insert", auto_id="TabInsert", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Draw'    (L252, T72, R325, B117)
   |    |    |    |    |    |    |    | ['TabItem3', 'DrawTabItem', 'Draw']
   |    |    |    |    |    |    |    | child_window(title="Draw", auto_id="TabDrawInk", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Design'    (L326, T72, R416, B117)
   |    |    |    |    |    |    |    | ['TabItem4', 'DesignTabItem', 'Design']
   |    |    |    |    |    |    |    | child_window(title="Design", auto_id="TabWordDesign", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Layout'    (L417, T72, R505, B117)
   |    |    |    |    |    |    |    | ['TabItem5', 'Layout', 'LayoutTabItem', 'Layout0', 'Layout1']
   |    |    |    |    |    |    |    | child_window(title="Layout", auto_id="TabPageLayoutWord", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'References'    (L506, T72, R632, B117)
   |    |    |    |    |    |    |    | ['TabItem6', 'References', 'ReferencesTabItem']
   |    |    |    |    |    |    |    | child_window(title="References", auto_id="TabReferences", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Mailings'    (L633, T72, R736, B117)
   |    |    |    |    |    |    |    | ['TabItem7', 'MailingsTabItem', 'Mailings']
   |    |    |    |    |    |    |    | child_window(title="Mailings", auto_id="TabMailings", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Review'    (L737, T72, R827, B117)
   |    |    |    |    |    |    |    | ['Review', 'TabItem8', 'ReviewTabItem']
   |    |    |    |    |    |    |    | child_window(title="Review", auto_id="TabReviewWord", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'View'    (L828, T72, R899, B117)
   |    |    |    |    |    |    |    | ['View', 'TabItem9', 'ViewTabItem']
   |    |    |    |    |    |    |    | child_window(title="View", auto_id="TabView", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | TabItem - 'Help'    (L900, T72, R970, B117)
   |    |    |    |    |    |    |    | ['TabItem10', 'HelpTabItem', 'Help']
   |    |    |    |    |    |    |    | child_window(title="Help", auto_id="HelpTab", control_type="TabItem")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Comments'    (L1532, T76, R1667, B112)
   |    |    |    |    |    |    |    | ['CommentsButton', 'Button10', 'Comments']
   |    |    |    |    |    |    |    | child_window(title="Comments", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | ComboBox - 'Editing'    (L1679, T76, R1803, B112)
   |    |    |    |    |    |    |    | ['ComboBox', 'Editing', 'EditingComboBox', 'ComboBox0', 'ComboBox1']
   |    |    |    |    |    |    |    | child_window(title="Editing", control_type="ComboBox")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | MenuItem - 'Share'    (L1815, T72, R1920, B117)
   |    |    |    |    |    |    |    | ['ShareMenuItem', 'MenuItem5', 'Share']
   |    |    |    |    |    |    |    | child_window(title="Share", control_type="MenuItem")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Pane - 'Lower Ribbon'    (L12, T117, R1866, B267)
   |    |    |    |    |    |    | ['Pane7', 'Lower RibbonPane', 'Lower Ribbon']
   |    |    |    |    |    |    | child_window(title="Lower Ribbon", control_type="Pane")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | GroupBox - 'Layout'    (L18, T117, R1866, B267)
   |    |    |    |    |    |    |    | ['GroupBox', 'Layout2', 'LayoutGroupBox', 'GroupBox0', 'GroupBox1']
   |    |    |    |    |    |    |    | child_window(title="Layout", control_type="Group")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Page Setup'    (L18, T120, R539, B264)
   |    |    |    |    |    |    |    |    | ['GroupBox2', 'Page SetupGroupBox', 'Page Setup']
   |    |    |    |    |    |    |    |    | child_window(title="Page Setup", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Margins'    (L30, T123, R102, B237)
   |    |    |    |    |    |    |    |    |    | ['MenuItem6', 'Margins', 'MarginsMenuItem', 'Margins0', 'Margins1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Margins", auto_id="PageMarginsGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Menu - 'Margins'    (L30, T237, R451, B858)
   |    |    |    |    |    |    |    |    |    |    | ['Menu', 'MarginsMenu', 'Margins2', 'Menu0', 'Menu1', 'MarginsMenu0', 'MarginsMenu1']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Margins", control_type="Menu")
   |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    | Menu - 'Margins'    (L30, T237, R451, B858)
   |    |    |    |    |    |    |    |    |    |    |    | ['Menu2', 'MarginsMenu2', 'Margins3']
   |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Margins", control_type="Menu")
   |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    | GroupBox - ' '    (L32, T239, R423, B923)
   |    |    |    |    |    |    |    |    |    |    |    |    | [' GroupBox', 'GroupBox3', ' ', ' GroupBox0', ' GroupBox1', ' 0', ' 1']
   |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title=" ", control_type="Group")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Normal Margins'    (L32, T239, R423, B353)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Normal Margins', 'ListItem', 'Normal MarginsListItem', 'ListItem0', 'ListItem1']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Normal Margins", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Narrow Margins'    (L32, T353, R423, B467)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Narrow MarginsListItem', 'ListItem2', 'Narrow Margins']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Narrow Margins", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Moderate Margins'    (L32, T467, R423, B581)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Moderate Margins', 'ListItem3', 'Moderate MarginsListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Moderate Margins", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Wide Margins'    (L32, T581, R423, B695)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Wide MarginsListItem', 'ListItem4', 'Wide Margins']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Wide Margins", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Mirrored Margins'    (L32, T695, R423, B809)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['ListItem5', 'Mirrored MarginsListItem', 'Mirrored Margins']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Mirrored Margins", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ListItem - 'Office 2003 Default Margins'    (L32, T809, R423, B923)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Office 2003 Default Margins', 'ListItem6', 'Office 2003 Default MarginsListItem']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Office 2003 Default Margins", control_type="ListItem")
   |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    | ScrollBar - ''    (L423, T239, R449, B809)
   |    |    |    |    |    |    |    |    |    |    |    |    | ['ScrollBar', 'ScrollBar0', 'ScrollBar1']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | Button - 'Line up'    (L423, T239, R449, B265)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Line upButton', 'Line up', 'Button11', 'Line upButton0', 'Line upButton1', 'Line up0', 'Line up1']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Line up", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | Button - 'Page up'    (L0, T0, R0, B0)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Page up', 'Page upButton', 'Button12', 'Page up0', 'Page up1', 'Page upButton0', 'Page upButton1']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Page up", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | Thumb - 'Position'    (L423, T265, R449, B696)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Thumb', 'PositionThumb', 'Position', 'Position0', 'Position1', 'Thumb0', 'Thumb1', 'PositionThumb0', 'PositionThumb1']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Position", control_type="Thumb")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | Button - 'Page down'    (L423, T696, R449, B783)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Page downButton', 'Button13', 'Page down', 'Page downButton0', 'Page downButton1', 'Page down0', 'Page down1']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Page down", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | Button - 'Line down'    (L423, T783, R449, B809)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Line down', 'Line downButton', 'Button14', 'Line down0', 'Line down1', 'Line downButton0', 'Line downButton1']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Line down", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    | GroupBox - ' '    (L32, T812, R449, B856)
   |    |    |    |    |    |    |    |    |    |    |    |    | [' GroupBox2', 'GroupBox4', ' 2']
   |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title=" ", control_type="Group")
   |    |    |    |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    |    |    |    | MenuItem - 'Custom Margins...'    (L32, T812, R449, B856)
   |    |    |    |    |    |    |    |    |    |    |    |    |    | ['Custom Margins...MenuItem', 'MenuItem7', 'Custom Margins...']
   |    |    |    |    |    |    |    |    |    |    |    |    |    | child_window(title="Custom Margins...", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Orientation'    (L105, T123, R202, B237)
   |    |    |    |    |    |    |    |    |    | ['Orientation', 'OrientationMenuItem', 'MenuItem8']
   |    |    |    |    |    |    |    |    |    | child_window(title="Orientation", auto_id="PageOrientationGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Size'    (L205, T123, R267, B237)
   |    |    |    |    |    |    |    |    |    | ['SizeMenuItem', 'MenuItem9', 'Size']
   |    |    |    |    |    |    |    |    |    | child_window(title="Size", auto_id="PageSizeGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Columns'    (L270, T123, R348, B237)
   |    |    |    |    |    |    |    |    |    | ['Columns', 'ColumnsMenuItem', 'MenuItem10']
   |    |    |    |    |    |    |    |    |    | child_window(title="Columns", auto_id="TableColumnsGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Breaks'    (L351, T123, R469, B159)
   |    |    |    |    |    |    |    |    |    | ['MenuItem11', 'Breaks', 'BreaksMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Breaks", auto_id="BreaksGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Line Numbers'    (L351, T162, R527, B198)
   |    |    |    |    |    |    |    |    |    | ['MenuItem12', 'Line Numbers', 'Line NumbersMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Line Numbers", auto_id="LineNumbersMenu", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Hyphenation'    (L351, T201, R520, B237)
   |    |    |    |    |    |    |    |    |    | ['HyphenationMenuItem', 'MenuItem13', 'Hyphenation']
   |    |    |    |    |    |    |    |    |    | child_window(title="Hyphenation", auto_id="HyphenationMenu", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Page Setup...'    (L515, T240, R539, B264)
   |    |    |    |    |    |    |    |    |    | ['Page Setup...Button', 'Button15', 'Page Setup...']
   |    |    |    |    |    |    |    |    |    | child_window(title="Page Setup...", auto_id="PageSetupDialog", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Paragraph'    (L539, T120, R971, B264)
   |    |    |    |    |    |    |    |    | ['ParagraphGroupBox', 'GroupBox5', 'Paragraph']
   |    |    |    |    |    |    |    |    | child_window(title="Paragraph", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | UpDown - '0"'    (L637, T164, R722, B195)
   |    |    |    |    |    |    |    |    |    | ['0"', 'UpDown', '0"UpDown', '0"0', '0"1', 'UpDown0', 'UpDown1', '0"UpDown0', '0"UpDown1']
   |    |    |    |    |    |    |    |    |    | child_window(title="0"", auto_id="ParagraphIndentLeft", control_type="Spinner")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'More'    (L722, T163, R748, B180)
   |    |    |    |    |    |    |    |    |    | ['MoreButton', 'More', 'Button16', 'MoreButton0', 'MoreButton1', 'More0', 'More1']
   |    |    |    |    |    |    |    |    |    | child_window(title="More", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Less'    (L722, T180, R748, B197)
   |    |    |    |    |    |    |    |    |    | ['Less', 'LessButton', 'Button17', 'Less0', 'Less1', 'LessButton0', 'LessButton1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Less", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | UpDown - '0"'    (L637, T203, R722, B234)
   |    |    |    |    |    |    |    |    |    | ['0"2', 'UpDown2', '0"UpDown2']
   |    |    |    |    |    |    |    |    |    | child_window(title="0"", auto_id="ParagraphIndentRight", control_type="Spinner")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'More'    (L722, T202, R748, B219)
   |    |    |    |    |    |    |    |    |    | ['MoreButton2', 'More2', 'Button18']
   |    |    |    |    |    |    |    |    |    | child_window(title="More", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Less'    (L722, T219, R748, B236)
   |    |    |    |    |    |    |    |    |    | ['Less2', 'LessButton2', 'Button19']
   |    |    |    |    |    |    |    |    |    | child_window(title="Less", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | UpDown - '0 pt'    (L847, T164, R932, B195)
   |    |    |    |    |    |    |    |    |    | ['0 ptUpDown', 'UpDown3', '0 pt']
   |    |    |    |    |    |    |    |    |    | child_window(title="0 pt", auto_id="ParagraphSpacingBefore", control_type="Spinner")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'More'    (L932, T163, R958, B180)
   |    |    |    |    |    |    |    |    |    | ['MoreButton3', 'More3', 'Button20']
   |    |    |    |    |    |    |    |    |    | child_window(title="More", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Less'    (L932, T180, R958, B197)
   |    |    |    |    |    |    |    |    |    | ['Less3', 'LessButton3', 'Button21']
   |    |    |    |    |    |    |    |    |    | child_window(title="Less", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | UpDown - '8 pt'    (L847, T203, R932, B234)
   |    |    |    |    |    |    |    |    |    | ['8 ptUpDown', 'UpDown4', '8 pt']
   |    |    |    |    |    |    |    |    |    | child_window(title="8 pt", auto_id="ParagraphSpacingAfter", control_type="Spinner")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'More'    (L932, T202, R958, B219)
   |    |    |    |    |    |    |    |    |    | ['MoreButton4', 'More4', 'Button22']
   |    |    |    |    |    |    |    |    |    | child_window(title="More", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Less'    (L932, T219, R958, B236)
   |    |    |    |    |    |    |    |    |    | ['Less4', 'LessButton4', 'Button23']
   |    |    |    |    |    |    |    |    |    | child_window(title="Less", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Paragraph...'    (L947, T240, R971, B264)
   |    |    |    |    |    |    |    |    |    | ['Paragraph...', 'Paragraph...Button', 'Button24']
   |    |    |    |    |    |    |    |    |    | child_window(title="Paragraph...", auto_id="ParagraphDialog", control_type="Button")
   |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    | GroupBox - 'Arrange'    (L971, T120, R1530, B264)
   |    |    |    |    |    |    |    |    | ['GroupBox6', 'ArrangeGroupBox', 'Arrange']
   |    |    |    |    |    |    |    |    | child_window(title="Arrange", control_type="Group")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Position'    (L983, T123, R1054, B237)
   |    |    |    |    |    |    |    |    |    | ['PositionMenuItem', 'MenuItem14', 'Position2']
   |    |    |    |    |    |    |    |    |    | child_window(title="Position", auto_id="PicturePositionGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Wrap Text'    (L1057, T123, R1119, B237)
   |    |    |    |    |    |    |    |    |    | ['MenuItem15', 'Wrap Text', 'Wrap TextMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Wrap Text", auto_id="TextWrapGallery", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Bring Forward'    (L1122, T123, R1212, B237)
   |    |    |    |    |    |    |    |    |    | ['SplitButton2', 'Bring ForwardSplitButton', 'Bring Forward', 'Bring Forward0', 'Bring Forward1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Bring Forward", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Bring Forward'    (L1122, T123, R1212, B180)
   |    |    |    |    |    |    |    |    |    |    | ['Bring ForwardButton', 'Button25', 'Bring Forward2']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Bring Forward", auto_id="ObjectBringForward", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L1122, T180, R1212, B237)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem2', 'MenuItem16', 'More Options2']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="ObjectBringForwardMenu_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | SplitButton - 'Send Backward'    (L1215, T123, R1315, B237)
   |    |    |    |    |    |    |    |    |    | ['SplitButton3', 'Send BackwardSplitButton', 'Send Backward', 'Send Backward0', 'Send Backward1']
   |    |    |    |    |    |    |    |    |    | child_window(title="Send Backward", control_type="SplitButton")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | Button - 'Send Backward'    (L1215, T123, R1315, B180)
   |    |    |    |    |    |    |    |    |    |    | ['Send Backward2', 'Send BackwardButton', 'Button26']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="Send Backward", auto_id="ObjectSendBackward", control_type="Button")
   |    |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    |    | MenuItem - 'More Options'    (L1215, T180, R1315, B237)
   |    |    |    |    |    |    |    |    |    |    | ['More OptionsMenuItem3', 'MenuItem17', 'More Options3']
   |    |    |    |    |    |    |    |    |    |    | child_window(title="More Options", auto_id="ObjectSendBackwardMenu_Dropdown", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | Button - 'Selection Pane...'    (L1318, T123, R1397, B237)
   |    |    |    |    |    |    |    |    |    | ['Button27', 'Selection Pane...', 'Selection Pane...Button']
   |    |    |    |    |    |    |    |    |    | child_window(title="Selection Pane...", auto_id="SelectionPane", control_type="Button")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Align'    (L1400, T123, R1508, B159)
   |    |    |    |    |    |    |    |    |    | ['Align', 'MenuItem18', 'AlignMenuItem']
   |    |    |    |    |    |    |    |    |    | child_window(title="Align", auto_id="ObjectAlignMenu", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Group'    (L1400, T162, R1517, B198)
   |    |    |    |    |    |    |    |    |    | ['MenuItem19', 'GroupMenuItem', 'Group']
   |    |    |    |    |    |    |    |    |    | child_window(title="Group", auto_id="ObjectsGroupMenu", control_type="MenuItem")
   |    |    |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    |    |    | MenuItem - 'Rotate'    (L1400, T201, R1518, B237)
   |    |    |    |    |    |    |    |    |    | ['RotateMenuItem', 'MenuItem20', 'Rotate']
   |    |    |    |    |    |    |    |    |    | child_window(title="Rotate", auto_id="ObjectRotateGallery", control_type="MenuItem")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | MenuItem - 'Ribbon Display Options'    (L1872, T231, R1902, B261)
   |    |    |    |    |    |    | ['Ribbon Display Options', 'Ribbon Display OptionsMenuItem', 'MenuItem21']
   |    |    |    |    |    |    | child_window(title="Ribbon Display Options", control_type="MenuItem")
   | 
   | Pane - 'MsoDockBottom'    (L0, T975, R1920, B1008)
   | ['MsoDockBottom', 'MsoDockBottomPane', 'Pane8']
   | child_window(title="MsoDockBottom", control_type="Pane")
   |    | 
   |    | Toolbar - ''    (L0, T975, R1920, B1008)
   |    | ['Word Count 0 wordsToolbar', 'Toolbar3']
   |    |    | 
   |    |    | Pane - 'Status Bar'    (L0, T975, R1920, B1008)
   |    |    | ['Status Bar', 'Pane9', 'Status BarPane']
   |    |    | child_window(title="Status Bar", control_type="Pane")
   |    |    |    | 
   |    |    |    | Pane - ''    (L0, T975, R1920, B1008)
   |    |    |    | ['Pane10', 'Word Count 0 wordsPane', 'Word Count 0 wordsPane0', 'Word Count 0 wordsPane1']
   |    |    |    |    | 
   |    |    |    |    | Pane - ''    (L0, T975, R1920, B1008)
   |    |    |    |    | ['Pane11', 'Word Count 0 wordsPane2']
   |    |    |    |    |    | 
   |    |    |    |    |    | StatusBar - ''    (L0, T975, R1920, B1008)
   |    |    |    |    |    | ['StatusBar', 'Word Count 0 wordsStatusBar']
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Page Number Page 1 of 1'    (L6, T976, R106, B1008)
   |    |    |    |    |    |    | ['Page Number Page 1 of 1Button', 'Page Number Page 1 of 1', 'Button28']
   |    |    |    |    |    |    | child_window(title="Page Number Page 1 of 1", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Static - 'Word Count 0 words'    (L111, T976, R190, B1008)
   |    |    |    |    |    |    | ['Word Count 0 words', 'Word Count 0 wordsStatic', 'Static', 'Static0', 'Static1']
   |    |    |    |    |    |    | child_window(title="Word Count 0 words", control_type="Text")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Spelling and Grammar Check No Errors'    (L195, T976, R242, B1008)
   |    |    |    |    |    |    | ['Spelling and Grammar Check No Errors', 'Spelling and Grammar Check No ErrorsButton', 'Button29']
   |    |    |    |    |    |    | child_window(title="Spelling and Grammar Check No Errors", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Language English (United States)'    (L242, T976, R420, B1008)
   |    |    |    |    |    |    | ['Language English (United States)', 'Language English (United States)Button', 'Button30']
   |    |    |    |    |    |    | child_window(title="Language English (United States)", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Static - 'Text Predictions Text Predictions: On'    (L425, T976, R583, B1008)
   |    |    |    |    |    |    | ['Text Predictions Text Predictions: OnStatic', 'Text Predictions Text Predictions: On', 'Static2']
   |    |    |    |    |    |    | child_window(title="Text Predictions Text Predictions: On", control_type="Text")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Accessibility Checker Accessibility: Good to go'    (L588, T976, R807, B1008)
   |    |    |    |    |    |    | ['Button31', 'Accessibility Checker Accessibility: Good to goButton', 'Accessibility Checker Accessibility: Good to go']
   |    |    |    |    |    |    | child_window(title="Accessibility Checker Accessibility: Good to go", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Focus '    (L1363, T976, R1453, B1008)
   |    |    |    |    |    |    | ['Focus Button', 'Focus ', 'Button32']
   |    |    |    |    |    |    | child_window(title="Focus ", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Read Mode'    (L1457, T976, R1517, B1008)
   |    |    |    |    |    |    | ['Read ModeButton', 'Button33', 'Read Mode']
   |    |    |    |    |    |    | child_window(title="Read Mode", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Print Layout'    (L1517, T976, R1577, B1008)
   |    |    |    |    |    |    | ['Print Layout', 'Print LayoutButton', 'Button34']
   |    |    |    |    |    |    | child_window(title="Print Layout", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Web Layout'    (L1577, T976, R1637, B1008)
   |    |    |    |    |    |    | ['Web LayoutButton', 'Button35', 'Web Layout']
   |    |    |    |    |    |    | child_window(title="Web Layout", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Zoom Out (Ctrl -)'    (L1638, T976, R1664, B1008)
   |    |    |    |    |    |    | ['Zoom Out (Ctrl -)Button', 'Zoom Out (Ctrl -)', 'Button36']
   |    |    |    |    |    |    | child_window(title="Zoom Out (Ctrl -)", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Slider - 'Zoom'    (L1664, T976, R1814, B1008)
   |    |    |    |    |    |    | ['Slider']
   |    |    |    |    |    |    | child_window(title="Zoom", control_type="Slider")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Zoom Out'    (L1664, T976, R1739, B1008)
   |    |    |    |    |    |    |    | ['Zoom Out', 'Zoom OutButton', 'Button37']
   |    |    |    |    |    |    |    | child_window(title="Zoom Out", control_type="Button")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Thumb - 'Position'    (L1739, T983, R1747, B1000)
   |    |    |    |    |    |    |    | ['Thumb2', 'PositionThumb2', 'Position3']
   |    |    |    |    |    |    |    | child_window(title="Position", control_type="Thumb")
   |    |    |    |    |    |    |    | 
   |    |    |    |    |    |    |    | Button - 'Zoom In'    (L1747, T976, R1814, B1008)
   |    |    |    |    |    |    |    | ['Zoom InButton', 'Button38', 'Zoom In']
   |    |    |    |    |    |    |    | child_window(title="Zoom In", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Button - 'Zoom In (Ctrl +)'    (L1814, T976, R1840, B1008)
   |    |    |    |    |    |    | ['Zoom In (Ctrl +)', 'Button39', 'Zoom In (Ctrl +)Button']
   |    |    |    |    |    |    | child_window(title="Zoom In (Ctrl +)", control_type="Button")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Static - 'Zoom 120%'    (L1840, T976, R1903, B1008)
   |    |    |    |    |    |    | ['Zoom 120%Static', 'Zoom 120%', 'Static3']
   |    |    |    |    |    |    | child_window(title="Zoom 120%", control_type="Text")
   |    |    |    |    |    |    | 
   |    |    |    |    |    |    | Thumb - 'Size box'    (L1903, T976, R1920, B1008)
   |    |    |    |    |    |    | ['Thumb3', 'Size box', 'Size boxThumb']
   |    |    |    |    |    |    | child_window(title="Size box", control_type="Thumb")
   | 
   | Pane - ''    (L0, T267, R1920, B975)
   | ['Pane12']
   |    | 
   |    | Pane - 'Document1'    (L0, T267, R1920, B975)
   |    | ['Document1', 'Document1Pane', 'Pane13']
   |    | child_window(title="Document1", control_type="Pane")
   |    |    | 
   |    |    | Document - ''    (L0, T267, R1894, B975)
   |    |    | ['Document']
   |    |    |    | 
   |    |    |    | Custom - 'Page 1'    (L212, T298, R1682, B975)
   |    |    |    | ['Page 1Custom', 'Page 1', 'Custom']
   |    |    |    | child_window(title="Page 1", auto_id="UIA_AutomationId_Word_Page_1", control_type="Custom")
   |    |    |    |    | 
   |    |    |    |    | Edit - 'Page 1 content'    (L212, T471, R1682, B975)
   |    |    |    |    | ['Edit2']
   |    |    |    |    | child_window(title="Page 1 content", auto_id="Body", control_type="Edit")
   |    |    | 
   |    |    | Pane - 'Vertical'    (L1894, T267, R1920, B975)
   |    |    | ['Vertical', 'Pane14', 'VerticalPane']
   |    |    | child_window(title="Vertical", control_type="Pane")
   |    |    |    | 
   |    |    |    | Pane - ''    (L1894, T267, R1920, B975)
   |    |    |    | ['Pane15']
   |    |    |    |    | 
   |    |    |    |    | ScrollBar - ''    (L1894, T267, R1920, B975)
   |    |    |    |    | ['ScrollBar2']
   |    |    |    |    |    | 
   |    |    |    |    |    | Button - 'Line up'    (L1894, T267, R1920, B293)
   |    |    |    |    |    | ['Line upButton2', 'Line up2', 'Button40']
   |    |    |    |    |    | child_window(title="Line up", control_type="Button")
   |    |    |    |    |    | 
   |    |    |    |    |    | Button - 'Page up'    (L0, T0, R0, B0)
   |    |    |    |    |    | ['Page up2', 'Page upButton2', 'Button41']
   |    |    |    |    |    | child_window(title="Page up", control_type="Button")
   |    |    |    |    |    | 
   |    |    |    |    |    | Thumb - ''    (L1894, T293, R1920, B529)
   |    |    |    |    |    | ['Thumb4']
   |    |    |    |    |    | 
   |    |    |    |    |    | Button - 'Page down'    (L1894, T529, R1920, B949)
   |    |    |    |    |    | ['Page downButton2', 'Button42', 'Page down2']
   |    |    |    |    |    | child_window(title="Page down", control_type="Button")
   |    |    |    |    |    | 
   |    |    |    |    |    | Button - 'Line down'    (L1894, T949, R1920, B975)
   |    |    |    |    |    | ['Line down2', 'Line downButton2', 'Button43']
   |    |    |    |    |    | child_window(title="Line down", control_type="Button")
   | 
   | TitleBar - ''    (L0, T-8, R1920, B0)
   | ['TitleBar2']
   |    | 
   |    | Menu - 'System'    (L0, T0, R33, B33)
   |    | ['SystemMenu', 'Menu3', 'System', 'System0', 'System1']
   |    | child_window(title="System", auto_id="MenuBar", control_type="MenuBar")
   |    |    | 
   |    |    | MenuItem - 'System'    (L0, T0, R33, B33)
   |    |    | ['MenuItem22', 'SystemMenuItem', 'System2']
   |    |    | child_window(title="System", control_type="MenuItem")
   |    | 
   |    | Button - 'Minimize'    (L0, T0, R0, B0)
   |    | ['Minimize2', 'MinimizeButton2', 'Button44']
   |    | child_window(title="Minimize", control_type="Button")
   |    | 
   |    | Button - 'Restore'    (L0, T0, R0, B0)
   |    | ['Restore', 'Button45', 'RestoreButton']
   |    | child_window(title="Restore", control_type="Button")
   |    | 
   |    | Button - 'Close'    (L0, T0, R0, B0)
   |    | ['Close2', 'CloseButton2', 'Button46']
   |    | child_window(title="Close", control_type="Button")
   | 
   | Menu - 'Menu Bar'    (L0, T0, R0, B0)
   | ['Menu4', 'Menu Bar', 'Menu BarMenu']
   | child_window(title="Menu Bar", control_type="MenuBar")
   |    | 
   |    | ComboBox - 'Ask a Question'    (L0, T0, R0, B0)
   |    | ['Ask a QuestionComboBox', 'ComboBox2', 'Ask a Question']
   |    | child_window(title="Ask a Question", control_type="ComboBox")"""
