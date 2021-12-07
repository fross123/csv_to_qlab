"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[775],{3905:function(e,t,r){r.d(t,{Zo:function(){return s},kt:function(){return d}});var n=r(7294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function a(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?a(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function u(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},a=Object.keys(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var l=n.createContext({}),c=function(e){var t=n.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},s=function(e){var t=c(e.components);return n.createElement(l.Provider,{value:t},e.children)},f={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},p=n.forwardRef((function(e,t){var r=e.components,o=e.mdxType,a=e.originalType,l=e.parentName,s=u(e,["components","mdxType","originalType","parentName"]),p=c(r),d=o,v=p["".concat(l,".").concat(d)]||p[d]||f[d]||a;return r?n.createElement(v,i(i({ref:t},s),{},{components:r})):n.createElement(v,i({ref:t},s))}));function d(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var a=r.length,i=new Array(a);i[0]=p;var u={};for(var l in t)hasOwnProperty.call(t,l)&&(u[l]=t[l]);u.originalType=e,u.mdxType="string"==typeof e?e:o,i[1]=u;for(var c=2;c<a;c++)i[c]=r[c];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}p.displayName="MDXCreateElement"},9960:function(e,t,r){r.d(t,{Z:function(){return d}});var n=r(3366),o=r(7294),a=r(3727),i=r(2263),u=r(3919),l=r(412),c=(0,o.createContext)({collectLink:function(){}}),s=r(4996),f=r(8780),p=["isNavLink","to","href","activeClassName","isActive","data-noBrokenLinkCheck","autoAddBaseUrl"];var d=function(e){var t,r,d=e.isNavLink,v=e.to,m=e.href,b=e.activeClassName,h=e.isActive,y=e["data-noBrokenLinkCheck"],g=e.autoAddBaseUrl,w=void 0===g||g,O=(0,n.Z)(e,p),k=(0,i.Z)().siteConfig,_=k.trailingSlash,j=k.baseUrl,C=(0,s.C)().withBaseUrl,x=(0,o.useContext)(c),P=v||m,N=(0,u.Z)(P),E=null==P?void 0:P.replace("pathname://",""),T=void 0!==E?(r=E,w&&function(e){return e.startsWith("/")}(r)?C(r):r):void 0;T&&N&&(T=(0,f.applyTrailingSlash)(T,{trailingSlash:_,baseUrl:j}));var U=(0,o.useRef)(!1),S=d?a.OL:a.rU,Z=l.default.canUseIntersectionObserver,B=(0,o.useRef)();(0,o.useEffect)((function(){return!Z&&N&&null!=T&&window.docusaurus.prefetch(T),function(){Z&&B.current&&B.current.disconnect()}}),[B,T,Z,N]);var L=null!==(t=null==T?void 0:T.startsWith("#"))&&void 0!==t&&t,D=!T||!N||L;return T&&N&&!L&&!y&&x.collectLink(T),D?o.createElement("a",Object.assign({href:T},P&&!N&&{target:"_blank",rel:"noopener noreferrer"},O)):o.createElement(S,Object.assign({},O,{onMouseEnter:function(){U.current||null==T||(window.docusaurus.preload(T),U.current=!0)},innerRef:function(e){var t,r;Z&&e&&N&&(t=e,r=function(){null!=T&&window.docusaurus.prefetch(T)},B.current=new window.IntersectionObserver((function(e){e.forEach((function(e){t===e.target&&(e.isIntersecting||e.intersectionRatio>0)&&(B.current.unobserve(t),B.current.disconnect(),r())}))})),B.current.observe(t))},to:T||""},d&&{isActive:h,activeClassName:b}))}},3919:function(e,t,r){function n(e){return!0===/^(\w*:|\/\/)/.test(e)}function o(e){return void 0!==e&&!n(e)}r.d(t,{b:function(){return n},Z:function(){return o}})},4996:function(e,t,r){r.d(t,{C:function(){return a},Z:function(){return i}});var n=r(2263),o=r(3919);function a(){var e=(0,n.Z)().siteConfig,t=(e=void 0===e?{}:e).baseUrl,r=void 0===t?"/":t,a=e.url;return{withBaseUrl:function(e,t){return function(e,t,r,n){var a=void 0===n?{}:n,i=a.forcePrependBaseUrl,u=void 0!==i&&i,l=a.absolute,c=void 0!==l&&l;if(!r)return r;if(r.startsWith("#"))return r;if((0,o.b)(r))return r;if(u)return t+r;var s=r.startsWith(t)?r:t+r.replace(/^\//,"");return c?e+s:s}(a,r,e,t)}}}function i(e,t){return void 0===t&&(t={}),(0,a().withBaseUrl)(e,t)}},8802:function(e,t){Object.defineProperty(t,"__esModule",{value:!0}),t.default=function(e,t){var r=t.trailingSlash,n=t.baseUrl;if(e.startsWith("#"))return e;if(void 0===r)return e;var o,a=e.split(/[#?]/)[0],i="/"===a||a===n?a:(o=a,r?function(e){return e.endsWith("/")?e:e+"/"}(o):function(e){return e.endsWith("/")?e.slice(0,-1):e}(o));return e.replace(a,i)}},8780:function(e,t,r){var n=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:!0}),t.uniq=t.applyTrailingSlash=void 0;var o=r(8802);Object.defineProperty(t,"applyTrailingSlash",{enumerable:!0,get:function(){return n(o).default}});var a=r(9964);Object.defineProperty(t,"uniq",{enumerable:!0,get:function(){return n(a).default}})},9964:function(e,t){Object.defineProperty(t,"__esModule",{value:!0}),t.default=function(e){return Array.from(new Set(e))}},2601:function(e,t,r){r.r(t),r.d(t,{frontMatter:function(){return c},contentTitle:function(){return s},metadata:function(){return f},assets:function(){return p},toc:function(){return d},default:function(){return m}});var n=r(7462),o=r(3366),a=(r(7294),r(3905)),i=r(9960),u=(r(4996),r(1207)),l=["components"],c={slug:"2021/1/15",title:"Version 2021.1.15",tags:["2021","1.15"]},s=void 0,f={permalink:"/csv_to_qlab/releases/2021/1/15",editUrl:"https://github.com/fross123/csv_to_qlab/edit/main/website/releases/releases/2021-11-24-v2021.1.15.mdx",source:"@site/releases/2021-11-24-v2021.1.15.mdx",title:"Version 2021.1.15",description:"* Various Bug Fixes",date:"2021-11-24T00:00:00.000Z",formattedDate:"November 24, 2021",tags:[{label:"2021",permalink:"/csv_to_qlab/releases/tags/2021"},{label:"1.15",permalink:"/csv_to_qlab/releases/tags/1-15"}],truncated:!1,authors:[],prevItem:{title:"Version 2021.1.2",permalink:"/csv_to_qlab/releases/2021/1/2"},nextItem:{title:"Version 2021.1.1",permalink:"/csv_to_qlab/releases/2021/1/1"}},p={authorsImageUrls:[]},d=[],v={toc:d};function m(e){var t=e.components,r=(0,o.Z)(e,l);return(0,a.kt)("wrapper",(0,n.Z)({},v,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("p",{parentName:"li"},"Various Bug Fixes")),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("p",{parentName:"li"},"Update to OSC handling to allow raw string for standard OSC messages")),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("p",{parentName:"li"},'Update to allow "Number Prefix" column to prefix the number of cues.\nEx: If you have a column already with the number of the cue, you may now add another column with "LX", and the numbers of your cues will start with LX, but will still trigger the number selected. The MIDI or OSC command will not include this prefix.'))),(0,a.kt)("div",{className:u.Z.buttons},(0,a.kt)(i.Z,{className:"button button--primary button--lg",to:"https://github.com/fross123/csv_to_qlab/releases/download/v2021.1.15/CSV-To-QLab.dmg",mdxType:"Link"},"Download Release v2021.1.15")))}m.isMDXComponent=!0},1207:function(e,t){t.Z={heroBanner:"heroBanner_etFc",buttons:"buttons_+YzY"}}}]);