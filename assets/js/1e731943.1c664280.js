"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[228],{3905:function(e,t,n){n.d(t,{Zo:function(){return l},kt:function(){return d}});var r=n(7294);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function u(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},i=Object.keys(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var c=r.createContext({}),s=function(e){var t=r.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):a(a({},t),e)),n},l=function(e){var t=s(e.components);return r.createElement(c.Provider,{value:t},e.children)},f={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},p=r.forwardRef((function(e,t){var n=e.components,o=e.mdxType,i=e.originalType,c=e.parentName,l=u(e,["components","mdxType","originalType","parentName"]),p=s(n),d=o,v=p["".concat(c,".").concat(d)]||p[d]||f[d]||i;return n?r.createElement(v,a(a({ref:t},l),{},{components:n})):r.createElement(v,a({ref:t},l))}));function d(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var i=n.length,a=new Array(i);a[0]=p;var u={};for(var c in t)hasOwnProperty.call(t,c)&&(u[c]=t[c]);u.originalType=e,u.mdxType="string"==typeof e?e:o,a[1]=u;for(var s=2;s<i;s++)a[s]=n[s];return r.createElement.apply(null,a)}return r.createElement.apply(null,n)}p.displayName="MDXCreateElement"},9960:function(e,t,n){n.d(t,{Z:function(){return d}});var r=n(3366),o=n(7294),i=n(3727),a=n(2263),u=n(3919),c=n(412),s=(0,o.createContext)({collectLink:function(){}}),l=n(4996),f=n(8780),p=["isNavLink","to","href","activeClassName","isActive","data-noBrokenLinkCheck","autoAddBaseUrl"];var d=function(e){var t,n,d=e.isNavLink,v=e.to,b=e.href,m=e.activeClassName,y=e.isActive,h=e["data-noBrokenLinkCheck"],g=e.autoAddBaseUrl,O=void 0===g||g,w=(0,r.Z)(e,p),k=(0,a.Z)().siteConfig,_=k.trailingSlash,j=k.baseUrl,C=(0,l.C)().withBaseUrl,P=(0,o.useContext)(s),E=v||b,x=(0,u.Z)(E),T=null==E?void 0:E.replace("pathname://",""),U=void 0!==T?(n=T,O&&function(e){return e.startsWith("/")}(n)?C(n):n):void 0;U&&x&&(U=(0,f.applyTrailingSlash)(U,{trailingSlash:_,baseUrl:j}));var Z=(0,o.useRef)(!1),D=d?i.OL:i.rU,R=c.default.canUseIntersectionObserver,S=(0,o.useRef)();(0,o.useEffect)((function(){return!R&&x&&null!=U&&window.docusaurus.prefetch(U),function(){R&&S.current&&S.current.disconnect()}}),[S,U,R,x]);var N=null!==(t=null==U?void 0:U.startsWith("#"))&&void 0!==t&&t,B=!U||!x||N;return U&&x&&!N&&!h&&P.collectLink(U),B?o.createElement("a",Object.assign({href:U},E&&!x&&{target:"_blank",rel:"noopener noreferrer"},w)):o.createElement(D,Object.assign({},w,{onMouseEnter:function(){Z.current||null==U||(window.docusaurus.preload(U),Z.current=!0)},innerRef:function(e){var t,n;R&&e&&x&&(t=e,n=function(){null!=U&&window.docusaurus.prefetch(U)},S.current=new window.IntersectionObserver((function(e){e.forEach((function(e){t===e.target&&(e.isIntersecting||e.intersectionRatio>0)&&(S.current.unobserve(t),S.current.disconnect(),n())}))})),S.current.observe(t))},to:U||""},d&&{isActive:y,activeClassName:m}))}},3919:function(e,t,n){function r(e){return!0===/^(\w*:|\/\/)/.test(e)}function o(e){return void 0!==e&&!r(e)}n.d(t,{b:function(){return r},Z:function(){return o}})},4996:function(e,t,n){n.d(t,{C:function(){return i},Z:function(){return a}});var r=n(2263),o=n(3919);function i(){var e=(0,r.Z)().siteConfig,t=(e=void 0===e?{}:e).baseUrl,n=void 0===t?"/":t,i=e.url;return{withBaseUrl:function(e,t){return function(e,t,n,r){var i=void 0===r?{}:r,a=i.forcePrependBaseUrl,u=void 0!==a&&a,c=i.absolute,s=void 0!==c&&c;if(!n)return n;if(n.startsWith("#"))return n;if((0,o.b)(n))return n;if(u)return t+n;var l=n.startsWith(t)?n:t+n.replace(/^\//,"");return s?e+l:l}(i,n,e,t)}}}function a(e,t){return void 0===t&&(t={}),(0,i().withBaseUrl)(e,t)}},8802:function(e,t){Object.defineProperty(t,"__esModule",{value:!0}),t.default=function(e,t){var n=t.trailingSlash,r=t.baseUrl;if(e.startsWith("#"))return e;if(void 0===n)return e;var o,i=e.split(/[#?]/)[0],a="/"===i||i===r?i:(o=i,n?function(e){return e.endsWith("/")?e:e+"/"}(o):function(e){return e.endsWith("/")?e.slice(0,-1):e}(o));return e.replace(i,a)}},8780:function(e,t,n){var r=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:!0}),t.uniq=t.applyTrailingSlash=void 0;var o=n(8802);Object.defineProperty(t,"applyTrailingSlash",{enumerable:!0,get:function(){return r(o).default}});var i=n(9964);Object.defineProperty(t,"uniq",{enumerable:!0,get:function(){return r(i).default}})},9964:function(e,t){Object.defineProperty(t,"__esModule",{value:!0}),t.default=function(e){return Array.from(new Set(e))}},973:function(e,t,n){n.r(t),n.d(t,{frontMatter:function(){return s},contentTitle:function(){return l},metadata:function(){return f},assets:function(){return p},toc:function(){return d},default:function(){return b}});var r=n(7462),o=n(3366),i=(n(7294),n(3905)),a=n(9960),u=(n(4996),n(1207)),c=["components"],s={slug:"0/0/0",title:"First Release",tags:["v0.0.0"]},l=void 0,f={permalink:"/csv_to_qlab/releases/0/0/0",editUrl:"https://github.com/fross123/csv_to_qlab/edit/main/website/releases/releases/2020-11-12-First-Release.mdx",source:"@site/releases/2020-11-12-First-Release.mdx",title:"First Release",description:"Initial Release. Download zip to demo.",date:"2020-11-12T00:00:00.000Z",formattedDate:"November 12, 2020",tags:[{label:"v0.0.0",permalink:"/csv_to_qlab/releases/tags/v-0-0-0"}],truncated:!1,authors:[],prevItem:{title:"Version 2021.1.0",permalink:"/csv_to_qlab/releases/2021/1/0"}},p={authorsImageUrls:[]},d=[],v={toc:d};function b(e){var t=e.components,n=(0,o.Z)(e,c);return(0,i.kt)("wrapper",(0,r.Z)({},v,n,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("p",null,"Initial Release. Download zip to demo."),(0,i.kt)("p",null,"Currently only available for MacOS."),(0,i.kt)("div",{className:u.Z.buttons},(0,i.kt)(a.Z,{className:"button button--primary button--lg",to:"https://github.com/fross123/csv_to_qlab/releases/download/v0.0.0/csv_to_qlab.zip",mdxType:"Link"},"Download Release v0.0.0")))}b.isMDXComponent=!0},1207:function(e,t){t.Z={heroBanner:"heroBanner_etFc",buttons:"buttons_+YzY"}}}]);