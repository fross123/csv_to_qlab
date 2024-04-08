"use strict";(self.webpackChunkcsv_to_qlab=self.webpackChunkcsv_to_qlab||[]).push([[1535],{5184:(e,i,n)=>{n.r(i),n.d(i,{assets:()=>d,contentTitle:()=>r,default:()=>h,frontMatter:()=>l,metadata:()=>a,toc:()=>o});var s=n(4848),t=n(8453);const l={sidebar_position:2},r="Prepare a CSV File",a={id:"tutorial-basics/prepare-csv-file",title:"Prepare a CSV File",description:"Examples",source:"@site/docs/tutorial-basics/prepare-csv-file.md",sourceDirName:"tutorial-basics",slug:"/tutorial-basics/prepare-csv-file",permalink:"/docs/tutorial-basics/prepare-csv-file",draft:!1,unlisted:!1,editUrl:"https://github.com/fross123/csv_to_qlab/edit/main/website/docs/tutorial-basics/prepare-csv-file.md",tags:[],version:"current",sidebarPosition:2,frontMatter:{sidebar_position:2},sidebar:"tutorialSidebar",previous:{title:"Installation",permalink:"/docs/tutorial-basics/installation"},next:{title:"Send a File to QLab",permalink:"/docs/tutorial-basics/send-to-qlab"}},d={},o=[{value:"Examples",id:"examples",level:2},{value:"Required columns",id:"required-columns",level:2},{value:"Optional Columns",id:"optional-columns",level:2},{value:"Notes",id:"notes",level:4},{value:"Follow",id:"follow",level:4},{value:"Color",id:"color",level:4},{value:"Target",id:"target",level:4},{value:"File Target",id:"file-target",level:4},{value:"Cue types with additional options",id:"cue-types-with-additional-options",level:2},{value:"Group Cues",id:"group-cues",level:3},{value:"Group Mode",id:"group-mode",level:4},{value:"Text Cues",id:"text-cues",level:3},{value:"Text",id:"text",level:4},{value:"Fade Cues",id:"fade-cues",level:3},{value:"Stop Target When Done",id:"stop-target-when-done",level:4},{value:"Fade Opacity",id:"fade-opacity",level:4},{value:"Video Cues",id:"video-cues",level:3},{value:"Stage Number",id:"stage-number",level:4},{value:"MIDI Cues",id:"midi-cues",level:3},{value:"MIDI Message Type",id:"midi-message-type",level:4},{value:"MIDI Q Number",id:"midi-q-number",level:4},{value:"MIDI Q List",id:"midi-q-list",level:4},{value:"MIDI Device ID",id:"midi-device-id",level:4},{value:"MIDI Control Number",id:"midi-control-number",level:4},{value:"MIDI Control Value",id:"midi-control-value",level:4},{value:"MIDI Patch Name",id:"midi-patch-name",level:4},{value:"MIDI Patch Number",id:"midi-patch-number",level:4},{value:"MIDI Raw String",id:"midi-raw-string",level:4},{value:"MIDI Command Format",id:"midi-command-format",level:4},{value:"MIDI Command",id:"midi-command",level:4},{value:"Network Cues",id:"network-cues",level:3},{value:"QLab 5",id:"qlab-5",level:4},{value:"Network Patch Number",id:"network-patch-number",level:5},{value:"Network Patch Name",id:"network-patch-name",level:5},{value:"Custom String",id:"custom-string",level:5},{value:"QLab 4",id:"qlab-4",level:4},{value:"Message Type",id:"message-type",level:5},{value:"OSC Cue Number",id:"osc-cue-number",level:5},{value:"Command",id:"command",level:5}];function c(e){const i={a:"a",admonition:"admonition",h1:"h1",h2:"h2",h3:"h3",h4:"h4",h5:"h5",hr:"hr",li:"li",p:"p",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",ul:"ul",...(0,t.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(i.h1,{id:"prepare-a-csv-file",children:"Prepare a CSV File"}),"\n",(0,s.jsx)(i.h2,{id:"examples",children:"Examples"}),"\n",(0,s.jsxs)(i.ul,{children:["\n",(0,s.jsxs)(i.li,{children:["\n",(0,s.jsx)(i.p,{children:(0,s.jsx)(i.a,{href:"https://github.com/fross123/csv_to_qlab/blob/main/app/static/example_file/example.csv",children:"Full Example Spreadsheet"})}),"\n"]}),"\n",(0,s.jsxs)(i.li,{children:["\n",(0,s.jsx)(i.p,{children:(0,s.jsx)(i.a,{href:"https://github.com/fross123/csv_to_qlab/blob/main/app/static/example_file/simple.csv",children:"Simple Example Spreadsheet"})}),"\n"]}),"\n"]}),"\n",(0,s.jsx)(i.h2,{id:"required-columns",children:"Required columns"}),"\n",(0,s.jsxs)(i.ul,{children:["\n",(0,s.jsx)(i.li,{children:"Number"}),"\n",(0,s.jsx)(i.li,{children:"Type"}),"\n",(0,s.jsx)(i.li,{children:"Name"}),"\n"]}),"\n",(0,s.jsxs)(i.table,{children:[(0,s.jsx)(i.thead,{children:(0,s.jsxs)(i.tr,{children:[(0,s.jsx)(i.th,{children:"Number"}),(0,s.jsx)(i.th,{children:"Type"}),(0,s.jsx)(i.th,{children:"Name"})]})}),(0,s.jsx)(i.tbody,{children:(0,s.jsxs)(i.tr,{children:[(0,s.jsx)(i.td,{children:"12"}),(0,s.jsx)(i.td,{children:"start"}),(0,s.jsx)(i.td,{children:"Cue 12 GO"})]})})]}),"\n",(0,s.jsx)(i.hr,{}),"\n",(0,s.jsx)(i.h2,{id:"optional-columns",children:"Optional Columns"}),"\n",(0,s.jsx)(i.h4,{id:"notes",children:"Notes"}),"\n",(0,s.jsx)(i.p,{children:'Anything you would like to go in the "Notes" area of the cue.'}),"\n",(0,s.jsx)(i.h4,{id:"follow",children:"Follow"}),"\n",(0,s.jsx)(i.admonition,{type:"tip",children:(0,s.jsx)(i.p,{children:"0, 1, 2 are the only options and the data must be a single number."})}),"\n",(0,s.jsxs)(i.ul,{children:["\n",(0,s.jsx)(i.li,{children:"0 - No Follow"}),"\n",(0,s.jsx)(i.li,{children:"1 - Auto-Continue"}),"\n",(0,s.jsx)(i.li,{children:"2 - Auto-Follow"}),"\n"]}),"\n",(0,s.jsx)(i.h4,{id:"color",children:"Color"}),"\n",(0,s.jsxs)(i.p,{children:["The color of the cue. See ",(0,s.jsx)(i.a,{href:"https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercolorname-string",children:"QLab's Color Options"})]}),"\n",(0,s.jsx)(i.h4,{id:"target",children:"Target"}),"\n",(0,s.jsx)(i.p,{children:"The cue's target. The cue being targeted must be above the cue being created."}),"\n",(0,s.jsx)(i.h4,{id:"file-target",children:"File Target"}),"\n",(0,s.jsx)(i.p,{children:"The location of assets for QLab to retrieve."}),"\n",(0,s.jsx)(i.p,{children:"Available types:"}),"\n",(0,s.jsxs)(i.ul,{children:["\n",(0,s.jsx)(i.li,{children:"Full paths, e.g. /Volumes/MyDisk/path/to/some/file.wav"}),"\n",(0,s.jsx)(i.li,{children:"Paths beginning with a tilde, e.g. ~/path/to some/file.mov"}),"\n",(0,s.jsx)(i.li,{children:"Relative paths, e.g. this/is/a/relative/path.mid"}),"\n",(0,s.jsx)(i.li,{children:"Paths beginning with a tilde (~) will be expanded; the tilde signifies \u201crelative to the user\u2019s home directory\u201d."}),"\n"]}),"\n",(0,s.jsx)(i.hr,{}),"\n",(0,s.jsx)(i.h2,{id:"cue-types-with-additional-options",children:"Cue types with additional options"}),"\n",(0,s.jsx)(i.h3,{id:"group-cues",children:"Group Cues"}),"\n",(0,s.jsx)(i.h4,{id:"group-mode",children:"Group Mode"}),"\n",(0,s.jsx)(i.admonition,{type:"info",children:(0,s.jsx)(i.p,{children:'Pre-Release - "Group Mode" is only available when run from source code.'})}),"\n",(0,s.jsxs)(i.p,{children:[(0,s.jsx)(i.a,{href:"https://qlab.app/docs/v5/scripting/osc-dictionary-v5/#cuecue_numbermode-number",children:"Options"}),":"]}),"\n",(0,s.jsxs)(i.ul,{children:["\n",(0,s.jsx)(i.li,{children:"0 - List"}),"\n",(0,s.jsx)(i.li,{children:"1 - Start first and enter"}),"\n",(0,s.jsx)(i.li,{children:"2 - Start first"}),"\n",(0,s.jsx)(i.li,{children:"3 - Timeline"}),"\n",(0,s.jsx)(i.li,{children:"4 - Start random"}),"\n",(0,s.jsx)(i.li,{children:"6 - Playlist"}),"\n"]}),"\n",(0,s.jsx)(i.admonition,{type:"tip",children:(0,s.jsx)(i.p,{children:'This is not a typo, "6" is for Playlist type.'})}),"\n",(0,s.jsx)(i.hr,{}),"\n",(0,s.jsx)(i.h3,{id:"text-cues",children:"Text Cues"}),"\n",(0,s.jsx)(i.h4,{id:"text",children:"Text"}),"\n",(0,s.jsx)(i.p,{children:"The text to enter into the text cue."}),"\n",(0,s.jsx)(i.hr,{}),"\n",(0,s.jsx)(i.h3,{id:"fade-cues",children:"Fade Cues"}),"\n",(0,s.jsx)(i.h4,{id:"stop-target-when-done",children:"Stop Target When Done"}),"\n",(0,s.jsx)(i.p,{children:'This accepts either "true" or "false" to check the box for "Stop Target When Done"'}),"\n",(0,s.jsx)(i.h4,{id:"fade-opacity",children:"Fade Opacity"}),"\n",(0,s.jsx)(i.p,{children:"Per QLab Docs, only 0 or 1 is accepted."}),"\n",(0,s.jsx)(i.admonition,{type:"tip",children:(0,s.jsx)(i.p,{children:"Also activates the checkbox next to opacity"})}),"\n",(0,s.jsx)(i.hr,{}),"\n",(0,s.jsx)(i.h3,{id:"video-cues",children:"Video Cues"}),"\n",(0,s.jsx)(i.h4,{id:"stage-number",children:"Stage Number"}),"\n",(0,s.jsx)(i.p,{children:'The stage number in order of the list in the "video outputs" setting'}),"\n",(0,s.jsx)(i.admonition,{type:"tip",children:(0,s.jsx)(i.p,{children:"Stages are in QLab 5 only."})}),"\n",(0,s.jsx)(i.hr,{}),"\n",(0,s.jsx)(i.h3,{id:"midi-cues",children:"MIDI Cues"}),"\n",(0,s.jsx)(i.h4,{id:"midi-message-type",children:"MIDI Message Type"}),"\n",(0,s.jsxs)(i.ul,{children:["\n",(0,s.jsx)(i.li,{children:'1 - MIDI Voice Message ("Musical MIDI")'}),"\n",(0,s.jsx)(i.li,{children:"2 - MIDI Show Control Message (MSC)"}),"\n",(0,s.jsx)(i.li,{children:"3 - MIDI SysEx Message"}),"\n"]}),"\n",(0,s.jsx)(i.h4,{id:"midi-q-number",children:"MIDI Q Number"}),"\n",(0,s.jsx)(i.p,{children:"The number of the cue. Specific to MSC cue types."}),"\n",(0,s.jsx)(i.h4,{id:"midi-q-list",children:"MIDI Q List"}),"\n",(0,s.jsx)(i.p,{children:"The Cue List for the MSC cue."}),"\n",(0,s.jsx)(i.h4,{id:"midi-device-id",children:"MIDI Device ID"}),"\n",(0,s.jsx)(i.h4,{id:"midi-control-number",children:"MIDI Control Number"}),"\n",(0,s.jsx)(i.h4,{id:"midi-control-value",children:"MIDI Control Value"}),"\n",(0,s.jsx)(i.h4,{id:"midi-patch-name",children:"MIDI Patch Name"}),"\n",(0,s.jsx)(i.p,{children:"The Name of the MIDI Patch"}),"\n",(0,s.jsx)(i.h4,{id:"midi-patch-number",children:"MIDI Patch Number"}),"\n",(0,s.jsx)(i.p,{children:"The patch of the MIDI cue in order by the workspace settings. Index 1 means the first patch in the patch list in Workspace Settings."}),"\n",(0,s.jsx)(i.h4,{id:"midi-raw-string",children:"MIDI Raw String"}),"\n",(0,s.jsx)(i.admonition,{type:"info",children:(0,s.jsx)(i.p,{children:'Pre-Release - "MIDI Raw String" is currently only available when run from source code.'})}),"\n",(0,s.jsx)(i.p,{children:"For Midi SysEx Messages"}),"\n",(0,s.jsx)(i.h4,{id:"midi-command-format",children:"MIDI Command Format"}),"\n",(0,s.jsx)(i.p,{children:(0,s.jsx)(i.a,{href:"https://qlab.app/docs/v5/scripting/parameter-reference/#midi-show-control-command-format-types",children:"Reference QLab Docs"})}),"\n",(0,s.jsx)(i.h4,{id:"midi-command",children:"MIDI Command"}),"\n",(0,s.jsx)(i.p,{children:(0,s.jsx)(i.a,{href:"https://qlab.app/docs/v5/scripting/parameter-reference/#midi-show-control-commands",children:"Reference QLab Docs"})}),"\n",(0,s.jsx)(i.hr,{}),"\n",(0,s.jsx)(i.h3,{id:"network-cues",children:"Network Cues"}),"\n",(0,s.jsx)(i.p,{children:"The way network cues work is slightly different in QLab 4 vs QLab 5"}),"\n",(0,s.jsx)(i.h4,{id:"qlab-5",children:"QLab 5"}),"\n",(0,s.jsx)(i.h5,{id:"network-patch-number",children:"Network Patch Number"}),"\n",(0,s.jsx)(i.p,{children:"The number of the network patch."}),"\n",(0,s.jsx)(i.h5,{id:"network-patch-name",children:"Network Patch Name"}),"\n",(0,s.jsx)(i.p,{children:"The Name of the network patch."}),"\n",(0,s.jsx)(i.h5,{id:"custom-string",children:"Custom String"}),"\n",(0,s.jsx)(i.p,{children:"The best way to facilitate the vast amount of commands available in QLab 5 was to use custom string. You should be able to craft desired strings easily using common spreadsheet formulas and tools."}),"\n",(0,s.jsx)(i.h4,{id:"qlab-4",children:"QLab 4"}),"\n",(0,s.jsx)(i.p,{children:"There are no plans to remove these features, but we will post here on this site if/when support for QLab 4 ends."}),"\n",(0,s.jsx)(i.h5,{id:"message-type",children:"Message Type"}),"\n",(0,s.jsxs)(i.p,{children:["Reference ",(0,s.jsx)(i.a,{href:"https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbermessagetype-number",children:"QLab Docs"})]}),"\n",(0,s.jsx)(i.h5,{id:"osc-cue-number",children:"OSC Cue Number"}),"\n",(0,s.jsx)(i.p,{children:"Only if using QLab Message Type"}),"\n",(0,s.jsx)(i.h5,{id:"command",children:"Command"}),"\n",(0,s.jsxs)(i.p,{children:["For QLab Messages, review the ",(0,s.jsx)(i.a,{href:"https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numberqlabcommand-number",children:"QLab Docs"})]}),"\n",(0,s.jsx)(i.p,{children:"For OSC Messages, you may now include a raw string in the column."})]})}function h(e={}){const{wrapper:i}={...(0,t.R)(),...e.components};return i?(0,s.jsx)(i,{...e,children:(0,s.jsx)(c,{...e})}):c(e)}},8453:(e,i,n)=>{n.d(i,{R:()=>r,x:()=>a});var s=n(6540);const t={},l=s.createContext(t);function r(e){const i=s.useContext(l);return s.useMemo((function(){return"function"==typeof e?e(i):{...i,...e}}),[i,e])}function a(e){let i;return i=e.disableParentContext?"function"==typeof e.components?e.components(t):e.components||t:r(e.components),s.createElement(l.Provider,{value:i},e.children)}}}]);