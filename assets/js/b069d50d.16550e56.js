"use strict";(self.webpackChunkcsv_to_qlab=self.webpackChunkcsv_to_qlab||[]).push([[8600],{3905:(e,t,a)=>{a.d(t,{Zo:()=>p,kt:()=>b});var n=a(7294);function o(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function r(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?r(Object(a),!0).forEach((function(t){o(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):r(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,o=function(e,t){if(null==e)return{};var a,n,o={},r=Object.keys(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||(o[a]=e[a]);return o}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(o[a]=e[a])}return o}var l=n.createContext({}),c=function(e){var t=n.useContext(l),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},p=function(e){var t=c(e.components);return n.createElement(l.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},d=n.forwardRef((function(e,t){var a=e.components,o=e.mdxType,r=e.originalType,l=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),d=c(a),b=o,m=d["".concat(l,".").concat(b)]||d[b]||u[b]||r;return a?n.createElement(m,i(i({ref:t},p),{},{components:a})):n.createElement(m,i({ref:t},p))}));function b(e,t){var a=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var r=a.length,i=new Array(r);i[0]=d;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:o,i[1]=s;for(var c=2;c<r;c++)i[c]=a[c];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}d.displayName="MDXCreateElement"},3681:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>p,contentTitle:()=>l,default:()=>b,frontMatter:()=>s,metadata:()=>c,toc:()=>u});var n=a(7462),o=a(3366),r=(a(7294),a(3905)),i=["components"],s={sidebar_position:3},l="Send a File to QLab",c={unversionedId:"tutorial-basics/send-to-qlab",id:"tutorial-basics/send-to-qlab",title:"Send a File to QLab",description:"Follow these steps to send your newly created CSV file over to QLab.",source:"@site/docs/tutorial-basics/send-to-qlab.md",sourceDirName:"tutorial-basics",slug:"/tutorial-basics/send-to-qlab",permalink:"/docs/tutorial-basics/send-to-qlab",draft:!1,editUrl:"https://github.com/fross123/csv_to_qlab/edit/main/website/docs/tutorial-basics/send-to-qlab.md",tags:[],version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"tutorialSidebar",previous:{title:"Prepare a CSV File",permalink:"/docs/tutorial-basics/prepare-csv-file"},next:{title:"Install from Source Code",permalink:"/docs/advanced/install-from-source"}},p={},u=[{value:"Open QLab",id:"open-qlab",level:2},{value:"If you are using QLab 5 and have an OSC Passcode.",id:"if-you-are-using-qlab-5-and-have-an-osc-passcode",level:2},{value:"Find the IP address",id:"find-the-ip-address",level:2},{value:"Fill out the form",id:"fill-out-the-form",level:2},{value:"Submit the Form",id:"submit-the-form",level:2},{value:"Make the Magic Happen!",id:"make-the-magic-happen",level:2}],d={toc:u};function b(e){var t=e.components,s=(0,o.Z)(e,i);return(0,r.kt)("wrapper",(0,n.Z)({},d,s,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"send-a-file-to-qlab"},"Send a File to QLab"),(0,r.kt)("p",null,"Follow these steps to send your newly created CSV file over to QLab."),(0,r.kt)("h2",{id:"open-qlab"},"Open QLab"),(0,r.kt)("p",null,"Open an empty QLab workspace."),(0,r.kt)("admonition",{type:"note"},(0,r.kt)("p",{parentName:"admonition"},"CSV to QLab will operate with both QLab 3 and QLab 4, however not all functions are available on QLab 3.")),(0,r.kt)("h2",{id:"if-you-are-using-qlab-5-and-have-an-osc-passcode"},"If you are using QLab 5 and have an OSC Passcode."),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Select the checkbox for QLab5."),(0,r.kt)("li",{parentName:"ul"},"Enter passcode found in QLab settings.")),(0,r.kt)("admonition",{type:"tip"},(0,r.kt)("p",{parentName:"admonition"},'Make sure that the passcode has full access to the workspace.\nNote that it is also possible to bypass this step and allow access with the "no passcode" option.')),(0,r.kt)("h2",{id:"find-the-ip-address"},"Find the IP address"),(0,r.kt)("p",null,"You will need the local IP address of the machine running QLab."),(0,r.kt)("admonition",{type:"tip"},(0,r.kt)("p",{parentName:"admonition"},"You can run CSV to QLab on the same machine.")),(0,r.kt)("p",null,"On QLab 4 you can find this in Settings -> OSC Controls."),(0,r.kt)("h2",{id:"fill-out-the-form"},"Fill out the form"),(0,r.kt)("p",null,"Enter the IP address and select your file in CSV to QLab keeping the QLab workspace open."),(0,r.kt)("h2",{id:"submit-the-form"},"Submit the Form"),(0,r.kt)("admonition",{type:"tip"},(0,r.kt)("p",{parentName:"admonition"},"If you see an error, please let us know, or submit an ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/fross123/csv_to_qlab/issues/new/choose"},"issue"),". We are here to help.")),(0,r.kt)("h2",{id:"make-the-magic-happen"},"Make the Magic Happen!"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"Success Page",src:a(9990).Z,width:"750",height:"600"})))}b.isMDXComponent=!0},9990:(e,t,a)=>{a.d(t,{Z:()=>n});const n=a.p+"assets/images/funny-success-quote-1-picture-quote-1-7738aed66b537905de19c4c1690be819.jpg"}}]);